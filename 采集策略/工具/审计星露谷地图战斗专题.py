#!/usr/bin/env python3
"""审计《地图场景系统》与《战斗探索系统》的职责、固定来源和导航。"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "星露谷物语"
MAP = GAME / "机制分析" / "地图场景系统.md"
COMBAT = GAME / "机制分析" / "战斗探索系统.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]

MAP_REVISIONS = {
    "Farm Maps": 191362,
    "Pelican Town": 192583,
    "Cindersap Forest": 192759,
    "The Mountain": 193446,
    "Bus Stop": 192757,
    "The Desert": 192758,
    "Ginger Island": 193461,
    "Minecart": 176698,
    "Boat": 191215,
    "Animals / Horse": 193812,
    "Warp Totem / Obelisks": 192592,
    "Return Scepter": 193944,
}

COMBAT_REVISIONS = {
    "Combat": 192831,
    "The Mines": 193833,
    "Skull Cavern": 193731,
    "Volcano Dungeon": 192615,
}


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
    map_text = MAP.read_text(encoding="utf-8")
    combat_text = COMBAT.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")

    assert_contains(
        map_text,
        [
            "PC v1.6.15",
            "机制规则族 | 预计 6 / 实际 6",
            "固定来源 | 预计 12 / 实际 12",
            "数值对象副本 | 0",
            "未知或待核实事实 | 0",
            "验收状态 | **已完成**",
            '<a id="map-topology"></a>',
            '<a id="map-unlocks"></a>',
            '<a id="map-transport"></a>',
            '<a id="map-resources"></a>',
            '<a id="map-comparisons"></a>',
            '<a id="map-sources"></a>',
            "[战斗探索系统](./战斗探索系统.md#combat-dungeons)",
            "[鱼类数据总览](../数值数据/鱼类数据总览.md)",
            "[道具装备数据总览](../数值数据/道具装备数据总览.md)",
            "[社区中心与Joja路线](../特色文档/社区中心与Joja路线.md)",
            "[齐先生的挑战与姜岛](../特色文档/齐先生的挑战与姜岛.md)",
            "https://www.storyofseasons.com/fomt/",
            "https://runefactory.com/rf4/",
        ],
        "地图场景系统",
    )
    assert_contains(
        combat_text,
        [
            "PC v1.6.15",
            "机制规则族 | 预计 5 / 实际 5",
            "固定来源 | 预计 4 / 实际 4",
            "数值对象副本 | 0",
            "未知或待核实事实 | 0",
            "验收状态 | **已完成**",
            '<a id="combat-loop"></a>',
            '<a id="combat-dungeons"></a>',
            '<a id="combat-challenges"></a>',
            '<a id="combat-data"></a>',
            '<a id="combat-comparisons"></a>',
            '<a id="combat-sources"></a>',
            "[地图场景系统](./地图场景系统.md#map-topology)",
            "[怪物数据总览](../数值数据/怪物数据总览.md)",
            "[道具装备数据总览](../数值数据/道具装备数据总览.md)",
            "[技能属性数据总览](../数值数据/技能属性数据总览.md)",
            "[角色属性战斗数据总览](../数值数据/角色属性战斗数据总览.md)",
            "[齐先生的挑战与姜岛](../特色文档/齐先生的挑战与姜岛.md)",
            "https://www.storyofseasons.com/fomt/",
            "https://runefactory.com/rf4/",
        ],
        "战斗探索系统",
    )

    map_revision_ids = {int(value) for value in re.findall(r"oldid=(\d+)", map_text)}
    combat_revision_ids = {int(value) for value in re.findall(r"oldid=(\d+)", combat_text)}
    if map_revision_ids != set(MAP_REVISIONS.values()):
        raise AssertionError(
            f"地图固定 revision 漂移：{sorted(map_revision_ids)}/{sorted(MAP_REVISIONS.values())}"
        )
    if combat_revision_ids != set(COMBAT_REVISIONS.values()):
        raise AssertionError(
            "战斗固定 revision 漂移："
            f"{sorted(combat_revision_ids)}/{sorted(COMBAT_REVISIONS.values())}"
        )

    forbidden_map = [
        "完整地图区域总览",
        "矿洞系统详解",
        "各区域资源分布",
        "星露谷物语提供17种移动方式",
        "推荐传送配置方案",
        "捐赠博物馆40件物品",
        "齐钻商店(500齐钻)",
    ]
    forbidden_combat = [
        "战斗在星露谷物语中约占",
        "推荐等级",
        "铱矿产出公式",
        "宝藏房间公式",
        "齐先生相关战斗任务",
        "装备值在相应数值数据文档完成全集审计前",
    ]
    stale = [
        f"map:{value}" for value in forbidden_map if value in map_text
    ] + [f"combat:{value}" for value in forbidden_combat if value in combat_text]
    if stale:
        raise AssertionError(f"地图/战斗旧口径残留：{stale}")

    combined = map_text + "\n" + combat_text
    unresolved = [
        line
        for line in combined.splitlines()
        if "待补充" in line or ("待核实" in line and "未知或待核实事实" not in line)
    ]
    if unresolved:
        raise AssertionError(f"地图/战斗专题含未决标记：{unresolved}")

    assert_contains(
        overview,
        [
            "地图场景系统](./机制分析/地图场景系统.md)",
            "战斗探索系统](./机制分析/战斗探索系统.md)",
        ],
        "游戏概览",
    )
    assert_contains(
        audit,
        [
            "地图/战斗机制域",
            "非数值文档 16 份中，11 份已完成、1 份部分完成、4 份采集中",
            "下一阶段进入时间/经济重叠域",
        ],
        "审计记录",
    )
    assert_contains(
        plan,
        [
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

    map_rows, map_urls = table_rows_and_urls(MAP)
    combat_rows, combat_urls = table_rows_and_urls(COMBAT)
    if (map_rows, map_urls) != (72, 34):
        raise AssertionError(f"地图文档证据漂移：{(map_rows, map_urls)}/(72, 34)")
    if (combat_rows, combat_urls) != (59, 11):
        raise AssertionError(f"战斗文档证据漂移：{(combat_rows, combat_urls)}/(59, 11)")
    print(
        "audit: map_rules=6/6, map_revisions=12/12, "
        "combat_rules=5/5, combat_revisions=4/4, data_duplicates=0, "
        "stale_claims=0, unresolved=0, "
        f"map_rows={map_rows}, map_urls={map_urls}, "
        f"combat_rows={combat_rows}, combat_urls={combat_urls}, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0"
    )


if __name__ == "__main__":
    main()
