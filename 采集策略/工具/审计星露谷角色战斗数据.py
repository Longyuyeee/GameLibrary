#!/usr/bin/env python3
"""审计《星露谷物语》角色属性、状态、战斗公式、唯一归属与本地导航。"""

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
ROLE_COMBAT = GAME / "数值数据" / "角色属性战斗数据总览.md"
SKILLS = GAME / "数值数据" / "技能属性数据总览.md"
TIME_MECHANISM = GAME / "机制分析" / "时间季节系统.md"
BATTLE_MECHANISM = GAME / "机制分析" / "战斗探索系统.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷角色战斗数据.py"

AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]
EXPECTED_ANCHORS = {
    "source-health",
    "source-energy",
    "source-combat-mechanics",
    "source-buffs",
    "source-attack",
    "source-crit-chance",
    "source-crit-power",
    "source-defense",
    "source-immunity",
    "source-luck",
    "source-magnetism",
    "source-speed",
    "source-weight",
}
FORBIDDEN_STALE_TEXT = [
    "理论最大约245HP",
    "**最大HP计算**",
    "实际暴击率 = [",
    "最终暴击率 ≈",
    "## 4. 武器系统与伤害数据",
    "## 5. 防御装备：靴子数据表",
    "### 7.2 战斗增益食物表",
    "## 8. 极限暴击流配装示例",
    "## 13. 战斗食物增益表",
    "体力耗尽昏倒(非2:00AM) | 无金币损失",
    "凌晨1:00 | ~75%恢复",
]


def load_generator_module():
    spec = importlib.util.spec_from_file_location("gamedocs_role_combat_generator", GENERATOR)
    if spec is None or spec.loader is None:
        raise AssertionError("无法加载角色战斗数据生成器")
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

    role_combat = ROLE_COMBAT.read_text(encoding="utf-8")
    skills = SKILLS.read_text(encoding="utf-8")
    time_mechanism = TIME_MECHANISM.read_text(encoding="utf-8")
    battle_mechanism = BATTLE_MECHANISM.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")

    assert_contains(
        role_combat,
        [
            "属性族 | 预计 11 / 实际 11",
            "可烹饪料理/饮料逐件表转交烹饪数据源",
            "非配方消耗品、工具、钓具、武器、戒指、鞋、衣物逐件表转交道具装备数据源",
            "固定来源 | 预计 13 / 实际 13",
            "域内源表 | 预计 11 张 / 实际 11 张；表体记录预计 54 / 实际 54",
            "规则事实块 | 预计 142 / 实际 142",
            "Buff/减益名册 | 预计 24 / 实际 24",
            "睡眠延迟惩罚 | 预计 12 个时点 / 实际 12",
            "域内源表保留固定 revision 的全部源列与合并单元格",
            "完整原文 3/3 字段，不做摘要或节选",
            "| 数量差异 | 0 |",
            "| 验收状态 | **已完成** |",
            "### 永久最大生命值（205）",
            "战斗等级 1–4、6–9（8 级 × 5）",
            "永久最大值 508",
            "最高 588",
            "精力到 −15",
            "金币损失上限 15,000g",
            "每点把被施加减益概率降低 9.1%",
            "总免疫达到 11 时完全免疫",
            "[技能属性数据总览](./技能属性数据总览.md#source-combat)",
            "[烹饪配方数据总览](./烹饪配方数据总览.md)",
            "[节日活动数据总览](./节日活动数据总览.md#source-desert-festival)",
            "[道具装备数据总览](./道具装备数据总览.md)",
            "非配方特殊消耗品；工具与钓具的逐件属性、单次行动精力消耗",
            "[怪物数据总览](./怪物数据总览.md)",
        ],
        "role/combat coverage",
    )

    actual_anchors = set(re.findall(r'<a id="(source-[a-z0-9-]+)"></a>', role_combat))
    if actual_anchors != EXPECTED_ANCHORS:
        raise AssertionError(
            f"角色战斗来源锚点漂移：actual={sorted(actual_anchors)}, "
            f"expected={sorted(EXPECTED_ANCHORS)}"
        )

    expected_revisions = {source.revision for source in generator.SOURCES}
    actual_revisions = {int(value) for value in re.findall(r"oldid=(\d+)", role_combat)}
    if actual_revisions != expected_revisions:
        raise AssertionError(
            f"角色战斗固定 revision 漂移：actual={sorted(actual_revisions)}, "
            f"expected={sorted(expected_revisions)}"
        )

    assert_contains(
        time_mechanism,
        [
            "## 2. 精力、疲惫与睡眠恢复",
            "12个时间档位不得用约数代替",
            "[精力固定源](../数值数据/角色属性战斗数据总览.md#source-energy)",
            "[生命固定源：失去意识规则](../数值数据/角色属性战斗数据总览.md#source-health)",
            "角色属性文档负责“触发后的完整数值与公式”",
            "非配方消耗品与工具的逐件数值由道具装备数据文档维护",
        ],
        "time/energy boundary",
    )
    assert_contains(
        battle_mechanism,
        [
            "永久最大值205",
            "永久最大508",
            "临时上限最高588",
            "每点按9.1%叠加",
            "## 13. 战斗状态与消耗品边界",
            "[角色状态24/24全集](../数值数据/角色属性战斗数据总览.md#source-buffs)",
            "道具与装备对象全集已由固定数据源统一维护",
            "本页不再保留装备对象副本",
            "不选取“推荐料理”代替全集",
        ],
        "battle mechanism alignment",
    )
    assert_contains(
        skills,
        [
            "通用生命/精力、角色状态和战斗公式留在[角色属性战斗数据总览]",
            "非配方特殊消耗品、工具、钓具、武器、护甲、戒指、饰品、服装、锻造与附魔留在[道具装备数据总览]",
        ],
        "skill ownership alignment",
    )

    stale_scope = role_combat + "\n" + time_mechanism + "\n" + battle_mechanism
    stale = [value for value in FORBIDDEN_STALE_TEXT if value in stale_scope]
    if stale:
        raise AssertionError(f"旧角色战斗节选或错误口径残留：{stale}")
    unresolved = [value for value in ("待补充", "待核实") if value in role_combat]
    if unresolved:
        raise AssertionError(f"生成角色战斗文档含未决标记：{unresolved}")

    role_kb = ROLE_COMBAT.stat().st_size / 1024
    assert_contains(
        overview,
        [f"[角色属性战斗数据总览](./数值数据/角色属性战斗数据总览.md) | {role_kb:.1f} KB"],
        "overview alignment",
    )
    assert_contains(
        audit,
        [
            "11 项属性族、13/13 固定 revision",
            "11 张源表、54 行数据、142 个规则事实块",
            "Buff/减益 24/24",
            "永久最大生命 205",
            "15 份数值数据文档已全部完成",
            "下一阶段进入全游戏导航补齐与剩余机制/特色文档审计",
        ],
        "audit record",
    )
    assert_contains(
        plan,
        ["道具装备数据域已完成", "下一阶段为全游戏导航补齐与剩余机制/特色文档审计"],
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
        "audit: attributes=11/11, sources=13/13, source_tables=11/11, "
        "source_rows=54/54, facts=142/142, buffs=24/24, sleep_penalties=12/12, "
        "max_health=205, max_energy=508/588, stale_claims=0, unresolved=0, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0"
    )


if __name__ == "__main__":
    main()
