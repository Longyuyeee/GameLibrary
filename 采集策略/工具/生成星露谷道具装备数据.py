#!/usr/bin/env python3
"""生成并审计《星露谷物语》PC v1.6.15 道具、工具、装备与关联规则全集。"""

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
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "道具装备数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-equipment-cache"
EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"


@dataclass(frozen=True)
class SourceSpec:
    english: str
    chinese: str
    revision: int
    table_sections: frozenset[str]
    fact_sections: frozenset[str]


SOURCES = (
    SourceSpec(
        "Tools",
        "工具与升级",
        188669,
        frozenset(
            {
                "Enchantments",
                "Hoes",
                "Pickaxes",
                "Axes",
                "Watering Cans",
                "Trash Cans",
                "Fishing Poles",
                "Pans",
                "Other Tools",
            }
        ),
        frozenset(
            {
                "Introduction",
                "Upgrades",
                "Enchantments",
                "Proficiency",
                "Affected Tools",
                "Unaffected Tools",
                "Hoes",
                "Pickaxes",
                "Axes",
                "Watering Cans",
                "Trash Cans",
                "Fishing Poles",
                "Pans",
                "Other Tools",
                "Tool Disposal",
            }
        ),
    ),
    SourceSpec(
        "Bait",
        "鱼饵",
        187707,
        frozenset({"Bait Items"}),
        frozenset({"Introduction", "Use", "Bait Items"}),
    ),
    SourceSpec(
        "Tackle",
        "渔具",
        192721,
        frozenset({"Tackle", "Secret"}),
        frozenset({"Introduction", "Tackle", "Stacking", "Profitability", "Secret"}),
    ),
    SourceSpec(
        "Weapons",
        "武器与弹药",
        192745,
        frozenset(
            {
                "Weapon Stats",
                "Sword",
                "Dagger",
                "Club",
                "Slingshot",
                "Slingshot Ammunition",
                "Unobtainable Weapons",
            }
        ),
        frozenset(
            {
                "Introduction",
                "Weapon Stats",
                "Sword",
                "Dagger",
                "Club",
                "Slingshot",
                "Slingshot Ammunition",
                "Unobtainable Weapons",
                "Weapon Level and Sell Price",
            }
        ),
    ),
    SourceSpec("Rings", "戒指", 190540, frozenset({"Introduction"}), frozenset({"Introduction"})),
    SourceSpec(
        "Footwear", "鞋靴", 192766, frozenset({"Introduction"}), frozenset({"Introduction"})
    ),
    SourceSpec(
        "Trinkets",
        "饰品",
        192096,
        frozenset({"Trinket List"}),
        frozenset({"Introduction", "Trinket List", "Drop Chances", "Monsters", "Crates and Barrels"}),
    ),
    SourceSpec(
        "Hats",
        "帽子",
        192817,
        frozenset({"Obtaining hats"}),
        frozenset({"Introduction", "Obtaining hats", "Secrets", "Notes"}),
    ),
    SourceSpec(
        "Tailoring",
        "衬衫、裤装与裁缝配方",
        193603,
        frozenset({"Shirts", "Pants", "Hats"}),
        frozenset({"Introduction", "Shirts", "Pants", "Hats", "Boots", "Notes"}),
    ),
    SourceSpec(
        "Dyeing",
        "染色",
        189829,
        frozenset({"Accepted Dye Pot Items", "Dye Strength"}),
        frozenset({"Introduction", "Dye Pots", "Accepted Dye Pot Items", "Sewing Machine", "Dye Strength"}),
    ),
    SourceSpec(
        "Forge",
        "锻造与附魔",
        193900,
        frozenset(
            {
                "Weapon forging",
                "Combat enchantments",
                "Innate enchantments",
                "Tool enchantments",
                "Infinity Weapons",
            }
        ),
        frozenset(
            {
                "Introduction",
                "Weapon forging",
                "Enchantments",
                "Combat enchantments",
                "Innate enchantments",
                "Tool enchantments",
                "Infinity Weapons",
                "Weapon Appearance",
                "Combined Rings",
                "Unforge",
                "Fishing",
                "Secrets",
            }
        ),
    ),
    SourceSpec(
        "Inventory",
        "背包与物品栏",
        171695,
        frozenset(),
        frozenset({"Introduction", "Inventory Screen", "Upgrades", "Tips"}),
    ),
    SourceSpec(
        "Special Items & Powers",
        "特殊物品与能力",
        189659,
        frozenset({"Special Items"}),
        frozenset({"Introduction", "Special Items"}),
    ),
    SourceSpec(
        "Books",
        "书籍",
        193598,
        frozenset({"Power Books", "Skill Books"}),
        frozenset({"Introduction", "Power Books", "Skill Books"}),
    ),
    SourceSpec(
        "Harvey's Clinic",
        "医疗补给",
        193867,
        frozenset({"Medical Supplies"}),
        frozenset({"Medical Supplies"}),
    ),
    SourceSpec(
        "Magic Rock Candy",
        "魔法糖冰棍",
        192339,
        frozenset({"Introduction"}),
        frozenset({"Introduction", "Locations", "Notes"}),
    ),
    SourceSpec(
        "Stardrop Tea",
        "星之果实茶",
        188132,
        frozenset({"Introduction"}),
        frozenset({"Introduction", "Tips"}),
    ),
    SourceSpec(
        "Stardrop",
        "星之果实",
        182085,
        frozenset({"Introduction"}),
        frozenset({"Introduction", "Locations", "Text", "Secret Text", "Achievements"}),
    ),
)

EXPECTED_SOURCE_COUNTS = {
    "Tools": ((12, 5, 5, 5, 5, 5, 5, 4, 11), 48),
    "Bait": ((7,), 11),
    "Tackle": ((10, 2), 8),
    "Weapons": ((5, 28, 16, 16, 2, 9, 2), 17),
    "Rings": ((30,), 1),
    "Footwear": ((18,), 2),
    "Trinkets": ((8,), 14),
    "Hats": ((122,), 7),
    "Tailoring": ((294, 14, 2, 30), 15),
    "Dyeing": ((6, 2, 545), 13),
    "Forge": ((6, 5, 3, 5, 12, 3), 28),
    "Inventory": ((), 9),
    "Special Items & Powers": ((12,), 2),
    "Books": ((19, 7), 9),
    "Harvey's Clinic": ((2,), 1),
    "Magic Rock Candy": ((1,), 3),
    "Stardrop Tea": ((7,), 5),
    "Stardrop": ((8,), 12),
}

EXPECTED_ROSTERS = {
    "bait": {
        "Bait",
        "Magnet",
        "Wild Bait",
        "Magic Bait",
        "Deluxe Bait",
        "Challenge Bait",
        "Targeted Bait",
    },
    "tackle": {
        "Spinner",
        "Dressed Spinner",
        "Trap Bobber",
        "Cork Bobber",
        "Lead Bobber",
        "Treasure Hunter",
        "Barbed Hook",
        "Curiosity Lure",
        "Quality Bobber",
        "Sonar Bobber",
    },
    "trinkets": {
        "Basilisk Paw",
        "Fairy Box",
        "Frog Egg",
        "Golden Spur",
        "Ice Rod",
        "Magic Hair Gel",
        "Magic Quiver",
        "Parrot Egg",
    },
    "medical": {"Energy Tonic", "Muscle Remedy"},
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
    value = re.sub(r'data-sort-value="[^"]*">?', "", value)
    value = re.sub(r"(?:\s*/\s*){2,}", " / ", value)
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
    encoded = quote(title.replace(" ", "_"), safe=":_/")
    return f"https://stardewvalleywiki.com/mediawiki/index.php?title={encoded}&oldid={revision}"


def table_names(table: SourceTable, column: int = 1) -> set[str]:
    return {row[column] for row in table.rows[1:] if len(row) > column and row[column]}


def validate(records: tuple[SourceRecord, ...]) -> dict[str, int]:
    if len(records) != 18 or {record.spec.english for record in records} != {
        spec.english for spec in SOURCES
    }:
        raise AssertionError("道具装备固定来源不是 18/18")
    by_title = {record.spec.english: record for record in records}
    for record in records:
        actual_rows = tuple(table.data_rows for _, table in record.tables)
        expected_rows, expected_facts = EXPECTED_SOURCE_COUNTS[record.spec.english]
        if actual_rows != expected_rows or len(record.facts) != expected_facts:
            raise AssertionError(
                f"{record.spec.english} 数量漂移："
                f"actual=({actual_rows}, {len(record.facts)}), "
                f"expected=({expected_rows}, {expected_facts})"
            )

    roster_tables = {
        "bait": by_title["Bait"].tables[0][1],
        "tackle": by_title["Tackle"].tables[0][1],
        "trinkets": by_title["Trinkets"].tables[0][1],
        "medical": by_title["Harvey's Clinic"].tables[0][1],
    }
    for key, table in roster_tables.items():
        actual = table_names(table)
        if actual != EXPECTED_ROSTERS[key]:
            raise AssertionError(f"{key} 名册漂移：actual={sorted(actual)}")

    required_headers = {
        "Weapons": (1, {"Name", "Damage", "Critical Strike Chance", "Location", "Sell Price"}),
        "Rings": (0, {"Name", "Description", "Effect", "Where to Find", "Sell Price"}),
        "Footwear": (0, {"Name", "Description", "Stats", "Source", "Sell Price"}),
        "Trinkets": (0, {"Name", "Re-Forged Stat", "Max Stat", "Description", "Source"}),
        "Hats": (0, {"Name", "Description", "How to Obtain"}),
        "Tailoring": (0, {"Name", "Description", "Dyeable"}),
    }
    for title, (table_index, headers) in required_headers.items():
        selected_table = by_title[title].tables[table_index][1]
        actual_headers = set(selected_table.rows[0])
        missing = headers - actual_headers
        if missing:
            raise AssertionError(f"{title} 必填源列缺失：{sorted(missing)}")

    tables = sum(len(record.tables) for record in records)
    rows = sum(table.data_rows for record in records for _, table in record.tables)
    facts = sum(len(record.facts) for record in records)
    if (tables, rows, facts) != (43, 1315, 205):
        raise AssertionError(f"道具装备总量漂移：{tables}/{rows}/{facts} != 43/1315/205")

    return {
        "sources": len(records),
        "tables": tables,
        "rows": rows,
        "facts": facts,
        "tools": sum(table.data_rows for _, table in by_title["Tools"].tables[1:]),
        "bait": by_title["Bait"].tables[0][1].data_rows,
        "tackle": by_title["Tackle"].tables[0][1].data_rows,
        "weapons": sum(by_title["Weapons"].tables[index][1].data_rows for index in range(1, 5)),
        "unobtainable_weapons": by_title["Weapons"].tables[6][1].data_rows,
        "ammo": by_title["Weapons"].tables[5][1].data_rows,
        "rings": by_title["Rings"].tables[0][1].data_rows,
        "footwear": by_title["Footwear"].tables[0][1].data_rows,
        "trinkets": by_title["Trinkets"].tables[0][1].data_rows,
        "hats": by_title["Hats"].tables[0][1].data_rows,
        "shirts": by_title["Tailoring"].tables[0][1].data_rows,
        "pants": by_title["Tailoring"].tables[1][1].data_rows,
        "dye_rows": by_title["Dyeing"].tables[2][1].data_rows,
        "forge_rows": sum(table.data_rows for _, table in by_title["Forge"].tables),
        "special_items": by_title["Special Items & Powers"].tables[0][1].data_rows,
        "books": sum(table.data_rows for _, table in by_title["Books"].tables),
        "medical": by_title["Harvey's Clinic"].tables[0][1].data_rows,
        "special_consumables": 3,
    }


def render_document() -> str:
    records = source_records()
    counts = validate(records)
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 道具装备数据总览",
        "",
        "# 道具、工具、装备与物品规则数据总览（Complete Items & Equipment Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        "> 数据来源：工具、鱼饵、渔具、武器、戒指、鞋靴、饰品、服装、锻造、背包、特殊物品与非配方特殊消耗品，共 18 个固定 revision（逐页见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷道具装备数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 道具、Mod 装备和自定义物品 |",
        "| 本文唯一归属 | 工具与升级、鱼竿/鱼饵/渔具、武器/弹弓/弹药、戒指、鞋靴、饰品、帽子/衬衫/裤装、裁缝与染色关系、锻造与附魔、背包、特殊能力物品、书籍、医疗补给及非配方特殊消耗品 |",
        "| 明确排除 | 作物/鱼/动物产品/怪物掉落的产出属性分别由对应数据域维护；烹饪配方与制作配方由配方域维护；技能/精通和角色属性/状态/公式由各自唯一数据源维护。本文只在弹药、染色、锻造、获取来源等关系表中保留这些对象的引用；History、Bugs、Glitches、Trivia、Gallery、References、纯导航及 Mod 数据不属于 PC v1.6.15 道具装备数据全集 |",
        f"| 固定来源 | 预计 18 / 实际 {counts['sources']} |",
        f"| 域内源表 | 预计 43 / 实际 {counts['tables']}；表体记录预计 1315 / 实际 {counts['rows']} |",
        f"| 规则事实块 | 预计 205 / 实际 {counts['facts']} |",
        "| 字段完整性 | 域内源表保留固定 revision 的全部源列与合并单元格；固定源空白统一显示为“—（固定源空白）”；规则事实逐条保留固定 revision、来源章节、完整原文 3/3 字段，不做推荐节选 |",
        "| 数量差异 | 0 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 对象与关系数量闭合",
        "",
        "| 数据族 | 预计 | 实际 | 字段/边界 |",
        "|---|---:|---:|---|",
        f"| 工具对象与升级层级 | 45 | {counts['tools']} | 名称、费用、材料、改进/描述、地点等源列全保留；附魔另计关系表 |",
        f"| 鱼饵 | 7 | {counts['bait']} | 名称、描述、说明、购买、制作 |",
        f"| 渔具 | 10 | {counts['tackle']} | 名称、描述、说明、购买、制作；另保留秘密交互 2 行 |",
        f"| 可用武器 | 62 | {counts['weapons']} | 剑 28 + 匕首 16 + 棍棒 16 + 弹弓 2 |",
        f"| 不可获取武器 | 2 | {counts['unobtainable_weapons']} | 与可用名册分开保留，不混入玩家可得数量 |",
        f"| 弹药关系 | 9 | {counts['ammo']} | 弹药倍率及普通/大师弹弓伤害 |",
        f"| 戒指 | 30 | {counts['rings']} | 描述、效果、来源、配方、购售价 |",
        f"| 鞋靴 | 18 | {counts['footwear']} | 描述、属性、来源、购售价 |",
        f"| 饰品 | 8 | {counts['trinkets']} | 重铸属性、最大属性、描述、来源、售价 |",
        f"| 帽子 | 122 | {counts['hats']} | 描述、成就、获取、废弃小屋价格 |",
        f"| 衬衫 | 294 | {counts['shirts']} | 描述、可染色、特殊属性/备注、裁缝配方 |",
        f"| 裤装 | 14 | {counts['pants']} | 描述、可染色、裁缝配方；紫色短裤特殊关系另保留 2 行 |",
        f"| 染色强度关系 | 545 | {counts['dye_rows']} | 物品、颜色名、满饱和 RGB、染色强度 |",
        f"| 锻造/附魔/无限武器关系 | 34 | {counts['forge_rows']} | 宝石、战斗附魔、固有附魔、工具附魔、无限武器 6 表 |",
        f"| 特殊物品能力 | 12 | {counts['special_items']} | 名称、用途、获取 |",
        f"| 书籍 | 26 | {counts['books']} | 能力书 19 + 技能书 7 |",
        f"| 医疗补给 | 2 | {counts['medical']} | Energy Tonic、Muscle Remedy 完整效果与价格 |",
        f"| 非配方特殊消耗品 | 3 | {counts['special_consumables']} | Magic Rock Candy、Stardrop Tea、Stardrop 固定详情页 |",
        "",
        "## 唯一归属与跨文档边界",
        "",
        "| 数据 | 唯一数据源 | 本文处理方式 |",
        "|---|---|---|",
        "| 道具、工具、装备对象与装备关系 | 本文 | 保留完整名册、全部源列、规则事实与固定 revision |",
        "| 角色生命、精力、Buff/减益、战斗公式 | [角色属性战斗数据总览](./角色属性战斗数据总览.md) | 只引用装备提供的属性，不复制公式或状态全集 |",
        "| 技能经验、职业与精通 | [技能属性数据总览](./技能属性数据总览.md) | 书籍和工具表只保留物品效果；经验公式与精通奖励留在技能域 |",
        "| 烹饪配方 | [烹饪配方数据总览](./烹饪配方数据总览.md) | 不复制料理节选或推荐表 |",
        "| 制作配方 | [制作配方数据总览](./制作配方数据总览.md) | 鱼饵、渔具、戒指和消耗品表保留固定页的制作列；完整原始配方字典仍以制作域为准 |",
        "| 作物、鱼、动物产品、怪物与掉落 | [作物](./作物数据总览.md) / [动物](./动物数据总览.md) / [怪物](./怪物数据总览.md) | 仅在弹药、染色、裁缝、锻造与来源关系中引用，不复制其生产/掉落全集 |",
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
            "- 复现：`python 采集策略/工具/生成星露谷道具装备数据.py --check`。",
            "",
            "[上一篇：角色属性战斗数据总览](./角色属性战斗数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：团队与开发历程](../特色文档/团队与开发历程.md)",
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
            "道具装备生成审计通过：sources=18/18, tables=43/43, rows=1315/1315, "
            "facts=205/205, tools=45/45, bait=7/7, tackle=10/10, weapons=62+2, "
            "rings=30/30, footwear=18/18, trinkets=8/8, hats=122/122, "
            "shirts=294/294, pants=14/14, dye_rows=545/545。"
        )
        return
    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    print(f"已生成 {OUTPUT.relative_to(ROOT)} ({len(expected.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
