#!/usr/bin/env python3
"""审计《符文工房3》的文件集合、概览、连续导航、数据状态和官方来源。"""

from __future__ import annotations

import argparse
import os
import re
import unicodedata
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "符文工房3"
OVERVIEW = GAME / "游戏概览.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "符文工房3.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
README = ROOT / "README.md"


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
    ChildDocument("NPC名册数据总览", GAME / "数值数据" / "NPC名册数据总览.md"),
    ChildDocument("NPC礼物数据总览", GAME / "数值数据" / "NPC礼物数据总览.md"),
    ChildDocument("NPC日程数据总览", GAME / "数值数据" / "NPC日程数据总览.md"),
    ChildDocument("委托任务数据总览", GAME / "数值数据" / "委托任务数据总览.md"),
    ChildDocument("作物数据总览", GAME / "数值数据" / "作物数据总览.md"),
    ChildDocument("加工配方数据总览", GAME / "数值数据" / "加工配方数据总览.md"),
    ChildDocument("动物怪物数据总览", GAME / "数值数据" / "动物怪物数据总览.md"),
    ChildDocument("怪物数据总览", GAME / "数值数据" / "怪物数据总览.md"),
    ChildDocument("技能属性数据总览", GAME / "数值数据" / "技能属性数据总览.md"),
    ChildDocument("节日活动数据总览", GAME / "数值数据" / "节日活动数据总览.md"),
    ChildDocument("角色属性战斗数据总览", GAME / "数值数据" / "角色属性战斗数据总览.md"),
    ChildDocument("道具装备数据总览", GAME / "数值数据" / "道具装备数据总览.md"),
    ChildDocument("变身系统", GAME / "特色文档" / "变身系统.md"),
    ChildDocument("团队与开发历程", GAME / "特色文档" / "团队与开发历程.md"),
    ChildDocument("角色弧线深度解析", GAME / "特色文档" / "角色弧线深度解析.md"),
    ChildDocument("委托任务系统", GAME / "特色文档" / "委托任务系统.md"),
    ChildDocument("新婚模式与外传", GAME / "特色文档" / "新婚模式与外传.md"),
]

DATA_DOCS = [child.path for child in CHILDREN if child.path.parent.name == "数值数据"]

OFFICIAL_SOURCES = [
    ("官方产品页", "https://www.runefactory.com/rf3/", "Rune Factory 3 Special"),
    ("官方在线手册", "https://manuals.marvelousgames.com/rf3sp/", "Web Manual"),
    ("农耕手册", "https://manuals.marvelousgames.com/rf3sp/08/", "Farming"),
    ("合成手册", "https://manuals.marvelousgames.com/rf3sp/09/", "Synthesizing"),
    ("战斗手册", "https://manuals.marvelousgames.com/rf3sp/10/", "Battling Monsters"),
    ("同伴手册", "https://manuals.marvelousgames.com/rf3sp/11/", "Fighting Together"),
    ("婚恋手册", "https://manuals.marvelousgames.com/rf3sp/14/", "Romance & Marriage"),
]


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
        anchors.add(base if duplicate_index == 0 else f"{base}-{duplicate_index}")
        duplicates[base] = duplicate_index + 1
    return anchors


def check_local_links(path: Path) -> tuple[int, int, list[str]]:
    checked = 0
    checked_anchors = 0
    broken: list[str] = []
    for _, target in markdown_links(path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://")):
            continue
        relative_target, _, fragment = target.partition("#")
        checked += 1
        resolved = path if not relative_target else (path.parent / unquote(relative_target)).resolve()
        if not resolved.exists():
            broken.append(f"{path.relative_to(ROOT)} -> {target}")
            continue
        if fragment and resolved.suffix.lower() == ".md":
            checked_anchors += 1
            if unquote(fragment).lower() not in document_anchors(resolved):
                broken.append(f"{path.relative_to(ROOT)} -> missing anchor {target}")
    return checked, checked_anchors, broken


def expected_footer(index: int) -> tuple[str, str, str]:
    current = CHILDREN[index]
    previous = CHILDREN[index - 1] if index else ChildDocument("游戏概览", OVERVIEW)
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


def check_official_sources() -> None:
    failures: list[str] = []
    for label, url, marker in OFFICIAL_SOURCES:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 GameDocs-v2.9-audit/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", "replace")
                status = response.status
            print(f"SOURCE {label} status={status} marker={marker in body}")
            if status != 200 or marker not in body:
                failures.append(f"{label}: status={status}, marker={marker in body}")
        except Exception as error:  # 网络错误也必须显示为真实失败
            failures.append(f"{label}: {type(error).__name__}: {error}")
    print(
        f"SOURCE_SUMMARY expected={len(OFFICIAL_SOURCES)} "
        f"actual={len(OFFICIAL_SOURCES) - len(failures)} failures={len(failures)}"
    )
    if failures:
        raise AssertionError(f"官方来源复现失败：{failures}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-sources", action="store_true")
    args = parser.parse_args()

    if args.check_sources:
        check_official_sources()

    errors: list[str] = []
    actual_game_docs = set(GAME.rglob("*.md"))
    expected_game_docs = {OVERVIEW, *(child.path for child in CHILDREN)}
    if actual_game_docs != expected_game_docs:
        missing = sorted(path.relative_to(ROOT) for path in expected_game_docs - actual_game_docs)
        extra = sorted(path.relative_to(ROOT) for path in actual_game_docs - expected_game_docs)
        errors.append(f"游戏文件集合漂移：missing={missing}, extra={extra}")

    overview = OVERVIEW.read_text(encoding="utf-8")
    overview_targets = [
        unquote(target)
        for _, target in markdown_links(overview)
        if target.startswith("./") and target.endswith(".md")
    ]
    expected_targets = [markdown_target(OVERVIEW, child.path) for child in CHILDREN]
    if overview_targets != expected_targets:
        errors.append(
            f"概览顺序或覆盖不符：actual={len(overview_targets)}/28, expected=28/28"
        )
    if "内容文档数: 28 份" not in overview or "v2.9 状态: **采集中**" not in overview:
        errors.append("概览未声明实际 28 份内容文档及 v2.9 采集中状态")

    overview_first = next(line for line in overview.splitlines() if line.strip())
    expected_overview_first = (
        "[项目首页](../../README.md) > [牧场经营类](../_index.md) > 符文工房3"
    )
    breadcrumb_count = int(overview_first == expected_overview_first)
    if not breadcrumb_count:
        errors.append("游戏概览缺少顶部面包屑")

    footer_count = 0
    for index, child in enumerate(CHILDREN):
        text = child.path.read_text(encoding="utf-8")
        nonempty = [line.strip() for line in text.splitlines() if line.strip()]
        if all(
            marker in nonempty[0]
            for marker in ("[项目首页]", "[牧场经营类]", "[符文工房3概览]")
        ):
            breadcrumb_count += 1
        else:
            errors.append(f"缺少顶部面包屑：{child.path.relative_to(ROOT)}")
        footer_parts = expected_footer(index)
        positions = [nonempty[-1].find(part) for part in footer_parts]
        if all(position >= 0 for position in positions) and positions == sorted(positions):
            footer_count += 1
        else:
            errors.append(f"连续导航不匹配：{child.path.relative_to(ROOT)}")

    coverage_declarations = sum(
        "数据覆盖声明" in path.read_text(encoding="utf-8") for path in DATA_DOCS
    )
    unresolved_docs = sum(
        bool(
            re.search(
                r"代表性|推测|待补充|待核实|需(?:要|进一步)数据挖掘|完整.*需",
                path.read_text(encoding="utf-8"),
            )
        )
        for path in DATA_DOCS
    )

    if not AUDIT.exists():
        errors.append("缺少符文工房3 v2.9 审计记录")
        audit = ""
    else:
        audit = AUDIT.read_text(encoding="utf-8")
    for value in (
        "当前状态：**采集中**",
        "数据文档完成状态 | 3/13",
        "数据覆盖声明 | 5/13",
        "驯养与产出怪物",
        "普通敌人、Boss、属性、掉落和区域名册",
        "下一阶段继续 NPC 日程数据",
    ):
        if value not in audit:
            errors.append(f"审计记录缺少：{value}")

    plan = PLAN.read_text(encoding="utf-8")
    for value in ("符文工房3", "已闭合 28 份内容文档", "下一阶段继续 NPC 日程"):
        if value not in plan:
            errors.append(f"全库计划缺少：{value}")
    readme = README.read_text(encoding="utf-8")
    if "[符文工房3](./牧场经营类/符文工房3/游戏概览.md)" not in readme or "| 28 |" not in next(
        line for line in readme.splitlines() if "[符文工房3]" in line
    ):
        errors.append("README 未同步符文工房3实际 28 份内容文档")

    audited_docs = sorted(GAME.rglob("*.md")) + [PLAN]
    if AUDIT.exists():
        audited_docs.append(AUDIT)
    local_links = 0
    anchor_links = 0
    broken: list[str] = []
    for document in audited_docs:
        checked, checked_anchors, failures = check_local_links(document)
        local_links += checked
        anchor_links += checked_anchors
        broken.extend(failures)
    if broken:
        errors.append(f"本地链接或锚点失效：{broken}")

    print(
        f"BASELINE game_docs={len(actual_game_docs)}/29, children={len(CHILDREN)}/28, "
        f"overview_links={len(overview_targets)}/28, breadcrumbs={breadcrumb_count}/29, "
        f"continuous_nav={footer_count}/28, coverage_declarations={coverage_declarations}/13, "
        f"unresolved_data_docs={unresolved_docs}/13, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links={len(broken)}"
    )
    if errors:
        raise AssertionError("\n".join(errors))


if __name__ == "__main__":
    main()
