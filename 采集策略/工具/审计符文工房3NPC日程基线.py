#!/usr/bin/env python3
"""审计《符文工房3》NPC 日程公开来源全集与本地基线。"""

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
OUTPUT = GAME / "数值数据" / "NPC日程数据总览.md"
GENERATOR = ROOT / "采集策略" / "工具" / "生成符文工房3NPC日程基线.py"
API = "https://therunefactory.fandom.com/api.php"
MANUAL = "https://runefactory.com/rf3s/manuals/switch/04/"
GUIDE = "https://gamefaqs.gamespot.com/pc/399231-rune-factory-3-special/faqs/60999"
REVISIONS = {
    "Shara": 133438, "Collette (RF3)": 125685, "Marian": 114457,
    "Karina": 133439, "Pia": 124502, "Sofia": 133441,
    "Sakuya": 133440, "Carmen": 133455, "Raven (RF3)": 133637,
    "Daria": 133436, "Kuruna": 133442, "Wells": 125717,
    "Monica": 133454, "Gaius": 133653, "Blaise": 133443,
    "Rusk": 133456, "Marjorie": 133450, "Hazel": 133458,
    "Sherman": 133459, "Evelyn": 133451, "Shino": 133460,
    "Carlos": 133452, "Ondorus": 133453, "Zaid": 133444,
    "Yue (RF3)": 133448, "Mei (RF3)": 133449,
}
WORK_MARKERS = {
    "Wells": "Flower Shop", "Monica": "Flower Shop",
    "Raven": "Blacksmith", "Gaius": "Blacksmith",
    "Collette": "Diner", "Blaise": "Diner", "Rusk": "Diner",
    "Sherman": "Diner or Mansion", "Sofia": "Mansion",
    "Evelyn": "Mansion", "Marian": "Magic Clinic",
    "Marjorie": "Magic Clinic", "Hezel": "Grocery Store",
    "Karina": "Grocery Store", "Pia": "Inn", "Sakuya": "Inn",
    "Shino": "Inn", "Carlos": "Fishing House",
    "Carmen": "Fishing House", "Daria": "House at Privera Forest",
}


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 GameDocs-v2.9-schedule-audit/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise AssertionError(f"HTTP {response.status}: {url}")
        return response.read().decode("utf-8", "replace").replace("\r", "")


def fixed_sources() -> dict[int, tuple[str, str]]:
    query = urllib.parse.urlencode({
        "action": "query", "prop": "revisions",
        "revids": "|".join(str(value) for value in REVISIONS.values()),
        "rvprop": "ids|content", "rvslots": "main", "format": "json",
        "formatversion": "2", "origin": "*",
    })
    data = json.loads(fetch(f"{API}?{query}"))
    found = {
        revision["revid"]: (page["title"], revision["slots"]["main"]["content"])
        for page in data["query"]["pages"] for revision in page.get("revisions", [])
    }
    if set(found) != set(REVISIONS.values()):
        raise AssertionError("26 个固定角色 revision 未全部返回")
    return found


def schedule_section(text: str) -> str | None:
    match = re.search(r"^==\s*Schedule\s*==\s*(.*?)(?=^==[^=]|\Z)", text, re.M | re.S | re.I)
    return match.group(1).strip() if match else None


def require(text: str, values: list[str], label: str) -> None:
    missing = [value for value in values if value not in text]
    if missing:
        raise AssertionError(f"{label} 缺少：{missing}")


def main() -> None:
    manual = fetch(MANUAL)
    require(manual, ["Each resident has their own schedule", "heading to work or chatting"], "官方手册")
    guide = fetch(GUIDE)
    require(guide, ["NPC Location are entirely random", "static", "working at their job"], "攻略动态规则")
    for person, place in WORK_MARKERS.items():
        if not re.search(rf"\|\[ \]\s*{re.escape(person)}\s*\|\s*{re.escape(place)}", guide):
            raise AssertionError(f"攻略固定地点缺失：{person}/{place}")

    fixed = fixed_sources()
    sections: dict[str, str | None] = {}
    for target, revision in REVISIONS.items():
        title, source = fixed[revision]
        if title != target:
            raise AssertionError(f"revision 标题漂移：{revision} {title}/{target}")
        sections[target] = schedule_section(source)
    nonempty = sum(bool(value) for value in sections.values())
    empty = sum(not value for value in sections.values())
    tables = sum("{|" in (value or "") for value in sections.values())
    if (nonempty, empty, tables) != (21, 5, 1):
        raise AssertionError(f"Schedule 来源差异：nonempty={nonempty}, empty={empty}, tables={tables}")
    if not all(day in (sections["Wells"] or "") for day in ("MON", "TUE", "WED", "THU", "FRI", "HOL")):
        raise AssertionError("Wells 6 个日类型行不完整")
    print("SOURCE expected_full_routes=26, actual_tables=1, prose_or_notes=20, empty_sections=5")
    print("SOURCE official_schedule_rule=1/1, static_work_locations=20/20, dynamic_rule=1/1, fixed_revisions=26/26")

    if not GENERATOR.exists():
        raise AssertionError(f"缺少生成器：{GENERATOR.relative_to(ROOT)}")
    subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, check=True)
    output = OUTPUT.read_text(encoding="utf-8")
    anchors = set(re.findall(r'<a id="(schedule-character-[a-z0-9-]+)"></a>', output))
    targets = set(re.findall(r"\]\(#(schedule-character-[a-z0-9-]+)\)", output))
    if len(anchors) != 26 or anchors != targets:
        raise AssertionError(f"日程锚点差异：anchors={len(anchors)}, targets={len(targets)}")
    require(output, [
        "验收状态 | 采集中", "固定工作地点 | 20/20", "非空 Schedule 章节 21/26",
        "空 Schedule 章节 5/26", "结构化来源表 1/26", "动态/随机移动",
        "完整确定路线 0/26", "### 26. Mei", "Wells 来源表 6/6",
    ], "本地日程基线")
    unresolved = [marker for marker in ("[[", "]]", "{|", "|}", "...省略") if marker in output]
    if unresolved:
        raise AssertionError(f"日程文档仍含未解析或省略标记：{unresolved}")
    print("audit: schedule_characters=26/26, anchors=26/26, static_work_locations=20/20, source_sections=26/26, completion_claim=0")


if __name__ == "__main__":
    main()
