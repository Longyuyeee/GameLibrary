#!/usr/bin/env python3
"""审计《星露谷物语》节日、比赛、奖励、库存、机制边界与本地导航。"""

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
FESTIVAL = GAME / "数值数据" / "节日活动数据总览.md"
TIME_MECHANISM = GAME / "机制分析" / "时间季节系统.md"
OVERVIEW = GAME / "游戏概览.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "星露谷物语.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成星露谷节日数据.py"

AUDITED_DOCS = sorted(GAME.rglob("*.md")) + [PLAN, AUDIT]
EXPECTED_ANCHORS = {
    "source-festivals",
    "source-egg-festival",
    "source-desert-festival",
    "source-flower-dance",
    "source-luau",
    "source-trout-derby",
    "source-dance-of-the-moonlight-jellies",
    "source-stardew-valley-fair",
    "source-spirit-s-eve",
    "source-festival-of-ice",
    "source-squidfest",
    "source-night-market",
    "source-feast-of-the-winter-star",
    "source-smoked-fish-supplement",
}
FORBIDDEN_STALE_TEXT = [
    "所有节日当天时间停止流逝",
    "所有节日日必定晴天",
    "夜市是唯一在晚上开放的节日",
    "Elegant Turban",
    "主要商船商品",
    "其他随机钓鱼物品",
    "约20个左右",
    "评分公式（简化）",
    "不可错过物品",
]


def load_generator_module():
    spec = importlib.util.spec_from_file_location("gamedocs_festival_generator", GENERATOR)
    if spec is None or spec.loader is None:
        raise AssertionError("无法加载节日数据生成器")
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

    festival = FESTIVAL.read_text(encoding="utf-8")
    time_mechanism = TIME_MECHANISM.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")

    assert_contains(
        festival,
        [
            "节日名册 | 预计 12 / 实际 12",
            "实际活动日期 | 预计 18 / 实际 18",
            "节日页预计 13 / 实际 13；上游缺口补全源预计 2 / 实际 2；合计 15",
            "节日源表 | 92 张；数据行 1052；规则事实块 242",
            "商店库存 | 节日页明示库存表 48 张、库存行 312",
            "沙漠节村民商店 27/27",
            "展览会源评分 552/552 + 烟熏鱼补全 71/71 = 623/623",
            "鱿鱼节奖励层级 8/8",
            "冬日星回礼 30/30",
            "夜市魔法船逐日表 3/3",
            "odd-numbered years",
            "After the player is married",
            '"rare" green jelly',
            "bag's full",
            "shop unavailable",
            "all possible rewards",
            "| 数量差异 | 0 |",
            "| 验收状态 | **已完成** |",
        ],
        "festival coverage",
    )

    actual_anchors = set(re.findall(r'<a id="(source-[a-z0-9-]+)"></a>', festival))
    if actual_anchors != EXPECTED_ANCHORS:
        raise AssertionError(
            f"节日来源锚点漂移：actual={sorted(actual_anchors)}, "
            f"expected={sorted(EXPECTED_ANCHORS)}"
        )

    expected_revisions = {
        *(source.revision for source in generator.SOURCES),
        generator.FISH_REVISION,
        generator.SMOKED_FISH_REVISION,
    }
    actual_revisions = {int(value) for value in re.findall(r"oldid=(\d+)", festival)}
    if actual_revisions != expected_revisions:
        raise AssertionError(
            f"节日固定 revision 漂移：actual={sorted(actual_revisions)}, "
            f"expected={sorted(expected_revisions)}"
        )

    assert_contains(
        time_mechanism,
        [
            "## 6. 节日与多日活动",
            "12/12 个活动、18/18 个实际活动日期",
            "沙漠节、鳟鱼大赛、鱿鱼节、夜市",
            "世界时钟继续推进",
            "封闭式节日",
            "[节日活动数据总览](../数值数据/节日活动数据总览.md)",
            "节日具体日期不在此复制",
        ],
        "time/festival boundary",
    )

    stale_scope = festival + "\n" + time_mechanism
    stale = [value for value in FORBIDDEN_STALE_TEXT if value in stale_scope]
    if stale:
        raise AssertionError(f"旧节日节选或错误口径残留：{stale}")
    unresolved = [value for value in ("待补充", "待核实") if value in festival]
    if unresolved:
        raise AssertionError(f"生成节日文档含未决标记：{unresolved}")

    festival_kb = FESTIVAL.stat().st_size / 1024
    assert_contains(
        overview,
        [f"[节日活动数据总览](./数值数据/节日活动数据总览.md) | {festival_kb:.1f} KB"],
        "overview alignment",
    )
    assert_contains(
        audit,
        [
            "12 个活动、18 个实际活动日期",
            "节日源表 92 张、数据行 1052、规则事实块 242",
            "48 张库存表、312 条库存行",
            "展览会 552 条源评分 + 71 条烟熏鱼补全",
            "17 份数值数据文档已全部完成",
            "下一阶段进入团队与开发历程专题",
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
        "audit: festivals=12/12, date_instances=18/18, sources=15/15, "
        "source_tables=92, source_rows=1052, facts=242, shop_tables=48, "
        "shop_rows=312, desert_shops=27/27, fair_scores=552+71/623, "
        "squid_prizes=8/8, feast_gifts=30/30, night_magic_days=3/3, "
        f"revisions={len(expected_revisions)}/{len(expected_revisions)}, "
        f"audited_docs={len(AUDITED_DOCS)}, local_links={local_links}, "
        f"anchors={anchor_links}, broken_links=0, stale_claims=0, unresolved=0"
    )


if __name__ == "__main__":
    main()
