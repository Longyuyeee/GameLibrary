#!/usr/bin/env python3
"""审计《星露谷物语》作物数据覆盖、纠错与本地导航。"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[2]
GAME_ROOT = REPO_ROOT / "牧场经营类" / "星露谷物语"
CROP_DOC = GAME_ROOT / "数值数据" / "作物数据总览.md"
MECHANISM_DOC = GAME_ROOT / "机制分析" / "作物种植系统.md"
EVENT_DOC = GAME_ROOT / "数值数据" / "NPC事件数据总览.md"
OVERVIEW_DOC = GAME_ROOT / "游戏概览.md"
PLAN_DOC = REPO_ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT_DOC = REPO_ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"

AUDITED_DOCS = [
    CROP_DOC,
    MECHANISM_DOC,
    EVENT_DOC,
    OVERVIEW_DOC,
    PLAN_DOC,
    AUDIT_DOC,
]

REQUIRED_CROPS = [
    "胡萝卜（Carrot）",
    "金皮西葫芦（Summer Squash）",
    "西蓝花（Broccoli）",
    "霜瓜（Powdermelon）",
    "齐瓜（Qi Fruit）",
    "纤维（Fiber）",
    "茶叶（Tea Leaves）",
]

REQUIRED_REVISIONS = [
    "oldid=193672",
    "oldid=55247",
    "oldid=193551",
    "oldid=193245",
    "oldid=193299",
    "oldid=193217",
    "oldid=192690",
]

FORBIDDEN_STALE_TEXT = [
    "秋葵(Okra)",
    "山药(Yam) | Yam | 160 G | 秋季 | 1.6版本新增可巨大化",
    "甘蓝(Kale) | Kale | 110 G | 春季 | 1.6版本新增可巨大化",
    "自带浇水（无需洒水器）",
    "姜岛每天都下雨",
    "rawScore =",
    "金星概率 = 0.2",
]


def markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)


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
        resolved = (path.parent / relative_target).resolve()
        if not resolved.exists():
            broken.append(f"{path.relative_to(REPO_ROOT)} -> {target}")
            continue
        if fragment and resolved.suffix.lower() == ".md":
            checked_anchors += 1
            if unquote(fragment).lower() not in document_anchors(resolved):
                broken.append(
                    f"{path.relative_to(REPO_ROOT)} -> missing anchor {target}"
                )
    return checked, checked_anchors, broken


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item not in text]
    if missing:
        raise AssertionError(f"{label} missing: {missing}")


def main() -> None:
    crop_text = CROP_DOC.read_text(encoding="utf-8")
    mechanism_text = MECHANISM_DOC.read_text(encoding="utf-8")

    assert_contains(
        crop_text,
        [
            "| 预计命名作物 | 47 |",
            "| 实际命名作物 | 47 |",
            "| 数量差异 | 0 |",
            "| 随机种子系统 | 3/3",
            "| 必填字段完整率 | 47/47",
            "英文 Crops 固定页为完整性主源",
            "英文页缺少的 Qi Fruit 详情由同站固定个人页补齐",
        ],
        "coverage statement",
    )
    assert_contains(crop_text, REQUIRED_CROPS, "required crops")
    assert_contains(crop_text, REQUIRED_REVISIONS, "fixed revisions")

    crop_anchors = re.findall(r'<a id="(crop-[a-z0-9-]+)"></a>', crop_text)
    named_anchors = [item for item in crop_anchors if item not in {
        "crop-index", "crop-random-seeds", "crop-wild-seeds"
    }]
    if len(named_anchors) != 47 or len(set(named_anchors)) != 47:
        raise AssertionError(
            f"crop anchors mismatch: count={len(named_anchors)}, unique={len(set(named_anchors))}"
        )

    assert_contains(
        mechanism_text,
        [
            "47/47 完成",
            "花椰菜（Cauliflower）",
            "甜瓜（Melon）",
            "南瓜（Pumpkin）",
            "霜瓜（Powdermelon）",
            "齐瓜（Qi Fruit）",
            "温室作物**仍需浇水**",
            "姜岛天气独立于星露谷本土",
        ],
        "mechanism corrections",
    )

    combined = crop_text + "\n" + mechanism_text
    stale = [item for item in FORBIDDEN_STALE_TEXT if item in combined]
    if stale:
        raise AssertionError(f"stale crop claims remain: {stale}")

    required_cross_links = [
        (CROP_DOC, "./NPC事件数据总览.md"),
        (CROP_DOC, "../机制分析/作物种植系统.md"),
        (CROP_DOC, "./鱼类数据总览.md"),
        (MECHANISM_DOC, "../数值数据/作物数据总览.md"),
        (EVENT_DOC, "./作物数据总览.md"),
        (OVERVIEW_DOC, "./数值数据/作物数据总览.md"),
        (OVERVIEW_DOC, "./机制分析/作物种植系统.md"),
    ]
    for document, target in required_cross_links:
        if target not in document.read_text(encoding="utf-8"):
            raise AssertionError(f"missing cross-link: {document.name} -> {target}")

    local_links = 0
    anchors = 0
    broken_links: list[str] = []
    for document in AUDITED_DOCS:
        checked, checked_anchors, broken = check_local_links(document)
        local_links += checked
        anchors += checked_anchors
        broken_links.extend(broken)
    if broken_links:
        raise AssertionError(f"broken local links: {broken_links}")

    print(
        "audit: named_crops=47/47, auxiliary_systems=3/3, "
        f"crop_anchors={len(named_anchors)}/47, fixed_revisions={len(REQUIRED_REVISIONS)}/7, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, anchors={anchors}, "
        "broken_links=0, stale_claims=0"
    )


if __name__ == "__main__":
    main()
