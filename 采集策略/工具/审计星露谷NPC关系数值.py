#!/usr/bin/env python3
"""审计《星露谷物语》NPC 关系数值文档的覆盖、关键口径和本地导航。"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[2]
GAME_ROOT = REPO_ROOT / "牧场经营类" / "星露谷物语"
RELATION_DOC = GAME_ROOT / "数值数据" / "NPC关系数值总览.md"
SCHEDULE_DOC = GAME_ROOT / "数值数据" / "NPC日程数据总览.md"

REQUIRED_RULE_FAMILIES = [
    "点数换算、显示与上限",
    "日常增减行为",
    "礼物计算、倍率与次数",
    "每日衰减",
    "电影、节日与社区中心",
    "恋爱与分手",
    "婚姻、配偶与嫉妒",
    "科罗布斯室友",
    "离婚、驱逐与记忆消除",
]

REQUIRED_FACTS = [
    "1 颗心 = 250 好感点",
    "2,749",
    "2,249",
    "3,749",
    "×1.1 / ×1.25 / ×1.5",
    "-2 / -10 / -20",
    "+1,056",
    "+750",
    "20%–40%",
    "1,250 点（5 心）",
    "50,000g",
    "30,000g",
    "×0.66（降低 34%）",
]

REQUIRED_SOURCE_REVISIONS = [
    "Friendship&oldid=193702",
    "Friendship_101&oldid=192434",
    "Marriage&oldid=192857",
    "Bouquet&oldid=193753",
    "Wilted_Bouquet&oldid=192666",
    "Krobus&oldid=192255",
    "Void_Ghost_Pendant&oldid=192321",
    "Movie_Theater&oldid=193933",
    "Luau&oldid=187204",
]

NAVIGATION_DOCS = [
    GAME_ROOT / "数值数据" / "NPC数据总览.md",
    GAME_ROOT / "数值数据" / "NPC礼物数据总览.md",
    RELATION_DOC,
    SCHEDULE_DOC,
    GAME_ROOT / "机制分析" / "NPC社交系统.md",
    GAME_ROOT / "游戏概览.md",
]

AUDITED_DOCS = NAVIGATION_DOCS + [
    REPO_ROOT / "采集策略" / "全库补全与导航重构计划.md",
    REPO_ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md",
]


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item not in text]
    if missing:
        raise AssertionError(f"{label} missing: {missing}")


def markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)


def heading_slug(heading: str) -> str:
    """近似 GitHub/CommonMark 的自动标题锚点规则，支持中文标题。"""
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
    text = path.read_text(encoding="utf-8")
    checked = 0
    checked_anchors = 0
    broken: list[str] = []
    for _, target in markdown_links(text):
        if target.startswith(("http://", "https://", "#")):
            continue
        relative_target, _, fragment = target.partition("#")
        if not relative_target:
            continue
        checked += 1
        resolved = (path.parent / relative_target).resolve()
        if not resolved.exists():
            broken.append(f"{path.relative_to(REPO_ROOT)} -> {target}")
            continue
        if fragment and resolved.suffix.lower() == ".md":
            checked_anchors += 1
            decoded_fragment = unquote(fragment).lower()
            if decoded_fragment not in document_anchors(resolved):
                broken.append(
                    f"{path.relative_to(REPO_ROOT)} -> missing anchor {target}"
                )
    return checked, checked_anchors, broken


def main() -> None:
    relation_text = RELATION_DOC.read_text(encoding="utf-8")

    family_rows = re.findall(r"^\| \d+ \| ([^|]+?) \|", relation_text, re.MULTILINE)
    if family_rows[:9] != REQUIRED_RULE_FAMILIES:
        raise AssertionError(
            f"rule family mismatch: expected={REQUIRED_RULE_FAMILIES}, actual={family_rows[:9]}"
        )

    assert_contains(relation_text, REQUIRED_FACTS, "required facts")
    assert_contains(relation_text, REQUIRED_SOURCE_REVISIONS, "source revisions")
    assert_contains(
        relation_text,
        [
            "| 规则族预计数 | 9 |",
            "| 规则族实际数 | 9 |",
            "| 数量差异 | 0 |",
            "| 字段完整率 | 9 / 9，100% |",
            "| 未解决来源冲突 | 0",
        ],
        "coverage statement",
    )

    link_count = 0
    anchor_count = 0
    broken_links: list[str] = []
    for document in AUDITED_DOCS:
        checked, checked_anchors, broken = check_local_links(document)
        link_count += checked
        anchor_count += checked_anchors
        broken_links.extend(broken)
    if broken_links:
        raise AssertionError(f"broken local links: {broken_links}")

    required_cross_links = [
        (NAVIGATION_DOCS[0], "./NPC关系数值总览.md"),
        (NAVIGATION_DOCS[0], "./NPC日程数据总览.md"),
        (NAVIGATION_DOCS[1], "./NPC关系数值总览.md"),
        (RELATION_DOC, "./NPC日程数据总览.md"),
        (SCHEDULE_DOC, "./NPC数据总览.md"),
        (SCHEDULE_DOC, "./NPC关系数值总览.md"),
        (NAVIGATION_DOCS[4], "../数值数据/NPC关系数值总览.md"),
        (NAVIGATION_DOCS[4], "../数值数据/NPC日程数据总览.md"),
        (NAVIGATION_DOCS[5], "./数值数据/NPC关系数值总览.md"),
        (NAVIGATION_DOCS[5], "./数值数据/NPC日程数据总览.md"),
    ]
    for document, target in required_cross_links:
        text = document.read_text(encoding="utf-8")
        if target not in text:
            raise AssertionError(f"missing cross-link: {document.name} -> {target}")

    print(
        "audit: "
        f"rule_families={len(family_rows[:9])}/9, "
        f"required_facts={len(REQUIRED_FACTS)}/{len(REQUIRED_FACTS)}, "
        f"source_revisions={len(REQUIRED_SOURCE_REVISIONS)}/{len(REQUIRED_SOURCE_REVISIONS)}, "
        f"navigation_docs={len(NAVIGATION_DOCS)}, audited_docs={len(AUDITED_DOCS)}, "
        f"local_links={link_count}, anchors={anchor_count}, "
        "broken_links=0, unresolved_conflicts=0"
    )


if __name__ == "__main__":
    main()
