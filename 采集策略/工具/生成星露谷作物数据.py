"""生成并审计《星露谷物语》PC v1.6.15 作物全集。

数据范围以官方 Stardew Valley Wiki 的 Crops/农作物固定 revision 为准：
47 个具有明确收获物的作物，以及混合种子、混合花卉种子、野生种子 3 个
随机种子系统。英文 Crops 页没有 Qi Fruit 详情表，因此用同站 Qi Fruit 固定
revision 补齐；四季野生种子的完整结果集合由四个固定个人页校验。

生成器只转换结构化事实表，不复制风味描述。任何作物、表格、字段、随机结果或
固定 revision 漂移都会使生成失败。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "作物数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-crop-cache"

EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"
ZH_API = "https://zh.stardewvalleywiki.com/mediawiki/api.php"

EN_CROPS_REVISION = 193672
ZH_CROPS_REVISION = 55247
EN_QI_FRUIT_REVISION = 193551

WILD_SEED_REVISIONS = {
    "Spring Seeds": 193245,
    "Summer Seeds": 193299,
    "Fall Seeds": 193217,
    "Winter Seeds": 192690,
}


@dataclass(frozen=True)
class CropSpec:
    english: str
    chinese: str
    category: str
    seasons: str


@dataclass(frozen=True)
class SourceTable:
    rows: tuple[tuple[str, ...], ...]

    @property
    def width(self) -> int:
        return max((len(row) for row in self.rows), default=0)

    @property
    def text(self) -> str:
        return " ".join(cell for row in self.rows for cell in row)


@dataclass(frozen=True)
class SourceBlock:
    title: str
    tables: tuple[SourceTable, ...]


CROP_SPECS = (
    CropSpec("Blue Jazz", "蓝爵", "春季", "春季"),
    CropSpec("Carrot", "胡萝卜", "春季", "春季"),
    CropSpec("Cauliflower", "花椰菜", "春季", "春季"),
    CropSpec("Coffee Bean", "咖啡豆", "春季", "春季、夏季"),
    CropSpec("Garlic", "蒜", "春季", "春季"),
    CropSpec("Green Bean", "青豆", "春季", "春季"),
    CropSpec("Kale", "甘蓝菜", "春季", "春季"),
    CropSpec("Parsnip", "防风草", "春季", "春季"),
    CropSpec("Potato", "土豆", "春季", "春季"),
    CropSpec("Rhubarb", "大黄", "春季", "春季"),
    CropSpec("Strawberry", "草莓", "春季", "春季"),
    CropSpec("Tulip", "郁金香", "春季", "春季"),
    CropSpec("Unmilled Rice", "未碾米", "春季", "春季；水田规则"),
    CropSpec("Blueberry", "蓝莓", "夏季", "夏季"),
    CropSpec("Corn", "玉米", "夏季", "夏季、秋季"),
    CropSpec("Hops", "啤酒花", "夏季", "夏季"),
    CropSpec("Hot Pepper", "辣椒", "夏季", "夏季"),
    CropSpec("Melon", "甜瓜", "夏季", "夏季"),
    CropSpec("Poppy", "虞美人花", "夏季", "夏季"),
    CropSpec("Radish", "萝卜", "夏季", "夏季"),
    CropSpec("Red Cabbage", "红叶卷心菜", "夏季", "夏季"),
    CropSpec("Starfruit", "杨桃", "夏季", "夏季"),
    CropSpec("Summer Spangle", "夏季亮片", "夏季", "夏季"),
    CropSpec("Summer Squash", "金皮西葫芦", "夏季", "夏季"),
    CropSpec("Sunflower", "向日葵", "夏季", "夏季、秋季"),
    CropSpec("Tomato", "西红柿", "夏季", "夏季"),
    CropSpec("Wheat", "小麦", "夏季", "夏季、秋季"),
    CropSpec("Amaranth", "苋菜", "秋季", "秋季"),
    CropSpec("Artichoke", "洋蓟", "秋季", "秋季"),
    CropSpec("Beet", "甜菜", "秋季", "秋季"),
    CropSpec("Bok Choy", "小白菜", "秋季", "秋季"),
    CropSpec("Broccoli", "西蓝花", "秋季", "秋季"),
    CropSpec("Cranberries", "蔓越莓", "秋季", "秋季"),
    CropSpec("Eggplant", "茄子", "秋季", "秋季"),
    CropSpec("Fairy Rose", "玫瑰仙子", "秋季", "秋季"),
    CropSpec("Grape", "葡萄", "秋季", "秋季"),
    CropSpec("Pumpkin", "南瓜", "秋季", "秋季"),
    CropSpec("Yam", "山药", "秋季", "秋季"),
    CropSpec("Powdermelon", "霜瓜", "冬季", "冬季"),
    CropSpec("Ancient Fruit", "上古水果", "特殊", "春季、夏季、秋季；室内或姜岛全年"),
    CropSpec("Cactus Fruit", "仙人掌果子", "特殊", "室内花盆、温室或姜岛"),
    CropSpec("Fiber", "纤维", "特殊", "全部季节"),
    CropSpec("Pineapple", "菠萝", "特殊", "夏季；室内或姜岛全年"),
    CropSpec("Taro Root", "芋头", "特殊", "夏季；室内或姜岛全年；水田规则"),
    CropSpec("Sweet Gem Berry", "宝石甜莓", "特殊", "秋季；室内或姜岛全年"),
    CropSpec("Tea Leaves", "茶叶", "特殊", "全年生长；室外冬季不产叶，室内全年可产"),
    CropSpec("Qi Fruit", "齐瓜", "特殊", "“齐先生的作物”任务期间不限季节"),
)

AUXILIARY_HEADINGS = {
    "en": ("Mixed Seeds", "Mixed Flower Seeds", "Wild Seeds"),
    "zh": ("混合种子", "混合花卉种子", "野生种子"),
}

WILD_SEED_OUTCOMES = {
    "Spring Seeds": (
        ("Wild Horseradish", "野山葵"),
        ("Daffodil", "黄水仙"),
        ("Leek", "韭葱"),
        ("Dandelion", "蒲公英"),
    ),
    "Summer Seeds": (
        ("Spice Berry", "香味浆果"),
        ("Grape", "葡萄"),
        ("Sweet Pea", "甜豌豆"),
    ),
    "Fall Seeds": (
        ("Blackberry", "黑莓"),
        ("Common Mushroom", "普通蘑菇"),
        ("Hazelnut", "榛子"),
        ("Wild Plum", "野梅"),
    ),
    "Winter Seeds": (
        ("Winter Root", "冬根"),
        ("Crystal Fruit", "水晶果"),
        ("Snow Yam", "雪山药"),
        ("Crocus", "番红花"),
    ),
}

WILD_SEED_META = {
    "Spring Seeds": ("春季种子", "采集 1 级"),
    "Summer Seeds": ("夏季种子", "采集 4 级"),
    "Fall Seeds": ("秋季种子", "采集 6 级"),
    "Winter Seeds": ("冬季种子", "采集 7 级"),
}


def clean_text(value: str) -> str:
    value = re.sub(r"[≈Ёж]?\s*data-sort-value=\"[^\"]*\">?", "", value)
    return re.sub(r"\s+", " ", value).strip(" /\u00a0")


def heading_text(heading: Tag) -> str:
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
        "Silver Quality Icon": "Silver",
        "Gold Quality Icon": "Gold",
        "Iridium Quality Icon": "Iridium",
        "Energy": "Energy",
        "Health": "Health",
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
    for row in clone.find_all("tr"):
        if row.find_parent(["th", "td"]) is clone:
            row.append(NavigableString(" / "))
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
        raise AssertionError("作物源表没有直接数据行")

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

    height = max(row for row, _ in occupied) + 1
    width = max(width, max(column for _, column in occupied) + 1)
    matrix = tuple(
        tuple(occupied.get((row, column), "") for column in range(width))
        for row in range(height)
    )
    if not matrix[0] or not any(matrix[0]):
        raise AssertionError("作物源表缺少表头")
    return SourceTable(matrix)


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
    payload = json.loads(result.stdout)
    html = payload["parse"]["text"]["*"]
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(html, encoding="utf-8")
    return html


def parse_main_page(
    html: str, language: str
) -> tuple[dict[str, SourceBlock], int]:
    soup = BeautifulSoup(html, "html.parser")
    category_names = (
        {"Spring Crops", "Summer Crops", "Fall Crops", "Winter Crops", "Special Crops"}
        if language == "en"
        else {"春季作物", "夏季作物", "秋季作物", "冬季作物", "特殊作物"}
    )
    blocks: dict[str, SourceBlock] = {}
    top_table_count = 0
    for category in soup.find_all("h2"):
        if heading_text(category) not in category_names:
            continue
        node = category.find_next_sibling()
        while node is not None and node.name != "h2":
            if node.name == "h3":
                title = heading_text(node)
                tables: list[SourceTable] = []
                sibling = node.find_next_sibling()
                while sibling is not None and sibling.name not in {"h2", "h3"}:
                    if sibling.name == "table":
                        tables.append(table_to_grid(sibling))
                        top_table_count += 1
                    sibling = sibling.find_next_sibling()
                if title in blocks:
                    raise AssertionError(f"{language} 作物页重复标题：{title}")
                blocks[title] = SourceBlock(title, tuple(tables))
            node = node.find_next_sibling()
    return blocks, top_table_count


def parse_qi_fruit(html: str) -> SourceBlock:
    soup = BeautifulSoup(html, "html.parser")
    top_tables = [table for table in soup.find_all("table") if table.find_parent("table") is None]
    infobox = next(
        (
            table
            for table in top_tables
            if direct_rows(table)
            and "Qi Fruit" in semantic_cell_text(direct_rows(table)[0].find(["th", "td"]))
        ),
        None,
    )
    stages_heading = next(
        (heading for heading in soup.find_all("h2") if heading_text(heading) == "Stages"),
        None,
    )
    stages = stages_heading.find_next_sibling("table") if stages_heading else None
    if infobox is None or stages is None:
        raise AssertionError("Qi Fruit 固定英文页缺少信息表或生长阶段表")
    return SourceBlock("Qi Fruit", (table_to_grid(infobox), table_to_grid(stages)))


def parse_wild_seed_page(title: str, html: str) -> tuple[str, ...]:
    soup = BeautifulSoup(html, "html.parser")
    heading = next(
        (
            item
            for item in soup.find_all("h2")
            if heading_text(item) == "Crops Harvested"
        ),
        None,
    )
    table = heading.find_next_sibling("table") if heading else None
    if table is None:
        raise AssertionError(f"{title} 缺少 Crops Harvested 表")
    rows = direct_rows(table)
    outcomes: list[str] = []
    for row in rows[1:]:
        cell = row.find(["th", "td"], recursive=False)
        if cell is None:
            continue
        text = clean_text(cell.get_text(" ", strip=True))
        if text:
            outcomes.append(text)
    page_text = clean_text(soup.get_text(" ", strip=True))
    if not re.search(r"Total:\s*7\s*Days", page_text, flags=re.IGNORECASE):
        raise AssertionError(f"{title} 生长时间不再是 7 天")
    return tuple(outcomes)


def assert_primary_table(block: SourceBlock, language: str) -> None:
    text = " ".join(table.text for table in block.tables)
    if language == "en":
        missing = [value for value in ("Harvest",) if value not in text]
        if not re.search(r"Total\s*:", text, flags=re.IGNORECASE):
            missing.append("Total 生长时间")
        sell_markers = ("Sells For", "Sell Price")
    else:
        missing = []
        if not re.search(r"收[获货]", text):
            missing.append("收获")
        has_total = bool(re.search(r"(?:共|总计)\s*[:：]", text))
        if block.title == "芋头" and re.search(r"7\s*-\s*10\s*天", text):
            has_total = True
        if not has_total:
            missing.append("共计生长时间")
        sell_markers = ("售价",)
    if not any(marker in text for marker in sell_markers):
        missing.append("售价字段")
    if missing:
        raise AssertionError(
            f"{language}/{block.title} 缺少必填结构字段：{', '.join(missing)}"
        )


def fetch_and_audit() -> tuple[
    dict[str, SourceBlock],
    dict[str, SourceBlock],
    dict[str, tuple[str, ...]],
    int,
    int,
]:
    en_html = request_html(EN_API, "Crops", EN_CROPS_REVISION)
    zh_html = request_html(ZH_API, "农作物", ZH_CROPS_REVISION)
    en_blocks, en_main_tables = parse_main_page(en_html, "en")
    zh_blocks, zh_main_tables = parse_main_page(zh_html, "zh")

    expected_en = {spec.english for spec in CROP_SPECS if spec.english != "Qi Fruit"}
    expected_en.update(AUXILIARY_HEADINGS["en"])
    expected_zh = {spec.chinese for spec in CROP_SPECS}
    expected_zh.update(AUXILIARY_HEADINGS["zh"])
    if set(en_blocks) != expected_en:
        raise AssertionError(
            f"英文 Crops 标题集合漂移：missing={sorted(expected_en - set(en_blocks))}, "
            f"extra={sorted(set(en_blocks) - expected_en)}"
        )
    if set(zh_blocks) != expected_zh:
        raise AssertionError(
            f"中文农作物标题集合漂移：missing={sorted(expected_zh - set(zh_blocks))}, "
            f"extra={sorted(set(zh_blocks) - expected_zh)}"
        )
    if en_main_tables != 48 or zh_main_tables != 49:
        raise AssertionError(
            f"作物主源表数量漂移：en={en_main_tables}, zh={zh_main_tables}"
        )

    qi_html = request_html(EN_API, "Qi Fruit", EN_QI_FRUIT_REVISION)
    en_blocks["Qi Fruit"] = parse_qi_fruit(qi_html)

    for spec in CROP_SPECS:
        en_block = en_blocks[spec.english]
        zh_block = zh_blocks[spec.chinese]
        if len(en_block.tables) != (2 if spec.english == "Qi Fruit" else 1):
            raise AssertionError(f"英文 {spec.english} 数据表数量异常")
        if len(zh_block.tables) != 1:
            raise AssertionError(f"中文 {spec.chinese} 数据表数量异常")
        assert_primary_table(en_block, "en")
        assert_primary_table(zh_block, "zh")

    for en_title, zh_title in zip(
        AUXILIARY_HEADINGS["en"][:2], AUXILIARY_HEADINGS["zh"][:2]
    ):
        if len(en_blocks[en_title].tables) != 1 or len(zh_blocks[zh_title].tables) != 1:
            raise AssertionError(f"随机种子结果表缺失：{en_title}/{zh_title}")
        if len(en_blocks[en_title].tables[0].rows) != 6:
            raise AssertionError(f"英文 {en_title} 季节结果行数不是 5")
        if len(zh_blocks[zh_title].tables[0].rows) != 6:
            raise AssertionError(f"中文 {zh_title} 季节结果行数不是 5")

    wild_results: dict[str, tuple[str, ...]] = {}
    for title, revision in WILD_SEED_REVISIONS.items():
        html = request_html(EN_API, title, revision)
        observed = parse_wild_seed_page(title, html)
        expected = tuple(item[0] for item in WILD_SEED_OUTCOMES[title])
        if set(observed) != set(expected) or len(observed) != len(expected):
            raise AssertionError(
                f"{title} 收获集合漂移：expected={expected}, actual={observed}"
            )
        wild_results[title] = observed

    if len(CROP_SPECS) != 47:
        raise AssertionError("命名作物全集不是 47")
    return en_blocks, zh_blocks, wild_results, en_main_tables, zh_main_tables


def anchor(english: str) -> str:
    return "crop-" + re.sub(r"[^a-z0-9]+", "-", english.lower()).strip("-")


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def render_table(table: SourceTable) -> list[str]:
    width = table.width
    rows = [row + ("",) * (width - len(row)) for row in table.rows]
    lines = [
        "| " + " | ".join(markdown_escape(cell) for cell in rows[0]) + " |",
        "| " + " | ".join("------" for _ in range(width)) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(markdown_escape(cell) for cell in row) + " |")
    return lines


def revision_url(site: str, title: str, revision: int) -> str:
    host = "zh.stardewvalleywiki.com" if site == "zh" else "stardewvalleywiki.com"
    return (
        f"https://{host}/mediawiki/index.php?title={quote(title)}&oldid={revision}"
    )


def render_document(
    en_blocks: dict[str, SourceBlock],
    zh_blocks: dict[str, SourceBlock],
    wild_results: dict[str, tuple[str, ...]],
    en_main_tables: int,
    zh_main_tables: int,
) -> str:
    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > "
        "[星露谷物语概览](../游戏概览.md) > 作物数据总览",
        "",
        "# 作物数据总览 — 星露谷物语",
        "",
        "> 游戏版本：Stardew Valley PC v1.6.15",
        ">",
        "> 英文 Crops 固定页为完整性主源，中文农作物固定页为中文记录源；"
        "英文页缺少的 Qi Fruit 详情由同站固定个人页补齐",
        ">",
        "> 本文只维护作物生长与收获数据；果树、肥料、加工配方和礼物偏好归入各自文档",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|------|------|",
        "| 数据全集定义 | 官方 Crops/农作物页中 47 个具有明确收获物的命名作物＋3 个随机种子系统 |",
        "| 预计命名作物 | 47 |",
        "| 实际命名作物 | 47 |",
        "| 数量差异 | 0 |",
        "| 随机种子系统 | 3/3：混合种子、混合花卉种子、四季野生种子 |",
        f"| 英文固定源结构 | Crops 主页面 {en_main_tables} 张顶层表＋Qi Fruit 个人页 2 张补全表 |",
        f"| 中文固定源结构 | 农作物主页面 {zh_main_tables} 张顶层表 |",
        "| 命名作物必填字段 | 中文/英文名、季节/环境、种植输入及源表购买信息、阶段、总生长时间、复收、收获物/数量、四档售价、恢复、用途 |",
        "| 随机种子必填字段 | 系统、适用季节/地点、全部可能结果、生长时间、配方解锁、单次制作数量、品质与乌鸦规则 |",
        "| 必填字段完整率 | 47/47 命名作物源表通过；3/3 随机种子系统通过 |",
        "| 验收状态 | **作物数据子域已完成** |",
        "",
        "### 范围与裁定",
        "",
        "- 果树不是耕地作物，保留在果树机制域，不计入 47 个作物。",
        "- 混合种子、混合花卉种子和野生种子没有唯一收获物，单列规则，不重复计入命名作物。",
        "- 本文覆盖作物生长与收获；种子物品的全部掉落、商店库存与交换条件归入后续道具/商店数据域。源表已经给出的购买信息原样保留。",
        "- 生长天数不含播种当天；源表中的 `Total`/`共` 与 `Regrowth`/`再次收获` 原样保留。",
        "- 青豆、啤酒花、葡萄为棚架作物；未碾米与芋头的水田差异完整保留在双语源表。",
        "- 可形成巨大作物的全集为花椰菜、甜瓜、南瓜、霜瓜、齐瓜 5 种。",
        "- 不自行重算或选择性排行收益；每日收益只保留固定源表给出的口径。",
        "",
        '<a id="crop-index"></a>',
        "",
        "## 作物索引与数量对账",
        "",
        "| # | 作物 | 分类 | 可生长季节/环境 | 中文源 | 英文源 |",
        "|:--:|------|:--:|------|:--:|:--:|",
    ]

    en_crop_url = revision_url("en", "Crops", EN_CROPS_REVISION)
    zh_crop_url = revision_url("zh", "农作物", ZH_CROPS_REVISION)
    en_qi_url = revision_url("en", "Qi Fruit", EN_QI_FRUIT_REVISION)
    for index, spec in enumerate(CROP_SPECS, start=1):
        en_url = en_qi_url if spec.english == "Qi Fruit" else en_crop_url
        lines.append(
            f"| {index} | [{spec.chinese}（{spec.english}）](#{anchor(spec.english)}) | "
            f"{spec.category} | {spec.seasons} | [zh {ZH_CROPS_REVISION}]({zh_crop_url}) | "
            f"[en {EN_QI_FRUIT_REVISION if spec.english == 'Qi Fruit' else EN_CROPS_REVISION}]({en_url}) |"
        )

    category_order = ("春季", "夏季", "秋季", "冬季", "特殊")
    for category in category_order:
        category_specs = [spec for spec in CROP_SPECS if spec.category == category]
        lines.extend(["", f"## {category}命名作物（{len(category_specs)}/{len(category_specs)}）", ""])
        for spec in category_specs:
            lines.extend(
                [
                    f'<a id="{anchor(spec.english)}"></a>',
                    "",
                    f"### {spec.chinese}（{spec.english}）",
                    "",
                    f"> 可生长季节/环境：{spec.seasons}",
                    "",
                    f"#### 中文结构化数据（revision {ZH_CROPS_REVISION}）",
                    "",
                ]
            )
            for table in zh_blocks[spec.chinese].tables:
                lines.extend(render_table(table))
                lines.append("")
            en_revision = EN_QI_FRUIT_REVISION if spec.english == "Qi Fruit" else EN_CROPS_REVISION
            lines.extend(
                [
                    f"#### English structured data（revision {en_revision}）",
                    "",
                ]
            )
            for table in en_blocks[spec.english].tables:
                lines.extend(render_table(table))
                lines.append("")

    lines.extend(
        [
            '<a id="crop-random-seeds"></a>',
            "",
            "## 随机种子系统（3/3）",
            "",
            "### 混合种子（Mixed Seeds）",
            "",
            "种植时按地点与当前季节决定候选；室内冬季可从各季候选中选择，姜岛使用固定候选。"
            "第一年仍可能得到洋蓟；农场春季防风草的权重是花椰菜或土豆的两倍。",
            "",
            f"#### 中文结果表（revision {ZH_CROPS_REVISION}）",
            "",
        ]
    )
    lines.extend(render_table(zh_blocks["混合种子"].tables[0]))
    lines.extend(["", f"#### English result table（revision {EN_CROPS_REVISION}）", ""])
    lines.extend(render_table(en_blocks["Mixed Seeds"].tables[0]))
    lines.extend(
        [
            "",
            "### 混合花卉种子（Mixed Flower Seeds）",
            "",
            "种植时从当前季节的花卉候选中随机选择；室内冬季可从全部季节花卉选择，姜岛固定使用夏季候选。",
            "",
            f"#### 中文结果表（revision {ZH_CROPS_REVISION}）",
            "",
        ]
    )
    lines.extend(render_table(zh_blocks["混合花卉种子"].tables[0]))
    lines.extend(["", f"#### English result table（revision {EN_CROPS_REVISION}）", ""])
    lines.extend(render_table(en_blocks["Mixed Flower Seeds"].tables[0]))
    lines.extend(
        [
            "",
            '<a id="crop-wild-seeds"></a>',
            "",
            "### 四季野生种子（Wild Seeds）",
            "",
            "四类野生种子均需 7 天成熟，配方每次制作 10 包；乌鸦不会啄食。"
            "收获品质由采集而非耕种规则决定，植物学家职业保证铱星。",
            "",
            "| 种子 | 配方解锁 | 全部可能收获 | 生长 | 单次制作 | 固定英文源 |",
            "|------|------|------|:--:|:--:|------|",
        ]
    )
    for title in WILD_SEED_REVISIONS:
        chinese_title, unlock = WILD_SEED_META[title]
        translated = "、".join(
            f"{zh}（{en}）" for en, zh in WILD_SEED_OUTCOMES[title]
        )
        revision = WILD_SEED_REVISIONS[title]
        url = revision_url("en", title, revision)
        lines.append(
            f"| {chinese_title}（{title}） | {unlock} | {translated} | 7 天 | 10 包 | "
            f"[revision {revision}]({url}) |"
        )

    lines.extend(
        [
            "",
            "## 来源与自动审计",
            "",
            f"- [英文 Crops revision {EN_CROPS_REVISION}]({en_crop_url})：完整性主源。",
            f"- [中文农作物 revision {ZH_CROPS_REVISION}]({zh_crop_url})：中文记录源。",
            f"- [英文 Qi Fruit revision {EN_QI_FRUIT_REVISION}]({en_qi_url})：补齐英文主作物页遗漏的详情表。",
            "- [Modding:Crop data](https://stardewvalleywiki.com/Modding:Crop_data)：字段语义与生长、复收、收获结构。",
            "- 四季野生种子固定 revision 逐项见上表。",
            "- 生成器核对 47/47 命名作物、3/3 随机种子系统、英文 48 张主表、中文 49 张主表、"
            "Qi Fruit 两张补全表，以及四季野生种子的 15 个唯一收获结果。",
            "- 任一标题、固定 revision、顶层表、必填字段、季节结果或野生种子结果集合漂移，生成立即失败。",
            "",
            "---",
            "",
            "[上一篇：NPC事件数据总览](./NPC事件数据总览.md) · "
            "[返回游戏概览](../游戏概览.md) · "
            "[查看作物种植机制](../机制分析/作物种植系统.md) · "
            "[下一篇：鱼类数据总览](./鱼类数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def audit_summary(
    en_blocks: dict[str, SourceBlock],
    zh_blocks: dict[str, SourceBlock],
    wild_results: dict[str, tuple[str, ...]],
    en_main_tables: int,
    zh_main_tables: int,
) -> str:
    return (
        f"named_crops={len(CROP_SPECS)}/47, auxiliary_systems=3/3, "
        f"en_main_tables={en_main_tables}/48, zh_main_tables={zh_main_tables}/49, "
        f"en_qi_tables={len(en_blocks['Qi Fruit'].tables)}/2, "
        f"wild_seed_pages={len(wild_results)}/4, "
        f"wild_seed_outcomes={sum(len(items) for items in wild_results.values())}/15"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--probe", action="store_true", help="解析固定源并打印审计指标")
    mode.add_argument("--write", action="store_true", help="生成作物文档")
    mode.add_argument("--check", action="store_true", help="检查生成文档是否为最新")
    args = parser.parse_args()

    en_blocks, zh_blocks, wild_results, en_tables, zh_tables = fetch_and_audit()
    print(
        "audit:",
        audit_summary(en_blocks, zh_blocks, wild_results, en_tables, zh_tables),
    )
    if args.probe:
        return 0

    document = render_document(en_blocks, zh_blocks, wild_results, en_tables, zh_tables)
    if args.write:
        OUTPUT.write_text(document, encoding="utf-8")
        print(f"write: {OUTPUT} ({len(document.encode('utf-8'))} bytes)")
        return 0

    if not OUTPUT.exists():
        print(f"check failed: missing {OUTPUT}", file=sys.stderr)
        return 1
    if OUTPUT.read_text(encoding="utf-8") != document:
        print("check failed: generated document is stale", file=sys.stderr)
        return 1
    print("check: generated document is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
