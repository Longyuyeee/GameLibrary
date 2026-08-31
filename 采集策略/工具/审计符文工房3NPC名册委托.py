#!/usr/bin/env python3
"""审计《符文工房3》角色注册表、委托注册表及机制归属。"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "符文工房3"
HUB = GAME / "数值数据" / "NPC数据总览.md"
ROSTER = GAME / "数值数据" / "NPC名册数据总览.md"
REQUESTS = GAME / "数值数据" / "委托任务数据总览.md"
MECHANISM = GAME / "机制分析" / "NPC社交系统.md"
REQUEST_MECHANISM = GAME / "特色文档" / "委托任务系统.md"
OVERVIEW = GAME / "游戏概览.md"
AUDIT = ROOT / "采集策略" / "审计记录" / "牧场经营类" / "符文工房3.md"
PLAN = ROOT / "采集策略" / "全库补全与导航重构计划.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成符文工房3NPC名册委托数据.py"
API = "https://therunefactory.fandom.com/api.php"

CHARACTER_REVISION = 127187
REQUEST_REVISION = 115531
RELATIONSHIP_REVISION = 98720
SECTIONS = {
    "Protagonist": 1,
    "Children": 2,
    "Bachelorettes": 11,
    "Villagers": 13,
    "Guests": 2,
}
BACHELORETTES = {
    "Shara", "Collette", "Marian", "Karina", "Pia", "Sofia",
    "Sakuya", "Carmen", "Raven", "Daria", "Kuruna",
}
STALE_CLAIMS = [
    "**Leo**",
    "邮箱(Mailbox) | 无每日限制",
    "多个委托可同时持有",
    "每个候补有9-10个专属委托",
    "每个候补(11位)有 **9-10个专属委托**",
    "完成全部10个委托是**结婚的必须条件**",
]


def fetch_revision(revision: int) -> tuple[str, str]:
    query = urllib.parse.urlencode(
        {
            "action": "query",
            "prop": "revisions",
            "revids": revision,
            "rvprop": "ids|content",
            "rvslots": "main",
            "format": "json",
            "formatversion": 2,
            "origin": "*",
        }
    )
    request = urllib.request.Request(
        f"{API}?{query}", headers={"User-Agent": "GameDocs-v2.9-audit/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    page = data["query"]["pages"][0]
    revision_data = page["revisions"][0]
    if revision_data["revid"] != revision:
        raise AssertionError(f"revision 漂移：{revision_data['revid']}/{revision}")
    return page["title"], revision_data["slots"]["main"]["content"]


def parse_characters(text: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for section in SECTIONS:
        match = re.search(
            rf"^==\s*{re.escape(section)}\s*==\s*(.*?)(?=^==|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            raise AssertionError(f"角色源缺少分组：{section}")
        result[section] = re.findall(
            r"'''\[\[(?:[^|\]]+\|)?([^\]]+)\]\]'''", match.group(1)
        )
    return result


def parse_requests(text: str, known_names: list[str]) -> list[tuple[int, str, str]]:
    poem = re.search(r"<poem>(.*?)</poem>", text, re.DOTALL)
    if not poem:
        raise AssertionError("委托固定源缺少 Request List 原始块")
    entries: list[tuple[int, str, str]] = []
    for hexadecimal, raw_label in re.findall(
        r"\[([0-9A-F]{8})\]\s*\n([^\n]+?)\{end\}", poem.group(1)
    ):
        identifier = int(hexadecimal, 16)
        if raw_label == "Dummy":
            continue
        issuer = next(
            (
                name
                for name in known_names
                if raw_label.startswith(f"{name}: ")
                or raw_label.startswith(f"{name} quest ")
            ),
            "Other",
        )
        entries.append((identifier, issuer, raw_label))
    return entries


def exact_anchor_count(text: str, prefix: str, expected: int) -> None:
    anchors = re.findall(rf'<a id="({re.escape(prefix)}[a-z0-9-]+)"></a>', text)
    if len(anchors) != expected or len(set(anchors)) != expected:
        raise AssertionError(
            f"{prefix} anchors={len(anchors)}, unique={len(set(anchors))}, expected={expected}"
        )


def assert_contains(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    if missing:
        raise AssertionError(f"{label} 缺少：{missing}")


def main() -> None:
    character_title, character_source = fetch_revision(CHARACTER_REVISION)
    request_title, request_source = fetch_revision(REQUEST_REVISION)
    relationship_title, relationship_source = fetch_revision(RELATIONSHIP_REVISION)

    groups = parse_characters(character_source)
    actual_groups = {name: len(values) for name, values in groups.items()}
    if actual_groups != SECTIONS:
        raise AssertionError(f"角色分组差异：actual={actual_groups}, expected={SECTIONS}")
    names = [name for values in groups.values() for name in values]
    if len(names) != 29 or len(set(names)) != 29:
        raise AssertionError(f"角色全集差异：count={len(names)}, unique={len(set(names))}")

    known_issuers = groups["Bachelorettes"] + groups["Villagers"]
    entries = parse_requests(request_source, known_issuers)
    identifiers = [entry[0] for entry in entries]
    if identifiers != list(range(1, 295)):
        raise AssertionError("委托 ID 不是连续的 1..294")
    issuer_counts = Counter(entry[1] for entry in entries)
    candidate_entries = sum(issuer_counts[name] for name in BACHELORETTES)
    if candidate_entries != 132 or any(issuer_counts[name] != 12 for name in BACHELORETTES):
        raise AssertionError(f"候补委托注册槽位差异：{candidate_entries}/132, {issuer_counts}")

    for value in (
        "Only one request for each quest listing can be accepted per day",
        "not possible to do two requests at the same time",
        "has 9 unique quests",
    ):
        if value not in request_source:
            raise AssertionError(f"Requests 固定源缺少规则：{value}")
    if "finish 10 of the bachelorette's requests" not in relationship_source:
        raise AssertionError("Relationships 固定源缺少结婚 10 委托规则")

    print(
        f"SOURCE characters={character_title}@{CHARACTER_REVISION} 29/29, "
        f"requests={request_title}@{REQUEST_REVISION} 294/294, "
        f"relationships={relationship_title}@{RELATIONSHIP_REVISION}, "
        f"candidate_request_slots={candidate_entries}/132"
    )

    if not GENERATOR.exists():
        raise AssertionError(f"缺少生成器：{GENERATOR.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True)

    roster = ROSTER.read_text(encoding="utf-8")
    requests = REQUESTS.read_text(encoding="utf-8")
    hub = HUB.read_text(encoding="utf-8")
    mechanism = MECHANISM.read_text(encoding="utf-8")
    request_mechanism = REQUEST_MECHANISM.read_text(encoding="utf-8")
    overview = OVERVIEW.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    plan = PLAN.read_text(encoding="utf-8")

    assert_contains(
        roster,
        [
            "| 预计条目数 | 29",
            "| 实际收录数 | 29",
            "| 数量差异 | 0",
            "主角 1/1",
            "子女形态 2/2",
            "候补 11/11",
            "村民 13/13",
            "访客 2/2",
            f"oldid={CHARACTER_REVISION}",
        ],
        "角色注册表",
    )
    assert_contains(
        requests,
        [
            "| 预计条目数 | 294",
            "| 实际收录数 | 294",
            "| 数量差异 | 0",
            "ID 1–294 连续",
            "候补注册条目 132/132",
            "每位候补 12/12",
            "9 个 unique quests",
            "完成 10 个该候补委托",
            f"oldid={REQUEST_REVISION}",
            f"oldid={RELATIONSHIP_REVISION}",
        ],
        "委托注册表",
    )
    exact_anchor_count(roster, "character-", 29)
    exact_anchor_count(requests, "request-", 294)

    combined_mechanisms = mechanism + request_mechanism
    stale = [value for value in STALE_CLAIMS if value in combined_mechanisms]
    if stale:
        raise AssertionError(f"NPC/委托机制仍含旧错误：{stale}")
    assert_contains(
        combined_mechanisms,
        [
            "[角色注册表 29/29]",
            "[委托注册表 294/294]",
            "每个来源每天至多接受 1 个",
            "同一时间只能进行 1 个委托",
            "12 个注册条目",
            "9 个 unique quests",
            "结婚要求完成 10 个该候补委托",
        ],
        "机制归属",
    )
    assert_contains(hub, ["NPC 子域完成状态 | 3/5", "礼物 | 已完成", "日程 | 采集中", "角色事件 | 采集中"], "NPC 数据中心")
    assert_contains(overview, ["内容文档数: 27 份", "数值数据 | 12 篇", "NPC名册数据总览", "NPC礼物数据总览", "委托任务数据总览"], "游戏概览")
    assert_contains(audit, ["数据文档完成状态 | 3/12", "NPC 子域 | 3/5", "角色注册表 29/29", "委托注册表 294/294", "下一阶段进入 NPC 日程数据"], "审计记录")
    assert_contains(plan, ["数据文档完成状态为 3/12", "下一阶段处理符文工房3的 NPC 日程数据"], "全库计划")

    print(
        "audit: roster=29/29, roster_anchors=29/29, requests=294/294, "
        "request_anchors=294/294, candidate_slots=132/132, fixed_revisions=3/3, "
        "stale_claims=0"
    )


if __name__ == "__main__":
    main()
