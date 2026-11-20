#!/usr/bin/env python3
"""生成并审计《星露谷物语》PC v1.6.15 节日、奖励与商店全集。"""

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
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "节日活动数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-festival-cache"
EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"
FISH_REVISION = 193885
SMOKED_FISH_REVISION = 191902


@dataclass(frozen=True)
class FestivalDefinition:
    english: str
    chinese: str
    season: str
    date: str
    day_count: int
    time: str
    location: str


FESTIVALS = (
    FestivalDefinition("Egg Festival", "复活节", "春", "13", 1, "9:00–14:00", "Pelican Town"),
    FestivalDefinition("Desert Festival", "沙漠节", "春", "15–17", 3, "10:00–2:00", "The Desert"),
    FestivalDefinition("Flower Dance", "花舞节", "春", "24", 1, "9:00–14:00", "Cindersap Forest"),
    FestivalDefinition("Luau", "夏威夷宴会", "夏", "11", 1, "9:00–14:00", "The Beach"),
    FestivalDefinition("Trout Derby", "鳟鱼大赛", "夏", "20–21", 2, "6:10–2:00", "Cindersap Forest"),
    FestivalDefinition(
        "Dance of the Moonlight Jellies",
        "月光水母起舞",
        "夏",
        "28",
        1,
        "22:00–24:00",
        "The Beach",
    ),
    FestivalDefinition("Stardew Valley Fair", "星露谷展览会", "秋", "16", 1, "9:00–15:00", "Pelican Town"),
    FestivalDefinition("Spirit's Eve", "亡灵节", "秋", "27", 1, "22:00–23:50", "Pelican Town"),
    FestivalDefinition("Festival of Ice", "冰雪节", "冬", "8", 1, "9:00–14:00", "Cindersap Forest"),
    FestivalDefinition("SquidFest", "鱿鱼节", "冬", "12–13", 2, "6:10–2:00", "The Beach"),
    FestivalDefinition("Night Market", "夜市", "冬", "15–17", 3, "17:00–2:00", "The Beach"),
    FestivalDefinition("Feast of the Winter Star", "冬日星盛宴", "冬", "25", 1, "9:00–14:00", "Pelican Town"),
)


@dataclass(frozen=True)
class SourceSpec:
    english: str
    chinese: str
    revision: int
    sections: frozenset[str]


SOURCES = (
    SourceSpec(
        "Festivals",
        "节日总页",
        193562,
        frozenset(
            {
                "Introduction",
                "Shop Closures",
                *(festival.english for festival in FESTIVALS),
            }
        ),
    ),
    SourceSpec(
        "Egg Festival",
        "复活节",
        192059,
        frozenset({"Introduction", "Shop", "Egg Hunt", "Trivia"}),
    ),
    SourceSpec(
        "Desert Festival",
        "沙漠节",
        191598,
        frozenset(
            {
                "Introduction",
                "Attractions",
                "The Races",
                "Calico Egg Merchant",
                "Villager Shops",
                "Emily's Outfit Services",
                "Chef",
                "Free Cactus",
                "Skull Cavern",
                "Harvey's Medical Station",
                "Willy's Fishing Quests",
                "Scholar",
                "Shrouded Figure",
                "Traveling Cart",
                "Villager Attendees",
                "Notes",
            }
        ),
    ),
    SourceSpec(
        "Flower Dance",
        "花舞节",
        184968,
        frozenset({"Introduction", "Shop", "Dance Partners", "Trivia"}),
    ),
    SourceSpec(
        "Luau",
        "夏威夷宴会",
        187204,
        frozenset(
            {
                "Introduction",
                "Shop",
                "Potluck",
                "Missing Something Response",
                "Best Response",
                "Good Response",
                "Neutral Response",
                "Bad Response",
                "Worst Response",
                "Secret Response",
            }
        ),
    ),
    SourceSpec(
        "Trout Derby",
        "鳟鱼大赛",
        192887,
        frozenset({"Introduction", "Derby Booth", "Prizes", "Tips", "Quotes"}),
    ),
    SourceSpec(
        "Dance of the Moonlight Jellies",
        "月光水母起舞",
        184308,
        frozenset({"Introduction", "Shop", "Trivia"}),
    ),
    SourceSpec(
        "Stardew Valley Fair",
        "星露谷展览会",
        193429,
        frozenset(
            {
                "Introduction",
                "Attractions",
                "Grange Display",
                "Scoring",
                "Base Points",
                "Number of Items",
                "Categories",
                "Sell Price & Quality",
                "Shop",
                "Fixed Stock",
                "Random Stock",
                "Trivia",
            }
        ),
    ),
    SourceSpec(
        "Spirit's Eve",
        "亡灵节",
        192510,
        frozenset({"Introduction", "Haunted Maze", "Surviving the Haunted Maze", "Shop", "Trivia"}),
    ),
    SourceSpec("Festival of Ice", "冰雪节", 192452, frozenset({"Introduction", "Shop", "Trivia"})),
    SourceSpec(
        "SquidFest",
        "鱿鱼节",
        193809,
        frozenset({"Introduction", "Booth", "Prizes", "Tips", "Quotes"}),
    ),
    SourceSpec(
        "Night Market",
        "夜市",
        193627,
        frozenset(
            {
                "Introduction",
                "Attractions",
                "Desert Trader",
                "Decoration Boat",
                "Famous Painter Lupini",
                "Fishing Submarine",
                "Magic Shop Boat",
                "Mermaid Boat",
                "Shrouded Figure",
                "Traveling Cart",
                "Villager Attendees",
                "Notes",
                "Trivia",
            }
        ),
    ),
    SourceSpec(
        "Feast of the Winter Star",
        "冬日星盛宴",
        179976,
        frozenset(
            {
                "Introduction",
                "Shop",
                "Fixed Stock",
                "Random Stock",
                "Gift-giving",
                "Possible Received Gifts",
                "Trivia",
            }
        ),
    ),
)

SHOP_SECTIONS = frozenset(
    {
        "Shop",
        "Calico Egg Merchant",
        "Villager Shops",
        "Fixed Stock",
        "Random Stock",
        "Decoration Boat",
        "Famous Painter Lupini",
        "Magic Shop Boat",
    }
)

FACT_ONLY_SECTIONS = {
    "Trout Derby": frozenset({"Characters"}),
    "SquidFest": frozenset({"Characters"}),
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


def semantic_cell_text(cell: Tag) -> str:
    return semantic_node_text(cell)


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
            if any(value.startswith("navbox") for value in classes):
                return True
    return False


def table_label(table: Tag, section: str, grid: SourceTable) -> str:
    first = grid.rows[0][0] if grid.rows and grid.rows[0] else ""
    if first and first.lower() not in {"image", "item", "booth", "place", "quality", "day"}:
        if len(first) <= 80:
            return f"{section} — {first}"
    parent = table.find_parent("table")
    if parent is not None:
        title_cell = parent.find("th")
        if isinstance(title_cell, Tag):
            parent_title = clean_text(title_cell.get_text(" ", strip=True))
            if parent_title and len(parent_title) <= 80:
                return f"{section} — {parent_title}"
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
        if section not in spec.sections:
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
    if "Introduction" in spec.sections:
        for child in root.children:
            if isinstance(child, Tag) and child.name == "h2":
                break
            if isinstance(child, Tag) and child.name in {"p", "ul", "ol", "dl", "pre"}:
                add("Introduction", child)

    fact_sections = spec.sections | FACT_ONLY_SECTIONS.get(spec.english, frozenset())
    for heading in soup.find_all(["h2", "h3", "h4"]):
        section = heading_text(heading)
        if section not in fact_sections:
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
    encoded = quote(title.replace(" ", "_"), safe=":_")
    return f"https://stardewvalleywiki.com/mediawiki/index.php?title={encoded}&oldid={revision}"


def record_text(record: SourceRecord) -> str:
    table_text = " ".join(cell for _, table in record.tables for row in table.rows for cell in row)
    fact_text = " ".join(value for _, value in record.facts)
    return f"{table_text} {fact_text}"


def base_section(label: str) -> str:
    return label.split(" — ", 1)[0]


def price_values(cell: Tag) -> tuple[int, ...]:
    values = tuple(int(value.replace(",", "")) for value in re.findall(r"([\d,]+)g", cell.get_text(" ", strip=True)))
    if len(values) not in {2, 4}:
        raise AssertionError(f"鱼价字段不是 N/S 或 N/S/G/I 档：{cell.get_text(' ', strip=True)}")
    return values


def grange_score(price: int, quality_index: int) -> int:
    thresholds = (
        (0, (1, 2, 3, 5)),
        (20, (2, 3, 4, 6)),
        (90, (3, 4, 5, 7)),
        (200, (4, 5, 6, 8)),
        (300, (5, 6, 6, 8)),
        (400, (6, 6, 6, 8)),
    )
    result = thresholds[0][1][quality_index]
    for minimum, points in thresholds:
        if price >= minimum:
            result = points[quality_index]
    return result


def smoked_profile(prices: tuple[int, ...], artisan: bool) -> str:
    smoked_prices = tuple(
        (price * 14) // 5 if artisan else price * 2
        for price in prices
    )
    points = tuple(grange_score(price, quality) for quality, price in enumerate(smoked_prices))
    price_text = "/".join([*(f"{price}g" for price in smoked_prices), *("—" for _ in range(4 - len(prices)))])
    point_text = "/".join([*(str(point) for point in points), *("—" for _ in range(4 - len(prices)))])
    return f"{price_text} → {point_text}"


def smoked_fish_score_rows() -> list[list[str]]:
    fish_html = request_html("Fish", FISH_REVISION)
    smoked_html = request_html("Smoked Fish", SMOKED_FISH_REVISION)
    smoked_text = clean_text(BeautifulSoup(smoked_html, "html.parser").get_text(" ", strip=True))
    required = ("retaining quality", "Fisher and Angler professions", "2.8 times")
    missing = [phrase for phrase in required if phrase not in smoked_text]
    if missing:
        raise AssertionError(f"烟熏鱼公式事实缺失：{missing}")

    soup = BeautifulSoup(fish_html, "html.parser")
    allowed_sections = {
        "Fishing Pole Fish",
        "Night Market Fish",
        "Legendary Fish",
        "Legendary Fish II",
        "Crab Pot Fish",
    }
    output: list[list[str]] = []
    seen: set[str] = set()
    for table in soup.find_all("table"):
        if table.find("table") is None:
            continue
        section = heading_text(table.find_previous(["h2", "h3", "h4"]))
        if section not in allowed_sections:
            continue
        for row in direct_rows(table):
            cells = row.find_all(["th", "td"], recursive=False)
            if len(cells) < 6 or cells[0].name != "td":
                continue
            name = clean_text(cells[1].get_text(" ", strip=True))
            if not name or name in seen:
                raise AssertionError(f"烟熏鱼名册名称为空或重复：{name}")
            seen.add(name)
            base_prices = price_values(cells[3])
            fisher_prices = price_values(cells[4])
            angler_prices = price_values(cells[5])
            output.append(
                [
                    name,
                    section,
                    smoked_profile(base_prices, False),
                    smoked_profile(fisher_prices, False),
                    smoked_profile(angler_prices, False),
                    smoked_profile(base_prices, True),
                    smoked_profile(fisher_prices, True),
                    smoked_profile(angler_prices, True),
                ]
            )
    if len(output) != 71:
        raise AssertionError(f"可烟熏鱼名册漂移：{len(output)} != 71")
    return output


def validate(records: tuple[SourceRecord, ...], smoked_rows: list[list[str]]) -> dict[str, int]:
    by_title = {record.spec.english: record for record in records}
    expected_titles = {spec.english for spec in SOURCES}
    if set(by_title) != expected_titles:
        raise AssertionError("节日固定页集合未闭合")
    if len(FESTIVALS) != 12 or sum(festival.day_count for festival in FESTIVALS) != 18:
        raise AssertionError("节日名册或日期实例不是 12/18")

    festivals_text = record_text(by_title["Festivals"])
    missing_roster = [festival.english for festival in FESTIVALS if festival.english not in festivals_text]
    if missing_roster:
        raise AssertionError(f"节日总页名册缺失：{missing_roster}")

    required_facts = {
        "Festivals": ("four exceptions", "do not need to be fed", "remain locked all day"),
        "Egg Festival": ("9 colored eggs", "Straw Hat", "Prize Ticket", "odd-numbered years"),
        "Desert Festival": ("Calico Eggs", "15th, 16th, and 17th", "Egg Rating"),
        "Flower Dance": ("four hearts", "250 points", "Rarecrow", "After the player is married"),
        "Luau": ("potluck soup", "Friendship", "Governor"),
        "Trout Derby": ("33% chance", "first prize", "10 possible prizes", "bag's full", "shop unavailable"),
        "Dance of the Moonlight Jellies": ("28th of every", "Moonlight Jellies", '"rare" green jelly'),
        "Stardew Valley Fair": ("Grange Display", "Star Tokens", "nine items"),
        "Spirit's Eve": ("Golden Pumpkin", "odd years", "Prize Ticket"),
        "Festival of Ice": ("five fish", "Sailor's Cap", "Prize Ticket"),
        "SquidFest": ("4 tiers", "counter resets between days", "Squid Hat", "all possible rewards"),
        "Night Market": ("three days", "9 paintings", "1-5-4-2-3"),
        "Feast of the Winter Star": (
            "secret gift-giving",
            "5x the normal amount",
            "list of gifts the player can receive",
        ),
    }
    for title, phrases in required_facts.items():
        text = record_text(by_title[title])
        missing = [phrase for phrase in phrases if phrase not in text]
        if missing:
            raise AssertionError(f"{title} 节日事实缺失：{missing}")

    fair_category_rows = sum(
        table.data_rows
        for label, table in by_title["Stardew Valley Fair"].tables
        if base_section(label) == "Categories" and "wikitable" in table.classes
    )
    desert_villager_tables = sum(
        1
        for label, _ in by_title["Desert Festival"].tables
        if base_section(label) == "Villager Shops"
    )
    squid_prize_rows = sum(
        table.data_rows
        for label, table in by_title["SquidFest"].tables
        if base_section(label) == "Prizes"
    )
    feast_gift_rows = sum(
        table.data_rows
        for label, table in by_title["Feast of the Winter Star"].tables
        if base_section(label) == "Possible Received Gifts"
    )
    night_magic_tables = sum(
        1
        for label, _ in by_title["Night Market"].tables
        if base_section(label) == "Magic Shop Boat"
    )
    checks = {
        "fair_category_rows": (fair_category_rows, 552),
        "desert_villager_tables": (desert_villager_tables, 27),
        "squid_prize_rows": (squid_prize_rows, 8),
        "feast_gift_rows": (feast_gift_rows, 30),
        "night_magic_tables": (night_magic_tables, 3),
    }
    failures = {name: values for name, values in checks.items() if values[0] != values[1]}
    if failures:
        raise AssertionError(f"节日专项数量漂移：{failures}")

    fair_fish_tables = [
        table
        for label, table in by_title["Stardew Valley Fair"].tables
        if label == "Categories — Fish"
    ]
    if len(fair_fish_tables) != 1 or fair_fish_tables[0].data_rows != 71:
        raise AssertionError("展览会 Fish 分类不是 71/71")
    fair_fish_text = " ".join(cell for row in fair_fish_tables[0].rows for cell in row)
    missing_smoked_names = [row[0] for row in smoked_rows if row[0] not in fair_fish_text]
    if missing_smoked_names:
        raise AssertionError(f"烟熏鱼名册与展览会 Fish 名册不闭合：{missing_smoked_names}")

    tables = sum(len(record.tables) for record in records)
    rows = sum(table.data_rows for record in records for _, table in record.tables)
    facts = sum(len(record.facts) for record in records)
    shop_tables = sum(
        1
        for record in records
        for label, _ in record.tables
        if base_section(label) in SHOP_SECTIONS
    )
    shop_rows = sum(
        table.data_rows
        for record in records
        for label, table in record.tables
        if base_section(label) in SHOP_SECTIONS
    )
    return {
        "festivals": len(FESTIVALS),
        "date_instances": sum(festival.day_count for festival in FESTIVALS),
        "sources": len(records) + 2,
        "tables": tables,
        "rows": rows,
        "facts": facts,
        "shop_tables": shop_tables,
        "shop_rows": shop_rows,
        "fair_category_rows": fair_category_rows,
        "smoked_fish_rows": len(smoked_rows),
        "fair_complete_rows": fair_category_rows + len(smoked_rows),
        "desert_villager_tables": desert_villager_tables,
        "squid_prize_rows": squid_prize_rows,
        "feast_gift_rows": feast_gift_rows,
        "night_magic_tables": night_magic_tables,
    }


def render_document() -> str:
    records = source_records()
    smoked_rows = smoked_fish_score_rows()
    counts = validate(records, smoked_rows)
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 节日活动数据总览",
        "",
        "# 节日、比赛、奖励与商店库存数据总览（Complete Festival Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        "> 数据来源：Festivals 总页、12 个节日详情页及 Fish/Smoked Fish 补全源，共 15 个固定 revision（逐页见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷节日数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 节日 |",
        "| 数据范围 | 全部节日与钓鱼小节、实际日期、进入时间/地点、活动规则、比赛、评分、奖励、节日页明示商店库存、每日/年份轮换、概率、限购和排除条件 |",
        "| 唯一归属 | 本文是节日日期、活动规则、比赛奖励和节日库存的唯一数据源；普通商店基础库存、物品属性、NPC 礼物基础值分别留在对应数据域，本文完整保留节日页给出的覆盖、变化和例外 |",
        "| 机制解释 | 时间暂停、商店关闭、动物喂食和连续活动例外见[时间季节系统](../机制分析/时间季节系统.md#6-节日与多日活动) |",
        f"| 节日名册 | 预计 12 / 实际 {counts['festivals']} |",
        f"| 实际活动日期 | 预计 18 / 实际 {counts['date_instances']}；多日活动逐日保留 |",
        f"| 固定来源 | 节日页预计 13 / 实际 13；上游缺口补全源预计 2 / 实际 2；合计 {counts['sources']} |",
        f"| 节日源表 | {counts['tables']} 张；数据行 {counts['rows']}；规则事实块 {counts['facts']} |",
        f"| 商店库存 | 节日页明示库存表 {counts['shop_tables']} 张、库存行 {counts['shop_rows']}；随机/逐日/逐年规则同时保留 |",
        f"| 专项对账 | 沙漠节村民商店 {counts['desert_villager_tables']}/27；展览会源评分 {counts['fair_category_rows']}/552 + 烟熏鱼补全 {counts['smoked_fish_rows']}/71 = {counts['fair_complete_rows']}/623；鱿鱼节奖励层级 {counts['squid_prize_rows']}/8；冬日星回礼 {counts['feast_gift_rows']}/30；夜市魔法船逐日表 {counts['night_magic_tables']}/3 |",
        "| 数量差异 | 0 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 边界与计数说明",
        "",
        "- 12 个活动按 Festivals 总页名册计数；沙漠节 3 日、鳟鱼大赛 2 日、鱿鱼节 2 日、夜市 3 日展开后，共 18 个实际活动日期。",
        "- `商店库存`只计算 13 个固定节日页直接明示的库存行；夜市 Traveling Cart、Desert Trader 等复用普通商店池的入口与例外完整保留为规则事实，不把外部基础库存复制成第二真源。",
        "- 展览会固定页明确标注尚未加入 Smoked Fish；本文保留原 552 行分类评分，并依据 Fish 71/71 名册、Smoked Fish 定价/品质/职业公式和展览会评分阈值生成 71 行补全矩阵，不能把上游 Stub 当作已完成。",
        "- 规则型摊位台词、非台词参赛者事实与影响玩法的 Trivia/Notes 保留；纯角色闲聊、邮件、画廊、历史、Bug 和外部链接不属于活动数值字段，不计入本数据域。",
        "",
        "## 全年活动名册（12 个活动 / 18 个日期）",
        "",
    ]
    schedule = [["#", "季节日期", "中文名", "英文名", "开放/进入时间", "地点", "日期数", "详情"]]
    for index, festival in enumerate(FESTIVALS, start=1):
        schedule.append(
            [
                str(index),
                f"{festival.season}{festival.date}",
                festival.chinese,
                festival.english,
                festival.time,
                festival.location,
                str(festival.day_count),
                f"[查看](#source-{slugify(festival.english)})",
            ]
        )
    lines.extend([markdown_table(schedule), "", "## 固定来源索引", ""])

    index_rows = [["#", "来源页", "固定 revision", "数据表/数据行/事实块", "跳转"]]
    for index, record in enumerate(records, start=1):
        data_rows = sum(table.data_rows for _, table in record.tables)
        index_rows.append(
            [
                str(index),
                f"{record.spec.chinese}（{record.spec.english}）",
                str(record.spec.revision),
                f"{len(record.tables)} / {data_rows} / {len(record.facts)}",
                f"[查看](#source-{slugify(record.spec.english)})",
            ]
        )
    index_rows.extend(
        [
            ["14", "鱼类名册补全源（Fish）", str(FISH_REVISION), "71 个可烟熏鱼名", "[查看](#source-smoked-fish-supplement)"],
            ["15", "烟熏鱼公式补全源（Smoked Fish）", str(SMOKED_FISH_REVISION), "6 种职业组合×可用品质", "[查看](#source-smoked-fish-supplement)"],
        ]
    )
    lines.extend([markdown_table(index_rows), ""])

    supplement_table = [
        [
            "鱼名",
            "鱼类分区",
            "无职业 N/S/G/I：售价→分数",
            "Fisher：售价→分数",
            "Angler：售价→分数",
            "Artisan：售价→分数",
            "Fisher+Artisan：售价→分数",
            "Angler+Artisan：售价→分数",
        ]
    ]
    supplement_table.extend(smoked_rows)
    lines.extend(
        [
            '<a id="source-smoked-fish-supplement"></a>',
            "## 上游缺口补全：烟熏鱼展览会评分（71/71）",
            "",
            f"展览会 [revision 193429]({fixed_url('Stardew Valley Fair', 193429)}) 的 Categories 章节明确标记 Smoked Fish 尚未加入。本文以 [Fish revision {FISH_REVISION}]({fixed_url('Fish', FISH_REVISION)}) 的 71/71 可烟熏鱼名册和三组精确品质价格、[Smoked Fish revision {SMOKED_FISH_REVISION}]({fixed_url('Smoked Fish', SMOKED_FISH_REVISION)}) 的保留品质与 `2× / 2.8×` 职业公式补齐。",
            "",
            "每格依次为普通/银/金/铱品质的烟熏售价和展览会分数；蟹笼鱼只存在普通/银品质，金/铱格以 `—` 明示不适用。Artisan 价格按游戏整数规则 `floor(原鱼实际售价×2×1.4)` 计算。烟熏鱼在展览会中计入 Artisan Goods 分类。",
            "",
            markdown_table(supplement_table),
            "",
        ]
    )

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
                    f"### {source_index}.{len(record.tables) + 1} 非表格活动事实",
                    "",
                    markdown_table(fact_rows),
                    "",
                ]
            )

    lines.extend(["## 来源与复现", ""])
    for spec in SOURCES:
        lines.append(
            f"- [{spec.english} revision {spec.revision}]({fixed_url(spec.english, spec.revision)})：{spec.chinese}活动数据。"
        )
    lines.extend(
        [
            f"- [Fish revision {FISH_REVISION}]({fixed_url('Fish', FISH_REVISION)})：71/71 个可烟熏鱼名与无职业、Fisher、Angler 的全部可用品质精确价格。",
            f"- [Smoked Fish revision {SMOKED_FISH_REVISION}]({fixed_url('Smoked Fish', SMOKED_FISH_REVISION)})：保留品质、2× 基础售价、Artisan 2.8× 及职业叠加规则。",
        ]
    )
    lines.extend(
        [
            "- 复现：`python 采集策略/工具/生成星露谷节日数据.py --check`。",
            "",
            "[上一篇：技能属性数据总览](./技能属性数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：角色属性战斗数据总览](./角色属性战斗数据总览.md)",
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
            "节日生成审计通过：festivals=12/12, date_instances=18/18, sources=15/15, "
            "desert_villager_shops=27/27, fair_source_scores=552/552, smoked_fish=71/71, "
            "squid_prizes=8/8, feast_gifts=30/30, night_magic_days=3/3。"
        )
        return
    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    print(f"已生成 {OUTPUT.relative_to(ROOT)} ({len(expected.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
