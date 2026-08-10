"""生成并审计《星露谷物语》PC v1.6.15 技能、职业与精通全集。

覆盖五项技能、统一等级经验、每级解锁、30 个职业、全部经验来源、
技能直接属性效果、精通点数与 15 条精通奖励。来源固定到 Skills、五个
技能页和 Mastery Cave 的 revision；只提取技能相关章节，避免把食物、
采集物、武器等其他数据域复制为第二真源。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "技能属性数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-skill-cache"
EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"


@dataclass(frozen=True)
class SourceSpec:
    english: str
    chinese: str
    revision: int
    sections: frozenset[str]


SKILL_NAMES = ("Farming", "Mining", "Foraging", "Fishing", "Combat")
PROFESSIONS = {
    "Farming": ("Rancher", "Tiller", "Coopmaster", "Shepherd", "Artisan", "Agriculturist"),
    "Mining": ("Miner", "Geologist", "Blacksmith", "Prospector", "Excavator", "Gemologist"),
    "Foraging": ("Forester", "Gatherer", "Lumberjack", "Tapper", "Botanist", "Tracker"),
    "Fishing": ("Fisher", "Trapper", "Angler", "Pirate", "Mariner", "Luremaster"),
    "Combat": ("Fighter", "Scout", "Brute", "Defender", "Acrobat", "Desperado"),
}
LEVEL_TOTALS = (100, 380, 770, 1300, 2150, 3300, 4800, 6900, 10000, 15000)

SOURCES = (
    SourceSpec(
        "Skills",
        "技能总页",
        192909,
        frozenset(
            {
                "Proficiency",
                "Affected Tools",
                "Unaffected Tools",
                "Farming",
                "Mining",
                "Foraging",
                "Fishing",
                "Combat",
                "Changing Professions",
                "Skill-Based Title",
                "Mastery",
            }
        ),
    ),
    SourceSpec(
        "Farming",
        "耕种",
        191914,
        frozenset(
            {
                "Farming Skill",
                "Effect of Coopmaster and Shepherd on Animal Product Quality Frequency",
                "Complete Formula",
                "Crop Quality Frequency",
                "Normal soil",
                "Soil with Basic Fertilizer",
                "Soil with Quality Fertilizer",
                "Soil with Deluxe Fertilizer",
                "Experience Points",
            }
        ),
    ),
    SourceSpec("Mining", "采矿", 192860, frozenset({"Mining Skill", "Experience Points"})),
    SourceSpec(
        "Foraging",
        "采集",
        193727,
        frozenset(
            {"Quality", "Quality Ratios", "Foraging Skill", "Tracker Profession", "Experience Points"}
        ),
    ),
    SourceSpec(
        "Fishing",
        "钓鱼",
        193904,
        frozenset(
            {
                "Specific Mechanics",
                "Types of Fish",
                "Bar Size",
                "Casting Distance",
                "Fish Bite Time",
                "Distance from Land",
                "Perfect Catches",
                "Fish Size & Quality",
                "Bubbles",
                "Fish Frenzies",
                "Energy",
                "Angled Casts",
                "Time",
                "Fishing Skill",
                "Experience Points",
            }
        ),
    ),
    SourceSpec("Combat", "战斗", 192831, frozenset({"Combat Skill", "Experience Points", "Substats"})),
    SourceSpec("Mastery Cave", "精通山洞", 191046, frozenset({"Masteries", "Completion"})),
)


@dataclass(frozen=True)
class SourceTable:
    rows: tuple[tuple[str, ...], ...]

    @property
    def width(self) -> int:
        return max((len(row) for row in self.rows), default=0)


@dataclass(frozen=True)
class SourceRecord:
    spec: SourceSpec
    tables: tuple[tuple[str, SourceTable], ...]
    facts: tuple[tuple[str, str], ...]


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip(" /\u00a0")


def heading_text(heading: Tag | None) -> str:
    if heading is None:
        return "基本信息"
    headline = heading.select_one(".mw-headline")
    text = (headline if isinstance(headline, Tag) else heading).get_text(" ", strip=True)
    return clean_text(re.sub(r"\[\s*(?:edit|编辑)\s*\]", "", text, flags=re.IGNORECASE))


def image_label(image: Tag) -> str:
    alt = clean_text(image.get("alt") or "")
    return re.sub(r"\.(?:png|gif|jpg|jpeg)$", "", alt, flags=re.IGNORECASE)


def semantic_cell_text(cell: Tag) -> str:
    clone = BeautifulSoup(str(cell), "html.parser").find(["th", "td"])
    if clone is None:
        return ""
    for unwanted in clone.find_all(["sup", "style", "script", "noscript"]):
        unwanted.decompose()
    for line_break in clone.find_all("br"):
        line_break.replace_with(NavigableString(" / "))
    for image in clone.find_all("img"):
        label = image_label(image)
        image.replace_with(NavigableString(f" {label} " if label else " "))
    return clean_text(clone.get_text(" ", strip=True))


def direct_rows(table: Tag) -> list[Tag]:
    body = table.find("tbody", recursive=False)
    parent = body if body is not None else table
    return parent.find_all("tr", recursive=False)


def table_to_grid(table: Tag) -> SourceTable:
    rows = direct_rows(table)
    if not rows:
        raise AssertionError("源表没有直接数据行")
    occupied: dict[tuple[int, int], str] = {}
    width = 0
    for row_index, row in enumerate(rows):
        column = 0
        for cell in row.find_all(["th", "td"], recursive=False):
            while (row_index, column) in occupied:
                column += 1
            value = semantic_cell_text(cell)
            rowspan = int(cell.get("rowspan") or 1)
            colspan = int(cell.get("colspan") or 1)
            for row_offset in range(rowspan):
                for col_offset in range(colspan):
                    occupied[(row_index + row_offset, column + col_offset)] = value
            column += colspan
        width = max(width, column)
    if not occupied:
        raise AssertionError("源表为空")
    height = max(row for row, _ in occupied) + 1
    width = max(width, max(column for _, column in occupied) + 1)
    return SourceTable(
        tuple(
            tuple(occupied.get((row, column), "") for column in range(width))
            for row in range(height)
        )
    )


def request_html(title: str, revision_id: int) -> str:
    safe_title = re.sub(r"[^a-zA-Z0-9_-]+", "-", title).strip("-") or "page"
    cache_file = CACHE / f"en-{revision_id}-{safe_title}.html"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")
    command = [
        "curl.exe" if sys.platform == "win32" else "curl",
        "--location",
        "--silent",
        "--show-error",
        "--fail-with-body",
        "--retry",
        "3",
        "--retry-delay",
        "1",
        "--max-time",
        "30",
        "--user-agent",
        "GameDocsAudit/2.9 (Longyuyeee/GameLibrary)",
        "--get",
        EN_API,
        "--data-urlencode",
        "action=parse",
        "--data-urlencode",
        "prop=text",
        "--data-urlencode",
        "format=json",
        "--data-urlencode",
        f"oldid={revision_id}",
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True, encoding="utf-8")
    html = json.loads(result.stdout)["parse"]["text"]["*"]
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(html, encoding="utf-8")
    return html


def is_navigation_table(table: Tag) -> bool:
    for node in (table, *table.parents):
        if isinstance(node, Tag):
            classes = set(node.get("class") or [])
            if any(value.startswith("navbox") for value in classes):
                return True
    return False


def relevant_tables(html: str, spec: SourceSpec) -> tuple[tuple[str, SourceTable], ...]:
    soup = BeautifulSoup(html, "html.parser")
    selected: list[tuple[str, SourceTable]] = []
    for table in soup.find_all("table"):
        if table.find("table") is not None or is_navigation_table(table):
            continue
        grid = table_to_grid(table)
        label = heading_text(table.find_previous(["h2", "h3", "h4"]))
        common_experience = (
            spec.english == "Skills"
            and grid.rows
            and tuple(cell.lower() for cell in grid.rows[0][:3])
            == ("lvl", "experience", "total experience")
        )
        if label not in spec.sections and not common_experience:
            continue
        if common_experience:
            label = "Level Experience"
        selected.append((label, grid))
    if not selected:
        raise AssertionError(f"固定页没有技能相关数据表：{spec.english}")
    return tuple(selected)


def relevant_facts(html: str, spec: SourceSpec) -> tuple[tuple[str, str], ...]:
    soup = BeautifulSoup(html, "html.parser")
    facts: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for heading in soup.find_all(["h2", "h3", "h4"]):
        section = heading_text(heading)
        if section not in spec.sections:
            continue
        sibling = heading.find_next_sibling()
        while sibling is not None and sibling.name not in {"h2", "h3", "h4"}:
            if sibling.name in {"p", "ul", "ol", "dl", "pre"}:
                value = clean_text(sibling.get_text(" / ", strip=True))
                key = (section, value)
                if value and key not in seen:
                    seen.add(key)
                    facts.append(key)
            sibling = sibling.find_next_sibling()
    return tuple(facts)


def source_record(spec: SourceSpec) -> SourceRecord:
    html = request_html(spec.english, spec.revision)
    return SourceRecord(spec, relevant_tables(html, spec), relevant_facts(html, spec))


def source_records() -> tuple[SourceRecord, ...]:
    with ThreadPoolExecutor(max_workers=7) as executor:
        return tuple(executor.map(source_record, SOURCES))


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def markdown_table(rows: list[list[str]]) -> str:
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    output = [
        "| " + " | ".join(markdown_escape(cell) for cell in normalized[0]) + " |",
        "|" + "|".join("---" for _ in range(width)) + "|",
    ]
    output.extend(
        "| " + " | ".join(markdown_escape(cell) for cell in row) + " |"
        for row in normalized[1:]
    )
    return "\n".join(output)


def source_table_markdown(table: SourceTable) -> str:
    rows = [list(row) for row in table.rows]
    if len(rows) == 1:
        rows.append(["—"] * table.width)
    return markdown_table(rows)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def fixed_url(title: str, revision: int) -> str:
    encoded = quote(title.replace(" ", "_"), safe=":_")
    return f"https://stardewvalleywiki.com/mediawiki/index.php?title={encoded}&oldid={revision}"


def body_rows(table: SourceTable) -> int:
    return max(0, len(table.rows) - 1)


def validate(records: tuple[SourceRecord, ...]) -> dict[str, int]:
    by_title = {record.spec.english: record for record in records}
    if set(by_title) != {spec.english for spec in SOURCES}:
        raise AssertionError("技能固定页集合未闭合")

    skills_record = by_title["Skills"]
    experience_rows: list[tuple[str, ...]] = []
    skill_tables: dict[str, SourceTable] = {}
    mastery_tables: list[SourceTable] = []
    for label, table in skills_record.tables:
        header = tuple(cell.lower() for cell in table.rows[0][:3]) if table.rows else ()
        if header == ("lvl", "experience", "total experience"):
            experience_rows.extend(table.rows[1:])
        if label in SKILL_NAMES:
            skill_tables[label] = table
        if label == "Mastery":
            mastery_tables.append(table)
    if len(experience_rows) != 10:
        raise AssertionError(f"统一等级经验行漂移：{len(experience_rows)}")
    levels = tuple(int(row[0].replace("+", "")) for row in experience_rows)
    totals = tuple(int(row[2].replace(",", "")) for row in experience_rows)
    if levels != tuple(range(1, 11)) or totals != LEVEL_TOTALS:
        raise AssertionError(f"统一等级经验值漂移：levels={levels}, totals={totals}")
    if set(skill_tables) != set(SKILL_NAMES):
        raise AssertionError(f"技能升级表集合漂移：{sorted(skill_tables)}")

    profession_count = 0
    for skill, table in skill_tables.items():
        text = " ".join(cell for row in table.rows for cell in row)
        missing_levels = [level for level in range(1, 11) if f"Level {level}" not in text]
        missing_professions = [name for name in PROFESSIONS[skill] if name not in text]
        if missing_levels or missing_professions:
            raise AssertionError(
                f"{skill} 升级表未闭合：levels={missing_levels}, professions={missing_professions}"
            )
        profession_count += len(PROFESSIONS[skill])
    if profession_count != 30:
        raise AssertionError(f"职业数量漂移：{profession_count}")

    mastery_cost = next(
        (table for table in mastery_tables if table.rows[0][0] == "Level"), None
    )
    mastery_rewards = next(
        (table for table in mastery_tables if table.rows[0][0] == "Name"), None
    )
    if mastery_cost is None or body_rows(mastery_cost) != 5:
        raise AssertionError("精通点数表不是 5/5")
    if mastery_rewards is None or body_rows(mastery_rewards) != 15:
        raise AssertionError("精通奖励表不是 15/15")
    if mastery_cost.rows[-1][2].replace(",", "") != "100000":
        raise AssertionError("精通累计点数终值不是 100,000")

    structured = 0
    farming_benchmark = 0
    farming_sources = 0
    for label, table in by_title["Farming"].tables:
        if label != "Experience Points":
            continue
        if table.rows[0][0] in {"Spring", "Summer", "Fall", "Winter"}:
            farming_sources += max(0, len(table.rows) - 2)
        elif table.rows[0][0] == "Lvl":
            farming_benchmark += body_rows(table)
    if farming_sources != 52 or farming_benchmark != 10:
        raise AssertionError(
            f"耕种经验表漂移：sources={farming_sources}, benchmark={farming_benchmark}"
        )
    structured += farming_sources + farming_benchmark

    expected_rows = {"Mining": 28, "Fishing": 10, "Combat": 47}
    for title, expected in expected_rows.items():
        actual = sum(
            body_rows(table)
            for label, table in by_title[title].tables
            if label == "Experience Points"
        )
        if actual != expected:
            raise AssertionError(f"{title} 经验结构行漂移：{actual} != {expected}")
        structured += actual
    if structured != 147:
        raise AssertionError(f"结构化经验行总数漂移：{structured}")

    required_facts = {
        "Farming": ("Farming experience", "Petting", "milking"),
        "Mining": ("Mining Skill", "experience"),
        "Foraging": ("14 XP", "250 XP", "do NOT grant"),
        "Fishing": ("XP =", "2.2", "2.4", "Legendary fish"),
        "Combat": (
            "250 Combat XP",
            "affects how much damage the player does",
            "affects how much damage the player takes",
        ),
        "Mastery Cave": ("50% rate", "100,000 Mastery points", "all 5 masteries"),
    }
    for title, phrases in required_facts.items():
        text = " ".join(value for _, value in by_title[title].facts)
        missing = [phrase for phrase in phrases if phrase not in text]
        if missing:
            raise AssertionError(f"{title} 技能事实缺失：{missing}")

    return {
        "skills": 5,
        "levels": 10,
        "unlocks": 50,
        "professions": 30,
        "mastery_levels": 5,
        "mastery_rewards": 15,
        "structured_xp": structured,
        "tables": sum(len(record.tables) for record in records),
        "rows": sum(body_rows(table) for record in records for _, table in record.tables),
        "facts": sum(len(record.facts) for record in records),
    }


def render_document() -> str:
    records = source_records()
    counts = validate(records)
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 技能属性数据总览",
        "",
        "# 技能、经验、职业与精通数据总览（Complete Skills, Professions & Mastery Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        "> 数据来源：Skills、Farming、Mining、Foraging、Fishing、Combat、Mastery Cave 共 7 个固定 revision（逐页见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷技能数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 技能 |",
        "| 数据范围 | 耕种、采矿、采集、钓鱼、战斗五项技能；统一经验阈值；1–10 级全部解锁；职业树；技能直接属性效果；全部经验来源、公式与排除项；精通点数和奖励 |",
        "| 唯一归属 | 本文是技能经验、升级解锁、职业与精通的唯一数据源；通用生命/精力、武器、护甲、增益和伤害计算留在[角色属性战斗数据总览](./角色属性战斗数据总览.md)，怪物击杀对象与掉落见[怪物数据总览](./怪物数据总览.md) |",
        f"| 技能名册 | 预计 5 / 实际 {counts['skills']} |",
        f"| 等级经验 | 预计 10 / 实际 {counts['levels']}；Lv10 累计 15,000 XP |",
        f"| 逐级解锁 | 预计 5×10=50 / 实际 {counts['unlocks']}；每个 Level 1–10 均存在 |",
        f"| 职业 | 预计 5×6=30 / 实际 {counts['professions']}；Lv5 两分支与各自 Lv10 两分支闭合 |",
        f"| 精通 | 点数等级预计 5 / 实际 {counts['mastery_levels']}；奖励行预计 15 / 实际 {counts['mastery_rewards']}；累计 100,000 点 |",
        f"| 经验来源 | 结构化来源/基准行预计 147 / 实际 {counts['structured_xp']}；采集、钓鱼、耕种等非表格公式、倍率、排除项完整保留 |",
        "| 数量差异 | 0 |",
        f"| 字段完整率 | 7/7 个固定页；技能相关数据表 {counts['tables']} 张、表体记录 {counts['rows']} 行、非历史事实块 {counts['facts']} 个全部保留 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 边界与计数说明",
        "",
        "- `逐级解锁 50`按五张技能升级表的 Level 1–10 槽位计数；每个槽位保留配方、商店解锁、能力或职业选择的全部源字段。",
        "- `职业 30`按每项技能 Lv5 两个职业与四个 Lv10 子职业计数，不把职业效果中的多个句子误算成新职业。",
        "- `结构化经验行 147`由耕种季节来源 52、耕种等级基准 10、采矿来源 28、钓鱼等级基准 10、战斗怪物经验 47 构成；采集与钓鱼的公式型来源保留为完整事实块，不能因没有表格而省略。",
        "- Farming 页的作物/动物品质公式只作为技能与职业的直接效果保留；完整作物和动物条目分别以对应数据文档为唯一名册。",
        "",
        "## 快速索引",
        "",
    ]
    index_rows = [["#", "来源页", "固定 revision", "数据表/表体行/事实块", "跳转"]]
    for index, record in enumerate(records, start=1):
        rows = sum(body_rows(table) for _, table in record.tables)
        spec = record.spec
        index_rows.append(
            [
                str(index),
                f"{spec.chinese}（{spec.english}）",
                str(spec.revision),
                f"{len(record.tables)} / {rows} / {len(record.facts)}",
                f"[查看](#source-{slugify(spec.english)})",
            ]
        )
    lines.extend([markdown_table(index_rows), ""])

    for source_index, record in enumerate(records, start=1):
        spec = record.spec
        lines.extend(
            [
                f'<a id="source-{slugify(spec.english)}"></a>',
                f"## {source_index}. {spec.chinese}（{spec.english}）",
                "",
                f"固定来源：[revision {spec.revision}]({fixed_url(spec.english, spec.revision)})；"
                f"保留技能相关数据表 {len(record.tables)} 张、非历史事实块 {len(record.facts)} 个。",
                "",
            ]
        )
        for table_index, (label, table) in enumerate(record.tables, start=1):
            lines.extend(
                [
                    f"### {source_index}.{table_index} {label}",
                    "",
                    source_table_markdown(table),
                    "",
                ]
            )
        if record.facts:
            fact_rows = [["来源章节", "固定页事实记录"]]
            fact_rows.extend([[section, value] for section, value in record.facts])
            lines.extend(
                [
                    f"### {source_index}.{len(record.tables) + 1} 非表格技能事实",
                    "",
                    markdown_table(fact_rows),
                    "",
                ]
            )

    lines.extend(
        [
            "## 来源与复现",
            "",
        ]
    )
    for spec in SOURCES:
        lines.append(
            f"- [{spec.english} revision {spec.revision}]({fixed_url(spec.english, spec.revision)})：{spec.chinese}技能相关表格与事实。"
        )
    lines.extend(
        [
            "- 复现：`python 采集策略/工具/生成星露谷技能数据.py --check`。",
            "",
            "[上一篇：怪物数据总览](./怪物数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：节日活动数据总览](./节日活动数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只校验来源与生成结果，不写文件")
    args = parser.parse_args()
    expected = render_document()
    if args.check:
        actual = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if actual != expected:
            raise SystemExit(f"生成文档与模板不一致：{OUTPUT.relative_to(ROOT)}")
        print(
            "技能生成审计通过：skills=5/5, levels=10/10, unlocks=50/50, "
            "professions=30/30, mastery=5_levels/15_rewards, structured_xp=147/147。"
        )
        return
    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    print(f"已生成 {OUTPUT.relative_to(ROOT)} ({len(expected.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
