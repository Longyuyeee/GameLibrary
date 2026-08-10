"""生成并审计《星露谷物语》PC v1.6.15 NPC 日程全集。

依赖：Python 3.10+、curl、beautifulsoup4。

英文 Stardew Valley Wiki 的 34 个可送礼居民页面作为完整性主源，中文页面
作为用户可读内容源。生成前逐人核对日程分区、条件分支和时间地点行数；两种
语言的记录全部保留，已知结构差异显式披露，未知差异则停止生成。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

from bs4 import BeautifulSoup, NavigableString, Tag


EN_API = "https://stardewvalleywiki.com/mediawiki/api.php"
ZH_API = "https://zh.stardewvalleywiki.com/mediawiki/api.php"
USER_AGENT = "GameDocsScheduleAudit/1.0"

EXPECTED_ENGLISH_NAMES = [
    "Alex", "Elliott", "Harvey", "Sam", "Sebastian", "Shane",
    "Abigail", "Emily", "Haley", "Leah", "Maru", "Penny",
    "Caroline", "Clint", "Demetrius", "Dwarf", "Evelyn", "George",
    "Gus", "Jas", "Jodi", "Kent", "Krobus", "Leo", "Lewis", "Linus",
    "Marnie", "Pam", "Pierre", "Robin", "Sandy", "Vincent", "Willy",
    "Wizard",
]

# 2026-08-10 审计锁定。更新来源时必须显式修改本表并重新执行中英文结构审计。
PINNED_REVISIONS = [
    ("Alex", "亚历克斯", 193663, 55068),
    ("Elliott", "艾利欧特", 192964, 55231),
    ("Harvey", "哈维", 193951, 54980),
    ("Sam", "山姆", 193676, 55076),
    ("Sebastian", "塞巴斯蒂安", 193877, 55064),
    ("Shane", "谢恩", 193586, 55046),
    ("Abigail", "阿比盖尔", 193689, 55185),
    ("Emily", "艾米丽", 191968, 55091),
    ("Haley", "海莉", 191939, 55013),
    ("Leah", "莉亚", 192966, 55041),
    ("Maru", "玛鲁", 193560, 55085),
    ("Penny", "潘妮", 193516, 55083),
    ("Caroline", "卡洛琳", 191301, 54977),
    ("Clint", "克林特", 191347, 55070),
    ("Demetrius", "德米特里厄斯", 193879, 54996),
    ("Dwarf", "矮人", 191010, 54688),
    ("Evelyn", "艾芙琳", 191129, 54548),
    ("George", "乔治", 193909, 54046),
    ("Gus", "格斯", 191548, 55267),
    ("Jas", "贾斯", 193899, 55188),
    ("Jodi", "乔迪", 191546, 55067),
    ("Kent", "肯特", 193910, 55035),
    ("Krobus", "科罗布斯", 192255, 55028),
    ("Leo", "雷欧", 192150, 55053),
    ("Lewis", "刘易斯", 191314, 54974),
    ("Linus", "莱纳斯", 193911, 55042),
    ("Marnie", "玛妮", 191544, 55084),
    ("Pam", "潘姆", 191550, 55017),
    ("Pierre", "皮埃尔", 192883, 55086),
    ("Robin", "罗宾", 191769, 55090),
    ("Sandy", "桑迪", 191345, 55081),
    ("Vincent", "文森特", 193876, 55079),
    ("Willy", "威利", 192689, 55075),
    ("Wizard", "法师", 193912, 55012),
]

EXPECTED_STRUCTURE_MISMATCHES = {
    "Sam", "Sebastian", "Abigail", "Haley", "Maru", "Lewis"
}

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "牧场经营类" / "星露谷物语" / "数值数据" / "NPC日程数据总览.md"
CACHE = ROOT / ".git" / "gamedocs-schedule-cache"


@dataclass(frozen=True)
class Revision:
    revision_id: int
    timestamp: str


@dataclass(frozen=True)
class ScheduleStep:
    time: str
    location: str


@dataclass(frozen=True)
class ScheduleGroup:
    condition: str
    steps: tuple[ScheduleStep, ...]


@dataclass(frozen=True)
class ScheduleSection:
    title: str
    groups: tuple[ScheduleGroup, ...]


@dataclass(frozen=True)
class SchedulePage:
    title: str
    revision: Revision
    notes: tuple[str, ...]
    sections: tuple[ScheduleSection, ...]

    @property
    def group_count(self) -> int:
        return sum(len(section.groups) for section in self.sections)

    @property
    def step_count(self) -> int:
        return sum(
            len(group.steps) for section in self.sections for group in section.groups
        )


@dataclass(frozen=True)
class VillagerSchedule:
    english_name: str
    chinese_name: str
    english: SchedulePage
    chinese: SchedulePage


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def visible_text(node: Tag) -> str:
    values: list[str] = []
    for item in node.descendants:
        if not isinstance(item, NavigableString):
            continue
        parent = item.parent
        if parent and parent.find_parent(["sup", "style", "script", "noscript"]):
            continue
        if parent and parent.name in {"sup", "style", "script", "noscript"}:
            continue
        text = clean_text(str(item))
        if text:
            values.append(text)
    return clean_text(" ".join(values))


def request_html(api_url: str, title: str, revision_id: int) -> str:
    site = "zh" if api_url == ZH_API else "en"
    cache_file = CACHE / f"{site}-{revision_id}.html"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")

    last_error: Exception | None = None
    for attempt in range(1, 5):
        try:
            command = [
                "curl.exe" if sys.platform == "win32" else "curl",
                "--location",
                "--silent",
                "--show-error",
                "--fail-with-body",
                "--max-time",
                "25",
                "--user-agent",
                USER_AGENT,
                "--get",
                "--data-urlencode",
                "action=parse",
                "--data-urlencode",
                f"oldid={revision_id}",
                "--data-urlencode",
                "prop=text",
                "--data-urlencode",
                "format=json",
                "--data-urlencode",
                "formatversion=2",
                api_url,
            ]
            if sys.platform == "win32":
                command.insert(1, "--ssl-no-revoke")
            response = subprocess.run(
                command,
                check=True,
                capture_output=True,
                timeout=30,
            )
            payload = json.loads(response.stdout.decode("utf-8"))
            html = str(payload["parse"]["text"])
            if not html:
                raise ValueError("API 返回空正文")
            CACHE.mkdir(parents=True, exist_ok=True)
            cache_file.write_text(html, encoding="utf-8")
            return html
        except (
            json.JSONDecodeError,
            KeyError,
            OSError,
            subprocess.SubprocessError,
            UnicodeDecodeError,
            ValueError,
        ) as error:
            last_error = error
            if attempt < 4:
                time.sleep(attempt * 2)
    raise RuntimeError(f"页面请求失败：{title}@{revision_id}") from last_error


def page_metadata() -> list[tuple[str, str, Revision, Revision]]:
    pinned_names = [item[0] for item in PINNED_REVISIONS]
    if pinned_names != EXPECTED_ENGLISH_NAMES:
        raise AssertionError("固定修订清单与预期 34 人的顺序或集合不一致")
    if len({item[1] for item in PINNED_REVISIONS}) != len(PINNED_REVISIONS):
        raise AssertionError("固定修订清单包含重复中文名")
    return [
        (
            english_name,
            chinese_name,
            Revision(english_revision, "pinned-2026-08-10"),
            Revision(chinese_revision, "pinned-2026-08-10"),
        )
        for english_name, chinese_name, english_revision, chinese_revision
        in PINNED_REVISIONS
    ]


def direct_rows(table: Tag) -> list[Tag]:
    body = table.find("tbody", recursive=False)
    parent = body if body else table
    return parent.find_all("tr", recursive=False)


def parse_step_rows(rows: Iterable[Tag]) -> tuple[ScheduleStep, ...]:
    steps: list[ScheduleStep] = []
    for row in rows:
        cells = row.find_all(["th", "td"], recursive=False)
        values = [visible_text(cell) for cell in cells]
        if not values:
            continue
        if len(values) >= 2 and values[0].lower() in {"time", "时间"}:
            continue
        if len(values) == 1:
            steps.append(ScheduleStep("说明", values[0]))
        else:
            steps.append(ScheduleStep(values[0], " / ".join(values[1:])))
    return tuple(steps)


def parse_inner_table(table: Tag) -> tuple[ScheduleStep, ...]:
    return parse_step_rows(direct_rows(table))


def parse_outer_table(table: Tag) -> ScheduleSection:
    rows = direct_rows(table)
    if len(rows) < 2:
        raise AssertionError("日程外层表缺少标题行或内容行")
    title = visible_text(rows[0])
    container = rows[1].find(["td", "th"], recursive=False)
    if not title or container is None:
        raise AssertionError("日程外层表无法解析标题或内容")

    # 部分个人页每个折叠表本身就是一个条件：首行为条件标题，其余行直接是
    # 时间/地点；另一些页面则以季节为外层，在第二行嵌套多个条件表。
    if container.find("table") is None:
        direct_steps = parse_step_rows(rows[1:])
        if direct_steps:
            return ScheduleSection(
                title, (ScheduleGroup(title, direct_steps),)
            )

    pending: list[str] = []
    groups: list[ScheduleGroup] = []
    for child in container.find_all(["p", "ul", "ol", "dl", "table"]):
        # 只处理当前外层表直属语义内容；条件表内部的段落属于地点描述，
        # 不能再次作为条件文字采集。
        if child.find_parent("table") is not table:
            continue
        if child.name == "p":
            text = visible_text(child)
            if text:
                pending.append(text)
        elif child.name == "table":
            condition = " / ".join(pending) if pending else "未命名日程"
            pending = []
            steps = parse_inner_table(child)
            if not steps:
                raise AssertionError(f"{title}/{condition} 没有时间地点行")
            groups.append(ScheduleGroup(condition, steps))
        elif child.name in {"ul", "ol", "dl"}:
            text = visible_text(child)
            if text:
                pending.append(text)

    if pending:
        groups.append(
            ScheduleGroup("补充说明", tuple(ScheduleStep("说明", note) for note in pending))
        )
    if not groups:
        raise AssertionError(f"{title} 没有可解析的条件组或时间地点行")
    return ScheduleSection(title, tuple(groups))


def parse_schedule_page(
    title: str, revision: Revision, html: str, language: str
) -> SchedulePage:
    soup = BeautifulSoup(html, "html.parser")
    heading: Tag | None = None
    for candidate in soup.select("h2"):
        headline = candidate.select_one(".mw-headline")
        text = visible_text(headline if isinstance(headline, Tag) else candidate)
        if (language == "en" and text == "Schedule") or (
            language == "zh" and "日程" in text
        ):
            heading = candidate
            break
    if heading is None:
        raise AssertionError(f"{title}@{revision.revision_id} 缺少日程章节")

    notes: list[str] = []
    sections: list[ScheduleSection] = []
    node = heading.find_next_sibling()
    while node is not None and node.name != "h2":
        if node.name == "p":
            text = visible_text(node)
            if text:
                notes.append(text)
        elif node.name == "table" and "mw-collapsible" in (node.get("class") or []):
            sections.append(parse_outer_table(node))
        elif node.name == "table":
            raise AssertionError(
                f"{title}@{revision.revision_id} 出现未识别的非折叠日程表"
            )
        elif node.name in {"ul", "ol", "dl"}:
            text = visible_text(node)
            if text:
                notes.append(text)
        elif isinstance(node, Tag) and node.find("table") is not None:
            raise AssertionError(
                f"{title}@{revision.revision_id} 出现未识别的嵌套日程表容器"
            )
        node = node.find_next_sibling()

    if not notes and not sections:
        raise AssertionError(f"{title}@{revision.revision_id} 日程章节为空")
    return SchedulePage(title, revision, tuple(notes), tuple(sections))


def fetch_villager(
    item: tuple[str, str, Revision, Revision]
) -> VillagerSchedule:
    english_name, chinese_name, english_revision, chinese_revision = item
    english_html = request_html(EN_API, english_name, english_revision.revision_id)
    chinese_html = request_html(ZH_API, chinese_name, chinese_revision.revision_id)
    return VillagerSchedule(
        english_name,
        chinese_name,
        parse_schedule_page(english_name, english_revision, english_html, "en"),
        parse_schedule_page(chinese_name, chinese_revision, chinese_html, "zh"),
    )


def fetch_all() -> list[VillagerSchedule]:
    metadata = page_metadata()
    schedules: list[VillagerSchedule] = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(fetch_villager, item): item[0] for item in metadata
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            schedules.append(future.result())
            print(
                f"[{completed:02d}/{len(metadata)}] 已解析 {futures[future]}",
                file=sys.stderr,
                flush=True,
            )
    order = {name: index for index, name in enumerate(EXPECTED_ENGLISH_NAMES)}
    return sorted(schedules, key=lambda item: order[item.english_name])


def structure_signature(page: SchedulePage) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(len(group.steps) for group in section.groups) for section in page.sections
    )


def structure_mismatches(
    schedules: Iterable[VillagerSchedule],
) -> list[str]:
    mismatches: list[str] = []
    for item in schedules:
        english = structure_signature(item.english)
        chinese = structure_signature(item.chinese)
        if english != chinese:
            mismatches.append(
                f"{item.english_name}/{item.chinese_name}: en={english}, zh={chinese}"
            )
    return mismatches


def mismatched_english_names(
    schedules: Iterable[VillagerSchedule],
) -> set[str]:
    return {
        item.english_name
        for item in schedules
        if structure_signature(item.english) != structure_signature(item.chinese)
    }


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def anchor(index: int, chinese_name: str, english_name: str) -> str:
    del index, chinese_name
    return f"npc-schedule-{english_name.lower()}"


def append_source_page(
    lines: list[str], page: SchedulePage, source_label: str
) -> None:
    lines.extend(
        [
            f"#### {source_label}",
            "",
            f"> {len(page.sections)} 个分区、{page.group_count} 个条件分支、"
            f"{page.step_count} 行。",
            "",
        ]
    )
    for note in page.notes:
        lines.append(f"- {note}")
    if page.notes:
        lines.append("")

    if not page.sections:
        lines.extend(["源页没有分时表；以上文字即该源的完整日程说明。", ""])
    for section in page.sections:
        lines.extend([f"##### {section.title}", ""])
        for group in section.groups:
            lines.extend(
                [
                    f"###### {group.condition}",
                    "",
                    "| 时间 | 地点/行动 |",
                    "|------|------|",
                ]
            )
            for step in group.steps:
                lines.append(
                    f"| {markdown_escape(step.time)} | "
                    f"{markdown_escape(step.location)} |"
                )
            lines.append("")


def render_document(schedules: list[VillagerSchedule]) -> str:
    observed_mismatches = mismatched_english_names(schedules)
    if observed_mismatches != EXPECTED_STRUCTURE_MISMATCHES:
        raise AssertionError(
            "中英文结构差异集合偏离审计基线："
            f"expected={sorted(EXPECTED_STRUCTURE_MISMATCHES)}, "
            f"actual={sorted(observed_mismatches)}"
        )

    en_section_count = sum(len(item.english.sections) for item in schedules)
    en_group_count = sum(item.english.group_count for item in schedules)
    en_step_count = sum(item.english.step_count for item in schedules)
    zh_section_count = sum(len(item.chinese.sections) for item in schedules)
    zh_group_count = sum(item.chinese.group_count for item in schedules)
    zh_step_count = sum(item.chinese.step_count for item in schedules)

    lines = [
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > "
        "[星露谷物语概览](../游戏概览.md) > [NPC数据总览](./NPC数据总览.md) > NPC日程数据总览",
        "",
        "# NPC日程数据总览 — 星露谷物语",
        "",
        "> 游戏版本：Stardew Valley PC v1.6.15",
        ">",
        "> 数据来源：英文 Stardew Valley Wiki 个人页为 PC v1.6.15 完整性主源；"
        "中文个人页为中文记录源",
        ">",
        "> 生成时逐人固定中英文 revision；两种语言的全部说明、分区、条件和时间地点行均保留",
        "",
        "## 数据覆盖声明",
        "",
        "| 项目 | 内容 |",
        "|------|------|",
        "| 数据全集定义 | 官方 Villagers 名册中 34 位可送礼居民个人页的完整日程章节 |",
        "| 预计居民数 | 34 |",
        "| 实际居民数 | 34 |",
        "| 数量差异 | 0 |",
        f"| 英文主源 | {en_section_count} 个分区 / {en_group_count} 个条件分支 / "
        f"{en_step_count} 行 |",
        f"| 中文记录源 | {zh_section_count} 个分区 / {zh_group_count} 个条件分支 / "
        f"{zh_step_count} 行 |",
        f"| 双源保留总量 | {en_section_count + zh_section_count} 个分区 / "
        f"{en_group_count + zh_group_count} 个条件分支 / "
        f"{en_step_count + zh_step_count} 行 |",
        "| 必填字段 | 居民、来源 revision、分区、条件、时间、地点/行动 |",
        "| 中英文结构一致 | 28/34 人 |",
        "| 已审计结构差异 | 6/34 人：山姆、塞巴斯蒂安、阿比盖尔、海莉、玛鲁、刘易斯 |",
        "| 验收状态 | **日程子域已完成**；节日地图内固定站位由节日数据域维护 |",
        "",
        "### 读取与优先级说明",
        "",
        "英文个人页已经按每个季节内从高到低排列分支；先满足的分支覆盖后续常规日程。"
        "游戏原始选择优先级还区分绿雨、婚后、被动节日、日期、爱心、巴士、雨天、"
        "季节星期与默认分支。本文保留个人页给出的完整顺序，不自行合并相似路线。",
        "",
        "姜岛度假村属于个人页的通用随机覆盖说明；节日、诊所预约等排除条件同样保留在"
        "每人说明中。固定地点且没有分时表的居民以完整文字说明收录，不伪造时间行。"
        "中英文发生冲突时，以英文主源判断 PC v1.6.15 行为；中文记录仍原样保留，"
        "用于检索、对照和后续翻译校正。",
        "",
        "## 居民索引与数量对账",
        "",
        "| # | 居民 | 英文主源（分区/分支/行） | 中文源（分区/分支/行） | 结构 | 中文 revision | 英文 revision |",
        "|:--:|------|:--:|:--:|:--:|:--:|:--:|",
    ]

    for index, item in enumerate(schedules, 1):
        zh_revision = item.chinese.revision.revision_id
        en_revision = item.english.revision.revision_id
        zh_url = (
            "https://zh.stardewvalleywiki.com/mediawiki/index.php?title="
            f"{quote(item.chinese_name)}&oldid={zh_revision}"
        )
        en_url = (
            "https://stardewvalleywiki.com/mediawiki/index.php?title="
            f"{quote(item.english_name)}&oldid={en_revision}"
        )
        lines.append(
            f"| {index} | [{item.chinese_name}（{item.english_name}）]"
            f"(#{anchor(index, item.chinese_name, item.english_name)}) | "
            f"{len(item.english.sections)}/{item.english.group_count}/"
            f"{item.english.step_count} | {len(item.chinese.sections)}/"
            f"{item.chinese.group_count}/{item.chinese.step_count} | "
            f"{'差异已审计' if item.english_name in observed_mismatches else '一致'} | "
            f"[zh {zh_revision}]({zh_url}) | "
            f"[en {en_revision}]({en_url}) |"
        )

    lines.extend(["", "## 逐人日程全集", ""])
    for index, item in enumerate(schedules, 1):
        lines.extend(
            [
                f'<a id="{anchor(index, item.chinese_name, item.english_name)}"></a>',
                "",
                f"### {index:02d}. {item.chinese_name}（{item.english_name}）",
                "",
                f"> 来源：中文 revision {item.chinese.revision.revision_id}；"
                f"英文 revision {item.english.revision.revision_id}",
                ">",
                "> 结构判定："
                + (
                    "中英文结构差异已审计；两源完整并列，行为判断以英文主源为准"
                    if item.english_name in observed_mismatches
                    else "中英文分区、条件组和行数签名一致；两源仍完整并列"
                ),
                "",
            ]
        )
        append_source_page(lines, item.chinese, "中文记录源（完整保留）")
        append_source_page(lines, item.english, "英文完整性主源（PC v1.6.15 判定基准）")

    lines.extend(
        [
            "## 来源与审计方法",
            "",
            "- [Villagers — 官方 34 位可送礼居民名册]"
            "(https://stardewvalleywiki.com/Villagers)",
            "- [Modding:Schedule data — 日程键优先级与时间地点字段]"
            "(https://stardewvalleywiki.com/Modding:Schedule_data)",
            "- 每位居民的中英文固定 revision 链接见索引表。",
            "- 生成器要求 34/34 人存在日程章节，并逐人比较中英文分区/分支/行数签名；"
            "所有中英文记录均进入本文。",
            "- 任何居民缺页、缺日程章节、空条件表，或结构差异居民集合偏离已审计的 6 人"
            "基线，都会使生成失败。",
            "",
            "---",
            "",
            "[上一篇：NPC关系数值总览](./NPC关系数值总览.md) · "
            "[返回NPC数据总览](./NPC数据总览.md) · "
            "[返回游戏概览](../游戏概览.md) · "
            "[下一篇：作物数据总览](./作物数据总览.md)",
            "",
        ]
    )
    return "\n".join(lines)


def audit_summary(schedules: list[VillagerSchedule]) -> str:
    mismatches = structure_mismatches(schedules)
    return (
        f"villagers={len(schedules)}/34, "
        f"en_sections={sum(len(item.english.sections) for item in schedules)}, "
        f"en_groups={sum(item.english.group_count for item in schedules)}, "
        f"en_steps={sum(item.english.step_count for item in schedules)}, "
        f"zh_sections={sum(len(item.chinese.sections) for item in schedules)}, "
        f"zh_groups={sum(item.chinese.group_count for item in schedules)}, "
        f"zh_steps={sum(item.chinese.step_count for item in schedules)}, "
        f"structure_mismatches={len(mismatches)}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--probe", action="store_true", help="只抓取并打印结构差异")
    mode.add_argument("--write", action="store_true", help="生成文档")
    mode.add_argument("--check", action="store_true", help="检查文档是否与当前来源一致")
    args = parser.parse_args()

    schedules = fetch_all()
    print("audit:", audit_summary(schedules))
    mismatches = structure_mismatches(schedules)
    if args.probe:
        for mismatch in mismatches:
            print("mismatch:", mismatch)
        observed = mismatched_english_names(schedules)
        return 0 if observed == EXPECTED_STRUCTURE_MISMATCHES else 1

    document = render_document(schedules)
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
