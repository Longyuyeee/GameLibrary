#!/usr/bin/env python3
"""由固定公开来源生成《符文工房3》NPC 日程来源基线。"""

from __future__ import annotations

import argparse
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "牧场经营类" / "符文工房3"
OUTPUT = GAME / "数值数据" / "NPC日程数据总览.md"
API = "https://therunefactory.fandom.com/api.php"
MANUAL = "https://runefactory.com/rf3s/manuals/switch/04/"
GUIDE = "https://gamefaqs.gamespot.com/pc/399231-rune-factory-3-special/faqs/60999"
ROLES = [
    ("Shara", 133438, "候补"), ("Collette (RF3)", 125685, "候补"),
    ("Marian", 114457, "候补"), ("Karina", 133439, "候补"),
    ("Pia", 124502, "候补"), ("Sofia", 133441, "候补"),
    ("Sakuya", 133440, "候补"), ("Carmen", 133455, "候补"),
    ("Raven (RF3)", 133637, "候补"), ("Daria", 133436, "候补"),
    ("Kuruna", 133442, "候补"), ("Wells", 125717, "村民"),
    ("Monica", 133454, "村民"), ("Gaius", 133653, "村民"),
    ("Blaise", 133443, "村民"), ("Rusk", 133456, "村民"),
    ("Marjorie", 133450, "村民"), ("Hazel", 133458, "村民"),
    ("Sherman", 133459, "村民"), ("Evelyn", 133451, "村民"),
    ("Shino", 133460, "村民"), ("Carlos", 133452, "村民"),
    ("Ondorus", 133453, "村民"), ("Zaid", 133444, "村民"),
    ("Yue (RF3)", 133448, "访客"), ("Mei (RF3)", 133449, "访客"),
]
WORK = {
    "Wells": "Flower Shop（花店）", "Monica": "Flower Shop（花店）",
    "Raven (RF3)": "Blacksmith（铁匠铺）", "Gaius": "Blacksmith（铁匠铺）",
    "Collette (RF3)": "Diner（餐馆）", "Blaise": "Diner（餐馆）",
    "Rusk": "Diner（餐馆）", "Sherman": "Diner or Mansion（餐馆或宅邸）",
    "Sofia": "Mansion（宅邸）", "Evelyn": "Mansion（宅邸）",
    "Marian": "Magic Clinic（魔法诊所）", "Marjorie": "Magic Clinic（魔法诊所）",
    "Hazel": "Grocery Store（杂货店；攻略原文误拼 Hezel）",
    "Karina": "Grocery Store（杂货店）", "Pia": "Inn（旅馆）",
    "Sakuya": "Inn（旅馆）", "Shino": "Inn（旅馆）",
    "Carlos": "Fishing House（钓鱼屋）", "Carmen": "Fishing House（钓鱼屋）",
    "Daria": "House at Privera Forest（普利贝拉森林入口的家）",
}


def fetch_revisions() -> dict[int, tuple[str, str]]:
    query = urllib.parse.urlencode({
        "action": "query", "prop": "revisions",
        "revids": "|".join(str(revision) for _, revision, _ in ROLES),
        "rvprop": "ids|content", "rvslots": "main", "format": "json",
        "formatversion": "2", "origin": "*",
    })
    request = urllib.request.Request(
        f"{API}?{query}", headers={"User-Agent": "GameDocs-v2.9-schedule-generator/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    found = {
        revision["revid"]: (page["title"], revision["slots"]["main"]["content"])
        for page in data["query"]["pages"] for revision in page.get("revisions", [])
    }
    if len(found) != 26:
        raise RuntimeError(f"固定 revision 缺失：actual={len(found)}/26")
    return found


def schedule_section(text: str) -> str:
    match = re.search(r"^==\s*Schedule\s*==\s*(.*?)(?=^==[^=]|\Z)", text, re.M | re.S | re.I)
    return match.group(1).strip() if match else ""


def display_name(target: str) -> str:
    return target.replace(" (RF3)", "")


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def wiki_url(title: str) -> str:
    return "https://therunefactory.fandom.com/wiki/" + urllib.parse.quote(title.replace(" ", "_"), safe="/:#")


def source_url(title: str, revision: int) -> str:
    return f"{wiki_url(title)}?oldid={revision}"


def readable(value: str) -> str:
    text = re.sub(r"\[\[(?:File|Image):[^\]]+\]\]", "", value, flags=re.I)
    text = re.sub(
        r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
        lambda match: f"[{(match.group(2) or match.group(1)).strip()}]({wiki_url(match.group(1).strip())})",
        text,
    )
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<br\s*/?>", "；", text, flags=re.I)
    text = re.sub(r"</?[^>]+>", "", text)
    text = text.replace("'''", "").replace("''", "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def wells_rows(section: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for day in ("MON", "TUE", "WED", "THU", "FRI", "HOL"):
        marker = re.search(rf"\|{day}\s*$", section, re.M)
        if not marker:
            raise RuntimeError(f"Wells 来源表缺少 {day}")
        end = section.find("|-", marker.end())
        block = section[marker.end() : end if end >= 0 else len(section)]
        cells: list[str] = []
        for line in block.splitlines():
            stripped = line.strip()
            if stripped == "|}":
                continue
            if stripped.startswith(("|", "!")):
                parts = re.split(r"\s\|\s*", stripped, maxsplit=1)
                value = readable(parts[1] if len(parts) == 2 else "")
                if value:
                    cells.append(value)
        rows.append((day, " → ".join(cells) if cells else "来源单元格为空"))
    return rows


def status(target: str, section: str) -> str:
    if not section:
        return "空章节"
    if target == "Wells":
        return "结构化表"
    if target == "Monica":
        return "非日程内容"
    return "文字说明"


def render_document(fixed: dict[int, tuple[str, str]]) -> str:
    sections: dict[str, str] = {}
    manifest: list[str] = []
    details: list[str] = []
    for number, (target, revision, group) in enumerate(ROLES, 1):
        title, source = fixed[revision]
        if title != target:
            raise RuntimeError(f"revision 标题漂移：{revision} {title}/{target}")
        section = schedule_section(source)
        sections[target] = section
        name = display_name(target)
        work = WORK.get(target, "—（攻略初始城镇清单未覆盖）")
        current_status = status(target, section)
        manifest.append(
            f"| {number} | [{name}](#schedule-character-{slug(name)}) | {group} | {work} | {current_status} | {revision} |"
        )
        details.extend([
            f'<a id="schedule-character-{slug(name)}"></a>',
            f"### {number}. {name}（{group}）", "",
            f"固定来源：[{target} revision {revision}]({source_url(target, revision)})", "",
            f"- **工作地点基线**：{work}",
            f"- **Schedule 章节状态**：{current_status}",
        ])
        if not section:
            details.append("- **固定页现有内容**：空；未提供任何日程字段。")
        elif target == "Wells":
            details.extend(["- **固定页现有表格（全部 6 行；来源没有时间列标题）**：", "", "| 日类型 | 来源地点序列 |", "|------|------|"])
            details.extend(f"| {day} | {route} |" for day, route in wells_rows(section))
        else:
            details.append(f"- **固定页现有内容（完整）**：{readable(section)}")
        if target == "Monica":
            details.append("- **审计判定**：该段实际描述 Flea Market 的 Mystery Prize，不是位置或时间数据，不能计作有效日程。")
        details.append("")

    nonempty = sum(bool(value) for value in sections.values())
    empty = 26 - nonempty
    return "\n".join([
        "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [符文工房3概览](../游戏概览.md) > NPC日程数据总览",
        "", "# NPC 日程数据总览 — 符文工房3", "",
        "> 游戏版本：Rune Factory 3 Special（Nintendo Switch / Windows，2023）", ">",
        f"> 机制来源：[官方 Playing the Game 手册]({MANUAL}) · 固定工作地点：[GameFAQs 完整攻略]({GUIDE})", "",
        "## 数据覆盖声明", "", "| 项目 | 当前实际 |", "|------|------|",
        "| 日程对象 | 26/26 个可接受礼物 NPC，均有固定角色 revision 与本页锚点 |",
        "| 固定工作地点 | 20/20 个攻略初始城镇清单对象；其余 6 人不在该清单分母 |",
        f"| 固定页章节 | 非空 Schedule 章节 {nonempty}/26；空 Schedule 章节 {empty}/26 |",
        "| 结构化程度 | 结构化来源表 1/26（Wells）；文字或备注 20/26；空 5/26 |",
        "| Wells 来源表 | Wells 来源表 6/6 日类型行；来源没有时间列标题 |",
        "| 完整路线 | 完整确定路线 0/26；公开来源不足以闭合天气、节日、休息日和剧情阶段分支 |",
        "| 数量差异 | 来源章节归档 0；完整路线仍缺 26 |",
        "| 验收状态 | 采集中 |", "",
        "官方手册确认居民各有日程，会去工作或与居民聊天。攻略进一步说明：NPC 非工作状态的位置具有动态/随机移动，只有工作地点相对固定。因此这里的“完整”是**现有固定来源的无遗漏归档**，不是对 NPC 完整行程的完成声明。", "",
        "## 一、预期与实际差异", "", "| 检查项 | 完成预期 | 当前真实来源 | 判定 |", "|------|---:|---:|------|",
        "| 角色日程对象 | 26 | 26 个固定 revision | 对象齐全 |",
        "| 可复现结构化路线 | 26 | 1 | 未闭合 |",
        "| 非结构化章节 | 0 | 20 | 已完整归档，不能冒充路线 |",
        "| 空章节 | 0 | 5 | 明确缺口 |",
        "| 固定工作地点 | 20 | 20 | 攻略清单已闭合 |", "",
        "## 二、角色索引与固定地点", "", "| # | 角色 | 类别 | 固定工作地点/范围 | 固定页状态 | revision |", "|---:|------|------|------|------|---:|",
        *manifest, "", "说明：攻略将 Hazel 拼为 `Hezel`，本页按角色注册表规范为 Hazel，同时保留该差异；攻略地点只裁定工作时的静态位置，不表示角色全天固定在此。", "",
        "## 三、26 个固定页 Schedule 章节全集", "", *details,
        "## 四、尚未闭合的完整日程字段", "",
        "| 待验证维度 | 当前缺口 | 所需真实证据 |", "|------|------|------|",
        "| 普通工作日 | 除 Wells 外没有逐时段路线 | 游戏资源中的行为表，或逐角色跨时段实机轨迹 |",
        "| 休息日/假日 | 仅零散人物说明；Wells 有 HOL 行但无时间列 | 多日重复实测并记录随机分支 |",
        "| 雨天 | 公开固定页未形成 26 人雨天分支 | 雨天逐角色轨迹或行为条件数据 |",
        "| 节日 | 仅 Gaius、Ondorus、Zaid 等零散说明 | 每类节日的地图/时间轨迹 |",
        "| 剧情阶段 | Unity Festival 前后只有少量人物说明 | 关键剧情节点前后的资源条件或实机对照 |",
        "| 动态规则 | 已知非工作位置随机，但候选地点与概率未知 | 可重复运行的多日样本或反编译行为数据 |", "",
        "## 五、使用边界", "",
        "- 点击上方角色名可跳到固定 revision 的完整现有 Schedule 内容；空章节不会被删除或补写。",
        "- `normally`、`often`、`from time to time`、`randomly` 等概率性措辞全部保留，不能改写成固定必达路线。",
        "- Wells 表没有时间列标题，不能按列序擅自推断具体钟点。",
        "- 完整日程完成前，[NPC 数据中心](./NPC数据总览.md)的日程状态与 NPC 子域完成数保持不变。", "", "---", "",
        "[上一篇：NPC礼物数据总览](./NPC礼物数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：委托任务数据总览](./委托任务数据总览.md)", "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = render_document(fetch_revisions())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != output:
            raise SystemExit(f"generated document differs: {OUTPUT.relative_to(ROOT)}")
    else:
        OUTPUT.write_text(output, encoding="utf-8", newline="\n")
    print("generation: schedule_characters=26/26, source_sections=26/26, nonempty=21, empty=5, static_work_locations=20/20, wells_rows=6/6, completion_claim=0")


if __name__ == "__main__":
    main()
