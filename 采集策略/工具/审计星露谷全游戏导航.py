#!/usr/bin/env python3
"""审计《星露谷物语》全游戏文档顺序、导航、历史汇总归属与本地链接。"""

from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "星露谷物语"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"


@dataclass(frozen=True)
class ChildDocument:
    title: str
    path: Path


CHILDREN = [
    ChildDocument("NPC社交系统", GAME / "机制分析" / "NPC社交系统.md"),
    ChildDocument("作物种植系统", GAME / "机制分析" / "作物种植系统.md"),
    ChildDocument("剧情与故事系统", GAME / "机制分析" / "剧情与故事系统.md"),
    ChildDocument("加工制造系统", GAME / "机制分析" / "加工制造系统.md"),
    ChildDocument("地图场景系统", GAME / "机制分析" / "地图场景系统.md"),
    ChildDocument("战斗探索系统", GAME / "机制分析" / "战斗探索系统.md"),
    ChildDocument("时间季节系统", GAME / "机制分析" / "时间季节系统.md"),
    ChildDocument("畜牧养殖系统", GAME / "机制分析" / "畜牧养殖系统.md"),
    ChildDocument("经济系统", GAME / "机制分析" / "经济系统.md"),
    ChildDocument("道具升级系统", GAME / "机制分析" / "道具升级系统.md"),
    ChildDocument("NPC数据总览", GAME / "数值数据" / "NPC数据总览.md"),
    ChildDocument("NPC礼物数据总览", GAME / "数值数据" / "NPC礼物数据总览.md"),
    ChildDocument("NPC关系数值总览", GAME / "数值数据" / "NPC关系数值总览.md"),
    ChildDocument("NPC日程数据总览", GAME / "数值数据" / "NPC日程数据总览.md"),
    ChildDocument("NPC事件数据总览", GAME / "数值数据" / "NPC事件数据总览.md"),
    ChildDocument("作物数据总览", GAME / "数值数据" / "作物数据总览.md"),
    ChildDocument("加工配方数据总览", GAME / "数值数据" / "加工配方数据总览.md"),
    ChildDocument("烹饪配方数据总览", GAME / "数值数据" / "烹饪配方数据总览.md"),
    ChildDocument("制作配方数据总览", GAME / "数值数据" / "制作配方数据总览.md"),
    ChildDocument("动物数据总览", GAME / "数值数据" / "动物数据总览.md"),
    ChildDocument("怪物数据总览", GAME / "数值数据" / "怪物数据总览.md"),
    ChildDocument("技能属性数据总览", GAME / "数值数据" / "技能属性数据总览.md"),
    ChildDocument("节日活动数据总览", GAME / "数值数据" / "节日活动数据总览.md"),
    ChildDocument("角色属性战斗数据总览", GAME / "数值数据" / "角色属性战斗数据总览.md"),
    ChildDocument("道具装备数据总览", GAME / "数值数据" / "道具装备数据总览.md"),
    ChildDocument("团队与开发历程", GAME / "特色文档" / "团队与开发历程.md"),
    ChildDocument("角色弧线深度解析", GAME / "特色文档" / "角色弧线深度解析.md"),
    ChildDocument("爷爷评价与完美追踪", GAME / "特色文档" / "爷爷评价与完美追踪.md"),
    ChildDocument("社区中心与Joja路线", GAME / "特色文档" / "社区中心与Joja路线.md"),
    ChildDocument("齐先生的挑战与姜岛", GAME / "特色文档" / "齐先生的挑战与姜岛.md"),
    ChildDocument(
        "经济、种植与畜牧历史汇总",
        GAME / "stardew-valley-economy-farming-animal-data.md",
    ),
]

LEGACY = CHILDREN[-1].path
AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]
NONDATA_BASELINE = {
    LEGACY: (19, 0, "已完成"),
    GAME / "机制分析" / "NPC社交系统.md": (7, 5, "已完成"),
    GAME / "机制分析" / "作物种植系统.md": (7, 6, "已完成"),
    GAME / "机制分析" / "剧情与故事系统.md": (77, 1, "采集中"),
    GAME / "机制分析" / "加工制造系统.md": (53, 14, "部分完成"),
    GAME / "机制分析" / "地图场景系统.md": (213, 8, "采集中"),
    GAME / "机制分析" / "战斗探索系统.md": (157, 11, "部分完成"),
    GAME / "机制分析" / "时间季节系统.md": (155, 7, "采集中"),
    GAME / "机制分析" / "畜牧养殖系统.md": (20, 2, "已完成"),
    GAME / "机制分析" / "经济系统.md": (243, 10, "采集中"),
    GAME / "机制分析" / "道具升级系统.md": (19, 0, "已完成"),
    GAME / "特色文档" / "团队与开发历程.md": (60, 4, "采集中"),
    GAME / "特色文档" / "角色弧线深度解析.md": (34, 18, "采集中"),
    GAME / "特色文档" / "爷爷评价与完美追踪.md": (209, 6, "采集中"),
    GAME / "特色文档" / "社区中心与Joja路线.md": (300, 6, "采集中"),
    GAME / "特色文档" / "齐先生的挑战与姜岛.md": (317, 9, "采集中"),
}


def markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)


def markdown_target(source: Path, target: Path) -> str:
    relative = Path(os.path.relpath(target, source.parent)).as_posix()
    if not relative.startswith("../"):
        relative = f"./{relative}"
    return relative


def heading_slug(heading: str) -> str:
    heading = heading.strip().lower()
    characters: list[str] = []
    for character in heading:
        if character in {"-", "_"}:
            characters.append(character)
        elif not unicodedata.category(character).startswith(("P", "S")):
            characters.append(character)
    return re.sub(r"\s+", "-", "".join(characters)).strip("-")


def document_anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors = {
        anchor.lower()
        for anchor in re.findall(r'<[a-zA-Z][^>]*\sid=["\']([^"\']+)["\']', text)
    }
    duplicates: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE):
        base = heading_slug(heading)
        duplicate_index = duplicates.get(base, 0)
        anchor = base if duplicate_index == 0 else f"{base}-{duplicate_index}"
        anchors.add(anchor)
        duplicates[base] = duplicate_index + 1
    return anchors


def check_local_links(path: Path) -> tuple[int, int, list[str]]:
    checked = 0
    checked_anchors = 0
    broken: list[str] = []
    for _, target in markdown_links(path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "#")):
            continue
        relative_target, _, fragment = target.partition("#")
        if not relative_target:
            continue
        checked += 1
        resolved = (path.parent / unquote(relative_target)).resolve()
        if not resolved.exists():
            broken.append(f"{path.relative_to(ROOT)} -> {target}")
            continue
        if fragment and resolved.suffix.lower() == ".md":
            checked_anchors += 1
            if unquote(fragment).lower() not in document_anchors(resolved):
                broken.append(f"{path.relative_to(ROOT)} -> missing anchor {target}")
    return checked, checked_anchors, broken


def expected_footer_parts(index: int) -> tuple[str, str, str]:
    current = CHILDREN[index]
    previous = CHILDREN[index - 1] if index > 0 else ChildDocument("游戏概览", OVERVIEW)
    following = (
        CHILDREN[index + 1]
        if index + 1 < len(CHILDREN)
        else ChildDocument("游戏概览", OVERVIEW)
    )
    return (
        f"[上一篇：{previous.title}]({markdown_target(current.path, previous.path)})",
        f"[返回游戏概览]({markdown_target(current.path, OVERVIEW)})",
        f"[下一篇：{following.title}]({markdown_target(current.path, following.path)})",
    )


def main() -> None:
    errors: list[str] = []

    actual_game_docs = set(GAME.rglob("*.md"))
    expected_game_docs = {OVERVIEW, *(child.path for child in CHILDREN)}
    if actual_game_docs != expected_game_docs:
        missing = sorted(path.relative_to(ROOT) for path in expected_game_docs - actual_game_docs)
        extra = sorted(path.relative_to(ROOT) for path in actual_game_docs - expected_game_docs)
        errors.append(f"游戏文档集合漂移：missing={missing}, extra={extra}")

    overview = OVERVIEW.read_text(encoding="utf-8")
    overview_targets = [
        unquote(target)
        for _, target in markdown_links(overview)
        if target.startswith("./") and target.endswith(".md")
    ]
    expected_targets = [markdown_target(OVERVIEW, child.path) for child in CHILDREN]
    if overview_targets != expected_targets:
        errors.append("游戏概览子文档链接顺序与 31 篇连续导航基线不一致")

    overview_first = next(line for line in overview.splitlines() if line.strip())
    if overview_first != "[项目首页](../../README.md) > [牧场经营类](../_index.md) > 星露谷物语":
        errors.append("游戏概览顶部面包屑不符合基线")

    breadcrumb_count = 1
    footer_count = 0
    for index, child in enumerate(CHILDREN):
        text = child.path.read_text(encoding="utf-8")
        nonempty = [line.strip() for line in text.splitlines() if line.strip()]
        first = nonempty[0]
        last = nonempty[-1]
        required_breadcrumb = (
            "[项目首页]",
            "[牧场经营类]",
            "[星露谷物语概览]",
        )
        if all(marker in first for marker in required_breadcrumb):
            breadcrumb_count += 1
        else:
            errors.append(f"缺少顶部面包屑：{child.path.relative_to(ROOT)}")

        footer_parts = expected_footer_parts(index)
        positions = [last.find(part) for part in footer_parts]
        if all(position >= 0 for position in positions) and positions == sorted(positions):
            footer_count += 1
        else:
            errors.append(
                f"连续导航不匹配：{child.path.relative_to(ROOT)}\n"
                f"  expected_parts={footer_parts}\n  actual={last}"
            )

    legacy = LEGACY.read_text(encoding="utf-8")
    required_legacy = [
        "历史迁移索引，不是数值数据源",
        "[经济系统](./机制分析/经济系统.md)",
        "[作物数据总览](./数值数据/作物数据总览.md)",
        "[动物数据总览](./数值数据/动物数据总览.md)",
        "[加工配方数据总览](./数值数据/加工配方数据总览.md)",
        "[道具装备数据总览](./数值数据/道具装备数据总览.md)",
        "[技能属性数据总览](./数值数据/技能属性数据总览.md)",
    ]
    missing_legacy = [value for value in required_legacy if value not in legacy]
    if missing_legacy:
        errors.append(f"历史汇总迁移索引缺项：{missing_legacy}")
    forbidden_legacy = [
        "### 1.3 主要收入来源",
        "### 2.2 完整作物列表",
        "### 3.1 动物种类",
        "#### 最高效畜牧自动化方案",
        "适用于游戏最新版本",
    ]
    stale_legacy = [value for value in forbidden_legacy if value in legacy]
    if stale_legacy:
        errors.append(f"历史汇总仍含旧数据副本或无版本口径：{stale_legacy}")

    audit = AUDIT.read_text(encoding="utf-8")
    for value in (
        "32/32 份文档具备顶部面包屑",
        "31/31 份子文档具备连续导航",
        "非数值文档审计矩阵",
        "根目录历史汇总已迁移为索引",
    ):
        if value not in audit:
            errors.append(f"审计记录缺少：{value}")

    status_counts = {"已完成": 0, "部分完成": 0, "采集中": 0}
    nondata_rows = 0
    nondata_urls = 0
    for path, (expected_rows, expected_urls, status) in NONDATA_BASELINE.items():
        text = path.read_text(encoding="utf-8")
        actual_rows = sum(line.startswith("|") for line in text.splitlines())
        actual_urls = len(re.findall(r"https?://[^\s\)>]+", text))
        if (actual_rows, actual_urls) != (expected_rows, expected_urls):
            errors.append(
                f"非数值文档证据漂移：{path.relative_to(ROOT)} "
                f"rows={actual_rows}/{expected_rows}, urls={actual_urls}/{expected_urls}"
            )
        status_counts[status] += 1
        nondata_rows += actual_rows
        nondata_urls += actual_urls
    expected_status_summary = "非数值文档 16 份中，5 份已完成、2 份部分完成、9 份采集中"
    if expected_status_summary not in audit:
        errors.append(f"审计记录缺少：{expected_status_summary}")
    if status_counts != {"已完成": 5, "部分完成": 2, "采集中": 9}:
        errors.append(f"非数值文档状态基线漂移：{status_counts}")

    plan = PLAN.read_text(encoding="utf-8")
    for value in (
        "全游戏导航链已完成",
        "下一阶段为剩余非数值文档逐域重建",
    ):
        if value not in plan:
            errors.append(f"执行计划缺少：{value}")

    local_links = 0
    anchor_links = 0
    broken: list[str] = []
    for document in AUDITED_DOCS:
        checked, checked_anchors, failures = check_local_links(document)
        local_links += checked
        anchor_links += checked_anchors
        broken.extend(failures)
    if broken:
        errors.append(f"本地链接或锚点失效：{broken}")

    if errors:
        raise AssertionError("\n".join(errors))

    print(
        f"audit: game_docs={len(actual_game_docs)}/32, breadcrumbs={breadcrumb_count}/32, "
        f"child_docs={len(CHILDREN)}/31, continuous_nav={footer_count}/31, "
        "overview_order=31/31, legacy_duplicates=0, nondata_docs=16/16, "
        f"nondata_rows={nondata_rows}/1890, external_urls={nondata_urls}/107, "
        "nondata_status=5_complete+2_partial+9_collecting, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0"
    )


if __name__ == "__main__":
    main()
