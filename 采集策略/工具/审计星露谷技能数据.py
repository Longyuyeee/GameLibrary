#!/usr/bin/env python3
"""审计《星露谷物语》技能、经验、职业、精通、唯一归属与本地导航。"""

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
SKILLS = GAME / "数值数据" / "技能属性数据总览.md"
ROLE_COMBAT = GAME / "数值数据" / "角色属性战斗数据总览.md"
BATTLE_MECHANISM = GAME / "机制分析" / "战斗探索系统.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷技能数据.py"

AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]
FORBIDDEN_DUPLICATE_HEADINGS = [
    "### 3.1 战斗技能与属性成长",
    "### 3.2 战斗职业分支",
    "### 11.2 战斗经验值表",
    "### 11.3 战斗职业树",
    "### 11.6 战斗精通(1.6新增)",
]


def load_generator_module():
    spec = importlib.util.spec_from_file_location("gamedocs_skill_generator", GENERATOR)
    if spec is None or spec.loader is None:
        raise AssertionError("无法加载技能数据生成器")
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

    skills = SKILLS.read_text(encoding="utf-8")
    role_combat = ROLE_COMBAT.read_text(encoding="utf-8")
    battle_mechanism = BATTLE_MECHANISM.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")

    assert_contains(
        skills,
        [
            "技能名册 | 预计 5 / 实际 5",
            "等级经验 | 预计 10 / 实际 10；Lv10 累计 15,000 XP",
            "逐级解锁 | 预计 5×10=50 / 实际 50",
            "职业 | 预计 5×6=30 / 实际 30",
            "精通 | 点数等级预计 5 / 实际 5；奖励行预计 15 / 实际 15；累计 100,000 点",
            "经验来源 | 结构化来源/基准行预计 147 / 实际 147",
            "技能相关数据表 35 张、表体记录 397 行、非历史事实块 156 个全部保留",
            "| 数量差异 | 0 |",
            "| 验收状态 | **已完成** |",
        ],
        "skill coverage",
    )

    anchors = re.findall(r'<a id="(source-[a-z0-9-]+)"></a>', skills)
    if len(anchors) != 7 or len(set(anchors)) != 7:
        raise AssertionError(
            f"技能来源锚点不闭合：count={len(anchors)}, unique={len(set(anchors))}, expected=7"
        )

    expected_revisions = {source.revision for source in generator.SOURCES}
    actual_revisions = {int(value) for value in re.findall(r"oldid=(\d+)", skills)}
    if actual_revisions != expected_revisions:
        raise AssertionError(
            f"技能固定 revision 漂移：actual={sorted(actual_revisions)}, "
            f"expected={sorted(expected_revisions)}"
        )

    assert_contains(
        role_combat,
        [
            "## 唯一归属与跨文档边界",
            "[技能属性数据总览](./技能属性数据总览.md#source-combat)",
            "技能经验、升级解锁、职业与精通",
            "道具与装备全集由固定数据源维护",
        ],
        "role/combat boundary",
    )
    assert_contains(
        battle_mechanism,
        [
            "[技能属性数据总览](../数值数据/技能属性数据总览.md)",
            "技能 5/5、逐级解锁 50/50、职业 30/30、精通奖励 15/15",
            "机制 → 对象 → 字段",
            "数值对象副本 | 0",
        ],
        "battle mechanism alignment",
    )

    duplicate_scope = role_combat + "\n" + battle_mechanism
    stale = [value for value in FORBIDDEN_DUPLICATE_HEADINGS if value in duplicate_scope]
    if stale:
        raise AssertionError(f"旧技能副本残留：{stale}")
    unresolved = [value for value in ("待补充", "待核实") if value in skills]
    if unresolved:
        raise AssertionError(f"生成技能文档含未决标记：{unresolved}")

    skill_kb = SKILLS.stat().st_size / 1024
    assert_contains(
        overview,
        [f"[技能属性数据总览](./数值数据/技能属性数据总览.md) | {skill_kb:.1f} KB"],
        "overview alignment",
    )
    assert_contains(
        audit,
        [
            "五项技能 5/5、统一等级经验 10/10、逐级解锁 50/50、职业 30/30",
            "精通等级 5/5 与奖励 15/15、结构化经验 147/147",
            "17 份数值数据文档已全部完成",
            "下一阶段进入齐先生/姜岛专题",
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
        "audit: skills=5/5, levels=10/10, unlocks=50/50, professions=30/30, "
        "mastery=5_levels/15_rewards, structured_xp=147/147, revisions=7/7, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0, duplicate_skill_tables=0, unresolved=0"
    )


if __name__ == "__main__":
    main()
