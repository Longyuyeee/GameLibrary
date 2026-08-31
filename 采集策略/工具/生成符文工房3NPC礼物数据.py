#!/usr/bin/env python3
"""由固定 MediaWiki revision 生成《符文工房3》NPC 礼物全集文档。"""

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
OUTPUT = GAME / "数值数据" / "NPC礼物数据总览.md"
API = "https://therunefactory.fandom.com/api.php"
CHARACTER_REVISION = 127187
RELATIONSHIP_REVISION = 98720
GROUP_LABELS = {"Bachelorettes": "候补", "Villagers": "村民", "Guests": "访客"}
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
FIELDS = (
    ("LovedGifts", "最爱（Loved）"),
    ("LikedGifts", "喜欢（Liked）"),
    ("NeutralGifts", "中立（Neutral）"),
    ("DislikedGifts", "讨厌（Disliked）"),
)


def api(params: dict[str, str]) -> dict:
    query = urllib.parse.urlencode(
        {**params, "format": "json", "formatversion": "2", "origin": "*"}
    )
    request = urllib.request.Request(
        f"{API}?{query}", headers={"User-Agent": "GameDocs-v2.9-gift-generator/1.0"}
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
        raise RuntimeError(f"固定 revision 缺失：{missing}")
    return found


def gift_section(text: str) -> str:
    match = re.search(
        r"^==\s*Gifts?\s*==\s*(.*?)(?=^==[^=]|\Z)",
        text,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if not match:
        raise RuntimeError("角色页缺少 Gifts 章节")
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


def character_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    for group in GROUP_LABELS:
        match = re.search(
            rf"^==\s*{group}\s*==\s*(.*?)(?=^==|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
        if not match:
            raise RuntimeError(f"角色全集缺少分组：{group}")
        entries.extend(
            (group, target, label or target)
            for target, label in re.findall(
                r"'''\[\[([^|\]]+)(?:\|([^\]]+))?\]\]'''", match.group(1)
            )
        )
    return entries


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def wiki_url(title: str) -> str:
    title = title.lstrip(":").replace(" ", "_")
    return "https://therunefactory.fandom.com/wiki/" + urllib.parse.quote(title, safe="/:#")


def source_url(title: str, revision: int) -> str:
    return f"{wiki_url(title)}?oldid={revision}"


def plain_template(match: re.Match[str]) -> str:
    parts = [part.strip() for part in match.group(1).split("|")]
    return parts[-1] if parts else ""


def readable_wikitext(value: str) -> tuple[str, list[str]]:
    notes = [re.sub(r"\s+", " ", note).strip() for note in re.findall(r"<!--(.*?)-->", value, re.DOTALL)]
    text = re.sub(r"<!--.*?-->", "", value, flags=re.DOTALL)
    text = re.sub(r"\[\[(?:File|Image):[^\]]+\]\]", "", text, flags=re.IGNORECASE)

    def rf3_item(match: re.Match[str]) -> str:
        item = match.group(1).strip()
        return f"[{item}]({wiki_url(item)})"

    text = re.sub(r"{{RF3I\|([^{}|]+)(?:\|[^{}]*)?}}", rf3_item, text, flags=re.IGNORECASE)
    text = re.sub(r"{{(?:Blue|Color|Hover)\|([^{}]+)}}", plain_template, text, flags=re.IGNORECASE)

    text = re.sub(r"\[\[([^\]]|\](?!\]))+\]\]", lambda match: wiki_link_parts(match.group(0)), text)
    text = re.sub(r"<br\s*/?>", "；", text, flags=re.IGNORECASE)
    text = re.sub(r"</?[^>]+>", "", text)
    text = text.replace("'''", "").replace("''", "")
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip(" ,")
    if any(marker in text for marker in ("[[", "]]", "{{", "}}", "<!--")):
        raise RuntimeError(f"存在未解析 Wiki 标记：{text[:160]}")
    return text or "来源未定义", [note for note in notes if note]


def wiki_link_parts(raw: str) -> str:
    inner = raw[2:-2]
    target, separator, label = inner.partition("|")
    target = target.strip()
    label = (label if separator else target).strip()
    label = re.sub(r"'{2,3}", "", label)
    return f"[{label}]({wiki_url(target)})"


def render_standard(
    number: int,
    display: str,
    target: str,
    group: str,
    revision: int,
    source: str,
) -> list[str]:
    section = gift_section(source)
    fields = template_fields(section)
    lines = [
        f'<a id="gift-character-{slug(display)}"></a>',
        f"### {number}. {display}（{GROUP_LABELS[group]}）",
        "",
        f"固定来源：[{target} revision {revision}]({source_url(target, revision)})",
        "",
    ]
    all_notes: list[str] = []
    for key, label in FIELDS:
        rendered, notes = readable_wikitext(fields[key])
        lines.append(f"- **{label}**：{rendered}")
        all_notes.extend(notes)
    birthday = fields.get("BirthdayGifts", "").strip()
    if birthday:
        rendered, notes = readable_wikitext(birthday)
        lines.append(f"- **生日字段**：{rendered}")
        all_notes.extend(notes)
    unique_notes = list(dict.fromkeys(all_notes))
    if unique_notes:
        lines.extend([f"- **来源编辑备注**：{note}" for note in unique_notes])
    lines.append("")
    return lines


def render_yue(number: int, revision: int, source: str) -> list[str]:
    fields = template_fields(gift_section(source))
    loved, loved_notes = readable_wikitext(fields.get("LovedGifts", ""))
    disliked, disliked_notes = readable_wikitext(fields.get("DislikedGifts", ""))
    notes = list(dict.fromkeys([*loved_notes, *disliked_notes]))
    lines = [
        '<a id="gift-character-yue"></a>',
        f"### {number}. Yue（访客）",
        "",
        f"固定来源：[Yue (RF3) revision {revision}]({source_url('Yue (RF3)', revision)})",
        "",
        f"- **最爱（Loved）**：{loved}",
        "- **喜欢（Liked）**：来源未定义",
        "- **中立（Neutral）**：来源未定义",
        f"- **讨厌（Disliked）**：{disliked}",
        "- **边界**：访客可接受礼物，但角色页未定义完整四层，空层级按原样保留。",
    ]
    lines.extend(f"- **来源编辑备注**：{note}" for note in notes)
    lines.append("")
    return lines


def render_mei(number: int, revision: int, source: str) -> list[str]:
    section = gift_section(source)
    liked_raw = "[[Baked Rice Ball]], [[Lobster]]"
    neutral_raw = "[[Grape Liqueur]], [[Salmon Rice Ball]], [[Rice Ball]], [[Wine]]"
    liked, _ = readable_wikitext(liked_raw)
    neutral, _ = readable_wikitext(neutral_raw)
    required = ["Baked Rice Ball", "Lobster", "Grape Liqueur", "Salmon Rice Ball", "Rice Ball", "Wine"]
    if any(value not in section for value in required):
        raise RuntimeError("Mei 固定页礼物例外发生变化")
    return [
        '<a id="gift-character-mei"></a>',
        f"### {number}. Mei（访客）",
        "",
        f"固定来源：[Mei (RF3) revision {revision}]({source_url('Mei (RF3)', revision)})",
        "",
        "- **最爱（Loved）**：来源未定义",
        f"- **喜欢（Liked）**：{liked}",
        f"- **中立（Neutral）**：{neutral}",
        "- **讨厌（Disliked）**：来源未定义",
        "- **边界**：页面不用标准模板；前两组对话明确说“like”，第三组使用普通致谢回应，因此按喜欢/中立分组，不补写不存在的层级。",
        "",
    ]


def render_document(fixed: dict[int, tuple[str, str]]) -> str:
    character_source = fixed[CHARACTER_REVISION][1]
    entries = character_entries(character_source)
    expected = [*STANDARD_REVISIONS, *GUEST_REVISIONS]
    if [target for _, target, _ in entries] != expected:
        raise RuntimeError("角色礼物对象与固定名册顺序不一致")

    manifest_rows: list[str] = []
    character_sections: list[str] = []
    for number, (group, target, display) in enumerate(entries, 1):
        revision = {**STANDARD_REVISIONS, **GUEST_REVISIONS}[target]
        title, source = fixed[revision]
        if title != target:
            raise RuntimeError(f"revision 标题漂移：{revision} {title}/{target}")
        structure = "标准四层" if target in STANDARD_REVISIONS else "访客例外"
        manifest_rows.append(
            f"| {number} | [{display}](#gift-character-{slug(display)}) | {GROUP_LABELS[group]} | {revision} | {structure} |"
        )
        if target == "Yue (RF3)":
            character_sections.extend(render_yue(number, revision, source))
        elif target == "Mei (RF3)":
            character_sections.extend(render_mei(number, revision, source))
        else:
            character_sections.extend(
                render_standard(number, display, target, group, revision, source)
            )

    return "\n".join(
        [
            "[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [符文工房3概览](../游戏概览.md) > NPC礼物数据总览",
            "",
            "# NPC 礼物数据总览 — 符文工房3",
            "",
            "> 游戏版本：Rune Factory 3 Special（Nintendo Switch / Windows，2023）",
            ">",
            f"> 对象来源：[Characters (RF3) revision {CHARACTER_REVISION}](https://therunefactory.fandom.com/wiki/Characters_%28RF3%29?oldid={CHARACTER_REVISION}) · 点数规则：[Relationships revision {RELATIONSHIP_REVISION}](https://therunefactory.fandom.com/wiki/Relationships_%28RF3%29?oldid={RELATIONSHIP_REVISION})",
            "",
            "## 数据覆盖声明",
            "",
            "| 项目 | 内容 |",
            "|------|------|",
            "| 覆盖对象 | 礼物对象 26/26：候补 11、村民 13、访客 2 |",
            "| 排除对象 | Micah 为玩家角色；Child 固定页明确不接受礼物 |",
            "| 标准字段 | 标准四层字段 96/96：24 名常驻关系角色 × Loved / Liked / Neutral / Disliked |",
            "| 访客字段 | 访客例外 2/2：Yue 标准模板空层级、Mei 对话式分组均按原文保留 |",
            "| 固定来源 | 角色与关系规则 2 个 revision + 角色礼物页 26 个 revision，共 28/28 |",
            "| 数量差异 | 0 |",
            "| 验收状态 | 已完成 |",
            "",
            "本页完整保留固定角色页中四个礼物偏好字段的道具、类别选择器、普通文本和编辑备注。相邻条目重复时也按来源顺序保留，不用去重掩盖源数据。",
            "",
            "## 一、礼物点数与层级口径",
            "",
            "| 来源层级 | Relationships 对应口径 | 候补爱情点数 |",
            "|------|------|---:|",
            "| Loved | favorite gift | +10 |",
            "| Liked | liked gift | +5 |",
            "| Neutral | 未列为增减项 | 0 |",
            "| Disliked | hated gift | -10 |",
            "",
            "生日送礼会让正负变化翻倍。点数表由 Relationships 固定页裁定；访客不提升常规关系，其页面礼物只作为互动偏好保存。",
            "",
            "## 二、角色来源清单 26/26",
            "",
            "| # | 角色 | 类别 | 固定 revision | 字段结构 |",
            "|---:|------|------|---:|------|",
            *manifest_rows,
            "",
            "## 三、完整礼物偏好",
            "",
            *character_sections,
            "## 四、来源边界",
            "",
            "- 24 名常驻关系角色的四层字段均非空；原页面中的类别链接（例如全部鱼、全部蔬菜、全部生鱼片）是集合选择器，不应擅自缩减为几个例子。",
            "- Yue 与 Mei 是访客。来源没有定义的层级明确显示“来源未定义”，不等价于所有其他物品均为 Neutral。",
            "- Steam 全村民指南只覆盖 Loved/Liked 且声明没有完成全部实测，因此仅用于人工交叉参考，不替代本页固定 revision 分母。",
            "- 本页不承担逐角色日程或角色事件；后两项状态见 [NPC 数据中心](./NPC数据总览.md)。",
            "",
            "---",
            "",
            "[上一篇：NPC名册数据总览](./NPC名册数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：NPC日程数据总览](./NPC日程数据总览.md)",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    revisions = [
        CHARACTER_REVISION,
        RELATIONSHIP_REVISION,
        *STANDARD_REVISIONS.values(),
        *GUEST_REVISIONS.values(),
    ]
    fixed = fetch_revisions(revisions)
    output = render_document(fixed)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != output:
            raise SystemExit(f"generated document differs: {OUTPUT.relative_to(ROOT)}")
    else:
        OUTPUT.write_text(output, encoding="utf-8", newline="\n")
    print(
        "generation: gift_characters=26/26, standard_profiles=24/24, "
        "standard_fields=96/96, guest_exceptions=2/2, fixed_revisions=28/28"
    )


if __name__ == "__main__":
    main()
