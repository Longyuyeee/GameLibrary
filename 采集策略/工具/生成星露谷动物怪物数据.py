"""生成并审计《星露谷物语》PC v1.6.15 动物与怪物全集。

动物域：
- Animals 固定页中的 14 个农场动物变体、宠物礼物池和全部养殖规则；
- 11 个农场动物类型固定页；
- 15 个原始动物产品固定页；
- Modding:Animal data 固定页中的完整字段定义。

怪物域：
- Monsters 固定页中的普通 45、危险模式 29 个名册槽位；
- 名册所指向的 58 个唯一怪物详情固定页；
- Modding:Monster data 固定页中的 49 条 PC 1.6.15 原始记录。

详情页保留全部顶层非导航数据表和非历史事实块，避免只摘录“重要掉落”。
所有来源均固定 revision；任意名册、原始键、页面、字段或输出漂移都会失败。
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
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "牧场经营类" / "星露谷物语" / "数值数据"
ANIMAL_OUTPUT = DATA_DIR / "动物数据总览.md"
MONSTER_OUTPUT = DATA_DIR / "怪物数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-animal-monster-cache"

EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"
ANIMALS_REVISION = 193812
ANIMAL_SCHEMA_REVISION = 188878
MONSTERS_REVISION = 191503
MONSTER_RAW_REVISION = 186331
ERADICATION_REVISION = 192769
ERADICATION_TITLE = "Adventurer's Guild"


@dataclass(frozen=True)
class PageSpec:
    english: str
    chinese: str
    revision: int
    category: str


ANIMAL_PAGES = (
    PageSpec("Chicken", "鸡", 189239, "农场动物类型"),
    PageSpec("Void Chicken", "虚空鸡", 192614, "农场动物类型"),
    PageSpec("Golden Chicken", "金色的鸡", 190362, "农场动物类型"),
    PageSpec("Duck", "鸭", 182104, "农场动物类型"),
    PageSpec("Rabbit", "兔子", 190501, "农场动物类型"),
    PageSpec("Dinosaur", "恐龙", 179765, "农场动物类型"),
    PageSpec("Cow", "牛", 193886, "农场动物类型"),
    PageSpec("Goat", "山羊", 190212, "农场动物类型"),
    PageSpec("Sheep", "绵羊", 190517, "农场动物类型"),
    PageSpec("Pig", "猪", 192521, "农场动物类型"),
    PageSpec("Ostrich", "鸵鸟", 190522, "农场动物类型"),
    PageSpec("Egg", "蛋", 182342, "原始动物产品"),
    PageSpec("Large Egg", "大鸡蛋", 190366, "原始动物产品"),
    PageSpec("Void Egg", "虚空蛋", 192608, "原始动物产品"),
    PageSpec("Golden Egg", "金蛋", 191965, "原始动物产品"),
    PageSpec("Duck Egg", "鸭蛋", 193152, "原始动物产品"),
    PageSpec("Duck Feather", "鸭毛", 193328, "原始动物产品"),
    PageSpec("Wool", "动物毛", 182268, "原始动物产品"),
    PageSpec("Rabbit's Foot", "兔子的脚", 193161, "原始动物产品"),
    PageSpec("Dinosaur Egg", "恐龙蛋", 186941, "原始动物产品"),
    PageSpec("Milk", "牛奶", 190620, "原始动物产品"),
    PageSpec("Large Milk", "大壶牛奶", 193186, "原始动物产品"),
    PageSpec("Goat Milk", "羊奶", 190400, "原始动物产品"),
    PageSpec("Large Goat Milk", "大瓶羊奶", 193191, "原始动物产品"),
    PageSpec("Truffle", "松露", 192621, "原始动物产品"),
    PageSpec("Ostrich Egg", "鸵鸟蛋", 190643, "原始动物产品"),
)


MONSTER_PAGES = (
    PageSpec("Armored Bug", "甲虫", 193819, "怪物详情"),
    PageSpec("Armored Bug (dangerous)", "甲虫（危险）", 185578, "怪物详情"),
    PageSpec("Bats", "蝙蝠", 190063, "怪物详情"),
    PageSpec("Blue Squid", "蓝鱿鱼", 177009, "怪物详情"),
    PageSpec("Bug", "臭虫", 188218, "怪物详情"),
    PageSpec("Bug (dangerous)", "臭虫（危险）", 177124, "怪物详情"),
    PageSpec("Carbon Ghost", "石碳幽灵", 181888, "怪物详情"),
    PageSpec("Cave Fly", "苍蝇", 191451, "怪物详情"),
    PageSpec("Cave Fly (dangerous)", "苍蝇（危险）", 177032, "怪物详情"),
    PageSpec("Duggy", "掘地虫", 193043, "怪物详情"),
    PageSpec("Duggy (dangerous)", "掘地虫（危险）", 186857, "怪物详情"),
    PageSpec("Dust Sprite", "灰尘精灵", 185427, "怪物详情"),
    PageSpec("Dust Sprite (dangerous)", "灰尘精灵（危险）", 179507, "怪物详情"),
    PageSpec("Dwarvish Sentry", "矮人哨兵", 184231, "怪物详情"),
    PageSpec("False Magma Cap", "假熔岩菇", 190375, "怪物详情"),
    PageSpec("Ghost", "幽灵", 190352, "怪物详情"),
    PageSpec("Grub", "蛆", 190256, "怪物详情"),
    PageSpec("Grub (dangerous)", "蛆（危险）", 190438, "怪物详情"),
    PageSpec("Haunted Skull", "幽灵头骨", 190414, "怪物详情"),
    PageSpec("Haunted Skull (dangerous)", "幽灵头骨（危险）", 191278, "怪物详情"),
    PageSpec("Hot Head", "熔岩大头", 190213, "怪物详情"),
    PageSpec("Iridium Crab", "铱蟹", 193008, "怪物详情"),
    PageSpec("Iridium Golem", "铱石魔", 190303, "怪物详情"),
    PageSpec("Lava Crab", "熔岩蟹", 190295, "怪物详情"),
    PageSpec("Lava Crab (dangerous)", "熔岩蟹（危险）", 190274, "怪物详情"),
    PageSpec("Lava Lurk", "熔岩潜伏怪", 190380, "怪物详情"),
    PageSpec("Magma Duggy", "熔岩掘地虫", 190407, "怪物详情"),
    PageSpec("Magma Sparker", "熔岩火球", 191014, "怪物详情"),
    PageSpec("Magma Sprite", "熔岩精灵", 193044, "怪物详情"),
    PageSpec("Metal Head", "金属大头", 190640, "怪物详情"),
    PageSpec("Metal Head (dangerous)", "金属大头（危险）", 190503, "怪物详情"),
    PageSpec("Mummy", "木乃伊", 193376, "怪物详情"),
    PageSpec("Mummy (dangerous)", "木乃伊（危险）", 192969, "怪物详情"),
    PageSpec("Mutant Fly", "突变苍蝇", 190672, "怪物详情"),
    PageSpec("Mutant Grub", "突变蛆", 190454, "怪物详情"),
    PageSpec("Pepper Rex", "霸王喷火龙", 190502, "怪物详情"),
    PageSpec("Putrid Ghost", "腐臭幽灵", 193604, "怪物详情"),
    PageSpec("Rock Crab", "岩石蟹", 190548, "怪物详情"),
    PageSpec("Rock Crab (dangerous)", "岩石蟹（危险）", 190504, "怪物详情"),
    PageSpec("Royal Serpent", "皇家飞蛇", 190673, "怪物详情"),
    PageSpec("Serpent", "飞蛇", 190493, "怪物详情"),
    PageSpec("Shadow Brute", "暗影狂徒", 190459, "怪物详情"),
    PageSpec("Shadow Brute (dangerous)", "暗影狂徒（危险）", 190473, "怪物详情"),
    PageSpec("Shadow Shaman", "暗影萨满", 193013, "怪物详情"),
    PageSpec("Shadow Shaman (dangerous)", "暗影萨满（危险）", 190477, "怪物详情"),
    PageSpec("Shadow Sniper", "暗影狙击手", 190515, "怪物详情"),
    PageSpec("Skeleton", "骷髅", 190663, "怪物详情"),
    PageSpec("Skeleton (dangerous)", "骷髅（危险）", 190547, "怪物详情"),
    PageSpec("Skeleton Mage", "骷髅法师", 190465, "怪物详情"),
    PageSpec("Slimes", "史莱姆（怪物）", 190458, "怪物详情"),
    PageSpec("Spider", "蜘蛛", 190683, "怪物详情"),
    PageSpec("Squid Kid", "鱿鱼娃", 192734, "怪物详情"),
    PageSpec("Squid Kid (dangerous)", "鱿鱼娃（危险）", 192735, "怪物详情"),
    PageSpec("Stick Bug", "竹节虫", 192635, "怪物详情"),
    PageSpec("Stone Golem", "石魔", 192726, "怪物详情"),
    PageSpec("Stone Golem (dangerous)", "石魔（危险）", 192715, "怪物详情"),
    PageSpec("Truffle Crab", "松露蟹", 192653, "怪物详情"),
    PageSpec("Wilderness Golem", "荒野石魔", 192658, "怪物详情"),
)


@dataclass(frozen=True)
class SourceTable:
    rows: tuple[tuple[str, ...], ...]

    @property
    def width(self) -> int:
        return max((len(row) for row in self.rows), default=0)


@dataclass(frozen=True)
class PageRecord:
    spec: PageSpec
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
    payload = json.loads(result.stdout)
    html = payload["parse"]["text"]["*"]
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(html, encoding="utf-8")
    return html


def is_navigation_table(table: Tag) -> bool:
    for node in (table, *table.parents):
        if not isinstance(node, Tag):
            continue
        classes = set(node.get("class") or [])
        if any(value.startswith("navbox") for value in classes):
            return True
    text = clean_text(table.get_text(" ", strip=True))
    return text.startswith("Monsters Mines") or text.startswith("Animals and Produce")


def source_tables(html: str) -> tuple[tuple[str, SourceTable], ...]:
    soup = BeautifulSoup(html, "html.parser")
    selected: list[tuple[str, SourceTable]] = []
    for table in soup.find_all("table"):
        # 只保留叶子表；Animals 的宠物礼物表嵌套在布局表中。
        if table.find("table") is not None or is_navigation_table(table):
            continue
        grid = table_to_grid(table)
        if not any(any(cell for cell in row) for row in grid.rows):
            continue
        caption = table.find("caption", recursive=False)
        label = clean_text(caption.get_text(" ", strip=True)) if caption else ""
        first = grid.rows[0][0] if grid.rows and grid.rows[0] else ""
        if first.endswith("Gifts") or first.endswith("礼物"):
            label = first
        if not label:
            label = heading_text(table.find_previous(["h2", "h3", "h4"]))
        selected.append((label or "基本信息", grid))
    return tuple(selected)


EXCLUDED_FACT_SECTIONS = {"Contents", "History", "References", "External links"}


def fact_blocks(html: str) -> tuple[tuple[str, str], ...]:
    soup = BeautifulSoup(html, "html.parser")
    facts: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    root = soup.select_one(".mw-parser-output") or soup

    for child in root.find_all(["p", "ul", "ol", "dl", "pre"], recursive=False):
        previous = child.find_previous_sibling(["h2", "h3", "h4"])
        section = heading_text(previous) if previous is not None else "导言"
        if section in EXCLUDED_FACT_SECTIONS:
            continue
        value = clean_text(child.get_text(" / ", strip=True))
        key = (section, value)
        if value and key not in seen:
            seen.add(key)
            facts.append(key)

    for heading in soup.find_all(["h2", "h3", "h4"]):
        section = heading_text(heading)
        if section in EXCLUDED_FACT_SECTIONS:
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


def page_record(spec: PageSpec) -> PageRecord:
    html = request_html(spec.english, spec.revision)
    tables = source_tables(html)
    facts = fact_blocks(html)
    if not tables and not facts:
        raise AssertionError(f"固定页没有可保留的数据：{spec.english}")
    return PageRecord(spec, tables, facts)


def page_records(specs: tuple[PageSpec, ...]) -> tuple[PageRecord, ...]:
    # 固定页彼此独立，并发下载只缩短首次建缓存时间；map 保持清单顺序不变。
    with ThreadPoolExecutor(max_workers=8) as executor:
        return tuple(executor.map(page_record, specs))


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


def fixed_url(title: str, revision: int) -> str:
    return (
        "https://stardewvalleywiki.com/mediawiki/index.php?title="
        f"{quote(title.replace(' ', '_'), safe=':_')}&oldid={revision}"
    )


def table_body_rows(table: SourceTable) -> int:
    return max(0, len(table.rows) - 1)


def render_record_pages(lines: list[str], records: tuple[PageRecord, ...], start: int = 1) -> None:
    for index, record in enumerate(records, start=start):
        spec = record.spec
        lines.extend(
            [
                f'<a id="page-{slugify(spec.english)}"></a>',
                f"## {index}. {spec.chinese}（{spec.english}）",
                "",
                f"固定来源：[revision {spec.revision}]({fixed_url(spec.english, spec.revision)})；"
                f"保留数据表 {len(record.tables)} 张、非历史事实块 {len(record.facts)} 个。",
                "",
            ]
        )
        for table_index, (label, table) in enumerate(record.tables, start=1):
            lines.extend(
                [
                    f"### {index}.{table_index} {label}",
                    "",
                    source_table_markdown(table),
                    "",
                ]
            )
        if record.facts:
            rows = [["来源章节", "固定页事实记录"]]
            rows.extend([[section, value] for section, value in record.facts])
            lines.extend(
                [
                    f"### {index}.{len(record.tables) + 1} 非表格事实记录",
                    "",
                    markdown_table(rows),
                    "",
                ]
            )


def animal_main_counts(tables: tuple[tuple[str, SourceTable], ...]) -> tuple[int, int, int]:
    roster_labels = {"Chickens", "Ducks", "Rabbits", "Dinosaurs", "Cows", "Goats", "Sheep", "Pigs", "Ostriches"}
    gift_labels = {"Cat Gifts", "Dog Gifts", "Turtle Gifts"}
    roster = sum(table_body_rows(table) for label, table in tables if label in roster_labels)
    gift_tables = [(label, table) for label, table in tables if label in gift_labels]
    gifts = 0
    for _, table in gift_tables:
        # 每张礼物表第一行是池标题，第二行是字段标题；Cat 表另有一行注释。
        rows = list(table.rows)
        data_rows = rows[2:]
        gifts += sum(1 for row in data_rows if len(row) >= 2 and re.search(r"%$", row[-1]))
    if roster != 14:
        raise AssertionError(f"Animals 农场动物变体数量漂移：{roster} != 14")
    if len(gift_tables) != 3 or gifts != 48:
        raise AssertionError(f"宠物礼物池漂移：表 {len(gift_tables)}、条目 {gifts}")
    return roster, len(gift_tables), gifts


def render_animal_document() -> str:
    if len(ANIMAL_PAGES) != 26 or len({item.english for item in ANIMAL_PAGES}) != 26:
        raise AssertionError("动物详情页常量必须是 26 个唯一条目")
    category_counts = {
        category: sum(1 for item in ANIMAL_PAGES if item.category == category)
        for category in {item.category for item in ANIMAL_PAGES}
    }
    if category_counts != {"农场动物类型": 11, "原始动物产品": 15}:
        raise AssertionError(f"动物详情分类漂移：{category_counts}")

    main_html = request_html("Animals", ANIMALS_REVISION)
    main_tables = source_tables(main_html)
    main_facts = fact_blocks(main_html)
    roster_count, gift_pool_count, gift_row_count = animal_main_counts(main_tables)
    schema_html = request_html("Modding:Animal data", ANIMAL_SCHEMA_REVISION)
    schema_tables = source_tables(schema_html)
    schema_facts = fact_blocks(schema_html)
    records = page_records(ANIMAL_PAGES)
    table_count = sum(len(record.tables) for record in records)
    row_count = sum(table_body_rows(table) for record in records for _, table in record.tables)
    fact_count = sum(len(record.facts) for record in records)

    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 动物数据总览",
        "",
        "# 动物与动物产品数据总览（Complete Animal & Animal Product Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        f"> 数据来源：[Animals 固定页]({fixed_url('Animals', ANIMALS_REVISION)})、[Modding:Animal data 固定页]({fixed_url('Modding:Animal data', ANIMAL_SCHEMA_REVISION)})、11 个动物类型与 15 个原始产品固定页（逐条见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷动物怪物数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 动物与 Mod 产品 |",
        "| 数据范围 | 官方 Animals 页全部宠物、马、动物照料、鸡舍/畜棚动物、史莱姆屋与环境动物事实；农场动物 11 个类型页；直接产出的 15 个原始动物产品页 |",
        "| 唯一归属 | 本文是动物、原始动物产品、宠物礼物及养殖数值的唯一数据源；怪物见[怪物数据总览](./怪物数据总览.md)，加工品见[加工配方数据总览](./加工配方数据总览.md)，机制解释见[畜牧养殖系统](../机制分析/畜牧养殖系统.md) |",
        f"| 农场动物名册 | 预计 {roster_count} 个展示变体 / 实际 {roster_count}；对应 11/11 个动物类型详情页 |",
        f"| 原始动物产品 | 预计 15 / 实际 {category_counts['原始动物产品']}；每个产品页的价格、品质、来源、用途与事实块全部保留 |",
        f"| 宠物礼物 | 预计 {gift_pool_count} 个池、{gift_row_count} 条概率行 / 实际 {gift_pool_count}、{gift_row_count} |",
        "| 数量差异 | 0 |",
        f"| 字段完整率 | 26/26 个详情页；详情数据表 {table_count} 张、表体记录 {row_count} 行、非历史事实块 {fact_count} 个全部保留；Animals 与字段定义另行完整保留 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 边界与阅读说明",
        "",
        "- `14 个展示变体`按 Animals 固定页的购买/产出表逐行计数；白、棕、蓝鸡和两种牛外观分别占展示行，动物类型页按共享机制合并为 11 页。",
        "- `15 个原始动物产品`只指鸡舍/畜棚动物直接产出的独立产品页；蛋黄酱、奶酪、布料、松露油等加工品归入加工机器数据，避免重复真源。",
        "- `N/A`、`None`、`不可购买`或源页未设字段是明确的游戏边界，不是漏采；固定页的全部数据表和非历史事实块均保留为英文原始记录。",
        "",
        "## 快速索引",
        "",
    ]
    index_rows = [["#", "分类", "条目", "固定 revision", "数据表/表体行/事实块"]]
    for index, record in enumerate(records, start=1):
        rows = sum(table_body_rows(table) for _, table in record.tables)
        spec = record.spec
        index_rows.append(
            [
                str(index),
                spec.category,
                f"[{spec.chinese}（{spec.english}）](#page-{slugify(spec.english)})",
                str(spec.revision),
                f"{len(record.tables)} / {rows} / {len(record.facts)}",
            ]
        )
    lines.extend([markdown_table(index_rows), ""])

    lines.extend(["## Animals 主名册与规则原文", ""])
    for index, (label, table) in enumerate(main_tables, start=1):
        lines.extend([f"### A.{index} {label}", "", source_table_markdown(table), ""])
    if main_facts:
        rows = [["来源章节", "固定页事实记录"]]
        rows.extend([[section, value] for section, value in main_facts])
        lines.extend([f"### A.{len(main_tables) + 1} 全部非历史事实块", "", markdown_table(rows), ""])

    lines.extend(["## Animal data 字段定义", ""])
    for index, (label, table) in enumerate(schema_tables, start=1):
        lines.extend([f"### S.{index} {label}", "", source_table_markdown(table), ""])
    if schema_facts:
        rows = [["来源章节", "固定页事实记录"]]
        rows.extend([[section, value] for section, value in schema_facts])
        lines.extend([f"### S.{len(schema_tables) + 1} 非表格字段说明", "", markdown_table(rows), ""])

    render_record_pages(lines, records)
    lines.extend(
        [
            "## 来源与复现",
            "",
            f"- [Animals revision {ANIMALS_REVISION}]({fixed_url('Animals', ANIMALS_REVISION)})：动物全集入口、宠物礼物、农场动物名册与养殖规则。",
            f"- [Modding:Animal data revision {ANIMAL_SCHEMA_REVISION}]({fixed_url('Modding:Animal data', ANIMAL_SCHEMA_REVISION)})：PC 1.6 数据字段、默认值与公式定义。",
            "- 26 个详情页逐条固定 revision，正文保留来源链接；复现：`python 采集策略/工具/生成星露谷动物怪物数据.py --check`。",
            "",
            "[上一篇：制作配方数据总览](./制作配方数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：怪物数据总览](./怪物数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def monster_rosters(html: str) -> tuple[list[tuple[str, str]], list[tuple[str, str]], tuple[tuple[str, SourceTable], ...]]:
    soup = BeautifulSoup(html, "html.parser")
    tables = [table for table in soup.find_all("table") if not is_navigation_table(table)]
    if len(tables) < 5:
        raise AssertionError(f"Monsters 名册表数量漂移：{len(tables)}")

    def collect(indexes: tuple[int, ...]) -> list[tuple[str, str]]:
        result: list[tuple[str, str]] = []
        seen: set[str] = set()
        for index in indexes:
            for row in direct_rows(tables[index])[1:]:
                for link in row.find_all("a"):
                    name = clean_text(link.get_text(" ", strip=True))
                    href = link.get("href") or ""
                    if name and href.startswith("/") and name not in seen:
                        seen.add(name)
                        result.append((name, href))
        return result

    normal = collect((0, 1, 2))
    dangerous = collect((3, 4))
    roster_tables = tuple((heading_text(table.find_previous(["h2", "h3"])), table_to_grid(table)) for table in tables[:5])
    if len(normal) != 45 or len(dangerous) != 29:
        raise AssertionError(f"怪物名册槽位漂移：普通 {len(normal)}、危险 {len(dangerous)}")
    linked_titles = {
        unquote(href[1:].split("#", 1)[0]).replace("_", " ")
        for _, href in normal + dangerous
    }
    expected_titles = {spec.english for spec in MONSTER_PAGES}
    if linked_titles != expected_titles:
        raise AssertionError(
            f"怪物详情页集合未闭合：缺 {sorted(linked_titles - expected_titles)}；多 {sorted(expected_titles - linked_titles)}"
        )
    return normal, dangerous, roster_tables


RAW_MONSTER_HEADERS = (
    "生命值",
    "伤害",
    "最少金币（未实现）",
    "最多金币（未实现）",
    "飞行",
    "随机移动时长",
    "全部原始掉落 ID/概率",
    "防御",
    "抖动率",
    "追击距离阈值",
    "速度",
    "攻击落空率",
    "矿井怪物",
    "经验值",
    "显示名",
)


def raw_monster_data(html: str) -> dict[str, tuple[str, ...]]:
    soup = BeautifulSoup(html, "html.parser")
    pre = soup.find("pre")
    if pre is None:
        raise AssertionError("Modding:Monster data 缺少原始字典")
    payload = json.loads(pre.get_text(" ", strip=True))
    result: dict[str, tuple[str, ...]] = {}
    for key, value in payload.items():
        fields = tuple(str(value).split("/"))
        if len(fields) != len(RAW_MONSTER_HEADERS):
            raise AssertionError(f"怪物原始字段数漂移：{key} = {len(fields)}")
        result[str(key)] = fields
    if len(result) != 49:
        raise AssertionError(f"怪物原始键数量漂移：{len(result)} != 49")
    return result


def render_monster_document() -> str:
    if len(MONSTER_PAGES) != 58 or len({item.english for item in MONSTER_PAGES}) != 58:
        raise AssertionError("怪物详情页常量必须是 58 个唯一条目")
    roster_html = request_html("Monsters", MONSTERS_REVISION)
    normal, dangerous, roster_tables = monster_rosters(roster_html)
    raw_html = request_html("Modding:Monster data", MONSTER_RAW_REVISION)
    raw = raw_monster_data(raw_html)
    guild_html = request_html(ERADICATION_TITLE, ERADICATION_REVISION)
    eradication_tables = [
        table for label, table in source_tables(guild_html) if label == "Monster Eradication Goals"
    ]
    if len(eradication_tables) != 1 or table_body_rows(eradication_tables[0]) != 12:
        raise AssertionError(
            "怪物猎杀目标漂移："
            f"表 {len(eradication_tables)}、条目 "
            f"{table_body_rows(eradication_tables[0]) if eradication_tables else 0}"
        )
    eradication_table = eradication_tables[0]
    records = page_records(MONSTER_PAGES)
    missing_drop_fields: list[str] = []
    for record in records:
        combined = " ".join(
            [cell for _, table in record.tables for row in table.rows for cell in row]
            + [value for _, value in record.facts]
        )
        if "Drop" not in combined and "drop" not in combined:
            missing_drop_fields.append(record.spec.english)
    if missing_drop_fields:
        raise AssertionError(f"怪物详情页未找到掉落字段：{missing_drop_fields}")

    table_count = sum(len(record.tables) for record in records)
    row_count = sum(table_body_rows(table) for record in records for _, table in record.tables)
    fact_count = sum(len(record.facts) for record in records)
    unique_labels = len({name for name, _ in normal + dangerous})

    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 怪物数据总览",
        "",
        "# 怪物、危险变体与完整掉落数据总览（Complete Monster & Drop Data）",
        "",
        "> 游戏版本：星露谷物语 PC v1.6.15",
        f"> 数据来源：[Monsters 固定页]({fixed_url('Monsters', MONSTERS_REVISION)})、[Modding:Monster data 固定页]({fixed_url('Modding:Monster data', MONSTER_RAW_REVISION)})、[Adventurer's Guild 固定页]({fixed_url(ERADICATION_TITLE, ERADICATION_REVISION)})、58 个怪物详情固定页（逐条见正文）",
        "> 生成日期：2026-08-10；本文件由 `采集策略/工具/生成星露谷动物怪物数据.py` 生成，请勿手工改表。",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|---|---|",
        "| 覆盖版本 | PC v1.6.15；不含 Mod 怪物 |",
        "| 数据范围 | Monsters 固定页全部普通区域与危险模式名册；全部指向详情页；Content/Data/Monsters 原始字典全部记录与 15 个字段；逐页保留生命、伤害、防御、速度、经验、位置、全部掉落、行为与特殊规则 |",
        "| 唯一归属 | 本文是怪物名册、数值、危险变体与掉落的唯一数据源；动物见[动物数据总览](./动物数据总览.md)，战斗机制见[战斗探索系统](../机制分析/战斗探索系统.md) |",
        f"| 官方展示名册 | 普通预计 45 / 实际 {len(normal)}；危险模式预计 29 / 实际 {len(dangerous)}；合计 74 个槽位、{unique_labels} 个唯一显示名 |",
        f"| 详情固定页 | 预计 58 / 实际 {len(records)}；Bats 与 Slimes 页分别覆盖多个颜色/层级变体 |",
        f"| 原始怪物字典 | 预计 49 / 实际 {len(raw)}；每条 15/15 字段，含全部原始掉落 ID 与概率串 |",
        "| 怪物猎杀目标 | 预计 12 / 实际 12；怪物类别、数量、奖励与奖励说明 4/4 字段完整 |",
        "| 已证实旧漏项 | Iridium Golem 与 Truffle Crab 均在官方名册、详情页和快速索引中；缺失数 0 |",
        "| 数量差异 | 0 |",
        f"| 字段完整率 | 58/58 个详情页均检出掉落字段；数据表 {table_count} 张、表体记录 {row_count} 行、非历史事实块 {fact_count} 个全部保留 |",
        "| 验收状态 | **已完成** |",
        "",
        "## 计数与边界说明",
        "",
        "- `74 个槽位`按 Monsters 固定页普通区 45 与危险区 29 分别计数；Carbon Ghost 与 Lava Bat 同时出现在普通/危险环境，因此唯一显示名是 72，不应错误去重为 72 个槽位。",
        "- `58 个详情页`是 74 个名册槽位去除重复链接、同页锚点和 Bats/Slimes 聚合页后的完整来源集合；生成器要求集合严格相等。",
        "- `49 条原始记录`是 PC 1.6.15 的 Content/Data/Monsters 字典，包含 Fireball、Crow、Frog、Cat 等底层实体，也不单独枚举由代码生成的全部公开变体；所以它不能替代 74 槽位的展示名册。两层数据均完整保留。",
        "- 掉落不再使用“重要掉落”口径：原始字典的对象 ID/概率串与每个详情固定页的 Drops/Special Drops、条件、数量和备注同时保留。",
        "",
        "## 怪物快速索引",
        "",
    ]
    index_rows = [["#", "怪物页", "固定 revision", "数据表/表体行/事实块"]]
    for index, record in enumerate(records, start=1):
        rows = sum(table_body_rows(table) for _, table in record.tables)
        spec = record.spec
        index_rows.append(
            [
                str(index),
                f"[{spec.chinese}（{spec.english}）](#page-{slugify(spec.english)})",
                str(spec.revision),
                f"{len(record.tables)} / {rows} / {len(record.facts)}",
            ]
        )
    lines.extend([markdown_table(index_rows), ""])

    lines.extend(["## 官方区域与危险模式名册", ""])
    for index, (label, table) in enumerate(roster_tables, start=1):
        lines.extend([f"### R.{index} {label}", "", source_table_markdown(table), ""])

    lines.extend(
        [
            "## 怪物猎杀目标（12/12）",
            "",
            f"固定来源：[Adventurer's Guild revision {ERADICATION_REVISION}]({fixed_url(ERADICATION_TITLE, ERADICATION_REVISION)})。",
            "",
            source_table_markdown(eradication_table),
            "",
        ]
    )

    lines.extend(["## PC v1.6.15 原始怪物字典（49/49）", ""])
    raw_rows = [["内部键", *RAW_MONSTER_HEADERS]]
    raw_rows.extend([[key, *fields] for key, fields in raw.items()])
    lines.extend([markdown_table(raw_rows), ""])

    render_record_pages(lines, records)
    lines.extend(
        [
            "## 来源与复现",
            "",
            f"- [Monsters revision {MONSTERS_REVISION}]({fixed_url('Monsters', MONSTERS_REVISION)})：普通、农场、危险矿井与危险骷髅洞穴名册。",
            f"- [Modding:Monster data revision {MONSTER_RAW_REVISION}]({fixed_url('Modding:Monster data', MONSTER_RAW_REVISION)})：明确标注为 PC 1.6.15 的 49 条原始数据。",
            f"- [Adventurer's Guild revision {ERADICATION_REVISION}]({fixed_url(ERADICATION_TITLE, ERADICATION_REVISION)})：12/12 个怪物猎杀目标及全部奖励字段。",
            "- 58 个详情页逐条固定 revision，正文保留来源链接；复现：`python 采集策略/工具/生成星露谷动物怪物数据.py --check`。",
            "",
            "[上一篇：动物数据总览](./动物数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：技能属性数据总览](./技能属性数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="只校验来源与生成结果，不写文件")
    args = parser.parse_args()

    outputs = {
        ANIMAL_OUTPUT: render_animal_document(),
        MONSTER_OUTPUT: render_monster_document(),
    }
    if args.check:
        drifted = []
        for path, expected in outputs.items():
            actual = path.read_text(encoding="utf-8") if path.exists() else ""
            if actual != expected:
                drifted.append(str(path.relative_to(ROOT)))
        if drifted:
            raise SystemExit("生成文档与模板不一致：" + "、".join(drifted))
        print("动物/怪物生成审计通过：动物 14 个变体、26 个详情页；怪物 45+29 个槽位、58 个详情页、49 条原始记录。")
        return

    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"已生成 {path.relative_to(ROOT)} ({len(content.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
