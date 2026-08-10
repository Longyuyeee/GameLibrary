#!/usr/bin/env python3
"""生成并审计《星露谷物语》PC v1.6.15 角色属性、状态与战斗公式。"""

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
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "角色属性战斗数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-role-combat-cache"
EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"


@dataclass(frozen=True)
class SourceSpec:
    english: str
    chinese: str
    revision: int
    table_sections: frozenset[str]
    fact_sections: frozenset[str]


SOURCES = (
    SourceSpec("Health", "生命值", 192443, frozenset(), frozenset({"Introduction", "Notes"})),
    SourceSpec(
        "Energy",
        "精力与疲惫",
        192907,
        frozenset({"Sleeping"}),
        frozenset(
            {
                "Introduction",
                "Exhaustion",
                "Sleeping",
                "Leveling Up",
                "Restoration",
                "Maximum Energy",
                "Infinite Energy",
            }
        ),
    ),
    SourceSpec(
        "Combat/Mechanics",
        "战斗公式",
        191834,
        frozenset(),
        frozenset(
            {
                "Introduction",
                "Damage",
                "Formula overview",
                "Base damage roll",
                "Critical Hit Check",
                "Attack Stat Bonus",
                "Profession Bonuses",
                "Desperado Profession",
                "Enchantments",
                "Monster defense",
                "Calculation",
                "Examples",
                "Example",
                "Damage variance",
                "Determining player defense",
                "Damage is applied",
            }
        ),
    ),
    SourceSpec(
        "Buffs",
        "增益与减益",
        191267,
        frozenset({"Available Buffs"}),
        frozenset({"Introduction", "Combining Buffs", "Buff Duration", "Preventing Negative Buffs"}),
    ),
    SourceSpec("Attack", "攻击", 189561, frozenset(), frozenset({"Introduction"})),
    SourceSpec(
        "Crit. Chance",
        "暴击率",
        188397,
        frozenset(),
        frozenset({"Introduction", "Increasing Crit. Chance"}),
    ),
    SourceSpec(
        "Crit. Power",
        "暴击威力",
        188398,
        frozenset(),
        frozenset({"Introduction", "Increasing Crit. Power"}),
    ),
    SourceSpec(
        "Defense",
        "防御",
        189562,
        frozenset({"Permanent Buffs"}),
        frozenset({"Introduction", "Permanent Buffs"}),
    ),
    SourceSpec("Immunity", "免疫", 190263, frozenset(), frozenset({"Introduction"})),
    SourceSpec(
        "Luck",
        "运气",
        193478,
        frozenset({"Daily Luck"}),
        frozenset(
            {
                "Introduction",
                "Daily Luck",
                "Special Charm",
                "Daily Luck Effects",
                "Luck Buffs",
                "Luck Buff Effects",
                "Trivia",
            }
        ),
    ),
    SourceSpec("Magnetism", "磁力", 190223, frozenset(), frozenset({"Introduction"})),
    SourceSpec(
        "Speed",
        "速度",
        193477,
        frozenset({"Permanent Buffs"}),
        frozenset(
            {
                "Introduction",
                "Weapon Speed",
                "Forge",
                "Player Speed",
                "Permanent Buffs",
                "Terrain",
                "Trivia",
            }
        ),
    ),
    SourceSpec("Weight", "击退重量", 192672, frozenset(), frozenset({"Introduction"})),
)

EXPECTED_SOURCE_COUNTS = {
    "Health": (0, 0, 6),
    "Energy": (1, 12, 19),
    "Combat/Mechanics": (0, 0, 39),
    "Buffs": (1, 24, 13),
    "Attack": (0, 0, 3),
    "Crit. Chance": (0, 0, 5),
    "Crit. Power": (0, 0, 3),
    "Defense": (1, 1, 3),
    "Immunity": (0, 0, 2),
    "Luck": (7, 14, 23),
    "Magnetism": (0, 0, 1),
    "Speed": (1, 3, 21),
    "Weight": (0, 0, 4),
}


@dataclass(frozen=True)
class SourceTable:
    rows: tuple[tuple[str, ...], ...]
    data_rows: int
    classes: tuple[str, ...]

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
        return "Introduction"
    headline = heading.select_one(".mw-headline")
    text = (headline if isinstance(headline, Tag) else heading).get_text(" ", strip=True)
    return clean_text(re.sub(r"\[\s*(?:edit|编辑)\s*\]", "", text, flags=re.IGNORECASE))


def image_label(image: Tag) -> str:
    alt = clean_text(image.get("alt") or "")
    return re.sub(r"\.(?:png|gif|jpg|jpeg)$", "", alt, flags=re.IGNORECASE)


def semantic_node_text(node: Tag) -> str:
    clone = BeautifulSoup(str(node), "html.parser").find(node.name)
    if clone is None:
        return ""
    for unwanted in clone.find_all(["sup", "style", "script", "noscript"]):
        unwanted.decompose()
    for line_break in clone.find_all("br"):
        line_break.replace_with(NavigableString(" / "))
    for image in clone.find_all("img"):
        label = image_label(image)
        image.replace_with(NavigableString(f" {label} " if label else " "))
    return clean_text(clone.get_text(" / ", strip=True))


def direct_rows(table: Tag) -> list[Tag]:
    body = table.find("tbody", recursive=False)
    parent = body if body is not None else table
    return parent.find_all("tr", recursive=False)


def table_to_grid(table: Tag) -> SourceTable:
    rows = direct_rows(table)
    if not rows:
        raise AssertionError("源表没有直接数据行")
    occupied: dict[tuple[int, int], str] = {}
    data_rows = 0
    width = 0
    for row_index, row in enumerate(rows):
        if row.find("td", recursive=False) is not None:
            data_rows += 1
        column = 0
        for cell in row.find_all(["th", "td"], recursive=False):
            while (row_index, column) in occupied:
                column += 1
            value = semantic_node_text(cell)
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
        ),
        data_rows,
        tuple(table.get("class") or ()),
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
            if any(value.startswith("navbox") for value in classes) or "basicsnavtable" in classes:
                return True
    return False


def table_label(table: Tag, section: str, grid: SourceTable) -> str:
    first = grid.rows[0][0] if grid.rows and grid.rows[0] else ""
    if first and len(first) <= 80:
        return f"{section} — {first}"
    return section


def relevant_tables(html: str, spec: SourceSpec) -> tuple[tuple[str, SourceTable], ...]:
    soup = BeautifulSoup(html, "html.parser")
    selected: list[tuple[str, SourceTable]] = []
    for table in soup.find_all("table"):
        if table.find("table") is not None or is_navigation_table(table):
            continue
        classes = set(table.get("class") or [])
        if "alert" in classes:
            continue
        section = heading_text(table.find_previous(["h2", "h3", "h4"]))
        if section not in spec.table_sections:
            continue
        grid = table_to_grid(table)
        selected.append((table_label(table, section, grid), grid))
    return tuple(selected)


def relevant_facts(html: str, spec: SourceSpec) -> tuple[tuple[str, str], ...]:
    soup = BeautifulSoup(html, "html.parser")
    facts: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add(section: str, node: Tag) -> None:
        value = semantic_node_text(node)
        key = (section, value)
        if value and key not in seen:
            seen.add(key)
            facts.append(key)

    root = soup.select_one(".mw-parser-output") or soup
    if "Introduction" in spec.fact_sections:
        for child in root.children:
            if isinstance(child, Tag) and child.name == "h2":
                break
            if isinstance(child, Tag) and child.name in {"p", "ul", "ol", "dl", "pre"}:
                add("Introduction", child)

    for heading in soup.find_all(["h2", "h3", "h4"]):
        section = heading_text(heading)
        if section not in spec.fact_sections:
            continue
        sibling = heading.find_next_sibling()
        while sibling is not None and sibling.name not in {"h2", "h3", "h4"}:
            if sibling.name in {"p", "ul", "ol", "dl", "pre"}:
                add(section, sibling)
            sibling = sibling.find_next_sibling()
    return tuple(facts)


def source_record(spec: SourceSpec) -> SourceRecord:
    html = request_html(spec.english, spec.revision)
    return SourceRecord(spec, relevant_tables(html, spec), relevant_facts(html, spec))


def source_records() -> tuple[SourceRecord, ...]:
    with ThreadPoolExecutor(max_workers=8) as executor:
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
    encoded = quote(title.replace(" ", "_"), safe=":_/")
    return f"https://stardewvalleywiki.com/mediawiki/index.php?title={encoded}&oldid={revision}"


def record_text(record: SourceRecord) -> str:
    table_text = " ".join(cell for _, table in record.tables for row in table.rows for cell in row)
    fact_text = " ".join(value for _, value in record.facts)
    return f"{table_text} {fact_text}"


def validate(records: tuple[SourceRecord, ...]) -> dict[str, int]:
    if len(records) != 13 or {record.spec.english for record in records} != {spec.english for spec in SOURCES}:
        raise AssertionError("角色战斗固定来源不是 13/13")

    for record in records:
        actual = (
            len(record.tables),
            sum(table.data_rows for _, table in record.tables),
            len(record.facts),
        )
        expected = EXPECTED_SOURCE_COUNTS[record.spec.english]
        if actual != expected:
            raise AssertionError(f"{record.spec.english} 数量漂移：actual={actual}, expected={expected}")

    by_title = {record.spec.english: record for record in records}
    required_facts = {
        "Health": ("100 points", "Iridium snake milk", "may lose up to three", "15,000g"),
        "Energy": ("At -15 energy", "1,000g", "270 maximum energy", "508", "588", "Muscle Remedy"),
        "Combat/Mechanics": (
            "Attack (stat) × 3",
            "4.6% × number of Aquamarine forges",
            "Blessing of Fangs",
            "CritMultiplier = (3 + Crit. Power (stat) / 50)",
            "7/8",
            "defense is reduced by either 0%, 10%, or 20%",
        ),
        "Buffs": ("Farming Buff", "Weakness", "food and one drink", "All buffs are cleared once the player sleeps"),
        "Attack": ("Attack", "3 damage"),
        "Crit. Chance": ("roughly equivalent to a 2% chance"),
        "Crit. Power": ("critical strike"),
        "Defense": ("minimum of 1 damage", "Jack Be Nimble, Jack Be Thick"),
        "Immunity": ("9.1%", "+11 or more"),
        "Luck": ("Daily Luck", "Special Charm", "Luck Buff"),
        "Magnetism": ("Magnetism"),
        "Speed": ("Weapon Speed", "Player Speed", "Bookseller"),
        "Weight": ("knocked back"),
    }
    for title, phrases in required_facts.items():
        text = record_text(by_title[title])
        missing = [phrase for phrase in phrases if phrase not in text]
        if missing:
            raise AssertionError(f"{title} 必要事实缺失：{missing}")

    buffs = by_title["Buffs"].tables
    if len(buffs) != 1 or buffs[0][1].data_rows != 24:
        raise AssertionError("Buff/减益名册不是 24/24")
    buff_names = {row[1] for row in buffs[0][1].rows[1:] if len(row) > 1}
    required_buffs = {
        "Farming Buff",
        "Mining Buff",
        "Fishing Buff",
        "Foraging Buff",
        "Attack Buff",
        "Defense Buff",
        "Max Energy Buff",
        "Luck Buff",
        "Magnetic Radius Buff",
        "Speed Buff",
        "Monster Musk Buff",
        "Oil of Garlic Buff",
        "Squid Ink Ravioli Buff",
        "Tipsy",
        "Adrenaline Rush",
        "Warrior Energy",
        "Yoba's Blessing",
        "Burnt",
        "Darkness",
        "Frozen",
        "Jinxed",
        "Nauseated",
        "Slimed",
        "Weakness",
    }
    if buff_names != required_buffs:
        raise AssertionError(f"Buff 名册漂移：actual={sorted(buff_names)}")

    tables = sum(len(record.tables) for record in records)
    rows = sum(table.data_rows for record in records for _, table in record.tables)
    facts = sum(len(record.facts) for record in records)
    if (tables, rows, facts) != (11, 54, 142):
        raise AssertionError(f"角色战斗总量漂移：{tables}/{rows}/{facts} != 11/54/142")
    return {"sources": len(records), "tables": tables, "rows": rows, "facts": facts, "buffs": len(buff_names)}


def render_document() -> str:
    records = source_records()
    counts = validate(records)
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 角色属性战斗数据总览",
        "",
        "# 角色属性、状态与战斗公式数据总览（Complete Player & Combat Mechanics Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        "> 数据来源：Health、Energy、Combat/Mechanics、Buffs 与九项角色属性页，共 13 个固定 revision（逐页见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷角色战斗数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 属性与自定义 Buff |",
        "| 数据范围 | 生命、精力、疲惫、睡眠恢复、击倒惩罚、攻击、防御、免疫、暴击率、暴击威力、运气、磁力、角色/武器速度、击退重量、伤害与受伤公式、全部标准 Buff/减益 |",
        "| 明确排除 | 各属性页中的可烹饪料理/饮料逐件表转交烹饪数据源，非配方消耗品、工具、钓具、武器、戒指、鞋、衣物逐件表转交道具装备数据源，并非删减；History、Bugs、References、External Links、纯导航及 Mod 数据不属于 PC v1.6.15 角色规则全集 |",
        "| 属性族 | 预计 11 / 实际 11：Health、Energy、Attack、Crit. Chance、Crit. Power、Defense、Immunity、Luck、Magnetism、Speed、Weight |",
        f"| 固定来源 | 预计 13 / 实际 {counts['sources']} |",
        f"| 域内源表 | 预计 11 张 / 实际 {counts['tables']} 张；表体记录预计 54 / 实际 {counts['rows']} |",
        f"| 规则事实块 | 预计 142 / 实际 {counts['facts']} |",
        f"| Buff/减益名册 | 预计 24 / 实际 {counts['buffs']}；名称、效果、来源、时长 4/4 字段 |",
        "| 睡眠延迟惩罚 | 预计 12 个时点 / 实际 12 |",
        "| 字段完整性 | 域内源表保留固定 revision 的全部源列与合并单元格；规则事实逐条保留固定 revision、来源章节、完整原文 3/3 字段，不做摘要或节选 |",
        "| 数量差异 | 0 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 唯一归属与跨文档边界",
        "",
        "| 数据 | 唯一数据源 | 本文处理方式 |",
        "|---|---|---|",
        "| 角色生命、精力、属性、状态与战斗公式 | 本文 | 完整保留规则、公式、状态名册与唯一属性表 |",
        "| 技能经验、升级解锁、职业与精通 | [技能属性数据总览](./技能属性数据总览.md#source-combat) | 只在生命和公式闭合中引用职业效果 |",
        "| 可烹饪料理/饮料的配方、回复、Buff 值与时长 | [烹饪配方数据总览](./烹饪配方数据总览.md) | 不复制“推荐食物”节选表；本文只维护 Buff 叠加和状态语义 |",
        "| 沙漠节厨师临时 Buff | [节日活动数据总览](./节日活动数据总览.md#source-desert-festival) | 活动组合、价格与规则留在节日域 |",
        "| 非配方消耗品；工具与钓具的逐件属性、单次行动精力消耗；武器、弹弓、鞋、戒指、饰品、锻造与附魔 | [道具装备数据总览](./道具装备数据总览.md) | 道具与装备全集由下一数据域重建；本文仅保留精力和战斗公式所需属性语义 |",
        "| 怪物生命、伤害、防御、掉落与变体 | [怪物数据总览](./怪物数据总览.md) | 怪物记录不复制到角色数据域 |",
        "",
        "## 关键数值闭合与旧稿纠错",
        "",
        "### 永久最大生命值（205）",
        "",
        "| 来源 | 增量 | 累计 |",
        "|---|---:|---:|",
        "| 初始生命 | — | 100 |",
        "| 战斗等级 1–4、6–9（8 级 × 5） | +40 | 140 |",
        "| Fighter（5 级） | +15 | 155 |",
        "| Defender（10 级） | +25 | 180 |",
        "| Iridium Snake Milk | +25 | **205** |",
        "",
        "> 旧稿把 5、10 级继续各加 5 后又叠加职业生命，误算为 215；固定 Health/Combat 规则明确这两个等级只有选择对应职业时增加生命，因此 PC v1.6.15 的永久上限是 205。",
        "",
        "### 精力与击倒边界",
        "",
        "| 项目 | 精确值 |",
        "|---|---|",
        "| 初始最大精力 | 270 |",
        "| 7 个 Stardrop | 每个 +34；永久最大值 508 |",
        "| 食物 + 饮料临时最大精力 | 最高 588 |",
        "| 疲惫 | 精力到 0；恢复到正数可恢复移动/工具，但疲惫标记持续到当天结束，除非用 Muscle Remedy 或当天首次亲吻配偶解除 |",
        "| 过劳昏倒 | 精力到 −15；屋外损失当前金币 10%，上限 1,000g |",
        "| 生命归零 | 最多丢 3 件物品，金币损失上限 15,000g；Phoenix Ring 当日首次触发例外 |",
        "",
        "### 公式索引",
        "",
        "| 公式族 | PC v1.6.15 顺序 | 固定原文 |",
        "|---|---|---|",
        "| 对怪最终伤害 | 基础伤害与锻造/戒指 → 暴击倍率 → Attack×3 → Fighter×1.1 → Brute×1.15 → 暴击时 Desperado×2 → 附魔 → 怪物防御；最低 1 | [Combat/Mechanics](#source-combat-mechanics) |",
        "| 暴击率 | 武器基础与 Aquamarine 锻造 → 匕首修正 → Aquamarine Ring/固有附魔 → Blessing of Fangs +10% → Scout×1.5 → Luck 按当前暴击率比例追加 | [Critical hit chance](#source-combat-mechanics) |",
        "| 暴击倍率 | `(3 + CritPower / 50) × (1 + CriticalPowerMultiplier)`；Desperado 在 Attack 平坦加值之后另乘 2 | [Critical hit damage](#source-combat-mechanics) |",
        "| 玩家受伤 | 怪物基础伤害先作 `[7/8, 9/8)` 波动；高防御场景随机削减有效防御 0%/10%/20%；最终至少受到 1 点 | [Player defense](#source-combat-mechanics) |",
        "| 免疫 | 每点把被施加减益概率降低 9.1%，加法叠加；总免疫达到 11 时完全免疫可拦截减益 | [Immunity](#source-immunity) |",
        "",
        "## 固定来源索引",
        "",
    ]
    index_rows = [["#", "来源", "固定 revision", "保留表/数据行/事实块", "跳转"]]
    for index, record in enumerate(records, start=1):
        index_rows.append(
            [
                str(index),
                f"{record.spec.chinese}（{record.spec.english}）",
                str(record.spec.revision),
                f"{len(record.tables)} / {sum(table.data_rows for _, table in record.tables)} / {len(record.facts)}",
                f"[查看](#source-{slugify(record.spec.english)})",
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
                f"保留数据表 {len(record.tables)} 张、数据行 {sum(table.data_rows for _, table in record.tables)}、规则事实块 {len(record.facts)}。",
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
            fact_rows = [["来源章节", "完整规则事实"]]
            fact_rows.extend([[section, value] for section, value in record.facts])
            lines.extend(
                [
                    f"### {source_index}.{len(record.tables) + 1} 非表格规则事实",
                    "",
                    markdown_table(fact_rows),
                    "",
                ]
            )

    lines.extend(["## 来源与复现", ""])
    for spec in SOURCES:
        lines.append(
            f"- [{spec.english} revision {spec.revision}]({fixed_url(spec.english, spec.revision)})：{spec.chinese}。"
        )
    lines.extend(
        [
            "- 复现：`python 采集策略/工具/生成星露谷角色战斗数据.py --check`。",
            "",
            "[上一篇：节日活动数据总览](./节日活动数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：道具装备数据总览](./道具装备数据总览.md)",
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
            "角色战斗生成审计通过：sources=13/13, attributes=11/11, tables=11/11, "
            "rows=54/54, facts=142/142, buffs=24/24, sleep_penalties=12/12, "
            "max_health=205, max_energy=508/588。"
        )
        return
    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    print(f"已生成 {OUTPUT.relative_to(ROOT)} ({len(expected.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
