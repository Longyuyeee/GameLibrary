#!/usr/bin/env python3
"""审计《鱼类数据总览》与《出货收集数据总览》的全集、字段和导航。"""

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
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷鱼类出货数据.py"
FISH = GAME / "数值数据" / "鱼类数据总览.md"
SHIPPING = GAME / "数值数据" / "出货收集数据总览.md"
CROP = GAME / "数值数据" / "作物数据总览.md"
PROCESSING = GAME / "数值数据" / "加工配方数据总览.md"
GRANDPA = GAME / "特色文档" / "爷爷评价与完美追踪.md"
MAP = GAME / "机制分析" / "地图场景系统.md"
TIME = GAME / "机制分析" / "时间季节系统.md"
ECONOMY = GAME / "机制分析" / "经济系统.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]

REVISIONS = (193885, 55286, 191813, 52128, 193038, 187068)


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
        [sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True
    )

    fish = FISH.read_text(encoding="utf-8")
    shipping = SHIPPING.read_text(encoding="utf-8")
    crop = CROP.read_text(encoding="utf-8")
    processing = PROCESSING.read_text(encoding="utf-8")
    grandpa = GRANDPA.read_text(encoding="utf-8")
    map_text = MAP.read_text(encoding="utf-8")
    time_text = TIME.read_text(encoding="utf-8")
    economy = ECONOMY.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")

    expected_shapes = {FISH: (143, 82), SHIPPING: (183, 311)}
    for path, expected in expected_shapes.items():
        actual = table_rows_and_urls(path)
        if actual != expected:
            raise AssertionError(
                f"生成文档结构漂移：{path.relative_to(ROOT)} rows/urls={actual}/{expected}"
            )

    assert_contains(
        fish,
        [
            "可捕获对象全集 | 预计 77 / 实际 77；名称唯一 77 / 77",
            "钓竿鱼 48 / 48；夜市鱼 3 / 3；传说鱼 5 / 5；传说鱼二代 5 / 5；蟹笼鱼 10 / 10；其他可捕获物 6 / 6",
            "鱼类图鉴 | 预计 72 / 实际 72",
            "可烟熏鱼 | 预计 71 / 实际 71",
            "Data/Fish 字段语义 | 蟹笼记录 7 / 7；钓竿鱼记录 14 / 14；合计 21 / 21",
            "规则事实块 | 预计 14 / 实际 14",
            "未知或待核实字段 | 0",
            "验收状态 | **已完成**",
            "英文固定页是 PC v1.6.15 数值裁定主源",
        ],
        "鱼类数据",
    )
    assert_contains(
        shipping,
        [
            "Full Shipment 槽位 | 预计 154 / 实际 154",
            "指定对象 140 / 140；颜色指定对象 4 / 4；任意同类变体 10 / 10",
            "Polyculture | 必须各出货 15 个的作物预计 28 / 实际 28",
            "Monoculture | 可任选并出货 300 个的作物预计 33 / 实际 33",
            "Full Shipment | 154 / 154 槽位各至少出货 1 个",
            "规则事实块 | 预计 5 / 实际 5",
            "未知或待核实字段 | 0",
            "验收状态 | **已完成**",
            '<a id="shipping-achievements"></a>',
            '<a id="shipping-slots"></a>',
            '<a id="shipping-facts"></a>',
        ],
        "出货收集数据",
    )

    fish_anchors = re.findall(r'<a id="fish-[^"]+"></a>', fish)
    shipping_anchors = re.findall(r'<a id="shipping-[^"]+-\d+"></a>', shipping)
    if len(fish_anchors) != 77 or len(set(fish_anchors)) != 77:
        raise AssertionError(f"鱼类对象锚点不是 77/77：{len(fish_anchors)}")
    if len(shipping_anchors) != 154 or len(set(shipping_anchors)) != 154:
        raise AssertionError(f"出货槽位锚点不是 154/154：{len(shipping_anchors)}")

    revision_text = fish + shipping
    missing_revisions = [revision for revision in REVISIONS if f"oldid={revision}" not in revision_text]
    if missing_revisions:
        raise AssertionError(f"鱼类/出货固定 revision 缺失：{missing_revisions}")

    assert_contains(
        grandpa,
        [
            "[鱼类数据总览](../数值数据/鱼类数据总览.md)",
            "[出货收集数据总览](../数值数据/出货收集数据总览.md)",
            "鱼类 77/77、图鉴 72/72 与 Full Shipment 154/154 已移交独立全集",
        ],
        "爷爷/完美归属",
    )
    assert_contains(
        map_text,
        [
            "[鱼类数据总览](../数值数据/鱼类数据总览.md)",
            "[77/77 可捕获对象与 72/72 图鉴](../数值数据/鱼类数据总览.md)",
            "不再维护“代表鱼类”",
        ],
        "地图机制归属",
    )
    assert_contains(
        time_text,
        [
            "[77/77 可捕获对象、72/72 图鉴](../数值数据/鱼类数据总览.md)",
            "[154/154 出货收集槽位](../数值数据/出货收集数据总览.md)",
            "[爷爷评分固定源](../特色文档/爷爷评价与完美追踪.md#source-grandpa)",
        ],
        "时间机制归属",
    )
    assert_contains(
        economy,
        [
            "../数值数据/出货收集数据总览.md#shipping-slots",
            "../数值数据/出货收集数据总览.md#shipping-achievements",
            "../数值数据/出货收集数据总览.md#shipping-facts",
        ],
        "经济机制归属",
    )
    assert_contains(
        crop,
        ["[下一篇：鱼类数据总览](./鱼类数据总览.md)"],
        "作物连续导航",
    )
    assert_contains(
        processing,
        ["[上一篇：出货收集数据总览](./出货收集数据总览.md)"],
        "加工连续导航",
    )

    forbidden = {
        "fish image alt leak": "Pufferfish.png",
        "old grandpa gap": "鱼类与出货对象 | 当前尚无独立全集文档",
        "old audit gap": "鱼类与出货对象全集缺少独立数据文档",
        "map subset": "| 水域 | 位置 | 代表鱼类 |",
        "grandpa duplicate": "| **评估时间** | 第3年春季第1天 |",
        "old fish shorthand": "钓到所有鱼(传奇鱼+普通鱼)",
        "old shipping score claim": "出货记录影响爷爷评分",
    }
    combined = fish + shipping + grandpa + map_text + time_text + economy + plan + audit
    stale = [label for label, value in forbidden.items() if value in combined]
    if stale:
        raise AssertionError(f"鱼类/出货旧口径残留：{stale}")

    assert_contains(
        overview,
        [
            "内容文档数: 33 份",
            "总大小: 约 2,504.1 KB",
            "数值数据 | 17 篇 | ~2,219.7 KB",
            "鱼类数据总览](./数值数据/鱼类数据总览.md) | 74.0 KB",
            "出货收集数据总览](./数值数据/出货收集数据总览.md) | 42.2 KB",
        ],
        "游戏概览",
    )
    assert_contains(
        audit,
        [
            "17 份数值数据文档已全部完成",
            "鱼类 77/77、图鉴 72/72、可烟熏鱼 71/71",
            "Full Shipment 154/154、Polyculture 28/28、Monoculture 33/33",
            "34/34 份文档具备顶部面包屑",
            "33/33 份子文档具备连续导航",
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
        ],
        "执行计划",
    )

    unresolved = [
        line
        for line in (fish + "\n" + shipping).splitlines()
        if "待补充" in line or ("待核实" in line and "未知或待核实字段" not in line)
    ]
    if unresolved:
        raise AssertionError(f"生成数据文档含未决标记：{unresolved}")

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
        "audit: catchables=77/77, fish_collection=72/72, smokable=71/71, "
        "fish_sections=48+3+5+5+10+6, fish_schema=21/21, fish_facts=14/14, "
        "shipping=154/154, shipping_scopes=140+4+10, polyculture=28/28, "
        "monoculture=33/33, revisions=6/6, stale_claims=0, unresolved=0, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0"
    )


if __name__ == "__main__":
    main()
