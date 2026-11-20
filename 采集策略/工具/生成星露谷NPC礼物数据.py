"""生成并审计《星露谷物语》v1.6.15 NPC 礼物全集文档。

依赖：Python 3.10+、requests、beautifulsoup4。

数据来自 Stardew Valley Wiki 的中英文“礼物列表”，并以英文 Wiki 公布的
v1.6.15 NPCGiftTastes 原始数据页作为版本基线。生成时强制校验：

- 中英文表均为 1 行通用规则 + 34 位可送礼村民；
- 每行必须有 NPC、生日、最爱、喜欢、一般、不喜欢、讨厌共 7 个字段；
- 中英文村民顺序与预期名单完全一致。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup, Tag


ZH_GIFTS_URL = "https://zh.stardewvalleywiki.com/%E7%A4%BC%E7%89%A9%E5%88%97%E8%A1%A8"
EN_GIFTS_URL = "https://stardewvalleywiki.com/List_of_All_Gifts"
ZH_FRIENDSHIP_URL = "https://zh.stardewvalleywiki.com/%E5%8F%8B%E8%B0%8A"
EN_FRIENDSHIP_URL = "https://stardewvalleywiki.com/Friendship"
RAW_GIFT_DATA_URL = "https://stardewvalleywiki.com/Modding:Gift_taste_data"

ZH_API = "https://zh.stardewvalleywiki.com/mediawiki/api.php"
EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"

EXPECTED_ENGLISH_NAMES = [
    "Alex",
    "Elliott",
    "Harvey",
    "Sam",
    "Sebastian",
    "Shane",
    "Abigail",
    "Emily",
    "Haley",
    "Leah",
    "Maru",
    "Penny",
    "Caroline",
    "Clint",
    "Demetrius",
    "Dwarf",
    "Evelyn",
    "George",
    "Gus",
    "Jas",
    "Jodi",
    "Kent",
    "Krobus",
    "Leo",
    "Lewis",
    "Linus",
    "Marnie",
    "Pam",
    "Pierre",
    "Robin",
    "Sandy",
    "Vincent",
    "Willy",
    "Wizard",
]

PREFERENCE_LABELS = [
    ("最爱", "+80"),
    ("喜欢", "+45"),
    ("一般", "+20"),
    ("不喜欢", "-20"),
    ("讨厌", "-40"),
]

# 中文礼物表 revision 53455 与较新的英文表/1.6.15 原始数据存在两处差异。
# 以下列表以英文表为全集和顺序，保留经过人工核对的中文译名。
CANONICAL_ZH_OVERRIDES: dict[tuple[str, int], tuple[str, ...]] = {
    ("Maru", 2): (
        "所有蛋（除了虚空蛋）",
        "所有水果（除了黑莓、水晶果、果树果实、美洲大树莓、草莓）",
        "所有奶类",
        "黄水仙",
        "蒲公英",
        "姜",
        "榛子",
        "韭葱",
        "野山葵",
        "冬根",
    ),
    ("Leo", 1): (
        "龙牙",
        "鹦鹉螺",
        "石英",
        "海胆",
        "香味浆果",
    ),
}

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "NPC礼物数据总览.md"


@dataclass(frozen=True)
class GiftRow:
    chinese_name: str
    english_name: str
    birthday: str
    preferences_zh: tuple[tuple[str, ...], ...]
    preferences_en: tuple[tuple[str, ...], ...]


def fetch_soup(url: str) -> BeautifulSoup:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def cell_items(cell: Tag) -> tuple[str, ...]:
    items = [clean_text(item.get_text(" ", strip=True)) for item in cell.select("li")]
    if not items:
        text = clean_text(cell.get_text(" ", strip=True))
        items = [text] if text else []
    return tuple(dict.fromkeys(item for item in items if item))


def parse_gift_table(url: str) -> list[tuple[tuple[str, ...], ...]]:
    soup = fetch_soup(url)
    table = soup.select_one("table.wikitable")
    if table is None:
        raise RuntimeError(f"未找到礼物表：{url}")

    rows: list[tuple[tuple[str, ...], ...]] = []
    for tr in table.select("tr")[1:]:
        cells = tr.select("td")
        if not cells:
            continue
        if len(cells) != 7:
            raise RuntimeError(f"礼物表出现非 7 字段行：{len(cells)}，来源 {url}")
        rows.append(tuple(cell_items(cell) for cell in cells))
    return rows


def revision_info(api_url: str, title: str) -> tuple[int, str]:
    response = requests.get(
        api_url,
        params={
            "action": "query",
            "prop": "revisions",
            "rvprop": "ids|timestamp",
            "titles": title,
            "format": "json",
            "formatversion": 2,
        },
        timeout=30,
    )
    response.raise_for_status()
    page = response.json()["query"]["pages"][0]
    revision = page["revisions"][0]
    return int(revision["revid"]), str(revision["timestamp"])


def first_list_after_heading(soup: BeautifulSoup, heading_text: str) -> tuple[str, ...]:
    for heading in soup.select("h3"):
        if clean_text(heading.get_text(" ", strip=True)) != heading_text:
            continue
        node = heading.find_next_sibling()
        while node is not None and node.name not in {"h2", "h3", "h4"}:
            if node.name == "ul":
                return cell_items(node)
            node = node.find_next_sibling()
    raise RuntimeError(f"未找到“{heading_text}”的通用规则列表")


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


def join_items(items: Iterable[str]) -> str:
    values = [escape_cell(clean_text(item)) for item in items]
    return "<br>".join(values) if values else "—"


def join_bilingual(zh_items: Iterable[str], en_items: Iterable[str]) -> str:
    chinese = list(zh_items)
    english = list(en_items)
    if len(chinese) != len(english):
        raise RuntimeError(f"中英文条目数量不一致：中文 {len(chinese)}，英文 {len(english)}")
    return "<br>".join(
        f"{escape_cell(clean_text(zh))}（{escape_cell(clean_text(en))}）"
        for zh, en in zip(chinese, english, strict=True)
    ) or "—"


def build_document() -> tuple[str, dict[str, int | str]]:
    zh_rows = parse_gift_table(ZH_GIFTS_URL)
    en_rows = parse_gift_table(EN_GIFTS_URL)

    if len(zh_rows) != 35 or len(en_rows) != 35:
        raise RuntimeError(
            f"礼物表行数不符：中文 {len(zh_rows)}，英文 {len(en_rows)}；预期均为 35"
        )

    english_names = [row[0][0] for row in en_rows[1:]]
    if english_names != EXPECTED_ENGLISH_NAMES:
        raise RuntimeError("英文村民顺序或名单发生变化，请人工审计后更新脚本")

    gift_rows: list[GiftRow] = []
    source_mismatches: list[tuple[str, int, int, int]] = []
    for zh, en in zip(zh_rows[1:], en_rows[1:], strict=True):
        english_name = en[0][0]
        preferences_zh = []
        preferences_en = []
        for preference_index, source_index in enumerate(range(2, 7)):
            zh_items = zh[source_index]
            en_items = en[source_index]
            if len(zh_items) != len(en_items):
                source_mismatches.append(
                    (english_name, preference_index, len(zh_items), len(en_items))
                )
                zh_items = CANONICAL_ZH_OVERRIDES.get((english_name, preference_index), ())
            if len(zh_items) != len(en_items):
                raise RuntimeError(
                    f"{english_name} 的偏好字段 {preference_index} 无法完成中英文对账"
                )
            preferences_zh.append(zh_items)
            preferences_en.append(en_items)
        gift_rows.append(
            GiftRow(
                chinese_name=zh[0][0],
                english_name=english_name,
                birthday=zh[1][0],
                preferences_zh=tuple(preferences_zh),
                preferences_en=tuple(preferences_en),
            )
        )

    if len(source_mismatches) != 2:
        raise RuntimeError(
            f"中英文源差异数量发生变化：当前 {len(source_mismatches)}，预期 2；请人工审计"
        )

    friendship_soup = fetch_soup(ZH_FRIENDSHIP_URL)
    universal_dislikes = first_list_after_heading(friendship_soup, "不喜欢的礼物")
    universal_hates = first_list_after_heading(friendship_soup, "讨厌的礼物")
    friendship_soup_en = fetch_soup(EN_FRIENDSHIP_URL)
    universal_dislikes_en = first_list_after_heading(friendship_soup_en, "Universal Dislikes")
    universal_hates_en = first_list_after_heading(friendship_soup_en, "Universal Hates")

    zh_revision, zh_timestamp = revision_info(ZH_API, "礼物列表")
    en_revision, en_timestamp = revision_info(EN_API, "List of All Gifts")
    raw_revision, raw_timestamp = revision_info(EN_API, "Modding:Gift taste data")

    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > "
        "[星露谷物语概览](../游戏概览.md) > [NPC数据总览](./NPC数据总览.md) > NPC礼物数据总览",
        "",
        "# NPC礼物数据总览 — 星露谷物语",
        "",
        "> 游戏版本：Stardew Valley PC v1.6.15",
        ">",
        f"> 中文礼物表版本：revision {zh_revision} ({zh_timestamp})",
        ">",
        f"> 英文礼物表版本：revision {en_revision} ({en_timestamp})",
        ">",
        f"> v1.6.15 原始数据页：revision {raw_revision} ({raw_timestamp})",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|------|------|",
        "| 覆盖版本 | PC v1.6.15；其他当前平台按等价内容核对，旧平台差异另记 |",
        "| 数据范围 | 34 位可送礼村民的生日与五档礼物偏好；采用“通用规则＋逐人覆盖项”表达完整结果 |",
        "| 预计条目数 | 34 位可送礼村民 |",
        f"| 实际收录数 | {len(gift_rows)} 位 |",
        f"| 数量差异 | {34 - len(gift_rows)} |",
        "| 每条规定字段 | 中文名、英文名、生日、最爱、喜欢、一般、不喜欢、讨厌 |",
        "| 字段完整率 | 34 / 34 行均具有 7 个源字段，100% |",
        "| 表达规则 | 每位村民的表格记录其对通用规则的覆盖项；未被覆盖的物品按通用规则判定；中文名后保留英文名用于消歧 |",
        "| 来源裁定 | 英文 v1.6.15 表与原始数据优先；中文表用于译名，已人工裁定 2 处源差异 |",
        "| 验收状态 | **礼物偏好子域已完成**；NPC 日程、事件与角色资料不在本文范围 |",
        "",
        "## 一、如何读取这份全集",
        "",
        "游戏使用两层规则计算礼物偏好：先应用通用五档规则，再应用村民个人覆盖项。本文完整保留这两层信息。"
        "例如某位村民的“喜欢”栏没有重复列出所有通用喜欢物品，不代表缺失；只有该村民覆盖通用结果的物品或类别才会出现在个人栏中。",
        "",
        "星之果茶固定增加 250 好感，不受普通 +80 规则限制；生日或冬日星盛宴赠送时按游戏的特殊规则处理。",
        "",
        "## 二、通用礼物规则",
        "",
        "| 偏好 | 好感 | 全量规则（中文＋英文原名） |",
        "|------|:--:|------|",
        f"| 最爱 | +80 | {join_bilingual(zh_rows[0][2], en_rows[0][2])} |",
        f"| 喜欢 | +45 | {join_bilingual(zh_rows[0][3], en_rows[0][3])} |",
        f"| 一般 | +20 | {join_bilingual(zh_rows[0][4], en_rows[0][4])} |",
        f"| 不喜欢 | -20 | {join_bilingual(universal_dislikes, universal_dislikes_en)} |",
        f"| 讨厌 | -40 | {join_bilingual(universal_hates, universal_hates_en)} |",
        "",
        "个人覆盖项优先于本表。完整覆盖项见下方 34 位村民的逐人数据。",
        "",
        "## 三、可送礼村民索引（34/34）",
        "",
        "| # | 村民 | 英文名 | 生日 | 类型 |",
        "|:--:|------|------|------|------|",
    ]

    for index, row in enumerate(gift_rows, start=1):
        kind = "婚恋候选人" if index <= 12 else "非婚恋村民"
        anchor = f"{index:02d}-{row.chinese_name.lower()}-{row.english_name.lower()}"
        lines.append(
            f"| {index} | [{escape_cell(row.chinese_name)}](#{anchor}) | "
            f"{escape_cell(row.english_name)} | {escape_cell(row.birthday)} | {kind} |"
        )

    lines.extend(["", "## 四、逐人礼物偏好覆盖项", ""])

    for index, row in enumerate(gift_rows, start=1):
        lines.extend(
            [
                f"### {index:02d}. {row.chinese_name} ({row.english_name})",
                "",
                f"> 生日：{row.birthday} | 类型：{'婚恋候选人' if index <= 12 else '非婚恋村民'}",
                "",
                "| 偏好 | 好感 | 对通用规则的完整覆盖项 |",
                "|------|:--:|------|",
            ]
        )
        for (label, points), zh_items, en_items in zip(
            PREFERENCE_LABELS,
            row.preferences_zh,
            row.preferences_en,
            strict=True,
        ):
            lines.append(
                f"| {label} | {points} | {join_bilingual(zh_items, en_items)} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 五、来源与对账",
            "",
            f"- [中文 Stardew Valley Wiki — 礼物列表]({ZH_GIFTS_URL})",
            f"- [英文 Stardew Valley Wiki — List of All Gifts]({EN_GIFTS_URL})",
            f"- [中文 Stardew Valley Wiki — 友谊]({ZH_FRIENDSHIP_URL})",
            f"- [英文 Stardew Valley Wiki — Friendship]({EN_FRIENDSHIP_URL})",
            f"- [英文 Stardew Valley Wiki — v1.6.15 NPCGiftTastes 原始数据]({RAW_GIFT_DATA_URL})",
            "",
            "生成审计：中英文礼物表均为 35 行，其中 1 行通用规则、34 行可送礼村民；"
            "34 位村民英文名及顺序完全一致；每行均为 7 个字段。",
            "",
            "来源差异裁定：中文 revision 53455 比英文表旧。玛鲁“一般”栏移除中文表额外的蘑菇类别；"
            "雷欧“喜欢”栏移除中文表额外的彩虹贝壳。两处均以英文 1.6.15 表和原始数据为准。",
            "",
            "---",
            "",
            "[上一篇：NPC数据总览](./NPC数据总览.md) · "
            "[返回游戏概览](../游戏概览.md) · "
            "[下一篇：NPC关系数值总览](./NPC关系数值总览.md)",
            "",
        ]
    )

    document = "\n".join(lines)
    stats: dict[str, int | str] = {
        "giftable_villagers": len(gift_rows),
        "source_rows_zh": len(zh_rows),
        "source_rows_en": len(en_rows),
        "fields_per_row": 7,
        "source_mismatches_found": len(source_mismatches),
        "source_mismatches_resolved": len(CANONICAL_ZH_OVERRIDES),
        "zh_revision": zh_revision,
        "en_revision": en_revision,
        "raw_revision": raw_revision,
    }
    return document, stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="写入生成文档")
    parser.add_argument("--check", action="store_true", help="检查现有文档是否与生成结果一致")
    args = parser.parse_args()

    if not args.write and not args.check:
        parser.error("必须指定 --write 或 --check")

    document, stats = build_document()
    print("audit:", ", ".join(f"{key}={value}" for key, value in stats.items()))

    if args.write:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(document, encoding="utf-8", newline="\n")
        print(f"written: {OUTPUT} ({len(document.encode('utf-8'))} bytes)")

    if args.check:
        if not OUTPUT.exists():
            print(f"missing: {OUTPUT}", file=sys.stderr)
            return 1
        existing = OUTPUT.read_text(encoding="utf-8")
        if existing != document:
            print("generated document is out of date", file=sys.stderr)
            return 1
        print("check: generated document is current")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
