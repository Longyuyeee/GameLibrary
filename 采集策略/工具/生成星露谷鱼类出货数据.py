#!/usr/bin/env python3
"""从固定 Wiki revision 生成 PC v1.6.15 鱼类与出货收集全集。

全集边界：
- 鱼类：Fish 固定页六个分区的 77 个可捕获对象；
- 鱼类图鉴：Collections 固定页的 72 个槽位；
- 可烟熏鱼：Fish 固定页除 Other Catchables 外的 71 个对象；
- 出货收集：Shipping/Collections 固定页的 154 个 Full Shipment 槽位；
- 出货成就：Polyculture 28、Monoculture 33、Full Shipment 154。

英文固定页负责 PC v1.6.15 完整性，中文固定页按同一顺序提供中文记录。
任一分区、对象、字段、集合关系、来源版本或顺序漂移都会使生成失败。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "牧场经营类" / "星露谷物语" / "数值数据"
FISH_OUTPUT = DATA_DIR / "鱼类数据总览.md"
SHIPPING_OUTPUT = DATA_DIR / "出货收集数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-fish-shipping-cache"

EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"
ZH_API = "https://zh.stardewvalleywiki.com/mediawiki/api.php"

EN_FISH_REVISION = 193885
ZH_FISH_REVISION = 55286
EN_COLLECTIONS_REVISION = 191813
ZH_COLLECTIONS_REVISION = 52128
EN_SHIPPING_REVISION = 193038
FISH_SCHEMA_REVISION = 187068


@dataclass(frozen=True)
class SectionSpec:
    english: str
    chinese: str
    chinese_label: str
    fields: tuple[str, ...]
    expected: int


COMMON_PRICE_FIELDS = ("price", "fisher", "angler")
SECTIONS = (
    SectionSpec(
        "Fishing Pole Fish",
        "常规鱼类",
        "钓竿鱼",
        (
            "name", "description", *COMMON_PRICE_FIELDS, "location", "time", "season",
            "weather", "size", "difficulty", "xp", "used",
        ),
        48,
    ),
    SectionSpec(
        "Night Market Fish",
        "夜市鱼",
        "夜市鱼",
        ("name", "description", *COMMON_PRICE_FIELDS, "size", "difficulty", "xp", "used"),
        3,
    ),
    SectionSpec(
        "Legendary Fish",
        "传说鱼类",
        "传说鱼",
        (
            "name", "description", *COMMON_PRICE_FIELDS, "location", "time", "season",
            "weather", "size", "difficulty", "xp",
        ),
        5,
    ),
    SectionSpec(
        "Legendary Fish II",
        "传说鱼类二代",
        "传说鱼二代",
        (
            "name", "description", *COMMON_PRICE_FIELDS, "location", "time", "season",
            "weather", "size", "difficulty", "xp",
        ),
        5,
    ),
    SectionSpec(
        "Crab Pot Fish",
        "蟹笼鱼类",
        "蟹笼鱼",
        (
            "name", "description", *COMMON_PRICE_FIELDS, "location", "trap_non_mariner",
            "trap_mariner", "size", "used",
        ),
        10,
    ),
    SectionSpec(
        "Other Catchables",
        "其他",
        "其他可捕获物",
        ("name", "description", "price", "location", "used"),
        6,
    ),
)


@dataclass(frozen=True)
class FishRecord:
    index: int
    section: SectionSpec
    english: dict[str, str]
    chinese: dict[str, str]
    page_url: str
    in_collection: bool
    smokable: bool


@dataclass(frozen=True)
class GridEntry:
    index: int
    table: int
    row: int
    column: int
    name: str
    page_url: str
    page_title: str


@dataclass(frozen=True)
class ShippingSlot:
    english: GridEntry
    chinese: GridEntry
    scope: str


def clean_text(value: str) -> str:
    value = re.sub(r'data-sort-value\s*=\s*"[^"]*"\s*>?', "", value)
    value = re.sub(r"\[\s*(?:edit|编辑)\s*\]", "", value, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", value).strip(" /\u00a0")


def heading_text(heading: Tag) -> str:
    headline = heading.select_one(".mw-headline")
    return clean_text((headline if isinstance(headline, Tag) else heading).get_text(" ", strip=True))


def semantic_cell_text(cell: Tag) -> str:
    clone = BeautifulSoup(str(cell), "html.parser").find(["th", "td"])
    if clone is None:
        return ""
    for unwanted in clone.find_all(["sup", "style", "script", "noscript"]):
        unwanted.decompose()
    for line_break in clone.find_all("br"):
        line_break.replace_with(NavigableString(" / "))
    for image in clone.find_all("img"):
        image.replace_with(NavigableString(" "))
    return clean_text(clone.get_text(" ", strip=True))


def request_html(api_url: str, title: str, revision: int) -> str:
    site = "zh" if api_url == ZH_API else "en"
    safe_title = re.sub(r"[^a-zA-Z0-9_-]+", "-", title).strip("-") or "page"
    cache_file = CACHE / f"{site}-{revision}-{safe_title}.html"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")
    command = [
        "curl.exe" if sys.platform == "win32" else "curl",
        "--location",
        "--silent",
        "--show-error",
        "--fail-with-body",
        "--max-time",
        "45",
        "--user-agent",
        "GameDocsAudit/2.9 (Longyuyeee/GameLibrary)",
        "--get",
        api_url,
        "--data-urlencode",
        "action=parse",
        "--data-urlencode",
        "format=json",
        "--data-urlencode",
        "formatversion=2",
        "--data-urlencode",
        f"oldid={revision}",
        "--data-urlencode",
        "prop=text",
    ]
    response = subprocess.run(command, check=True, capture_output=True)
    payload = json.loads(response.stdout.decode("utf-8"))
    html = payload["parse"]["text"]
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(html, encoding="utf-8", newline="\n")
    return html


def find_heading(soup: BeautifulSoup, tag: str, label: str) -> Tag:
    matches = [heading for heading in soup.find_all(tag) if heading_text(heading) == label]
    if len(matches) != 1:
        raise AssertionError(f"固定页章节不唯一：{tag} {label} -> {len(matches)}")
    return matches[0]


def direct_rows(table: Tag) -> list[Tag]:
    body = table.find("tbody", recursive=False)
    return (body if body is not None else table).find_all("tr", recursive=False)


def fish_wrapper(soup: BeautifulSoup, section: str) -> Tag:
    heading = find_heading(soup, "h3", section)
    node = heading.find_next_sibling()
    while node is not None and node.name not in {"h2", "h3"}:
        if isinstance(node, Tag) and node.name == "table":
            for row in direct_rows(node):
                cells = row.find_all(["th", "td"], recursive=False)
                if len(cells) >= 6 and cells[0].name == "td":
                    return node
        node = node.find_next_sibling()
    raise AssertionError(f"找不到鱼类数据表：{section}")


def parse_fish_rows(soup: BeautifulSoup, spec: SectionSpec) -> list[tuple[dict[str, str], str]]:
    table = fish_wrapper(soup, spec.english)
    output: list[tuple[dict[str, str], str]] = []
    for row in direct_rows(table):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells or cells[0].name != "td":
            continue
        if len(cells) != len(spec.fields) + 1:
            raise AssertionError(
                f"{spec.english} 字段数漂移：{len(cells) - 1}/{len(spec.fields)}"
            )
        values = {field: semantic_cell_text(cell) for field, cell in zip(spec.fields, cells[1:])}
        name_link = cells[1].find("a")
        href = name_link.get("href") if isinstance(name_link, Tag) else ""
        page_url = f"https://stardewvalleywiki.com{href}" if href and href.startswith("/") else href
        output.append((values, page_url or "—"))
    if len(output) != spec.expected:
        raise AssertionError(f"{spec.english} 对象数漂移：{len(output)}/{spec.expected}")
    return output


def parse_language_fish_rows(
    soup: BeautifulSoup, heading: str, fields: tuple[str, ...], expected: int
) -> dict[str, dict[str, str]]:
    table = fish_wrapper(soup, heading)
    output: dict[str, dict[str, str]] = {}
    for row in direct_rows(table):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells or cells[0].name != "td":
            continue
        if len(cells) != len(fields) + 1:
            raise AssertionError(f"{heading} 中文字段数漂移：{len(cells) - 1}/{len(fields)}")
        image = cells[0].find("img")
        identity = clean_text(image.get("alt") or "") if isinstance(image, Tag) else ""
        identity = re.sub(r"\.(?:png|gif|jpg|jpeg)$", "", identity, flags=re.IGNORECASE)
        identity = identity.replace("_", " ")
        if not identity or identity in output:
            raise AssertionError(f"{heading} 中文对象图像标识为空或重复：{identity}")
        output[identity] = {
            field: semantic_cell_text(cell) for field, cell in zip(fields, cells[1:])
        }
    if len(output) != expected:
        raise AssertionError(f"{heading} 中文对象数漂移：{len(output)}/{expected}")
    return output


def section_facts(soup: BeautifulSoup, heading_tag: str, label: str) -> list[str]:
    heading = find_heading(soup, heading_tag, label)
    output: list[str] = []
    node = heading.find_next_sibling()
    while node is not None and node.name not in {"h2", "h3"}:
        if isinstance(node, Tag) and node.name in {"p", "ul", "ol", "dl"}:
            value = clean_text(node.get_text(" ", strip=True))
            if value and value not in {"Page One", "Page Two", "Page Three"}:
                output.append(value)
        node = node.find_next_sibling()
    return output


def parse_grid(
    api_url: str, revision: int, title: str, heading_label: str
) -> tuple[list[GridEntry], int]:
    soup = BeautifulSoup(request_html(api_url, title, revision), "html.parser")
    heading = find_heading(soup, "h2", heading_label)
    output: list[GridEntry] = []
    table_index = 0
    node = heading.find_next_sibling()
    while node is not None and node.name != "h2":
        if isinstance(node, Tag) and node.name == "table":
            table_index += 1
            for row_index, row in enumerate(direct_rows(node), start=1):
                column_index = 0
                for cell in row.find_all("td", recursive=False):
                    column_index += 1
                    name = semantic_cell_text(cell)
                    if not name:
                        continue
                    link = cell.find("a")
                    href = link.get("href") if isinstance(link, Tag) else ""
                    page_title = link.get("title") if isinstance(link, Tag) else ""
                    if href and href.startswith("/"):
                        host = "https://zh.stardewvalleywiki.com" if api_url == ZH_API else "https://stardewvalleywiki.com"
                        href = f"{host}{href}"
                    output.append(
                        GridEntry(
                            len(output) + 1,
                            table_index,
                            row_index,
                            column_index,
                            name,
                            href or "—",
                            clean_text(page_title or "—"),
                        )
                    )
        node = node.find_next_sibling()
    return output, table_index


def grid_coordinates(entries: list[GridEntry]) -> list[tuple[int, int, int]]:
    return [(entry.table, entry.row, entry.column) for entry in entries]


def source_table(table: Tag) -> list[list[str]]:
    rows: list[list[str]] = []
    occupied: dict[tuple[int, int], str] = {}
    width = 0
    direct = direct_rows(table)
    for row_index, row in enumerate(direct):
        column = 0
        for cell in row.find_all(["th", "td"], recursive=False):
            while (row_index, column) in occupied:
                column += 1
            value = semantic_cell_text(cell)
            rowspan = int(cell.get("rowspan") or 1)
            colspan = int(cell.get("colspan") or 1)
            for row_offset in range(rowspan):
                for column_offset in range(colspan):
                    occupied[(row_index + row_offset, column + column_offset)] = value
            column += colspan
        width = max(width, column)
    height = max((row for row, _ in occupied), default=-1) + 1
    for row in range(height):
        rows.append([occupied.get((row, column), "") for column in range(width)])
    return rows


def fish_schema_tables() -> list[list[list[str]]]:
    soup = BeautifulSoup(
        request_html(EN_API, "Modding:Fish data", FISH_SCHEMA_REVISION), "html.parser"
    )
    heading = find_heading(soup, "h3", "Fish")
    tables: list[list[list[str]]] = []
    node = heading.find_next_sibling()
    while node is not None and node.name not in {"h2", "h3"}:
        if isinstance(node, Tag) and node.name == "table":
            tables.append(source_table(node))
        node = node.find_next_sibling()
    if len(tables) != 2 or [len(table) - 1 for table in tables] != [7, 14]:
        raise AssertionError(
            f"Data/Fish 字段表漂移：tables={len(tables)}, rows={[len(t) - 1 for t in tables]}"
        )
    return tables


def achievement_rosters(shipping_soup: BeautifulSoup) -> tuple[list[str], list[str], list[str]]:
    poly_heading = find_heading(shipping_soup, "h3", "Polyculture")
    polyculture: list[str] = []
    node = poly_heading.find_next_sibling()
    while node is not None and node.name not in {"h2", "h3"}:
        if isinstance(node, Tag):
            for link in node.find_all("a"):
                name = clean_text(link.get_text(" ", strip=True))
                href = link.get("href") or ""
                if name and name != "Crops" and href.startswith("/") and name not in polyculture:
                    polyculture.append(name)
        node = node.find_next_sibling()

    mono_heading = find_heading(shipping_soup, "h3", "Monoculture")
    extras: list[str] = []
    node = mono_heading.find_next_sibling()
    while node is not None and node.name not in {"h2", "h3"}:
        if isinstance(node, Tag):
            for link in node.find_all("a"):
                name = clean_text(link.get_text(" ", strip=True))
                href = link.get("href") or ""
                if name and name != "Crops" and href.startswith("/") and name not in extras:
                    extras.append(name)
        node = node.find_next_sibling()
    monoculture = [*polyculture, *(name for name in extras if name not in polyculture)]
    if len(polyculture) != 28 or len(extras) != 5 or len(monoculture) != 33:
        raise AssertionError(
            f"出货成就作物名册漂移：poly={len(polyculture)}, extras={len(extras)}, mono={len(monoculture)}"
        )
    return polyculture, extras, monoculture


def fixed_url(host: str, title: str, revision: int) -> str:
    encoded = quote(title.replace(" ", "_"), safe=":_")
    return f"{host}/mediawiki/index.php?title={encoded}&oldid={revision}"


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        raise AssertionError("不能生成空表")
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    output = ["| " + " | ".join(markdown_cell(value) for value in normalized[0]) + " |"]
    output.append("|" + "|".join("---" for _ in range(width)) + "|")
    output.extend(
        "| " + " | ".join(markdown_cell(value or "—") for value in row) + " |"
        for row in normalized[1:]
    )
    return "\n".join(output)


def pair_value(chinese: dict[str, str], english: dict[str, str], field: str) -> str:
    zh = chinese.get(field, "")
    en = english.get(field, "")
    if not zh and not en:
        return "—（该分区不适用）"
    if zh == en:
        return zh or "—"
    return f"中：{zh or '—'}<br>EN：{en or '—'}"


def english_value(english: dict[str, str], field: str) -> str:
    return english.get(field) or "—（该分区不适用）"


def build_data() -> tuple[list[FishRecord], list[ShippingSlot], dict[str, object]]:
    english_fish_soup = BeautifulSoup(
        request_html(EN_API, "Fish", EN_FISH_REVISION), "html.parser"
    )
    chinese_fish_soup = BeautifulSoup(
        request_html(ZH_API, "鱼", ZH_FISH_REVISION), "html.parser"
    )
    fish_collection_en, fish_collection_en_tables = parse_grid(
        EN_API, EN_COLLECTIONS_REVISION, "Collections", "Fish"
    )
    fish_collection_zh, fish_collection_zh_tables = parse_grid(
        ZH_API, ZH_COLLECTIONS_REVISION, "收集品", "鱼"
    )
    if len(fish_collection_en) != 72 or len(fish_collection_zh) != 72:
        raise AssertionError(
            f"鱼类图鉴槽位漂移：en={len(fish_collection_en)}, zh={len(fish_collection_zh)}"
        )
    if fish_collection_en_tables != 2 or fish_collection_zh_tables != 2:
        raise AssertionError("鱼类图鉴源表不是英文 2 张/中文 2 张")
    if grid_coordinates(fish_collection_en) != grid_coordinates(fish_collection_zh):
        raise AssertionError("鱼类图鉴中英文 72 槽位坐标不一致")
    collection_names = {entry.name for entry in fish_collection_en}
    if len(collection_names) != 72:
        raise AssertionError("鱼类图鉴英文名存在重复")

    records: list[FishRecord] = []
    for spec in SECTIONS:
        english_rows = parse_fish_rows(english_fish_soup, spec)
        chinese_rows = parse_language_fish_rows(
            chinese_fish_soup, spec.chinese, spec.fields, spec.expected
        )
        english_names = {english["name"] for english, _ in english_rows}
        if english_names != set(chinese_rows):
            raise AssertionError(
                f"{spec.english} 中英文对象集合不一致："
                f"missing_zh={sorted(english_names - set(chinese_rows))}, "
                f"extra_zh={sorted(set(chinese_rows) - english_names)}"
            )
        for english, page_url in english_rows:
            chinese = chinese_rows[english["name"]]
            records.append(
                FishRecord(
                    len(records) + 1,
                    spec,
                    english,
                    chinese,
                    page_url,
                    english["name"] in collection_names,
                    spec.english != "Other Catchables",
                )
            )
    names = [record.english["name"] for record in records]
    if len(records) != 77 or len(set(names)) != 77:
        raise AssertionError(f"鱼类全集名称不闭合：records={len(records)}, unique={len(set(names))}")
    if sum(record.in_collection for record in records) != 72:
        raise AssertionError("鱼类全集与图鉴 72 项不闭合")
    if sum(record.smokable for record in records) != 71:
        raise AssertionError("可烟熏鱼集合不是 71 项")
    missing_collection = sorted(collection_names - set(names))
    if missing_collection:
        raise AssertionError(f"图鉴存在不在鱼类全集中的对象：{missing_collection}")
    legendary_two = {
        record.english["name"]
        for record in records
        if record.section.english == "Legendary Fish II"
    }
    if legendary_two & collection_names or len(legendary_two) != 5:
        raise AssertionError("传说鱼二代与图鉴排除关系漂移")

    shipping_main, shipping_main_tables = parse_grid(
        EN_API, EN_SHIPPING_REVISION, "Shipping", "Collection"
    )
    shipping_cross, shipping_cross_tables = parse_grid(
        EN_API, EN_COLLECTIONS_REVISION, "Collections", "Items Shipped"
    )
    shipping_zh, shipping_zh_tables = parse_grid(
        ZH_API, ZH_COLLECTIONS_REVISION, "收集品", "售出 的物品（农场和采集品）"
    )
    shipping_names = [entry.name for entry in shipping_main]
    cross_names = [entry.name for entry in shipping_cross]
    if shipping_names != cross_names:
        raise AssertionError("Shipping 与 Collections 的 154 槽位顺序不一致")
    if len(shipping_main) != 154 or len(shipping_zh) != 154:
        raise AssertionError(
            f"出货收集槽位漂移：main={len(shipping_main)}, zh={len(shipping_zh)}"
        )
    if (shipping_main_tables, shipping_cross_tables, shipping_zh_tables) != (3, 3, 3):
        raise AssertionError("出货收集固定源不是 3+3+3 张表")
    shipping_coordinates = grid_coordinates(shipping_main)
    if (
        shipping_coordinates != grid_coordinates(shipping_cross)
        or shipping_coordinates != grid_coordinates(shipping_zh)
    ):
        raise AssertionError("出货收集中英文 154 槽位坐标不一致")
    slots: list[ShippingSlot] = []
    for english, chinese in zip(shipping_main, shipping_zh):
        if "(any)" in english.name:
            scope = "任意同类变体（1 个收集槽）"
        elif "(white)" in english.name or "(brown)" in english.name:
            scope = "颜色指定对象"
        else:
            scope = "指定对象"
        slots.append(ShippingSlot(english, chinese, scope))
    scope_counts = {
        scope: sum(slot.scope == scope for slot in slots)
        for scope in {slot.scope for slot in slots}
    }
    if scope_counts != {
        "指定对象": 140,
        "颜色指定对象": 4,
        "任意同类变体（1 个收集槽）": 10,
    }:
        raise AssertionError(f"出货槽位语义计数漂移：{scope_counts}")

    fish_facts: list[tuple[str, str]] = []
    for label in ("Night Market Fish", "Legendary Fish", "Legendary Fish II", "Crab Pot Fish"):
        fish_facts.extend((label, fact) for fact in section_facts(english_fish_soup, "h3", label))
    collections_soup = BeautifulSoup(
        request_html(EN_API, "Collections", EN_COLLECTIONS_REVISION), "html.parser"
    )
    fish_facts.extend(
        ("Collections / Fish", fact)
        for fact in section_facts(collections_soup, "h2", "Fish")
    )
    if len(fish_facts) != 14:
        raise AssertionError(f"鱼类规则事实块漂移：{len(fish_facts)}/14")

    shipping_soup = BeautifulSoup(
        request_html(EN_API, "Shipping", EN_SHIPPING_REVISION), "html.parser"
    )
    shipping_facts: list[tuple[str, str]] = []
    for tag, label in (
        ("h2", "Collection"),
        ("h2", "Achievements"),
        ("h3", "Polyculture"),
        ("h3", "Monoculture"),
        ("h3", "Full Shipment"),
    ):
        facts = section_facts(shipping_soup, tag, label)
        if not facts:
            raise AssertionError(f"Shipping 规则章节为空：{label}")
        shipping_facts.append((label, facts[0]))
    if len(shipping_facts) != 5:
        raise AssertionError(f"出货规则事实块漂移：{len(shipping_facts)}/5")
    polyculture, mono_extras, monoculture = achievement_rosters(shipping_soup)

    schema_tables = fish_schema_tables()
    meta: dict[str, object] = {
        "fish_facts": fish_facts,
        "shipping_facts": shipping_facts,
        "schema_tables": schema_tables,
        "polyculture": polyculture,
        "mono_extras": mono_extras,
        "monoculture": monoculture,
        "scope_counts": scope_counts,
        "fish_collection_tables": fish_collection_en_tables + fish_collection_zh_tables,
        "shipping_collection_tables": shipping_main_tables + shipping_cross_tables + shipping_zh_tables,
    }
    return records, slots, meta


def render_fish(records: list[FishRecord], meta: dict[str, object]) -> str:
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 鱼类数据总览",
        "",
        "# 鱼类、图鉴与可捕获物数据总览（Complete Fish Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        "> 完整性主源：英文 Fish 固定页；中文记录源：中文《鱼》固定页；图鉴集合由中英文 Collections 固定页交叉核对。",
        "> 本文件由 `采集策略/工具/生成星露谷鱼类出货数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 鱼类 |",
        "| 数据范围 | Fish 固定页六个可捕获对象分区；全部可读字段；鱼类图鉴成员；可烟熏成员；Data/Fish 字段语义；影响集合判定的完整规则事实 |",
        "| 固定来源 | 预计 5 / 实际 5：英文 Fish、中文鱼、英文 Collections、中文收集品、Modding:Fish data |",
        "| 可捕获对象全集 | 预计 77 / 实际 77；名称唯一 77 / 77 |",
        "| 分区对账 | 钓竿鱼 48 / 48；夜市鱼 3 / 3；传说鱼 5 / 5；传说鱼二代 5 / 5；蟹笼鱼 10 / 10；其他可捕获物 6 / 6 |",
        "| 鱼类图鉴 | 预计 72 / 实际 72；英文 2 张表与中文 2 张表顺序闭合 |",
        "| 可烟熏鱼 | 预计 71 / 实际 71；包含传说鱼二代，不含 6 个其他可捕获物 |",
        "| Data/Fish 字段语义 | 蟹笼记录 7 / 7；钓竿鱼记录 14 / 14；合计 21 / 21 |",
        "| 规则事实块 | 预计 14 / 实际 14 |",
        "| 必填字段 | 77 / 77 保留分区适用的名称、描述、三组品质价格、地点、时间、季节、天气、尺寸、难度/行为、基础经验、蟹笼概率、用途、图鉴/烟熏关系和来源 |",
        "| 数量差异 | 0 |",
        "| 未知或待核实字段 | 0；`—（该分区不适用）`是固定表结构不适用，不是缺漏 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 边界与集合关系",
        "",
        "- `77` 是固定 Fish 页六个分区的全部可捕获对象，不等于图鉴数量，也不等于可烟熏数量。",
        "- `72` 个图鉴槽位排除 5 条传说鱼二代，但包含海草、绿藻、白藻及三种凝胶；必须用钓竿或蟹笼捕获才计入，购买、采集或怪物掉落不计入。",
        "- `71` 个可烟熏对象由 48 条钓竿鱼、3 条夜市鱼、5 条传说鱼、5 条传说鱼二代和 10 条蟹笼鱼组成。",
        "- 英文固定页是 PC v1.6.15 数值裁定主源；中文页用于名称、描述、地点、时间、季节、天气、尺寸和用途本地化。中文页中的旧经验或职业价格不覆盖英文主源。",
        "- 鱼饵、钓具、鱼竿归属[道具装备数据总览](./道具装备数据总览.md)；钓鱼技能与经验公式归属[技能属性数据总览](./技能属性数据总览.md#source-fishing)。本页不复制这些对象。",
        "",
        "## 分区索引",
        "",
        "| 分区 | 对象数 | 图鉴成员 | 可烟熏 |",
        "|---|---:|---:|---:|",
    ]
    for spec in SECTIONS:
        subset = [record for record in records if record.section == spec]
        lines.append(
            f"| {spec.chinese_label} / {spec.english} | {len(subset)} | "
            f"{sum(record.in_collection for record in subset)} | {sum(record.smokable for record in subset)} |"
        )
    lines.extend(["", "## 77 / 77 可捕获对象完整字段", ""])
    rows = [[
        "# / 对象", "分区", "名称与描述", "品质售价（基础 / Fisher / Angler）", "地点与时间",
        "季节与天气", "尺寸", "难度/行为与基础 XP", "蟹笼概率", "用途", "集合关系", "对象页",
    ]]
    for record in records:
        anchor = slugify(record.english["name"])
        rows.append(
            [
                f'<a id="fish-{anchor}"></a>{record.index}',
                f"{record.section.chinese_label}<br>{record.section.english}",
                f"{pair_value(record.chinese, record.english, 'name')}<br>{pair_value(record.chinese, record.english, 'description')}",
                "N/S/G/I 基础：" + english_value(record.english, "price")
                + "<br>Fisher：" + english_value(record.english, "fisher")
                + "<br>Angler：" + english_value(record.english, "angler"),
                pair_value(record.chinese, record.english, "location")
                + "<br>时间：" + pair_value(record.chinese, record.english, "time"),
                "季节：" + pair_value(record.chinese, record.english, "season")
                + "<br>天气：" + pair_value(record.chinese, record.english, "weather"),
                pair_value(record.chinese, record.english, "size"),
                english_value(record.english, "difficulty")
                + "<br>XP：" + english_value(record.english, "xp"),
                "非水手：" + english_value(record.english, "trap_non_mariner")
                + "<br>水手：" + english_value(record.english, "trap_mariner"),
                pair_value(record.chinese, record.english, "used"),
                f"图鉴：{'是' if record.in_collection else '否'}<br>可烟熏：{'是' if record.smokable else '否'}",
                f"[英文对象页]({record.page_url})",
            ]
        )
    lines.extend([markdown_table(rows), "", "## 集合判定与特殊规则（14 / 14）", ""])
    fact_rows = [["来源章节", "完整规则事实"]]
    fact_rows.extend([list(row) for row in meta["fish_facts"]])  # type: ignore[arg-type]
    lines.extend([markdown_table(fact_rows), "", "## Data/Fish 字段语义（21 / 21）", ""])
    schema_tables: list[list[list[str]]] = meta["schema_tables"]  # type: ignore[assignment]
    lines.extend(["### 蟹笼记录字段（7 / 7）", "", markdown_table(schema_tables[0]), ""])
    lines.extend(["### 钓竿鱼记录字段（14 / 14）", "", markdown_table(schema_tables[1]), ""])
    lines.extend(
        [
            "## 固定来源与复现",
            "",
            f"- [Fish revision {EN_FISH_REVISION}]({fixed_url('https://stardewvalleywiki.com', 'Fish', EN_FISH_REVISION)})：77 个对象的完整性主源与全部可读字段。",
            f"- [中文鱼 revision {ZH_FISH_REVISION}]({fixed_url('https://zh.stardewvalleywiki.com', '鱼', ZH_FISH_REVISION)})：77 个对象的中文记录源。",
            f"- [Collections revision {EN_COLLECTIONS_REVISION}]({fixed_url('https://stardewvalleywiki.com', 'Collections', EN_COLLECTIONS_REVISION)}) 与 [中文收集品 revision {ZH_COLLECTIONS_REVISION}]({fixed_url('https://zh.stardewvalleywiki.com', '收集品', ZH_COLLECTIONS_REVISION)})：72 / 72 鱼类图鉴槽位与计入规则。",
            f"- [Modding:Fish data revision {FISH_SCHEMA_REVISION}]({fixed_url('https://stardewvalleywiki.com', 'Modding:Fish data', FISH_SCHEMA_REVISION)})：Data/Fish 21 个字段槽位语义。",
            "- 复现：`python 采集策略/工具/生成星露谷鱼类出货数据.py --check`。",
            "",
            "---",
            "",
            "[上一篇：作物数据总览](./作物数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：出货收集数据总览](./出货收集数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def render_shipping(slots: list[ShippingSlot], meta: dict[str, object]) -> str:
    scope_counts: dict[str, int] = meta["scope_counts"]  # type: ignore[assignment]
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 出货收集数据总览",
        "",
        "# 出货收集与相关成就数据总览（Complete Shipping Collection Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        "> 本页维护 Full Shipment 对应的 Shipping Collection 槽位及三个出货成就，不把“所有可放入出货箱的物品”误写成收集全集。",
        "> 本文件由 `采集策略/工具/生成星露谷鱼类出货数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 物品 |",
        "| 数据范围 | Shipping Collection 154 个固定槽位、槽位顺序、中文/英文名称、具体/颜色/任意变体语义、对象页入口，以及 Polyculture、Monoculture、Full Shipment 三个出货成就的完整名册和阈值 |",
        "| 固定来源 | 预计 3 / 实际 3：Shipping、Collections、中文收集品 |",
        "| Full Shipment 槽位 | 预计 154 / 实际 154；Shipping 与 Collections 顺序 154 / 154 一致；中文映射 154 / 154 |",
        f"| 槽位语义 | 指定对象 {scope_counts['指定对象']} / 140；颜色指定对象 {scope_counts['颜色指定对象']} / 4；任意同类变体 {scope_counts['任意同类变体（1 个收集槽）']} / 10 |",
        "| Polyculture | 必须各出货 15 个的作物预计 28 / 实际 28 |",
        "| Monoculture | 可任选并出货 300 个的作物预计 33 / 实际 33；28 个 Polyculture 作物 + 5 个额外花卉/果实 |",
        "| Full Shipment | 154 / 154 槽位各至少出货 1 个 |",
        "| 规则事实块 | 预计 5 / 实际 5 |",
        "| 必填字段 | 154 / 154：槽位号、源表坐标、中文名、英文名、变体语义、对象页目标全部非空 |",
        "| 数量差异 | 0 |",
        "| 未知或待核实字段 | 0 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 范围边界与唯一归属",
        "",
        "- 本页的 `全集` 是玩家菜单 Shipping Collection 中用于 Full Shipment/完美度判定的 154 个槽位，不是所有拥有出售价格或可进入出货箱的游戏对象。",
        "- `Honey (any)`、`Wine (any)`、`Smoked Fish (any)` 等 10 个条目各自只占一个收集槽；不同原料变体不扩张槽位数。",
        "- 作物属性归属[作物数据总览](./作物数据总览.md)，动物产品归属[动物数据总览](./动物数据总览.md)，加工结果归属[加工配方数据总览](./加工配方数据总览.md)；本页只维护出货收集身份和成就关系，避免复制第二份价格或产出表。",
        "",
        '<a id="shipping-achievements"></a>',
        "## 三个出货成就",
        "",
        "| 成就 | 条件 | 对象全集 |",
        "|---|---|---|",
        "| Polyculture | 下列 28 种作物各出货 15 个 | 28 / 28 |",
        "| Monoculture | 33 种候选作物中任意一种出货 300 个 | 33 / 33 |",
        "| Full Shipment | Shipping Collection 154 个槽位各至少出货 1 个 | 154 / 154 |",
        "",
        "### Polyculture 作物（28 / 28）",
        "",
        ", ".join(meta["polyculture"]),  # type: ignore[arg-type]
        "",
        "### Monoculture 额外候选（5 / 5）",
        "",
        ", ".join(meta["mono_extras"]),  # type: ignore[arg-type]
        "",
        '<a id="shipping-slots"></a>',
        "## Full Shipment 槽位全集（154 / 154）",
        "",
    ]
    slot_rows = [["槽位", "源表坐标", "中文名", "英文名", "槽位语义", "对象页"]]
    for slot in slots:
        anchor = slugify(slot.english.name)
        slot_rows.append(
            [
                f'<a id="shipping-{anchor}-{slot.english.index}"></a>{slot.english.index}',
                f"表 {slot.english.table} / 行 {slot.english.row} / 列 {slot.english.column}",
                slot.chinese.name,
                slot.english.name,
                slot.scope,
                f"[英文对象页]({slot.english.page_url}) / [中文对象页]({slot.chinese.page_url})",
            ]
        )
    lines.extend(
        [
            markdown_table(slot_rows),
            "",
            '<a id="shipping-facts"></a>',
            "## 出货规则事实（5 / 5）",
            "",
        ]
    )
    fact_rows = [["来源章节", "完整规则事实"]]
    fact_rows.extend([list(row) for row in meta["shipping_facts"]])  # type: ignore[arg-type]
    lines.extend(
        [
            markdown_table(fact_rows),
            "",
            "## 固定来源与复现",
            "",
            f"- [Shipping revision {EN_SHIPPING_REVISION}]({fixed_url('https://stardewvalleywiki.com', 'Shipping', EN_SHIPPING_REVISION)})：154 个主收集槽、三个出货成就、28/33 作物名册与阈值。",
            f"- [Collections revision {EN_COLLECTIONS_REVISION}]({fixed_url('https://stardewvalleywiki.com', 'Collections', EN_COLLECTIONS_REVISION)})：英文 154 槽位顺序交叉验证。",
            f"- [中文收集品 revision {ZH_COLLECTIONS_REVISION}]({fixed_url('https://zh.stardewvalleywiki.com', '收集品', ZH_COLLECTIONS_REVISION)})：中文 154 槽位映射。",
            "- 复现：`python 采集策略/工具/生成星露谷鱼类出货数据.py --check`。",
            "",
            "---",
            "",
            "[上一篇：鱼类数据总览](./鱼类数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：加工配方数据总览](./加工配方数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def build_documents() -> tuple[str, str]:
    records, slots, meta = build_data()
    return render_fish(records, meta), render_shipping(slots, meta)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只检查生成结果与当前文档是否一致")
    args = parser.parse_args()
    fish, shipping = build_documents()
    if args.check:
        failures: list[str] = []
        for path, expected in ((FISH_OUTPUT, fish), (SHIPPING_OUTPUT, shipping)):
            actual = path.read_text(encoding="utf-8") if path.exists() else ""
            if actual != expected:
                failures.append(str(path.relative_to(ROOT)))
        if failures:
            raise SystemExit(f"生成文档与模板不一致：{failures}")
    else:
        FISH_OUTPUT.write_text(fish, encoding="utf-8", newline="\n")
        SHIPPING_OUTPUT.write_text(shipping, encoding="utf-8", newline="\n")
    print(
        "鱼类/出货生成审计通过：catchables=77/77, fish_collection=72/72, "
        "smokable=71/71, fish_schema=21/21, shipping=154/154, "
        "polyculture=28/28, monoculture=33/33。"
    )


if __name__ == "__main__":
    main()
