#!/usr/bin/env python3
"""审计《星露谷物语》动物、怪物全集、唯一归属与本地导航。"""

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
ANIMAL = GAME / "数值数据" / "动物数据总览.md"
MONSTER = GAME / "数值数据" / "怪物数据总览.md"
LEGACY_MIXED = GAME / "数值数据" / "动物怪物数据总览.md"
ANIMAL_MECHANISM = GAME / "机制分析" / "畜牧养殖系统.md"
BATTLE_MECHANISM = GAME / "机制分析" / "战斗探索系统.md"
CRAFTING = GAME / "数值数据" / "制作配方数据总览.md"
SKILLS = GAME / "数值数据" / "技能属性数据总览.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷动物怪物数据.py"

AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]

FORBIDDEN_STALE_TEXT = [
    "品质分数 = (好感度 + 心情修正值) / 2000",
    "满好感+满心情时品质分布",
    "美国毒蜥",
    "Blue Serpent",
    "Radioactive Bat",
    "完整12个猎杀目标",
]


def load_generator_module():
    spec = importlib.util.spec_from_file_location("gamedocs_animal_monster_generator", GENERATOR)
    if spec is None or spec.loader is None:
        raise AssertionError("无法加载动物/怪物生成器")
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


def exact_anchor_count(text: str, prefix: str, expected: int) -> None:
    anchors = re.findall(rf'<a id="({re.escape(prefix)}[a-z0-9-]+)"></a>', text)
    if len(anchors) != expected or len(set(anchors)) != expected:
        raise AssertionError(
            f"{prefix} anchors mismatch: count={len(anchors)}, unique={len(set(anchors))}, "
            f"expected={expected}"
        )


def fixed_revisions(text: str) -> set[int]:
    return {int(value) for value in re.findall(r"oldid=(\d+)", text)}


def main() -> None:
    if LEGACY_MIXED.exists():
        raise AssertionError(f"旧混合文件仍存在：{LEGACY_MIXED.relative_to(ROOT)}")

    subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True)
    generator = load_generator_module()

    animal = ANIMAL.read_text(encoding="utf-8")
    monster = MONSTER.read_text(encoding="utf-8")
    animal_mechanism = ANIMAL_MECHANISM.read_text(encoding="utf-8")
    battle_mechanism = BATTLE_MECHANISM.read_text(encoding="utf-8")
    crafting = CRAFTING.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")

    assert_contains(
        animal,
        [
            "预计 14 个展示变体 / 实际 14",
            "对应 11/11 个动物类型详情页",
            "预计 15 / 实际 15",
            "预计 3 个池、48 条概率行 / 实际 3、48",
            "详情数据表 192 张、表体记录 409 行、非历史事实块 225 个全部保留",
            "| 数量差异 | 0 |",
            "| 验收状态 | **已完成** |",
        ],
        "animal coverage",
    )
    assert_contains(
        monster,
        [
            "普通预计 45 / 实际 45",
            "危险模式预计 29 / 实际 29",
            "合计 74 个槽位、72 个唯一显示名",
            "预计 58 / 实际 58",
            "预计 49 / 实际 49；每条 15/15 字段",
            "预计 12 / 实际 12",
            "Iridium Golem 与 Truffle Crab",
            "58/58 个详情页均检出掉落字段",
            "| 数量差异 | 0 |",
            "| 验收状态 | **已完成** |",
        ],
        "monster coverage",
    )
    exact_anchor_count(animal, "page-", 26)
    exact_anchor_count(monster, "page-", 58)

    expected_animal_revisions = {
        generator.ANIMALS_REVISION,
        generator.ANIMAL_SCHEMA_REVISION,
        *(spec.revision for spec in generator.ANIMAL_PAGES),
    }
    expected_monster_revisions = {
        generator.MONSTERS_REVISION,
        generator.MONSTER_RAW_REVISION,
        generator.ERADICATION_REVISION,
        *(spec.revision for spec in generator.MONSTER_PAGES),
    }
    missing_animal_revisions = expected_animal_revisions - fixed_revisions(animal)
    missing_monster_revisions = expected_monster_revisions - fixed_revisions(monster)
    if missing_animal_revisions or missing_monster_revisions:
        raise AssertionError(
            f"固定 revision 缺失：animal={sorted(missing_animal_revisions)}, "
            f"monster={sorted(missing_monster_revisions)}"
        )

    assert_contains(
        animal_mechanism,
        [
            "[动物与动物产品数据总览](../数值数据/动物数据总览.md)",
            "大型产品分数 = (好感度 + 心情修正值) / 1200",
            "品质分数 = (好感度 / 1000) - (1 - 心情 / 225)",
            "出售价格 = 数据中的基础出售值 × (好感度 / 1000 + 0.3)",
        ],
        "animal mechanism alignment",
    )
    assert_contains(
        battle_mechanism,
        [
            "[怪物数据总览](../数值数据/怪物数据总览.md)",
            "普通区域名册 45/45、危险名册 29/29、详情页 58/58、原始记录 49/49",
            "危险模式怪物的生命、伤害、防御、经验和掉落则回到怪物数据全集",
            "数值对象副本 | 0",
        ],
        "battle mechanism alignment",
    )
    assert_contains(
        crafting,
        ["[下一篇：动物数据总览](./动物数据总览.md)"],
        "crafting navigation",
    )
    assert_contains(
        overview,
        [
            "[动物数据总览](./数值数据/动物数据总览.md) | 148.5 KB",
            "[怪物数据总览](./数值数据/怪物数据总览.md) | 158.3 KB",
            "总大小: 约 2,530.0 KB",
        ],
        "overview alignment",
    )
    assert_contains(
        audit,
        [
            "动物 14 个变体、26 个详情页",
            "怪物 45+29 个名册槽位、58 个详情页、49 条原始记录、12 个猎杀目标",
            "17 份数值数据文档已全部完成",
            "下一阶段进入符文工房3",
        ],
        "audit record",
    )
    assert_contains(
        plan,
        ["17 份数值文档和 16 份非数值文档全部完成", "下一阶段处理符文工房3"],
        "execution plan",
    )

    stale = [
        value
        for value in FORBIDDEN_STALE_TEXT
        if value in animal_mechanism or value in battle_mechanism
    ]
    if stale:
        raise AssertionError(f"旧动物/怪物口径残留：{stale}")
    unresolved = [
        value for value in ("待补充", "待核实") if value in animal or value in monster
    ]
    if unresolved:
        raise AssertionError(f"生成数据文档含未决标记：{unresolved}")

    game_markdown = "\n".join(
        path.read_text(encoding="utf-8") for path in GAME.rglob("*.md")
    )
    if "动物怪物数据总览.md" in game_markdown:
        raise AssertionError("星露谷物语文档仍链接旧混合文件")

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
        "audit: animal_variants=14/14, animal_pages=26/26, products=15/15, "
        "pet_gifts=3_pools/48_rows, monster_roster=45+29, monster_pages=58/58, "
        "raw_monsters=49/49x15, eradication_goals=12/12, "
        f"fixed_revisions={len(expected_animal_revisions) + len(expected_monster_revisions)}/"
        f"{len(expected_animal_revisions) + len(expected_monster_revisions)}, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0, stale_claims=0, unresolved=0"
    )


if __name__ == "__main__":
    main()
