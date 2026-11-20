#!/usr/bin/env python3
"""由固定 MediaWiki revision 生成《符文工房3》角色与委托注册表。"""

from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "符文工房3"
ROSTER = GAME / "数值数据" / "NPC名册数据总览.md"
REQUESTS = GAME / "数值数据" / "委托任务数据总览.md"
API = "https://therunefactory.fandom.com/api.php"

CHARACTER_REVISION = 127187
REQUEST_REVISION = 115531
RELATIONSHIP_REVISION = 98720
SECTION_ORDER = ["Protagonist", "Children", "Bachelorettes", "Villagers", "Guests"]
SECTION_LABELS = {
    "Protagonist": ("主角", "玩家角色；不计入可提升关系的 NPC"),
    "Children": ("子女形态", "婚后家庭角色槽位；男孩/女孩为两个展示形态"),
    "Bachelorettes": ("候补", "可提升关系、约会与结婚"),
    "Villagers": ("村民", "常驻可提升关系对象；不可结婚"),
    "Guests": ("访客", "客串角色；可互动/送礼但不可提升常规关系"),
}


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
        f"{API}?{query}", headers={"User-Agent": "GameDocs-v2.9-generator/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    page = data["query"]["pages"][0]
    revision_data = page["revisions"][0]
    if revision_data["revid"] != revision:
        raise RuntimeError(f"revision 漂移：{revision_data['revid']}/{revision}")
    return page["title"], revision_data["slots"]["main"]["content"]


def parse_characters(text: str) -> dict[str, list[tuple[str, str]]]:
    groups: dict[str, list[tuple[str, str]]] = {}
    for section in SECTION_ORDER:
        match = re.search(
            rf"^==\s*{re.escape(section)}\s*==\s*(.*?)(?=^==|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            raise RuntimeError(f"角色源缺少分组：{section}")
        groups[section] = [
            (target, label or target)
            for target, label in re.findall(
                r"'''\[\[([^|\]]+)(?:\|([^\]]+))?\]\]'''", match.group(1)
            )
        ]
    counts = {section: len(values) for section, values in groups.items()}
    expected = {"Protagonist": 1, "Children": 2, "Bachelorettes": 11, "Villagers": 13, "Guests": 2}
    if counts != expected:
        raise RuntimeError(f"角色分组差异：{counts}/{expected}")
    return groups


def parse_requests(text: str, known_names: list[str]) -> list[tuple[int, str, str]]:
    poem = re.search(r"<poem>(.*?)</poem>", text, re.DOTALL)
    if not poem:
        raise RuntimeError("委托源缺少 Request List 原始块")
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
    if [entry[0] for entry in entries] != list(range(1, 295)):
        raise RuntimeError("委托 ID 不是连续的 1..294")
    return entries


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def wiki_url(title: str) -> str:
    return "https://therunefactory.fandom.com/wiki/" + urllib.parse.quote(
        title.replace(" ", "_"), safe=""
    )


def render_roster(groups: dict[str, list[tuple[str, str]]]) -> str:
    rows: list[str] = []
    index = 0
    for section in SECTION_ORDER:
        category, boundary = SECTION_LABELS[section]
        for target, display in groups[section]:
            index += 1
            rows.append(f'<a id="character-{slug(display)}"></a>')
            rows.append(
                f"| {index} | [{display}]({wiki_url(target)}) | {category} | {boundary} |"
            )
    group_rows = [
        "| 主角 | 1 | 1 | 0 |",
        "| 子女形态 | 2 | 2 | 0 |",
        "| 候补 | 11 | 11 | 0 |",
        "| 村民 | 13 | 13 | 0 |",
        "| 访客 | 2 | 2 | 0 |",
        "| **合计** | **29** | **29** | **0** |",
    ]
    return "\n".join(
        [
            "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [符文工房3概览](../游戏概览.md) > NPC名册数据总览",
            "",
            "# NPC 名册数据总览 — 符文工房3",
            "",
            "> 游戏版本：Rune Factory 3 Special（Nintendo Switch / Windows，2023）",
            ">",
            f"> 全集来源：[Characters (RF3) revision {CHARACTER_REVISION}](https://therunefactory.fandom.com/wiki/Characters_%28RF3%29?oldid={CHARACTER_REVISION})",
            "",
            "## 数据覆盖声明",
            "",
            "| 项目 | 内容 |",
            "|------|------|",
            "| 覆盖版本 | Rune Factory 3 Special；原 DS 版名称只作为同一角色的历史别名 |",
            "| 数据范围 | Characters 固定页列出的主角、子女形态、候补、村民和访客角色槽位 |",
            "| 预计条目数 | 29 |",
            "| 实际收录数 | 29 |",
            "| 数量差异 | 0 |",
            "| 字段完整率 | 29/29 均有序号、英文显示名、来源页面、类别和交互边界 |",
            f"| 主要来源 | Characters (RF3) revision {CHARACTER_REVISION} |",
            "| 验收状态 | 已完成 |",
            "",
            "本页只裁定角色注册表，不承担礼物、逐日行程或角色事件。那些子域在 [NPC 数据中心](./NPC数据总览.md) 单独记录状态。",
            "",
            "## 一、分组数量对账",
            "",
            "| 分组 | 预计 | 实际 | 差异 |",
            "|------|---:|---:|---:|",
            *group_rows,
            "",
            "对账摘要：主角 1/1、子女形态 2/2、候补 11/11、村民 13/13、访客 2/2。旧稿只列候补和村民 24 人；本页补入 Micah、两种 Child 形态、Yue 和 Mei。`Leo` 不在固定角色页中，不纳入 RF3 名册。",
            "",
            "## 二、完整角色注册表 29/29",
            "",
            "| # | 英文显示名 / 来源页 | 类别 | 交互边界 |",
            "|---:|------|------|------|",
            *rows,
            "",
            "## 三、来源与字段边界",
            "",
            f"- 固定 revision：`{CHARACTER_REVISION}`；生成器按五个源分组的全部链接顺序生成，不手工挑选角色。",
            "- 子女的 Male/Female 是来源页中的两个展示槽位，不据此推断存在两个同时出生的孩子。",
            "- Yue 与 Mei 属于 Guests；其个别礼物互动不等于可提升普通关系等级。",
            "- 中文译名将在礼物/日程子域固定本地化来源后统一建立映射，本注册表以固定源英文名作为稳定键。",
            "",
            "---",
            "",
            "[上一篇：NPC数据总览](./NPC数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：NPC礼物数据总览](./NPC礼物数据总览.md)",
            "",
        ]
    )


def render_requests(entries: list[tuple[int, str, str]], bachelorettes: list[str]) -> str:
    counts = Counter(entry[1] for entry in entries)
    issuer_order: list[str] = []
    for _, issuer, _ in entries:
        if issuer not in issuer_order:
            issuer_order.append(issuer)
    count_rows = [
        f"| {issuer} | {counts[issuer]} |"
        for issuer in issuer_order
    ]
    rows: list[str] = []
    for identifier, issuer, raw_label in entries:
        escaped = raw_label.replace("|", "\\|")
        rows.append(f'<a id="request-{identifier:03d}"></a>')
        rows.append(
            f"| {identifier} | `0x{identifier:08X}` | {issuer} | {escaped} |"
        )
    candidate_slots = sum(counts[name] for name in bachelorettes)
    if candidate_slots != 132:
        raise RuntimeError(f"候补注册条目差异：{candidate_slots}/132")
    return "\n".join(
        [
            "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [符文工房3概览](../游戏概览.md) > 委托任务数据总览",
            "",
            "# 委托任务数据总览 — 符文工房3",
            "",
            "> 游戏版本：Rune Factory 3 Special（Nintendo Switch / Windows，2023）",
            ">",
            f"> 注册表来源：[Requests (RF3) revision {REQUEST_REVISION}](https://therunefactory.fandom.com/wiki/Requests_%28RF3%29?oldid={REQUEST_REVISION}) · 关系规则：[Relationships revision {RELATIONSHIP_REVISION}](https://therunefactory.fandom.com/wiki/Relationships_%28RF3%29?oldid={RELATIONSHIP_REVISION})",
            "",
            "## 数据覆盖声明",
            "",
            "| 项目 | 内容 |",
            "|------|------|",
            "| 覆盖版本 | Rune Factory 3 / Special 共用的英文 Request List 注册表 |",
            "| 数据范围 | 固定页原始块中的实际委托 ID、十六进制 ID、规范发布者和原始英文标签；不把未公开的条件/奖励字段填成假定值 |",
            "| 预计条目数 | 294 |",
            "| 实际收录数 | 294 |",
            "| 数量差异 | 0 |",
            "| 字段完整率 | 294/294 均保留十进制 ID、十六进制 ID、发布者与原始标签 |",
            f"| 主要来源 | Requests revision {REQUEST_REVISION}；Relationships revision {RELATIONSHIP_REVISION} |",
            "| 验收状态 | 已完成 |",
            "",
            "固定源 Request List 的 ID 0 是 `Dummy`；本页收录全部实际委托，ID 1–294 连续、无缺号、无重复。条件、需求物、奖励和剧情结果不在该原始注册块中，因此不伪造为本表字段。",
            "",
            "## 一、发布者数量对账",
            "",
            "| 规范发布者 | 注册条目数 |",
            "|------|---:|",
            *count_rows,
            f"| **合计** | **{len(entries)}** |",
            "",
            "候补注册条目 132/132：11 位候补每位候补 12/12 个注册条目。Requests 正文同时说明每位候补有 **9 个 unique quests**；Relationships 则说明结婚要求**完成 10 个该候补委托**。注册槽位、唯一剧情委托和结婚计数是三个不同口径，不能合并成“每人 10 个专属委托”。",
            "",
            "## 二、完整委托注册表 294/294",
            "",
            "| 十进制 ID | 十六进制 ID | 规范发布者 | 固定源原始标签 |",
            "|---:|------|------|------|",
            *rows,
            "",
            "## 三、规则边界",
            "",
            "- Requests 固定页明确：公告板、邮箱和猫头鹰三个来源中，每个来源每天至多接受 1 个委托。",
            "- 同一时间只能进行 1 个委托；完成或取消当前委托后才能接取另一个。取消后，当天不能再从同一来源接取新委托。",
            "- `Wells quest 23` 等标签按固定源原文保留；规范发布者列只用于检索归组，不改写原始标签。",
            "- 玩法解释见 [委托任务系统](../特色文档/委托任务系统.md)，角色范围见 [NPC名册数据总览](./NPC名册数据总览.md)。",
            "",
            "---",
            "",
            "[上一篇：NPC日程数据总览](./NPC日程数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：作物数据总览](./作物数据总览.md)",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    _, character_source = fetch_revision(CHARACTER_REVISION)
    _, request_source = fetch_revision(REQUEST_REVISION)
    _, relationship_source = fetch_revision(RELATIONSHIP_REVISION)
    if "finish 10 of the bachelorette's requests" not in relationship_source:
        raise RuntimeError("Relationships 固定源缺少结婚委托规则")

    groups = parse_characters(character_source)
    bachelorettes = [display for _, display in groups["Bachelorettes"]]
    villagers = [display for _, display in groups["Villagers"]]
    entries = parse_requests(request_source, bachelorettes + villagers)
    outputs = {
        ROSTER: render_roster(groups),
        REQUESTS: render_requests(entries, bachelorettes),
    }

    if args.check:
        mismatches = [
            path.relative_to(ROOT)
            for path, expected in outputs.items()
            if not path.exists() or path.read_text(encoding="utf-8") != expected
        ]
        if mismatches:
            raise SystemExit(f"generated documents differ: {mismatches}")
    else:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8", newline="\n")

    print(
        "generation: characters=29/29 (1+2+11+13+2), requests=294/294, "
        "request_ids=1..294, candidate_slots=132/132, revisions=3/3"
    )


if __name__ == "__main__":
    main()
