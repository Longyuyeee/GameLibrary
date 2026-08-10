"""生成并审计《星露谷物语》PC v1.6.15 NPC 爱心事件全集。

依赖：Python 3.10+、curl、beautifulsoup4。

复用 NPC 日程生成器锁定的 34 人中英文页面 revision 与页面缓存。英文个人页
作为完整性主源，中文个人页作为中文记录源；两种语言的爱心事件章节全部保留。
生成前核对人物、事件标题、触发/补充段落、详情表、列表/选择项和嵌套表结构。
已知跨语言结构差异显式披露，未知差异则停止生成。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

from bs4 import NavigableString, Tag

from 生成星露谷NPC日程数据 import (
    EN_API,
    ZH_API,
    EXPECTED_ENGLISH_NAMES,
    PINNED_REVISIONS,
    Revision,
    clean_text,
    direct_rows,
    parse_schedule_page,
    request_html,
    visible_text,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "NPC事件数据总览.md"

EXPECTED_EVENT_COUNT = 178
EXPECTED_DETAIL_TABLE_COUNT = 175
EXPECTED_METRIC_MISMATCHES = {
    "Alex",
    "Elliott",
    "Harvey",
    "Sam",
    "Sebastian",
    "Shane",
    "Abigail",
    "Emily",
    "Leah",
    "Maru",
    "Penny",
    "Clint",
    "Demetrius",
    "Jodi",
    "Pam",
    "Pierre",
    "Robin",
    "Wizard",
}
CHINESE_EVENT_HEADINGS = {"爱心事件", "好感度事件"}


@dataclass(frozen=True)
class DetailBlock:
    label: str
    markdown_blocks: tuple[str, ...]
    list_item_count: int
    nested_table_count: int
    nested_row_count: int


@dataclass(frozen=True)
class HeartEvent:
    title: str
    paragraphs: tuple[str, ...]
    details: tuple[DetailBlock, ...]

    @property
    def list_item_count(self) -> int:
        return sum(item.list_item_count for item in self.details)

    @property
    def nested_table_count(self) -> int:
        return sum(item.nested_table_count for item in self.details)

    @property
    def nested_row_count(self) -> int:
        return sum(item.nested_row_count for item in self.details)


@dataclass(frozen=True)
class EventPage:
    title: str
    revision: Revision
    intro: tuple[str, ...]
    events: tuple[HeartEvent, ...]

    @property
    def paragraph_count(self) -> int:
        return len(self.intro) + sum(len(event.paragraphs) for event in self.events)

    @property
    def detail_table_count(self) -> int:
        return sum(len(event.details) for event in self.events)

    @property
    def list_item_count(self) -> int:
        return sum(event.list_item_count for event in self.events)

    @property
    def nested_table_count(self) -> int:
        return sum(event.nested_table_count for event in self.events)

    @property
    def nested_row_count(self) -> int:
        return sum(event.nested_row_count for event in self.events)

    @property
    def metric_signature(self) -> tuple[int, int, int, int, int, int]:
        return (
            len(self.events),
            self.paragraph_count,
            self.detail_table_count,
            self.list_item_count,
            self.nested_table_count,
            self.nested_row_count,
        )


@dataclass(frozen=True)
class VillagerEvents:
    english_name: str
    chinese_name: str
    english: EventPage
    chinese: EventPage


def heading_text(heading: Tag) -> str:
    headline = heading.select_one(".mw-headline")
    return visible_text(headline if isinstance(headline, Tag) else heading)


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def semantic_tokens(value: str) -> list[str]:
    return re.findall(r"[\w]+|[+-]\d+", value, flags=re.UNICODE)


def markdown_semantic_tokens(value: str) -> list[str]:
    cleaned: list[str] = []
    for line in value.splitlines():
        if re.fullmatch(r"\s*\|?(?:\s*:?-+:?\s*\|)+\s*", line):
            continue
        line = re.sub(r"^\s*(?:-|\d+\.)\s+", "", line)
        cleaned.append(line.replace("|", " "))
    return semantic_tokens(" ".join(cleaned))


def render_nested_table(table: Tag) -> str:
    rows = direct_rows(table)
    if not rows:
        raise AssertionError("事件详情内嵌表没有行")

    values: list[list[str]] = []
    first_is_header = False
    for index, row in enumerate(rows):
        cells = row.find_all(["th", "td"], recursive=False)
        if not cells:
            continue
        if index == 0 and all(cell.name == "th" for cell in cells):
            first_is_header = True
        values.append([visible_text(cell) for cell in cells])
    if not values:
        raise AssertionError("事件详情内嵌表没有可见单元格")

    width = max(len(row) for row in values)
    values = [row + [""] * (width - len(row)) for row in values]
    if not first_is_header:
        return "\n".join(
            "- "
            + " / ".join(
                markdown_escape(cell) for cell in row if clean_text(cell)
            )
            for row in values
        )

    lines = [
        "| " + " | ".join(markdown_escape(cell) for cell in values[0]) + " |",
        "| " + " | ".join("------" for _ in range(width)) + " |",
    ]
    for row in values[1:]:
        lines.append(
            "| " + " | ".join(markdown_escape(cell) for cell in row) + " |"
        )
    return "\n".join(lines)


def render_list(list_node: Tag) -> str:
    ordered = list_node.name == "ol"
    lines: list[str] = []
    for index, item in enumerate(list_node.find_all("li", recursive=False), start=1):
        marker = f"{index}." if ordered else "-"
        text = visible_text(item)
        if text:
            lines.append(f"{marker} {text}")
    return "\n".join(lines)


def render_definition_list(node: Tag) -> str:
    lines: list[str] = []
    for child in node.find_all(["dt", "dd"], recursive=False):
        text = visible_text(child)
        if not text:
            continue
        lines.append(f"- **{text}**" if child.name == "dt" else f"  - {text}")
    return "\n".join(lines)


def render_rich_content(container: Tag) -> tuple[str, ...]:
    blocks: list[str] = []
    inline: list[str] = []

    def flush_inline() -> None:
        text = clean_text(" ".join(inline))
        inline.clear()
        if text:
            blocks.append(text)

    for child in container.children:
        if isinstance(child, NavigableString):
            text = clean_text(str(child))
            if text:
                inline.append(text)
            continue
        if not isinstance(child, Tag):
            continue

        if child.name in {"style", "script", "noscript", "sup", "link"}:
            continue
        if child.name == "br":
            flush_inline()
        elif child.name == "p":
            flush_inline()
            text = visible_text(child)
            if text:
                blocks.append(text)
        elif child.name in {"ul", "ol"}:
            flush_inline()
            rendered = render_list(child)
            if rendered:
                blocks.append(rendered)
        elif child.name == "dl":
            flush_inline()
            rendered = render_definition_list(child)
            if rendered:
                blocks.append(rendered)
        elif child.name == "table":
            flush_inline()
            blocks.append(render_nested_table(child))
        elif child.name in {"div", "section", "blockquote"}:
            flush_inline()
            blocks.extend(render_rich_content(child))
        elif child.name == "img":
            # 心数图标和物品缩略图是装饰；紧邻链接文字已经提供数据名称。
            continue
        else:
            text = visible_text(child)
            if text:
                inline.append(text)
    flush_inline()

    raw_tokens = semantic_tokens(visible_text(container))
    rendered_tokens = markdown_semantic_tokens("\n".join(blocks))
    if raw_tokens != rendered_tokens:
        mismatch_at = next(
            (
                index
                for index, (raw, rendered) in enumerate(
                    zip(raw_tokens, rendered_tokens)
                )
                if raw != rendered
            ),
            min(len(raw_tokens), len(rendered_tokens)),
        )
        raise AssertionError(
            "事件详情富文本转换丢失或重排了可见文本："
            f"token={mismatch_at}, "
            f"raw={raw_tokens[mismatch_at:mismatch_at + 8]}, "
            f"rendered={rendered_tokens[mismatch_at:mismatch_at + 8]}"
        )
    return tuple(blocks)


def parse_detail_table(table: Tag) -> DetailBlock:
    rows = direct_rows(table)
    if len(rows) < 2:
        raise AssertionError("爱心事件详情表缺少标题行或内容行")
    label = visible_text(rows[0]) or "详情"
    container = rows[1].find(["td", "th"], recursive=False)
    if container is None:
        raise AssertionError(f"{label} 缺少内容单元格")

    nested_tables = container.find_all("table")
    return DetailBlock(
        label=label,
        markdown_blocks=render_rich_content(container),
        list_item_count=len(container.find_all("li")),
        nested_table_count=len(nested_tables),
        nested_row_count=sum(len(direct_rows(item)) for item in nested_tables),
    )


def parse_event(
    title: str, nodes: Iterable[Tag], page_title: str, revision_id: int
) -> HeartEvent:
    paragraphs: list[str] = []
    details: list[DetailBlock] = []
    for node in nodes:
        if node.name == "p":
            text = visible_text(node)
            if text:
                paragraphs.append(text)
        elif node.name == "table":
            if "mw-collapsible" not in (node.get("class") or []):
                raise AssertionError(
                    f"{page_title}@{revision_id}/{title} 出现未识别的详情表"
                )
            details.append(parse_detail_table(node))
        elif visible_text(node):
            raise AssertionError(
                f"{page_title}@{revision_id}/{title} 出现未识别节点 {node.name}"
            )
    return HeartEvent(title, tuple(paragraphs), tuple(details))


def parse_event_page(
    title: str, revision: Revision, html: str, language: str
) -> EventPage:
    # 日程解析器已对同一固定页面执行完整 HTML 解析；这里复用它的 BeautifulSoup
    # 依赖并单独定位爱心事件章节。
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    section: Tag | None = None
    for candidate in soup.select("h2"):
        text = heading_text(candidate)
        if (language == "en" and text == "Heart Events") or (
            language == "zh" and text in CHINESE_EVENT_HEADINGS
        ):
            section = candidate
            break
    if section is None:
        raise AssertionError(f"{title}@{revision.revision_id} 缺少爱心事件章节")

    intro: list[str] = []
    events: list[HeartEvent] = []
    current_title: str | None = None
    current_nodes: list[Tag] = []

    node = section.find_next_sibling()
    while node is not None and node.name != "h2":
        if node.name in {"h3", "h4", "h5"}:
            if current_title is not None:
                events.append(
                    parse_event(
                        current_title,
                        current_nodes,
                        title,
                        revision.revision_id,
                    )
                )
            current_title = heading_text(node)
            current_nodes = []
        elif node.name == "p" and current_title is None:
            text = visible_text(node)
            if text:
                intro.append(text)
        elif isinstance(node, Tag):
            if current_title is None:
                if visible_text(node):
                    raise AssertionError(
                        f"{title}@{revision.revision_id} 事件标题前出现未识别内容"
                    )
            else:
                current_nodes.append(node)
        node = node.find_next_sibling()

    if current_title is not None:
        events.append(
            parse_event(current_title, current_nodes, title, revision.revision_id)
        )
    if not events:
        raise AssertionError(f"{title}@{revision.revision_id} 爱心事件章节为空")
    return EventPage(title, revision, tuple(intro), tuple(events))


def fetch_all() -> list[VillagerEvents]:
    items: list[VillagerEvents] = []
    for index, (english_name, chinese_name, en_revision, zh_revision) in enumerate(
        PINNED_REVISIONS, start=1
    ):
        english_revision = Revision(en_revision, "pinned-2026-08-10")
        chinese_revision = Revision(zh_revision, "pinned-2026-08-10")
        english_html = request_html(EN_API, english_name, en_revision)
        chinese_html = request_html(ZH_API, chinese_name, zh_revision)

        # 同一缓存页面先通过日程解析，防止事件生成器使用损坏或错误的居民页。
        parse_schedule_page(english_name, english_revision, english_html, "en")
        parse_schedule_page(chinese_name, chinese_revision, chinese_html, "zh")
        items.append(
            VillagerEvents(
                english_name,
                chinese_name,
                parse_event_page(english_name, english_revision, english_html, "en"),
                parse_event_page(chinese_name, chinese_revision, chinese_html, "zh"),
            )
        )
        print(
            f"[{index:02d}/{len(PINNED_REVISIONS)}] 已解析 {english_name}",
            file=sys.stderr,
            flush=True,
        )
    if [item.english_name for item in items] != EXPECTED_ENGLISH_NAMES:
        raise AssertionError("事件居民集合与预期 34 人不一致")
    return items


def mismatched_english_names(items: Iterable[VillagerEvents]) -> set[str]:
    return {
        item.english_name
        for item in items
        if item.english.metric_signature != item.chinese.metric_signature
    }


def assert_coverage(items: list[VillagerEvents]) -> None:
    if len(items) != len(EXPECTED_ENGLISH_NAMES):
        raise AssertionError("事件居民数量不是 34")
    en_events = sum(len(item.english.events) for item in items)
    zh_events = sum(len(item.chinese.events) for item in items)
    if en_events != EXPECTED_EVENT_COUNT or zh_events != EXPECTED_EVENT_COUNT:
        raise AssertionError(
            f"事件标题数量偏离基线：en={en_events}, zh={zh_events}"
        )
    en_details = sum(item.english.detail_table_count for item in items)
    zh_details = sum(item.chinese.detail_table_count for item in items)
    if (
        en_details != EXPECTED_DETAIL_TABLE_COUNT
        or zh_details != EXPECTED_DETAIL_TABLE_COUNT
    ):
        raise AssertionError(
            f"事件详情表数量偏离基线：en={en_details}, zh={zh_details}"
        )
    observed = mismatched_english_names(items)
    if observed != EXPECTED_METRIC_MISMATCHES:
        raise AssertionError(
            "中英文事件结构差异集合偏离审计基线："
            f"expected={sorted(EXPECTED_METRIC_MISMATCHES)}, "
            f"actual={sorted(observed)}"
        )


def anchor(english_name: str) -> str:
    return f"npc-event-{english_name.lower()}"


def render_source_page(
    lines: list[str], page: EventPage, source_label: str
) -> None:
    lines.extend(
        [
            f"#### {source_label}",
            "",
            f"> {len(page.events)} 个事件/后续条目、{page.paragraph_count} 个事件外层条件或补充段落、"
            f"{page.detail_table_count} 张详情表、{page.list_item_count} 个列表/选择项、"
            f"{page.nested_table_count} 张嵌套结果表（{page.nested_row_count} 行）。",
            "",
        ]
    )
    for text in page.intro:
        lines.append(text)
        lines.append("")

    for event in page.events:
        lines.extend([f"##### {event.title}", ""])
        if not event.paragraphs and not event.details:
            lines.extend(
                [
                    "*源页将此项作为下方子事件的分组标题，没有独立内容块。*",
                    "",
                ]
            )
        if event.paragraphs:
            lines.append("**触发条件或事件外补充：**")
            lines.append("")
            for paragraph in event.paragraphs:
                lines.append(f"- {paragraph}")
            lines.append("")
        for index, detail in enumerate(event.details, start=1):
            suffix = f" {index}" if len(event.details) > 1 else ""
            lines.extend([f"**{detail.label}{suffix}：**", ""])
            for block in detail.markdown_blocks:
                lines.extend([block, ""])


def totals(items: list[VillagerEvents], language: str) -> tuple[int, ...]:
    pages = [getattr(item, language) for item in items]
    return (
        sum(len(page.events) for page in pages),
        sum(page.paragraph_count for page in pages),
        sum(page.detail_table_count for page in pages),
        sum(page.list_item_count for page in pages),
        sum(page.nested_table_count for page in pages),
        sum(page.nested_row_count for page in pages),
    )


def render_document(items: list[VillagerEvents]) -> str:
    assert_coverage(items)
    en = totals(items, "english")
    zh = totals(items, "chinese")
    mismatches = mismatched_english_names(items)

    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > "
        "[星露谷物语概览](../游戏概览.md) > [NPC数据总览](./NPC数据总览.md) > NPC事件数据总览",
        "",
        "# NPC事件数据总览 — 星露谷物语",
        "",
        "> 游戏版本：Stardew Valley PC v1.6.15",
        ">",
        "> 数据来源：英文 Stardew Valley Wiki 个人页为完整性主源；中文个人页为中文记录源",
        ">",
        "> 生成时逐人固定中英文 revision；两种语言的全部触发段落、详情叙述、选择和结果表均保留",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|------|------|",
        "| 数据全集定义 | 官方 Villagers 名册中 34 位可送礼居民个人页的完整 Heart Events/爱心事件章节 |",
        "| 预计居民数 | 34 |",
        "| 实际居民数 | 34 |",
        "| 数量差异 | 0 |",
        f"| 英文主源 | {en[0]} 个事件/后续条目 / {en[1]} 个外层段落 / {en[2]} 张详情表 / "
        f"{en[3]} 个列表或选择项 / {en[4]} 张嵌套表（{en[5]} 行） |",
        f"| 中文记录源 | {zh[0]} 个事件/后续条目 / {zh[1]} 个外层段落 / {zh[2]} 张详情表 / "
        f"{zh[3]} 个列表或选择项 / {zh[4]} 张嵌套表（{zh[5]} 行） |",
        "| 必填字段 | 居民、来源 revision、事件标题/心数、触发条件、详情、选择、友情点及其他后果 |",
        "| 中英文事件数量一致 | 34/34 人；178/178 个事件或后续条目 |",
        f"| 深层结构一致 | {34 - len(mismatches)}/34 人 |",
        f"| 已审计深层结构差异 | {len(mismatches)}/34 人；双源完整并列，不静默覆盖 |",
        "| 排除边界 | 12 位不可送礼 NPC 不属于个人爱心事件全集；装饰性心数/物品缩略图不重复收录 |",
        "| 验收状态 | **NPC 爱心事件子域已完成** |",
        "",
        "### 读取与裁定说明",
        "",
        "本文把个人页 Heart Events/爱心事件章节中的所有标题视为全集条目，包括标准心数过场、"
        "Anytime 邮件、0 心事件、分段事件、群体 10 心、婚后 14 心和事件后续。",
        "",
        "事件标题后的外层段落通常给出地点、时间、天气、季节、日期、关系状态与前置事件；"
        "折叠详情表保留剧情、所有选项、友情点变化、配方/物品/邮件及其他后果。"
        "中英文结构或内容不同时，以英文主源判断 PC v1.6.15 行为，中文记录仍完整保留。",
        "",
        "## 居民索引与数量对账",
        "",
        "| # | 居民 | 英文（事件/段落/详情/列表/嵌套表行） | 中文（事件/段落/详情/列表/嵌套表行） | 深层结构 | 中文 revision | 英文 revision |",
        "|:--:|------|:--:|:--:|:--:|:--:|:--:|",
    ]

    for index, item in enumerate(items, start=1):
        en_page = item.english
        zh_page = item.chinese
        en_revision = en_page.revision.revision_id
        zh_revision = zh_page.revision.revision_id
        en_url = (
            "https://stardewvalleywiki.com/mediawiki/index.php?title="
            f"{quote(item.english_name)}&oldid={en_revision}"
        )
        zh_url = (
            "https://zh.stardewvalleywiki.com/mediawiki/index.php?title="
            f"{quote(item.chinese_name)}&oldid={zh_revision}"
        )
        lines.append(
            f"| {index} | [{item.chinese_name}（{item.english_name}）](#{anchor(item.english_name)}) | "
            f"{len(en_page.events)}/{en_page.paragraph_count}/{en_page.detail_table_count}/"
            f"{en_page.list_item_count}/{en_page.nested_row_count} | "
            f"{len(zh_page.events)}/{zh_page.paragraph_count}/{zh_page.detail_table_count}/"
            f"{zh_page.list_item_count}/{zh_page.nested_row_count} | "
            f"{'差异已审计' if item.english_name in mismatches else '一致'} | "
            f"[zh {zh_revision}]({zh_url}) | [en {en_revision}]({en_url}) |"
        )

    lines.extend(["", "## 逐人爱心事件全集", ""])
    for index, item in enumerate(items, start=1):
        lines.extend(
            [
                f'<a id="{anchor(item.english_name)}"></a>',
                "",
                f"### {index:02d}. {item.chinese_name}（{item.english_name}）",
                "",
                f"> 来源：中文 revision {item.chinese.revision.revision_id}；"
                f"英文 revision {item.english.revision.revision_id}",
                ">",
                "> 结构判定："
                + (
                    "事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准"
                    if item.english_name in mismatches
                    else "中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列"
                ),
                "",
            ]
        )
        render_source_page(lines, item.chinese, "中文记录源（完整保留）")
        render_source_page(lines, item.english, "英文完整性主源（PC v1.6.15 判定基准）")

    lines.extend(
        [
            "## 来源与审计方法",
            "",
            "- [Villagers — 官方 34 位可送礼居民名册]"
            "(https://stardewvalleywiki.com/Villagers)",
            "- [Modding:Event data — 事件触发条件、已看事件、友情点与后果命令]"
            "(https://stardewvalleywiki.com/Modding:Event_data)",
            "- 每位居民的中英文固定 revision 链接见索引表。",
            "- 生成器要求 34/34 人存在事件章节、178/178 个事件标题和 175/175 张详情表；"
            "富文本转换还逐表验证可见文本 token 顺序不丢失。",
            "- 任何居民缺页、缺事件章节、空事件块、未知表型、标题/详情数量漂移，或深层差异居民集合"
            "偏离已审计基线，都会使生成失败。",
            "",
            "---",
            "",
            "[上一篇：NPC日程数据总览](./NPC日程数据总览.md) · "
            "[返回NPC数据总览](./NPC数据总览.md) · "
            "[返回游戏概览](../游戏概览.md) · "
            "[下一篇：作物数据总览](./作物数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def audit_summary(items: list[VillagerEvents]) -> str:
    en = totals(items, "english")
    zh = totals(items, "chinese")
    return (
        f"villagers={len(items)}/34, "
        f"en_events={en[0]}, en_paragraphs={en[1]}, en_details={en[2]}, "
        f"en_list_items={en[3]}, en_nested_tables={en[4]}, en_nested_rows={en[5]}, "
        f"zh_events={zh[0]}, zh_paragraphs={zh[1]}, zh_details={zh[2]}, "
        f"zh_list_items={zh[3]}, zh_nested_tables={zh[4]}, zh_nested_rows={zh[5]}, "
        f"metric_mismatches={len(mismatched_english_names(items))}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--probe", action="store_true", help="只解析并打印审计指标")
    mode.add_argument("--write", action="store_true", help="生成文档")
    mode.add_argument("--check", action="store_true", help="检查文档是否与固定来源一致")
    args = parser.parse_args()

    items = fetch_all()
    assert_coverage(items)
    print("audit:", audit_summary(items))
    if args.probe:
        for item in items:
            if item.english_name in EXPECTED_METRIC_MISMATCHES:
                print(
                    "mismatch:",
                    f"{item.english_name}/{item.chinese_name}: "
                    f"en={item.english.metric_signature}, "
                    f"zh={item.chinese.metric_signature}",
                )
        return 0

    document = render_document(items)
    if args.write:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(document, encoding="utf-8")
        print(f"write: {OUTPUT} ({len(document.encode('utf-8'))} bytes)")
        return 0

    if not OUTPUT.exists():
        print(f"check failed: document does not exist: {OUTPUT}", file=sys.stderr)
        return 1
    current = OUTPUT.read_text(encoding="utf-8")
    if current != document:
        print("check failed: generated document is stale", file=sys.stderr)
        return 1
    print("check: generated document is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
