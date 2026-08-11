#!/usr/bin/env python3
"""审计星露谷剧情分析、角色弧线、爷爷/完美与社区中心/Joja 专题。"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "星露谷物语"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷剧情路线专题.py"
STORY = GAME / "机制分析" / "剧情与故事系统.md"
ARCS = GAME / "特色文档" / "角色弧线深度解析.md"
GRANDPA = GAME / "特色文档" / "爷爷评价与完美追踪.md"
ROUTE = GAME / "特色文档" / "社区中心与Joja路线.md"
CRAFTING = GAME / "数值数据" / "制作配方数据总览.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]

SOURCE_REVISIONS = {
    "Grandpa": 182923,
    "Perfection": 184492,
    "Statue_Of_Perfection": 186368,
    "Statue_Of_True_Perfection": 182682,
    "The_Summit": 193935,
    "Bundles": 193528,
    "Remixed_Bundles": 191838,
    "Community_Center": 193096,
    "Joja_Community_Development_Form": 187019,
    "Movie_Theater": 193933,
}

SOURCE_ANCHORS = {
    "source-grandpa",
    "source-perfection",
    "source-statue-of-perfection",
    "source-statue-of-true-perfection",
    "source-the-summit",
    "source-bundles",
    "source-remixed-bundles",
    "source-community-center",
    "source-joja-community-development-form",
    "source-movie-theater",
}

FORBIDDEN_STALE_TEXT = (
    "~3%",
    "~15%",
    "~30%",
    "工艺室 | 完成春季采集",
    "修复矿区矿车",
    "高效凑满12分推荐路线",
    "最难完成",
    "~730,000g",
    "推荐选择",
    "Eric Barone在GameDeveloper",
    "IGN十周年专访中",
    "Stardew Valley Wiki: Relationship System",
    "stardewvalley.fandom.com",
    "文档版本: v2.6",
    "销量: 3000万+",
)


def assert_contains(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    if missing:
        raise AssertionError(f"{label} 缺少：{missing}")


def heading_slug(heading: str) -> str:
    characters: list[str] = []
    for character in heading.strip().lower():
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


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def check_local_links(path: Path) -> tuple[int, int, list[str]]:
    checked = 0
    checked_anchors = 0
    broken: list[str] = []
    for target in markdown_links(path.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "#")):
            continue
        relative_target, _, fragment = target.partition("#")
        if not relative_target:
            continue
        checked += 1
        resolved = (path.parent / unquote(relative_target)).resolve()
        if not resolved.exists():
            broken.append(f"{path.relative_to(ROOT)} -> {target}")
        elif fragment and resolved.suffix.lower() == ".md":
            checked_anchors += 1
            if unquote(fragment).lower() not in document_anchors(resolved):
                broken.append(f"{path.relative_to(ROOT)} -> missing anchor {target}")
    return checked, checked_anchors, broken


def table_rows_and_urls(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    return (
        sum(line.startswith("|") for line in text.splitlines()),
        len(re.findall(r"https?://[^\s\)>]+", text)),
    )


def main() -> None:
    subprocess.run(
        [sys.executable, str(GENERATOR), "--check"],
        cwd=ROOT,
        check=True,
    )

    story = STORY.read_text(encoding="utf-8")
    arcs = ARCS.read_text(encoding="utf-8")
    grandpa = GRANDPA.read_text(encoding="utf-8")
    route = ROUTE.read_text(encoding="utf-8")
    crafting = CRAFTING.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")

    expected_shape = {
        STORY: (18, 0),
        ARCS: (15, 0),
        GRANDPA: (129, 5),
        ROUTE: (725, 5),
    }
    for path, expected in expected_shape.items():
        actual = table_rows_and_urls(path)
        if actual != expected:
            raise AssertionError(
                f"专题结构漂移：{path.relative_to(ROOT)} rows/urls={actual}/{expected}"
            )

    assert_contains(
        grandpa,
        [
            "固定来源 | 预计 5 / 实际 5",
            "预计 10 / 实际 10；表体记录预计 49 / 实际 49",
            "规则事实块 | 预计 32 / 实际 32",
            "爷爷评分条件 | 预计 19 / 实际 19",
            "蜡烛结果档位 | 预计 4 / 实际 4",
            "完美度类别 | 预计 11 / 实际 11",
            "完美雕像 | 预计 2 / 实际 2",
            "Crafting Recipes Made",
            "Wedding Ring / is not required",
            "| 149 | 10% |",
            "制作数据域仍维护 150/150 个配方对象",
            "[鱼类数据总览](../数值数据/鱼类数据总览.md)",
            "[出货收集数据总览](../数值数据/出货收集数据总览.md)",
            "鱼类 77/77、图鉴 72/72 与 Full Shipment 154/154 已移交独立全集",
            "验收状态 | **已完成**",
        ],
        "爷爷/完美专题",
    )
    assert_contains(
        crafting,
        [
            "预计条目数 | 150（PC 1.6.15 原始数据键）",
            "实际收录数 | 150（中英文展示行与原始键一一映射）",
            "数量差异 | 0",
        ],
        "制作配方全集",
    )
    assert_contains(
        route,
        [
            "固定来源 | 预计 5 / 实际 5",
            "预计 95 / 实际 95；表体记录预计 440 / 实际 440",
            "规则事实块 | 预计 68 / 实际 68",
            "标准房间收集包 | 预计 30 / 实际 30",
            "遗失收集包 | 预计 1 / 实际 1",
            "混合模式候选包 | 预计 47 / 实际 47",
            "验收状态 | **已完成**",
        ],
        "社区中心/Joja 专题",
    )

    combined_data = grandpa + route
    missing_anchors = sorted(SOURCE_ANCHORS - document_anchors(GRANDPA) - document_anchors(ROUTE))
    if missing_anchors:
        raise AssertionError(f"专题固定源锚点缺失：{missing_anchors}")
    missing_revisions = [
        f"{title}:{revision}"
        for title, revision in SOURCE_REVISIONS.items()
        if f"oldid={revision}" not in combined_data
    ]
    if missing_revisions:
        raise AssertionError(f"固定 revision 缺失：{missing_revisions}")

    npc_documents = [
        "NPC数据总览.md",
        "NPC礼物数据总览.md",
        "NPC关系数值总览.md",
        "NPC日程数据总览.md",
        "NPC事件数据总览.md",
    ]
    for document in npc_documents:
        if document not in story or document not in arcs:
            raise AssertionError(f"分析入口未同时链接 NPC 全集：{document}")
    for anchor in (
        "source-bundles",
        "source-remixed-bundles",
        "source-community-center",
        "source-joja-community-development-form",
        "source-movie-theater",
        "source-grandpa",
        "source-perfection",
        "source-the-summit",
    ):
        if anchor not in story:
            raise AssertionError(f"剧情机制入口缺少专题锚点：{anchor}")
    for anchor in (
        "npc-event-shane",
        "npc-event-linus",
        "npc-event-george",
        "npc-event-kent",
        "npc-event-pam",
        "npc-event-penny",
        "npc-event-krobus",
    ):
        if anchor not in arcs:
            raise AssertionError(f"角色弧线入口缺少事件锚点：{anchor}")

    combined_four = story + arcs + grandpa + route
    stale = [value for value in FORBIDDEN_STALE_TEXT if value in combined_four]
    if stale:
        raise AssertionError(f"四份专题仍含旧口径：{stale}")
    assert_contains(
        story + arcs,
        [
            "不重复保存",
            "不承担 NPC 全集",
            "事实和解释",
            "不使用未核验的开发者引语",
        ],
        "分析/数据边界",
    )

    assert_contains(
        overview,
        [
            "总大小: 约 2,520.6 KB",
            "剧情与故事系统](./机制分析/剧情与故事系统.md) | 8.1 KB",
            "角色弧线深度解析](./特色文档/角色弧线深度解析.md) | 7.2 KB",
            "爷爷评价与完美追踪](./特色文档/爷爷评价与完美追踪.md) | 17.3 KB",
            "社区中心与Joja路线](./特色文档/社区中心与Joja路线.md) | 111.2 KB",
        ],
        "游戏概览",
    )
    assert_contains(
        audit,
        [
            "非数值文档 16 份中，11 份已完成、1 份部分完成、4 份采集中",
            "剧情路线专题固定 10/10 个 revision、105 张源表、489 行数据与 100 个规则事实块",
            "标准收集包 30/30、遗失收集包 1/1、混合模式候选包 47/47",
            "鱼类 77/77、图鉴 72/72、可烟熏鱼 71/71",
            "Full Shipment 154/154、Polyculture 28/28、Monoculture 33/33",
            "17 份数值数据文档已全部完成",
            "下一阶段进入时间/经济重叠域",
        ],
        "审计记录",
    )
    assert_contains(
        plan,
        [
            "17 份数值数据文档与全游戏导航链已完成",
            "鱼类/出货全集已完成",
            "下一阶段为剩余非数值文档逐域重建",
            "地图/战斗重叠域已完成",
            "先处理时间/经济重叠域",
        ],
        "执行计划",
    )

    local_links = 0
    anchor_links = 0
    broken: list[str] = []
    for document in AUDITED_DOCS:
        checked, checked_anchors, failures = check_local_links(document)
        local_links += checked
        anchor_links += checked_anchors
        broken.extend(failures)
    if broken:
        raise AssertionError(f"本地链接或锚点失效：{broken}")

    print(
        "audit: fixed_revisions=10/10, source_tables=105/105, source_rows=489/489, "
        "facts=100/100, grandpa=19+4+11+2, standard_bundles=30/30, missing_bundle=1/1, "
        "remixed_candidates=47/47, analysis_docs=2/2, stale_claims=0, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0"
    )


if __name__ == "__main__":
    main()
