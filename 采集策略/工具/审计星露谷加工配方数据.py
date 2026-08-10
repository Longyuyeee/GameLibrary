#!/usr/bin/env python3
"""审计《星露谷物语》加工、烹饪、制作全集及本地导航。"""

from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "星露谷物语"
PROCESSING = GAME / "数值数据" / "加工配方数据总览.md"
COOKING = GAME / "数值数据" / "烹饪配方数据总览.md"
CRAFTING = GAME / "数值数据" / "制作配方数据总览.md"
MECHANISM = GAME / "机制分析" / "加工制造系统.md"
CROP = GAME / "数值数据" / "作物数据总览.md"
ANIMAL = GAME / "数值数据" / "动物数据总览.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷加工配方数据.py"

AUDITED_DOCS = [
    PROCESSING,
    COOKING,
    CRAFTING,
    MECHANISM,
    CROP,
    ANIMAL,
    OVERVIEW,
    PLAN,
    AUDIT,
]

MASTER_REVISIONS = [192044, 191352, 193813, 55288, 189276, 54998, 193377]
MACHINE_REVISIONS = [
    191201,
    179542,
    183811,
    193436,
    192587,
    193087,
    190254,
    190554,
    190486,
    190576,
    191568,
    184986,
    181347,
    191954,
    185834,
    191357,
    193826,
    190283,
    190431,
    192243,
    191559,
    190575,
    190496,
    191358,
    190521,
    190492,
    190616,
    193620,
    192744,
    192692,
]

FORBIDDEN_STALE_TEXT = [
    "空瓶×1",
    "甜宝石莓(Sweet Gem Berry) | 3,000 | 9,000",
    "Joja可乐(Joja Cola) | 铁锭×1",
    "常用作物加工对比",
    "高价值鱼加工收益",
    "建筑材料总表(罗宾建造)",
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
            broken.append(f"{path.relative_to(ROOT)} -> {target}")
            continue
        if fragment and resolved.suffix.lower() == ".md":
            checked_anchors += 1
            if unquote(fragment).lower() not in document_anchors(resolved):
                broken.append(
                    f"{path.relative_to(ROOT)} -> missing anchor {target}"
                )
    return checked, checked_anchors, broken


def assert_contains(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    if missing:
        raise AssertionError(f"{label} missing: {missing}")


def exact_anchor_count(text: str, prefix: str, expected: int) -> None:
    anchors = re.findall(rf'<a id="({re.escape(prefix)}[a-z0-9-]+)"></a>', text)
    if len(anchors) != expected or len(set(anchors)) != expected:
        raise AssertionError(
            f"{prefix} anchors mismatch: count={len(anchors)}, unique={len(set(anchors))}, "
            f"expected={expected}"
        )


def main() -> None:
    subprocess.run(
        [sys.executable, str(GENERATOR), "--check"],
        cwd=ROOT,
        check=True,
    )

    processing = PROCESSING.read_text(encoding="utf-8")
    cooking = COOKING.read_text(encoding="utf-8")
    crafting = CRAFTING.read_text(encoding="utf-8")
    mechanism = MECHANISM.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")

    assert_contains(
        processing,
        [
            "| 预计条目数 | 30 台：工匠设备 10、精炼设备 20 |",
            "| 实际收录数 | 30 台：工匠设备 10、精炼设备 20 |",
            "| 数量差异 | 0 |",
            "固定页数据表 59 张、表体记录 478 行、非历史事实块 62 个全部保留",
            "| 烹饪配方 | 81/81 |",
            "| 制作配方 | 150/150 |",
        ],
        "processing coverage",
    )
    assert_contains(
        cooking,
        [
            "| 预计条目数 | 81（PC 1.6.15 原始数据键） |",
            "| 实际收录数 | 81（中英文展示行与原始键一一映射） |",
            "| 来源对账 | 英文 81/81；中文 81/81；原始数据 81/81 |",
            "**苔藓汤**",
        ],
        "cooking coverage",
    )
    assert_contains(
        crafting,
        [
            "| 预计条目数 | 150（PC 1.6.15 原始数据键） |",
            "| 实际收录数 | 150（中英文展示行与原始键一一映射） |",
            "| 来源对账 | 英文 150/150；中文 150/150；原始数据 150/150 |",
            "| 杂项 / Misc | 17 |",
            "Blue Grass Starter",
        ],
        "crafting coverage",
    )
    exact_anchor_count(processing, "machine-", 30)
    exact_anchor_count(cooking, "recipe-", 81)
    exact_anchor_count(crafting, "recipe-", 150)

    revision_text = processing + cooking + crafting
    missing_revisions = [
        revision
        for revision in MASTER_REVISIONS + MACHINE_REVISIONS
        if f"oldid={revision}" not in revision_text
    ]
    if missing_revisions:
        raise AssertionError(f"fixed revisions missing: {missing_revisions}")

    assert_contains(
        mechanism,
        [
            "[加工机器 30/30](../数值数据/加工配方数据总览.md)",
            "[烹饪配方 81/81](../数值数据/烹饪配方数据总览.md)",
            "[制作配方 150/150](../数值数据/制作配方数据总览.md)",
            "与《牧场物语》系列对比",
            "与《波西亚时光》对比",
        ],
        "mechanism alignment",
    )
    assert_contains(
        overview,
        [
            "./数值数据/加工配方数据总览.md",
            "./数值数据/烹饪配方数据总览.md",
            "./数值数据/制作配方数据总览.md",
        ],
        "overview links",
    )
    assert_contains(
        audit,
        [
            "加工机器 30/30",
            "烹饪配方 81/81",
            "制作配方 150/150",
        ],
        "audit record",
    )

    stale = [
        value
        for value in FORBIDDEN_STALE_TEXT
        if value in processing or value in mechanism
    ]
    if stale:
        raise AssertionError(f"stale processing claims remain: {stale}")
    unresolved = [
        value
        for value in ("待补充", "待核实")
        if any(value in text for text in (processing, cooking, crafting))
    ]
    if unresolved:
        raise AssertionError(f"generated recipe docs contain unresolved markers: {unresolved}")

    local_links = 0
    anchor_links = 0
    broken: list[str] = []
    for document in AUDITED_DOCS:
        checked, checked_anchors, errors = check_local_links(document)
        local_links += checked
        anchor_links += checked_anchors
        broken.extend(errors)
    if broken:
        raise AssertionError(f"broken local links: {broken}")

    print(
        "audit: machines=30/30 (tables=59, rows=478, facts=62), "
        "cooking=81/81, crafting=150/150, recipe_anchors=231/231, "
        f"fixed_revisions={len(MASTER_REVISIONS) + len(MACHINE_REVISIONS)}/"
        f"{len(MASTER_REVISIONS) + len(MACHINE_REVISIONS)}, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0, stale_claims=0, unresolved=0"
    )


if __name__ == "__main__":
    main()
