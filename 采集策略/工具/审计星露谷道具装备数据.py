#!/usr/bin/env python3
"""审计《星露谷物语》道具装备全集、唯一归属、机制去重与本地导航。"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "星露谷物语"
EQUIPMENT = GAME / "数值数据" / "道具装备数据总览.md"
ROLE_COMBAT = GAME / "数值数据" / "角色属性战斗数据总览.md"
SKILLS = GAME / "数值数据" / "技能属性数据总览.md"
BATTLE = GAME / "机制分析" / "战斗探索系统.md"
UPGRADE = GAME / "机制分析" / "道具升级系统.md"
ECONOMY = GAME / "机制分析" / "经济系统.md"
MAP = GAME / "机制分析" / "地图场景系统.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷道具装备数据.py"

AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]
EXPECTED_ANCHORS = {
    "source-tools",
    "source-bait",
    "source-tackle",
    "source-weapons",
    "source-rings",
    "source-footwear",
    "source-trinkets",
    "source-hats",
    "source-tailoring",
    "source-dyeing",
    "source-forge",
    "source-inventory",
    "source-special-items-powers",
    "source-books",
    "source-harvey-s-clinic",
    "source-magic-rock-candy",
    "source-stardrop-tea",
    "source-stardrop",
}
FORBIDDEN_STALE_TEXT = [
    "### 3.2 常见渔具(Tackle)表",
    "### 4.2 顶级剑类武器对比",
    "### 4.3 顶级锤类武器对比",
    "### 4.4 顶级匕首类武器对比",
    "### 4.5 综合最强武器排行",
    "最佳组合推荐",
    "最强推荐",
    "社区推荐最佳附魔",
    "### 5.3 剑类武器排名",
    "### 5.4 锤类武器排名",
    "### 5.5 匕首类武器排名",
    "### 8.2 全部戒指效果",
    "### 8.3 最佳戒指组合推荐",
    "### 9.2 饰品列表",
    "### 10.1 全部靴子数据",
    "### 3.2 剑类武器数据",
    "### 3.3 锤类武器数据",
    "### 3.4 匕首类武器数据",
    "### 5.2 全戒指列表",
    "### 6.2 饰品列表",
    "### 7.1 靴子属性和列表",
    "### 9.2 常用战斗/采矿食物",
    "**约187,000 G**",
    "待审旧稿",
    "将在下一数据域统一重建",
]


def load_generator_module():
    spec = importlib.util.spec_from_file_location("gamedocs_equipment_generator", GENERATOR)
    if spec is None or spec.loader is None:
        raise AssertionError("无法加载道具装备数据生成器")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


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
                broken.append(f"{path.relative_to(ROOT)} -> missing anchor {target}")
    return checked, checked_anchors, broken


def assert_contains(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    if missing:
        raise AssertionError(f"{label} missing: {missing}")


def main() -> None:
    subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True)
    generator = load_generator_module()

    equipment = EQUIPMENT.read_text(encoding="utf-8")
    role_combat = ROLE_COMBAT.read_text(encoding="utf-8")
    skills = SKILLS.read_text(encoding="utf-8")
    battle = BATTLE.read_text(encoding="utf-8")
    upgrade = UPGRADE.read_text(encoding="utf-8")
    economy = ECONOMY.read_text(encoding="utf-8")
    map_text = MAP.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")

    assert_contains(
        equipment,
        [
            "固定来源 | 预计 18 / 实际 18",
            "域内源表 | 预计 43 / 实际 43；表体记录预计 1315 / 实际 1315",
            "规则事实块 | 预计 205 / 实际 205",
            "History、Bugs、Glitches、Trivia、Gallery、References、纯导航及 Mod 数据不属于",
            "工具对象与升级层级 | 45 | 45",
            "鱼饵 | 7 | 7",
            "渔具 | 10 | 10",
            "可用武器 | 62 | 62",
            "不可获取武器 | 2 | 2",
            "弹药关系 | 9 | 9",
            "戒指 | 30 | 30",
            "鞋靴 | 18 | 18",
            "饰品 | 8 | 8",
            "帽子 | 122 | 122",
            "衬衫 | 294 | 294",
            "裤装 | 14 | 14",
            "染色强度关系 | 545 | 545",
            "锻造/附魔/无限武器关系 | 34 | 34",
            "特殊物品能力 | 12 | 12",
            "书籍 | 26 | 26",
            "医疗补给 | 2 | 2",
            "非配方特殊消耗品 | 3 | 3",
            "—（固定源空白）",
            "| 数量差异 | 0 |",
            "| 验收状态 | **已完成** |",
        ],
        "equipment coverage",
    )

    actual_anchors = set(re.findall(r'<a id="(source-[a-z0-9-]+)"></a>', equipment))
    if actual_anchors != EXPECTED_ANCHORS:
        raise AssertionError(
            f"道具装备来源锚点漂移：actual={sorted(actual_anchors)}, "
            f"expected={sorted(EXPECTED_ANCHORS)}"
        )
    expected_revisions = {source.revision for source in generator.SOURCES}
    actual_revisions = {int(value) for value in re.findall(r"oldid=(\d+)", equipment)}
    if actual_revisions != expected_revisions:
        raise AssertionError(
            f"道具装备固定 revision 漂移：actual={sorted(actual_revisions)}, "
            f"expected={sorted(expected_revisions)}"
        )

    assert_contains(
        upgrade,
        [
            "本页只解释升级、装备和使用流程",
            "45/45 条工具对象与升级层级",
            "可用武器 62/62",
            "30/30 枚戒指",
            "8/8 件饰品",
            "鞋靴 18/18",
            "帽子 122/122",
            "衬衫 294/294、裤装 14/14",
            "545 条物品染色强度关系",
            "[背包与物品栏固定源](../数值数据/道具装备数据总览.md#source-inventory)",
        ],
        "upgrade mechanism alignment",
    )
    assert_contains(
        battle,
        [
            "[道具装备数据总览](../数值数据/道具装备数据总览.md)",
            "可用武器 62/62、弹药 9/9、戒指 30/30、鞋靴 18/18、饰品 8/8",
            "[锻造固定源](../数值数据/道具装备数据总览.md#source-forge)",
            "数值对象副本 | 0",
            "不能再抄一张武器排行",
        ],
        "battle/equipment alignment",
    )
    assert_contains(
        economy,
        ["45/45 条工具对象与升级层级", "不使用“全部工具约值”代替逐项数据"],
        "economy/tool alignment",
    )
    assert_contains(
        map_text,
        [
            "[道具装备数据总览](../数值数据/道具装备数据总览.md)",
            "传送物品、工具、装备、锻造与配方",
            "数值对象副本 | 0",
        ],
        "map/forge alignment",
    )
    assert_contains(
        role_combat,
        ["道具与装备全集由固定数据源维护", "非配方特殊消耗品"],
        "role/equipment ownership",
    )
    assert_contains(
        skills,
        ["非配方特殊消耗品、工具、钓具、武器、护甲、戒指、饰品、服装、锻造与附魔留在[道具装备数据总览]"],
        "skill/equipment ownership",
    )

    stale_scope = "\n".join((equipment, battle, upgrade, economy, map_text, role_combat))
    stale = [value for value in FORBIDDEN_STALE_TEXT if value in stale_scope]
    if stale:
        raise AssertionError(f"旧道具装备节选、推荐或待审口径残留：{stale}")
    unresolved = [value for value in ("待补充", "待核实") if value in equipment]
    if unresolved:
        raise AssertionError(f"生成道具装备文档含未决标记：{unresolved}")
    if "data-sort-value=" in equipment:
        raise AssertionError("生成道具装备文档含未清理的源站排序标记")

    equipment_kb = EQUIPMENT.stat().st_size / 1024
    assert_contains(
        overview,
        [f"[道具装备数据总览](./数值数据/道具装备数据总览.md) | {equipment_kb:.1f} KB"],
        "overview alignment",
    )
    assert_contains(
        audit,
        [
            "18/18 固定 revision",
            "43 张源表、1315 行数据、205 个规则事实块",
            "工具 45/45、鱼饵 7/7、渔具 10/10、可用武器 62/62",
            "戒指 30/30、鞋靴 18/18、饰品 8/8",
            "帽子 122/122、衬衫 294/294、裤装 14/14",
            "17 份数值数据文档已全部完成",
            "下一阶段进入加工制造剩余比较来源",
        ],
        "audit record",
    )
    assert_contains(
        plan,
        ["17 份数值数据文档与全游戏导航链已完成", "下一阶段为剩余非数值文档逐域重建"],
        "execution plan",
    )

    local_links = 0
    anchor_links = 0
    broken: list[str] = []
    for document in AUDITED_DOCS:
        checked, checked_anchors, errors = check_local_links(document)
        local_links += checked
        anchor_links += checked_anchors
        broken.extend(errors)
    if broken:
        raise AssertionError(f"本地链接或锚点失效：{broken}")

    print(
        "audit: sources=18/18, source_tables=43/43, source_rows=1315/1315, "
        "facts=205/205, tools=45/45, bait=7/7, tackle=10/10, weapons=62+2, "
        "ammo=9/9, rings=30/30, footwear=18/18, trinkets=8/8, hats=122/122, "
        "shirts=294/294, pants=14/14, dye_rows=545/545, forge_rows=34/34, "
        "stale_claims=0, unresolved=0, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0"
    )


if __name__ == "__main__":
    main()
