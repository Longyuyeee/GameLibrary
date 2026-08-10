"""生成并审计《星露谷物语》PC v1.6.15 加工、烹饪与制作全集。

全集边界：
- 加工机器：官方 Equipment 固定页中 Artisan 10 台、Refining 20 台；
- 烹饪配方：Content/Data/CookingRecipes 81 条；
- 制作配方：Content/Data/CraftingRecipes 150 条。

生成器固定官方 Stardew Valley Wiki 中英文展示页和 1.6.15 原始配方页的
revision。中英文展示表负责可读字段，原始数据负责内部键、原料 ID、产物 ID、
产量与解锁条件对账。机器页保留固定 revision 中全部顶层非导航数据表和
非历史事实块。任意条目、字段、表格、顺序或 revision 漂移都会使生成失败。
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

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "牧场经营类" / "星露谷物语" / "数值数据"
PROCESSING_OUTPUT = DATA_DIR / "加工配方数据总览.md"
COOKING_OUTPUT = DATA_DIR / "烹饪配方数据总览.md"
CRAFTING_OUTPUT = DATA_DIR / "制作配方数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-processing-recipe-cache"

EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"
ZH_API = "https://zh.stardewvalleywiki.com/mediawiki/api.php"

EN_EQUIPMENT_REVISION = 192044
EN_COOKING_REVISION = 193813
ZH_COOKING_REVISION = 55288
EN_CRAFTING_REVISION = 189276
ZH_CRAFTING_REVISION = 54998
RAW_RECIPE_REVISION = 193377
EN_MACHINES_REVISION = 191352


@dataclass(frozen=True)
class MachineSpec:
    english: str
    chinese: str
    category: str
    revision: int


MACHINES = (
    MachineSpec("Bee House", "蜂房", "工匠设备", 191201),
    MachineSpec("Cask", "木桶", "工匠设备", 179542),
    MachineSpec("Cheese Press", "压酪机", "工匠设备", 183811),
    MachineSpec("Dehydrator", "烘干机", "工匠设备", 193436),
    MachineSpec("Fish Smoker", "熏鱼机", "工匠设备", 192587),
    MachineSpec("Keg", "小桶", "工匠设备", 193087),
    MachineSpec("Loom", "织布机", "工匠设备", 190254),
    MachineSpec("Mayonnaise Machine", "蛋黄酱机", "工匠设备", 190554),
    MachineSpec("Oil Maker", "产油机", "工匠设备", 190486),
    MachineSpec("Preserves Jar", "罐头瓶", "工匠设备", 190576),
    MachineSpec("Bait Maker", "鱼饵制造机", "精炼设备", 191568),
    MachineSpec("Bone Mill", "碎骨机", "精炼设备", 184986),
    MachineSpec("Charcoal Kiln", "煤炭窑", "精炼设备", 181347),
    MachineSpec("Crystalarium", "宝石复制机", "精炼设备", 191954),
    MachineSpec("Deluxe Worm Bin", "高级虫饵盒", "精炼设备", 185834),
    MachineSpec("Furnace", "熔炉", "精炼设备", 191357),
    MachineSpec("Geode Crusher", "晶球破开器", "精炼设备", 193826),
    MachineSpec("Heavy Furnace", "重型熔炉", "精炼设备", 190283),
    MachineSpec("Heavy Tapper", "重型树液采集器", "精炼设备", 190431),
    MachineSpec("Lightning Rod", "避雷针", "精炼设备", 192243),
    MachineSpec("Mushroom Log", "蘑菇树桩", "精炼设备", 191559),
    MachineSpec("Ostrich Incubator", "鸵鸟孵化器", "精炼设备", 190575),
    MachineSpec("Recycling Machine", "回收机", "精炼设备", 190496),
    MachineSpec("Seed Maker", "种子生产器", "精炼设备", 191358),
    MachineSpec("Slime Egg-Press", "史莱姆压蛋器", "精炼设备", 190521),
    MachineSpec("Slime Incubator", "史莱姆孵化器", "精炼设备", 190492),
    MachineSpec("Solar Panel", "太阳能板", "精炼设备", 190616),
    MachineSpec("Tapper", "树液采集器", "精炼设备", 193620),
    MachineSpec("Wood Chipper", "碎木机", "精炼设备", 192744),
    MachineSpec("Worm Bin", "虫饵盒", "精炼设备", 192692),
)

COOKING_ALIASES = {
    "Cheese Cauliflower": "Cheese Cauli.",
    "Cookie": "Cookies",
    "Cranberry Sauce": "Cran. Sauce",
    "Eggplant Parmesan": "Eggplant Parm.",
    "Vegetable Medley": "Vegetable Stew",
}


@dataclass(frozen=True)
class SourceTable:
    rows: tuple[tuple[str, ...], ...]

    @property
    def width(self) -> int:
        return max((len(row) for row in self.rows), default=0)


@dataclass(frozen=True)
class TableRecord:
    headers: tuple[str, ...]
    values: tuple[str, ...]


@dataclass(frozen=True)
class RecipeTable:
    category: str
    records: tuple[TableRecord, ...]


def clean_text(value: str) -> str:
    value = re.sub(r"[≈Ёж]?\s*data-sort-value=\"[^\"]*\">?", "", value)
    return re.sub(r"\s+", " ", value).strip(" /\u00a0")


def heading_text(heading: Tag | None) -> str:
    if heading is None:
        return "数据表"
    headline = heading.select_one(".mw-headline")
    text = (headline if isinstance(headline, Tag) else heading).get_text(" ", strip=True)
    text = re.sub(r"\[\s*(?:edit|编辑)\s*\]", "", text, flags=re.IGNORECASE)
    return clean_text(text)


def image_label(image: Tag) -> str:
    alt = clean_text(image.get("alt") or "")
    if not alt:
        return ""
    alt = re.sub(r"\.(?:png|gif|jpg|jpeg)$", "", alt, flags=re.IGNORECASE)
    replacements = {
        "Gold": "G",
        "Energy": "能量",
        "Health": "生命值",
        "Cooking Channel": "The Queen of Sauce",
    }
    return replacements.get(alt, alt)


def semantic_cell_text(cell: Tag) -> str:
    clone = BeautifulSoup(str(cell), "html.parser").find(["th", "td"])
    if clone is None:
        return ""
    for unwanted in clone.find_all(["sup", "style", "script", "noscript"]):
        unwanted.decompose()
    for line_break in clone.find_all("br"):
        line_break.replace_with(NavigableString(" / "))
    text_without_images = clean_text(clone.get_text(" ", strip=True))
    for image in clone.find_all("img"):
        parent = image.parent
        parent_text = clean_text(parent.get_text(" ", strip=True)) if isinstance(parent, Tag) else ""
        label = "" if parent_text else image_label(image)
        if label and re.search(rf"\b{re.escape(label)}\b", text_without_images, flags=re.IGNORECASE):
            label = ""
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


def request_html(api_url: str, title: str, revision_id: int) -> str:
    site = "zh" if api_url == ZH_API else "en"
    safe_title = re.sub(r"[^a-zA-Z0-9_-]+", "-", title).strip("-") or "page"
    cache_file = CACHE / f"{site}-{revision_id}-{safe_title}.html"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")
    command = [
        "curl.exe" if sys.platform == "win32" else "curl",
        "--location",
        "--silent",
        "--show-error",
        "--fail-with-body",
        "--max-time",
        "30",
        "--user-agent",
        "GameDocsAudit/2.9 (Longyuyeee/GameLibrary)",
        "--get",
        api_url,
        "--data-urlencode",
        "action=parse",
        "--data-urlencode",
        f"oldid={revision_id}",
        "--data-urlencode",
        "prop=text",
        "--data-urlencode",
        "format=json",
    ]
    result = subprocess.run(command, check=True, capture_output=True)
    html = json.loads(result.stdout)["parse"]["text"]["*"]
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(html, encoding="utf-8")
    return html


def combine_headers(grid: SourceTable, header_indexes: list[int]) -> tuple[str, ...]:
    headers: list[str] = []
    for column in range(grid.width):
        parts: list[str] = []
        for index in header_indexes:
            value = grid.rows[index][column]
            if value and value not in parts:
                parts.append(value)
        headers.append(" / ".join(parts) or f"字段 {column + 1}")
    return tuple(headers)


def parse_record_table(table: Tag) -> tuple[TableRecord, ...]:
    rows = direct_rows(table)
    grid = table_to_grid(table)
    data_indexes = [
        index for index, row in enumerate(rows) if row.find("td", recursive=False) is not None
    ]
    if not data_indexes:
        return ()
    header_indexes = list(range(data_indexes[0]))
    if not header_indexes:
        raise AssertionError("数据表缺少表头")
    headers = combine_headers(grid, header_indexes)
    return tuple(TableRecord(headers, grid.rows[index]) for index in data_indexes)


def top_level_tables(html: str) -> list[Tag]:
    soup = BeautifulSoup(html, "html.parser")
    return [table for table in soup.find_all("table") if table.find_parent("table") is None]


def parse_recipe_tables(html: str, kind: str) -> tuple[RecipeTable, ...]:
    tables = top_level_tables(html)
    if kind == "cooking":
        target = next(
            table
            for table in tables
            if any(
                marker in table.get_text(" ", strip=True)
                for marker in ("Recipe Source", "食谱来源")
            )
            and len(parse_record_table(table)) == 81
        )
        return (RecipeTable("Recipes", parse_record_table(target)),)
    result: list[RecipeTable] = []
    for table in tables:
        records = parse_record_table(table)
        if not records:
            continue
        headers = " ".join(records[0].headers)
        has_ingredients = "Ingredients" in headers or "材料" in headers
        has_source = "Recipe Source" in headers or "配方来源" in headers
        if not has_ingredients or not has_source:
            continue
        result.append(RecipeTable(heading_text(table.find_previous("h2")), records))
    return tuple(result)


def parse_raw_recipes(html: str) -> tuple[dict[str, str], dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    blocks = [json.loads(pre.get_text()) for pre in soup.find_all("pre")]
    if len(blocks) != 2:
        raise AssertionError(f"原始配方页应有 2 个 JSON 块，实际 {len(blocks)}")
    cooking = {str(key): str(value) for key, value in blocks[0].items()}
    crafting = {str(key): str(value) for key, value in blocks[1].items()}
    if len(cooking) != 81 or len(crafting) != 150:
        raise AssertionError(
            f"原始配方数量漂移：cooking={len(cooking)}, crafting={len(crafting)}"
        )
    return cooking, crafting


def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def field_index(headers: tuple[str, ...], needles: tuple[str, ...]) -> int:
    for index, header in enumerate(headers):
        normalized = header.lower()
        if any(needle.lower() in normalized for needle in needles):
            return index
    raise AssertionError(f"找不到字段 {needles}；现有表头 {headers}")


def record_name(record: TableRecord, language: str) -> str:
    needles = ("Name",) if language == "en" else ("名称",)
    return record.values[field_index(record.headers, needles)]


def record_field(record: TableRecord, needles: tuple[str, ...]) -> str:
    return record.values[field_index(record.headers, needles)]


def serialize_other_fields(record: TableRecord, language: str) -> str:
    exclusions = (
        ("Image", "Name", "Ingredients", "Recipe Source")
        if language == "en"
        else ("图片", "名称", "材料", "所需原料", "食谱来源", "配方来源")
    )
    parts: list[str] = []
    for header, value in zip(record.headers, record.values):
        if any(exclusion in header for exclusion in exclusions) or not value:
            continue
        parts.append(f"{header}: {value}")
    return "；".join(parts) or "—"


def page_name_to_raw_key(page_name: str, kind: str, raw: dict[str, str]) -> str:
    candidate = page_name
    if kind == "cooking":
        candidate = COOKING_ALIASES.get(candidate, candidate)
    else:
        candidate = re.sub(r" \(\d+\)$", "", candidate)
        match = re.match(r"^(Wild Seeds \([A-Za-z]+\))", candidate)
        if match:
            candidate = match.group(1)
    if candidate in raw:
        return candidate
    by_normalized = {normalize_name(key): key for key in raw}
    normalized = normalize_name(candidate)
    if normalized not in by_normalized:
        raise AssertionError(f"展示页配方无法映射到原始键：{page_name}")
    return by_normalized[normalized]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
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


def pair_recipe_tables(
    english: tuple[RecipeTable, ...], chinese: tuple[RecipeTable, ...], kind: str
) -> list[tuple[str, str, tuple[TableRecord, TableRecord]]]:
    if len(english) != len(chinese):
        raise AssertionError(
            f"{kind} 中英文分类表数量不同：{len(english)} != {len(chinese)}"
        )
    pairs: list[tuple[str, str, tuple[TableRecord, TableRecord]]] = []
    for en_table, zh_table in zip(english, chinese):
        if len(en_table.records) != len(zh_table.records):
            raise AssertionError(
                f"{kind} 分类行数不同：{en_table.category} "
                f"{len(en_table.records)} != {len(zh_table.records)}"
            )
        for en_record, zh_record in zip(en_table.records, zh_table.records):
            pairs.append((en_table.category, zh_table.category, (en_record, zh_record)))
    return pairs


def raw_fields(raw_value: str, kind: str) -> tuple[str, str, str]:
    parts = raw_value.split("/")
    if kind == "cooking":
        if len(parts) < 4:
            raise AssertionError(f"烹饪原始字段不足：{raw_value}")
        return parts[0], parts[2], parts[3]
    if len(parts) < 5:
        raise AssertionError(f"制作原始字段不足：{raw_value}")
    return parts[0], parts[2], parts[4]


def render_recipe_document(
    kind: str,
    english: tuple[RecipeTable, ...],
    chinese: tuple[RecipeTable, ...],
    raw: dict[str, str],
) -> str:
    pairs = pair_recipe_tables(english, chinese, kind)
    expected = 81 if kind == "cooking" else 150
    if len(pairs) != expected:
        raise AssertionError(f"{kind} 展示表条目数漂移：{len(pairs)} != {expected}")
    seen: set[str] = set()
    grouped: list[tuple[str, str, list[list[str]]]] = []
    group_lookup: dict[tuple[str, str], list[list[str]]] = {}
    for category_en, category_zh, (en_record, zh_record) in pairs:
        en_name = record_name(en_record, "en")
        zh_name = record_name(zh_record, "zh")
        raw_key = page_name_to_raw_key(en_name, kind, raw)
        if raw_key in seen:
            raise AssertionError(f"{kind} 重复映射原始键：{raw_key}")
        seen.add(raw_key)
        raw_ingredients, raw_yield, raw_unlock = raw_fields(raw[raw_key], kind)
        en_ingredients = record_field(en_record, ("Ingredients",))
        zh_ingredients = record_field(zh_record, ("所需原料", "材料"))
        en_source = record_field(en_record, ("Recipe Source",))
        zh_source = record_field(zh_record, ("食谱来源", "配方来源"))
        key = (category_en, category_zh)
        if key not in group_lookup:
            rows = [[
                "# / 配方",
                "所需原料（中 / EN）",
                "来源（中 / EN）",
                "展示页其余字段（中文）",
                "Display fields (EN)",
                "1.6.15 原始字段",
            ]]
            group_lookup[key] = rows
            grouped.append((category_en, category_zh, rows))
        anchor = f"recipe-{slugify(raw_key)}"
        group_lookup[key].append([
            f'<a id="{anchor}"></a>{len(seen)}. **{zh_name}**<br>{en_name}<br>内部键: `{raw_key}`',
            f"中: {zh_ingredients}<br>EN: {en_ingredients}",
            f"中: {zh_source}<br>EN: {en_source}",
            serialize_other_fields(zh_record, "zh"),
            serialize_other_fields(en_record, "en"),
            f"原料 ID×数量: `{raw_ingredients}`<br>产物 ID×数量: `{raw_yield}`<br>解锁条件: `{raw_unlock or 'none'}`",
        ])
    if seen != set(raw):
        raise AssertionError(f"{kind} 原始键未闭合：{sorted(set(raw) - seen)}")

    cooking = kind == "cooking"
    title = "烹饪配方数据总览" if cooking else "制作配方数据总览"
    en_title = "Complete Cooking Recipe Data" if cooking else "Complete Crafting Recipe Data"
    en_revision = EN_COOKING_REVISION if cooking else EN_CRAFTING_REVISION
    zh_revision = ZH_COOKING_REVISION if cooking else ZH_CRAFTING_REVISION
    page_title = "Cooking" if cooking else "Crafting"
    zh_page_title = "烹饪" if cooking else "打造"
    output_lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > " + title,
        "",
        f"# {title}（{en_title}）",
        "",
        f"> 游戏版本：星露谷物语 PC v1.6.15",
        f"> 数据来源：[英文 {page_title} 固定页](https://stardewvalleywiki.com/mediawiki/index.php?title={page_title}&oldid={en_revision})、[中文{zh_page_title}固定页](https://zh.stardewvalleywiki.com/mediawiki/index.php?oldid={zh_revision})、[PC 1.6.15 原始配方数据](https://stardewvalleywiki.com/mediawiki/index.php?title=Modding:Recipe_data&oldid={RAW_RECIPE_REVISION})",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷加工配方数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        f"| 覆盖版本 | PC v1.6.15；不含 Mod 配方 |",
        f"| 数据范围 | `Content/Data/{'CookingRecipes' if cooking else 'CraftingRecipes'}` 的全部配方；加工机器产出见[加工配方数据总览](./加工配方数据总览.md) |",
        f"| 预计条目数 | {expected}（PC 1.6.15 原始数据键） |",
        f"| 实际收录数 | {len(seen)}（中英文展示行与原始键一一映射） |",
        "| 数量差异 | 0 |",
        f"| 字段完整率 | {len(seen)}/{expected}：名称、描述、原料、产物/产量、解锁来源与条件、展示页专属数值、原始内部键全部保留 |",
        f"| 来源对账 | 英文 {expected}/{expected}；中文 {expected}/{expected}；原始数据 {expected}/{expected} |",
        "| 验收状态 | **已完成** |",
        "",
        "## 字段说明",
        "",
        "- 中文与英文展示字段按相同行序对齐；原始内部键用于消除译名、缩写与单次产量后缀造成的歧义。",
        "- `原料 ID×数量 / 产物 ID×数量 / 解锁条件` 原样保留 PC 1.6.15 数据字段；可读名称、价格、效果和来源来自固定展示页。",
        "- `—` 表示该配方类型没有该字段，并非漏采；任一原始键无法映射时生成器会直接失败。",
        "",
        "## 快速索引",
        "",
    ]
    index_rows = [["分组", "条目数", "跳转"]]
    offset = 0
    for index, (category_en, category_zh, rows) in enumerate(grouped, start=1):
        count = len(rows) - 1
        anchor = f"group-{index}"
        index_rows.append([f"{category_zh} / {category_en}", str(count), f"[查看](#{anchor})"])
        offset += count
    if offset != expected:
        raise AssertionError(f"{kind} 分类小计不等于总计：{offset}")
    output_lines.extend([markdown_table(index_rows), ""])
    for index, (category_en, category_zh, rows) in enumerate(grouped, start=1):
        output_lines.extend([
            f'<a id="group-{index}"></a>',
            f"## {index}. {category_zh} / {category_en}",
            "",
            markdown_table(rows),
            "",
        ])
    output_lines.extend([
        "## 来源与复现",
        "",
        f"- [英文 {page_title} revision {en_revision}](https://stardewvalleywiki.com/mediawiki/index.php?title={page_title}&oldid={en_revision})：英文可读字段与条目顺序。",
        f"- [中文{zh_page_title} revision {zh_revision}](https://zh.stardewvalleywiki.com/mediawiki/index.php?oldid={zh_revision})：中文名称与可读字段。",
        f"- [Modding:Recipe data revision {RAW_RECIPE_REVISION}](https://stardewvalleywiki.com/mediawiki/index.php?title=Modding:Recipe_data&oldid={RAW_RECIPE_REVISION})：明确标注为 PC 1.6.15 的原始字典。",
        "- 复现：`python 采集策略/工具/生成星露谷加工配方数据.py --check`。",
        "",
    ])
    if cooking:
        output_lines.append("[上一篇：加工配方数据总览](./加工配方数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：制作配方数据总览](./制作配方数据总览.md)")
    else:
        output_lines.append("[上一篇：烹饪配方数据总览](./烹饪配方数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：动物怪物数据总览](./动物怪物数据总览.md)")
    output_lines.append("")
    return "\n".join(output_lines)


EXCLUDED_MACHINE_SECTIONS = {
    "History",
    "References",
    "Notes",
    "Footnotes",
    "External links",
}


def machine_tables(html: str) -> list[tuple[str, SourceTable]]:
    soup = BeautifulSoup(html, "html.parser")
    selected: list[tuple[str, SourceTable]] = []
    for table in soup.find_all("table"):
        if table.find_parent("table") is not None:
            continue
        classes = set(table.get("class") or [])
        if any(value.startswith("navbox") for value in classes):
            continue
        table_text = clean_text(table.get_text(" ", strip=True))
        if (
            table_text.startswith("Equipment Artisan")
            and "Refining" in table_text
            and "Farming" in table_text
        ):
            continue
        grid = table_to_grid(table)
        if not any(any(cell for cell in row) for row in grid.rows):
            continue
        caption = table.find("caption", recursive=False)
        label = clean_text(caption.get_text(" ", strip=True)) if caption else ""
        if not label:
            label = heading_text(table.find_previous(["h2", "h3"]))
        if label == "数据表":
            label = "基本信息"
        selected.append((label, grid))
    if not selected:
        raise AssertionError("机器固定页没有可保留的数据表")
    return selected


def machine_facts(html: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    facts: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for heading in soup.find_all(["h2", "h3"]):
        section = heading_text(heading)
        if section in EXCLUDED_MACHINE_SECTIONS:
            continue
        sibling = heading.find_next_sibling()
        while sibling is not None and sibling.name not in {"h2", "h3"}:
            if sibling.name in {"p", "ul", "ol", "dl"}:
                value = clean_text(sibling.get_text(" / ", strip=True))
                key = (section, value)
                if value and key not in seen:
                    seen.add(key)
                    facts.append(key)
            sibling = sibling.find_next_sibling()
    return facts


def render_processing_document() -> tuple[str, int, int, int]:
    if len(MACHINES) != 30 or len({item.english for item in MACHINES}) != 30:
        raise AssertionError("机器全集常量必须是 30 个唯一条目")
    equipment_html = request_html(EN_API, "Equipment", EN_EQUIPMENT_REVISION)
    equipment_text = BeautifulSoup(equipment_html, "html.parser").get_text(" ", strip=True)
    missing_roster = [item.english for item in MACHINES if item.english not in equipment_text]
    if missing_roster:
        raise AssertionError(f"Equipment 固定页缺少机器：{missing_roster}")
    counts = {
        category: sum(1 for item in MACHINES if item.category == category)
        for category in {item.category for item in MACHINES}
    }
    if counts != {"工匠设备": 10, "精炼设备": 20}:
        raise AssertionError(f"机器分类数量漂移：{counts}")

    rendered: list[
        tuple[MachineSpec, list[tuple[str, SourceTable]], list[tuple[str, str]]]
    ] = []
    table_count = 0
    row_count = 0
    fact_count = 0
    for machine in MACHINES:
        html = request_html(EN_API, machine.english, machine.revision)
        tables = machine_tables(html)
        facts = machine_facts(html)
        rendered.append((machine, tables, facts))
        table_count += len(tables)
        row_count += sum(max(0, len(table.rows) - 1) for _, table in tables)
        fact_count += len(facts)

    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 加工配方数据总览",
        "",
        "# 加工与机器产出数据总览（Complete Processing Machine Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        f"> 数据来源：[Equipment 固定页](https://stardewvalleywiki.com/mediawiki/index.php?title=Equipment&oldid={EN_EQUIPMENT_REVISION})、[Modding:Machines 固定页](https://stardewvalleywiki.com/mediawiki/index.php?title=Modding:Machines&oldid={EN_MACHINES_REVISION})、30 个机器固定页（逐条见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷加工配方数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 机器 |",
        "| 数据范围 | 官方 Equipment 页的工匠设备与精炼设备；逐机保留固定页全部顶层非导航数据表和非历史事实块 |",
        "| 唯一归属 | 本文只负责机器的配方、输入、产出、时间、概率、价格等数据；烹饪和制作分别见独立全集；农场建筑与房屋升级不属于本域 |",
        "| 预计条目数 | 30 台：工匠设备 10、精炼设备 20 |",
        "| 实际收录数 | 30 台：工匠设备 10、精炼设备 20 |",
        "| 数量差异 | 0 |",
        f"| 字段完整率 | 30/30；固定页数据表 {table_count} 张、表体记录 {row_count} 行、非历史事实块 {fact_count} 个全部保留 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 配方域导航",
        "",
        "| 数据集合 | 预计/实际 | 入口 |",
        "|---|---:|---|",
        "| 加工机器 | 30/30 | 本文下方 30 台固定页记录 |",
        "| 烹饪配方 | 81/81 | [烹饪配方数据总览](./烹饪配方数据总览.md) |",
        "| 制作配方 | 150/150 | [制作配方数据总览](./制作配方数据总览.md) |",
        "| 机制解释与策略 | 不承担全集 | [加工制造系统](../机制分析/加工制造系统.md) |",
        "",
        "## 机器快速索引",
        "",
    ]
    index_rows = [["#", "分类", "机器", "固定 revision", "数据表/表体行"]]
    for index, (machine, tables, facts) in enumerate(rendered, start=1):
        rows = sum(max(0, len(table.rows) - 1) for _, table in tables)
        index_rows.append([
            str(index),
            machine.category,
            f"[{machine.chinese}（{machine.english}）](#machine-{slugify(machine.english)})",
            str(machine.revision),
            f"{len(tables)} / {rows} / 事实块 {len(facts)}",
        ])
    lines.extend([markdown_table(index_rows), ""])
    for index, (machine, tables, facts) in enumerate(rendered, start=1):
        lines.extend([
            f'<a id="machine-{slugify(machine.english)}"></a>',
            f"## {index}. {machine.chinese}（{machine.english}）",
            "",
            f"固定来源：[revision {machine.revision}](https://stardewvalleywiki.com/mediawiki/index.php?title={machine.english.replace(' ', '_')}&oldid={machine.revision})；保留数据表 {len(tables)} 张。",
            "",
        ])
        for table_index, (label, table) in enumerate(tables, start=1):
            lines.extend([
                f"### {index}.{table_index} {label}",
                "",
                source_table_markdown(table),
                "",
            ])
        if facts:
            fact_rows = [["来源章节", "固定页事实记录"]]
            fact_rows.extend([[section, value] for section, value in facts])
            lines.extend([
                f"### {index}.{len(tables) + 1} 非表格事实记录",
                "",
                markdown_table(fact_rows),
                "",
            ])
    lines.extend([
        "## 来源、边界与复现",
        "",
        f"- [Equipment revision {EN_EQUIPMENT_REVISION}](https://stardewvalleywiki.com/mediawiki/index.php?title=Equipment&oldid={EN_EQUIPMENT_REVISION}) 定义 10 台工匠设备与 20 台精炼设备的全集。",
        f"- [Modding:Machines revision {EN_MACHINES_REVISION}](https://stardewvalleywiki.com/mediawiki/index.php?title=Modding:Machines&oldid={EN_MACHINES_REVISION}) 解释 PC 1.6 的机器输入、输出、条件、概率、品质和价格修正规则。",
        "- 30 个逐机固定 revision 是可读字段与表格的直接来源；正文每台机器均有独立链接。",
        "- 建筑造价、房屋升级、法师塔建筑不再混入加工数据；后续在建筑/升级唯一数据域中完成对账。",
        "- 复现：`python 采集策略/工具/生成星露谷加工配方数据.py --check`。",
        "",
        "[上一篇：作物数据总览](./作物数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：烹饪配方数据总览](./烹饪配方数据总览.md)",
        "",
    ])
    return "\n".join(lines), table_count, row_count, fact_count


def write_or_check(path: Path, content: str, check: bool) -> None:
    if check:
        if not path.exists():
            raise AssertionError(f"缺少生成文件：{path.relative_to(ROOT)}")
        existing = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        if existing != content.replace("\r\n", "\n"):
            raise AssertionError(f"生成文件与模板不一致：{path.relative_to(ROOT)}")
        return
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只核验生成文件")
    args = parser.parse_args()

    raw_html = request_html(EN_API, "Modding:Recipe data", RAW_RECIPE_REVISION)
    cooking_raw, crafting_raw = parse_raw_recipes(raw_html)
    cooking_en = parse_recipe_tables(
        request_html(EN_API, "Cooking", EN_COOKING_REVISION), "cooking"
    )
    cooking_zh = parse_recipe_tables(
        request_html(ZH_API, "烹饪", ZH_COOKING_REVISION), "cooking"
    )
    crafting_en = parse_recipe_tables(
        request_html(EN_API, "Crafting", EN_CRAFTING_REVISION), "crafting"
    )
    crafting_zh = parse_recipe_tables(
        request_html(ZH_API, "打造", ZH_CRAFTING_REVISION), "crafting"
    )

    processing, machine_tables_count, machine_rows, machine_facts_count = (
        render_processing_document()
    )
    cooking = render_recipe_document(
        "cooking", cooking_en, cooking_zh, cooking_raw
    )
    crafting = render_recipe_document(
        "crafting", crafting_en, crafting_zh, crafting_raw
    )
    write_or_check(PROCESSING_OUTPUT, processing, args.check)
    write_or_check(COOKING_OUTPUT, cooking, args.check)
    write_or_check(CRAFTING_OUTPUT, crafting, args.check)
    print(
        "generation: machines=30/30 "
        f"(tables={machine_tables_count}, rows={machine_rows}, facts={machine_facts_count}), "
        "cooking=81/81 (en=81, zh=81, raw=81), "
        "crafting=150/150 (en=150, zh=150, raw=150)"
    )


if __name__ == "__main__":
    main()
