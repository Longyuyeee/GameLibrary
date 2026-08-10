[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > NPC数据总览

# NPC数据总览 — 星露谷物语

> 游戏版本：Stardew Valley PC v1.6.15
>
> 本文定位：NPC 数据域入口与官方居民名册；详细数据按礼物、日程、事件、关系数值拆分

## 数据覆盖声明

| 项目 | 内容 |
|------|------|
| 覆盖版本 | PC v1.6.15 |
| 名册范围 | Stardew Valley Wiki “Villagers/居民”页面列出的可攻略人物、可社交人物和其他人物 |
| 预计居民数 | 46：34 位可送礼居民＋12 位不可送礼人物 |
| 实际收录数 | 46 |
| 数量差异 | 0 |
| 本文规定字段 | 中文名、英文名、生日、送礼能力、关系类型、详细数据入口 |
| 名册字段完整率 | 46 / 46，100% |
| NPC 数据域状态 | **采集中**：名册、礼物偏好、关系数值和日程子域完成；爱心事件子域尚未验收 |

## 一、NPC 数据域结构

| 数据维度 | 文档 | 状态 | 验收范围 |
|------|------|:--:|------|
| 居民名册 | 本文 | 已完成 | 官方 Villagers 页面 46 / 46 人 |
| 礼物偏好 | [NPC礼物数据总览](./NPC礼物数据总览.md) | 已完成 | 34 / 34 位可送礼居民，五档偏好规则和个人覆盖项 |
| 关系数值 | [NPC关系数值总览](./NPC关系数值总览.md) | 已完成 | 点数、增减、礼物倍率、衰减、公共活动、恋爱、婚姻、室友、离婚与记忆 9 / 9 规则族 |
| 日程 | [NPC日程数据总览](./NPC日程数据总览.md) | 已完成 | 34 / 34 人；英文主源 220 分区、622 分支、3,066 行，中文源完整并列，总计保留 6,115 行 |
| 爱心事件 | `NPC事件数据总览.md` | 待采集 | 触发心数、地点、时间、天气、前置、选择与后果 |

机制解读见 [NPC社交系统](../机制分析/NPC社交系统.md)。尚未创建的事件数据文档不计入已完成文档数；创建后必须先完成全集与字段对账。

## 二、可送礼居民（34/34）

### 2.1 婚恋候选人（12/12）

| # | 中文名 | 英文名 | 生日 | 送礼 | 关系类型 | 详细数据 |
|:--:|------|------|------|:--:|------|------|
| 1 | 亚历克斯 | Alex | 夏季 13日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#01-亚历克斯-alex) · [日程](./NPC日程数据总览.md#npc-schedule-alex) |
| 2 | 艾利欧特 | Elliott | 秋季 5日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#02-艾利欧特-elliott) · [日程](./NPC日程数据总览.md#npc-schedule-elliott) |
| 3 | 哈维 | Harvey | 冬季 14日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#03-哈维-harvey) · [日程](./NPC日程数据总览.md#npc-schedule-harvey) |
| 4 | 山姆 | Sam | 夏季 17日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#04-山姆-sam) · [日程](./NPC日程数据总览.md#npc-schedule-sam) |
| 5 | 塞巴斯蒂安 | Sebastian | 冬季 10日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#05-塞巴斯蒂安-sebastian) · [日程](./NPC日程数据总览.md#npc-schedule-sebastian) |
| 6 | 谢恩 | Shane | 春季 20日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#06-谢恩-shane) · [日程](./NPC日程数据总览.md#npc-schedule-shane) |
| 7 | 阿比盖尔 | Abigail | 秋季 13日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#07-阿比盖尔-abigail) · [日程](./NPC日程数据总览.md#npc-schedule-abigail) |
| 8 | 艾米丽 | Emily | 春季 27日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#08-艾米丽-emily) · [日程](./NPC日程数据总览.md#npc-schedule-emily) |
| 9 | 海莉 | Haley | 春季 14日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#09-海莉-haley) · [日程](./NPC日程数据总览.md#npc-schedule-haley) |
| 10 | 莉亚 | Leah | 冬季 23日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#10-莉亚-leah) · [日程](./NPC日程数据总览.md#npc-schedule-leah) |
| 11 | 玛鲁 | Maru | 夏季 10日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#11-玛鲁-maru) · [日程](./NPC日程数据总览.md#npc-schedule-maru) |
| 12 | 潘妮 | Penny | 秋季 2日 | 是 | 婚恋候选人 | [礼物](./NPC礼物数据总览.md#12-潘妮-penny) · [日程](./NPC日程数据总览.md#npc-schedule-penny) |

### 2.2 非婚恋可送礼居民（22/22）

| # | 中文名 | 英文名 | 生日 | 送礼 | 关系类型 | 详细数据 |
|:--:|------|------|------|:--:|------|------|
| 13 | 卡洛琳 | Caroline | 冬季 7日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#13-卡洛琳-caroline) · [日程](./NPC日程数据总览.md#npc-schedule-caroline) |
| 14 | 克林特 | Clint | 冬季 26日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#14-克林特-clint) · [日程](./NPC日程数据总览.md#npc-schedule-clint) |
| 15 | 德米特里厄斯 | Demetrius | 夏季 19日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#15-德米特里厄斯-demetrius) · [日程](./NPC日程数据总览.md#npc-schedule-demetrius) |
| 16 | 矮人 | Dwarf | 夏季 22日 | 是 | 特殊村民 | [礼物](./NPC礼物数据总览.md#16-矮人-dwarf) · [日程](./NPC日程数据总览.md#npc-schedule-dwarf) |
| 17 | 艾芙琳 | Evelyn | 冬季 20日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#17-艾芙琳-evelyn) · [日程](./NPC日程数据总览.md#npc-schedule-evelyn) |
| 18 | 乔治 | George | 秋季 24日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#18-乔治-george) · [日程](./NPC日程数据总览.md#npc-schedule-george) |
| 19 | 格斯 | Gus | 夏季 8日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#19-格斯-gus) · [日程](./NPC日程数据总览.md#npc-schedule-gus) |
| 20 | 贾斯 | Jas | 夏季 4日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#20-贾斯-jas) · [日程](./NPC日程数据总览.md#npc-schedule-jas) |
| 21 | 乔迪 | Jodi | 秋季 11日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#21-乔迪-jodi) · [日程](./NPC日程数据总览.md#npc-schedule-jodi) |
| 22 | 肯特 | Kent | 春季 4日 | 是 | 第 2 年回归村民 | [礼物](./NPC礼物数据总览.md#22-肯特-kent) · [日程](./NPC日程数据总览.md#npc-schedule-kent) |
| 23 | 科罗布斯 | Krobus | 冬季 1日 | 是 | 可邀请室友 | [礼物](./NPC礼物数据总览.md#23-科罗布斯-krobus) · [日程](./NPC日程数据总览.md#npc-schedule-krobus) |
| 24 | 雷欧 | Leo | 夏季 26日 | 是 | 姜岛村民 | [礼物](./NPC礼物数据总览.md#24-雷欧-leo) · [日程](./NPC日程数据总览.md#npc-schedule-leo) |
| 25 | 刘易斯 | Lewis | 春季 7日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#25-刘易斯-lewis) · [日程](./NPC日程数据总览.md#npc-schedule-lewis) |
| 26 | 莱纳斯 | Linus | 冬季 3日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#26-莱纳斯-linus) · [日程](./NPC日程数据总览.md#npc-schedule-linus) |
| 27 | 玛妮 | Marnie | 秋季 18日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#27-玛妮-marnie) · [日程](./NPC日程数据总览.md#npc-schedule-marnie) |
| 28 | 潘姆 | Pam | 春季 18日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#28-潘姆-pam) · [日程](./NPC日程数据总览.md#npc-schedule-pam) |
| 29 | 皮埃尔 | Pierre | 春季 26日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#29-皮埃尔-pierre) · [日程](./NPC日程数据总览.md#npc-schedule-pierre) |
| 30 | 罗宾 | Robin | 秋季 21日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#30-罗宾-robin) · [日程](./NPC日程数据总览.md#npc-schedule-robin) |
| 31 | 桑迪 | Sandy | 秋季 15日 | 是 | 沙漠村民 | [礼物](./NPC礼物数据总览.md#31-桑迪-sandy) · [日程](./NPC日程数据总览.md#npc-schedule-sandy) |
| 32 | 文森特 | Vincent | 春季 10日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#32-文森特-vincent) · [日程](./NPC日程数据总览.md#npc-schedule-vincent) |
| 33 | 威利 | Willy | 夏季 24日 | 是 | 普通村民 | [礼物](./NPC礼物数据总览.md#33-威利-willy) · [日程](./NPC日程数据总览.md#npc-schedule-willy) |
| 34 | 法师 | Wizard | 冬季 17日 | 是 | 特殊村民 | [礼物](./NPC礼物数据总览.md#34-法师-wizard) · [日程](./NPC日程数据总览.md#npc-schedule-wizard) |

## 三、不可送礼人物（12/12）

这些角色属于官方“其他人物/Non-giftable NPCs”名册，不接受常规礼物，因此没有生日礼物偏好表。

| # | 中文名 | 英文名 | 送礼 | 主要身份/功能 |
|:--:|------|------|:--:|------|
| 1 | 贝啼 | Birdie | 否 | 姜岛任务角色 |
| 2 | 门卫 | Bouncer | 否 | 沙漠俱乐部门卫 |
| 3 | 菲兹 | Fizz | 否 | 完美度豁免业务角色 |
| 4 | 吉尔 | Gil | 否 | 冒险者公会奖励角色 |
| 5 | 州长 | Governor | 否 | 夏威夷宴会评审角色 |
| 6 | 爷爷 | Grandpa | 否 | 农场评价与开场叙事角色 |
| 7 | 冈瑟 | Gunther | 否 | 博物馆管理角色 |
| 8 | 仆从 | Henchman | 否 | 女巫沼泽任务角色 |
| 9 | 马龙 | Marlon | 否 | 冒险者公会管理角色 |
| 10 | 莫里斯 | Morris | 否 | Joja 路线角色 |
| 11 | 齐先生 | Mr. Qi | 否 | 挑战、核桃房与完美度角色 |
| 12 | 蜗牛教授 | Professor Snail | 否 | 姜岛化石调查角色 |

## 四、名册对账

| 分类 | 官方预计 | 本文实际 | 差异 |
|------|:--:|:--:|:--:|
| 婚恋候选人 | 12 | 12 | 0 |
| 非婚恋可送礼居民 | 22 | 22 | 0 |
| 不可送礼人物 | 12 | 12 | 0 |
| **合计** | **46** | **46** | **0** |

## 五、来源

- [中文 Stardew Valley Wiki — 居民](https://zh.stardewvalleywiki.com/%E5%B1%85%E6%B0%91)
- [英文 Stardew Valley Wiki — Villagers](https://stardewvalleywiki.com/Villagers)
- [中文 Stardew Valley Wiki — 礼物列表](https://zh.stardewvalleywiki.com/%E7%A4%BC%E7%89%A9%E5%88%97%E8%A1%A8)
- [英文 Stardew Valley Wiki — List of All Gifts](https://stardewvalleywiki.com/List_of_All_Gifts)
- [英文 Stardew Valley Wiki — v1.6.15 NPCGiftTastes 原始数据](https://stardewvalleywiki.com/Modding:Gift_taste_data)
- [英文 Stardew Valley Wiki — Friendship revision 193702](https://stardewvalleywiki.com/mediawiki/index.php?title=Friendship&oldid=193702)
- [英文 Stardew Valley Wiki — 日程键优先级与字段](https://stardewvalleywiki.com/Modding:Schedule_data)

---

[上一篇：NPC社交系统](../机制分析/NPC社交系统.md) · [返回游戏概览](../游戏概览.md) · [下一篇：NPC礼物数据总览](./NPC礼物数据总览.md)
