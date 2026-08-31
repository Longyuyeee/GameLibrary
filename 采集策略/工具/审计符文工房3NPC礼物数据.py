#!/usr/bin/env python3
"""审计《符文工房3》全部可送礼角色的固定来源与生成文档。"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "符文工房3"
GENERATOR = ROOT / "采集策略" / "工具" / "生成符文工房3NPC礼物数据.py"
OUTPUT = GAME / "数值数据" / "NPC礼物数据总览.md"
HUB = GAME / "数值数据" / "NPC数据总览.md"
MECHANISM = GAME / "机制分析" / "NPC社交系统.md"
OVERVIEW = GAME / "游戏概览.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "符文工房3.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
API = "https://therunefactory.fandom.com/api.php"

CHARACTER_REVISION = 127187
RELATIONSHIP_REVISION = 98720
STANDARD_REVISIONS = {
    "Shara": 133438,
    "Collette (RF3)": 125685,
    "Marian": 114457,
    "Karina": 133439,
    "Pia": 124502,
    "Sofia": 133441,
    "Sakuya": 133440,
    "Carmen": 133455,
    "Raven (RF3)": 133637,
    "Daria": 133436,
    "Kuruna": 133442,
    "Wells": 125717,
    "Monica": 133454,
    "Gaius": 133653,
    "Blaise": 133443,
    "Rusk": 133456,
    "Marjorie": 133450,
    "Hazel": 133458,
    "Sherman": 133459,
    "Evelyn": 133451,
    "Shino": 133460,
    "Carlos": 133452,
    "Ondorus": 133453,
    "Zaid": 133444,
}
GUEST_REVISIONS = {"Yue (RF3)": 133448, "Mei (RF3)": 133449}
FIELDS = ("LovedGifts", "LikedGifts", "NeutralGifts", "DislikedGifts")


def api(params: dict[str, str]) -> dict:
    query = urllib.parse.urlencode(
        {**params, "format": "json", "formatversion": "2", "origin": "*"}
    )
    request = urllib.request.Request(
        f"{API}?{query}", headers={"User-Agent": "GameDocs-v2.9-gift-audit/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_revisions(revisions: list[int]) -> dict[int, tuple[str, str]]:
    data = api(
        {
            "action": "query",
            "prop": "revisions",
            "revids": "|".join(str(value) for value in revisions),
            "rvprop": "ids|content",
            "rvslots": "main",
        }
    )
    found: dict[int, tuple[str, str]] = {}
    for page in data["query"]["pages"]:
        for revision in page.get("revisions", []):
            found[revision["revid"]] = (
                page["title"], revision["slots"]["main"]["content"]
            )
    missing = sorted(set(revisions) - set(found))
    if missing:
        raise AssertionError(f"固定 revision 缺失：{missing}")
    return found


def gift_section(text: str) -> str:
    match = re.search(
        r"^==\s*Gifts?\s*==\s*(.*?)(?=^==[^=]|\Z)",
        text,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if not match:
        raise AssertionError("角色页缺少 Gifts 章节")
    return match.group(1).strip()


def template_fields(section: str) -> dict[str, str]:
    markers = list(re.finditer(r"^\|\s*(\w+)\s*=\s*", section, re.MULTILINE))
    values: dict[str, str] = {}
    for index, marker in enumerate(markers):
        end = markers[index + 1].start() if index + 1 < len(markers) else len(section)
        value = section[marker.end() : end]
        if index + 1 == len(markers):
            value = re.sub(r"\n?}}\s*$", "", value)
        values[marker.group(1)] = value.strip()
    return values


def character_targets(text: str) -> list[str]:
    targets: list[str] = []
    for section_name in ("Bachelorettes", "Villagers", "Guests"):
        section = re.search(
            rf"^==\s*{section_name}\s*==\s*(.*?)(?=^==|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not section:
            raise AssertionError(f"角色全集缺少分组：{section_name}")
        targets.extend(
            target
            for target, _ in re.findall(
                r"'''\[\[([^|\]]+)(?:\|([^\]]+))?\]\]'''", section.group(1)
            )
        )
    return targets


def assert_contains(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    if missing:
        raise AssertionError(f"{label} 缺少：{missing}")


def main() -> None:
    all_revisions = [
        CHARACTER_REVISION,
        RELATIONSHIP_REVISION,
        *STANDARD_REVISIONS.values(),
        *GUEST_REVISIONS.values(),
    ]
    fixed = fetch_revisions(all_revisions)
    targets = character_targets(fixed[CHARACTER_REVISION][1])
    expected_targets = [*STANDARD_REVISIONS, *GUEST_REVISIONS]
    if targets != expected_targets:
        raise AssertionError(f"礼物对象差异：actual={targets}, expected={expected_targets}")

    filled_fields = 0
    for target, revision in STANDARD_REVISIONS.items():
        title, source = fixed[revision]
        if title != target:
            raise AssertionError(f"revision 标题漂移：{revision} {title}/{target}")
        section = gift_section(source)
        if "{{RF3Gifts" not in section:
            raise AssertionError(f"{target} 未使用标准礼物模板")
        fields = template_fields(section)
        missing = [field for field in FIELDS if not fields.get(field, "").strip()]
        if missing:
            raise AssertionError(f"{target} 礼物层级为空：{missing}")
        filled_fields += len(FIELDS)

    yue = gift_section(fixed[GUEST_REVISIONS["Yue (RF3)"]][1])
    yue_fields = template_fields(yue)
    assert_contains(yue_fields.get("LovedGifts", ""), ["Aquamarine"], "Yue Loved")
    assert_contains(yue_fields.get("DislikedGifts", ""), ["Squid"], "Yue Disliked")
    mei = gift_section(fixed[GUEST_REVISIONS["Mei (RF3)"]][1])
    mei_items = [
        "Baked Rice Ball",
        "Lobster",
        "Grape Liqueur",
        "Salmon Rice Ball",
        "Rice Ball",
        "Wine",
    ]
    assert_contains(mei, mei_items, "Mei 礼物例外")

    relationship = re.sub(r"\s+", " ", fixed[RELATIONSHIP_REVISION][1])
    assert_contains(
        relationship,
        [
            "liked gift | +5",
            "favorite gift | +10",
            "hated gift | -10",
            "birthday will increase love points by double",
        ],
        "关系点数规则",
    )
    print(
        "SOURCE gift_characters=26/26, standard_profiles=24/24, "
        f"standard_fields={filled_fields}/96, guest_exceptions=2/2, "
        f"fixed_revisions={len(all_revisions)}/{len(all_revisions)}"
    )

    if not GENERATOR.exists():
        raise AssertionError(f"缺少生成器：{GENERATOR.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True)
    output = OUTPUT.read_text(encoding="utf-8")
    anchors = set(re.findall(r'<a id="(gift-character-[a-z0-9-]+)"></a>', output))
    manifest_targets = set(re.findall(r"\]\(#(gift-character-[a-z0-9-]+)\)", output))
    if len(anchors) != 26 or len(manifest_targets) != 26 or anchors != manifest_targets:
        raise AssertionError(
            f"礼物角色锚点差异：anchors={len(anchors)}/26, "
            f"targets={len(manifest_targets)}/26"
        )
    unresolved = [marker for marker in ("[[", "{{RF3I", "<!--", "...省略") if marker in output]
    if unresolved:
        raise AssertionError(f"礼物文档仍含未解析或省略标记：{unresolved}")
    assert_contains(
        output,
        [
            "礼物对象 26/26",
            "标准四层字段 96/96",
            "访客例外 2/2",
            "来源未定义",
            "Aquamarine",
            "Baked Rice Ball",
            "oldid=133438",
            "oldid=133449",
        ],
        "礼物数据文档",
    )

    hub = HUB.read_text(encoding="utf-8")
    mechanism = MECHANISM.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")
    assert_contains(hub, ["NPC 子域完成状态 | 3/5", "礼物 | 已完成", "日程 | 采集中", "角色事件 | 采集中"], "NPC 数据中心")
    assert_contains(mechanism, ["[NPC 礼物数据 26/26]", "Loved / Liked / Neutral / Disliked"], "NPC 社交机制")
    assert_contains(overview, ["内容文档数: 27 份", "数值数据 | 12 篇", "NPC礼物数据总览"], "游戏概览")
    assert_contains(audit, ["数据文档完成状态 | 3/12", "NPC 子域 | 3/5", "礼物对象 26/26", "下一阶段进入 NPC 日程数据"], "审计记录")
    assert_contains(plan, ["数据文档完成状态为 3/12", "下一阶段处理符文工房3的 NPC 日程数据"], "全库计划")
    print(
        "audit: gift_characters=26/26, standard_profiles=24/24, "
        "standard_fields=96/96, guest_exceptions=2/2, anchors=26/26, anchor_targets=26/26, "
        "unparsed_markers=0, omissions=0"
    )


if __name__ == "__main__":
    main()
