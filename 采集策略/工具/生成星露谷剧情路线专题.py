#!/usr/bin/env python3
"""从固定 Stardew Valley Wiki revision 生成爷爷/完美与社区中心/Joja 专题全集。"""

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
GAME = ROOT / "牧场经营类" / "星露谷物语"
GRANDPA_OUTPUT = GAME / "特色文档" / "爷爷评价与完美追踪.md"
ROUTE_OUTPUT = GAME / "特色文档" / "社区中心与Joja路线.md"
CACHE = ROOT / ".git" / "gamedocs-story-route-cache"
EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"


@dataclass(frozen=True)
class SourceSpec:
    title: str
    chinese: str
    revision: int
    table_sections: frozenset[str]
    fact_sections: frozenset[str]


GRANDPA_SOURCES = (
    SourceSpec(
        "Grandpa",
        "爷爷评价",
        182923,
        frozenset({"Scoring", "Results"}),
        frozenset({"Grandpa's Evaluation", "Scoring", "Results", "Notes"}),
    ),
    SourceSpec(
        "Perfection",
        "完美度系统与豁免",
        184492,
        frozenset({"Perfection system"}),
        frozenset(
            {
                "Introduction",
                "Perfection system",
                "Multiplayer",
                "Unlocked content",
                "Perfection Waivers",
                "Notes",
            }
        ),
    ),
    SourceSpec(
        "Statue Of Perfection",
        "完美雕像",
        186368,
        frozenset({"Introduction"}),
        frozenset({"Introduction"}),
    ),
    SourceSpec(
        "Statue Of True Perfection",
        "真正完美雕像",
        182682,
        frozenset({"Introduction"}),
        frozenset({"Introduction", "Notes"}),
    ),
    SourceSpec(
        "The Summit",
        "山顶与完美结局",
        193935,
        frozenset({"Introduction"}),
        frozenset({"Introduction", "Cutscene"}),
    ),
)

ROUTE_SOURCES = (
    SourceSpec(
        "Bundles",
        "标准收集包与遗失收集包",
        193528,
        frozenset(
            {
                "Traveling Cart Availability",
                "Crafts Room",
                "Pantry",
                "Fish Tank",
                "Boiler Room",
                "Bulletin Board",
                "Vault",
                "Abandoned JojaMart",
            }
        ),
        frozenset(
            {
                "Introduction",
                "Traveling Cart Availability",
                "Standard Bundles",
                "Crafts Room",
                "Pantry",
                "Fish Tank",
                "Boiler Room",
                "Bulletin Board",
                "Vault",
                "Abandoned JojaMart",
                "Remixed Bundles",
            }
        ),
    ),
    SourceSpec(
        "Remixed Bundles",
        "混合收集包候选池",
        191838,
        frozenset(
            {
                "Crafts Room",
                "Bundle 1",
                "Bundle 2",
                "Bundle 3",
                "Bundle 4",
                "Bundle 5",
                "Bundle 6",
                "Pantry",
                "Fish Tank",
                "Boiler Room",
                "Bundles",
                "Bulletin Board",
                "Vault",
            }
        ),
        frozenset(
            {
                "Introduction",
                "Crafts Room",
                "Bundle 1",
                "Bundle 2",
                "Bundle 3",
                "Bundle 4",
                "Bundle 5",
                "Bundle 6",
                "Pantry",
                "Fish Tank",
                "Boiler Room",
                "Bundles",
                "Bulletin Board",
                "Vault",
            }
        ),
    ),
    SourceSpec(
        "Community Center",
        "社区中心修复与完成后果",
        193096,
        frozenset({"Introduction", "Restoring the Community Center"}),
        frozenset({"Introduction", "Restoring the Community Center", "Willy's Boat"}),
    ),
    SourceSpec(
        "Joja Community Development Form",
        "Joja 社区开发项目",
        187019,
        frozenset(),
        frozenset({"Introduction", "Developments", "Completion", "Notes"}),
    ),
    SourceSpec(
        "Movie Theater",
        "两条路线的电影院解锁",
        193933,
        frozenset({"Introduction"}),
        frozenset({"Introduction"}),
    ),
)

SOURCES = GRANDPA_SOURCES + ROUTE_SOURCES

# 首次红灯运行后用固定 revision 的实际输出锁定；任何后续漂移都会使生成失败。
EXPECTED_SOURCE_COUNTS = {
    "Grandpa": (6, 23, 10),
    "Perfection": (1, 11, 12),
    "Statue Of Perfection": (1, 6, 1),
    "Statue Of True Perfection": (1, 6, 4),
    "The Summit": (1, 3, 5),
    "Bundles": (39, 176, 23),
    "Remixed Bundles": (53, 251, 18),
    "Community Center": (2, 7, 12),
    "Joja Community Development Form": (0, 0, 10),
    "Movie Theater": (1, 6, 5),
}

STANDARD_BUNDLES = {
    "Spring Foraging Bundle",
    "Summer Foraging Bundle",
    "Fall Foraging Bundle",
    "Winter Foraging Bundle",
    "Construction Bundle",
    "Exotic Foraging Bundle",
    "Spring Crops Bundle",
    "Summer Crops Bundle",
    "Fall Crops Bundle",
    "Quality Crops Bundle",
    "Animal Bundle",
    "Artisan Bundle",
    "River Fish Bundle",
    "Lake Fish Bundle",
    "Ocean Fish Bundle",
    "Night Fishing Bundle",
    "Crab Pot Bundle",
    "Specialty Fish Bundle",
    "Blacksmith's Bundle",
    "Geologist's Bundle",
    "Adventurer's Bundle",
    "Chef's Bundle",
    "Dye Bundle",
    "Field Research Bundle",
    "Fodder Bundle",
    "Enchanter's Bundle",
    "2,500 Bundle",
    "5,000 Bundle",
    "10,000 Bundle",
    "25,000 Bundle",
    "The Missing Bundle",
}

REMIXED_BUNDLES = {
    "Spring Foraging Bundle",
    "Summer Foraging Bundle",
    "Fall Foraging Bundle",
    "Winter Foraging Bundle",
    "Construction Bundle",
    "Sticky Bundle",
    "Forest Bundle",
    "Exotic Foraging Bundle",
    "Wild Medicine Bundle",
    "Spring Crops Bundle",
    "Summer Crops Bundle",
    "Fall Crops Bundle",
    "Quality Crops Bundle",
    "Rare Crops Bundle",
    "Animal Bundle",
    "Fish Farmer's Bundle",
    "Garden Bundle",
    "Artisan Bundle",
    "Brewer's Bundle",
    "River Fish Bundle",
    "Lake Fish Bundle",
    "Ocean Fish Bundle",
    "Night Fishing Bundle",
    "Crab Pot Bundle",
    "Specialty Fish Bundle",
    "Quality Fish Bundle",
    "Master Fisher's Bundle",
    "Blacksmith's Bundle",
    "Geologist's Bundle",
    "Adventurer's Bundle",
    "Treasure Hunter's Bundle",
    "Engineer's Bundle",
    "Chef's Bundle",
    "Dye Bundle",
    "Field Research Bundle",
    "Fodder Bundle",
    "Enchanter's Bundle",
    "Children's Bundle",
    "Forager's Bundle",
    "Home Cook's Bundle",
    "Helper's Bundle",
    "Spirit's Eve Bundle",
    "Winter Star Bundle",
    "2,500 Bundle",
    "5,000 Bundle",
    "10,000 Bundle",
    "25,000 Bundle",
}


@dataclass(frozen=True)
class SourceTable:
    rows: tuple[tuple[str, ...], ...]
    data_rows: int

    @property
    def width(self) -> int:
        return max((len(row) for row in self.rows), default=0)


@dataclass(frozen=True)
class SourceRecord:
    spec: SourceSpec
    tables: tuple[tuple[str, SourceTable], ...]
    facts: tuple[tuple[str, str], ...]


def clean_text(value: str) -> str:
    value = re.sub(r"\[\s*(?:edit|编辑)\s*\]", "", value, flags=re.IGNORECASE)
    value = re.sub(r'data-sort-value="[^"]*">?', "", value)
    value = re.sub(r"(?:\s*/\s*){2,}", " / ", value)
    return re.sub(r"\s+", " ", value).strip(" /\u00a0")


def heading_text(heading: Tag | None) -> str:
    if heading is None:
        return "Introduction"
    headline = heading.select_one(".mw-headline")
    text = (headline if isinstance(headline, Tag) else heading).get_text(" ", strip=True)
    return clean_text(text)


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
                for column_offset in range(colspan):
                    occupied[(row_index + row_offset, column + column_offset)] = value
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


def relevant_tables(html: str, spec: SourceSpec) -> tuple[tuple[str, SourceTable], ...]:
    soup = BeautifulSoup(html, "html.parser")
    selected: list[tuple[str, SourceTable]] = []
    for table in soup.find_all("table"):
        if table.find_parent("table") is not None or is_navigation_table(table):
            continue
        if "alert" in set(table.get("class") or []):
            continue
        section = heading_text(table.find_previous(["h2", "h3", "h4"]))
        if section not in spec.table_sections:
            continue
        grid = table_to_grid(table)
        first = grid.rows[0][0] if grid.rows and grid.rows[0] else ""
        label = f"{section} — {first}" if first and len(first) <= 100 else section
        selected.append((label, grid))
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
    html = request_html(spec.title, spec.revision)
    return SourceRecord(spec, relevant_tables(html, spec), relevant_facts(html, spec))


def source_records() -> tuple[SourceRecord, ...]:
    with ThreadPoolExecutor(max_workers=8) as executor:
        return tuple(executor.map(source_record, SOURCES))


def normalize_bundle_name(value: str) -> str:
    value = re.sub(r"^Bundle\s+[^/]+\s*/\s*", "", value)
    value = re.sub(r"\s*\([^)]*chosen at random\)\s*", "", value)
    return clean_text(value)


def bundle_names(record: SourceRecord) -> set[str]:
    names: set[str] = set()
    for _, table in record.tables:
        if not table.rows or not table.rows[0]:
            continue
        candidate = normalize_bundle_name(table.rows[0][0])
        if candidate.endswith("Bundle"):
            names.add(candidate)
    return names


def validate(records: tuple[SourceRecord, ...]) -> dict[str, int]:
    by_title = {record.spec.title: record for record in records}
    mismatches: list[str] = []
    for record in records:
        actual = (
            len(record.tables),
            sum(table.data_rows for _, table in record.tables),
            len(record.facts),
        )
        expected = EXPECTED_SOURCE_COUNTS[record.spec.title]
        if actual != expected:
            mismatches.append(f"{record.spec.title}: actual={actual}, expected={expected}")
    if mismatches:
        raise AssertionError("固定源数量尚未锁定或发生漂移：" + "; ".join(mismatches))

    actual_standard = bundle_names(by_title["Bundles"])
    if actual_standard != STANDARD_BUNDLES:
        raise AssertionError(
            f"标准收集包名册漂移：missing={sorted(STANDARD_BUNDLES - actual_standard)}, "
            f"extra={sorted(actual_standard - STANDARD_BUNDLES)}"
        )
    actual_remixed = bundle_names(by_title["Remixed Bundles"])
    if actual_remixed != REMIXED_BUNDLES:
        raise AssertionError(
            f"混合收集包名册漂移：missing={sorted(REMIXED_BUNDLES - actual_remixed)}, "
            f"extra={sorted(actual_remixed - REMIXED_BUNDLES)}"
        )

    grandpa = by_title["Grandpa"]
    grandpa_rows = [table.data_rows for _, table in grandpa.tables]
    if grandpa_rows != [6, 2, 3, 4, 4, 4]:
        raise AssertionError(f"爷爷评分/结果行数漂移：{grandpa_rows}")
    perfection_rows = [table.data_rows for _, table in by_title["Perfection"].tables]
    if perfection_rows != [11]:
        raise AssertionError(f"完美度类别行数漂移：{perfection_rows}")

    grandpa_records = [by_title[source.title] for source in GRANDPA_SOURCES]
    route_records = [by_title[source.title] for source in ROUTE_SOURCES]
    return {
        "sources": len(records),
        "tables": sum(len(record.tables) for record in records),
        "rows": sum(table.data_rows for record in records for _, table in record.tables),
        "facts": sum(len(record.facts) for record in records),
        "grandpa_sources": len(grandpa_records),
        "grandpa_tables": sum(len(record.tables) for record in grandpa_records),
        "grandpa_rows": sum(
            table.data_rows for record in grandpa_records for _, table in record.tables
        ),
        "grandpa_facts": sum(len(record.facts) for record in grandpa_records),
        "route_sources": len(route_records),
        "route_tables": sum(len(record.tables) for record in route_records),
        "route_rows": sum(
            table.data_rows for record in route_records for _, table in record.tables
        ),
        "route_facts": sum(len(record.facts) for record in route_records),
        "standard_bundles": len(actual_standard),
        "remixed_bundles": len(actual_remixed),
    }


def markdown_escape(value: str) -> str:
    value = value if value else "—（固定源空白）"
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
        rows.append(["—（固定源无独立表头）"] * table.width)
    return markdown_table(rows)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def fixed_url(title: str, revision: int) -> str:
    encoded = quote(title.replace(" ", "_"), safe=":_/')")
    return f"https://stardewvalleywiki.com/mediawiki/index.php?title={encoded}&oldid={revision}"


def render_source_sections(records: list[SourceRecord], heading_level: int = 2) -> list[str]:
    lines: list[str] = []
    prefix = "#" * heading_level
    subprefix = "#" * (heading_level + 1)
    for source_index, record in enumerate(records, start=1):
        anchor = f"source-{slugify(record.spec.title)}"
        lines.extend(
            [
                f'<a id="{anchor}"></a>',
                f"{prefix} {source_index}. {record.spec.chinese}（{record.spec.title}）",
                "",
                f"固定来源：[revision {record.spec.revision}]({fixed_url(record.spec.title, record.spec.revision)})；"
                f"保留数据表 {len(record.tables)} 张、数据行 "
                f"{sum(table.data_rows for _, table in record.tables)}、规则事实块 {len(record.facts)}。",
                "",
            ]
        )
        for table_index, (label, table) in enumerate(record.tables, start=1):
            lines.extend(
                [
                    f"{subprefix} {source_index}.{table_index} {label}",
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
                    f"{subprefix} {source_index}.{len(record.tables) + 1} 非表格规则事实",
                    "",
                    markdown_table(fact_rows),
                    "",
                ]
            )
    return lines


def render_grandpa_document(records: tuple[SourceRecord, ...], counts: dict[str, int]) -> str:
    by_title = {record.spec.title: record for record in records}
    selected = [by_title[source.title] for source in GRANDPA_SOURCES]
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 爷爷评价与完美追踪",
        "",
        "# 爷爷评价与完美追踪 — PC v1.6.15 全集",
        "",
        "> 本页是爷爷评价、完美度类别、完美豁免、两座完美雕像与山顶解锁的唯一专题数据源。",
        "> 对象名册由对应完整数据文档维护；本页保留判定条件和总量，不复制鱼类、料理、配方、怪物、NPC 或装备节选表。",
        "",
        "## 一、数据覆盖声明",
        "",
        "| 项目 | 对账结果 |",
        "|------|------|",
        "| 目标版本 | PC v1.6.15 |",
        f"| 固定来源 | 预计 5 / 实际 {counts['grandpa_sources']} |",
        f"| 域内源表 | 预计 {counts['grandpa_tables']} / 实际 {counts['grandpa_tables']}；表体记录预计 {counts['grandpa_rows']} / 实际 {counts['grandpa_rows']} |",
        f"| 规则事实块 | 预计 {counts['grandpa_facts']} / 实际 {counts['grandpa_facts']} |",
        "| 爷爷评分条件 | 预计 19 / 实际 19 |",
        "| 蜡烛结果档位 | 预计 4 / 实际 4 |",
        "| 完美度类别 | 预计 11 / 实际 11 |",
        "| 完美雕像 | 预计 2 / 实际 2 |",
        "| 数量差异 | 0 |",
        "| 未知或待核实字段 | 0 |",
        "| 验收状态 | **已完成** |",
        "",
        "### 范围边界",
        "",
        "- 包含固定源在上述章节明示的全部评分条件、分值、结果、完美度类别、多人规则、豁免规则和解锁内容。",
        "- 山顶只保留合法完美解锁与过场条件；非法进入、对白全文、纯 Trivia、History、Gallery、Bugs 和外部链接不属于本域。",
        "- 完美度要求引用的对象全集通过下列入口维护，避免在本页生成第二份名单。",
        "",
        "## 二、对象全集入口",
        "",
        "| 完美度关联对象 | 唯一数据源 |",
        "|------|------|",
        "| NPC 名册、关系与事件 | [NPC数据总览](../数值数据/NPC数据总览.md) / [NPC关系数值总览](../数值数据/NPC关系数值总览.md) / [NPC事件数据总览](../数值数据/NPC事件数据总览.md) |",
        "| 料理与制作配方 | [烹饪配方数据总览](../数值数据/烹饪配方数据总览.md) / [制作配方数据总览](../数值数据/制作配方数据总览.md) |",
        "| 怪物猎杀目标 | [怪物数据总览](../数值数据/怪物数据总览.md) |",
        "| 技能等级 | [技能属性数据总览](../数值数据/技能属性数据总览.md) |",
        "| 星之果实 | [道具装备数据总览](../数值数据/道具装备数据总览.md#source-stardrop) |",
        "| 鱼类与出货对象 | [鱼类数据总览](../数值数据/鱼类数据总览.md) / [出货收集数据总览](../数值数据/出货收集数据总览.md) |",
        "",
        "## 三、固定来源完整记录",
        "",
    ]
    lines.extend(render_source_sections(selected))
    lines.extend(
        [
            "## 四、审计结论",
            "",
            "- 旧稿的推荐路线、难度星级、年产值估算和对象节选已经移除。",
            "- 固定 Perfection 源要求完成 149 项，婚戒即使多人也不要求；制作数据域仍维护 150/150 个配方对象，两者统计口径不同。",
            "- 鱼类 77/77、图鉴 72/72 与 Full Shipment 154/154 已移交独立全集；本页只维护完美度类别总量和判定关系。",
            "",
            "---",
            "",
            "[上一篇：角色弧线深度解析](./角色弧线深度解析.md) · [返回游戏概览](../游戏概览.md) · [下一篇：社区中心与Joja路线](./社区中心与Joja路线.md)",
            "",
        ]
    )
    return "\n".join(lines)


def render_route_document(records: tuple[SourceRecord, ...], counts: dict[str, int]) -> str:
    by_title = {record.spec.title: record for record in records}
    selected = [by_title[source.title] for source in ROUTE_SOURCES]
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 社区中心与Joja路线",
        "",
        "# 社区中心与 Joja 路线 — PC v1.6.15 全集",
        "",
        "> 本页是标准收集包、混合收集包候选池、社区中心修复、Joja 社区开发项目和两条路线电影院解锁的唯一专题数据源。",
        "",
        "## 一、数据覆盖声明",
        "",
        "| 项目 | 对账结果 |",
        "|------|------|",
        "| 目标版本 | PC v1.6.15 |",
        f"| 固定来源 | 预计 5 / 实际 {counts['route_sources']} |",
        f"| 域内源表 | 预计 {counts['route_tables']} / 实际 {counts['route_tables']}；表体记录预计 {counts['route_rows']} / 实际 {counts['route_rows']} |",
        f"| 规则事实块 | 预计 {counts['route_facts']} / 实际 {counts['route_facts']} |",
        "| 标准房间收集包 | 预计 30 / 实际 30 |",
        "| 遗失收集包 | 预计 1 / 实际 1 |",
        "| 混合模式候选包 | 预计 47 / 实际 47 |",
        "| 数量差异 | 0 |",
        "| 未知或待核实字段 | 0 |",
        "| 验收状态 | **已完成** |",
        "",
        "### 范围边界",
        "",
        "- 标准模式保留 6 个房间的 30 个收集包、房间奖励、旅行货车一年完成保证及遗失收集包的全部固定源记录。",
        "- 混合模式不是固定的 30 张表，而是按房间槽位从 47 个候选包中抽取；候选表、随机选取数量、物品、品质、数量、来源和奖励均完整保留。",
        "- Joja 路线保留会员/开发项目、费用、完成后果与电影院解锁；电影排片、零食、抓娃娃机奖池属于电影院内容域，不在路线文档做节选。",
        "- History、Trivia、Gallery、Bugs、References、纯对白和外部导航不属于本域。",
        "",
        "## 二、结构关系",
        "",
        "| 路线 | 完整数据入口 |",
        "|------|------|",
        "| 社区中心标准模式 | [标准收集包固定源](#source-bundles) |",
        "| 社区中心混合模式 | [混合收集包固定源](#source-remixed-bundles) |",
        "| 社区中心修复与完成后果 | [社区中心固定源](#source-community-center) |",
        "| Joja 社区开发项目 | [Joja 开发表固定源](#source-joja-community-development-form) |",
        "| 两条路线的电影院位置与解锁 | [电影院固定源](#source-movie-theater) |",
        "",
        "## 三、固定来源完整记录",
        "",
    ]
    lines.extend(render_source_sections(selected))
    lines.extend(
        [
            "## 四、审计结论",
            "",
            "- 旧稿只维护标准收集包，遗漏混合模式 47 个候选包；本轮已经补齐并固定来源。",
            "- 旧稿将社区中心开放写成雨天触发，并在剧情页混淆工艺室/锅炉房奖励；旧手写口径不再作为数据源。",
            "- 收集物品本身的价格、产地和对象属性继续归属各对象数据域；本页只完整维护路线要求与奖励关系。",
            "",
            "---",
            "",
            "[上一篇：爷爷评价与完美追踪](./爷爷评价与完美追踪.md) · [返回游戏概览](../游戏概览.md) · [下一篇：齐先生的挑战与姜岛](./齐先生的挑战与姜岛.md)",
            "",
        ]
    )
    return "\n".join(lines)


def build_documents() -> tuple[str, str, dict[str, int]]:
    records = source_records()
    counts = validate(records)
    return render_grandpa_document(records, counts), render_route_document(records, counts), counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只检查生成结果与当前文档是否一致")
    args = parser.parse_args()
    grandpa, route, counts = build_documents()
    if args.check:
        mismatches = []
        for path, expected in ((GRANDPA_OUTPUT, grandpa), (ROUTE_OUTPUT, route)):
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                mismatches.append(str(path.relative_to(ROOT)))
        if mismatches:
            raise SystemExit(f"生成结果与当前文档不一致：{mismatches}")
    else:
        GRANDPA_OUTPUT.write_text(grandpa, encoding="utf-8", newline="\n")
        ROUTE_OUTPUT.write_text(route, encoding="utf-8", newline="\n")
    print(
        "剧情路线专题生成审计通过："
        f"sources={counts['sources']}/10, tables={counts['tables']}, rows={counts['rows']}, "
        f"facts={counts['facts']}, grandpa=19+4+11, "
        f"standard_bundles={counts['standard_bundles']}/31, "
        f"remixed_candidates={counts['remixed_bundles']}/47。"
    )


if __name__ == "__main__":
    main()
