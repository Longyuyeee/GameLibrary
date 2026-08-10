[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > [NPC数据总览](./NPC数据总览.md) > NPC日程数据总览

# NPC日程数据总览 — 星露谷物语

> 游戏版本：Stardew Valley PC v1.6.15
>
> 数据来源：英文 Stardew Valley Wiki 个人页为 PC v1.6.15 完整性主源；中文个人页为中文记录源
>
> 生成时逐人固定中英文 revision；两种语言的全部说明、分区、条件和时间地点行均保留

## 数据覆盖声明

| 项目 | 内容 |
|------|------|
| 数据全集定义 | 官方 Villagers 名册中 34 位可送礼居民个人页的完整日程章节 |
| 预计居民数 | 34 |
| 实际居民数 | 34 |
| 数量差异 | 0 |
| 英文主源 | 220 个分区 / 622 个条件分支 / 3066 行 |
| 中文记录源 | 220 个分区 / 619 个条件分支 / 3049 行 |
| 双源保留总量 | 440 个分区 / 1241 个条件分支 / 6115 行 |
| 必填字段 | 居民、来源 revision、分区、条件、时间、地点/行动 |
| 中英文结构一致 | 28/34 人 |
| 已审计结构差异 | 6/34 人：山姆、塞巴斯蒂安、阿比盖尔、海莉、玛鲁、刘易斯 |
| 验收状态 | **日程子域已完成**；节日地图内固定站位由节日数据域维护 |

### 读取与优先级说明

英文个人页已经按每个季节内从高到低排列分支；先满足的分支覆盖后续常规日程。游戏原始选择优先级还区分绿雨、婚后、被动节日、日期、爱心、巴士、雨天、季节星期与默认分支。本文保留个人页给出的完整顺序，不自行合并相似路线。

姜岛度假村属于个人页的通用随机覆盖说明；节日、诊所预约等排除条件同样保留在每人说明中。固定地点且没有分时表的居民以完整文字说明收录，不伪造时间行。中英文发生冲突时，以英文主源判断 PC v1.6.15 行为；中文记录仍原样保留，用于检索、对照和后续翻译校正。

## 居民索引与数量对账

| # | 居民 | 英文主源（分区/分支/行） | 中文源（分区/分支/行） | 结构 | 中文 revision | 英文 revision |
|:--:|------|:--:|:--:|:--:|:--:|:--:|
| 1 | [亚历克斯（Alex）](#npc-schedule-alex) | 5/24/119 | 5/24/119 | 一致 | [zh 55068](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E4%BA%9A%E5%8E%86%E5%85%8B%E6%96%AF&oldid=55068) | [en 193663](https://stardewvalleywiki.com/mediawiki/index.php?title=Alex&oldid=193663) |
| 2 | [艾利欧特（Elliott）](#npc-schedule-elliott) | 5/27/85 | 5/27/85 | 一致 | [zh 55231](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%89%BE%E5%88%A9%E6%AC%A7%E7%89%B9&oldid=55231) | [en 192964](https://stardewvalleywiki.com/mediawiki/index.php?title=Elliott&oldid=192964) |
| 3 | [哈维（Harvey）](#npc-schedule-harvey) | 5/27/118 | 5/27/118 | 一致 | [zh 54980](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%93%88%E7%BB%B4&oldid=54980) | [en 193951](https://stardewvalleywiki.com/mediawiki/index.php?title=Harvey&oldid=193951) |
| 4 | [山姆（Sam）](#npc-schedule-sam) | 5/41/211 | 5/37/187 | 差异已审计 | [zh 55076](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%B1%B1%E5%A7%86&oldid=55076) | [en 193676](https://stardewvalleywiki.com/mediawiki/index.php?title=Sam&oldid=193676) |
| 5 | [塞巴斯蒂安（Sebastian）](#npc-schedule-sebastian) | 5/41/261 | 5/41/260 | 差异已审计 | [zh 55064](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%A1%9E%E5%B7%B4%E6%96%AF%E8%92%82%E5%AE%89&oldid=55064) | [en 193877](https://stardewvalleywiki.com/mediawiki/index.php?title=Sebastian&oldid=193877) |
| 6 | [谢恩（Shane）](#npc-schedule-shane) | 5/29/109 | 5/29/109 | 一致 | [zh 55046](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%B0%A2%E6%81%A9&oldid=55046) | [en 193586](https://stardewvalleywiki.com/mediawiki/index.php?title=Shane&oldid=193586) |
| 7 | [阿比盖尔（Abigail）](#npc-schedule-abigail) | 5/46/257 | 5/46/256 | 差异已审计 | [zh 55185](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E9%98%BF%E6%AF%94%E7%9B%96%E5%B0%94&oldid=55185) | [en 193689](https://stardewvalleywiki.com/mediawiki/index.php?title=Abigail&oldid=193689) |
| 8 | [艾米丽（Emily）](#npc-schedule-emily) | 11/14/50 | 11/14/50 | 一致 | [zh 55091](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%89%BE%E7%B1%B3%E4%B8%BD&oldid=55091) | [en 191968](https://stardewvalleywiki.com/mediawiki/index.php?title=Emily&oldid=191968) |
| 9 | [海莉（Haley）](#npc-schedule-haley) | 5/25/132 | 5/25/133 | 差异已审计 | [zh 55013](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%B5%B7%E8%8E%89&oldid=55013) | [en 191939](https://stardewvalleywiki.com/mediawiki/index.php?title=Haley&oldid=191939) |
| 10 | [莉亚（Leah）](#npc-schedule-leah) | 5/21/93 | 5/21/93 | 一致 | [zh 55041](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%8E%89%E4%BA%9A&oldid=55041) | [en 192966](https://stardewvalleywiki.com/mediawiki/index.php?title=Leah&oldid=192966) |
| 11 | [玛鲁（Maru）](#npc-schedule-maru) | 5/24/124 | 5/25/129 | 差异已审计 | [zh 55085](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%8E%9B%E9%B2%81&oldid=55085) | [en 193560](https://stardewvalleywiki.com/mediawiki/index.php?title=Maru&oldid=193560) |
| 12 | [潘妮（Penny）](#npc-schedule-penny) | 5/38/191 | 5/38/191 | 一致 | [zh 55083](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%BD%98%E5%A6%AE&oldid=55083) | [en 193516](https://stardewvalleywiki.com/mediawiki/index.php?title=Penny&oldid=193516) |
| 13 | [卡洛琳（Caroline）](#npc-schedule-caroline) | 12/12/55 | 12/12/55 | 一致 | [zh 54977](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%8D%A1%E6%B4%9B%E7%90%B3&oldid=54977) | [en 191301](https://stardewvalleywiki.com/mediawiki/index.php?title=Caroline&oldid=191301) |
| 14 | [克林特（Clint）](#npc-schedule-clint) | 8/8/28 | 8/8/28 | 一致 | [zh 55070](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%85%8B%E6%9E%97%E7%89%B9&oldid=55070) | [en 191347](https://stardewvalleywiki.com/mediawiki/index.php?title=Clint&oldid=191347) |
| 15 | [德米特里厄斯（Demetrius）](#npc-schedule-demetrius) | 4/17/97 | 4/17/97 | 一致 | [zh 54996](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%BE%B7%E7%B1%B3%E7%89%B9%E9%87%8C%E5%8E%84%E6%96%AF&oldid=54996) | [en 193879](https://stardewvalleywiki.com/mediawiki/index.php?title=Demetrius&oldid=193879) |
| 16 | [矮人（Dwarf）](#npc-schedule-dwarf) | 0/0/0 | 0/0/0 | 一致 | [zh 54688](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%9F%AE%E4%BA%BA&oldid=54688) | [en 191010](https://stardewvalleywiki.com/mediawiki/index.php?title=Dwarf&oldid=191010) |
| 17 | [艾芙琳（Evelyn）](#npc-schedule-evelyn) | 10/10/51 | 10/10/51 | 一致 | [zh 54548](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%89%BE%E8%8A%99%E7%90%B3&oldid=54548) | [en 191129](https://stardewvalleywiki.com/mediawiki/index.php?title=Evelyn&oldid=191129) |
| 18 | [乔治（George）](#npc-schedule-george) | 10/10/36 | 10/10/36 | 一致 | [zh 54046](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E4%B9%94%E6%B2%BB&oldid=54046) | [en 193909](https://stardewvalleywiki.com/mediawiki/index.php?title=George&oldid=193909) |
| 19 | [格斯（Gus）](#npc-schedule-gus) | 9/9/31 | 9/9/31 | 一致 | [zh 55267](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%A0%BC%E6%96%AF&oldid=55267) | [en 191548](https://stardewvalleywiki.com/mediawiki/index.php?title=Gus&oldid=191548) |
| 20 | [贾斯（Jas）](#npc-schedule-jas) | 11/11/46 | 11/11/46 | 一致 | [zh 55188](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%B4%BE%E6%96%AF&oldid=55188) | [en 193899](https://stardewvalleywiki.com/mediawiki/index.php?title=Jas&oldid=193899) |
| 21 | [乔迪（Jodi）](#npc-schedule-jodi) | 4/34/210 | 4/34/210 | 一致 | [zh 55067](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E4%B9%94%E8%BF%AA&oldid=55067) | [en 191546](https://stardewvalleywiki.com/mediawiki/index.php?title=Jodi&oldid=191546) |
| 22 | [肯特（Kent）](#npc-schedule-kent) | 7/7/37 | 7/7/37 | 一致 | [zh 55035](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%82%AF%E7%89%B9&oldid=55035) | [en 193910](https://stardewvalleywiki.com/mediawiki/index.php?title=Kent&oldid=193910) |
| 23 | [科罗布斯（Krobus）](#npc-schedule-krobus) | 0/0/0 | 0/0/0 | 一致 | [zh 55028](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%A7%91%E7%BD%97%E5%B8%83%E6%96%AF&oldid=55028) | [en 192255](https://stardewvalleywiki.com/mediawiki/index.php?title=Krobus&oldid=192255) |
| 24 | [雷欧（Leo）](#npc-schedule-leo) | 8/35/177 | 8/35/177 | 一致 | [zh 55053](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E9%9B%B7%E6%AC%A7&oldid=55053) | [en 192150](https://stardewvalleywiki.com/mediawiki/index.php?title=Leo&oldid=192150) |
| 25 | [刘易斯（Lewis）](#npc-schedule-lewis) | 4/45/255 | 4/45/258 | 差异已审计 | [zh 54974](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%88%98%E6%98%93%E6%96%AF&oldid=54974) | [en 191314](https://stardewvalleywiki.com/mediawiki/index.php?title=Lewis&oldid=191314) |
| 26 | [莱纳斯（Linus）](#npc-schedule-linus) | 8/8/41 | 8/8/41 | 一致 | [zh 55042](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%8E%B1%E7%BA%B3%E6%96%AF&oldid=55042) | [en 193911](https://stardewvalleywiki.com/mediawiki/index.php?title=Linus&oldid=193911) |
| 27 | [玛妮（Marnie）](#npc-schedule-marnie) | 10/10/47 | 10/10/47 | 一致 | [zh 55084](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%8E%9B%E5%A6%AE&oldid=55084) | [en 191544](https://stardewvalleywiki.com/mediawiki/index.php?title=Marnie&oldid=191544) |
| 28 | [潘姆（Pam）](#npc-schedule-pam) | 8/8/25 | 8/8/25 | 一致 | [zh 55017](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%BD%98%E5%A7%86&oldid=55017) | [en 191550](https://stardewvalleywiki.com/mediawiki/index.php?title=Pam&oldid=191550) |
| 29 | [皮埃尔（Pierre）](#npc-schedule-pierre) | 6/6/29 | 6/6/29 | 一致 | [zh 55086](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%9A%AE%E5%9F%83%E5%B0%94&oldid=55086) | [en 192883](https://stardewvalleywiki.com/mediawiki/index.php?title=Pierre&oldid=192883) |
| 30 | [罗宾（Robin）](#npc-schedule-robin) | 10/10/43 | 10/10/43 | 一致 | [zh 55090](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%BD%97%E5%AE%BE&oldid=55090) | [en 191769](https://stardewvalleywiki.com/mediawiki/index.php?title=Robin&oldid=191769) |
| 31 | [桑迪（Sandy）](#npc-schedule-sandy) | 3/3/15 | 3/3/15 | 一致 | [zh 55081](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%A1%91%E8%BF%AA&oldid=55081) | [en 191345](https://stardewvalleywiki.com/mediawiki/index.php?title=Sandy&oldid=191345) |
| 32 | [文森特（Vincent）](#npc-schedule-vincent) | 11/11/49 | 11/11/49 | 一致 | [zh 55079](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%96%87%E6%A3%AE%E7%89%B9&oldid=55079) | [en 193876](https://stardewvalleywiki.com/mediawiki/index.php?title=Vincent&oldid=193876) |
| 33 | [威利（Willy）](#npc-schedule-willy) | 11/11/44 | 11/11/44 | 一致 | [zh 55075](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%A8%81%E5%88%A9&oldid=55075) | [en 192689](https://stardewvalleywiki.com/mediawiki/index.php?title=Willy&oldid=192689) |
| 34 | [法师（Wizard）](#npc-schedule-wizard) | 0/0/0 | 0/0/0 | 一致 | [zh 55012](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%B3%95%E5%B8%88&oldid=55012) | [en 193912](https://stardewvalleywiki.com/mediawiki/index.php?title=Wizard&oldid=193912) |

## 逐人日程全集

<a id="npc-schedule-alex"></a>

### 01. 亚历克斯（Alex）

> 来源：中文 revision 55068；英文 revision 193663
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个分区、24 个条件分支、119 行。

- 春季 时，除非下雨，亚历克斯一般会在08:00出门，站在房子右边的一棵树下。在下午时他会走到狗窝旁边。
- 夏季 时，亚历克斯通常会在早上去海滩，下午时则去 博物馆 左边的 冰淇淋摊 工作。在夏季16日，他会前往 哈维的诊所 体检。
- 冬季 时，他几乎每天都会 温泉 里的健身房锻炼。
- 姜岛 海滩度假村修复后，亚历克斯偶尔会去度个假，直到18:00离开回 家 睡觉，亚历克斯不会在他体检日和 节日 当天去度假。
- 下面显示的是亚历克斯的行程表，从上到下优先级逐次下降，例如雨天行程的优先级会比在它下面的高。

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 出门站在 家 旁边的树下。 |
| 10:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:30 | 站在厨师处。 |
| 00:50 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开他的房间站在家门口旁边。 |
| 13:00 | 回到自己的房间练习举重。 |
| 16:00 | 出门站在靠近房子的狗窝旁边。 |
| 18:30 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期三（玩家与亚历克斯和 海莉 的友谊均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 12:00 | 前往 海莉和艾米丽的家 。 |
| 16:30 | 离开海莉和艾米丽的家来到狗窝旁边。 |
| 18:40 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期天（已触发亚历克斯14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 11:00 | 前往 星之果实酒吧 的里屋。 |
| 15:00 | 离开星之果实酒吧来到狗窝旁边。 |
| 18:30 | 进入他家，站在家门口旁边。 |
| 20:00 | 回到他的房间里。 |
| 22:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 13:00 | 回到自己的房间练习举重。 |
| 16:00 | 出门站在靠近房子的狗窝旁边。 |
| 18:30 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于厨房。 |

###### 夏季16日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开他的房间站在家门口旁边。 |
| 10:30 | 前往 哈维的诊所 。 |
| 11:00 | 在诊所的等待室。 |
| 13:40 | 在诊所的检查室。 |
| 16:00 | 离开诊所回家。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开他的房间站在家门口旁边。 |
| 13:00 | 回到自己的房间练习举重。 |
| 16:00 | 出门站在靠近房子的狗窝旁边。 |
| 18:30 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期三（玩家与亚历克斯和 海莉 的友谊均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 12:00 | 前往 海莉和艾米丽的家 。 |
| 16:30 | 离开海莉和艾米丽的家来到狗窝旁边。 |
| 18:40 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期天（已触发亚历克斯14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 11:00 | 前往 星之果实酒吧 的里屋。 |
| 15:00 | 离开星之果实酒吧来到狗窝旁边。 |
| 18:30 | 进入他家，站在家门口旁边。 |
| 20:00 | 回到他的房间里。 |
| 22:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 离开家，前往 海滩 。 |
| 12:00 | 离开海滩去 博物馆 附近的 冰淇淋摊 工作。 |
| 17:00 | 回家在自己房间练习举重。 |
| 19:00 | 离开自己房间站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开他的房间站在家门口旁边。 |
| 13:00 | 回到自己的房间练习举重。 |
| 16:00 | 出门站在靠近房子的狗窝旁边。 |
| 18:30 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期三（玩家与亚历克斯和 海莉 的友谊均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 12:00 | 前往 海莉和艾米丽的家 。 |
| 16:30 | 离开海莉和艾米丽的家来到狗窝旁边。 |
| 18:40 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期天（已触发亚历克斯14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 11:00 | 前往 星之果实酒吧 的里屋。 |
| 15:00 | 离开星之果实酒吧来到狗窝旁边。 |
| 18:30 | 进入他家，站在家门口旁边。 |
| 20:00 | 回到他的房间里。 |
| 22:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 13:00 | 回到自己的房间练习举重。 |
| 16:00 | 出门站在靠近房子的狗窝旁边。 |
| 18:30 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

##### 冬季

###### 冬季17日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 出门前往 温泉 的健身房锻炼。 |
| 15:00 | 离开温泉的健身房，前往海滩参加 夜市 。 |
| 00:00 | 离开夜市回家。 |

###### 星期三（玩家与亚历克斯和 海莉 的友谊均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 12:00 | 前往 海莉和艾米丽的家 。 |
| 16:30 | 离开海莉和艾米丽的家来到狗窝旁边。 |
| 18:40 | 回家站在家门口旁边。 |
| 20:00 | 回到自己的房间站在衣橱前面。 |
| 22:00 | 上床睡觉。 |

###### 星期天（已触发亚历克斯14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 出门站在家旁边的树下。 |
| 11:00 | 前往 星之果实酒吧 的里屋。 |
| 15:00 | 离开星之果实酒吧来到狗窝旁边。 |
| 18:30 | 进入他家，站在家门口旁边。 |
| 20:00 | 回到他的房间里。 |
| 22:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 待在他的房间中。 |
| 09:00 | 出门前往 温泉 的健身房锻炼。 |
| 15:00 | 离开温泉的健身房回家。 |
| 18:00 | 出门站在靠近房子的狗窝旁边。 |
| 19:30 | 回家站在家门口旁边。 |
| 21:00 | 回到自己的房间站在衣橱前面。 |
| 22:40 | 上床睡觉。 |

##### 婚后

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开农场参加 沙漠节 ，站在厨师处。 |
| 00:40 | 返回农场。 |

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 离开农场前往 河间大道1号 ，站在厨房。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农场前往 河间大道1号 探望他的祖父母。 |
| 18:00 | 返回农场。 |
| 22:00 | 上床睡觉。 |

###### 星期天（已触发亚历克斯14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农场站在他祖父母家旁边的树下。 |
| 11:00 | 前往 星之果实酒吧 的里屋。 |
| 15:00 | 离开星之果实酒吧来到狗窝旁边。 |
| 18:30 | 进入他祖父母的家，站在家门口旁边。 |
| 20:00 | 待在祖父母家自己的房间里。 |
| 22:00 | 返回农场。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、24 个条件分支、119 行。

- During Spring and Fall , Alex exits his home at 8am unless it is raining. He stands by the tree to the right of his house, playing with his gridball, and he moves towards the left of the fenced-in area in the afternoon.
- During Summer , he can be found on the beach in the morning and running the Ice Cream Stand to the left of the museum in the afternoon. On the 16th of Summer , he has an appointment at the clinic .
- During Winter , he works out at the Spa almost every day. When he is not there, he will be at his house.
- After the Beach Resort on Ginger Island is unlocked, Alex may randomly spend the day there. After leaving the Island at 6pm, Alex will immediately go home to bed. Alex never visits the Resort on Festival days or his checkup day at Harvey's Clinic .
- Shown below are Alex's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 15

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | Leaves his house to stand under the tree outside. |
| 10:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:30 AM | Stands by the chef stand. |
| 12:50 AM | Boards bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room and stands in the entryway. |
| 1:00 PM | Goes to his room to lift weights. |
| 4:00 PM | Leaves his room to go stand outside by the dog pen. |
| 6:30 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 12:00 PM | Goes to Haley and Emily's house. |
| 4:30 PM | Leaves Haley and Emily's house to go stand by the dog pen. |
| 6:40 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 11:00 AM | Goes to the back room of the Stardrop Saloon . |
| 3:00 PM | Leaves to stand by the dog kennel. |
| 6:30 PM | Goes inside of his house and stands in the entryway. |
| 8:00 PM | Goes to stand inside of his room. |
| 10:00 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 1:00 PM | Leaves the tree to go back to his room to lift weights. |
| 4:00 PM | Leaves his room to go stand outside by the dog pen. |
| 6:30 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the kitchen. |

###### Summer 16

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 10:30 AM | Goes to clinic. |
| 11:00 AM | In clinic waiting room. |
| 1:40 PM | Clinic examination room. |
| 4:00 PM | Returns home for the night. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room and stands in the entryway. |
| 1:00 PM | Goes to his room to lift weights. |
| 4:00 PM | Leaves his house to go stand by the dog pen. |
| 6:30 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 12:00 PM | Goes to Haley and Emily's house. |
| 4:30 PM | Leaves Haley and Emily's house to go stand by the dog pen. |
| 6:40 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 11:00 AM | Goes to the back room of the Stardrop Saloon . |
| 3:00 PM | Leaves to stand by the dog kennel. |
| 6:30 PM | Goes inside of his house and stands in the entryway. |
| 8:00 PM | Goes to stand inside of his room. |
| 10:00 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | Leaves home to go to beach. |
| 12:00 PM | Leaves beach to go work at ice cream stand. |
| 5:00 PM | Heads home to lift weights in his room. |
| 7:00 PM | Stands in front entryway of house. |
| 8:00 PM | Goes to his room to stand by his dresser. |
| 10:00 PM | Goes to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room and stands in the entryway. |
| 1:00 PM | Goes to his room to lift weights. |
| 4:00 PM | Leaves his house to go stand by the dog pen. |
| 6:30 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 12:00 PM | Goes to Haley and Emily's house. |
| 4:30 PM | Leaves Haley and Emily's house to go stand by the dog pen. |
| 6:40 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 11:00 AM | Goes to the back room of the Stardrop Saloon . |
| 3:00 PM | Leaves to stand by the dog kennel. |
| 6:30 PM | Goes inside of his house and stands in the entryway. |
| 8:00 PM | Goes to stand inside of his room. |
| 10:00 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 1:00 PM | Goes to his room to lift weights. |
| 4:00 PM | Leaves his house to go stand by the dog pen. |
| 6:30 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

##### Winter

###### Winter 17

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his house to go to the Spa . |
| 3:00 PM | Leaves the gym section of the Spa, heads to the beach to attend the Night Market . |
| 12:00 AM | Leaves the Night Market and returns home. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 12:00 PM | Goes to Haley and Emily's house. |
| 4:30 PM | Leaves Haley and Emily's house to go stand by the dog pen. |
| 6:40 PM | Goes back into his house and stands in the entryway. |
| 8:00 PM | Goes to his room and stands by his dresser. |
| 10:00 PM | Goes to bed. |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his room to go outside and stand beneath nearby tree. |
| 11:00 AM | Goes to the back room of the Stardrop Saloon . |
| 3:00 PM | Leaves to stand by the dog kennel. |
| 6:30 PM | Goes inside of his house and stands in the entryway. |
| 8:00 PM | Goes to stand inside of his room. |
| 10:00 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his bedroom. |
| 9:00 AM | Leaves his house to go to the Spa . |
| 3:00 PM | Leaves the gym section of the Spa, heads home to his room. |
| 6:00 PM | Leaves his house to stand by the dog kennel. |
| 7:30 PM | Goes back inside his house and stands in the entryway. |
| 9:00 PM | Goes back to his bedroom and stands by his dresser. |
| 10:40 PM | Goes to bed. |

##### Marriage

###### Spring 15

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves farm to attend the Desert Festival and stand by the chef stand. |
| 12:40 AM | Heads back to farm. |

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Leaves home to walk to his grandparents' house and stand in the kitchen. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves farm to visit his grandparents . |
| 6:00 PM | Heads back to farm. |
| 10:00 PM | Goes to bed. |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves farm to go stand beneath a tree by his grandparent's house. |
| 11:00 AM | Goes to the back room of the Stardrop Saloon . |
| 3:00 PM | Leaves to stand by the dog kennel. |
| 6:30 PM | Goes inside of his grandparent's house and stands in the entryway. |
| 8:00 PM | Goes to stand inside of his room. |
| 10:00 PM | Leaves for the Farmhouse . |

<a id="npc-schedule-elliott"></a>

### 02. 艾利欧特（Elliott）

> 来源：中文 revision 55231；英文 revision 192964
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个分区、27 个条件分支、85 行。

- 姜岛 海滩度假村 修复后，艾利欧特偶尔会去度个假，18:00离开小岛后，艾利欧特将立即回家睡觉。艾利欧特不会在节日或诊所预约日当天去度假。
- 下面是艾利欧特的时间表，在每个季节内从高到低排列。例如，如果是下雨天，这个时间表就会优先于下面的所有其他时间表。

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:00 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:40 | 站在赛跑跑道南侧的悬崖前。 |
| 01:40 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 全天 | 呆在 家 中。 |

###### 星期四 星期五（任何玩家与艾利欧特的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 皮埃尔的杂货店 。 |
| 17:30 | 离开皮埃尔的店，回家休息。 |

###### 星期五、星期天（玩家与 莉亚 的友谊低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:00 | 离开家，站在鱼店旁边的船坞上。 |
| 17:00 | 离开船坞，前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧，回家休息。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 12:00 | 离开家，站在小屋南侧的海滩上。 |
| 13:30 | 离开海滩回到小屋。 |
| 15:00 | 离开小屋，站在沙滩入口北侧的桥上。 |
| 18:00 | 离开桥，回家休息。 |

##### 夏季

###### 夏季9日

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 离开 家 ，去 哈维的诊所 。 |
| 13:30 | 从诊所内候诊室移至检查室。 |
| 16:00 | 离开诊所，回家休息。 |

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 全天 | 呆在 家 中。 |

###### 星期四 星期五（任何玩家与艾利欧特的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 皮埃尔的杂货店 。 |
| 17:30 | 离开皮埃尔的店，回家休息。 |

###### 星期五、星期天（玩家与 莉亚 的友谊低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:00 | 离开家，站在鱼店旁边的船坞上。 |
| 17:00 | 离开船坞，前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧，回家休息。 |

###### 星期五、星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 12:00 | 离开家，站在小屋南侧的海滩上。 |
| 13:30 | 离开海滩回到小屋。 |
| 15:00 | 离开小屋，站在沙滩入口北侧的桥上。 |
| 18:00 | 离开桥，回家休息。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 煤矿森林 位于 莉亚的农舍 南部的地方。 |
| 18:00 | 离开森林，回家休息。 |
| 19:40 | 到家，上床睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 全天 | 呆在 家 中。 |

###### 星期四 星期五（任何玩家与艾利欧特的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 皮埃尔的杂货店 。 |
| 17:30 | 离开皮埃尔的店，回家休息。 |

###### 星期五、星期天（玩家与 莉亚 的友谊低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:00 | 离开家，站在鱼店旁边的船坞上。 |
| 17:00 | 离开船坞，前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧，回家休息。 |

###### 星期五、星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 12:00 | 离开家，站在小屋南侧的海滩上。 |
| 13:30 | 离开海滩回到小屋。 |
| 15:00 | 离开小屋，站在沙滩入口北侧的桥上。 |
| 18:00 | 离开桥，回家休息。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 博物馆 。 |
| 17:30 | 离开博物馆，回家休息。 |
| 18:40 | 回到家，站在他的盆景树旁。 |
| 21:00 | 离开他的盆景树，走到他的写字台前。 |

##### 冬季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 全天 | 呆在 家 中。 |

###### 冬季17日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 博物馆 。 |
| 16:50 | 离开博物馆，参加 夜市 。 |
| 01:00 | 离开夜市，回家休息。 |

###### 冬季12日和13日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开家，站在 鱼店 旁边的船坞上。 |
| 17:00 | 离开船坞，前往 星之果实酒吧 。 |
| 00:00 | 离开酒吧，回家休息。 |

###### 星期四 星期五（任何玩家与艾利欧特的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 皮埃尔的杂货店 。 |
| 17:30 | 离开皮埃尔的店，回家休息。 |

###### 星期五、星期天（玩家与 莉亚 的友谊低于6心）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:00 | 离开家，站在鱼店旁边的船坞上。 |
| 17:00 | 离开船坞，前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧，回家休息。 |

###### 星期五、星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 12:00 | 离开家，站在小屋南侧的海滩上。 |
| 13:30 | 离开海滩回到小屋。 |
| 15:00 | 离开小屋，站在沙滩入口北侧的桥上。 |
| 18:00 | 离开桥，回家休息。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于 家 中。 |
| 11:30 | 离开家，前往 博物馆 。 |
| 17:30 | 离开博物馆，回家休息。 |

##### 婚后

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农场参加 沙漠节 ，站在悬崖上俯瞰 绿洲 。 |
| 00:30 | 离开沙漠，返回农场。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开 农舍 ，前往海滩。 |
| 17:00 | 离开海滩，返回农场。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、27 个条件分支、85 行。

- After the Beach Resort on Ginger Island is unlocked, Elliott may randomly spend the day there. After leaving the Island at 6pm, Elliott will immediately go home to bed. Elliott never visits the Resort on Festival days or his checkup day at Harvey's Clinic .
- Below are Elliott's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:00 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:40 AM | Stands at the cliffside south of the racing line. |
| 1:40 AM | Boards bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| All day | Inside his house . |

###### Thursday Friday (Any player has at least 6 hearts with Elliott)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home and heads to Pierre's General Store . |
| 5:30 PM | Leaves Pierre's and heads home for the night. |

###### Friday and Sunday (No player has 6 hearts with Leah)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:00 AM | Leaves his cabin to stand on the docks next to Willy's house . |
| 5:00 PM | Leaves the docks to visit The Stardrop Saloon . |
| 11:40 PM | Leaves the saloon to return home for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 12:00 PM | Leaves his cabin to stand on the beach south of his house. |
| 1:30 PM | Leaves the beach and returns to his cabin. |
| 3:00 PM | Leaves his cabin to stand on the bridge just north of the beach. |
| 6:00 PM | Leaves the bridge to return home for the night. |

##### Summer

###### Summer 9

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Leaves his house and goes to the Clinic . |
| 1:30 PM | Moves from waiting room to examination room inside Clinic. |
| 4:00 PM | Leaves the clinic and returns home for the night. |

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the Saloon . |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| All day | Inside his house . |

###### Thursday Friday (Any player has at least 6 hearts with Elliott)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home and heads to Pierre's General Store . |
| 5:30 PM | Leaves Pierre's and heads home for the night. |

###### Friday and Sunday (No player has 6 hearts with Leah)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:00 AM | Leaves his cabin to stand on the docks next to Willy's house . |
| 5:00 PM | Leaves the docks to visit The Stardrop Saloon . |
| 11:40 PM | Leaves the saloon to return home for the night. |

###### Friday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 12:00 PM | Leaves his cabin to stand on the beach south of his house. |
| 1:30 PM | Leaves the beach and returns to his cabin. |
| 3:00 PM | Leaves his cabin to stand on the bridge just north of the beach. |
| 6:00 PM | Leaves the bridge to return home for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home , heads to the forest south of Leah's Cottage . |
| 6:00 PM | Leaves the forest to return home for the night. |
| 7:40 PM | Arrives home and goes to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| All day | Inside his house . |

###### Thursday Friday (Any player has at least 6 hearts with Elliott)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home and heads to Pierre's General Store . |
| 5:30 PM | Leaves Pierre's and heads home for the night. |

###### Friday and Sunday (No player has 6 hearts with Leah)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:00 AM | Leaves his cabin to stand on the docks next to Willy's house . |
| 5:00 PM | Leaves the docks to visit The Stardrop Saloon . |
| 11:40 PM | Leaves the saloon to return home for the night. |

###### Friday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 12:00 PM | Leaves his cabin to stand on the beach south of his house. |
| 1:30 PM | Leaves the beach and returns to his cabin. |
| 3:00 PM | Leaves his cabin to stand on the bridge just north of the beach. |
| 6:00 PM | Leaves the bridge to return home for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home , heads to the Library . |
| 5:30 PM | Leaves the library to return home for the night. |
| 6:40 PM | Returns home and stands by his bonsai tree. |
| 9:00 PM | Leaves his bonsai tree and walks over to his writing desk. |

##### Winter

###### Rain

| 时间 | 地点/行动 |
|------|------|
| All day | Inside his house . |

###### Winter 17

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home , heads to the Museum . |
| 4:50 PM | Leaves the library to attend the Night Market . |
| 1:00 AM | Leaves the Night Market and returns to his cabin. |

###### Winter 12 and 13

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves his cabin to stand on the docks next to Willy's house . |
| 5:00 PM | Leaves the docks to visit The Stardrop Saloon . |
| 12:00 AM | Leaves the saloon to return home for the night. |

###### Thursday Friday (Any player has at least 6 hearts with Elliott)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home and heads to Pierre's General Store . |
| 5:30 PM | Leaves Pierre's and heads home for the night. |

###### Friday and Sunday (No player has 6 hearts with Leah)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:00 AM | Leaves his cabin to stand on the docks next to Willy's house . |
| 5:00 PM | Leaves the docks to visit The Stardrop Saloon . |
| 11:40 PM | Leaves the saloon to return home for the night. |

###### Friday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 12:00 PM | Leaves his cabin to stand on the beach south of his house. |
| 1:30 PM | Leaves the beach and returns to his cabin. |
| 3:00 PM | Leaves his cabin to stand on the bridge just north of the beach. |
| 6:00 PM | Leaves the bridge to return home for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home . |
| 11:30 AM | Leaves home , heads to the Library . |
| 5:30 PM | Leaves the library to return home for the night. |

##### Marriage

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to attend the Desert Festival and stand on the cliff overlooking the Oasis. |
| 12:30 AM | Leaves the Desert Festival and heads home to the farm. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves the Farmhouse and heads to the beach. |
| 5:00 PM | Leaves the beach and heads home to the farm. |

<a id="npc-schedule-harvey"></a>

### 03. 哈维（Harvey）

> 来源：中文 revision 54980；英文 revision 193951
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个分区、27 个条件分支、118 行。

- 哈维在每个星期二和星期四都会为村民做定期体检。在大多数其他日子里，他早上会在诊所前台值班，下午则在小镇里活动。
- 在雨天，无论诊所中是否有病人，哈维都会在12:12离开诊所柜台，上楼到自己房间去。一段时间后，他会前往 星之果实酒吧 。
- 在姜岛的 海滩度假村 解锁后，哈维可能会前往姜岛。18:00离开姜岛后，哈维会立刻回家睡觉。哈维不会在周二、周四或 节日 当天前往姜岛。
- 下面显示的是哈维的行程表，从上到下优先级逐次下降，比如下雨时行程安排的优先级就会比它下面的高。如果是一个下雨的星期五，那么哈维会按照下雨时的行程表行动。

##### 春季

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季15日、16日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 08:40 | 站在医疗站帐篷前。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里。 |
| 08:40 | 在诊所前台工作。 |
| 12:00 | 上楼回到自己的房间，坐在收音机旁边。 |
| 16:00 | 走到书架旁边看书。 |
| 17:30 | 出门前往 星之果实酒吧 。 |
| 22:00 | 回家睡觉。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:30 | 在 诊所 的检查室中。 |
| 12:50 | 走到候诊室中。 |
| 13:30 | 返回检查室。 |
| 16:30 | 在诊所前台工作。 |
| 18:00 | 上楼回到自己的房间，站在书架旁边。 |
| 23:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 出门前往 皮埃尔的杂货店 。 |
| 15:00 | 返回自己在诊所里的房间。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 出门前往 博物馆 。 |
| 15:00 | 离开博物馆，返回自己在诊所里的房间。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 出门，前往小镇广场左边的公园。 |
| 17:30 | 返回诊所，站在前台旁边。 |
| 18:40 | 上楼回到自己的房间，站在书架旁边。 |
| 22:00 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里。 |
| 08:40 | 在诊所前台工作。 |
| 12:00 | 上楼回到自己的房间，坐在收音机旁边。 |
| 16:00 | 走到书架旁边看书。 |
| 17:30 | 出门前往 星之果实酒吧 。 |
| 22:00 | 回家睡觉。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:30 | 在 诊所 的检查室中。 |
| 12:50 | 走到候诊室中。 |
| 13:30 | 返回检查室。 |
| 16:30 | 在诊所前台工作。 |
| 18:00 | 上楼回到自己的房间，站在书架旁边。 |
| 23:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 出门前往 皮埃尔的杂货店 。 |
| 15:00 | 返回自己在诊所里的房间。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 出门前往 博物馆 。 |
| 15:00 | 离开博物馆，返回自己在诊所里的房间。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 前往 社区中心 的西侧，喷泉的南侧。 |
| 17:30 | 返回诊所，站在前台旁边。 |
| 18:40 | 上楼回到自己的房间，站在书架旁边。 |
| 22:00 | 上床睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里。 |
| 08:40 | 在诊所前台工作。 |
| 12:00 | 上楼回到自己的房间，坐在收音机旁边。 |
| 16:00 | 走到书架旁边看书。 |
| 17:30 | 出门前往 星之果实酒吧 。 |
| 22:00 | 回家睡觉。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:30 | 在 诊所 的检查室中。 |
| 12:50 | 走到候诊室中。 |
| 13:30 | 返回检查室。 |
| 16:30 | 在诊所前台工作。 |
| 18:00 | 上楼回到自己的房间，站在书架旁边。 |
| 23:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 出门前往 皮埃尔的杂货店 。 |
| 15:00 | 返回自己在诊所里的房间。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 出门前往 博物馆 。 |
| 15:00 | 离开博物馆，返回自己在诊所里的房间。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 出门，站在一颗树旁，位于通往 沙滩 的桥的西侧。 |
| 17:00 | 返回自己的房间，坐在收音机旁边。 |
| 22:00 | 上床睡觉。 |

##### 冬季

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 站在他房间内的微波炉旁边。 |
| 08:40 | 在诊所前台工作。 |
| 12:00 | 上楼回到自己的房间，坐在收音机旁边。 |
| 16:00 | 走到房间内的书架旁边。 |
| 17:00 | 出门去沙滩参加 夜市 。 |
| 00:00 | 回家睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里。 |
| 08:40 | 在诊所前台工作。 |
| 12:00 | 上楼回到自己的房间，坐在收音机旁边。 |
| 16:00 | 走到书架旁边看书。 |
| 17:30 | 出门前往 星之果实酒吧 。 |
| 22:00 | 回家睡觉。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:30 | 在 诊所 的检查室中。 |
| 12:50 | 走到候诊室中。 |
| 13:30 | 返回检查室。 |
| 16:30 | 在诊所前台工作。 |
| 18:00 | 上楼回到自己的房间，站在书架旁边。 |
| 23:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 站在他房间内的冰箱旁边。 |
| 08:30 | 在诊所前台工作。 |
| 12:00 | 出门前往 皮埃尔的杂货店 。 |
| 15:00 | 返回自己在诊所里的房间。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 出门前往 博物馆 。 |
| 15:00 | 离开博物馆，返回自己在诊所里的房间。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于他的房间。 |
| 08:40 | 在诊所前台工作。 |
| 12:00 | 上楼回到自己的房间，坐在收音机旁边。 |
| 16:00 | 走到房间内的书架旁边看书。 |
| 17:50 | 出门前往 星之果实酒吧 。 |
| 22:00 | 回家睡觉。 |

##### 婚后

###### 春季15日、16日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开农场，前往 沙漠 。 |
| 09:40 | 站在医疗站帐篷前。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农场，前往 皮埃尔的杂货店 。 |
| 12:00 | 前往 社区中心 左侧的喷泉。 |
| 17:00 | 返回农场。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 离开农场，前往诊所。 |
| 18:00 | 离开诊所，返回农场。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、27 个条件分支、118 行。

- On Tuesdays and Thursdays Harvey gives villagers their annual or quarterly checkups. On most other days he spends the morning manning the counter at the clinic, and the afternoon taking exercise around town.
- On rainy days, Harvey leaves the clinic and walks upstairs to his room at 12pm, regardless of whether or not there are patients in the clinic. Later, he stops by the Stardrop Saloon .
- After the Beach Resort on Ginger Island is unlocked, Harvey may randomly spend the day there. After leaving the Island at 6pm, Harvey will immediately go home to bed. Harvey never visits the Resort on Tuesdays, Thursdays, or Festival days.
- Shown below are Harvey's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Spring 15, 16 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 7:20 AM | Boards bus to Calico Desert to attend the Desert Festival . |
| 8:40 AM | Stands at the medical tent. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room. |
| 8:40 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes upstairs to his room, sits in front of radio. |
| 4:00 PM | Moves to bookshelf to read. |
| 5:30 PM | Heads to the Stardrop Saloon . |
| 10:00 PM | Returns home and goes to bed. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:30 AM | In exam room of clinic . |
| 12:50 PM | Moves to waiting room. |
| 1:30 PM | Returns to exam room. |
| 4:30 PM | Works at the clinic's front desk. |
| 6:00 PM | Goes up to his room, stands in front of bookshelf. |
| 11:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes to Pierre's General Store . |
| 3:00 PM | Returns to his room above the clinic. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to go to the Museum . |
| 3:00 PM | Leaves the Museum to return to his room above the clinic. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Walks around the park west of the town square. |
| 5:30 PM | Returns to clinic, stands at right side of front desk. |
| 6:40 PM | Goes upstairs to his room, reads in front of bookshelf. |
| 10:00 PM | Goes to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | At the Stardrop Saloon . |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room. |
| 8:40 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes upstairs to his room, sits in front of radio. |
| 4:00 PM | Moves to bookshelf to read. |
| 5:30 PM | Heads to the Stardrop Saloon . |
| 10:00 PM | Returns home and goes to bed. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:30 AM | In exam room of clinic . |
| 12:50 PM | Moves to waiting room. |
| 1:30 PM | Returns to exam room. |
| 4:30 PM | Works at the clinic's front desk. |
| 6:00 PM | Goes upstairs to his room, reads in front of bookshelf. |
| 11:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes to Pierre's General Store . |
| 3:00 PM | Returns to his room above the clinic. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to go to the Museum . |
| 3:00 PM | Leaves the Museum to return to his room above the clinic. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Walks south of fountain west of the Community Center . |
| 5:30 PM | Returns to clinic, stands at right side of front desk. |
| 6:40 PM | Goes up to his room, reads in front of bookshelf. |
| 10:00 PM | Goes to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room. |
| 8:40 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes upstairs to his room, sits in front of radio. |
| 4:00 PM | Moves to bookshelf to read. |
| 5:30 PM | Heads to the Stardrop Saloon . |
| 10:00 PM | Returns home and goes to bed. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:30 AM | In exam room of clinic . |
| 12:50 PM | Moves to waiting room. |
| 1:30 PM | Returns to exam room. |
| 4:30 PM | Works at the clinic's front desk. |
| 6:00 PM | Goes upstairs to his room, reads in front of bookshelf. |
| 11:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes to Pierre's General Store . |
| 3:00 PM | Returns to his room above the clinic. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to go to the Museum . |
| 3:00 PM | Leaves the Museum to return to his room above the clinic. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Walks into town, stands by tree west of bridge to the Beach . |
| 5:00 PM | Returns to his room, sits in front of radio. |
| 10:00 PM | Goes to bed. |

##### Winter

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in front of microwave in his room. |
| 8:40 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes upstairs to his room, sits in front of radio. |
| 4:00 PM | Moves to bookshelf in his room. |
| 5:00 PM | Walks to beach to attend Night Market . |
| 12:00 AM | Returns home and goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room. |
| 8:40 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes upstairs to his room, sits in front of radio. |
| 4:00 PM | Moves to bookshelf to read. |
| 5:30 PM | Heads to the Stardrop Saloon . |
| 10:00 PM | Returns home and goes to bed. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:30 AM | In exam room of clinic . |
| 12:50 PM | Moves to waiting room. |
| 1:30 PM | Returns to exam room. |
| 4:30 PM | Works at the clinic's front desk. |
| 6:00 PM | Goes upstairs to his room, reads in front of bookshelf. |
| 11:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Stands in front of refrigerator in his room. |
| 8:30 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes to Pierre's General Store . |
| 3:00 PM | Returns to his room above the clinic. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to go to the Museum . |
| 3:00 PM | Leaves the Museum to return to his room above the clinic. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room. |
| 8:40 AM | Works at the clinic's front desk. |
| 12:00 PM | Goes upstairs to his room, sits in front of radio. |
| 4:00 PM | Moves to bookshelf to read. |
| 5:50 PM | Heads to the Stardrop Saloon . |
| 10:00 PM | Returns home and goes to bed. |

##### Marriage

###### Spring 15, 16 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves the farmhouse and heads to the Desert Festival . |
| 9:40 AM | Stands at the medical tent. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves the farmhouse and heads to Pierre's General Store . |
| 12:00 PM | Walks to fountain left of Community Center . |
| 5:00 PM | Leaves town and heads home to the farm. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | Leaves the farmhouse and heads to the clinic. |
| 6:00 PM | Leaves the clinic to return home to the farm. |

<a id="npc-schedule-sam"></a>

### 04. 山姆（Sam）

> 来源：中文 revision 55076；英文 revision 193676
>
> 结构判定：中英文结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个分区、37 个条件分支、187 行。

- 山姆经常在 他的卧室 中练习吉他。他也经常在家门口玩掌机游戏，或练习滑板。周末他会在 星之果实酒吧 打台球。当下雨时他会整天待在家里，或者在 星之果实酒吧 待上几个小时。 春季 时他经常去星之果实酒吧， 秋季 常去小镇西边的 煤矿森林 ， 夏季 则会去 沙滩 。每年秋季11日，山姆都会去 哈维的诊所 进行体检。
- 当 Joja超市 还在营业时，山姆每周一和周三会去做兼职。玩家完成 社区中心 的 收集包 后， Joja超市 倒闭，山姆便改去 博物馆 的古物矿产展示区（在壁炉附近）工作。
- 姜岛海滩度假村 解锁后，山姆可能会前往姜岛。18:00离开姜岛后，山姆会立刻上床睡觉。山姆不会在 节日 当天或他的体检日（秋季11日）前往姜岛。
- 在特殊条件（例如：季节、天气或者日期）下，他的行动可能会有所不同。以下是山姆的日程安排，优先度从高到低排序。（例如：如果当天下雨，雨天的日程安排会覆盖其下方的所有日程安排。）

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:50 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:40 | 站在免费仙人掌处附近的池塘西侧。 |
| 00:50 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季9日和23日（玩家与 潘妮 和山姆的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 他的卧室 里睡觉。 |
| 09:00 | 起床，站在卧室里。 |
| 11:00 | 离开家，站在 冰淇淋摊 附近的桥上。 |
| 16:00 | 走到 柳巷2号 门前的树下，开始玩他的掌机游戏。 |
| 19:00 | 返回 他的卧室 。 |
| 21:30 | 上床睡觉。 |

###### 春季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 醒来，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:40 | 离开家，站在位于 刘易斯 家附近的河边。 |
| 18:30 | 回家。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在他卧室的柜子前面。 |
| 11:00 | 在 他的卧室 里弹吉他。 |
| 15:00 | 在厨房玩掌机游戏。 |
| 17:00 | 返回他的房间，站在柜子前面。 |
| 18:30 | 站在他卧室的桌子前面。 |
| 20:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 11:00 | 在他家里走动。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 19:40 | 离开 星之果实酒吧 ，回家睡觉。 |

###### 星期一、星期三

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在 他的卧室 的中间。 |
| 11:00 | 离开家，前往 Joja超市 。（若社区中心已修复则为 博物馆 ） |
| 12:50 | 到达 Joja超市 （若社区中心已修复则为 博物馆 ）开始工作。 |
| 16:00 | 完成工作，回家。 |
| 18:00 | 到家，站在书架前面。 |
| 21:30 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里弹吉他。 |
| 11:00 | 离开卧室，在 屋 外玩滑板。 |
| 15:00 | 前往 星之果实酒吧 。 |
| 16:00 | 到达 星之果实酒吧 ，在游乐场打台球。 |
| 21:20 | 离开星之果实酒吧，回家。 |
| 22:20 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:40 | 离开家，站在位于 刘易斯 家附近的河边。 |
| 18:30 | 回家。 |
| 21:00 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于客厅。 |

###### 夏季9日和23日（玩家与 潘妮 和山姆的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 他的卧室 里睡觉。 |
| 09:00 | 起床，站在卧室里。 |
| 11:00 | 离开家，站在 冰淇淋摊 附近的桥上。 |
| 16:00 | 走到 柳巷2号 门前的树下，开始玩他的掌机游戏。 |
| 19:00 | 返回 他的卧室 。 |
| 21:30 | 上床睡觉。 |

###### 夏季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 醒来，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:40 | 离开家，站在位于 刘易斯 家附近的河边。 |
| 18:30 | 回家。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在他卧室的柜子前面。 |
| 11:00 | 在 他的卧室 里弹吉他。 |
| 15:00 | 在厨房玩掌机游戏。 |
| 17:00 | 返回他的房间，站在柜子前面。 |
| 18:30 | 站在他卧室的桌子前面。 |
| 20:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 11:00 | 在他家里走动。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 19:40 | 离开 星之果实酒吧 ，回家睡觉。 |

###### 星期一、星期三

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在 他的卧室 的中间。 |
| 11:00 | 离开家，前往 Joja超市 。（若社区中心已修复则为 博物馆 ） |
| 12:50 | 到达 Joja超市 （若社区中心已修复则为 博物馆 ）开始工作。 |
| 16:00 | 完成工作，回家。 |
| 18:00 | 到家，站在书架前面。 |
| 21:30 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里弹吉他。 |
| 11:00 | 离开卧室，在 屋 外玩滑板。 |
| 15:00 | 前往 星之果实酒吧 。 |
| 16:00 | 到达 星之果实酒吧 ，在游乐场打台球。 |
| 21:20 | 离开星之果实酒吧，回家。 |
| 22:20 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 11:00 | 在 他的卧室 里弹吉他。 |
| 13:40 | 离开家，前往 沙滩 ，和弟弟 文森特 一起待在火堆旁。 |
| 19:00 | 回家。 |
| 21:00 | 上床睡觉。 |

##### 秋季

###### 秋季11日

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 在 他的卧室 里醒来。 |
| 11:30 | 前往 哈维的诊所 进行每年例行的身体健康检查，在候诊室玩掌机游戏。 |
| 13:30 | 在诊所接受检查。 |
| 16:00 | 离开诊所，前往 镇上 。 |
| 21:00 | 回家睡觉。 |

###### 秋季9日和23日（玩家与 潘妮 和山姆的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 他的卧室 里睡觉。 |
| 09:00 | 起床，站在卧室里。 |
| 11:00 | 离开家，站在 冰淇淋摊 附近的桥上。 |
| 16:00 | 走到 柳巷2号 门前的树下，开始玩他的掌机游戏。 |
| 19:00 | 返回 他的卧室 。 |
| 21:30 | 上床睡觉。 |

###### 秋季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 醒来，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:40 | 离开家，站在位于 刘易斯 家附近的河边。 |
| 18:30 | 回家。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在他卧室的柜子前面。 |
| 11:00 | 在 他的卧室 里弹吉他。 |
| 15:00 | 在厨房玩掌机游戏。 |
| 17:00 | 返回他的房间，站在柜子前面。 |
| 18:30 | 站在他卧室的桌子前面。 |
| 20:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 11:00 | 在他家里走动。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 19:40 | 离开 星之果实酒吧 ，回家睡觉。 |

###### 星期一、星期三

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在 他的卧室 的中间。 |
| 11:00 | 离开家，前往 Joja超市 。（若社区中心已修复则为 博物馆 ） |
| 12:50 | 到达 Joja超市 （若社区中心已修复则为 博物馆 ）开始工作。 |
| 16:00 | 完成工作，回家。 |
| 18:00 | 到家，站在书架前面。 |
| 21:30 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里弹吉他。 |
| 11:00 | 离开卧室，在 屋 外玩滑板。 |
| 15:00 | 前往 星之果实酒吧 。 |
| 16:00 | 到达 星之果实酒吧 ，在游乐场打台球。 |
| 21:20 | 离开星之果实酒吧，回家。 |
| 22:20 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:20 | 离开家，前往 煤矿森林 ，位于 莉亚的农舍 的西南方。 |
| 19:00 | 回家。 |
| 21:00 | 上床睡觉。 |

##### 冬季

###### 冬季17日

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 17:00 | 参加 夜市 。 |
| 00:00 | 回家睡觉。 |

###### 冬季9日和23日（玩家与 潘妮 和山姆的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 他的卧室 里睡觉。 |
| 09:00 | 起床，站在卧室里。 |
| 11:00 | 离开家，站在 冰淇淋摊 附近的桥上。 |
| 16:00 | 走到 柳巷2号 门前的树下，开始玩他的掌机游戏。 |
| 19:00 | 返回 他的卧室 。 |
| 21:30 | 上床睡觉。 |

###### 冬季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 醒来，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:40 | 离开家，站在位于 刘易斯 家附近的河边。 |
| 18:30 | 回家。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在他卧室的柜子前面。 |
| 11:00 | 在 他的卧室 里弹吉他。 |
| 15:00 | 在厨房玩掌机游戏。 |
| 17:00 | 返回他的房间，站在柜子前面。 |
| 18:30 | 站在他卧室的桌子前面。 |
| 20:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 11:00 | 在他家里走动。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 19:40 | 离开 星之果实酒吧 ，回家睡觉。 |

###### 星期一、星期三

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，站在 他的卧室 的中间。 |
| 11:00 | 离开家，前往 Joja超市 。（若社区中心已修复则为 博物馆 ） |
| 12:50 | 到达 Joja超市 （若社区中心已修复则为 博物馆 ）开始工作。 |
| 16:00 | 完成工作，回家。 |
| 18:00 | 到家，站在书架前面。 |
| 21:30 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里弹吉他。 |
| 11:00 | 离开卧室，在 屋 外玩滑板。 |
| 15:00 | 前往 星之果实酒吧 。 |
| 16:00 | 到达 星之果实酒吧 ，在游乐场打台球。 |
| 21:20 | 离开星之果实酒吧，回家。 |
| 22:20 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，在 他的卧室 里走动。 |
| 10:40 | 在 他的卧室 里弹吉他。 |
| 13:20 | 离开家，前往 星之果实酒吧 。 |
| 19:00 | 回家。 |
| 21:00 | 上床睡觉。 |

##### 婚后

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 前往 柳巷1号 的客厅。 |

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:20 | 参加 沙漠节 ，站在免费仙人掌处附近的池塘西侧。 |
| 01:00 | 回家。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 08:00 | 离开农场前往 鹈鹕镇 。 |
| 09:30 | 到达 柳巷1号 ，站在厨房。 |
| 11:00 | 走到客厅。 |
| 15:00 | 离开 柳巷1号 ，返回农场。 |
| 16:00 | 到达农场农舍。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 08:00 | 离开农场前往 鹈鹕镇 。 |
| 09:30 | 到达 柳巷1号 ，站在厨房。 |
| 11:00 | 离开 柳巷1号 。 |
| 11:50 | 在 星之果实酒吧 门前的长椅旁玩滑板。 |
| 15:00 | 前往 星之果实酒吧 。 |
| 15:30 | 在 星之果实酒吧 打台球。 |
| 21:00 | 离开酒吧，返回农场。 |
| 23:00 | 到达农舍。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、41 个条件分支、211 行。

- Sam can often be found practicing his guitar in his bedroom , sometimes with Sebastian playing an electric piano. He's also frequently seen outside of his house playing a handheld video game, or attempting skateboard tricks. On weekends he can be found playing pool at the Stardrop Saloon .
- He works part-time on Monday and Wednesday at JojaMart (if it is in business), or at the Museum in the Artifacts and Minerals display (if the Community Center has been restored). He frequents the Stardrop Saloon during spring , goes to the Beach during summer , and visits the woods west of town in the fall .
- When it's raining he'll often stay home all day, or visit the Stardrop Saloon for a few hours.
- On the 11th of Fall, he has an appointment at the clinic .
- His schedule can deviate if there are specific conditions like season, weather or certain days of the week.
- After the Beach Resort on Ginger Island is unlocked, Sam may randomly spend the day there. After leaving the Island at 6pm, Sam will immediately go home to bed. Sam never visits the Resort on Festival days or his checkup day at Harvey's Clinic .
- Below are his schedule deviations prioritized highest to lowest (for example when it rains that schedule will override all others below it)

##### Spring

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:50 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:40 AM | Stands west of the pond near the cactus stand. |
| 12:50 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes bus back to the Valley. |

###### Spring 9 and 23 (No player has 6 hearts with Penny or Sam)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in his bed at his home . |
| 9:00 AM | Wakes up and stands in his bedroom. |
| 11:00 AM | Walks into town , stands on the bridge near the Ice Cream Stand . |
| 4:00 PM | Walk to the pink tree in front of 2 Willow Lane , plays his handheld video game. |
| 7:00 PM | Returns home from town . |
| 9:30 PM | Goes into his bedroom to go to bed. |

###### Spring 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:40 PM | Leaves his bedroom , walks into town , and stands near Lewis ' house by the river. |
| 6:30 PM | Returns home from town . |
| 9:00 PM | Goes into his bedroom to go to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, stands in front of the dresser in his room . |
| 11:00 AM | Plays guitar inside his room . |
| 3:00 PM | Plays his handheld video game in the kitchen inside his house . |
| 5:00 PM | Returns to his bedroom . and stands in front of his dresser. |
| 6:30 PM | At his desk inside his bedroom . |
| 8:00 PM | Goes to go to bed . |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 11:00 AM | Moves around inside his home . |
| 2:00 PM | Leaves his bedroom and walks to The Stardrop Saloon . "Nothing like an ice cold Joja Cola on a sopping wet day, huh? Just kidding. Hehehe." |
| 7:40 PM | Leaves The Stardrop Saloon and returns to his bedroom to go to bed. |

###### Monday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and stands in the middle of his bedroom . |
| 11:00 AM | Leaves his bedroom and walks to JojaMart (or Museum if Community Center is restored). |
| 12:50 PM | Arrives at JojaMart (or Museum if Community Center is restored) and starts work. |
| 4:00 PM | Finshes work at JojaMart (or Museum if Community Center is restored) and walks home . |
| 6:00 PM | Arrives in his bedroom and stands in front of his bookshelf. |
| 9:30 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and plays guitar inside his bedroom . |
| 11:00 AM | Leaves his bedroom and skateboards outside of his house . |
| 3:00 PM | Walks to the Stardrop Saloon . |
| 4:00 PM | Arrives at the Stardrop Saloon and plays pool near the arcade. |
| 9:20 PM | Leaves the Stardrop Saloon and walks home . |
| 10:20 PM | Arrives at home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Wakes up for the day inside his bedroom and walks just outside to stand by the river in front of Haley and Emily's house . |
| 11:00 AM | Walks to a nearby bush and plays his handheld video game in town . |
| 12:30 PM | Leaves town , goes to his bedroom with Sebastian to practice guitar. |
| 3:00 PM | Hangs out in his room with Sebastian . |
| 6:00 PM | Leaves his home to walk to the river in front of his house with Sebastian . |
| 7:40 PM | Returns to his bedroom to go to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:40 PM | Leaves his bedroom , walks into town , and stands near Lewis ' house by the river. |
| 6:30 PM | Returns home from town . |
| 9:00 PM | Goes into his bedroom to go to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the living room. |

###### Summer 9 and 23 (No player has 6 hearts with Penny or Sam)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in his bed at his home . |
| 9:00 AM | Wakes up and stands in his bedroom. |
| 11:00 AM | Walks into town , stands on the bridge near the Ice Cream Stand . |
| 4:00 PM | Walk to the pink tree in front of 2 Willow Lane , plays his handheld video game. |
| 7:00 PM | Returns home from town . |
| 9:30 PM | Goes into his bedroom to go to bed. |

###### Summer 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:40 PM | Leaves his bedroom , walks into town , and stands near Lewis ' house by the river. |
| 6:30 PM | Returns home from town . |
| 9:00 PM | Goes into his bedroom to go to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, stands in front of the dresser in his room . |
| 11:00 AM | Plays guitar inside his room . |
| 3:00 PM | Plays his handheld video game in the kitchen inside his house . |
| 5:00 PM | Returns to his bedroom . and stands in front of his dresser. |
| 6:30 PM | At his desk inside his bedroom . |
| 8:00 PM | Goes to go to bed . |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 11:00 AM | Moves around inside his home . |
| 2:00 PM | Leaves his bedroom and walks to The Stardrop Saloon . "Nothing like an ice cold Joja Cola on a sopping wet day, huh? Just kidding. Hehehe." |
| 7:40 PM | Leaves The Stardrop Saloon and returns to his bedroom to go to bed. |

###### Monday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and stands in the middle of his bedroom . |
| 11:00 AM | Leaves his bedroom and walks to JojaMart (or Museum if Community Center is restored). |
| 12:50 PM | Arrives at JojaMart (or Museum if Community Center is restored) and starts work. |
| 4:00 PM | Finshes work at JojaMart (or Museum if Community Center is restored) and walks home . |
| 6:00 PM | Arrives in his bedroom and stands in front of his bookshelf. |
| 9:30 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and plays guitar inside his bedroom . |
| 11:00 AM | Leaves his bedroom and skateboards outside of his house . |
| 3:00 PM | Walks to the Stardrop Saloon . |
| 4:00 PM | Arrives at the Stardrop Saloon and plays pool near the arcade. |
| 9:20 PM | Leaves the Stardrop Saloon and walks home . |
| 10:20 PM | Arrives at home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Wakes up for the day inside his bedroom and walks just outside to stand by the river in front of Haley and Emily's house . |
| 11:00 AM | Walks to a nearby bush and plays his handheld video game in town . |
| 12:30 PM | Leaves town , goes to his bedroom with Sebastian to practice guitar. |
| 3:00 PM | Hangs out in his room with Sebastian . |
| 6:00 PM | Leaves his home to walk to the river in front of his house with Sebastian . |
| 7:40 PM | Returns to his bedroom to go to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 11:00 AM | Plays guitar inside his bedroom . |
| 1:40 PM | Leaves his bedroom and walks to the beach by the firepit with his brother Vincent . |
| 7:00 PM | Returns home from the beach . |
| 9:00 PM | Goes into his bedroom to go to bed. |

##### Fall

###### Fall 11

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day inside his bedroom . "I gotta go visit Uncle Doctor today... Great." |
| 11:30 AM | Walks to the clinic for his annual checkup, plays his handheld video game in the waiting room. |
| 1:30 PM | Gets medical checkup at the clinic . "I'm a healthy boy, doc. Can I go now? This is boring." |
| 4:00 PM | Leaves the clinic to walk into town . "I just got out of the doctor's office. Completely healthy and vigorous, just as I expected." |
| 9:00 PM | Returns to his bedroom to go to bed. |

###### Fall 9 and 23 (No player has 6 hearts with Penny or Sam)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in his bed at his home . |
| 9:00 AM | Wakes up and stands in his bedroom. |
| 11:00 AM | Walks into town , stands on the bridge near the Ice Cream Stand . |
| 4:00 PM | Walk to the pink tree in front of 2 Willow Lane , plays his handheld video game. |
| 7:00 PM | Returns home from town . |
| 9:30 PM | Goes into his bedroom to go to bed. |

###### Fall 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:40 PM | Leaves his bedroom , walks into town , and stands near Lewis ' house by the river. |
| 6:30 PM | Returns home from town . |
| 9:00 PM | Goes into his bedroom to go to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, stands in front of the dresser in his room . |
| 11:00 AM | Plays guitar inside his room . |
| 3:00 PM | Plays his handheld video game in the kitchen inside his house . |
| 5:00 PM | Returns to his bedroom . and stands in front of his dresser. |
| 6:30 PM | At his desk inside his bedroom . |
| 8:00 PM | Goes to go to bed . |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 11:00 AM | Moves around inside his home . |
| 2:00 PM | Leaves his bedroom and walks to The Stardrop Saloon . "Nothing like an ice cold Joja Cola on a sopping wet day, huh? Just kidding. Hehehe." |
| 7:40 PM | Leaves The Stardrop Saloon and returns to his bedroom to go to bed. |

###### Monday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and stands in the middle of his bedroom . |
| 11:00 AM | Leaves his bedroom and walks to JojaMart (or Museum if Community Center is restored). |
| 12:50 PM | Arrives at JojaMart (or Museum if Community Center is restored) and starts work. |
| 4:00 PM | Finshes work at JojaMart (or Museum if Community Center is restored) and walks home . |
| 6:00 PM | Arrives in his bedroom and stands in front of his bookshelf. |
| 9:30 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and plays guitar inside his bedroom . |
| 11:00 AM | Leaves his bedroom and skateboards outside of his house . |
| 3:00 PM | Walks to the Stardrop Saloon . |
| 4:00 PM | Arrives at the Stardrop Saloon and plays pool near the arcade. |
| 9:20 PM | Leaves the Stardrop Saloon and walks home . |
| 10:20 PM | Arrives at home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Wakes up for the day inside his bedroom and walks just outside to stand by the river in front of Haley and Emily's house . |
| 11:00 AM | Walks to a nearby bush and plays his handheld video game in town . |
| 12:30 PM | Leaves town , goes to his bedroom with Sebastian to practice guitar. |
| 3:00 PM | Hangs out in his room with Sebastian . |
| 6:00 PM | Leaves his home to walk to the river in front of his house with Sebastian . |
| 7:40 PM | Returns to his bedroom to go to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:20 PM | Leaves his bedroom walks to The Forest southwest of Leah's Cottage . |
| 7:00 PM | Returns home from The Forest . |
| 9:00 PM | Goes into his bedroom to go to bed. |

##### Winter

###### Winter 17

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 5:00 PM | Attends the Night Market . |
| 12:00 AM | Goes into his bedroom to go to bed. |

###### Winter 9 and 23 (No player has 6 hearts with Penny or Sam)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in his bed at his home . |
| 9:00 AM | Wakes up and stands in his bedroom. |
| 11:00 AM | Walks into town , stands on the bridge near the Ice Cream Stand . |
| 4:00 PM | Walk to the pink tree in front of 2 Willow Lane , plays his handheld video game. |
| 7:00 PM | Returns home from town . |
| 9:30 PM | Goes into his bedroom to go to bed. |

###### Winter 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:40 PM | Leaves his bedroom , walks into town , and stands near Lewis ' house by the river. |
| 6:30 PM | Returns home from town . |
| 9:00 PM | Goes into his bedroom to go to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, stands in front of the dresser in his room . |
| 11:00 AM | Plays guitar inside his room . |
| 3:00 PM | Plays his handheld video game in the kitchen inside his house . |
| 5:00 PM | Returns to his bedroom . and stands in front of his dresser. |
| 6:30 PM | At his desk inside his bedroom . |
| 8:00 PM | Goes to go to bed . |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 11:00 AM | Moves around inside his home . |
| 2:00 PM | Leaves his bedroom and walks to The Stardrop Saloon . "Nothing like an ice cold Joja Cola on a sopping wet day, huh? Just kidding. Hehehe." |
| 7:40 PM | Leaves The Stardrop Saloon and returns to his bedroom to go to bed. |

###### Monday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and stands in the middle of his bedroom . |
| 11:00 AM | Leaves his bedroom and walks to JojaMart (or Museum if Community Center is restored). |
| 12:50 PM | Arrives at JojaMart (or Museum if Community Center is restored) and starts work. |
| 4:00 PM | Finshes work at JojaMart (or Museum if Community Center is restored) and walks home . |
| 6:00 PM | Arrives in his bedroom and stands in front of his bookshelf. |
| 9:30 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and plays guitar inside his bedroom . |
| 11:00 AM | Leaves his bedroom and skateboards outside of his house . |
| 3:00 PM | Walks to the Stardrop Saloon . |
| 4:00 PM | Arrives at the Stardrop Saloon and plays pool near the arcade. |
| 9:20 PM | Leaves the Stardrop Saloon and walks home . |
| 10:20 PM | Arrives at home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Wakes up for the day inside his bedroom and walks just outside to stand by the river in front of Haley and Emily's house . |
| 11:00 AM | Walks to a nearby bush and plays his handheld video game in town . |
| 12:30 PM | Leaves town , goes to his bedroom with Sebastian to practice guitar. |
| 3:00 PM | Hangs out in his room with Sebastian . |
| 6:00 PM | Leaves his home to walk to the river in front of his house with Sebastian . |
| 7:40 PM | Returns to his bedroom to go to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up for the day, moves around his room . |
| 10:40 AM | Plays guitar inside his bedroom . |
| 1:20 PM | Leaves his bedroom and walks to the Stardrop Saloon . |
| 7:00 PM | Returns home from the Stardrop Saloon . |
| 9:00 PM | Goes into his bedroom to go to bed. |

##### Marriage

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Walks to his parents' living room. |

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:20 AM | Walks to the Desert Festival and stands west of the pond near the cactus stand. |
| 1:00 AM | Returns home. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 8:00 AM | Leaves home and heads for Pelican Town . |
| 9:30 AM | Arrives at 1 Willow Lane and stands in the kitchen. |
| 11:00 AM | Moves to living room. |
| 3:00 PM | Leaves 1 Willow Lane to return home. |
| 4:00 PM | Arrives at the farmhouse. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 8:00 AM | Leaves home and heads for Pelican Town . |
| 9:30 AM | Arrives at 1 Willow Lane and stands in the kitchen. |
| 11:00 AM | Leaves house. |
| 11:50 AM | Skateboarding south of the Stardrop Saloon, by the benches. |
| 3:00 PM | Heads into the Stardrop Saloon . |
| 3:30 PM | Playing pool in the Stardrop Saloon . |
| 9:00 PM | Leaves the Saloon to return home. |
| 11:00 PM | Arrives at the farmhouse. |

<a id="npc-schedule-sebastian"></a>

### 05. 塞巴斯蒂安（Sebastian）

> 来源：中文 revision 55064；英文 revision 193877
>
> 结构判定：中英文结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个分区、41 个条件分支、260 行。

- 塞巴斯蒂安会在 夏季 4日时前往 哈维的诊所 体检。
- 姜岛 海滩度假村修复后，塞巴斯蒂安偶尔会去度个假，直到18:00离开回 木匠的商店 睡觉，塞巴斯蒂安不会在他体检日和 节日 当天去度假。
- 下面显示的是塞巴斯蒂安的行程表，每个季节（或部分）的行程从上到下优先级逐次下降，比如下雨时行程安排的优先级就会比它下面的高。如果是一个下雨的星期五，那么塞巴斯蒂安会按照下雨时的行程表行动。

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 12:00 | 在火烈鸟周围闲逛。 |
| 01:40 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季11日（玩家与塞巴斯蒂安的友谊低于6心） 春季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:00 | 起床，坐到电脑前。 |
| 12:00 | 在自己房间里，站在沙发旁。 |
| 17:10 | 离开他的房间，前往厨房。 |
| 18:00 | 离开厨房回到自己房间。 |
| 18:20 | 回到房间。 |
| 21:30 | 上床睡觉。 |

###### 春季11日和25日（任何玩家与塞巴斯蒂安的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，出门前往 海滩 。 |
| 13:30 | 站在 鱼店 左边的长码头最南端。 |
| 17:00 | 离开码头，回 家 。 |
| 19:40 | 到家，上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开家，前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，站在街机厅的红沙发旁。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期四（ 铁路 已解锁）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 14:00 | 出门前往 火车站 抽烟。 |
| 15:00 | 在火车站抽烟。 |
| 18:20 | 站在火车站东侧的隧道边上。 |
| 20:10 | 站在火车站西侧的隧道边上。 |
| 21:30 | 回家。 |
| 22:20 | 到家。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 出门前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，和 山姆 一起打台球。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 出门前往 山姆 的家。 |
| 11:30 | 和 山姆 一起站在 海莉和艾米丽的家 门口。 |
| 12:30 | 跟着 山姆 去他家。 |
| 13:00 | 位于 山姆 的房间。 |
| 18:00 | 离开 山姆的家 ，和 山姆 一起去靠近山姆家的河边。 |
| 18:20 | 和山姆站在一起，在 山姆家 门口的河边抽烟。 |
| 19:30 | 回 家 。 |
| 21:40 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房，回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于他的房间。 |

###### 夏季4日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 站在自己房间的书架旁边。 |
| 10:00 | 出门，前往 哈维的诊所 。 |
| 11:50 | 到达诊所，待在候诊室中。 |
| 13:40 | 前往诊所的检查室。 |
| 16:00 | 回 家 。 |
| 18:00 | 到达他的房间，上床睡觉。 |

###### 夏季11日（玩家与塞巴斯蒂安的友谊低于6心） 夏季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:00 | 起床，坐到电脑前。 |
| 12:00 | 在自己房间里，站在沙发旁。 |
| 17:30 | 离开他的房间，前往厨房。 |
| 18:30 | 坐在电脑前。 |
| 21:30 | 上床睡觉。 |

###### 夏季11日和25日（任何玩家与塞巴斯蒂安的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，出门前往 海滩 。 |
| 13:30 | 站在 鱼店 左边的长码头最南端。 |
| 17:00 | 离开码头，回 家 。 |
| 19:40 | 到家，上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开家，前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，站在街机厅的红沙发旁。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期四（ 铁路 已解锁）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 14:00 | 出门前往 火车站 抽烟。 |
| 15:00 | 在火车站抽烟。 |
| 18:20 | 站在火车站东侧的隧道边上。 |
| 20:10 | 站在火车站西侧的隧道边上。 |
| 21:30 | 回家。 |
| 22:20 | 到家。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 出门前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，和 山姆 一起打台球。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 出门前往 山姆 的家。 |
| 11:30 | 和 山姆 一起站在 海莉和艾米丽的家 门口。 |
| 12:30 | 跟着 山姆 去他家。 |
| 13:00 | 位于 山姆 的房间。 |
| 18:00 | 离开 山姆的家 ，和 山姆 一起去靠近山姆家的河边。 |
| 18:20 | 和山姆站在一起，在 山姆家 门口的河边抽烟。 |
| 19:30 | 回 家 。 |
| 21:40 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房，回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

##### 秋季

###### 秋季11日（玩家与塞巴斯蒂安的友谊低于6心） 秋季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:00 | 起床，坐到电脑前。 |
| 12:00 | 在自己房间里，站在沙发旁。 |
| 17:30 | 离开他的房间，前往厨房。 |
| 18:00 | 离开厨房回到自己房间。 |
| 18:30 | 坐在电脑前。 |
| 21:30 | 上床睡觉。 |

###### 秋季11日和25日（任何玩家与塞巴斯蒂安的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，出门前往 海滩 。 |
| 13:30 | 站在 鱼店 左边的长码头最南端。 |
| 17:00 | 离开码头，回 家 。 |
| 19:40 | 到家，上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开家，前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，站在街机厅的红沙发旁。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期四（ 铁路 已解锁）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 14:00 | 出门前往 火车站 抽烟。 |
| 15:00 | 在火车站抽烟。 |
| 18:20 | 站在火车站东侧的隧道边上。 |
| 20:10 | 站在火车站西侧的隧道边上。 |
| 21:30 | 回家。 |
| 22:20 | 到家。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 出门前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，和 山姆 一起打台球。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 出门前往 山姆 的家。 |
| 11:30 | 和 山姆 一起站在 海莉和艾米丽的家 门口。 |
| 12:30 | 跟着 山姆 去他家。 |
| 13:00 | 位于 山姆 的房间。 |
| 18:00 | 离开 山姆的家 ，和 山姆 一起去靠近山姆家的河边。 |
| 18:20 | 和山姆站在一起，在 山姆家 门口的河边抽烟。 |
| 19:30 | 回 家 。 |
| 21:40 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 12:00 | 离开家，走到他家旁边的湖边。 |
| 14:00 | 走到靠近 矿井 入口的湖边。 |
| 15:00 | 离开矿井入口，走到湖的另一边。 |
| 15:30 | 在位于桥附近的湖边抽烟。 |
| 16:00 | 回家，然后去厨房里。 |
| 17:30 | 离开厨房。 |
| 18:00 | 坐在电脑前。 |
| 21:30 | 上床睡觉。 |

##### 冬季

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:40 | 离开厨房回到自己房间，继续坐在电脑前。 |
| 17:00 | 出门参加 夜市 。 |
| 23:30 | 离开夜市，回家。 |

###### 冬季11日（玩家与塞巴斯蒂安的友谊低于6心） 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:00 | 起床，坐到电脑前。 |
| 12:00 | 在自己房间里，站在沙发旁。 |
| 17:30 | 离开他的房间，前往厨房。 |
| 18:30 | 坐在电脑前。 |
| 21:30 | 上床睡觉。 |

###### 冬季11日和25日（任何玩家与塞巴斯蒂安的友谊均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，出门前往 海滩 。 |
| 13:30 | 站在 鱼店 左边的长码头最南端。 |
| 17:00 | 离开码头，回 家 。 |
| 19:40 | 到家，上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开家，前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，站在街机厅的红沙发旁。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期四（ 铁路 已解锁）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 14:00 | 出门前往 火车站 抽烟。 |
| 15:00 | 在火车站抽烟。 |
| 18:20 | 站在火车站东侧的隧道边上。 |
| 20:10 | 站在火车站西侧的隧道边上。 |
| 21:30 | 回家。 |
| 22:20 | 到家。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 出门前往 星之果实酒吧 。 |
| 17:20 | 到达 星之果实酒吧 ，和 山姆 一起打台球。 |
| 21:10 | 回 家 。 |
| 23:10 | 到家。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 出门前往 山姆 的家。 |
| 11:30 | 和 山姆 一起站在 海莉和艾米丽的家 门口。 |
| 12:30 | 跟着 山姆 去他家。 |
| 13:00 | 位于 山姆 的房间。 |
| 18:00 | 离开 山姆的家 ，和 山姆 一起去靠近山姆家的河边。 |
| 18:20 | 和山姆站在一起，在 山姆家 门口的河边抽烟。 |
| 19:30 | 回 家 。 |
| 21:40 | 到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在自己的床上。 |
| 10:30 | 起床，坐到电脑前。 |
| 15:00 | 离开电脑，前往厨房。 |
| 15:30 | 离开厨房，回到自己房间。 |
| 16:10 | 坐在电脑前。 |
| 18:30 | 出门前往东面的湖边抽烟。 |
| 19:30 | 在房子旁边的湖边抽烟。 |
| 21:30 | 回家。 |

##### 婚后

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农场参加 沙漠节 ，站在仙人掌商人的东北部。 |
| 01:20 | 返回农场。 |

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 离开农场，前往他原先的房间。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 09:00 | 离开农场，前往 深山 。 |
| 09:30 | 经过小镇广场。 |
| 10:30 | 到达他之前经常在湖边站的地方。 |
| 13:00 | 离开湖边，去探望 罗宾 。 |
| 17:20 | 离开深山，返回农场。 |
| 19:20 | 到达农场。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 09:00 | 离开农场，前往 海滩 。 |
| 11:00 | 站在 鱼店 左边的长码头最南端。 |
| 15:00 | 离开码头，前往 星之果实酒吧 。 |
| 16:30 | 到达 星之果实酒吧 ，和 山姆 一起打台球。 |
| 21:30 | 离开酒吧，返回农场。 |
| 22:50 | 到达农场。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、41 个条件分支、261 行。

- After the Beach Resort on Ginger Island is unlocked, Sebastian may randomly spend the day there. After leaving the Island at 6pm, Sebastian will immediately go home to bed. Sebastian never visits the Resort on Festival days or his checkup day at Harvey's Clinic .
- Shown below are Sebastian's schedules prioritized highest to lowest in each season. For example, when it rains that schedule will override all others below it.

##### Spring

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 12:00 PM | Hangs out near the flamingo. |
| 1:40 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

###### Spring 11 (No player has 6 hearts with Sebastian) Spring 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:00 AM | Gets out of bed and moves to his computer. |
| 12:00 PM | In his room, standing by couch. Abigail arrives. |
| 5:00 PM | Abigail leaves. |
| 5:10 PM | Leaving his room to go to the kitchen. |
| 6:00 PM | Leaving kitchen to return to his room. |
| 6:20 PM | Back in room. |
| 9:30 PM | Goes to bed. |

###### Spring 11 and 25 (Any player has at least 6 hearts with Sebastian)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and leaves house to go to the beach . |
| 1:30 PM | Standing at the end of long pier furthest west of the fish shop . |
| 5:00 PM | Leaves the pier to go home . |
| 7:40 PM | Arrives home and goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaving house to go to the Saloon. |
| 5:20 PM | At the Saloon , standing by red sofa in arcade. |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Thursday ( Railroad Accessible)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 2:00 PM | Leaving home to go smoke by train station. |
| 3:00 PM | Smoking by the train station. |
| 6:20 PM | Standing east of train station, by tunnel. |
| 8:10 PM | Standing west of train station, by tunnel. |
| 9:30 PM | Heads home. |
| 10:20 PM | Arrives home. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his room to go play pool with Sam at the Saloon . |
| 5:20 PM | In the Saloon , playing pool with Sam . |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves house to go to Sam 's house. |
| 11:30 AM | In front of Haley and Emily 's house with Sam . |
| 12:30 PM | Follows Sam to his room. |
| 1:00 PM | In Sam 's room. |
| 6:00 PM | Leaves Sam's house with Sam and goes to the river. |
| 6:20 PM | Smoking by the river outside Sam's house with him. |
| 7:30 PM | Going home from in front of Sam's house . |
| 9:40 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In his room. |

###### Summer 4

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his room, by bookcase. |
| 10:00 AM | Leaving house to go to the clinic . |
| 11:50 AM | In the clinic 's waiting room. |
| 1:40 PM | In the clinic 's examination room. |
| 4:00 PM | Heads home . |
| 6:00 PM | Arrives at his room and goes to bed. |

###### Summer 11 (No player has 6 hearts with Sebastian) Summer 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:00 AM | Gets out of bed and moves to his computer. |
| 12:00 PM | In his room, standing by couch. |
| 5:30 PM | Leaving his room to go to the kitchen. |
| 6:30 PM | On his computer. |
| 9:30 PM | Goes to bed. |

###### Summer 11 and 25 (Any player has at least 6 hearts with Sebastian)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and leaves house to go to the beach . |
| 1:30 PM | Standing at the end of long pier to the left of the fish shop . |
| 5:00 PM | Leaves the pier to go home . |
| 7:40 PM | Arrives home and goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaving house to go to the Saloon. |
| 5:20 PM | At the Saloon , standing by red sofa in arcade. |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Thursday ( Railroad Accessible)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 2:00 PM | Leaving home to go smoke by train station. |
| 3:00 PM | Smoking by the train station. |
| 6:20 PM | Standing east of train station, by tunnel. |
| 8:10 PM | Standing west of train station, by tunnel. |
| 9:30 PM | Heads home. |
| 10:20 PM | Arrives home. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his room to go play pool with Sam at the Saloon . |
| 5:20 PM | In the Saloon , playing pool with Sam . |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves house to go to Sam 's house. |
| 11:30 AM | In front of Haley and Emily 's house with Sam . |
| 12:30 PM | Follows Sam to his room. |
| 1:00 PM | In Sam 's room. |
| 6:00 PM | Leaves Sam's house with Sam and goes to the river. |
| 6:20 PM | Smoking by the river outside Sam's house with him. |
| 7:30 PM | Going home from in front of Sam's house . |
| 9:40 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

##### Fall

###### Fall 11 (No player has 6 hearts with Sebastian) Fall 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:00 AM | Gets out of bed and moves to his computer. |
| 12:00 PM | In his room, standing by couch. |
| 5:30 PM | Leaving his room to go to the kitchen. |
| 6:00 PM | Leaves the kitchen to go back to his room. |
| 6:30 PM | On his computer. |
| 9:30 PM | Goes to bed. |

###### Fall 11 and 25 (Any player has at least 6 hearts with Sebastian)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and leaves house to go to the beach . |
| 1:30 PM | Standing at the end of long pier to the left of the fish shop . |
| 5:00 PM | Leaves the pier to go home . |
| 7:40 PM | Arrives home and goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaving house to go to the Saloon. |
| 5:20 PM | At the Saloon , standing by red sofa in arcade. |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Thursday ( Railroad Accessible)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 2:00 PM | Leaving home to go smoke by train station. |
| 3:00 PM | Smoking by the train station. |
| 6:20 PM | Standing east of train station, by tunnel. |
| 8:10 PM | Standing west of train station, by tunnel. |
| 9:30 PM | Heads home. |
| 10:20 PM | Arrives home. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his room to go play pool with Sam at the Saloon . |
| 5:20 PM | In the Saloon , playing pool with Sam . |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves house to go to Sam 's house. |
| 11:30 AM | In front of Haley and Emily 's house with Sam . |
| 12:30 PM | Follows Sam to his room. |
| 1:00 PM | In Sam 's room. |
| 6:00 PM | Leaves Sam's house with Sam and goes to the river. |
| 6:20 PM | Smoking by the river outside Sam's house with him. |
| 7:30 PM | Going home from in front of Sam's house . |
| 9:40 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 12:00 PM | Leaves home and walks to lake next to his house. |
| 2:00 PM | Goes to the part of the lake outside the mines entrance. |
| 3:00 PM | Leaves the mines entrance and heads to the other side of the lake. |
| 3:30 PM | Is smoking at the edge of the lake close to the bridge. |
| 4:00 PM | Returns home to his kitchen. |
| 5:30 PM | Leaves his kitchen. |
| 6:00 PM | On his computer. |
| 9:30 PM | Leaves his computer and goes to bed. |

##### Winter

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and goes to his computer. |
| 3:00 PM | Leaves room and goes to kitchen. |
| 3:40 PM | Goes back to room and returns to his computer. |
| 5:00 PM | Leaves his home to attend Night Market . |
| 11:30 PM | Leaves Night Market to return home. |

###### Winter 11 (No player has 6 hearts with Sebastian) Winter 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:00 AM | Gets out of bed and moves to his computer. |
| 12:00 PM | In his room, standing by couch. |
| 5:30 PM | Leaving his room to go to the kitchen. |
| 6:30 PM | On his computer. |
| 9:30 PM | Goes to bed. |

###### Winter 11 and 25 (Any player has at least 6 hearts with Sebastian)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and leaves house to go to the beach . |
| 1:30 PM | Standing at the end of long pier to the left of the fish shop . |
| 5:00 PM | Leaves the pier to go home . |
| 7:40 PM | Arrives home and goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaving house to go to the Saloon. |
| 5:20 PM | At the Saloon , standing by red sofa in arcade. |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Thursday ( Railroad Accessible)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 2:00 PM | Leaving home to go smoke by train station. |
| 3:00 PM | Smoking by the train station. |
| 6:20 PM | Standing east of train station, by tunnel. |
| 8:10 PM | Standing west of train station, by tunnel. |
| 9:30 PM | Heads home. |
| 10:20 PM | Arrives home. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his room to go play pool with Sam at the Saloon . |
| 5:20 PM | In the Saloon , playing pool with Sam . |
| 9:10 PM | Heads home . |
| 11:10 PM | Arrives home . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves house to go to Sam 's house. |
| 11:30 AM | In front of Haley and Emily 's house with Sam . |
| 12:30 PM | Follows Sam to his room. |
| 1:00 PM | In Sam 's room. |
| 6:00 PM | Leaves Sam's house with Sam and goes to the river. |
| 6:20 PM | Smoking by the river outside Sam's house with him. |
| 7:30 PM | Going home from in front of Sam's house . |
| 9:40 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In his bed. |
| 10:30 AM | Gets out of bed and moves to his computer. |
| 3:00 PM | Leaves his computer and goes to the kitchen. |
| 3:30 PM | Leaves the kitchen to go back to his room. |
| 4:10 PM | On his computer. |
| 6:30 PM | Leaves home and walks to lake next to his house to smoke. |
| 7:30 PM | Smoking by the lake next to his house. |
| 9:30 PM | Goes back to his house. |

##### Marriage

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to go to the Desert Festival and stand north-east of the cactus stand. |
| 1:20 AM | Leaves to go home. |

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Leaves home to walk to his old room. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 9:00 AM | Leaves to go to the mountain. |
| 9:30 AM | Walks through the town square. |
| 10:30 AM | Arrives at his old spot by the mountain lake. |
| 1:00 PM | Leaves to go visit Robin . |
| 5:20 PM | Leaves the mountain and heads home. |
| 7:20 PM | Arrives home. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 9:00 AM | Leaves to go the beach . |
| 11:00 AM | Standing at the end of the long pier to the left of the fish shop . |
| 3:00 PM | Leaves to go to The Stardrop Saloon . |
| 4:30 PM | Arrives at the saloon, playing at the pool table with Sam . |
| 9:30 PM | Leaves to go home. |
| 10:50 PM | Arrives home. |

<a id="npc-schedule-shane"></a>

### 06. 谢恩（Shane）

> 来源：中文 revision 55046；英文 revision 193586
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个分区、29 个条件分支、109 行。

- 姜岛 海滩度假村修复后，谢恩偶尔会去度个假，直到18:00离开回 家 睡觉，谢恩不会在 节日 当天去度假。值得一提的是，谢恩不去 哈维的诊所 体检。
- 下面显示的是谢恩的行程表，每个季节（或部分）的行程从上到下优先级逐次下降，比如下雨时行程安排的优先级就会比它下面的高。

##### 春季

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:00 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:10 | 站在厨师处。 |
| 00:30 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 星期一至星期五（ 社区中心 未修复） 雨天（社区中心未修复）

| 时间 | 地点/行动 |
|------|------|
| 07:10 | 离开 玛妮的牧场 并前往 Joja超市 。 |
| 17:00 | 离开 Joja超市 并前往 星之果实酒吧 。 |
| 23:10 | 离开 星之果实酒吧 ，回到 玛妮的牧场 。 |

###### 星期一至星期五（ 社区中心 已修复） 雨天（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 11:00 | 离开厨房，回到自己的房间。 |
| 12:00 | 离开他的房间，站在 玛妮的牧场 的壁炉旁。 |
| 14:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 12:00 | 离开 玛妮的牧场 并前往 皮埃尔的杂货店 。 |
| 17:00 | 离开 皮埃尔的杂货店 并前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 10:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 的里屋。 |
| 15:00 | 走到壁炉旁边的位置。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 12:30 | 位于 玛妮的牧场 的厨房。 |
| 18:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于厨房。 |

###### 星期一至星期五（ 社区中心 未修复） 雨天（社区中心未修复）

| 时间 | 地点/行动 |
|------|------|
| 07:10 | 离开 玛妮的牧场 并前往 Joja超市 。 |
| 17:00 | 离开 Joja超市 并前往 星之果实酒吧 。 |
| 23:10 | 离开 星之果实酒吧 ，回到 玛妮的牧场 。 |

###### 星期一至星期五 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 11:00 | 离开厨房，回到自己的房间。 |
| 12:00 | 离开他的房间，站在 玛妮的牧场 的壁炉旁。 |
| 14:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 12:00 | 离开 玛妮的牧场 并前往 皮埃尔的杂货店 。 |
| 17:00 | 离开 皮埃尔的杂货店 并前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 10:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 的里屋。 |
| 15:00 | 走到壁炉旁边的位置。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 12:30 | 位于 玛妮的牧场 的厨房。 |
| 18:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

##### 秋季

###### 星期一至星期五（ 社区中心 未修复） 雨天（社区中心未修复）

| 时间 | 地点/行动 |
|------|------|
| 07:10 | 离开 玛妮的牧场 并前往 Joja超市 。 |
| 17:00 | 离开 Joja超市 并前往 星之果实酒吧 。 |
| 23:10 | 离开 星之果实酒吧 ，回到 玛妮的牧场 。 |

###### 星期一至星期五 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 11:00 | 离开厨房，回到自己的房间。 |
| 12:00 | 离开他的房间，站在 玛妮的牧场 的壁炉旁。 |
| 14:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 12:00 | 离开 玛妮的牧场 并前往 皮埃尔的杂货店 。 |
| 17:00 | 离开 皮埃尔的杂货店 并前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 10:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 的里屋。 |
| 15:00 | 走到壁炉旁边的位置。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 12:30 | 位于 玛妮的牧场 的厨房。 |
| 18:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

##### 冬季

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 位于 玛妮的牧场 。 |
| 11:00 | 离开厨房，回到自己的房间。 |
| 15:00 | 离开玛妮的牧场，参加 夜市 。 |
| 23:00 | 离开夜市回家。 |

###### 星期一至星期五（ 社区中心 未修复） 雨天（社区中心未修复）

| 时间 | 地点/行动 |
|------|------|
| 07:10 | 离开 玛妮的牧场 并前往 Joja超市 。 |
| 17:00 | 离开 Joja超市 并前往 星之果实酒吧 。 |
| 23:10 | 离开 星之果实酒吧 ，回到 玛妮的牧场 。 |

###### 星期一至星期五 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 11:00 | 离开厨房，回到自己的房间。 |
| 12:00 | 离开他的房间，站在 玛妮的牧场 的壁炉旁。 |
| 14:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 12:00 | 离开 玛妮的牧场 并前往 皮埃尔的杂货店 。 |
| 17:00 | 离开 皮埃尔的杂货店 并前往 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 离开他的房间，站在 玛妮的牧场 的厨房里。 |
| 10:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 的里屋。 |
| 15:00 | 走到壁炉旁边的位置。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 12:30 | 位于 玛妮的牧场 的厨房。 |
| 18:00 | 离开 玛妮的牧场 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 并回到 玛妮的牧场 。 |

##### 婚后

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 前往参加 沙漠节 ，站在厨师处。 |
| 00:30 | 乘坐巴士返回星露谷。 |

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 前往 玛妮的牧场 并站在厨房里。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 09:30 | 离开农场。 |
| 10:30 | 到达 玛妮的牧场 。 |
| 11:30 | 离开 玛妮的牧场 。 |
| 11:50 | 站在 煤矿森林 北边的大树下。 |
| 17:00 | 离开大树向家走去。 |
| 19:30 | 到达农场。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 08:30 | 离开家，前往 鹈鹕镇 的河边。 |
| 10:00 | 站在河边。 |
| 13:00 | 离开河边走向 皮埃尔的杂货店 。 |
| 17:00 | 离开 皮埃尔的杂货店 走向 星之果实酒吧 。 |
| 22:00 | 离开 星之果实酒吧 并回家。 |

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 08:30 | 离开家，前往 鹈鹕镇 的河边。 |
| 10:00 | 离开河边，前往 星之果实酒吧 的里屋。 |
| 15:00 | 走到Joja自动售货机前面。 |
| 20:00 | 离开 星之果实酒吧 并回家。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、29 个条件分支、109 行。

- If it is raining, Shane will go to work at JojaMart on Saturdays or Sundays, if the Community Center is not complete. He will also go to work at JojaMart until the day after completing the Community Center. Otherwise, he is usually found at The Stardrop Saloon in the evenings.
- After the Beach Resort on Ginger Island is unlocked, Shane may randomly spend the day there. After leaving the Island at 6pm, Shane will immediately go home to bed. Shane never visits the Resort on Festival days.
- Shown below are Shane's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:00 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:10 AM | Stands by the chef stand. |
| 12:30 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

###### Monday - Friday (Community Center Not Restored) Rain (Community Center Not Restored)

| 时间 | 地点/行动 |
|------|------|
| 7:10 AM | Leaves Marnie's Ranch and heads to JojaMart . |
| 5:00 PM | Leaves JojaMart and heads for the Stardrop Saloon . |
| 11:10 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Monday - Friday (Community Center Restored) Rain (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 11:00 AM | Leaves the kitchen and returns to his room. |
| 12:00 PM | Leaves his room and stands by the fireplace at Marnie's Ranch . |
| 2:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 12:00 PM | Leaves Marnie's Ranch and heads to Pierre's General Store . |
| 5:00 PM | Leaves Pierre's General Store and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 10:00 AM | Leaves Marnie's Ranch and heads to the back room of the Stardrop Saloon . |
| 3:00 PM | Moves to his spot next to the fireplace. |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 12:30 PM | In kitchen at Marnie's Ranch . |
| 6:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the kitchen. |

###### Monday - Friday (Community Center Not Restored) Rain (Community Center Not Restored)

| 时间 | 地点/行动 |
|------|------|
| 7:10 AM | Leaves Marnie's Ranch and heads to JojaMart . |
| 5:00 PM | Leaves JojaMart and heads for the Stardrop Saloon . |
| 11:10 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Monday - Friday Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 11:00 AM | Leaves the kitchen and returns to his room. |
| 12:00 PM | Leaves his room and stands by the fireplace at Marnie's Ranch . |
| 2:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 12:00 PM | Leaves Marnie's Ranch and heads to Pierre's General Store . |
| 5:00 PM | Leaves Pierre's General Store and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 10:00 AM | Leaves Marnie's Ranch and heads to the back room of the Stardrop Saloon . |
| 3:00 PM | Moves to his spot next to the fireplace. |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 12:30 PM | In kitchen at Marnie's Ranch . |
| 6:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

##### Fall

###### Monday - Friday (Community Center Not Restored) Rain (Community Center Not Restored)

| 时间 | 地点/行动 |
|------|------|
| 7:10 AM | Leaves Marnie's Ranch and heads to JojaMart . |
| 5:00 PM | Leaves JojaMart and heads for the Stardrop Saloon . |
| 11:10 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Monday - Friday Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 11:00 AM | Leaves the kitchen and returns to his room. |
| 12:00 PM | Leaves his room and stands by the fireplace at Marnie's Ranch . |
| 2:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 12:00 PM | Leaves Marnie's Ranch and heads to Pierre's General Store . |
| 5:00 PM | Leaves Pierre's General Store and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 10:00 AM | Leaves Marnie's Ranch and heads to the back room of the Stardrop Saloon . |
| 3:00 PM | Moves to his spot next to the fireplace. |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 12:30 PM | In kitchen at Marnie's Ranch . |
| 6:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

##### Winter

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | At Marnie's Ranch . |
| 11:00 AM | Leaves the kitchen to head to his room. |
| 3:00 PM | Leaves Marnie's Ranch to attend the Night Market . |
| 11:00 PM | Leaves the Night Market to return home. |

###### Monday - Friday (Community Center Not Restored) Rain (Community Center Not Restored)

| 时间 | 地点/行动 |
|------|------|
| 7:10 AM | Leaves Marnie's Ranch and heads to JojaMart . |
| 5:00 PM | Leaves JojaMart and heads for the Stardrop Saloon . |
| 11:10 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Monday - Friday Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 11:00 AM | Leaves the kitchen and returns to his room. |
| 12:00 PM | Leaves his room and stands by the fireplace at Marnie's Ranch . |
| 2:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 12:00 PM | Leaves Marnie's Ranch and heads to Pierre's General Store . |
| 5:00 PM | Leaves Pierre's General Store and heads to the Stardrop Saloon . |
| 11:00 PM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 7:00AM | Leaves his room and stands in kitchen at Marnie's Ranch . |
| 10:00AM | Leaves Marnie's Ranch and heads to the back room of the Stardrop Saloon . |
| 3:00PM | Moves to his spot next to the fireplace. |
| 12:00AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 12:30 PM | In kitchen at Marnie's Ranch . |
| 6:00 PM | Leaves Marnie's Ranch and heads to the Stardrop Saloon . |
| 12:00 AM | Leaves the Stardrop Saloon and heads back to Marnie's Ranch . |

##### Marriage

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Walks to the Desert Festival and stands by the chef stand. |
| 12:30 AM | Boards the bus back to the Valley. |

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Walks to Marnie's Ranch and stands in the kitchen. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 9:30 AM | Starts leaving home. |
| 10:30 AM | Arrives at Marnie's Ranch . |
| 11:30 AM | Leaves Marnie's Ranch . |
| 11:50 AM | Stands under big tree, north in Cindersap Forest . |
| 05:00 PM | Leaves big tree and heads home. |
| 07:30 PM | Arrives at home. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 8:30 AM | Leaves home and heads for the river in Pelican Town . |
| 10:00 AM | Standing by river. |
| 1:00 PM | Leaves the river and heads to Pierre's General Store . |
| 5:00 PM | Leaves Pierre's General Store and heads to the Stardrop Saloon . |
| 10:00 PM | Leaves the Stardrop Saloon and heads back home. |

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 8:30 AM | Leaves home and heads for the river in Pelican Town . |
| 10:00 AM | Leaves the river and heads to the back room of the Stardrop Saloon . |
| 3:00 PM | Moves to stand in front of the Joja Vending Machine. |
| 8:00 PM | Leaves the Stardrop Saloon and heads back home. |

<a id="npc-schedule-abigail"></a>

### 07. 阿比盖尔（Abigail）

> 来源：中文 revision 55185；英文 revision 193689
>
> 结构判定：中英文结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个分区、46 个条件分支、256 行。

- 姜岛 海滩度假村 修复后，阿比盖尔偶尔会去度个假，18:00离开小岛后，阿比盖尔将立即回家睡觉。阿比盖尔不会在节日或诊所预约日当天去度假。
- 下面显示的是阿比盖尔在每个季节中优先级从高到低的日程表。例如，如果下雨，那么此日程就将覆盖其下的所有日程。

##### 春季

###### 春季4日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的卧室。 |
| 12:30 | 离开家，前往 哈维的诊所 进行每年例行的身体健康检查。 |
| 13:30 | 离开候诊室，前往诊所的检查室。 |
| 16:00 | 离开 哈维的诊所 ，返回她的卧室。 |
| 20:00 | 上床睡觉。 |

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:10 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:00 | 站在仙人掌商人西面的悬崖旁。 |
| 01:30 | 走向巴士，返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季6日和16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 前往 深山 ，站在湖泊的西南角吹笛子。 |
| 20:00 | 回家。 |
| 21:40 | 到 家 。 |

###### 春季11日和25日（玩家与 塞巴斯蒂安 和阿比盖尔的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室的床上。 |
| 10:30 | 离开 家 。 |
| 12:00 | 到达 塞巴斯蒂安 的房间。 |
| 17:00 | 离开 塞巴斯蒂安 的房间。 |
| 18:30 | 回 家 。 |
| 18:50 | 返回卧室。 |

###### 春季11日和25日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 13:00 | 离开 家 ，前往 Joja超市 附近的桥。 |
| 13:30 | 站在 Joja超市 附近的桥上。 |
| 16:30 | 回 家 。 |
| 17:20 | 位于她的卧室，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 11:00 | 离开她的房间，在杂货店柜台前站着。 |
| 13:00 | 前往厨房。 |
| 15:00 | 返回她的房间。 |
| 22:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 14:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 14:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 星期三

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 离开 家 ，前往 博物馆 。 |
| 12:00 | 在 博物馆 图书馆里看书。 |
| 18:00 | 前往 墓园 。 |
| 19:00 | 站在 莫娜 的坟墓前。 |
| 22:00 | 回 家 。 |
| 22:40 | 到 家 。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 15:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 21:40 | 到 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 10:30 | 离开 她的房间 ，前往 卡洛琳 和 皮埃尔 的房间。 |
| 13:00 | 离开 家 ，前往 法师塔 。 |
| 16:00 | 位于 煤矿森林 的 法师塔 附近。 |
| 20:00 | 回 家 。 |
| 22:30 | 到 家 。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 13:00 | 离开 家 ，前往 Joja超市 附近的桥。 |
| 13:30 | 站在 Joja超市 附近的桥上。 |
| 16:30 | 回 家 。 |
| 17:20 | 位于她的卧室，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 家里的客厅 。 |

###### 夏季6日和16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 前往 深山 ，站在湖泊的西南角吹笛子。 |
| 20:00 | 回家。 |
| 21:40 | 到 家 。 |

###### 夏季11日和25日（玩家与 塞巴斯蒂安 和阿比盖尔的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室的床上。 |
| 10:30 | 离开 家 。 |
| 12:00 | 到达 塞巴斯蒂安 的房间。 |
| 17:00 | 离开 塞巴斯蒂安 的房间。 |
| 18:30 | 回 家 。 |
| 18:50 | 返回卧室。 |

###### 夏季11日和25日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 13:00 | 离开 家 ，前往 Joja超市 附近的桥。 |
| 13:30 | 站在 Joja超市 附近的桥上。 |
| 16:30 | 回 家 。 |
| 17:20 | 位于她的卧室，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 11:00 | 离开她的房间，在杂货店柜台前站着。 |
| 13:00 | 前往厨房。 |
| 15:00 | 返回她的房间。 |
| 22:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 14:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 14:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 星期三

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 离开 家 ，前往 博物馆 。 |
| 12:00 | 在 博物馆 图书馆里看书。 |
| 18:00 | 前往 墓园 。 |
| 19:00 | 站在 莫娜 的坟墓前。 |
| 22:00 | 回 家 。 |
| 22:40 | 到 家 。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 15:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 21:40 | 到 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 离开 她的房间 ，前往 卡洛琳 和 皮埃尔 的房间。 |
| 13:00 | 离开 家 ，前往 法师塔 。 |
| 16:00 | 位于 煤矿森林 的 法师塔 附近。 |
| 20:00 | 回 家 。 |
| 22:30 | 到 家 。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开 家 ，前往 火车站台 。 |
| 13:00 | 在 火车站台 前等待。 |
| 14:00 | 前往位于 木匠的商店 东面的湖。 |
| 15:00 | 位于 深山 ， 木匠的商店 东面的湖的附近。 |
| 17:30 | 回 家 。 |
| 19:30 | 到 家 。 |
| 20:00 | 位于卧室，玩电子游戏。 |
| 20:10 | 上床睡觉。 |

##### 秋季

###### 秋季6日和16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 前往 深山 ，站在湖泊的西南角吹笛子。 |
| 20:00 | 回 家 。 |
| 21:40 | 到 家 。 |

###### 秋季11日和25日（玩家与 塞巴斯蒂安 和阿比盖尔的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室的床上。 |
| 10:30 | 离开 家 。 |
| 12:00 | 到达 塞巴斯蒂安 的房间。 |
| 17:00 | 离开 塞巴斯蒂安 的房间。 |
| 18:30 | 回 家 。 |
| 18:50 | 返回卧室。 |

###### 秋季11日和25日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 13:00 | 离开 家 ，前往 Joja超市 附近的桥。 |
| 13:30 | 站在 Joja超市 附近的桥上。 |
| 16:30 | 回 家 。 |
| 17:20 | 位于她的卧室，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 11:00 | 离开她的房间，在杂货店柜台前站着。 |
| 13:00 | 前往厨房。 |
| 15:00 | 返回她的房间。 |
| 22:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 14:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 14:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 11:00 | 离开 家 ，前往 沙滩 。 |
| 13:00 | 站在位于 鱼店 西面的长栈桥的最南端。 |
| 18:00 | 回 家 。 |
| 19:30 | 到 家 ，上床睡觉。 |

###### 星期三

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 离开 家 ，前往 博物馆 。 |
| 12:00 | 在 博物馆 图书馆里看书。 |
| 18:00 | 前往 墓园 。 |
| 19:00 | 站在 莫娜 的坟墓前。 |
| 22:00 | 回 家 。 |
| 22:40 | 到 家 。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 15:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 21:40 | 到 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 10:30 | 离开 她的房间 ，前往 卡洛琳 和 皮埃尔 的房间。 |
| 13:00 | 离开 家 ，前往 法师塔 。 |
| 16:00 | 位于 煤矿森林 的 法师塔 附近。 |
| 20:00 | 回 家 。 |
| 22:30 | 到 家 。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 13:00 | 离开 家 ，前往 巴士站 。 |
| 14:20 | 位于 巴士站 。 |
| 17:00 | 回 家 。 |
| 18:30 | 位于她的卧室，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

##### 冬季

###### 冬季6日和16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 前往 深山 ，站在湖泊的西南角吹笛子。 |
| 20:00 | 回 家 。 |
| 21:40 | 到 家 。 |

###### 冬季11日和25日（玩家与 塞巴斯蒂安 和阿比盖尔的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室的床上。 |
| 10:30 | 离开 家 。 |
| 12:00 | 到达 塞巴斯蒂安 的房间。 |
| 17:00 | 离开 塞巴斯蒂安 的房间。 |
| 18:30 | 回 家 。 |
| 18:50 | 返回卧室。 |

###### 冬季11日和25日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 离开厨房，在杂货店柜台前站着。 |
| 13:00 | 离开 家 ，前往 Joja超市 附近的桥。 |
| 13:30 | 站在 Joja超市 附近的桥上。 |
| 16:30 | 回 家 。 |
| 17:20 | 位于她的卧室，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 前往 木匠的商店 ，站在柜台旁边。 |
| 14:30 | 前往沙滩参加 夜市 。 |
| 00:00 | 回 家 。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 11:00 | 离开她的房间，在杂货店柜台前站着。 |
| 13:00 | 前往厨房。 |
| 15:00 | 返回她的房间。 |
| 22:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 14:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 14:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 星期三

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 离开 家 ，前往 博物馆 。 |
| 12:00 | 在 博物馆 图书馆里看书。 |
| 18:00 | 前往 墓园 。 |
| 19:00 | 站在 莫娜 的坟墓前。 |
| 22:00 | 回 家 。 |
| 22:40 | 到 家 。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 11:00 | 离开厨房，在杂货店柜台前站着。 |
| 15:00 | 离开 家 ，前往 星之果实酒吧 。 |
| 15:50 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 21:00 | 回 家 。 |
| 21:40 | 到 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 10:30 | 离开 她的房间 ，前往 卡洛琳 和 皮埃尔 的房间。 |
| 13:00 | 离开 家 ，前往 法师塔 。 |
| 16:00 | 位于 煤矿森林 的 法师塔 附近。 |
| 20:00 | 回 家 。 |
| 22:30 | 到 家 。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 她的房间 ，前往厨房。 |
| 10:30 | 前往 木匠的商店 ，站在柜台旁边。 |
| 14:30 | 回 家 ，玩电子游戏。 |
| 19:30 | 上床睡觉。 |

##### 婚后

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开农场去参加 沙漠节 ，站在钓鱼水池的上方。 |
| 01:30 | 返回农场。 |

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 前往 皮埃尔的杂货店 中的客厅。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 农场 ，主屋的厨房里。 |
| 08:30 | 离开 农场 ，前往 皮埃尔的杂货店 。 |
| 09:30 | 到达 皮埃尔的杂货店 ，站在 皮埃尔 附近的柜台旁边。 |
| 13:00 | 离开 皮埃尔的杂货店 ，前往墓园。 |
| 13:40 | 站在 莫娜 的坟墓前。 |
| 17:00 | 离开 墓园 ，前往 星之果实酒吧 。 |
| 17:30 | 到达 星之果实酒吧 ，前往 游乐场 。 |
| 17:40 | 开始玩 草原王者大冒险 。 |
| 20:30 | 停止玩游戏，前往农场。 |
| 22:00 | 回到农场，上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 农场 。 |
| 08:30 | 前往 皮埃尔的杂货店 ，站在杂货店厨房。 |
| 11:00 | 前往 深山 。 |
| 11:40 | 位于 深山湖泊 的西面。 |
| 15:00 | 前往 星之果实酒吧 。 |
| 17:30 | 位于 星之果实酒吧 ，坐在 游乐场 的沙发上。 |
| 20:30 | 返回 农场 。 |
| 22:00 | 回到农场，上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、46 个条件分支、257 行。

- After the Beach Resort on Ginger Island is unlocked, Abigail may randomly spend the day there. After leaving the Island at 6pm, Abigail will immediately go home to bed. Abigail never visits the Resort on Festival days or her checkup day at Harvey's Clinic .
- Shown below are Abigail's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 4

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:30 PM | Leaves her room to go to the clinic for her annual check-up. |
| 1:30 PM | Leaves the waiting room and enters the exam room of the clinic . |
| 4:00 PM | Leaves the clinic and goes home back to her room. |
| 8:00 PM | Goes to bed. |

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:10 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:00 AM | Stands at the cliffside west of the cactus stand. |
| 1:30 AM | Starts walking back to the bus. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Spring 6 and 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Goes to the Mountain , standing on the southwest corner of the lake, playing the flute. |
| 8:00 PM | Heads home to go to bed. |
| 9:40 PM | Arrives at home . |

###### Spring 11 and 25 (No player has 6 hearts with Sebastian or Abigail)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In bed. |
| 10:30 AM | Leaves Pierre's store . |
| 12:00 PM | Arrives in Sebastian ’s room. |
| 5:00 PM | Leaves Sebastian ’s room. |
| 6:30 PM | Returns home . |
| 6:50 PM | Back in room. |

###### Spring 11 and 25

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's store . |
| 1:00 PM | Leaves the house to go to stand on bridge near JojaMart . |
| 1:30 PM | Standing on the bridge near JojaMart . |
| 4:30 PM | Heads home . |
| 5:20 PM | In her room , playing video games. |
| 7:30 PM | Goes to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 11:00 AM | Leaves her room to stand in Pierre's General Store . |
| 1:00 PM | Goes to the kitchen . |
| 3:00 PM | Returns to her room . |
| 10:00 PM | Goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 2:00 PM | Leaving the house to go to the Stardrop Saloon . |
| 2:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves home to go to Museum . |
| 12:00 PM | Inside Museum library looking at books. |
| 6:00 PM | Walks to the Graveyard . |
| 7:00 PM | Standing in front of Mona 's grave. |
| 10:00 PM | Heads home . |
| 10:40 PM | Arrives at home . |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Leaving home to go to the Stardrop Saloon . |
| 3:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 9:40 PM | Arrives home . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 10:30 AM | Leaves her room to go into Caroline and Pierre 's room. |
| 1:00 PM | Leaving home to go to the Wizard's Tower . |
| 4:00 PM | Near Wizard's Tower in Cindersap Forest . |
| 8:00 PM | Heads home . |
| 10:30 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's store . |
| 1:00 PM | Leaves the house to go to stand on bridge near JojaMart . |
| 1:30 PM | Standing on the bridge near JojaMart . |
| 4:30 PM | Heads home . |
| 5:20 PM | In her room , playing video games. |
| 7:30 PM | Goes to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the living room . |

###### Summer 6 and 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Goes to the Mountain , standing on the southwest corner of the lake, playing the flute. |
| 8:00 PM | Heads home to go to bed. |
| 9:40 PM | Arrives at home . |

###### Summer 11 and 25 (No player has 6 hearts with Sebastian or Abigail)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In bed. |
| 10:30 AM | Leaves Pierre's store . |
| 12:00 PM | Arrives in Sebastian ’s room. |
| 5:00 PM | Leaves Sebastian ’s room. |
| 6:30 PM | Returns home . |
| 6:50 PM | Back in room. |

###### Summer 11 and 25

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's store . |
| 1:00 PM | Leaves the house to go to stand on bridge near JojaMart . |
| 1:30 PM | Standing on the bridge near JojaMart . |
| 4:30 PM | Heads home . |
| 5:20 PM | In her room , playing video games. |
| 7:30 PM | Goes to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 11:00 AM | Leaves her room to stand in Pierre's General Store . |
| 1:00 PM | Goes to the kitchen . |
| 3:00 PM | Returns to her room . |
| 10:00 PM | Goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 2:00 PM | Leaving the house to go to the Stardrop Saloon . |
| 2:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves home to go to the library . |
| 12:00 PM | Inside library , looking at books. |
| 6:00 PM | Walks to the Graveyard . |
| 7:00 PM | Standing in front of Mona 's grave. |
| 10:00 PM | Heads home . |
| 10:40 PM | Arrives at home . |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Leaving home to go to the the Stardrop Saloon . |
| 3:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 9:40 PM | Arrives home . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Leaves her room to go into Caroline and Pierre 's room. |
| 1:00 PM | Leaves home , walks to the Wizard's Tower . |
| 4:00 PM | Standing in front of the Wizard's Tower in Cindersap Forest . |
| 8:00 PM | Heads home . |
| 10:30 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves home , walks to the Train Platform . |
| 1:00 PM | Waiting in front of the Train Platform . |
| 2:00 PM | Walks to the lake east of the Carpenter's Shop . |
| 3:00 PM | Standing by the Mountain lake east of the Carpenter's Shop . |
| 5:30 PM | Heads home . |
| 7:30 PM | Arrives home . |
| 8:00 PM | Plays video games. |
| 8:10 PM | Goes to bed. |

##### Fall

###### Fall 6 and 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Goes to the Mountain , standing on the southwest corner of the lake, playing the flute. |
| 8:00 PM | Heads home to go to bed. |
| 9:40 PM | Arrives at home . |

###### Fall 11 and 25 (No player has 6 hearts with Sebastian or Abigail)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In bed. |
| 10:30 AM | Leaves Pierre's store . |
| 12:00 PM | Arrives in Sebastian ’s room. |
| 5:00 PM | Leaves Sebastian ’s room. |
| 6:30 PM | Returns home . |
| 6:50 PM | Back in room. |

###### Fall 11 and 25

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's store . |
| 1:00 PM | Leaves the house to go to stand on bridge near JojaMart . |
| 1:30 PM | Standing on the bridge near JojaMart . |
| 4:30 PM | Heads home . |
| 5:20 PM | In her room , playing video games. |
| 7:30 PM | Goes to bed. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 11:00 AM | Leaves her room to stand in Pierre's General Store . |
| 1:00 PM | Goes to the kitchen . |
| 3:00 PM | Returns to her room . |
| 10:00 PM | Goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 2:00 PM | Leaving the house to go to the Stardrop Saloon . |
| 2:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 11:00 AM | Leaving home to go to the Beach . |
| 1:00 PM | Standing at the end of long pier to the left of the Fish Shop . |
| 6:00 PM | Heads home . |
| 7:30 PM | Arrives home and goes to bed. |

###### Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Leaves home to go to library . |
| 12:00 PM | Inside library , looking at books. |
| 6:00 PM | Walks to the Graveyard . |
| 7:00 PM | Standing in front of Mona 's grave. |
| 10:00 PM | Heads home . |
| 10:40 PM | Arrives at home . |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Leaving Pierre's General Store to go to the Stardrop Saloon . |
| 3:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 9:40 PM | Arrives home . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 10:30 AM | Leaves her room to go into Caroline and Pierre 's room. |
| 1:00 PM | Leaving home to go to the Wizard's Tower . |
| 4:00 PM | Near the Wizard's Tower in Cindersap Forest . |
| 8:00 PM | Heads home . |
| 10:30 PM | Arrives at home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 1:00 PM | Leaving the house to go to stand at Bus Stop . |
| 2:20 PM | Standing at Bus Stop . |
| 5:00 PM | Heads home . |
| 6:30 PM | In her room , playing video games. |
| 7:30 PM | Goes to bed. |

##### Winter

###### Winter 6 and 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Goes to the Mountain , standing on the southwest corner of the lake, playing the flute. |
| 8:00 PM | Heads home to go to bed. |
| 9:40 PM | Arrives at home . |

###### Winter 11 and 25 (No player has 6 hearts with Sebastian or Abigail)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In bed. |
| 10:30 AM | Leaves Pierre's store . |
| 12:00 PM | Arrives in Sebastian ’s room. |
| 5:00 PM | Leaves Sebastian ’s room. |
| 6:30 PM | Returns home . |
| 6:50 PM | Back in room. |

###### Winter 11 and 25

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room to go to the kitchen . |
| 10:30 AM | Leaves the kitchen to stand in Pierre's store . |
| 1:00 PM | Leaves the house to go to stand on bridge near JojaMart . |
| 1:30 PM | Standing on the bridge near JojaMart . |
| 4:30 PM | Heads home . |
| 5:20 PM | In her room , playing video games. |
| 7:30 PM | Goes to bed. |

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 10:30 AM | Walking to the Carpenter's Shop . Stands next to the counter. |
| 2:30 PM | Walks to beach to attend Night Market . |
| 12:00 AM | Back at home . |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 11:00 AM | Leaves her room to stand in Pierre's General Store . |
| 1:00 PM | Goes to the kitchen . |
| 3:00 PM | Returns to her room . |
| 10:00 PM | Goes to bed. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 2:00 PM | Leaving the house to go to the Stardrop Saloon . |
| 2:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Wednesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves home to go to the library . |
| 12:00 PM | Inside the library , looking at books. |
| 6:00 PM | Walks to the Graveyard . |
| 7:00 PM | Standing in front of Mona 's grave. |
| 10:00 PM | Heads home . |
| 10:40 PM | Arrives at home . |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 11:00 AM | Leaves the kitchen to stand in Pierre's General Store . |
| 3:00 PM | Leaving Pierre's General Store to go to the Stardrop Saloon . |
| 3:50 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 9:00 PM | Heads home . |
| 9:40 PM | Arrives home . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room . |
| 10:30 AM | Leaves her room to go into Caroline and Pierre 's room. |
| 1:00 PM | Leaving home to go to the Wizard's Tower . |
| 4:00 PM | Near the Wizard's Tower in Cindersap Forest . |
| 8:00 PM | Heads home . |
| 10:30 PM | Arrives home . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaving her room to go to the kitchen . |
| 10:30 AM | Walking to the Carpenter's Shop . Stands next to the counter. |
| 2:30 PM | Heads back home and plays video games. |
| 7:30 PM | Goes to bed. |

##### Marriage

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves home to go to the Desert Festival and stand north of the fishing pond. |
| 1:30 AM | Returns home . |

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Walks to her parent's living room. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home , in the kitchen. |
| 8:30 AM | Leaves home to go to Pierre's General Store . |
| 9:30 AM | Arrives at Pierre's General Store , stands by the counter near Pierre . |
| 1:00 PM | Leaves Pierre's General Store , walking to the Graveyard. |
| 1:40 PM | Standing in front of Mona 's grave. |
| 5:00 PM | Leaves the Graveyard , heading to the Stardrop Saloon . |
| 5:30 PM | Arrives at the Stardrop Saloon , heads to the arcade . |
| 5:40 PM | Begins playing Journey of the Prairie King . |
| 8:30 PM | Stops playing Journey of the Prairie King , starts walking home . |
| 10:00 PM | At home in bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home . |
| 8:30 AM | Heads to Pierre's General Store and stands in the kitchen . |
| 11:00 AM | Walking to the Mountain . |
| 11:40 AM | West side of the Mountain Lake. |
| 3:00 PM | Walking to the Stardrop Saloon . |
| 5:30 PM | In the Stardrop Saloon , sitting on a sofa in the arcade . |
| 8:30 PM | Walking home . |
| 10:00 PM | Arrives home . |
| 10:30 PM | At home in bed. |

<a id="npc-schedule-emily"></a>

### 08. 艾米丽（Emily）

> 来源：中文 revision 55091；英文 revision 191968
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 11 个分区、14 个条件分支、50 行。

- 姜岛的海滩度假村 解锁后，艾米丽有时会去那儿。18:00离开姜岛后，艾米丽会立即回家上床睡觉。艾米丽不会在秋季15日（桑迪的生日）、冬季11日（她的体检日）或节日当天去姜岛。
- 以下是艾米丽的日程安排，优先度从高到低排序。例如，如果当天下雨，雨天的时间表会比下方的优先级更高。

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 春季15日、16日和17日（巴士站已修复）

###### 春季15日、16日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:30 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:00 | 站在她的 服装服务处 。 |
| 00:30 | 乘坐巴士返回星露谷。 |

##### 秋季15日（巴士站已修复）

###### 秋季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 10:30 | 离开家前往 沙漠 探望 桑迪 。 |
| 00:00 | 回家休息。 |

##### 冬季11日

###### 冬季11日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 10:30 | 出门前往 哈维的诊所 ，待在候诊室。 |
| 13:30 | 走进检查室。 |
| 16:00 | 离开哈维的诊所，去 星之果实酒吧 工作。 |
| 00:30 | 回家睡觉。 |

##### 冬季15日

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 12:00 | 从卧室中出来，站在客厅里。 |
| 14:30 | 出门去参加 夜市 。 |
| 00:30 | 回家睡觉。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 12:00 | 从卧室中出来，站在客厅里。 |
| 15:30 | 出门去 星之果实酒吧 工作。 |
| 00:30 | 回家睡觉。 |

##### 星期二

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 10:00 | 出门前往 皮埃尔的杂货店 ，参加健身锻炼。 |
| 13:00 | 开始健身锻炼。 |
| 16:00 | 离开杂货店，去 星之果实酒吧 工作。 |
| 00:30 | 回家睡觉。 |

##### 星期五（社区中心已修复）

###### 星期五（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 10:00 | 走向 社区中心 ，站在工艺室中。 |
| 15:30 | 离开社区中心，去 星之果实酒吧 工作。 |
| 00:30 | 回家睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室中。 |
| 12:00 | 从卧室中出来，站在客厅里。 |
| 15:30 | 出门去 星之果实酒吧 工作。 |
| 00:30 | 回家睡觉。 |

##### 婚后

###### 春季15日、16日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开农场参加 沙漠节 ，站在她的 服装服务处 。 |
| 00:30 | 返回农场。 |

###### 秋季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 12:00 | 到达 绿洲 探望 桑迪 。 |
| 13:00 | 从 绿洲 出门，在 沙漠 中散步。 |
| 00:00 | 回家休息。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农舍，前往 柳巷2号 ，站在厨房里。 |
| 11:00 | 离开 柳巷2号 ，站在 社区中心 东侧，看着镇上的河流。 |
| 15:00 | 去 星之果实酒吧 工作。 |
| 22:00 | 离开酒吧，回家。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农舍，前往 鱼店 西侧的码头。 |
| 13:00 | 离开 沙滩 ，前往 皮埃尔的杂货店 。 |
| 15:00 | 离开杂货店，去 星之果实酒吧 工作。 |
| 22:00 | 离开酒吧，回家。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 11 个分区、14 个条件分支、50 行。

- After the Beach Resort on Ginger Island is unlocked, Emily may randomly spend the day there. After leaving the Island at 6pm, Emily will immediately go home to bed. Emily never visits the Resort on Fall 15, Festival days, or her checkup day at Harvey's Clinic .
- Shown below are Emily's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

##### Spring 15, 16 and 17 (Bus Service Restored)

###### Spring 15, 16 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:30 AM | Boards bus to Calico Desert to attend the Desert Festival . |
| 10:00 AM | Stands at her outfit services. |
| 12:30 AM | Boards bus back to the Valley. |

##### Fall 15 (Bus Service Restored)

###### Fall 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 10:30 AM | Leaves home for Calico Desert to visit Sandy on her birthday. |
| 12:00 AM | Goes home for the night. |

##### Winter 11

###### Winter 11

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 10:30 AM | Leaves home for Harvey's Clinic , waits in waiting room. |
| 1:30 PM | Moves to exam room. |
| 4:00 PM | Leaves clinic to work at The Stardrop Saloon . |
| 12:30 AM | Goes home for the night. |

##### Winter 15

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 12:00 PM | Leaves bedroom to stand in living room. |
| 2:30 PM | Leaves home to attend the Night Market . |
| 12:30 AM | Goes home for the night. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In The Stardrop Saloon . |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 12:00 PM | Leaves bedroom to stand in living room. |
| 3:30 PM | Leaves home to work at The Stardrop Saloon . |
| 12:30 AM | Goes home for the night. |

##### Tuesday

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 10:00 AM | Leaves home to attend aerobics class at Pierre's General Store . |
| 1:00 PM | Aerobics class begins. |
| 4:00 PM | Leaves Pierre's to work at The Stardrop Saloon . |
| 12:30 AM | Goes home for the night. |

##### Friday (Community Center Restored)

###### Friday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 10:00 AM | Walks to Community Center , stands in Crafts Room. |
| 3:30 PM | Leaves the Community Center to work at The Stardrop Saloon . |
| 12:30 AM | Goes home for the night. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 12:00 PM | Leaves bedroom to stand in living room. |
| 3:30 PM | Leaves home to work at The Stardrop Saloon . |
| 12:30 AM | Goes home for the night. |

##### Marriage

###### Spring 15, 16 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves home to attend the Desert Festival and stand at her outfit services. |
| 12:30 AM | Heads home. |

###### Fall 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 12:00 PM | Arrives at the Oasis to visit Sandy on her birthday. |
| 1:00 PM | Leaves the Oasis and walks around Calico Desert . |
| 12:00 AM | Heads home for the night. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to walk to 2 Willow Lane , stands in kitchen. |
| 11:00 AM | Leaves 2 Willow Lane to go to town , stands east of Community Center and looks at the river. |
| 3:00 PM | Heads for the Stardrop Saloon to work. |
| 10:00 PM | Leaves the Saloon to return home. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves house to go to docks west of Fish Shop . |
| 1:00 PM | Leaves beach to go to Pierre's General Store . |
| 3:00 PM | Leaves Pierre's to go to work at the Stardrop Saloon . |
| 10:00 PM | Leaves the Saloon to return home. |

<a id="npc-schedule-haley"></a>

### 09. 海莉（Haley）

> 来源：中文 revision 55013；英文 revision 191939
>
> 结构判定：中英文结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个分区、25 个条件分支、133 行。

- 姜岛 海滩度假村 修复后，海莉偶尔会去度个假，18:00离开小岛后，海莉将立即回家睡觉。海莉不会在节日或诊所预约日当天去度假。
- 下面显示的是海莉在每个季节中优先级从高到低的日程表。例如，如果下雨，那么此日程就将覆盖其下的所有日程。

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:50 | 在 艾米丽 的 服装服务 西侧走动。 |
| 01:30 | 乘坐巴士返回星露谷。 |

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:00 | 在 绿洲 南侧的悬崖前晒日光浴。 |
| 21:00 | 起身并走回巴士。 |
| 21:30 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 起床，站在卧室的梳妆台旁。 |
| 11:30 | 走到卧室的梳妆镜前。 |
| 12:00 | 离开卧室，前往厨房。 |
| 16:00 | 返回卧室。 |
| 19:00 | 离开卧室，站在客厅里。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:00 | 离开卧室，前往厨房。 |
| 11:00 | 离开家，前往 玛妮的牧场 南边的河。 |
| 12:20 | 待在河边，拍照。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 23:00 | 上床睡觉。 |

###### 星期三（玩家与海莉和 亚历克斯 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:10 | 位于客厅。 |
| 16:30 | 前往厨房。 |
| 20:00 | 返回卧室。 |
| 22:30 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 11:00 | 离开家，前往喷泉。 |
| 12:20 | 站在 社区中心 左侧的喷泉旁边。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 22:30 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 起床，站在卧室的梳妆台旁。 |
| 11:30 | 走到卧室的梳妆镜前。 |
| 12:00 | 离开卧室，前往厨房。 |
| 16:00 | 返回卧室。 |
| 19:00 | 离开卧室，站在客厅里。 |
| 22:00 | 上床睡觉。 |

###### 星期三（玩家与海莉和 亚历克斯 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:10 | 位于客厅。 |
| 16:30 | 前往厨房。 |
| 20:00 | 返回卧室。 |
| 22:30 | 上床睡觉。 |

###### 星期三（任何玩家与 亚历克斯 的 友谊 均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 11:00 | 离开家，前往喷泉。 |
| 12:20 | 站在 社区中心 左侧的喷泉旁边。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 22:30 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:30 | 离开家，前往 沙滩 。 |
| 11:50 | 位于沙滩的西北角。 |
| 13:30 | 前往亚历克斯的 冰淇淋摊 。 |
| 14:30 | 位于 博物馆 附近的 冰淇淋摊 。 |
| 17:00 | 回家。 |
| 18:20 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 23:00 | 上床睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 起床，站在卧室的梳妆台旁。 |
| 11:30 | 走到卧室的梳妆镜前。 |
| 12:00 | 离开卧室，前往厨房。 |
| 16:00 | 返回卧室。 |
| 19:00 | 离开卧室，站在客厅里。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:00 | 离开卧室，前往厨房。 |
| 11:00 | 离开家，前往 玛妮的牧场 南边的河。 |
| 12:20 | 待在河边，拍照。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 23:00 | 上床睡觉。 |

###### 星期三（玩家与海莉和 亚历克斯 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:10 | 位于客厅。 |
| 16:30 | 前往厨房。 |
| 20:00 | 返回卧室。 |
| 22:30 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 11:00 | 离开家，前往喷泉。 |
| 12:20 | 站在 社区中心 左侧的喷泉旁边。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 22:30 | 上床睡觉。 |

##### 冬季

###### 冬季9日

| 时间 | 地点/行动 |
|------|------|
| 11:30 | 位于 哈维的诊所 。 |
| 16:00 | 回家。 |

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 起床，站在卧室的梳妆台旁。 |
| 11:30 | 走到卧室的梳妆镜前。 |
| 12:00 | 离开卧室，前往厨房。 |
| 16:30 | 参加 夜市 。 |
| 00:00 | 回家。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 起床，站在卧室的梳妆台旁。 |
| 11:30 | 走到卧室的梳妆镜前。 |
| 12:00 | 离开卧室，前往厨房。 |
| 16:00 | 返回卧室。 |
| 19:00 | 离开卧室，站在客厅里。 |
| 22:00 | 上床睡觉。 |

###### 星期三（玩家与海莉和 亚历克斯 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:10 | 位于客厅。 |
| 16:30 | 前往厨房。 |
| 20:00 | 返回卧室。 |
| 22:30 | 上床睡觉。 |

###### 星期三（任何玩家与 亚历克斯 的 友谊 均达到6心）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 11:00 | 离开家，前往喷泉。 |
| 12:20 | 站在 社区中心 左侧的喷泉旁边。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 22:30 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 11:00 | 离开家，前往喷泉。 |
| 12:20 | 站在 社区中心 左侧的喷泉旁边。 |
| 16:30 | 回家。 |
| 17:50 | 在家做晚饭。 |
| 20:20 | 位于卧室。 |
| 22:30 | 上床睡觉。 |

##### 婚后

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开农场，参加 沙漠节 。 |
| 10:00 | 在 艾米丽 的 服装服务 西侧走动。 |
| 00:00 | 回家。 |

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开农场参加 沙漠节 ，在 绿洲 南侧的悬崖前晒日光浴。 |
| 21:00 | 回家 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 09:30 | 离开农场。 |
| 10:40 | 到达 柳巷2号 。 |
| 15:40 | 离开 柳巷2号 。 |
| 17:00 | 返回农场。 |
| 22:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、25 个条件分支、132 行。

- After the Beach Resort on Ginger Island is unlocked, Haley may randomly spend the day there. After leaving the Island at 6pm, Haley will immediately go home to bed. Haley never visits the Resort on Festival days or her checkup day at Harvey's Clinic .
- Shown below are Haley's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:50 AM | Walks around the area west of Emily 's outfit services . |
| 1:30 AM | Boards the bus back to the Valley. |

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:00 AM | Sunbathes on the cliff south of the Oasis . |
| 9:00 PM | Gets up and heads back to the bus. |
| 9:30 PM | Takes the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and stands by her dresser in her bedroom. |
| 11:30 AM | Moves to the vanity mirror in her bedroom. |
| 12:00 PM | Leaves her room to go to the kitchen. |
| 4:00 PM | Returns to her room. |
| 7:00 PM | Leaves her room and stands in the living room. |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:00 AM | Leaves her room to go to kitchen. |
| 11:00 AM | Leaving home to go to the river south of Marnie's Ranch . |
| 12:20 PM | By the river south of Marnie's Ranch , taking pictures. |
| 4:30 PM | Heads home. |
| 5:50 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 11:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:10 PM | In the living room. |
| 4:30 PM | Moves to the kitchen. |
| 8:00 PM | Returns to her room |
| 10:30 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 11:00 AM | Leaving home to go to the fountain. |
| 12:20 PM | By the fountain, west of Community Center . |
| 4:30 PM | Heads home. |
| 5:50 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 10:30 PM | Goes to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In The Stardrop Saloon . |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and stands by her dresser in her bedroom. |
| 11:30 AM | Moves to the vanity mirror in her bedroom. |
| 12:00 PM | Leaves her room to go to the kitchen. |
| 4:00 PM | Returns to her room. |
| 7:00 PM | Leaves her room and stands in the living room. |
| 10:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:10 PM | In the living room. |
| 4:30 PM | Moves to the kitchen. |
| 8:00 PM | Returns to her room |
| 10:30 PM | Goes to bed. |

###### Wednesday (Any player has at least 6 hearts with Alex)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 11:00 AM | Leaving home to go to the fountain. |
| 12:20 PM | By the fountain, west of Community Center . |
| 4:30 PM | Heads home. |
| 5:50 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 10:30 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:30 AM | Leaving house to go to beach . |
| 11:50 AM | At the beach, northwest corner. |
| 1:30 PM | Goes to Alex's ice cream stand . |
| 2:30 PM | At Alex's ice cream stand , next to museum/library . |
| 5:00 PM | Heads home. |
| 6:20 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 11:00 PM | Goes to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and stands by her dresser in her bedroom. |
| 11:30 AM | Moves to the vanity mirror in her bedroom. |
| 12:00 PM | Leaves her room to go to the kitchen. |
| 4:00 PM | Returns to her room. |
| 7:00 PM | Leaves her room and stands in the living room. |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:00 AM | Leaves her room to go to kitchen. |
| 11:00 AM | Leaving home to go to the river south of Marnie's Ranch . |
| 12:20 PM | By the river south of Marnie's Ranch , taking pictures. |
| 4:30 PM | Heads home. |
| 5:50 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 11:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:10 PM | In the living room. |
| 4:30 PM | Moves to the kitchen. |
| 8:00 PM | Returns to her room |
| 10:30 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 11:00 AM | Leaving home to go to the fountain. |
| 12:20 PM | By the fountain, west of Community Center . |
| 4:30 PM | Heads home. |
| 5:50 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 10:30 PM | Goes to bed. |

##### Winter

###### Winter 9

| 时间 | 地点/行动 |
|------|------|
| 11:30 AM | Harvey's Clinic. |
| 4:00 PM | Walks home. |

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and stands by her dresser in her bedroom. |
| 11:30 AM | Moves to the vanity in her bedroom. |
| 12:00 PM | Leaves her room to go to the kitchen. |
| 4:30 PM | Attends the Night Market . |
| 12:00 AM | Returns home. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and stands by her dresser in her bedroom. |
| 11:30 AM | Moves to the vanity in her bedroom. |
| 12:00 PM | Leaves her room to go to the kitchen. |
| 4:00 PM | Returns to her room. |
| 7:00 PM | Leaves her room and stands in the living room. |
| 10:00 PM | Goes to bed. |

###### Wednesday (No player has 6 hearts with Haley or Alex)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:10 PM | In the living room. |
| 4:30 PM | Moves to the kitchen. |
| 8:00 PM | Returns to her room |
| 10:30 PM | Goes to bed. |

###### Wednesday (Any player has at least 6 hearts with Alex)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 11:00 AM | Leaving home to go to the fountain. |
| 12:20 PM | By the fountain, west of Community Center . |
| 4:30 PM | Heads home. |
| 5:50 PM | At home, cooking dinner. |
| 8:20 PM | In her room. |
| 10:30 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Wakes up and stands by her dresser in her bedroom. |
| 11:30 AM | Moves to the vanity in her bedroom. |
| 12:00 PM | Leaves her room to go to the kitchen. |
| 4:00 PM | Returns to her room. |
| 7:00 PM | Leaves her room and stands in the living room. |
| 10:00 PM | Goes to bed. |

##### Marriage

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves home to attend the Desert Festival . |
| 10:00 AM | Walks around the area west of Emily 's outfit services . |
| 12:00 AM | Heads home. |

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves home to attend the Desert Festival and sunbathe on the cliff south of the Oasis . |
| 9:00 PM | Heads home. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home. |
| 9:30 AM | Starts leaving home. |
| 10:40 AM | Arrives at 2 Willow Lane . |
| 3:40 PM | Starts leaving 2 Willow Lane . |
| 5:00 PM | Goes back home. |
| 10:00 PM | Goes to bed. |

<a id="npc-schedule-leah"></a>

### 10. 莉亚（Leah）

> 来源：中文 revision 55041；英文 revision 192966
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个分区、21 个条件分支、93 行。

- 姜岛 海滩度假村修复后，莉亚偶尔会去度个假，直到18:00离开回 家 睡觉，莉亚不会在她体检日（春季16日）和 节日 当天去度假。
- 下面显示的是莉亚的行程表，从上到下优先级逐次下降，例如雨天行程的优先级会比在它下面的高。

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:40 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:20 | 站在赛跑跑道南侧的沙制雕塑前。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 10:30 | 离开家前往 哈维的诊所 的候诊室。 |
| 13:30 | 走到诊所里靠左的检查室。 |
| 16:00 | 离开诊所前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧回到家里睡觉。 |

###### 雨天 星期五、星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 走到她的画板前画画。 |
| 14:00 | 站在小屋里的书架前。 |
| 16:00 | 离开小屋前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧回到家里睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 11:00 | 前往 皮埃尔的杂货店 购物。 |
| 17:00 | 离开杂货店回家并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 离开 小屋 ，走到小屋西南部的河边。站在河岸，凝视着水面。 |
| 15:00 | 走到 煤矿森林 中心湖桥尽头，画画。 |
| 18:30 | 走到 煤矿森林 中心湖西侧。 |
| 19:30 | 回到她的 小屋 ，站在书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 站在自己的 小屋 门口，欣赏苔藓雨。 |
| 13:00 | 回到她的 小屋 ，站在床的旁边。 |
| 22:00 | 上床睡觉。 |

###### 雨天 星期五、星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 走到她的画板前画画。 |
| 14:00 | 站在小屋里的书架前。 |
| 16:00 | 离开小屋前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧回到家里睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 11:00 | 前往 皮埃尔的杂货店 购物。 |
| 17:00 | 离开杂货店回家并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表（海滩桥梁已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 离开她的 小屋 穿过小镇去 沙滩 的 潮汐池 画画。 |
| 19:00 | 离开沙滩，回到她的 小屋 并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 离开她的 小屋 穿过小镇去 沙滩 画画。 |
| 19:00 | 离开沙滩，回到她的 小屋 并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

##### 秋季

###### 雨天 星期五、星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 走到她的画板前画画。 |
| 14:00 | 站在小屋里的书架前。 |
| 16:00 | 离开小屋前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧回到家里睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 11:00 | 前往 皮埃尔的杂货店 购物。 |
| 17:00 | 离开杂货店回家并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 离开她的 小屋 ，前往小镇河流的东面、 铁匠铺 的上面。 |
| 19:00 | 离开小镇，回到她的 小屋 并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

##### 冬季

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 走到她的画板前画画。 |
| 14:00 | 站在小屋里的书架前。 |
| 16:00 | 离开小屋参加 夜市 。 |
| 23:40 | 离开夜市回家睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 走到她的画板前画画。 |
| 14:00 | 站在小屋里的书架前。 |
| 16:00 | 离开小屋前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧回到家里睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 11:00 | 前往 皮埃尔的杂货店 购物。 |
| 17:00 | 离开杂货店回家并站在小屋里的书架前。 |
| 22:00 | 站在小屋里的桌子前。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床在她的 小屋 里雕刻。 |
| 12:00 | 走到她的画板前画画。 |
| 14:00 | 站在小屋里的书架前。 |
| 16:00 | 离开小屋前往 星之果实酒吧 。 |
| 23:40 | 离开酒吧回到家里睡觉。 |

##### 婚后

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开农场参加 沙漠节 站在钓鱼池旁边。 |
| 01:20 | 回到农场。 |

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 离开农场前往她的 小屋 门口，欣赏苔藓雨。 |
| 13:00 | 回到她的小屋，站在床的旁边。 |
| 22:00 | 在她的小屋内上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开农场走到她的 小屋 西南部的河边。站在河岸，凝视着水面。 |
| 15:00 | 站在她的 小屋 门口。 |
| 17:30 | 离开煤矿森林并回到农场。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、21 个条件分支、93 行。

- After the Beach Resort on Ginger Island is unlocked, Leah may randomly spend the day there. After leaving the Island at 6pm, Leah will immediately go home to bed. Leah never visits the Resort on Festival days or her checkup day at Harvey's Clinic .
- Shown below are Leah's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:40 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:20 AM | Stands by the sand sculpture south of the racing line. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Spring 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 10:30 AM | Goes to the waiting room of Harvey's Clinic . |
| 1:30 PM | Moves from the waiting room to the left exam room in the Clinic. |
| 4:00 PM | Leaves the Clinic and walks to The Stardrop Saloon . |
| 11:40 PM | Leaves the Saloon to return home and sleep. |

###### Friday, Saturday and Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Moves to her easel to paint. |
| 2:00 PM | Stands in front of the bookcase in her cottage. |
| 4:00 PM | Leaves her cottage and walks to The Stardrop Saloon . |
| 11:40 PM | Leaves the Saloon to return home and sleep. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 11:00 AM | Goes to shop at Pierre's General Store . |
| 5:00 PM | Leaves the store to return home and stand in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Walks to the edge of the river near the island southwest of her cottage. |
| 3:00 PM | Walks to the end of the pier over the forest pond and draws. |
| 6:30 PM | Walks to the west side of the forest pond. |
| 7:30 PM | Walks back to her cottage and stands in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Stands outside her cottage. |
| 1:00 PM | Stands in her cottage, next to her bed. |
| 10:00 PM | Goes to bed for the night. |

###### Rain Friday and Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Moves to her easel to paint. |
| 2:00 PM | Stands in front of the bookcase in her cottage. |
| 4:00 PM | Leaves her cottage and walks to The Stardrop Saloon . |
| 11:40 PM | Leaves the Saloon to return home and sleep. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 11:00 AM | Goes to shop at Pierre's General Store . |
| 5:00 PM | Leaves the store to return home and stands in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

###### Regular Schedule (Beach Bridge Repaired)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Leaves her cottage to draw at the tidal pools at the beach. |
| 7:00 PM | Leaves the beach to return home and stands in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Leaves her cottage to draw at the beach. |
| 7:00 PM | Leaves the beach to return home and stands in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

##### Fall

###### Rain Friday and Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Moves to her easel to paint. |
| 2:00 PM | Stands in front of the bookcase in her cottage. |
| 4:00 PM | Leaves her cottage and walks to The Stardrop Saloon . |
| 11:40 PM | Leaves the Saloon to return home and sleep. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 11:00 AM | Goes to shop at Pierre's General Store . |
| 5:00 PM | Leaves the store to return home and stand in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Walks to the east side of the river in town , above the Blacksmith . |
| 7:00 PM | Leaves town to return home and stand in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

##### Winter

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Moves to her easel to paint. |
| 2:00 PM | Stands in front of the bookcase in her cottage. |
| 4:00 PM | Leaves her cottage to attend the Night Market . |
| 11:40 PM | Leaves the Night Market to return home and sleep. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Moves to her easel to paint. |
| 2:00 PM | Stands in front of the bookcase in her cottage. |
| 4:00 PM | Leaves her cottage and walks to The Stardrop Saloon . |
| 11:40 PM | Leaves the Saloon to return home and sleep. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 11:00 AM | Goes to shop at Pierre's General Store . |
| 5:00 PM | Leaves the store to return home and stand in front of her bookcase. |
| 10:00 PM | Stands at the table in her house. |
| 12:00 AM | Goes to bed for the night. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Sculpts in her cottage. |
| 12:00 PM | Moves to her easel to paint. |
| 2:00 PM | Stands in front of the bookcase in her cottage. |
| 4:00 PM | Leaves her cottage and walks to The Stardrop Saloon . |
| 11:40 PM | Leaves the Saloon to return home and sleep. |

##### Marriage

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves home to head to the Desert Festival and stand by the fishing pond. |
| 1:20 AM | Returns home. |

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Leaves home to walk to her cottage and stand outside. |
| 1:00 PM | Stands in her cottage, next to her bed. |
| 10:00 PM | In bed in her cottage. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves the farmhouse to walk to the bridge near the small island southwest of her cottage. |
| 3:00 PM | Stands outside of her cottage. |
| 5:30 PM | Leaves the forest to return home to the farm. |

<a id="npc-schedule-maru"></a>

### 11. 玛鲁（Maru）

> 来源：中文 revision 55085；英文 revision 193560
>
> 结构判定：中英文结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个分区、25 个条件分支、129 行。

- 姜岛 海滩度假村修复后，玛鲁偶尔会去度个假，直到18:00离开回家睡觉，玛鲁不会在周二，周四和 节日 当天去度假。
- 下面显示的是玛鲁在每个季节中优先级从高到低的日程表。例如，如果下雨，那么此日程就将覆盖其下的所有日程。

##### 春季

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:50 | 在赛跑终点线附近观看比赛。 |
| 00:20 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:50 | 站在 木匠的商店 房内的入口处。 |
| 14:40 | 位于实验室。 |
| 16:40 | 位于卧室。 |
| 23:00 | 上床睡觉。 |

###### 星期一、星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 13:30 | 前往 星之果实酒吧 南边的长椅。 |
| 15:20 | 坐在酒吧门前的长椅上。 |
| 18:30 | 回家。 |
| 20:30 | 位于卧室。 |
| 23:00 | 上床睡觉。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开家，前往 哈维的诊所 。 |
| 09:20 | 在诊所作为护士工作。 |
| 16:45 | 离开诊所，回家。 |
| 18:30 | 位于 木匠的商店 的厨房。 |
| 22:20 | 位于卧室。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 14:00 | 前往 社区中心 东边的长椅。 |
| 15:00 | 坐在长椅上。 |
| 18:00 | 回家。 |
| 19:00 | 位于卧室。 |
| 22:00 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 塞巴斯蒂安 的房间。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:30 | 站在 木匠的商店 房内的入口处。 |
| 14:30 | 前往家里的实验室。 |
| 16:30 | 位于卧室。 |
| 23:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 13:30 | 前往 星之果实酒吧 南边的长椅。 |
| 15:20 | 坐在酒吧门前的长椅上。 |
| 18:30 | 回家。 |
| 20:10 | 到家。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 离开家，前往 哈维的诊所 。 |
| 09:40 | 在诊所作为护士工作。 |
| 16:45 | 离开诊所，回家。 |
| 18:40 | 位于 木匠的商店 的厨房。 |
| 22:00 | 返回卧室。 |
| 00:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 12:30 | 返回卧室，和 潘妮 待在一起。 |
| 23:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 14:00 | 离开家，前往东边的湖。 |
| 14:40 | 站在湖边。 |
| 19:00 | 回家。 |
| 19:40 | 位于房子外面，使用望远镜观测。 |
| 00:00 | 回屋睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 12:30 | 站在 木匠的商店 房内的入口处。 |
| 14:30 | 前往家里的实验室。 |
| 16:30 | 返回卧室。 |
| 23:00 | 上床睡觉。 |

###### 星期一、星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 13:30 | 前往 星之果实酒吧 南边的长椅。 |
| 15:20 | 坐在酒吧门前的长椅上。 |
| 18:30 | 回家。 |
| 20:10 | 到家。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 离开家，前往 哈维的诊所 。 |
| 09:40 | 在诊所作为护士工作。 |
| 16:45 | 离开诊所，回家。 |
| 18:40 | 位于 木匠的商店 的厨房。 |
| 22:00 | 返回卧室。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 位于实验室。 |
| 14:00 | 前往 社区中心 东边的长椅。 |
| 15:00 | 坐在长椅上。 |
| 18:00 | 回家。 |
| 19:10 | 位于她的卧室。 |
| 22:00 | 上床睡觉。 |

##### 冬季

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开她的房间。 |
| 09:20 | 位于家中的实验室。 |
| 11:00 | 前往她的房间。 |
| 15:40 | 离开家，参加 夜市 。 |
| 23:30 | 离开夜市，回家。 |

###### 星期一、星期天

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 离开卧室。 |
| 10:20 | 位于实验室。 |
| 13:30 | 前往 星之果实酒吧 南边的长椅。 |
| 15:30 | 坐在酒吧门前的长椅上。 |
| 18:30 | 回家。 |
| 20:00 | 到家。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 离开家，前往 哈维的诊所 。 |
| 09:40 | 在诊所作为护士工作。 |
| 16:45 | 离开诊所，回家。 |
| 18:40 | 位于 木匠的商店 的厨房。 |
| 22:00 | 返回卧室。 |

###### 社区中心 已修复

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 前往家中的实验室。 |
| 14:40 | 离开家，前往 社区中心 工艺室。 |
| 18:00 | 回家。 |
| 18:40 | 位于家中的厨房。 |
| 22:00 | 返回卧室。 |
| 00:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于卧室。 |
| 10:20 | 前往家中的实验室。 |
| 14:40 | 离开家，前往 社区中心 东边的长椅。 |
| 18:00 | 回家。 |
| 18:40 | 位于家中的厨房。 |
| 22:00 | 返回卧室。 |
| 00:00 | 上床睡觉。 |

##### 婚后

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 离开农场，前往 塞巴斯蒂安 的房间。 |

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:50 | 在赛跑终点线附近观看比赛。 |
| 00:10 | 乘坐巴士返回星露谷。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于农场。 |
| 08:00 | 前往 木匠的商店 。 |
| 10:00 | 位于 木匠的商店 。 |
| 14:00 | 前往 社区中心 。 |
| 15:00 | 坐在社区中心右边的长椅上。 |
| 18:00 | 返回农场。 |
| 19:30 | 到达。 |

###### 星期二、星期四

| 时间 | 地点/行动 |
|------|------|
| 07:30 | 离开农场，前往 哈维的诊所 。 |
| 09:00 | 站在诊所柜台的后面。 |
| 14:00 | 离开柜台，站在诊所等候区看文件。 |
| 16:40 | 离开诊所，返回农场。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、24 个条件分支、124 行。

- After the Beach Resort on Ginger Island is unlocked, Maru may randomly spend the day there. After leaving the Island at 6pm, Maru will immediately go home to bed. Maru never visits the Resort on Tuesdays, Thursdays, or Festival days.
- Shown below are Maru's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 9:50 AM | Watches the races near the finish line. |
| 12:20 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:50 PM | Stands in Entryway/Store (Home). |
| 2:40 PM | In the lab. |
| 4:40 PM | In her room. |
| 11:00 PM | Goes to bed. |

###### Monday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:20 AM | In the lab. |
| 1:30 PM | Heading to bench south of the Saloon. |
| 3:20 PM | Sitting on bench south of the Saloon. |
| 6:30 PM | Heading home. |
| 8:30 PM | At home, in her room. |
| 11:00 PM | Goes to bed. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves home and heads to Harvey's. |
| 9:20 AM | Working at Harvey's clinic as a nurse. |
| 4:45 PM | Leaves Harvey's and heads home. |
| 6:30 PM | At home, in the kitchen. |
| 10:20 PM | In her room. |
| 12:00 AM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:20 AM | In the lab. |
| 2:00 PM | Heads to bench east of the Community Center. |
| 3:00 PM | Sitting on bench east of the Community Center. |
| 6:00 PM | Heads home. |
| 7:00 PM | At home, in her room. |
| 10:00 PM | Goes to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In Sebastian 's room. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 12:30 PM | Leaves her room to stand in the "store" part of the house. |
| 2:30 PM | Goes to the lab in her house. |
| 4:30 PM | At home, in her room. |
| 11:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:20 AM | In the lab. |
| 1:30 PM | Leaving house to go sit on a bench in front of Saloon. |
| 3:20 PM | Sitting on a bench in front of Stardrop Saloon. |
| 6:30 PM | Heads home. |
| 8:10 PM | Arrives home. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | Leaving home to go to work at the clinic. |
| 9:40 AM | Working at Harvey's clinic as a nurse. |
| 4:45 PM | Heads home. |
| 6:40 PM | At home, in the kitchen. |
| 10:00 PM | Goes to her room. |
| 12:00 AM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:20 AM | In the lab. |
| 12:30 PM | Returns to her room, with Penny. |
| 11:00 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:00 AM | Leaves her room. |
| 10:20 AM | In the lab. |
| 2:00 PM | Leaving house to go to stand by lake, east of house. |
| 2:40 PM | Standing by lake, east of house. |
| 7:00 PM | Heads home. |
| 7:40 PM | Outside house, looking through telescope. |
| 12:00 AM | Heads inside and goes to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 12:30 PM | Leaves her room to stand in the "store" part of the house. |
| 2:30 PM | Goes to the lab in her house. |
| 4:30 PM | Returns to her room. |
| 11:00 PM | Goes to bed. |

###### Monday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 10:20 AM | In the lab. |
| 1:30 PM | Leaving house to go sit on a bench in front of the Saloon. |
| 3:20 PM | Sitting on a bench in front of the Stardrop Saloon. |
| 6:30 PM | Heads home. |
| 8:10 PM | Arrives at home. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | Leaving home to go to work at the clinic. |
| 9:40 AM | Working at Harvey's clinic as a nurse. |
| 4:45 PM | Heads home. |
| 6:40 PM | At home, in the kitchen. |
| 10:00 PM | Goes to her room. |
| 12:00 AM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:20 AM | In the lab. |
| 2:00 PM | Leaving house to go sit on bench, east of Community Center. |
| 3:00 PM | Sitting on bench, east of the Community Center. |
| 6:00 PM | Heads home. |
| 7:10 PM | At home, in her room. |
| 10:00 PM | Goes to bed. |

##### Winter

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room. |
| 9:20 AM | In lab at home. |
| 11:00 AM | Goes to her room. |
| 3:40 PM | Leaves home to attend Night Market. |
| 11:30 PM | Leaves Night Market to return home. |

###### Monday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves room. |
| 10:20 AM | In lab at home. |
| 1:30 PM | Leaves lab at home. |
| 3:30 PM | Sits down on bench north of graveyard. |
| 6:30 PM | Gets up from bench and walks home. |
| 8:00 PM | Returns home. |

###### Tuesday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | Leaving home to go to work at the clinic. |
| 9:40 AM | Working at Harvey's clinic as a nurse. |
| 4:45 PM | Heads home. |
| 6:40 PM | At home, in the kitchen. |
| 10:00 PM | In bedroom. |

###### Community Center Restored

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her room and goes to the lab in her house. |
| 11:00 AM | Leaves house to visit the Community Center Crafts Room. |
| 4:00 PM | Heads home. |
| 5:40 PM | At home, in her room. |
| 10:00 PM | Goes to bed. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:20 AM | Goes to the lab in her house. |
| 2:40 PM | Leaves to sit on the bench by the Community Center. |
| 6:00 PM | Heads home. |
| 6:40 PM | At home, in the kitchen. |
| 10:00 PM | Goes to her room. |
| 12:00 AM | Goes to bed. |

##### Marriage

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Leaves home to walk to Sebastian's room. |

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 9:50 AM | Watches the races near the finish line. |
| 12:10 AM | Boards the bus back to the Valley. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At farmhouse. |
| 8:00 AM | Walking to Carpenter's Shop. |
| 10:00 AM | Carpenter's Shop . |
| 2:00 PM | Walking to Community Center. |
| 3:00 PM | Sits on bench to right of Community Center. |
| 6:00 PM | Walking Home. |
| 7:30 PM | At Home. |

<a id="npc-schedule-penny"></a>

### 12. 潘妮（Penny）

> 来源：中文 revision 55083；英文 revision 193516
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个分区、38 个条件分支、191 行。

- 潘妮经常在 鹈鹕镇 上看书，或者在 拖车 中做家务。周二、周三、周五时，她会去 博物馆 给 贾斯 和 文森特 上课，然后送他们俩回家。在周六，她会带孩子们去鹈鹕镇西北角的游乐场游玩。
- 在 冬季 的第四天，她会去 哈维的诊所 做体检。
- 如果碰上雨天，潘妮可能会一直待在 拖车 里，或者去 博物馆 看书。
- 姜岛的海滩度假村 解锁后，潘妮有时会去那儿。18:00离开姜岛后，潘妮会立即回家上床睡觉。潘妮不会在周二、周三、周五、冬季4日（她的体检日）或节日当天去姜岛。

##### 春季

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:30 | 登上前往 沙漠 的巴士，参加 沙漠节 。 |
| 10:00 | 站在传送雕像附近。 |
| 01:00 | 登上巴士返回鹈鹕镇。 |

###### 沙漠节（作为商铺卖家）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 登上巴士前往 沙漠 。 |
| 11:30 | 到达她的 商铺 。 |
| 00:00 | 离开商铺，登上巴士返回鹈鹕镇。 |

###### 春季9日和23日（玩家与潘妮和 山姆 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 09:00 | 起床，站在她的卧室里。 |
| 11:00 | 离开拖车，走到 鹈鹕镇 上 冰淇淋摊 旁边的桥上，并坐下。 |
| 16:00 | 从 鹈鹕镇 返回 拖车 ，开始洗碗。 |
| 18:40 | 走到 拖车 中她的房间，上床睡觉。 |

###### 春季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 08:00 | 离开 拖车 ，前往 墓园 附近看书。 |
| 12:30 | 返回 拖车 ，洗碗。 |
| 16:00 | 离开 拖车 ，和 玛鲁 一起坐在 星之果实酒吧 门前的长椅上。 |
| 18:40 | 返回 拖车 ，上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于 拖车 中她的卧室。 |
| 11:00 | 前往厨房。 |
| 13:00 | 开始洗碗。 |
| 15:00 | 坐在沙发上，可能是在看电视。 |
| 18:00 | 返回卧室，在书架旁看书。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 08:10 | 离开 拖车 ，前往 博物馆 ，坐在外面。 |
| 12:00 | 进入 博物馆 ，看着书架。 |
| 16:00 | 离开 博物馆 ，返回 拖车 看电视。 |
| 19:00 | 走到 拖车 里的水槽前洗碗。 |
| 21:00 | 上床睡觉。 |

###### 星期一、星期四、星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开 拖车 ，前往 墓园 附近看书。 |
| 12:30 | 返回 拖车 ，洗碗。 |
| 16:00 | 离开 拖车 ，和 玛鲁 一起坐在 星之果实酒吧 门前的长椅上。 |
| 18:40 | 返回 拖车 ，上床睡觉。 |

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 拖车 ，前往 博物馆 辅导 贾斯 和 文森特 学习。 |
| 14:00 | 离开 博物馆 ，站在 冰淇淋摊 旁，看着 贾斯 和 文森特 玩耍。 |
| 16:20 | 陪 文森特 走到他 家 ，和他说再见。 |
| 17:50 | 陪 贾斯 走到她 家 ，和她说再见。 |
| 18:30 | 返回 拖车 ，上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 10:00 | 离开 拖车 ，在 墓园 旁与 贾斯 和 文森特 会面。 |
| 12:00 | 将 贾斯 和 文森特 带到小镇广场北面的 游乐场 ，看着他们玩耍。 |
| 17:00 | 送 贾斯 和 文森特 回家，将他们送到 艾米丽和海莉家 门口。 |
| 18:30 | 返回 拖车 ，上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

###### 夏季9日和23日（玩家与潘妮和 山姆 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 09:00 | 起床，站在她的卧室里。 |
| 11:00 | 离开拖车，走到 鹈鹕镇 上 冰淇淋摊 旁边的桥上，并坐下。 |
| 16:00 | 从 鹈鹕镇 返回 拖车 ，开始洗碗。 |
| 18:40 | 走到 拖车 中她的房间，上床睡觉。 |

###### 夏季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 08:00 | 离开 拖车 ，前往 墓园 附近看书。 |
| 12:30 | 返回 拖车 ，洗碗。 |
| 16:00 | 离开 拖车 ，和 玛鲁 一起坐在 星之果实酒吧 门前的长椅上。 |
| 18:40 | 返回 拖车 ，上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于 拖车 中她的卧室。 |
| 11:00 | 前往厨房。 |
| 13:00 | 开始洗碗。 |
| 15:00 | 坐在沙发上，可能是在看电视。 |
| 18:00 | 返回卧室，在书架旁看书。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 08:10 | 离开 拖车 ，前往 博物馆 ，坐在外面。 |
| 12:00 | 进入 博物馆 ，看着书架。 |
| 16:00 | 离开 博物馆 ，返回 拖车 看电视。 |
| 19:00 | 走到 拖车 里的水槽前洗碗。 |
| 21:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开 拖车 ，前往 Joja超市 上方的河边。 |
| 09:20 | 站在Joja超市上方，小河的右边。 |
| 12:00 | 前往 木匠的商店 。 |
| 13:40 | 到达 木匠的商店 中 玛鲁 的房间，和玛鲁坐在一起。 |
| 18:00 | 离开 木匠的商店 ，返回 拖车 洗碗。 |
| 21:00 | 返回卧室，上床睡觉。 |

###### 星期一、星期四

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 起床，穿过 小镇 ，站在 Joja超市 后面的河边。 |
| 09:30 | 站在 Joja超市 后面的小河边。 |
| 13:00 | 步行穿过 小镇 ，前往 社区中心 。 |
| 14:30 | 在 社区中心 右侧的长椅坐下。 |
| 18:00 | 离开，返回 拖车 。 |
| 19:00 | 返回 拖车 ，上床睡觉。 |

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 拖车 ，前往 博物馆 。 |
| 10:00 | 到达 博物馆 。 |
| 14:00 | 鹈鹕镇 ，在 博物馆 外面的桥附近。 |
| 16:00 | 在 柳巷2号 外，送 文森特 和 贾斯 回家。 |
| 18:30 | 离开 玛妮的牧场 ，开始回家。 |
| 20:00 | 到达 拖车 ，上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 离开 拖车 ，前往 墓园 附近。 |
| 11:00 | 和孩子们待在 墓园 附近。 |
| 12:00 | 和孩子们一起去 社区中心 左侧的操场。 |
| 13:00 | 在游乐场，和孩子们玩耍。 |
| 17:00 | 送 贾斯 和 文森特 到 艾米丽 家。 |
| 18:00 | 在 艾米丽 家附近和 贾斯 与 文森特 交谈。 |
| 20:00 | 前往 拖车 。 |
| 21:00 | 到达 拖车 ，上床睡觉。 |

##### 秋季

###### 秋季9日和23日（玩家与潘妮和 山姆 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 09:00 | 起床，站在她的卧室里。 |
| 11:00 | 离开拖车，走到 鹈鹕镇 上 冰淇淋摊 旁边的桥上，并坐下。 |
| 16:00 | 从 鹈鹕镇 返回 拖车 ，开始洗碗。 |
| 18:40 | 走到 拖车 中她的房间，上床睡觉。 |

###### 秋季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 08:00 | 离开 拖车 ，前往 墓园 附近看书。 |
| 12:30 | 返回 拖车 ，洗碗。 |
| 16:00 | 离开 拖车 ，和 玛鲁 一起坐在 星之果实酒吧 门前的长椅上。 |
| 18:40 | 返回 拖车 ，上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于 拖车 中她的卧室。 |
| 11:00 | 前往厨房。 |
| 13:00 | 开始洗碗。 |
| 15:00 | 坐在沙发上，可能是在看电视。 |
| 18:00 | 返回卧室，在书架旁看书。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 08:10 | 离开 拖车 ，前往 博物馆 ，坐在外面。 |
| 12:00 | 进入 博物馆 ，看着书架。 |
| 16:00 | 离开 博物馆 ，返回 拖车 看电视。 |
| 19:00 | 走到 拖车 里的水槽前洗碗。 |
| 21:00 | 上床睡觉。 |

###### 星期一、星期四、星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 离开 拖车 ，前往 墓园 附近看书。 |
| 12:30 | 返回 拖车 ，洗碗。 |
| 16:00 | 离开 拖车 ，和 玛鲁 一起坐在 星之果实酒吧 门前的长椅上。 |
| 18:40 | 返回 拖车 ，上床睡觉。 |

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 拖车 ，前往 博物馆 辅导 贾斯 和 文森特 学习。 |
| 14:00 | 离开 博物馆 ，站在 冰淇淋摊 旁，看着 贾斯 和 文森特 玩耍。 |
| 16:20 | 陪 文森特 走到他 家 ，和他说再见。 |
| 17:50 | 陪 贾斯 走到她 家 ，和她说再见。 |
| 18:30 | 返回 拖车 ，上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 10:00 | 离开 拖车 ，在 墓园 旁与 贾斯 和 文森特 会面。 |
| 12:00 | 将 贾斯 和 文森特 带到小镇广场北面的 游乐场 ，看着他们玩耍。 |
| 17:00 | 送 贾斯 和 文森特 回家，将他们送到 艾米丽和海莉家 门口。 |
| 18:30 | 返回 拖车 ，上床睡觉。 |

##### 冬季

###### 冬季4日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床，在 拖车 里四处移动。 |
| 11:30 | 离开 拖车 ，前往 哈维的诊所 进行每年例行的身体健康检查。 |
| 13:30 | 继续在 诊所 内接受检查。 |
| 16:00 | 离开 诊所 ，前往 Joja超市 西侧的桥桥边坐下。 |
| 19:00 | 离开 小镇 ，回到 拖车 洗碗。 |
| 21:00 | 回卧室睡觉休息。 |

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 拖车 已解锁。潘妮呆在卧室中。 |
| 11:00 | 进入厨房。 |
| 13:00 | 洗碗。 |
| 15:00 | 坐在沙发上，可能在看电视。 |
| 16:00 | 参加 夜市 。 |
| 23:50 | 上床睡觉。 |

###### 冬季9日和23日（玩家与潘妮和 山姆 的 友谊 均低于6心）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 09:00 | 起床，站在她的卧室里。 |
| 11:00 | 离开拖车，走到 鹈鹕镇 上 冰淇淋摊 旁边的桥上，并坐下。 |
| 16:00 | 从 鹈鹕镇 返回 拖车 ，开始洗碗。 |
| 18:40 | 走到 拖车 中她的房间，上床睡觉。 |

###### 冬季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 拖车 里她的床上。 |
| 08:00 | 离开 拖车 ，前往 墓园 附近看书。 |
| 12:30 | 返回 拖车 ，洗碗。 |
| 16:00 | 离开 拖车 ，和 玛鲁 一起坐在 星之果实酒吧 门前的长椅上。 |
| 18:40 | 返回 拖车 ，上床睡觉。 |

###### 雨天（第一种选择）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于 拖车 中她的卧室。 |
| 11:00 | 前往厨房。 |
| 13:00 | 开始洗碗。 |
| 15:00 | 坐在沙发上，可能是在看电视。 |
| 18:00 | 返回卧室，在书架旁看书。 |
| 21:00 | 上床睡觉。 |

###### 雨天（第二种选择）

| 时间 | 地点/行动 |
|------|------|
| 08:10 | 离开 拖车 ，前往 博物馆 ，坐在外面。 |
| 12:00 | 进入 博物馆 ，看着书架。 |
| 16:00 | 离开 博物馆 ，返回 拖车 看电视。 |
| 19:00 | 走到 拖车 里的水槽前洗碗。 |
| 21:00 | 上床睡觉。 |

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 拖车 ，前往 博物馆 辅导 贾斯 和 文森特 学习。 |
| 14:00 | 离开 博物馆 ，站在 冰淇淋摊 旁，看着 贾斯 和 文森特 玩耍。 |
| 16:20 | 陪 文森特 走到他 家 ，和他说再见。 |
| 17:50 | 陪 贾斯 走到她 家 ，和她说再见。 |
| 18:30 | 返回 拖车 ，上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于她的房间。 |
| 10:00 | 离开 拖车 ，在 墓园 旁与 贾斯 和 文森特 会面。 |
| 12:00 | 将 贾斯 和 文森特 带到小镇广场北面的 游乐场 ，看着他们玩耍。 |
| 17:00 | 送 贾斯 和 文森特 回家，将他们送到 艾米丽和海莉家 门口。 |
| 18:30 | 返回 拖车 ，上床睡觉。 |

###### 社区中心 已修复

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床后，在 拖车 内转悠。 |
| 10:30 | 离开 拖车 ，前往 社区中心 读书。 |
| 15:00 | 在 社区中心 内晃悠。 |
| 18:00 | 离开 社区中心 ，返回 拖车 ，洗碗。 |
| 21:00 | 上床睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床后，在 拖车 内转悠。 |
| 10:30 | 离开 拖车 ，来到 墓园 左边的树下读书。 |
| 18:00 | 离开 博物馆 ，返回 拖车 洗碗。 |
| 21:00 | 上床睡觉。 |

##### 婚后

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:30 | 登上前往 沙漠 的巴士，参加 沙漠节 。 |
| 10:00 | 站在传送雕像附近。 |
| 01:00 | 登上巴士返回鹈鹕镇。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开 农舍 去 皮埃尔的杂货店 。 |
| 11:30 | 离开 皮埃尔的杂货店 ，在镇上读书。 |
| 16:00 | 坐在镇上。 |
| 18:10 | 离开小镇回到农场。 |
| 22:00 | 上床睡觉。 |

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开 农舍 ，前往 博物馆 。 |
| 14:00 | 离开 博物馆 ，和 文森特 与 贾斯 一起回到 镇上 。 |
| 16:20 | 在 海莉 和 艾米丽 的房子前，送 文森特 回家。 |
| 17:50 | 前往 玛妮的牧场 ，送 贾斯 回家。 |
| 18:30 | 离开 玛妮的牧场 ，回家休息。 |
| 20:10 | 到达 农舍 。 |
| 22:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个分区、38 个条件分支、191 行。

- Penny can usually be found in town reading or cleaning up at the trailer . On Tuesday, Wednesday, and Friday she tutors Jas and Vincent at the museum , walking them both home afterwards. On Saturdays she'll take them to the town playground .
- When it's raining Penny can either be found inside her trailer or visiting the museum looking at the selection of books.
- After the Beach Resort on Ginger Island is unlocked, Penny may randomly spend the day there. After leaving the Island at 6pm, Penny will immediately go home to bed. Penny never visits the Resort on Tuesday, Wednesday, Friday, Festival days, or her checkup day at Harvey's Clinic .

##### Spring

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:30 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:00 AM | Stands near the Calico warp statue. |
| 1:00 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes bus back to the Valley. |

###### Spring 9 and 23 (No player has 6 hearts with Penny or Sam )

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 9:00 AM | Wakes up and stands in her bedroom. |
| 11:00 AM | Walks to town and sits on the bridge near the Ice Cream Stand . |
| 4:00 PM | Returns from town to the trailer and does some dishes. |
| 6:40 PM | Goes to bed in her room in the trailer for the evening. |

###### Spring 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 8:00 AM | Leaves her trailer and goes outside to read near the town graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom in the Trailer . |
| 11:00 AM | Moves to the kitchen. |
| 1:00 PM | Does some dishes. |
| 3:00 PM | Sits on the couch, probably watching TV. |
| 6:00 PM | Returns to her bedroom, reading by the bookshelf. |
| 9:00 PM | Goes to bed for the evening. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 8:10 AM | Leaves the trailer and walks to the Museum to sit outside. |
| 12:00 PM | Goes inside the Museum to look at the bookshelves. |
| 4:00 PM | Leaves the Museum and returns to the trailer to watch some television. |
| 7:00 PM | Moves over to the sink in the trailer to do some dishes. |
| 9:00 PM | Goes to bed for the evening. |

###### Monday, Thursday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves her trailer and goes outside to read near the Graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her trailer and goes to the museum/library to tutor Jas and Vincent . |
| 2:00 PM | Leaves the library and stands near the Ice Cream Stand watching over Jas and Vincent . |
| 4:20 PM | Walks Vincent to 1 Willow Lane and says goodbye. |
| 5:50 PM | Walks Jas to Marnie's Ranch and says goodbye. |
| 6:30 PM | Returns to her trailer for the evening. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:00 AM | Leaves her trailer to meet up with Jas and Vincent near the town graveyard . |
| 12:00 PM | Walks Jas and Vincent to the playground north of town square and watches them play. |
| 5:00 PM | Walks Jas and Vincent back to town and drops them off in front of Emily and Haley's house . |
| 6:30 PM | Returns to her trailer for the evening. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In The Stardrop Saloon . |

###### Summer 9 and 23 (No player has 6 hearts with Penny or Sam )

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 9:00 AM | Wakes up and stands in her bedroom. |
| 11:00 AM | Walks to town and sits on the bridge near the Ice Cream Stand . |
| 4:00 PM | Returns from town to the trailer and does some dishes. |
| 6:40 PM | Goes to bed in her room in the trailer for the evening. |

###### Summer 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 8:00 AM | Leaves her trailer and goes outside to read near the town graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom in the Trailer . |
| 11:00 AM | Moves to the kitchen. |
| 1:00 PM | Does some dishes. |
| 3:00 PM | Sits on the couch, probably watching TV. |
| 6:00 PM | Returns to her bedroom, reading by the bookshelf. |
| 9:00 PM | Goes to bed for the evening. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 8:10 AM | Leaves the trailer and walks to the Museum to sit outside. |
| 12:00 PM | Goes inside the Museum to look at the bookshelves. |
| 4:00 PM | Leaves the Museum and returns to the trailer to watch some television. |
| 7:00 PM | Moves over to the sink in the trailer to do some dishes. |
| 9:00 PM | Goes to bed for the evening. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves her trailer and walks to the river above JojaMart . |
| 9:20 AM | Stands above JojaMart, to the right of the river. |
| 12:00 PM | Goes to the Carpenter's Shop . |
| 1:40 PM | Arrives at Maru 's room in the Carpenter's Shop and sits with Maru. |
| 6:00 PM | Leaves Carpenter's Shop and returns to the trailer to do dishes. |
| 9:00 PM | Goes to bed for the evening. |

###### Monday and Thursday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Wakes up and walks through town to stand by the river behind JojaMart . |
| 9:30 AM | Watching the river behind JojaMart . |
| 1:00 PM | Walks back through town and to the Community Center . |
| 2:30 PM | Sitting on a bench to the right of the Community Center . |
| 6:00 PM | Leaves town and returns to the trailer . |
| 7:00 PM | Arrives at the trailer for the evening. |

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves the trailer and walks to the Museum . |
| 10:00 AM | In the Museum . |
| 2:00 PM | Pelican Town , outside of the Museum near bridge. |
| 4:00 PM | Outside 2 Willow Lane , walking Vincent and Jas home. |
| 6:30 PM | Leaves Marnie's Ranch and returns to home for the evening. |
| 8:00 PM | Arrives at the trailer for the evening. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves her trailer and goes outside near the town graveyard . |
| 11:00 AM | With the kids near the town graveyard . |
| 12:00 PM | Walk kids to the playground, west of the Community Center . |
| 1:00 PM | At the playground, play with kids. |
| 5:00 PM | Walks Jas and Vincent to Emily 's house. |
| 6:00 PM | Beside Emily 's house, talking with Jas and Vincent . |
| 8:00 PM | Goes to the trailer . |
| 9:00 PM | Arrives at the trailer for the evening. |

##### Fall

###### Fall 9 and 23 (No player has 6 hearts with Penny or Sam )

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 9:00 AM | Wakes up and stands in her bedroom. |
| 11:00 AM | Walks to town and sits on the bridge near the Ice Cream Stand . |
| 4:00 PM | Returns from town to the trailer and does some dishes. |
| 6:40 PM | Goes to bed in her room in the trailer for the evening. |

###### Fall 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 8:00 AM | Leaves her trailer and goes outside to read near the town graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom in the Trailer . |
| 11:00 AM | Moves to the kitchen. |
| 1:00 PM | Does some dishes. |
| 3:00 PM | Sits on the couch, probably watching TV. |
| 6:00 PM | Returns to her bedroom, reading by the bookshelf. |
| 9:00 PM | Goes to bed for the evening. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 8:10 AM | Leaves the trailer and walks to the Museum to sit outside. |
| 12:00 PM | Goes inside the Museum to look at the bookshelves. |
| 4:00 PM | Leaves the Museum and returns to the trailer to watch some television. |
| 7:00 PM | Moves over to the sink in the trailer to do some dishes. |
| 9:00 PM | Goes to bed for the evening. |

###### Monday, Thursday and Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves her trailer and goes outside to read near the Graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her trailer and goes to the museum/library to tutor Jas and Vincent . |
| 2:00 PM | Leaves the library and stands near the Ice Cream Stand watching over Jas and Vincent . |
| 4:20 PM | Walks Vincent to 1 Willow Lane and says goodbye. |
| 5:50 PM | Walks Jas to Marnie's Ranch and says goodbye. |
| 6:30 PM | Returns to her trailer for the evening. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:00 AM | Leaves her trailer to meet up with Jas and Vincent near the town graveyard . |
| 12:00 PM | Walks Jas and Vincent to the playground north of town square and watches them play. |
| 5:00 PM | Walks Jas and Vincent back to town and drops them off in front of Emily and Haley's house . |
| 6:30 PM | Returns to her trailer for the evening. |

##### Winter

###### Winter 4

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up and moves around her trailer . |
| 11:30 AM | Walks from her trailer to Harvey's Clinic for her annual checkup. |
| 1:30 PM | Continues her checkup at the clinic . |
| 4:00 PM | Leaves the clinic and goes to sit by the bridge west from JojaMart . |
| 7:00 PM | Leaves town and returns to the trailer to do dishes. |
| 9:00 PM | Goes to bed in her room in the trailer for the evening. |

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Trailer is unlocked. Penny is in her bedroom. |
| 11:00 AM | Moves to the kitchen. |
| 1:00 PM | Does some dishes. |
| 3:00 PM | Sits on the couch, probably watching TV. |
| 4:00 PM | Attends the Night Market . |
| 11:50 PM | Goes to bed for the evening. |

###### Winter 9 and 23 (No player has 6 hearts with Penny or Sam )

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 9:00 AM | Wakes up and stands in her bedroom. |
| 11:00 AM | Walks to town and sits on the bridge near the Ice Cream Stand . |
| 4:00 PM | Returns from town to the trailer and does some dishes. |
| 6:40 PM | Goes to bed in her room in the trailer for the evening. |

###### Winter 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Sleeps in her bed in the trailer . |
| 8:00 AM | Leaves her trailer and goes outside to read near the town graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

###### Rain (Option 1)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom in the Trailer . |
| 11:00 AM | Moves to the kitchen. |
| 1:00 PM | Does some dishes. |
| 3:00 PM | Sits on the couch, probably watching TV. |
| 6:00 PM | Returns to her bedroom, reading by the bookshelf. |
| 9:00 PM | Goes to bed for the evening. |

###### Rain (Option 2)

| 时间 | 地点/行动 |
|------|------|
| 8:10 AM | Leaves the trailer and walks to the Museum to sit outside. |
| 12:00 PM | Goes inside the Museum to look at the bookshelves. |
| 4:00 PM | Leaves the Museum and returns to the trailer to watch some television. |
| 7:00 PM | Moves over to the sink in the trailer to do some dishes. |
| 9:00 PM | Goes to bed for the evening. |

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves her trailer and goes to the museum/library to tutor Jas and Vincent . |
| 2:00 PM | Leaves the library and stands near the Ice Cream Stand watching over Jas and Vincent . |
| 4:20 PM | Walks Vincent to 1 Willow Lane and says goodbye. |
| 5:50 PM | Walks Jas to Marnie's Ranch and says goodbye. |
| 6:30 PM | Returns to her trailer for the evening. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her room. |
| 10:00 AM | Leaves her trailer to meet up with Jas and Vincent near the town graveyard . |
| 12:00 PM | Walks Jas and Vincent to the playground north of town square and watches them play. |
| 5:00 PM | Walks Jas and Vincent back to town and drops them off in front of Emily and Haley's house . |
| 8:50 PM | Returns to her trailer for the evening. |

###### Community Center Restored

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up and moves around her trailer . |
| 10:30 AM | Leaves her trailer and walks to the Community Center to read. |
| 3:00 PM | Continues moving around the Community Center . |
| 6:00 PM | Leaves the Community Center and returns to the trailer to do dishes. |
| 9:00 PM | Goes to bed in her room in the trailer for the evening. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Leaves her trailer and goes outside to read near the Graveyard . |
| 12:30 PM | Returns to the trailer to wash dishes. |
| 4:00 PM | Leaves the trailer again to go outside the saloon where she sits on a bench with Maru . |
| 6:40 PM | Returns to her trailer for the evening. |

##### Marriage

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:30 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:00 AM | Stands near the Calico warp statue. |
| 1:00 AM | Boards the bus back to the Valley. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves the farmhouse and heads to Pierre's General Store . |
| 11:30 AM | Leaves Pierre's. In town, reading. |
| 4:00 PM | Sitting in town. |
| 6:10 PM | Leaves town to return home to the farm. |
| 10:00 PM | Goes to bed |

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves the the farm and walks to the Museum . |
| 2:00 PM | Leaves the Museum and walks with Vincent and Jas to town . |
| 4:20 PM | In front of Haley and Emily 's house while walking Vincent and Jas home. |
| 5:50 PM | Walks Jas home to Marnie's Ranch in the woods west of town . |
| 6:30 PM | Leaves Marnie's Ranch and returns to home for the evening. |
| 8:10 PM | Arrives back at the Farmhouse . |
| 10:00 PM | Goes to bed. |

<a id="npc-schedule-caroline"></a>

### 13. 卡洛琳（Caroline）

> 来源：中文 revision 54977；英文 revision 191301
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 12 个分区、12 个条件分支、55 行。

- 姜岛 海滩度假村 修复后，卡洛琳偶尔会去度个假，18:00离开小岛后，卡洛琳将立即回家睡觉。卡洛琳不会在节日或诊所预约日当天去度假。
- 下面显示的是卡洛琳的行程表，从上到下优先级逐次下降，比如下雨时行程安排的优先级就会比它下面的高。如果是一个下雨的星期五，那么卡洛琳会按照下雨时的行程表行动。

##### 春季15日（巴士站已修复）

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:40 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:00 | 站在 村民商店 的东侧。 |
| 00:50 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 秋季25日

###### 秋季25日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 10:00 | 离开厨房前往她的卧室。 |
| 12:00 | 前往 哈维的诊所 ，然后站在候诊室中。 |
| 13:30 | 走到诊所里靠左边的检查室。 |
| 16:00 | 回家然后待在客厅里。 |
| 21:00 | 上床睡觉。 |

##### 冬季16日

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 12:00 | 走到杂货店的货架之间。 |
| 13:30 | 出门前往小镇广场。 |
| 16:00 | 离开小镇广场前往 夜市 。 |
| 23:30 | 离开夜市回家。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 在 家 里的客厅。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 12:00 | 走到杂货店的货架之间。 |
| 13:30 | 前往她的卧室并站在书架旁边看书。 |
| 16:00 | 离开卧室前往客厅。 |
| 21:00 | 上床睡觉。 |

##### 星期二

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 站在家里客厅最上面的桌子旁边。 |
| 10:30 | 走到客厅中间。 |
| 13:00 | 在客厅和其他有氧健身俱乐部的成员一起健身。 |
| 16:00 | 结束健身，待在客厅里和其他人聊天。 |
| 18:10 | 前往厨房吃点零食。 |
| 21:00 | 上床睡觉。 |

##### 星期三

###### 星期三

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 10:00 | 前往家里的日光房，站在茶苗旁边。 |
| 12:00 | 出门前往 社区中心 左边的喷泉。 |
| 17:00 | 回家站在客厅里。 |
| 21:00 | 上床睡觉。 |

##### 星期五

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 10:00 | 前往家里的日光房，站在茶苗旁边。 |
| 12:00 | 出门前往 博物馆 看书。 |
| 17:00 | 回家待在客厅中。 |
| 21:00 | 上床睡觉。 |

##### 星期六（社区中心已修复）

###### 星期六（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 11:00 | 出门前往 社区中心 ，然后待在大厅的书架旁边看书。 |
| 17:00 | 回家站在客厅里。 |
| 21:00 | 上床睡觉。 |

##### 星期天

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 站在她的卧室里。 |
| 10:40 | 在卧室的书架旁边看书。 |
| 13:30 | 走到杂货店的货架之间。 |
| 14:40 | 出门前往 社区中心 南边的树下。 |
| 18:30 | 回家站在她的卧室里。 |
| 21:00 | 上床睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在 家 中厨房。 |
| 10:00 | 前往家里的日光房，站在茶苗旁边。 |
| 12:00 | 走到杂货店的货架之间。 |
| 13:30 | 出门，和 乔迪 一起站在小镇广场。 |
| 16:00 | 回家站在客厅里。 |
| 21:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 12 个分区、12 个条件分支、55 行。

- After the Beach Resort on Ginger Island is unlocked, Caroline may randomly spend the day there. After leaving the Island at 6pm, Caroline will immediately go home to bed. Caroline never visits the Resort on Festival days or her checkup day at Harvey's Clinic .
- Shown below is Caroline's schedule, prioritized from the top down. For example, if it is raining, that schedule overrides all schedules below it.

##### Spring 15 (Bus Service Restored)

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:40 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:00 AM | Stands east of the villager shops. |
| 12:50 AM | Boards bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

##### Fall 25

###### Fall 25

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 10:00 AM | Leaves the kitchen, walks to her bedroom. |
| 12:00 PM | Walks to Harvey's Clinic and stands in waiting room. |
| 1:30 PM | Moves to the left examination room in Harvey's Clinic. |
| 4:00 PM | Returns home and stands in her living room. |
| 9:00 PM | Goes to bed. |

##### Winter 16

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 12:00 PM | Walks to an aisle of the general store. |
| 1:30 PM | Goes to stand in the town square . |
| 4:00 PM | Leaves the town square to attend the Night Market . |
| 11:30 PM | Leaves the Night Market to return home and sleep. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the living room . |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 12:00 PM | Walks to an aisle of the general store. |
| 1:30 PM | Walks to her bedroom and reads next to her bookcase. |
| 4:00 PM | Leaves bedroom to stand in the living room. |
| 9:00 PM | Goes to bed. |

##### Tuesday

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In her living room, near the uppermost dresser. |
| 10:30 AM | Moves more towards the middle of the living room. |
| 1:00 PM | Caroline exercises with the Aerobics class in her living room. |
| 4:00 PM | Aerobics class ends, she stands in the living room chatting. |
| 6:10 PM | Walks to kitchen and eats some cookies. |
| 9:00 PM | Goes to bed. |

##### Wednesday

###### Wednesday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 10:00 AM | In her sunroom, near her tea sapling. |
| 12:00 PM | Walks to the fountain to the west of the Community Center . |
| 5:00 PM | Returns home and stands in her living room. |
| 9:00 PM | Goes to bed. |

##### Friday

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 10:00 AM | In her sunroom, near her tea sapling. |
| 12:00 PM | Goes to the Museum to read between some bookshelves. |
| 5:00 PM | Returns home and stands in her living room. |
| 9:00 PM | Goes to bed. |

##### Saturday (Community Center Restored)

###### Saturday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 11:00 AM | Walks to Community Center and stands in the reading area in the main room. |
| 5:00 PM | Returns home and stands in her living room. |
| 9:00 PM | Goes to bed. |

##### Sunday

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Stands in her bedroom. |
| 10:40 AM | Moves one space over to stand in front of her bookshelf. |
| 1:30 PM | Walks to an aisle of the general store. |
| 2:40 PM | Leaves home to stand below the tree south of the Community Center . |
| 6:30 PM | Returns home to stand in her bedroom. |
| 9:00 PM | Goes to bed. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen of Pierre's General Store . |
| 10:00 AM | In her sunroom, near her tea sapling. |
| 12:00 PM | Walks to an aisle of the general store. |
| 1:30 PM | Leaves home to stand in town square with Jodi. |
| 4:00 PM | Returns home and stands in her living room. |
| 9:00 PM | Goes to bed. |

<a id="npc-schedule-clint"></a>

### 14. 克林特（Clint）

> 来源：中文 revision 55070；英文 revision 191347
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 8 个分区、8 个条件分支、28 行。

- 在重建 社区中心 后，克林特每个星期五都会离开铁匠铺，从而无法让玩家购物，升级工具或是破开晶石，除非星期五下雨。
- 姜岛的海滩度假村 解锁后，克林特有时会在星期五去那儿度假。18:00离开姜岛后，克林特会立即回家上床睡觉。克林特不会在冬季16日（他的体检日）或节日当天去姜岛。
- 以下是克林特的日程安排，优先度从高到低排序。例如，如果当天下雨，雨天的时间表会比它下方的优先级更高。

##### 春季16日（巴士站已修复）

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:40 | 站在 绿洲 的东侧。 |
| 01:30 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 冬季15日

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 08:50 | 在 铁匠铺 的柜台后面。 |
| 17:00 | 离开铁匠铺，参加 夜市 。 |
| 00:00 | 回铁匠铺睡觉。 |

##### 冬季16日

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在 铁匠铺 的柜台后面。 |
| 10:30 | 离开 铁匠铺 前往 诊所 ，到达后在候诊室等候。 |
| 13:30 | 在左侧的检查室做年度体检。 |
| 16:00 | 离开 诊所 ，前往 星之果实酒吧 。 |
| 00:00 | 回铁匠铺睡觉。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 离开 铁匠铺 前往 星之果实酒吧 。 |
| 07:20 | 在 星之果实酒吧 内。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在 铁匠铺 的柜台后面。 |
| 17:00 | 到铁砧旁工作。 |
| 19:00 | 离开 铁匠铺 前往 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 ，回家睡觉。 |

##### 星期五（社区中心已修复）

###### 星期五（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:50 | 出门到 社区中心 的锅炉房去。 |
| 17:00 | 离开 社区中心 前往 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 ，回家睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在 铁匠铺 的柜台后面。 |
| 17:00 | 到铁砧旁工作。 |
| 19:00 | 离开 铁匠铺 前往 星之果实酒吧 。 |
| 20:20 | 到达 星之果实酒吧 。 |
| 00:00 | 离开 星之果实酒吧 ，回家睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个分区、8 个条件分支、28 行。

- Clint is unavailable for shopping, tool upgrades, or geode processing on Fridays after the Community Center is restored, unless it is raining.
- After the Beach Resort on Ginger Island is unlocked, Clint may randomly spend Friday there. After leaving the Island at 6pm, Clint will immediately go home to bed.
- Shown below are Clint's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring 16 (Bus Service Restored)

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:40 AM | Stands east of the Oasis . |
| 1:30 AM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Winter 15

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 8:50 AM | Behind the counter of the Blacksmith . |
| 5:00 PM | Leaves the Blacksmith to attend the Night Market . |
| 12:00 AM | Returns to the Blacksmith to sleep. |

##### Winter 16

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Behind the counter of the Blacksmith . |
| 10:30 AM | Leaves the Blacksmith to go to the waiting room of Harvey's Clinic . |
| 1:30 PM | Moves to the left examination room in the Clinic. |
| 4:00 PM | Leaves the Clinic for The Saloon . |
| 12:00 AM | Returns home to sleep. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Leaves home and heads to the Saloon . |
| 7:20 AM | In the Saloon. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Behind the counter of the Blacksmith . |
| 5:00 PM | Moves to work on the anvil. |
| 7:00 PM | Heads to The Saloon . |
| 12:00 AM | Returns home to sleep. |

##### Friday (Community Center Restored)

###### Friday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:50 AM | Leaves home, heads to the Community Center Boiler Room. |
| 5:00 PM | Leaves the Community Center and heads to The Saloon . |
| 12:00 AM | Returns home to sleep. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Behind the counter of the Blacksmith . |
| 5:00 PM | Moves to work on the anvil. |
| 7:00 PM | Heads to The Saloon . |
| 8:20 PM | In the Saloon. |
| 12:00 AM | Returns home to sleep. |

<a id="npc-schedule-demetrius"></a>

### 15. 德米特里厄斯（Demetrius）

> 来源：中文 revision 54996；英文 revision 193879
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 4 个分区、17 个条件分支、97 行。

- 姜岛 海滩度假村修复后，德米特里厄斯偶尔会去度个假，直到18:00离开回家睡觉，德米特里厄斯不会在他体检日（夏季25日）和节日当天去度假。
- 下面显示的是德米特里厄斯在每个季节中优先级从高到低的日程表。例如，如果下雨，那么此日程就将覆盖其下的所有日程。

##### 春季

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:30 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:40 | 站在厨师处。 |
| 01:20 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室中看报纸。 |
| 11:00 | 在实验室显微镜下做笔记。 |
| 15:00 | 站在 木匠的商店 柜台后面，接近罗宾。 |
| 15:40 | 回到实验室显微镜下做笔记。 |
| 18:00 | 走进厨房，站在冰箱前。 |
| 19:20 | 站在厨房的火炉前。 |
| 20:00 | 来到自己的卧室，站在书架旁。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室显微镜下做笔记。 |
| 16:00 | 前往 星之果实酒吧 。 |
| 17:50 | 位于 星之果实酒吧 ，站在 罗宾 旁边。 |
| 19:20 | 在酒吧和 罗宾 跳舞。 |
| 21:00 | 离开酒吧，回家睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，站在厨房的水槽前。 |
| 11:00 | 实验室显微镜下做笔记。 |
| 14:30 | 出门，站在 木匠的商店 车库旁边的盆栽附近。 |
| 15:30 | 站在 木匠的商店 东南方向的悬崖边。 |
| 19:00 | 回到家里，走进厨房，站在冰箱前。 |
| 20:40 | 站在厨房的火炉前。 |
| 21:00 | 来到自己的卧室，站在书架旁。 |
| 22:30 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 站在 木匠的商店 东边附近的灌木丛中采集样本。 |

###### 夏季25日

| 时间 | 地点/行动 |
|------|------|
| 08:40 | 离开 家 ，前往 哈维的诊所 。 |
| 13:30 | 走到诊所左侧的检查室。 |
| 16:00 | 离开诊所回家，站在他卧室的书架旁边。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室中看报纸。 |
| 11:00 | 在实验室显微镜下做笔记。 |
| 15:00 | 站在 木匠的商店 柜台后面，接近罗宾。 |
| 15:40 | 回到实验室显微镜下做笔记。 |
| 18:00 | 走进厨房，站在冰箱前。 |
| 19:20 | 站在厨房的火炉前。 |
| 20:00 | 来到自己的卧室，站在书架旁。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室显微镜下做笔记。 |
| 16:00 | 前往 星之果实酒吧 。 |
| 17:50 | 位于 星之果实酒吧 ，站在 罗宾 旁边。 |
| 19:20 | 在酒吧和 罗宾 跳舞。 |
| 21:00 | 离开酒吧，回家睡觉。 |
| 22:40 | 和 罗宾 一起到家。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，站在厨房的水槽前。 |
| 11:00 | 前往 社区中心 西侧的喷泉。 |
| 19:00 | 回到家里，走进厨房，站在冰箱前。 |
| 20:40 | 站在厨房的火炉前。 |
| 21:00 | 来到自己的卧室，站在书架旁。 |
| 22:30 | 上床睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室中看报纸。 |
| 11:00 | 在实验室显微镜下做笔记。 |
| 15:00 | 站在 木匠的商店 柜台后面，接近罗宾。 |
| 15:40 | 回到实验室显微镜下做笔记。 |
| 18:00 | 走进厨房，站在冰箱前。 |
| 19:20 | 站在厨房的火炉前。 |
| 20:00 | 来到自己的卧室，站在书架旁。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室显微镜下做笔记。 |
| 16:00 | 前往 星之果实酒吧 。 |
| 17:50 | 位于 星之果实酒吧 ，站在 罗宾 旁边。 |
| 19:20 | 在酒吧和 罗宾 跳舞。 |
| 21:00 | 离开酒吧，回家睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，站在厨房的水槽前。 |
| 11:00 | 出门，前往湖泊北部靠近桥梁的地方，做笔记。 |
| 19:00 | 回到家里，走进厨房，站在冰箱前。 |
| 20:40 | 站在厨房的火炉前。 |
| 21:00 | 来到自己的卧室，站在书架旁。 |
| 22:30 | 上床睡觉。 |

##### 冬季

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室中看报纸。 |
| 11:00 | 在实验室显微镜下做笔记。 |
| 15:00 | 站在 木匠的商店 柜台后面，接近罗宾。 |
| 15:40 | 离开家，参加 夜市 。 |
| 23:30 | 离开夜市，回家睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室中看报纸。 |
| 11:00 | 在实验室显微镜下做笔记。 |
| 15:00 | 站在 木匠的商店 柜台后面，接近罗宾。 |
| 15:40 | 回到实验室显微镜下做笔记。 |
| 18:00 | 走进厨房，站在冰箱前。 |
| 19:20 | 站在厨房的火炉前。 |
| 20:00 | 来到自己的卧室，站在书架旁。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室显微镜下做笔记。 |
| 16:00 | 前往 星之果实酒吧 。 |
| 17:50 | 位于 星之果实酒吧 ，站在 罗宾 旁边。 |
| 19:20 | 在酒吧和 罗宾 跳舞。 |
| 21:00 | 离开酒吧，回家睡觉。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:50 | 在 家 里，实验室中看报纸。 |
| 11:00 | 在实验室显微镜下做笔记。 |
| 15:00 | 站在 木匠的商店 柜台后面，接近罗宾。 |
| 15:40 | 回到实验室显微镜下做笔记。 |
| 18:00 | 走进厨房，站在冰箱前。 |
| 19:20 | 站在厨房的火炉前。 |
| 20:00 | 来到自己的卧室，站在书架旁。 |
| 22:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个分区、17 个条件分支、97 行。

- After the Beach Resort on Ginger Island is unlocked, Demetrius may randomly spend the day there. After leaving the Island at 6pm, Demetrius will immediately go home to bed. Demetrius never visits the Resort on Festival days or his checkup day at Harvey's Clinic .
- Shown below are Demetrius' schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:30 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:40 AM | Stands by the chef stand. |
| 1:20 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | In his Home , reading a newspaper in the laboratory. |
| 11:00 AM | Taking notes at the microscope. |
| 3:00 PM | Behind the counter of the Carpenter's Shop in the entryway. |
| 3:40 PM | Moves back to the microscope in the laboratory. |
| 6:00 PM | Stands in front of the fridge in his kitchen. |
| 7:20 PM | Stands in front of the stove in his kitchen. |
| 8:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , taking notes at the microscope. |
| 4:00 PM | Heads to The Saloon. |
| 5:50 PM | In The Saloon standing next to Robin . |
| 7:20 PM | Dances with Robin in the Saloon. |
| 9:00 PM | Heads home from the Saloon to sleep. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , standing in front of the sink in his kitchen. |
| 11:00 AM | Taking notes at the microscope. |
| 2:30 PM | Stands outside, next to the potted plant next to his garage. |
| 3:30 PM | Stands at the cliff southeast of his house. |
| 7:00 PM | Goes inside and stands in front of the fridge in his kitchen. |
| 8:40 PM | Stands in front of the stove in his kitchen. |
| 9:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:30 PM | Goes to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | Collects samples at a bush near his house. |

###### Summer 25

| 时间 | 地点/行动 |
|------|------|
| 08:40 AM | Leaves home for the Clinic . |
| 1:30 PM | Moves to the left examination room in the Clinic. |
| 4:00 PM | Leaves the Clinic to go home and stand next to the bookcase in his bedroom. |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | In his Home , reading a newspaper in the laboratory. |
| 11:00 AM | Taking notes at the microscope. |
| 3:00 PM | Behind the counter of the Carpenter's Shop in the entryway. |
| 3:40 PM | Moves back to the microscope in the laboratory. |
| 6:00 PM | Stands in front of the fridge in his kitchen. |
| 7:20 PM | Stands in front of the stove in his kitchen. |
| 8:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , taking notes at the microscope. |
| 4:00 PM | Heads to The Saloon. |
| 5:50 PM | In The Saloon standing next to Robin . |
| 7:20 PM | Dances with Robin in the Saloon. |
| 9:00 PM | Heads home from the Saloon to sleep. |
| 10:40 PM | Arrives home with Robin . |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , standing in front of the sink in his kitchen. |
| 11:00 AM | Goes to the fountain west of the Community Center. |
| 7:00 PM | Heads home to stand in front of the fridge in his kitchen. |
| 8:40 PM | Stands in front of the stove in his kitchen. |
| 9:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:30 PM | Goes to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | In his Home , reading a newspaper in the laboratory. |
| 11:00 AM | Taking notes at the microscope. |
| 3:00 PM | Behind the counter of the Carpenter's Shop in the entryway. |
| 3:40 PM | Moves back to the microscope in the laboratory. |
| 6:00 PM | Stands in front of the fridge in his kitchen. |
| 7:20 PM | Stands in front of the stove in his kitchen. |
| 8:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , taking notes at the microscope. |
| 4:00 PM | Heads to The Saloon. |
| 5:50 PM | In The Saloon standing next to Robin . |
| 7:20 PM | Dances with Robin in the Saloon. |
| 9:00 PM | Heads home from the Saloon to sleep. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , standing in front of the sink in his kitchen. |
| 11:00 AM | Heads outside to take notes by the northern end of the lake. |
| 7:00 PM | Heads home to stand in front of the fridge in his kitchen. |
| 8:40 PM | Stands in front of the stove in his kitchen. |
| 9:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:30 PM | Goes to bed. |

##### Winter

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | In his Home , reading a newspaper in the laboratory. |
| 11:00 AM | Taking notes at the microscope. |
| 3:00 PM | Behind the counter of the Carpenter's Shop in the entryway. |
| 3:40 PM | Leaves home to attend the Night Market. |
| 11:30 PM | Leaves Night Market to return home and sleep. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | In his Home , reading a newspaper in the laboratory. |
| 11:00 AM | Taking notes at the microscope. |
| 3:00 PM | Behind the counter of the Carpenter's Shop in the entryway. |
| 3:40 PM | Moves back to the microscope in the laboratory. |
| 6:00 PM | Stands in front of the fridge in his kitchen. |
| 7:20 PM | Stands in front of the stove in his kitchen. |
| 8:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:00 PM | Goes to bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | At home , taking notes at the microscope. |
| 4:00 PM | Heads to The Saloon. |
| 5:50 PM | In The Saloon standing next to Robin . |
| 7:20 PM | Dances with Robin in the Saloon. |
| 9:00 PM | Heads home from the Saloon to sleep. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:50 AM | In his Home , reading a newspaper in the laboratory. |
| 11:00 AM | Taking notes at the microscope. |
| 3:00 PM | Behind the counter of the Carpenter's Shop in the entryway. |
| 3:40 PM | Moves back to the microscope in the laboratory. |
| 6:00 PM | Stands in front of the fridge in his kitchen. |
| 7:20 PM | Stands in front of the stove in his kitchen. |
| 8:00 PM | Stands next to the bookshelf in his bedroom. |
| 10:00 PM | Goes to bed. |

<a id="npc-schedule-dwarf"></a>

### 16. 矮人（Dwarf）

> 来源：中文 revision 54688；英文 revision 191010
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 0 个分区、0 个条件分支、0 行。

- 矮人会一直呆在 矿井 中，就在入口的东边。他自称晚上有时会出去偷东西吃，但实际上不会移动。

源页没有分时表；以上文字即该源的完整日程说明。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 0 个分区、0 个条件分支、0 行。

- The Dwarf lives just to the east of the entrance to the mines and does not move from there.

源页没有分时表；以上文字即该源的完整日程说明。

<a id="npc-schedule-evelyn"></a>

### 17. 艾芙琳（Evelyn）

> 来源：中文 revision 54548；英文 revision 191129
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 10 个分区、10 个条件分支、51 行。

- 艾芙琳常常待在家中的厨房里，或者在照料镇中心的花园。
- 每个季节的第2天，她都会去 哈维的诊所 体检。每个季节的第23天，她会陪乔治一起去体检。艾芙琳不会去姜岛的 海滩度假村 。
- 下面显示的是艾芙琳的日程表，从上到下按优先顺序排列。例如，如果下雨，那么此日程就将覆盖其下的所有日程。

##### 春季17日（巴士站已修复）

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:50 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:00 | 与 乔治 一同在靠近巴士的路边。 |
| 22:50 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 站在厨房里。 |

##### 每个季节的第2天（星期二）

###### 每个季节的第2天（星期二）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:30 | 离开家，前往 哈维的诊所 的候诊室。 |
| 13:30 | 走到诊所里靠左边的检查室。 |
| 16:00 | 离开诊所，回到家里的厨房。 |
| 19:00 | 走到她家客厅的书架前。 |
| 21:30 | 去卧室睡觉。 |

##### 每个季节的第23天（星期二）

###### 每个季节的第23天（星期二）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:40 | 和 乔治 一起离开家，前往 哈维的诊所 的候诊室。 |
| 13:30 | 和乔治一起前往检查室。 |
| 16:10 | 离开诊所，回到家里的厨房。 |
| 19:00 | 走到她家客厅的书架前。 |
| 21:30 | 去卧室睡觉。 |

##### 冬季17日

###### 冬季17日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:40 | 陪乔治看电视。 |
| 12:10 | 站在餐桌旁。 |
| 13:00 | 在家里坐着。 |
| 16:30 | 到达 夜市 。 |
| 23:40 | 回到卧室。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:40 | 陪乔治看电视。 |
| 12:10 | 站在餐桌旁。 |
| 16:30 | 站在厨房电器旁。 |
| 19:00 | 走到她家客厅的书架前。 |
| 21:30 | 去卧室睡觉。 |

##### 星期一、星期四和星期六（社区中心已修复）

###### 星期一、星期四和星期六（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:40 | 陪乔治看电视。 |
| 12:10 | 前往社区中心，坐在工艺室的扶手椅上。 |
| 16:30 | 回家，站在厨房电器旁。 |
| 19:00 | 走到她家客厅的书架前。 |
| 21:30 | 去卧室睡觉。 |

##### 夏季日常时间表

###### 夏季日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:40 | 陪乔治看电视。 |
| 12:10 | 站在餐桌旁。 |
| 13:00 | 前去照料小镇广场西北方的盆栽。 |
| 16:30 | 站在厨房电器旁。 |
| 19:00 | 走到她家客厅的书架前。 |
| 21:30 | 去卧室睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家中的厨房。 |
| 10:40 | 陪乔治看电视。 |
| 12:10 | 站在餐桌旁。 |
| 13:00 | 前去照料小镇广场东南方的盆栽。 |
| 16:30 | 站在厨房电器旁。 |
| 19:00 | 走到她家客厅的书架前。 |
| 21:30 | 去卧室睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 10 个分区、10 个条件分支、51 行。

- She can usually be found in her home's kitchen or tending to the gardens in the center of town. On the 2nd of every season, she has an appointment at the clinic , and on the 23rd of every season she accompanies George to his appointment. Evelyn never visits the Beach Resort on Ginger Island.
- Shown below are Evelyn's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring 17 (Bus Service Restored)

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:50 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:00 AM | With George , at the roadside near the bus. |
| 10:50 PM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | Standing in her kitchen. |

##### Tuesday the 2nd

###### Tuesday the 2nd

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:30 AM | Leaves home to sit in the waiting room of Harvey's clinic. |
| 1:30 PM | Moves to the left examination room. |
| 4:00 PM | Returns home from the clinic to stand in her kitchen. |
| 7:00 PM | Moves to stand in front of the bookcase in her living room. |
| 9:30 PM | Goes to her bedroom. |

##### Tuesday the 23rd

###### Tuesday the 23rd

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:40 AM | Leaves home to wait in Harvey's clinic with George. |
| 1:30 PM | Moves to the left examination room with George. |
| 4:10 PM | Returns home from the clinic to stand in her kitchen. |
| 7:00 PM | Moves to stand in front of the bookcase in her living room. |
| 9:30 PM | Goes to her bedroom. |

##### Winter 17

###### Winter 17

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:40 AM | Stands next to the TV with George. |
| 12:10 PM | Stands at her kitchen table. |
| 1:00 PM | Sits in her house. |
| 4:30 PM | Arrives at the Night Market . |
| 11:40 PM | Arrives in her bedroom. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:40 AM | Stands next to the TV with George. |
| 12:10 PM | Stands at her kitchen table. |
| 4:30 PM | Stands in her kitchen, near the appliances. |
| 7:00 PM | Moves to stand in front of the bookcase in her living room. |
| 9:30 PM | Goes to her bedroom. |

##### Monday, Thursday and Saturday (Community Center Restored)

###### Monday, Thursday and Saturday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:40 AM | Stands next to the TV with George. |
| 12:10 PM | Heads to the community center to sit in the armchair in the crafts room. |
| 4:30 PM | Stands in her kitchen, near the appliances. |
| 7:00 PM | Moves to stand in front of the bookcase in her living room. |
| 9:30 PM | Goes to her bedroom. |

##### Summer

###### Summer

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:40 AM | Stands next to the TV with George. |
| 12:10 PM | Stands at her kitchen table. |
| 1:00 PM | Goes to tend the plants just northwest of town square. |
| 4:30 PM | Stands in her kitchen, near the appliances. |
| 7:00 PM | Moves to stand in front of the bookcase in her living room. |
| 9:30 PM | Goes to her bedroom. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Standing in her kitchen. |
| 10:40 AM | Stands next to the TV with George. |
| 12:10 PM | Stands at her kitchen table. |
| 1:00 PM | Goes to tend the plants just southeast of town square. |
| 4:30 PM | Stands in her kitchen, near the appliances. |
| 7:00 PM | Moves to stand in front of the bookcase in her living room. |
| 9:30 PM | Goes to her bedroom. |

<a id="npc-schedule-george"></a>

### 18. 乔治（George）

> 来源：中文 revision 54046；英文 revision 193909
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 10 个分区、10 个条件分支、36 行。

- 下面显示的是乔治的日程表，从上到下按优先顺序排列。例如，如果下雨，那么此日程就将覆盖其下的所有日程。
- 每个季节第23天，乔治都会和 艾芙琳 一起去 哈维的诊所 体检。乔治不会去姜岛的 海滩度假村 。

##### 春季17日（巴士站已修复）

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:50 | 与 艾芙琳 一同在靠近巴士的路边。 |
| 22:50 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 冬季17日

###### 冬季17日

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家看电视。 |
| 12:00 | 在家里厨房的餐桌旁边。 |
| 16:20 | 离开家前往 夜市 。 |
| 23:40 | 离开夜市回家。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于厨房。 |

##### 每个季节的23日（星期二）

###### 每个季节的23日（星期二）

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家里厨房的餐桌旁边。 |
| 10:30 | 离开家前往 哈维的诊所 的候诊室。 |
| 13:30 | 前往诊所里靠左边的检查室。 |
| 16:00 | 离开诊所回家看电视。 |
| 20:00 | 回到他的卧室睡觉。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家看电视。 |
| 12:00 | 在家里厨房的餐桌旁边。 |
| 15:00 | 再次回去看电视。 |
| 20:00 | 回到他的卧室睡觉。 |

##### 夏季的星期五

###### 夏季的星期五

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家看电视。 |
| 12:00 | 离开家待在家旁边的的树下面。 |
| 15:00 | 回家看电视。 |
| 20:00 | 回到他的卧室睡觉。 |

##### 星期天（已触发 亚历克斯 14心事件）

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家看电视。 |
| 11:00 | 前往 星之果实酒吧 的里屋看体育比赛。 |
| 15:00 | 回家看电视。 |
| 20:00 | 回到他的卧室睡觉。 |

##### 星期天

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家看电视。 |
| 10:00 | 离开家前往 皮埃尔 家中的 由巴 祭坛处。 |
| 14:00 | 离开 由巴 祭坛回家继续看电视。 |
| 20:00 | 回到他的卧室睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 在家看电视。 |
| 12:00 | 在家里厨房的餐桌旁边。 |
| 15:00 | 继续去看电视。 |
| 20:00 | 回到他的卧室睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 10 个分区、10 个条件分支、36 行。

- The 23rd of every season, George has an appointment at Harvey's Clinic , accompanied by Evelyn . George never visits the Beach Resort on Ginger Island.
- Shown below are George's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring 17 (Bus Service Restored)

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 9:50 AM | With Evelyn , at the roadside near the bus. |
| 10:50 PM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Winter 17

###### Winter 17

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, watching TV. |
| 12:00 PM | At his kitchen table. |
| 4:20 PM | Leaves home to attend the Night Market . |
| 11:40 PM | Leaves the Night Market to return home. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the kitchen. |

##### Tuesday the 23rd (All Seasons)

###### Tuesday the 23rd (All Seasons)

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, at the kitchen table. |
| 10:30 AM | Leaves home for the waiting room of Harvey's Clinic . |
| 1:30 PM | Moves to the left exam room inside the Clinic. |
| 4:00 PM | Leaves the Clinic to watch TV at home. |
| 8:00 PM | Goes to his bedroom for the night. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, watching TV. |
| 12:00 PM | At his kitchen table. |
| 3:00 PM | Goes to watch TV again. |
| 8:00 PM | Goes to his bedroom for the night. |

##### Summer Friday

###### Summer Friday

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, watching TV. |
| 12:00 PM | Leaves home to sit outside, under the tree west of his house. |
| 3:00 PM | Returns home to watch TV. |
| 8:00 PM | Goes to his bedroom for the night. |

##### Sunday (Alex's 14 heart event seen)

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, watching TV. |
| 11:00 AM | Heads to the back room of the Saloon to watch sports. |
| 3:00 PM | Returns home to watch TV. |
| 8:00 PM | Goes to his bedroom for the night. |

##### Sunday

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, watching TV. |
| 10:00 AM | Leaves home and heads for the Statue of Yoba inside Pierre 's home. |
| 2:00 PM | Leaves the Statue of Yoba and heads home to watch TV. |
| 8:00 PM | Goes to his bedroom for the night. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | At home, watching TV. |
| 12:00 PM | At his kitchen table. |
| 3:00 PM | Goes to watch TV again. |
| 8:00 PM | Goes to his bedroom for the night. |

<a id="npc-schedule-gus"></a>

### 19. 格斯（Gus）

> 来源：中文 revision 55267；英文 revision 191548
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 9 个分区、9 个条件分支、31 行。

- 在姜岛的 海滩度假村 解锁后，格斯可能会前往姜岛。他会在酒吧里留下一个钱箱，所以玩家仍然能够进行购买。18:00离开姜岛后，格斯会在酒吧工作到12:30分，然后去睡觉。在 节日 或 诊所 检查日，格斯不会前往姜岛。
- 以下是格斯的日程安排，优先度从高到低排序。如果当天下雨，雨天的时间表会比下方的优先级更高。

##### 春季15日（巴士站已修复）

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:50 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:10 | 站在 威利 的钓鱼挑战的钓鱼池旁。 |
| 00:50 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 站在 星之果实酒吧 的吧台前。 |

##### 秋季4日

###### 秋季4日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里，坐在沙发上。 |
| 10:30 | 前往 诊所 候诊室，看着一张海报。 |
| 13:30 | 移到诊所的左边检查室。 |
| 16:00 | 离开诊所，去打理酒吧。 |
| 00:00 | 去他的卧室睡觉。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里，坐在沙发上。 |
| 12:00 | 在吧台后面擦拭杯子。 |
| 16:30 | 停止擦拭杯子，打理吧台。 |
| 00:00 | 回到自己的卧室睡觉。 |

##### 星期一

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开家去 皮埃尔的杂货店 。 |
| 11:00 | 回到酒馆照看吧台。 |
| 00:00 | 回到自己的卧室睡觉。 |

##### 星期二（社区中心已修复）

###### 星期二（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里，坐在沙发上。 |
| 08:30 | 去 社区中心 的茶水间。 |
| 12:30 | 回到酒馆看管酒吧。 |
| 00:00 | 回到自己的卧室睡觉。 |

##### 星期天（已触发 亚历克斯 14心事件）

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里，坐在沙发上。 |
| 11:40 | 去酒馆的后厅。 |
| 15:00 | 去打理酒吧。 |
| 00:00 | 去他的卧室睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在他的房间里，坐在沙发上。 |
| 12:00 | 在吧台后面擦拭杯子。 |
| 16:30 | 停止擦拭杯子，打理吧台。 |
| 00:00 | 回到自己的卧室睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 9 个分区、9 个条件分支、31 行。

- After the Beach Resort on Ginger Island is unlocked, Gus may randomly spend the day there. (He will leave a cash box on the bar, so the player is still able to make purchases.) After leaving the Island at 6pm, Gus will tend bar until 12:30am, when he goes to bed. Gus never visits the Resort on Festival days or his checkup day at Harvey's Clinic .
- Shown below are Gus' schedules prioritized highest to lowest. For example, if he is a vendor at the Desert Festival, that schedule overrides all others.

##### Spring 15 (Bus Service Restored)

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:50 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:10 AM | Stands at the pond near Willy 's fishing challenge. |
| 12:50 AM | Boards bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Stands in front of the bar in the Stardrop Saloon . |

##### Fall 4

###### Fall 4

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room, sitting on the couch. |
| 10:30 AM | Heads to the Clinic waiting room and looks at a poster. |
| 1:30 PM | Moves to the left examination room in the clinic. |
| 4:00 PM | Leaves the clinic to go tend the bar. |
| 12:00 AM | Goes to his bedroom to sleep. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room, sitting on the couch. |
| 12:00 PM | Cleans glasses behind the bar. |
| 4:30 PM | Quits cleaning glasses and tends the bar. |
| 12:00 AM | Goes to his bedroom to sleep. |

##### Monday

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Leaves home to go to Pierre's General Store . |
| 11:00 AM | Returns to the Saloon to tend the bar. |
| 12:00 AM | Goes to his bedroom to sleep. |

##### Tuesday (Community Center Restored)

###### Tuesday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room, sitting on the couch. |
| 8:30 AM | Goes to the kitchen in the Community Center . |
| 12:30 PM | Returns to the Saloon to tend the bar. |
| 12:00 AM | Goes to his bedroom to sleep. |

##### Sunday (Alex's 14 heart event seen)

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room, sitting on the couch. |
| 11:40 AM | Goes to the backroom of the Saloon. |
| 3:00 PM | Goes to tend the bar. |
| 12:00 AM | Goes to his bedroom to sleep. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In his room, sitting on the couch. |
| 12:00 PM | Cleans glasses behind the bar. |
| 4:30 PM | Quits cleaning glasses and tends the bar. |
| 12:00 AM | Goes to his bedroom to sleep. |

<a id="npc-schedule-jas"></a>

### 20. 贾斯（Jas）

> 来源：中文 revision 55188；英文 revision 193899
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 11 个分区、11 个条件分支、46 行。

- 在 海滩度假村 解锁后，贾斯可能会前往姜岛。18:00离开姜岛后，贾斯会立刻回家睡觉。贾斯不会在星期二、星期三、星期五、 节日 或她的 诊所 预约日（冬季18日）前往度假村。贾斯也不会在没有成年人陪同的情况下前往度假村。
- 以下是贾斯的日程安排，优先度从高到低排序。（例如：如果当天下雨，雨天的日程安排会覆盖其下方的所有日程安排。）

##### 春季17日（巴士站已修复）

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:00 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:20 | 站在 村民商铺 的南侧。 |
| 11:30 | 下楼梯前往悬崖下，站在池塘北侧的一棵树下。 |
| 23:40 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 家 里的厨房。 |

##### 每个季节9日（星期二）和23日（星期二）

###### 每个季节9日（星期二）和23日（星期二）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室里。 |
| 11:00 | 离开家并前往玛妮的牧场西边的大树下跳绳。 |
| 15:00 | 回家，在商店的入口通道处读书。 |
| 19:00 | 回她的卧室。 |
| 21:00 | 睡觉。 |

##### 冬季15日

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室里。 |
| 11:00 | 离开家并前往玛妮的牧场西边的大树下跳绳。 |
| 14:50 | 离开森林去参加 夜市 。 |
| 23:00 | 离开夜市并回家。 |

##### 冬季18日

###### 冬季18日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室里。 |
| 10:30 | 离开家前往 哈维的诊所 。 |
| 13:30 | 移动到诊所的检查室。 |
| 16:00 | 离开诊所，在玛妮的牧场的入口通道处读书。 |
| 20:00 | 回到她的房间睡觉。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室里。 |
| 11:00 | 站在商店的入口通道处。 |
| 15:00 | 移动到壁炉房间读书。 |
| 19:00 | 回她的卧室。 |
| 21:00 | 睡觉。 |

##### 星期二、星期三、星期五

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 家 ，前往 博物馆 。 |
| 14:00 | 离开博物馆，站在博物馆西南方的河边。 |
| 16:20 | 离开河边，走到 艾米丽和海莉的房子 南边的小路上。 |
| 17:50 | 离开小镇并走回家睡觉。 |

##### 星期六

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 离开家，走去小镇，站在 柳巷2号 东边大树的西南方。 |
| 12:00 | 走向 社区中心 西边的游乐场并跳绳。 |
| 17:00 | 离开游乐场，站在 柳巷2号 的东南方。 |
| 20:00 | 走回家并睡觉。 |

##### 夏季

###### 夏季

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室里。 |
| 11:00 | 站在牧场外看着牛栏。 |
| 13:20 | 走去 沙滩 跳绳。 |
| 16:00 | 离开沙滩回家，在玛妮的牧场入口通道处读书。 |
| 19:00 | 回她的卧室。 |
| 21:00 | 睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在她的卧室里。 |
| 11:00 | 离开家并前往玛妮的牧场西边的大树下跳绳。 |
| 15:00 | 回家，在商店的入口通道处读书。 |
| 19:00 | 回她的卧室。 |
| 21:00 | 睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 11 个分区、11 个条件分支、46 行。

- After the Beach Resort on Ginger Island is unlocked, Jas may randomly spend the day there. After leaving the Island at 6pm, Jas will immediately go home to bed. Jas never visits the Resort on Tuesdays, Wednesdays, Fridays, Festival days or her checkup day at Harvey's Clinic . Jas also never visits the Resort without an adult accompanying her.
- Shown below are Jas' schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring 17 (Bus Service Restored)

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:00 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:20 AM | Stands south of the villager shops. |
| 11:30 AM | Takes the stairs down to the cliff and stands under a tree north of the pond. |
| 11:40 PM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the kitchen. |

##### Tuesday the 9th and Tuesday the 23rd

###### Tuesday the 9th and Tuesday the 23rd

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 11:00 AM | Leaves home to stand under the large tree west of Marnie's Ranch and jump rope. |
| 3:00 PM | Returns home, reads in the entryway of the shop. |
| 7:00 PM | Goes to her bedroom. |
| 9:00 PM | Goes to sleep. |

##### Winter 15

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 11:00 AM | Leaves home to stand under the large tree west of Marnie's Ranch and jump rope. |
| 2:50 PM | Leaves the forest to attend the Night Market . |
| 11:00 PM | Leaves the Night Market to return home. |

##### Winter 18

###### Winter 18

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 10:30 AM | Leaves home to go to Harvey's Clinic . |
| 1:30 PM | Moves to exam room inside Clinic. |
| 4:00 PM | Leaves Clinic, reads in the entryway of Marnie's Ranch. |
| 8:00 PM | Goes to her room to sleep. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 11:00 AM | Stands in the entryway of the shop. |
| 3:00 PM | Moves to the fireplace room to read. |
| 7:00 PM | Goes to her bedroom. |
| 9:00 PM | Goes to sleep. |

##### Tuesday, Wednesday and Friday

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves home to go to the Museum . |
| 2:00 PM | Leaves Museum, stands at river southwest of Museum. |
| 4:20 PM | Leaves riverbank, walks to path south of Emily and Haley's house . |
| 5:50 PM | Leaves town and walks home to go to sleep. |

##### Saturday

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves home, walks to town, stands southwest of the large tree that's east of 2 Willow Lane . |
| 12:00 PM | Walks to playground west of Community Center , jumps rope. |
| 5:00 PM | Leaves playground, stands southeast of 2 Willow Lane . |
| 8:00 PM | Walks home and goes to sleep. |

##### Summer

###### Summer

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 11:00 AM | Stands outside ranch looking at cow pen. |
| 1:20 PM | Walks to the Beach to jump rope. |
| 4:00 PM | Leaves beach to walk home, reads in the entryway of Marnie's Ranch. |
| 7:00 PM | Goes to her bedroom. |
| 9:00 PM | Goes to sleep. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In her bedroom. |
| 11:00 AM | Leaves home to stand under the large tree west of Marnie's Ranch and jump rope. |
| 3:00 PM | Returns home, reads in the entryway of the shop. |
| 7:00 PM | Goes to her bedroom. |
| 9:00 PM | Goes to sleep. |

<a id="npc-schedule-jodi"></a>

### 21. 乔迪（Jodi）

> 来源：中文 revision 55067；英文 revision 191546
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 4 个分区、34 个条件分支、210 行。

- 姜岛 海滩度假村 修复后，乔迪偶尔会去度个假，18:00离开小岛后，乔迪将立即回家睡觉。乔迪不会在节日或诊所预约日当天去度假。乔迪也不会在文森特的诊所预约日去度假。
- 下面显示的是乔迪在每个季节中优先级从高到低的日程表。例如，如果下雨，那么此日程就将覆盖其下的所有日程。

##### 春季

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:30 | 和 文森特 一起站在一家村民摊位的旁边。 |
| 00:10 | 乘坐巴士返回星露谷。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季11日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:30 | 前往 哈维的诊所 的候诊室。 |
| 13:30 | 前往左侧检查室。 |
| 16:00 | 前往文森特的房间。 |
| 20:00 | 前往客厅。 |
| 21:00 | 让文森特睡觉。 |
| 22:00 | 回房睡觉。 |

###### 春季18日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:30 | 前往 哈维的诊所 的候诊室。 |
| 13:30 | 前往左侧检查室。 |
| 16:00 | 返回厨房。 |
| 19:30 | 位于客厅。 |
| 21:00 | 让文森特睡觉。 |
| 22:00 | 回房睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:30 | 走到客厅。 |
| 16:00 | 位于厨房。 |
| 19:30 | 位于客厅。 |
| 21:00 | 让文森特睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:10 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 进入 皮埃尔的杂货店 。 |
| 11:30 | 站在皮埃尔家客厅的壁炉旁。 |
| 13:00 | 开始和 玛妮 、 卡洛琳 、 艾米丽 以及 罗宾 健身。 |
| 16:00 | 停止健身，和玛妮、卡洛琳、艾米丽以及罗宾一起站在壁炉旁。 |
| 18:20 | 离开皮埃尔的杂货店，回家。 |
| 19:10 | 到达自己家中。 |
| 21:10 | 让 文森特 睡觉。 |
| 22:00 | 离开文森特的房间，前往自己的卧室。 |
| 22:20 | 上床睡觉。 |

###### 星期三、星期五（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 到达 皮埃尔的杂货店 。 |
| 17:00 | 位于家里的厨房。 |
| 21:00 | 位于文森特的房间。 |
| 22:00 | 回房睡觉。 |

###### 星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 离开家，前往 Joja超市 。 |
| 12:50 | 到达 Joja超市 。 |
| 17:00 | 离开 Joja超市 ，回家。 |
| 18:30 | 站在家里的冰箱前面。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期六（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:00 | 离开家，前往社区中心，站在社区中心的大厅里。 |
| 17:00 | 回家，站在客厅。 |
| 21:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:00 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 到达皮埃尔的杂货店，走进客厅旁边的教堂。 |
| 16:00 | 离开 皮埃尔的杂货店 ，回家。 |
| 17:00 | 在家里的沙发上。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:30 | 坐在客厅里。 |
| 13:30 | 离开家，前往小镇广场。 |
| 16:00 | 离开广场，回家。 |
| 16:30 | 站在厨房里。 |
| 19:30 | 站在客厅里。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于客厅。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:30 | 走到客厅。 |
| 16:00 | 位于厨房。 |
| 19:30 | 位于客厅。 |
| 21:00 | 让文森特睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:10 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 进入 皮埃尔的杂货店 。 |
| 11:30 | 站在皮埃尔家客厅的壁炉旁。 |
| 13:00 | 开始和 玛妮 、 卡洛琳 、 艾米丽 以及 罗宾 健身。 |
| 16:00 | 停止健身，和玛妮、卡洛琳、艾米丽以及罗宾一起站在壁炉旁。 |
| 18:20 | 离开皮埃尔的杂货店，回家。 |
| 19:10 | 到达自己家中。 |
| 21:10 | 让 文森特 睡觉。 |
| 22:00 | 离开文森特的房间，前往自己的卧室。 |
| 22:20 | 上床睡觉。 |

###### 星期三、星期五（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 到达 皮埃尔的杂货店 。 |
| 17:00 | 位于家里的厨房。 |
| 21:00 | 位于文森特的房间。 |
| 22:00 | 回房睡觉。 |

###### 星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 离开家，前往 Joja超市 。 |
| 12:50 | 到达 Joja超市 。 |
| 17:00 | 离开 Joja超市 ，回家。 |
| 18:30 | 站在家里的冰箱前面。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期六（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:00 | 离开家，前往社区中心，站在社区中心的大厅里。 |
| 17:00 | 回家，站在客厅。 |
| 21:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:00 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 到达皮埃尔的杂货店，走进客厅旁边的教堂。 |
| 16:00 | 离开 皮埃尔的杂货店 ，回家。 |
| 17:00 | 在家里的沙发上。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:30 | 坐在客厅里。 |
| 13:30 | 离开家，前往小镇广场。 |
| 16:00 | 离开广场，回家。 |
| 16:30 | 站在厨房里。 |
| 19:30 | 站在客厅里。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

##### 秋季

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:30 | 走到客厅。 |
| 16:00 | 位于厨房。 |
| 19:30 | 位于客厅。 |
| 21:00 | 让文森特睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:10 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 进入 皮埃尔的杂货店 。 |
| 11:30 | 站在皮埃尔家客厅的壁炉旁。 |
| 13:00 | 开始和 玛妮 、 卡洛琳 、 艾米丽 以及 罗宾 健身。 |
| 16:00 | 停止健身，和玛妮、卡洛琳、艾米丽以及罗宾一起站在壁炉旁。 |
| 18:20 | 离开皮埃尔的杂货店，回家。 |
| 19:10 | 到达自己家中。 |
| 21:10 | 让 文森特 睡觉。 |
| 22:00 | 离开文森特的房间，前往自己的卧室。 |
| 22:20 | 上床睡觉。 |

###### 星期三、星期五（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 到达 皮埃尔的杂货店 。 |
| 17:00 | 位于家里的厨房。 |
| 21:00 | 位于文森特的房间。 |
| 22:00 | 回房睡觉。 |

###### 星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 离开家，前往 Joja超市 。 |
| 12:50 | 到达 Joja超市 。 |
| 17:00 | 离开 Joja超市 ，回家。 |
| 18:30 | 站在家里的冰箱前面。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期六（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:00 | 离开家，前往社区中心，站在社区中心的大厅里。 |
| 17:00 | 回家，站在客厅。 |
| 21:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:00 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 到达皮埃尔的杂货店，走进客厅旁边的教堂。 |
| 16:00 | 离开 皮埃尔的杂货店 ，回家。 |
| 17:00 | 在家里的沙发上。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:30 | 坐在客厅里。 |
| 13:30 | 离开家，前往小镇广场。 |
| 16:00 | 离开广场，回家。 |
| 16:30 | 站在厨房里。 |
| 19:30 | 站在客厅里。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

##### 冬季

###### 冬季17日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:40 | 坐在客厅的蓝色沙发上。 |
| 14:00 | 站在 柳巷1号 的东北方。 |
| 16:30 | 参加 夜市 。 |
| 23:30 | 回家。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:30 | 走到客厅。 |
| 16:00 | 位于厨房。 |
| 19:30 | 位于客厅。 |
| 21:00 | 让文森特睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:10 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 进入 皮埃尔的杂货店 。 |
| 11:30 | 站在皮埃尔家客厅的壁炉旁。 |
| 13:00 | 开始和 玛妮 、 卡洛琳 、 艾米丽 以及 罗宾 健身。 |
| 16:00 | 停止健身，和玛妮、卡洛琳、艾米丽以及罗宾一起站在壁炉旁。 |
| 18:20 | 离开皮埃尔的杂货店，回家。 |
| 19:10 | 到达自己家中。 |
| 21:10 | 让 文森特 睡觉。 |
| 22:00 | 离开文森特的房间，前往自己的卧室。 |
| 22:20 | 上床睡觉。 |

###### 星期三、星期五（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 到达 皮埃尔的杂货店 。 |
| 17:00 | 位于家里的厨房。 |
| 21:00 | 位于文森特的房间。 |
| 22:00 | 回房睡觉。 |

###### 星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:00 | 离开家，前往 Joja超市 。 |
| 12:50 | 到达 Joja超市 。 |
| 17:00 | 离开 Joja超市 ，回家。 |
| 18:30 | 站在家里的冰箱前面。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

###### 星期六（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:00 | 离开家，前往社区中心，站在社区中心的大厅里。 |
| 17:00 | 回家，站在客厅。 |
| 21:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 10:00 | 离开家，前往 皮埃尔的杂货店 。 |
| 11:00 | 到达皮埃尔的杂货店，走进客厅旁边的教堂。 |
| 16:00 | 离开 皮埃尔的杂货店 ，回家。 |
| 17:00 | 在家里的沙发上。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 位于厨房。 |
| 11:30 | 坐在客厅里。 |
| 13:30 | 离开家，前往小镇广场。 |
| 16:00 | 离开广场，回家。 |
| 16:30 | 站在厨房里。 |
| 19:30 | 站在客厅里。 |
| 21:00 | 让 文森特 睡觉。 |
| 22:00 | 回房睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个分区、34 个条件分支、210 行。

- After the Beach Resort on Ginger Island is unlocked, Jodi may randomly spend the day there. After leaving the Island at 6pm, Jodi will immediately go home to bed. Jodi never visits the Resort on Festival days or her checkup day at Harvey's Clinic . She also won't visit the Resort on Vincent 's checkup day.
- Shown below are Jodi's schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:30 AM | Stands by one of the villager shops with Vincent . |
| 12:10 AM | Boards the bus back to the Valley. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

###### Spring 11

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In the kitchen. |
| 11:30 AM | Walks to the waiting room at Harvey's Clinic . |
| 1:30 PM | Moves to the left examination room. |
| 4:00 PM | Walks to Vincent's room. |
| 8:00 PM | Moves to the living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Spring 18

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:30 AM | Walks to the waiting room at Harvey's Clinic . |
| 1:30 PM | Moves to the left examination room. |
| 4:00 PM | Returns to the kitchen. |
| 7:30 PM | In the living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:30 AM | Moves to the living room. |
| 4:00 PM | In the kitchen. |
| 7:30 PM | In the living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In the kitchen. |
| 10:10 AM | Leaves her house, heading to Pierre's General Store . |
| 11:00 AM | Enters Pierre's General Store . |
| 11:30 AM | Standing by the fireplace in the back area of Pierre's. |
| 1:00 PM | Begins exercising with Marnie , Caroline , Emily , and Robin . |
| 4:00 PM | Stands by the fireplace with Caroline, Marnie, and Robin. |
| 6:20 PM | Exits Pierre's, heading home. |
| 7:10 PM | Enters her house. |
| 9:10 PM | Puts Vincent to bed. |
| 10:00 PM | Leaves Vincent 's room, heads to bed. |
| 10:20 PM | Enters her bedroom and goes to sleep. |

###### Wednesday and Friday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside her house, in the kitchen. |
| 11:00 AM | Arrives at Pierre's General Store . |
| 5:00 PM | Inside her house, in the kitchen. |
| 9:00 PM | Vincent's Room. |
| 10:00 PM | Go to bed. |

###### Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:00 AM | Leaves her house and heads for JojaMart . |
| 12:50 PM | Arrives at JojaMart . |
| 5:00 PM | Leaves JojaMart and heads home. |
| 6:30 PM | At home in front of fridge. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed |

###### Saturday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:00 AM | Leaves home, walks to Community Center, stands inside main room. |
| 5:00 PM | Returns home, stands in living room. |
| 9:00 PM | Goes to bed |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | At home in the kitchen. |
| 10:00 AM | Leaves home, walks to Pierre's General Store . |
| 11:00 AM | Arrives at Pierre's, walks into the Chapel in the back. |
| 4:00 PM | Leaves Pierre's General Store , walks home. |
| 5:00 PM | At home on Couch. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:30 AM | Sits in living room. |
| 1:30 PM | Leaves and heads to Town Square. |
| 4:00 PM | Leaves and heads to her home. |
| 4:30 PM | Stands in kitchen. |
| 7:30 PM | Stands in living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the living room. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:30 AM | Moves to the living room. |
| 4:00 PM | In the kitchen. |
| 7:30 PM | In the living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In the kitchen. |
| 10:10 AM | Leaves her house, heading to Pierre's General Store . |
| 11:00 AM | Enters Pierre's General Store . |
| 11:30 AM | Standing by the fireplace in the back area of Pierre's. |
| 1:00 PM | Begins exercising with Marnie , Caroline , Emily , and Robin . |
| 4:00 PM | Stands by the fireplace with Caroline, Marnie, and Robin. |
| 6:20 PM | Exits Pierre's, heading home. |
| 7:10 PM | Enters her house. |
| 9:10 PM | Puts Vincent to bed. |
| 10:00 PM | Leaves Vincent 's room, heads to bed. |
| 10:20 PM | Enters her bedroom and goes to sleep. |

###### Wednesday and Friday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside her house, in the kitchen. |
| 11:00 AM | Arrives at Pierre's General Store . |
| 5:00 PM | Inside her house, in the kitchen. |
| 9:00 PM | Vincent's Room. |
| 10:00 PM | Go to bed. |

###### Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:00 AM | Leaves her house and heads for JojaMart . |
| 12:50 PM | Arrives at JojaMart . |
| 5:00 PM | Leaves JojaMart and heads home. |
| 6:30 PM | At home in front of fridge. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Saturday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:00 AM | Leaves home, walks to Community Center, stands inside main room. |
| 5:00 PM | Returns home, stands in living room. |
| 9:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | At home in the kitchen. |
| 10:00 AM | Leaves home, walks to Pierre's General Store . |
| 11:00 AM | Arrives at Pierre's, walks into the Chapel in the back. |
| 4:00 PM | Leaves Pierre's General Store , walks home. |
| 5:00 PM | At home on Couch. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:30 AM | Sits in living room. |
| 1:30 PM | Leaves and heads to Town Square. |
| 4:00 PM | Leaves and heads to her home. |
| 4:30 PM | Stands in kitchen. |
| 7:30 PM | Stands in living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

##### Fall

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:30 AM | Moves to the living room. |
| 4:00 PM | In the kitchen. |
| 7:30 PM | In the living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In the kitchen. |
| 10:10 AM | Leaves her house, heading to Pierre's General Store . |
| 11:00 AM | Enters Pierre's General Store . |
| 11:30 AM | Standing by the fireplace in the back area of Pierre's. |
| 1:00 PM | Begins exercising with Marnie , Caroline , Emily , and Robin . |
| 4:00 PM | Stands by the fireplace with Caroline, Marnie, and Robin. |
| 6:20 PM | Exits Pierre's, heading home. |
| 7:10 PM | Enters her house. |
| 9:10 PM | Puts Vincent to bed. |
| 10:00 PM | Leaves Vincent 's room, heads to bed. |
| 10:20 PM | Enters her bedroom and goes to sleep. |

###### Wednesday and Friday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside her house, in the kitchen. |
| 11:00 AM | Arrives at Pierre's General Store . |
| 5:00 PM | Inside her house, in the kitchen. |
| 9:00 PM | Vincent's Room. |
| 10:00 PM | Go to bed. |

###### Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:00 AM | Leaves her house and heads for JojaMart . |
| 12:50 PM | Arrives at JojaMart . |
| 5:00 PM | Leaves JojaMart and heads home. |
| 6:30 PM | At home in front of fridge. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Saturday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:00 AM | Leaves home, walks to Community Center, stands inside main room. |
| 5:00 PM | Returns home, stands in living room. |
| 9:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | At home in the kitchen. |
| 10:00 AM | Leaves home, walks to Pierre's General Store . |
| 11:00 AM | Arrives at Pierre's, walks into the Chapel in the back. |
| 4:00 PM | Leaves Pierre's General Store , walks home. |
| 5:00 PM | At home on Couch. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:30 AM | Sits in living room. |
| 1:30 PM | Leaves and heads to Town Square. |
| 4:00 PM | Leaves and heads to her home. |
| 4:30 PM | Stands in kitchen. |
| 7:30 PM | Stands in living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

##### Winter

###### Winter 17

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside her house, in the kitchen. |
| 11:40 AM | Inside her house, in the living room, sitting on the blue sofa. |
| 2:00 PM | Meets with Caroline in the north near her house. |
| 4:30 PM | Attends the Night Market . |
| 11:30 PM | Returns home. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:30 AM | Moves to the living room. |
| 4:00 PM | In the kitchen. |
| 7:30 PM | In the living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In the kitchen. |
| 10:10 AM | Leaves her house, heading to Pierre's General Store . |
| 11:00 AM | Enters Pierre's General Store . |
| 11:30 AM | Standing by the fireplace in the back area of Pierre's. |
| 1:00 PM | Begins exercising with Marnie , Caroline , Emily , and Robin . |
| 4:00 PM | Stands by the fireplace with Caroline, Marnie, and Robin. |
| 6:20 PM | Exits Pierre's, heading home. |
| 7:10 PM | Enters her house. |
| 9:10 PM | Puts Vincent to bed. |
| 10:00 PM | Leaves Vincent 's room, heads to bed. |
| 10:20 PM | Enters her bedroom and goes to sleep. |

###### Wednesday and Friday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside her house, in the kitchen. |
| 11:00 AM | Arrives at Pierre's General Store . |
| 5:00 PM | Inside her house, in the kitchen. |
| 9:00 PM | Vincent's Room. |
| 10:00 PM | Go to bed. |

###### Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:00 AM | Leaves her house and heads for JojaMart . |
| 12:50 PM | Arrives at JojaMart . |
| 5:00 PM | Leaves JojaMart and heads home. |
| 6:30 PM | At home in front of fridge. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

###### Saturday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | In the kitchen. |
| 11:00 AM | Leaves home, walks to Community Center, stands inside main room. |
| 5:00 PM | Returns home, stands in living room. |
| 9:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | At home in the kitchen. |
| 10:00 AM | Leaves home, walks to Pierre's General Store . |
| 11:00 AM | Arrives at Pierre's, walks into the Chapel in the back. |
| 4:00 PM | Leaves Pierre's General Store , walks home. |
| 5:00 PM | At home on Couch. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | In kitchen. |
| 11:30 AM | Sits in living room. |
| 1:30 PM | Leaves and heads to Town Square. |
| 4:00 PM | Leaves and heads to her home. |
| 4:30 PM | Stands in kitchen. |
| 7:30 PM | Stands in living room. |
| 9:00 PM | Puts Vincent to bed. |
| 10:00 PM | Heads to bed. |

<a id="npc-schedule-kent"></a>

### 22. 肯特（Kent）

> 来源：中文 revision 55035；英文 revision 193910
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 7 个分区、7 个条件分支、37 行。

- 姜岛 海滩度假村 修复后，肯特偶尔会去度个假，18:00离开小岛后，肯特将立即回家睡觉。肯特不会在节日当天去度假。
- 下面显示的是肯特的日程表，从上到下按优先顺序排列。例如下雨时优先采用雨天日程表。

##### 春季17日（巴士站已修复）

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开家参加 沙漠节 并站在其中一个村民 商店摊位 前。 |
| 00:00 | 回家睡觉。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 在家，站在客厅里。 |
| 14:00 | 离开家，站在家北面的树下。 |
| 17:00 | 回家，站在入口。 |
| 19:00 | 前往厨房。 |
| 21:00 | 离开家，站在家门口的树下。 |
| 23:00 | 回家睡觉。 |

##### 星期五、星期六

###### 星期五、星期六

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 离开家，站在 下水道 和去 海滩 的桥之间的树下。 |
| 10:30 | 回家，站在客厅里。 |
| 14:00 | 离开家，站在家北面的树下。 |
| 17:00 | 前往 星之果实酒吧 。 |
| 23:50 | 离开酒吧，回家睡觉。 |

##### 星期天（已触发 亚历克斯 14心事件）

###### 星期天（已触发 亚历克斯 14心事件）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家，站在厨房里。 |
| 08:30 | 离开家，前往 皮埃尔的杂货店 里的祭坛房间。 |
| 11:10 | 前往 星之果实酒吧 的里室。 |
| 15:00 | 回家，站在入口。 |
| 19:00 | 前往厨房。 |
| 21:00 | 离开家，站在家门口的树下。 |
| 23:00 | 回家睡觉。 |

##### 星期天

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 在家，站在厨房里。 |
| 10:10 | 离开家，前往 皮埃尔的杂货店 里的祭坛房间。 |
| 14:00 | 离开祭坛房间，前往皮埃尔的柜台。 |
| 16:00 | 离开皮埃尔的杂货店，回家站在入口。 |
| 19:00 | 前往厨房。 |
| 21:00 | 离开家，站在家门口的树下。 |
| 23:00 | 回家睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 离开家，站在 下水道 和去 海滩 的桥之间的树下。 |
| 10:30 | 回家，站在客厅里。 |
| 14:00 | 离开家，站在家北面的树下。 |
| 17:00 | 回家，站在入口。 |
| 19:00 | 前往厨房。 |
| 21:00 | 离开家，站在家门口的树下。 |
| 23:00 | 回家睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个分区、7 个条件分支、37 行。

- After the Beach Resort on Ginger Island is unlocked, Kent may randomly spend the day there. After leaving the Island at 6pm, Kent will immediately go home to bed. Kent never visits the Resort on Festival days.
- Shown below is Kent's schedule, prioritized from the top down. For example, if it is raining, that schedule overrides all schedules below it.

##### Spring 17 (Bus Service Restored)

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves home to head to the Desert Festival and stand by one of the villager shops. |
| 12:00 AM | Heads to bed. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | At home, standing in his living room. |
| 2:00 PM | Leaves home, stands under a tree just north of his house. |
| 5:00 PM | Returns home and stands in the entryway. |
| 7:00 PM | Heads to the kitchen. |
| 9:00 PM | Leaves home, stands under the tree in front of his house. |
| 11:00 PM | Returns home to sleep. |

##### Friday and Saturday

###### Friday and Saturday

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Leaves home, stands under the tree between the sewer entrance and the bridge to the beach . |
| 10:30 AM | Returns home to stand in his living room. |
| 2:00 PM | Leaves home, stands under a tree just north of his house. |
| 5:00 PM | Goes to The Stardrop Saloon . |
| 11:50 PM | Leaves the Saloon and returns home to sleep. |

##### Sunday (Alex's 14 heart event seen)

###### Sunday (Alex's 14 heart event seen)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home, standing in the kitchen. |
| 8:30 AM | Leaves home, heads to the altar room inside Pierre's General Store . |
| 11:10 AM | Leaves Pierre's and heads to the back room of the Stardrop Saloon . |
| 3:00 PM | Leaves the Saloon and heads home to stand in the entryway. |
| 7:00 PM | Heads to the kitchen. |
| 9:00 PM | Leaves home, stands under the tree in front of his house. |
| 11:00 PM | Returns home to sleep. |

##### Sunday

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | At home, standing in the kitchen. |
| 10:10 AM | Leaves home, heads to the altar room inside Pierre's General Store . |
| 2:00 PM | Leaves the altar room, moves to Pierre's counter. |
| 4:00 PM | Leaves Pierre's and heads home to stand in the entryway. |
| 7:00 PM | Heads to the kitchen. |
| 9:00 PM | Leaves home, stands under the tree in front of his house. |
| 11:00 PM | Returns home to sleep. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | Leaves home, stands under the tree between the sewer entrance and the bridge to the beach . |
| 10:30 AM | Returns home to stand in his living room. |
| 2:00 PM | Leaves home, stands under a tree just north of his house. |
| 5:00 PM | Returns home, stands in the entryway. |
| 7:00 PM | Heads to the kitchen. |
| 9:00 PM | Leaves home, stands under the tree in front of his house. |
| 11:00 PM | Returns home to sleep. |

<a id="npc-schedule-krobus"></a>

### 23. 科罗布斯（Krobus）

> 来源：中文 revision 55028；英文 revision 192255
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 0 个分区、0 个条件分支、0 行。

- 科罗布斯不能待在阳光下，所以他会一直在 下水道 中，不会移动。他也不会参与任何居民活动。与科罗布斯成为室友后，它会待在 农舍 中。

源页没有分时表；以上文字即该源的完整日程说明。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 0 个分区、0 个条件分支、0 行。

- Krobus can always be found in the Sewers once the Player obtains the Rusty Key .

源页没有分时表；以上文字即该源的完整日程说明。

<a id="npc-schedule-leo"></a>

### 24. 雷欧（Leo）

> 来源：中文 revision 55053；英文 revision 192150
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 8 个分区、35 个条件分支、177 行。

- 雷欧住在姜岛上不会离开，直到玩家与他的好感度达到6心。
- 住在 深山 的 树屋 中，在周日和部分周一返回 姜岛 。

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在他的小屋里。 |
| 11:00 | 站在他的小屋门外。 |
| 14:00 | 回他的小屋。 |
| 21:00 | 上床。 |

##### 星期二

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在他的小屋里。 |
| 10:30 | 走到岛屿南部的码头，站在岛屿东南部入口附近。 |
| 13:30 | 走到他的小屋旁的丛林（岛屿东部），站在西南角的灌木丛旁。 |
| 17:00 | 走到岛屿北部，站在 姜岛商人 右侧。 |
| 20:00 | 回到家上床。 |

##### 星期天

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在他的小屋里。 |
| 09:30 | 通过丛林东部隐藏的路，走到宝石鸟神龛。 |
| 14:00 | 站在他的小屋门外。 |
| 17:00 | 回他的小屋。 |
| 21:00 | 上床。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在他的小屋内。 |
| 10:30 | 站在他的小屋门外。 |
| 12:00 | 走到岛屿南部的码头，站在西北角，紧挨着鹦鹉栖息地。 |
| 15:00 | 走到岛屿北部，站在地图的西北角，火山入口的西部。 |
| 20:00 | 回到家上床。 |

##### 春季

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开树屋前往 沙漠 参加 沙漠节 ，站在仙人掌商人的东北方。 |
| 00:00 | 回家。 |

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

###### 春季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 位于他的树屋。 |
| 07:00 | 站在他树屋的东面。 |
| 09:30 | 前往 深山湖泊 的西侧。 |
| 14:00 | 回到树屋东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 位于他的树屋。 |
| 10:00 | 前往 莱纳斯 的帐篷。 |
| 15:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 姜岛 他的小屋里。 |
| 09:30 | 位于岛屿南部的鹦鹉栖息地旁。 |
| 14:00 | 站在他的小屋门外。 |
| 17:00 | 进入小屋。 |
| 21:00 | 上床睡觉。 |

###### 星期二、星期三

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于他的树屋。 |
| 09:00 | 前往 博物馆 。 |
| 14:00 | 位于博物馆南边。 |
| 16:20 | 离开博物馆，站在他树屋的东面。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期四、星期五

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 位于他的树屋。 |
| 07:00 | 站在他树屋的东面。 |
| 09:30 | 前往 深山湖泊 的西侧。 |
| 14:00 | 回到树屋东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 离开树屋，站在 海莉和艾米丽家 旁。 |
| 12:00 | 在游乐场玩耍。 |
| 17:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 前往姜岛他的小屋。 |
| 10:30 | 在岛屿南部，岛屿东南入口处附近。 |
| 13:30 | 在他的小屋外。 |
| 17:00 | 在 姜岛商人 的东面。 |
| 20:00 | 去他的小屋睡觉。 |

##### 夏季

###### 夏季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 位于他的树屋。 |
| 07:00 | 站在他树屋的东面。 |
| 09:30 | 前往 深山湖泊 的西侧。 |
| 14:00 | 回到树屋东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 位于他的树屋。 |
| 10:00 | 前往 莱纳斯 的帐篷。 |
| 15:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 姜岛 他的小屋里。 |
| 09:30 | 位于岛屿南部的鹦鹉栖息地旁。 |
| 14:00 | 站在他的小屋门外。 |
| 17:00 | 进入小屋。 |
| 21:00 | 上床睡觉。 |

###### 星期二、星期三

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于他的树屋。 |
| 09:00 | 前往 博物馆 。 |
| 14:00 | 位于博物馆南边。 |
| 16:20 | 离开博物馆，站在他树屋的东面。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期四、星期五

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 位于他的树屋。 |
| 09:40 | 站在 深山湖泊 的西侧。 |
| 13:00 | 绕过树走到湖泊的西南侧。 |
| 16:00 | 站在他树屋的东面。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 离开树屋，站在 海莉和艾米丽家 旁。 |
| 12:00 | 在游乐场玩耍。 |
| 17:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 位于姜岛他的小屋。 |
| 10:30 | 在岛屿南部，岛屿东南入口处附近。 |
| 13:30 | 在他的小屋外。 |
| 17:00 | 在 姜岛商人 的东面。 |
| 20:00 | 去他的小屋睡觉。 |

##### 秋季

###### 秋季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 位于他的树屋。 |
| 07:00 | 站在他树屋的东面。 |
| 09:30 | 前往 深山湖泊 的西侧。 |
| 14:00 | 回到树屋东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 位于他的树屋。 |
| 10:00 | 前往 莱纳斯 的帐篷。 |
| 15:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 姜岛 他的小屋里。 |
| 09:30 | 位于岛屿南部的鹦鹉栖息地旁。 |
| 14:00 | 站在他的小屋门外。 |
| 17:00 | 进入小屋。 |
| 21:00 | 上床睡觉。 |

###### 星期二、星期三

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于他的树屋。 |
| 09:00 | 前往 博物馆 。 |
| 14:00 | 位于博物馆南边。 |
| 16:20 | 离开博物馆，站在他树屋的东面。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期四、星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于他的树屋。 |
| 07:40 | 站在他树屋的东面。 |
| 09:00 | 站在 社区中心 南边。 |
| 14:00 | 站在 深山湖泊 的西侧。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 离开树屋，站在 海莉和艾米丽家 旁。 |
| 12:00 | 在游乐场玩耍。 |
| 17:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 前往姜岛他的小屋。 |
| 10:30 | 在岛屿南部，岛屿东南入口处附近。 |
| 13:30 | 在他的小屋外。 |
| 17:00 | 在 姜岛商人 的东面。 |
| 20:00 | 去他的小屋睡觉。 |

##### 冬季

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 11:00 | 走到莱纳斯帐篷外的入口处。 |
| 16:00 | 前往海滩参加 夜市 。 |
| 23:30 | 回家睡觉。 |

###### 冬季9日和23日

| 时间 | 地点/行动 |
|------|------|
| 06:30 | 位于他的树屋。 |
| 07:00 | 站在他树屋的东面。 |
| 09:30 | 前往 深山湖泊 的西侧。 |
| 14:00 | 回到树屋东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 07:00 | 位于他的树屋。 |
| 10:00 | 前往 莱纳斯 的帐篷。 |
| 15:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于 姜岛 他的小屋里。 |
| 09:30 | 位于岛屿南部的鹦鹉栖息地旁。 |
| 14:00 | 站在他的小屋门外。 |
| 17:00 | 进入小屋。 |
| 21:00 | 上床睡觉。 |

###### 星期二、星期三

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 位于他的树屋。 |
| 09:00 | 前往 博物馆 。 |
| 14:00 | 位于博物馆南边。 |
| 16:20 | 离开博物馆，站在他树屋的东面。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期四、星期五

| 时间 | 地点/行动 |
|------|------|
| 11:00 | 站在他树屋的东面。 |
| 14:00 | 在 博物馆 读书。 |
| 20:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 离开树屋，站在 海莉和艾米丽家 旁。 |
| 12:00 | 在游乐场玩耍。 |
| 17:00 | 站在他树屋的东面。 |
| 19:00 | 进入树屋。 |
| 22:00 | 上床睡觉。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 前往姜岛他的小屋。 |
| 10:30 | 在岛屿南部，岛屿东南入口处附近。 |
| 13:30 | 在他的小屋外。 |
| 17:00 | 在 姜岛商人 的东面。 |
| 20:00 | 去他的小屋睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个分区、35 个条件分支、177 行。

- Leo lives on Ginger Island and doesn’t leave until the player has reached 6 hearts of friendship with him.
- Leo lives in a treehouse in The Mountain , and visits Ginger Island on Sundays and some Mondays.

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside his hut. |
| 11:00 AM | Stands outside the entrance to his hut. |
| 2:00 PM | Returns inside his hut. |
| 9:00 PM | Goes to bed. |

##### Tuesday

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside his hut. |
| 10:30 AM | Walks to the dock on Island South, stands near the entrance to Island Southeast. |
| 1:30 PM | Walks to the jungle outside his hut (Island East), stands near the bushes at the southwest corner. |
| 5:00 PM | Walks to Island North, stands to the right of the Island Trader . |
| 8:00 PM | Goes home to bed. |

##### Sunday

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside his hut. |
| 9:30 AM | Walks to the Gem Bird Shrine, through the hidden passage in the east of the Jungle. |
| 2:00 PM | Stands outside the entrance to his hut. |
| 5:00 PM | Enters his hut. |
| 9:00 PM | Goes to bed. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Inside his hut. |
| 10:30 AM | Stands outside the entrance to his hut. |
| 12:00 PM | Walks to the docks at Island South, stands at the northwest corner, next to the parrot perch. |
| 3:00 PM | Walks to Island North, stands at the northwest corner of the map, west of the volcano entrance. |
| 8:00 PM | Returns home and goes to bed. |

##### Spring

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his treehouse to head to the desert festival and stand north-east of the cactus stand. |
| 12:00 AM | Returns home. |

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

###### Spring 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | In his treehouse. |
| 7:00 AM | Stands to the east of his treehouse. |
| 9:30 AM | Walks to the west of the mountain lake. |
| 2:00 PM | Returns to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | In his treehouse. |
| 10:00 AM | Visits Linus’ tent. |
| 3:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his hut on Ginger Island. |
| 9:30 AM | Next to the parrot perch in Island South. |
| 2:00 PM | Stands outside his hut. |
| 5:00 PM | Enters his hut. |
| 9:00 PM | Goes to bed. |

###### Tuesday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his treehouse. |
| 9:00 AM | Walks to the museum library. |
| 2:00 PM | South of the museum. |
| 4:20 PM | Leaves the museum to stand to the east of his treehouse. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Thursday and Friday

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | In his treehouse. |
| 7:00 AM | Stands to the east of his treehouse. |
| 9:30 AM | Walks to the west of the mountain lake. |
| 2:00 PM | Returns to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Leaves his treehouse to stand next to Haley and Emily's house. |
| 12:00 PM | Plays on the playground. |
| 5:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Walks to his hut on Ginger Island from his treehouse. |
| 10:30 AM | In Island South, near the entrance to Island Southeast. |
| 1:30 PM | Outside his hut. |
| 5:00 PM | To the east of the Island Trader . |
| 8:00 PM | Goes to bed in his hut. |

##### Summer

###### Summer 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | In his treehouse. |
| 7:00 AM | Stands to the east of his treehouse. |
| 9:30 AM | Walks to the west of the mountain lake. |
| 2:00 PM | Returns to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | In his treehouse. |
| 10:00 AM | Visits Linus’ tent. |
| 3:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his hut on Ginger Island. |
| 9:30 AM | Next to the parrot perch in Island South. |
| 2:00 PM | Stands outside his hut. |
| 5:00 PM | Enters his hut. |
| 9:00 PM | Goes to bed. |

###### Tuesday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his treehouse. |
| 9:00 AM | Walks to the museum library. |
| 2:00 PM | South of the museum. |
| 4:20 PM | Leaves the museum to stand to the east of his treehouse. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Thursday and Friday

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | Stands outside of his treehouse. |
| 9:40 AM | Stands on the west edge of the mountain lake. |
| 1:00 PM | Walks around the tree to the southwest of the mountain lake. |
| 4:00 PM | Stands to the east of his treehouse. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Leaves his treehouse to stand next to Haley and Emily's house. |
| 12:00 PM | Plays on the playground. |
| 5:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | In his hut on Ginger Island. |
| 10:30 AM | In Island South, near the entrance to Island Southeast. |
| 1:30 PM | Outside his hut. |
| 5:00 PM | To the east of the Island Trader . |
| 8:00 PM | Goes to bed in his hut. |

##### Fall

###### Fall 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | In his treehouse. |
| 7:00 AM | Stands to the east of his treehouse. |
| 9:30 AM | Walks to the west of the mountain lake. |
| 2:00 PM | Returns to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | In his treehouse. |
| 10:00 AM | Visits Linus’ tent. |
| 3:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his hut on Ginger Island. |
| 9:30 AM | Next to the parrot perch in Island South. |
| 2:00 PM | Stands outside his hut. |
| 5:00 PM | Enters his hut. |
| 9:00 PM | Goes to bed. |

###### Tuesday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his treehouse. |
| 9:00 AM | Walks to the museum library. |
| 2:00 PM | South of the museum. |
| 4:20 PM | Leaves the museum to stands to the east of his treehouse. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Thursday and Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his treehouse. |
| 7:40 AM | Stands to the east of his treehouse. |
| 9:00 AM | Stands south of the community center. |
| 2:00 PM | Stands to the west of the mountain lake. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Leaves his treehouse to stand next to Haley and Emily's house. |
| 12:00 PM | Plays on the playground. |
| 5:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Walks to his hut on Ginger Island. |
| 10:30 AM | In Island South, near the entrance to Island Southeast. |
| 1:30 PM | Outside his hut. |
| 5:00 PM | To the east of the Island Trader . |
| 8:00 PM | Goes to bed in his hut. |

##### Winter

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 11:00 AM | Walks to Linus’ tent and stands outside the entrance. |
| 4:00 PM | Walks to beach to attend Night Market . |
| 11:30 PM | Goes home to bed. |

###### Winter 9 and 23

| 时间 | 地点/行动 |
|------|------|
| 6:30 AM | In his treehouse. |
| 7:00 AM | Stands to the east of his treehouse. |
| 9:30 AM | Walks to the west of the mountain lake. |
| 2:00 PM | Returns to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 7:00 AM | In his treehouse. |
| 10:00 AM | Visits Linus’ tent. |
| 3:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his hut on Ginger Island. |
| 9:30 AM | Next to the parrot perch in Island South. |
| 2:00 PM | Stands outside his hut. |
| 5:00 PM | Enters his hut. |
| 9:00 PM | Goes to bed. |

###### Tuesday and Wednesday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In his treehouse. |
| 9:00 AM | Walks to the museum library. |
| 2:00 PM | South of the museum. |
| 4:20 PM | Leaves the museum to stands to the east of his treehouse. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Thursday and Friday

| 时间 | 地点/行动 |
|------|------|
| 11:00 AM | Stands to the east of his treehouse. |
| 2:00 PM | Reads books in the museum library. |
| 8:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Leaves his treehouse to stand next to Haley and Emily's house. |
| 12:00 PM | Plays on the playground. |
| 5:00 PM | Stands to the east of his treehouse. |
| 7:00 PM | Enters his treehouse. |
| 10:00 PM | Goes to bed. |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Walks to his hut on Ginger Island. |
| 10:30 AM | In Island South, near the entrance to Island Southeast. |
| 1:30 PM | Outside his hut. |
| 5:00 PM | To the east of the Island Trader . |
| 8:00 PM | Goes to bed in his hut. |

<a id="npc-schedule-lewis"></a>

### 25. 刘易斯（Lewis）

> 来源：中文 revision 54974；英文 revision 191314
>
> 结构判定：中英文结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 4 个分区、45 个条件分支、258 行。

- 姜岛 海滩度假村 修复后，刘易斯偶尔会去度个假，18:00离开小岛后，刘易斯将立即回家睡觉。刘易斯不会在节日或诊所预约日当天去度假。

##### 春季

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:50 | 站在巴士南边的一根杆子下。 |
| 01:00 | 乘坐巴士返回星露谷。 |

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:50 | 站在一个村民商铺的旁边。 |
| 00:00 | 乘坐巴士返回星露谷。 |

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:40 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:50 | 站在巴士站，位于 沙漠商人 附近。 |
| 01:10 | 乘坐巴士返回星露谷。 |

###### 春季1日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 鱼店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 春季3日和24日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 玛妮的牧场 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 春季6日和20日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 铁匠铺 。 |
| 13:00 | 离开 铁匠铺 ，前往 博物馆 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 春季15日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 木匠的商店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 刘易斯位于厨房。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 14:30 | 到达 星之果实酒吧 。 |
| 19:40 | 离开酒吧，回 家 。 |
| 20:10 | 到家，走到厨房。 |
| 22:00 | 回卧室睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:30 | 前往 皮埃尔的杂货店 。 |
| 12:20 | 进入 皮埃尔的杂货店 。 |
| 16:00 | 离开杂货店。 |
| 16:50 | 进入 镇长的庄园 并盯着炉子看（可能是在做饭）。 |
| 21:00 | 走到左侧桌子前面。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 皮埃尔的杂货店 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 前往喷泉。 |
| 21:30 | 位于 星之果实酒吧 。 |
| 23:10 | 回 家 。 |

###### 社区中心已修复

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 09:00 | 打理房子旁边的花草。在 09:40 时往东面走。 |
| 10:40 | 离开 镇长的庄园 。 |
| 11:40 | 进入 社区中心 。 |
| 12:10 | 站在 社区中心 的金库房间。 |
| 17:10 | 走到 社区中心 的壁炉前面。 |
| 18:30 | 离开 社区中心 ，回 家 。 |
| 19:40 | 到家，走到厨房。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 10:00 | 离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 小镇广场 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 离开，站在 皮埃尔的杂货店 外的布告栏前面。 |
| 16:00 | 回 家 。 |
| 16:30 | 到 家 。 |
| 22:00 | 上床睡觉。 |

##### 夏季

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

###### 夏季1日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 鱼店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 夏季3日和24日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 玛妮的牧场 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 夏季6日和20日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 铁匠铺 。 |
| 13:00 | 离开 铁匠铺 ，前往 博物馆 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 夏季15日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 木匠的商店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 刘易斯位于厨房。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 14:30 | 到达 星之果实酒吧 。 |
| 19:40 | 离开酒吧，回 家 。 |
| 20:10 | 到家，走到厨房。 |
| 22:00 | 回卧室睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:30 | 前往 皮埃尔的杂货店 。 |
| 12:20 | 进入 皮埃尔的杂货店 。 |
| 16:00 | 离开杂货店。 |
| 16:50 | 进入 镇长的庄园 并盯着炉子看（可能是在做饭）。 |
| 21:00 | 走到左侧桌子前面。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 皮埃尔的杂货店 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 前往喷泉。 |
| 21:30 | 位于 星之果实酒吧 。 |
| 23:10 | 回 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 13:00 | 站在 海滩 的码头上。 |
| 16:50 | 进入 镇长的庄园 。 |

###### 社区中心已修复

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 09:00 | 打理房子旁边的花草。在 09:40 时往东面走。 |
| 10:40 | 离开 镇长的庄园 。 |
| 11:40 | 进入 社区中心 。 |
| 12:10 | 站在 社区中心 的金库房间。 |
| 17:10 | 走到 社区中心 的壁炉前面。 |
| 18:30 | 离开 社区中心 ，回 家 。 |
| 19:40 | 到家，走到厨房。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 10:00 | 离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 小镇广场 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 离开，站在 皮埃尔的杂货店 外的布告栏前面。 |
| 16:00 | 回 家 。 |
| 16:30 | 到 家 。 |
| 22:00 | 上床睡觉。 |

##### 秋季

###### 秋季1日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 鱼店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 秋季3日和24日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 玛妮的牧场 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 秋季6日和20日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 铁匠铺 。 |
| 13:00 | 离开 铁匠铺 ，前往 博物馆 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 秋季9日

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 站在 镇长的庄园 的餐厅里。 |
| 10:30 | 到达 玛妮的牧场 。 |
| 11:00 | 离开 玛妮的牧场 。 |
| 12:30 | 进入 诊所 。 |
| 16:00 | 离开 诊所 。 |
| 17:30 | 到达 玛妮的牧场 ，盯着微波炉看（可能在做饭）。 |
| 21:20 | 前往玛妮卧室的床边。 |

###### 秋季15日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 木匠的商店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 刘易斯位于厨房。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 14:30 | 到达 星之果实酒吧 。 |
| 19:40 | 离开酒吧，回 家 。 |
| 20:10 | 到家，走到厨房。 |
| 22:00 | 回卧室睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:30 | 前往 皮埃尔的杂货店 。 |
| 12:20 | 进入 皮埃尔的杂货店 。 |
| 16:00 | 离开杂货店。 |
| 16:50 | 进入 镇长的庄园 并盯着炉子看（可能是在做饭）。 |
| 21:00 | 走到左侧桌子前面。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 皮埃尔的杂货店 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 前往喷泉。 |
| 21:30 | 位于 星之果实酒吧 。 |
| 23:10 | 回 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 09:30 | 打理房子旁边的花草。 |
| 11:00 | 离开 庄园 ，走到 莉亚的农舍 附近的河边。 |
| 13:30 | 站在 莉亚的农舍 附近的河边。 |
| 16:00 | 回 家 。 |
| 17:30 | 位于 家 里。 |
| 22:00 | 上床睡觉。 |

###### 社区中心已修复

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 09:00 | 打理房子旁边的花草。在 09:40 时往东面走。 |
| 10:40 | 离开 镇长的庄园 。 |
| 11:40 | 进入 社区中心 。 |
| 12:10 | 站在 社区中心 的金库房间。 |
| 17:10 | 走到 社区中心 的壁炉前面。 |
| 18:30 | 离开 社区中心 ，回 家 。 |
| 19:40 | 到家，走到厨房。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 10:00 | 离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 小镇广场 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 离开，站在 皮埃尔的杂货店 外的布告栏前面。 |
| 16:00 | 回 家 。 |
| 16:30 | 到 家 。 |
| 22:00 | 上床睡觉。 |

##### 冬季

###### 冬季1日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 鱼店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 冬季3日和24日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 玛妮的牧场 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 冬季6日和20日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 铁匠铺 。 |
| 13:00 | 离开 铁匠铺 ，前往 博物馆 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 10:00 | 离开家，前往 木匠的商店 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 10:00 | 出门，站在他的花园前面。 |
| 11:40 | 前往小镇广场。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 站在 皮埃尔的杂货店 外的布告栏前面。 |
| 16:20 | 参加 夜市 。 |
| 23:00 | 回 家 。 |

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 刘易斯位于厨房。 |
| 14:00 | 离开家，前往 星之果实酒吧 。 |
| 14:30 | 到达 星之果实酒吧 。 |
| 19:40 | 离开酒吧，回 家 。 |
| 20:10 | 到家，走到厨房。 |
| 22:00 | 回卧室睡觉。 |

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:30 | 前往 皮埃尔的杂货店 。 |
| 12:20 | 进入 皮埃尔的杂货店 。 |
| 16:00 | 离开杂货店。 |
| 16:50 | 进入 镇长的庄园 并盯着炉子看（可能是在做饭）。 |
| 21:00 | 走到左侧桌子前面。 |
| 22:00 | 上床睡觉。 |

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 10:00 | 起床，离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 皮埃尔的杂货店 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 前往喷泉。 |
| 21:30 | 位于 星之果实酒吧 。 |
| 23:10 | 回 家 。 |

###### 星期天

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 位于厨房。 |
| 11:00 | 离开 家 ，前往 博物馆 。 |
| 16:00 | 回 家 。 |
| 22:00 | 上床睡觉。 |

###### 社区中心已修复

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 09:00 | 打理房子旁边的花草。在 09:40 时往东面走。 |
| 10:40 | 离开 镇长的庄园 。 |
| 11:40 | 进入 社区中心 。 |
| 12:10 | 站在 社区中心 的金库房间。 |
| 17:10 | 走到 社区中心 的壁炉前面。 |
| 18:30 | 离开 社区中心 ，回 家 。 |
| 19:40 | 到家，走到厨房。 |

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 位于厨房。 |
| 10:00 | 离开 镇长的庄园 。 |
| 10:10 | 打理房子旁边的花草。 |
| 11:40 | 前往 小镇广场 。 |
| 12:30 | 站在 哈维的诊所 旁边树的前面。 |
| 14:00 | 离开，站在 皮埃尔的杂货店 外的布告栏前面。 |
| 16:00 | 回 家 。 |
| 16:30 | 到 家 。 |
| 22:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个分区、45 个条件分支、255 行。

- After the Beach Resort on Ginger Island is unlocked, Lewis may randomly spend the day there. After leaving the Island at 6pm, Lewis will immediately go home to bed. Lewis never visits the Resort on Festival days or his checkup day at Harvey's Clinic .

##### Spring

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Greets Pam as he boards the bus to Calico Desert for the Desert Festival . |
| 9:50 AM | Stands under a pole south of the bus. |
| 1:00 AM | Boards the bus back to the Valley. |

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 9:50 AM | Stands by one of the villager shops. |
| 12:00 AM | Boards the bus back to the Valley. |

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:40 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 9:50 AM | Stands at the bus stop next to the Desert Trader . |
| 1:10 AM | Boards the bus back to the Valley. |

###### Spring 1

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Fish Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Spring 3 and 24

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to Marnie's Ranch . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Spring 6 and 20

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Blacksmith . |
| 1:00 PM | Leaves the Blacksmith to go to the Museum . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Spring 15

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Carpenter's Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 2:00 PM | Departs for the the saloon . |
| 2:30 PM | Arrives at the the saloon . |
| 7:40 PM | Departs for home . |
| 8:10 PM | Arrives home. Moves to his kitchen. |
| 10:00 PM | Leaves kitchen to go to bed. Mayor's Manor is locked. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor |
| 11:30 AM | Stops gardening and heads towards Pierre's . |
| 12:20 PM | Enters Pierre's . |
| 4:00 PM | Leaves Pierre's . |
| 4:50 PM | Enters Manor and stares at stove (presumably cooking). |
| 9:00 PM | Moves from stove to Pelican Town Data Book. |
| 10:00 PM | Heads to Bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:40 AM | Stops gardening and heads towards Pierre's . |
| 12:30 PM | Stands outside of Clinic in front of tree. |
| 2:00 PM | Moves to the fountain. |
| 9:30 PM | In The Stardrop Saloon . |
| 11:10 PM | Goes back to Manor . |

###### Community Center Restored

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 9:00 AM | Gardens in front of Manor . Moves to east side at 9:40 AM. |
| 10:40 AM | Leaves the Manor . |
| 11:40 AM | Enters Community Center . |
| 12:10 PM | Stands in the Vault Room in the Community Center . |
| 5:10 PM | Moves to stand in front of the fireplace in the Community Center . |
| 6:30 PM | Leaves the Community Center to go to Manor . |
| 7:40 PM | Arrives home. Moves to his kitchen. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Stands in his kitchen at home . |
| 10:00 AM | Exits Manor . |
| 10:10 AM | Gardens in front of Manor . |
| 11:40 AM | Stops gardening and heads to town square . |
| 12:30 PM | Stands in front of tree to the left of Clinic . |
| 2:00 PM | Leaves tree and stands in front of the notice board at Pierre's . |
| 4:00 PM | Heads home . |
| 4:30 PM | Arrives home for the night. |
| 10:00 PM | Goes to bed. Mayor's Manor is locked. |

##### Summer

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In The Stardrop Saloon . |

###### Summer 1

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Fish Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Summer 3 and 24

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to Marnie's Ranch . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Summer 6 and 20

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Blacksmith . |
| 1:00 PM | Leaves the Blacksmith to go to the Museum . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Summer 15

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Carpenter's Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 2:00 PM | Departs for the the saloon . |
| 2:30 PM | Arrives at the the saloon . |
| 7:40 PM | Departs for home . |
| 8:10 PM | Arrives home. Moves to his kitchen. |
| 10:00 PM | Leaves kitchen to go to bed. Mayor's Manor is locked. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:30 AM | Stops gardening and heads towards Pierre's . |
| 12:20 PM | Enters Pierre's . |
| 4:00 PM | Leaves Pierre's . |
| 4:50 PM | Enters Manor and stares at stove (presumably cooking). |
| 9:00 PM | Moves from stove to Pelican Town Data Book. |
| 10:00 PM | Heads to Bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:40 AM | Stops gardening and heads towards Pierre's . |
| 12:30 PM | Stands outside of Clinic in front of tree. |
| 2:00 PM | Moves to the fountain. |
| 9:30 PM | In The Stardrop Saloon . |
| 11:10 PM | Goes back to Manor . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Leaves his Manor . |
| 10:10 AM | Gardening in front of his Manor . |
| 1:00 PM | Standing on the pier at the The Beach . |
| 4:50 PM | Enters his Manor . |

###### Community Center Restored

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 9:00 AM | Gardens in front of Manor . Moves to east side at 9:40 AM. |
| 10:40 AM | Leaves the Manor . |
| 11:40 AM | Enters Community Center . |
| 12:10 PM | Stands in the Vault Room in the Community Center . |
| 5:10 PM | Moves to stand in front of the fireplace in the Community Center . |
| 6:30 PM | Leaves the Community Center to go to Manor . |
| 7:40 PM | Arrives home. Moves to his kitchen. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Stands in his kitchen at home . |
| 10:00 AM | Exits Manor . |
| 10:10 AM | Gardens in front of Manor . |
| 11:40 AM | Stops gardening and heads to town square . |
| 12:30 PM | Stands in front of tree to the left of Clinic . |
| 2:00 PM | Leaves tree and stands in front of the notice board at Pierre's . |
| 4:00 PM | Heads home . |
| 4:30 PM | Arrives home for the night. |
| 10:00 PM | Goes to bed. Mayor's Manor is locked. |

##### Fall

###### Fall 1

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Fish Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Fall 3 and 24

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to Marnie's Ranch . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Fall 6 and 20

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Blacksmith . |
| 1:00 PM | Leaves the Blacksmith to go to the Museum . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Fall 9

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:30 AM | Heads to Clinic . |
| 5:00 PM | Leaves Clinic and heads to The Stardrop Saloon . |
| 9:00 PM | Leaves the saloon and goes to Marnie's bed. |

###### Fall 15

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Carpenter's Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 2:00 PM | Departs for the the saloon . |
| 2:30 PM | Arrives at the the saloon . |
| 7:40 PM | Departs for home . |
| 8:10 PM | Arrives home. Moves to his kitchen. |
| 10:00 PM | Leaves kitchen to go to bed. Mayor's Manor is locked. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:30 AM | Stops gardening and heads towards Pierre's . |
| 12:20 PM | Enters Pierre's . |
| 4:00 PM | Leaves Pierre's . |
| 4:50 PM | Enters Manor and stares at stove (presumably cooking). |
| 9:00 PM | Moves from stove to Pelican Town Data Book. |
| 10:00 PM | Heads to Bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:40 AM | Stops gardening and heads towards Pierre's . |
| 12:30 PM | Stands outside of Clinic in front of tree. |
| 2:00 PM | Moves to the fountain. |
| 9:30 PM | In The Stardrop Saloon . |
| 11:10 PM | Goes back to Manor . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 9:30 AM | Gardens in front of the Manor . |
| 11:00 AM | Walks from the Manor to river near Leah's cabin. |
| 1:30 PM | Stands by river near Leah's cabin. |
| 4:00 PM | Walks from river to Mayor's Manor . |
| 5:30 PM | Inside the Manor . |
| 10:00 PM | Sleeps in Mayor's Manor bedroom. |

###### Community Center Restored

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 9:00 AM | Gardens in front of Manor . Moves to east side at 9:40 AM. |
| 10:40 AM | Leaves the Manor . |
| 11:40 AM | Enters Community Center . |
| 12:10 PM | Stands in the Vault Room in the Community Center . |
| 5:10 PM | Moves to stand in front of the fireplace in the Community Center . |
| 6:30 PM | Leaves the Community Center to go to Manor . |
| 7:40 PM | Arrives home. Moves to his kitchen. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Stands in his kitchen at home . |
| 10:00 AM | Exits Manor . |
| 10:10 AM | Gardens in front of Manor . |
| 11:40 AM | Stops gardening and heads to town square . |
| 12:30 PM | Stands in front of tree to the left of Clinic . |
| 2:00 PM | Leaves tree and stands in front of the notice board at Pierre's . |
| 4:00 PM | Heads home . |
| 4:30 PM | Arrives home for the night. |
| 10:00 PM | Goes to bed. Mayor's Manor is locked. |

##### Winter

###### Winter 1

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Fish Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Winter 3 and 24

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to Marnie's Ranch . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Winter 6 and 20

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Blacksmith . |
| 1:00 PM | Leaves the Blacksmith to go to the Museum . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 10:00 AM | Leaves home to head to the Carpenter's Shop . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Standing in kitchen. |
| 10:00 AM | Walks outside to stand in his garden. |
| 11:40 AM | Walks to town square. |
| 12:30 PM | Stands in front of tree beside Harvey's Clinic . |
| 2:00 PM | Stands in front of bulletin board at Pierre's . |
| 4:20 PM | Attends the Night Market . |
| 11:00 PM | Returns to the Manor . |

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 2:00 PM | Departs for the the saloon . |
| 2:30 PM | Arrives at the the saloon . |
| 7:40 PM | Departs for home . |
| 8:10 PM | Arrives home. Moves to his kitchen. |
| 10:00 PM | Leaves kitchen to go to bed. Mayor's Manor is locked. |

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:30 AM | Stops gardening and heads towards Pierre's . |
| 12:20 PM | Enters Pierre's . |
| 4:00 PM | Leaves Pierre's . |
| 4:50 PM | Enters Manor and stares at stove (presumably cooking). |
| 9:00 PM | Moves from stove to Pelican Town Data Book. |
| 10:00 PM | Heads to Bed. |

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 10:00 AM | Wakes up and exits Manor . |
| 10:10 AM | Gardening in front of Manor . |
| 11:40 AM | Stops gardening and heads towards Pierre's . |
| 12:30 PM | Stands outside of Clinic in front of tree. |
| 2:00 PM | Moves to the fountain. |
| 9:30 PM | In The Stardrop Saloon . |
| 11:10 PM | Goes back to Manor . |

###### Sunday

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Stands in his kitchen. |
| 11:00 AM | Leave home to head to the Museum . |
| 4:00 PM | Heads home . |
| 10:00 PM | Goes to bed. |

###### Community Center Restored

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Mayor's Manor is unlocked. Lewis is in his kitchen. |
| 9:00 AM | Gardens in front of Manor . Moves to east side at 9:40 AM. |
| 10:40 AM | Leaves the Manor . |
| 11:40 AM | Enters Community Center . |
| 12:10 PM | Stands in the Vault Room in the Community Center . |
| 5:10 PM | Moves to stand in front of the fireplace in the Community Center . |
| 6:30 PM | Leaves the Community Center to go to Manor . |
| 7:40 PM | Arrives home. Moves to his kitchen. |

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Stands in his kitchen at home . |
| 10:00 AM | Exits Manor . |
| 10:10 AM | Gardens in front of Manor . |
| 11:40 AM | Stops gardening and heads to town square . |
| 12:30 PM | Stands in front of tree to the left of Clinic . |
| 2:00 PM | Leaves tree and stands in front of the notice board at Pierre's . |
| 4:00 PM | Heads home . |
| 4:30 PM | Arrives home for the night. |
| 10:00 PM | Goes to bed. Mayor's Manor is locked. |

<a id="npc-schedule-linus"></a>

### 26. 莱纳斯（Linus）

> 来源：中文 revision 55042；英文 revision 193911
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 8 个分区、8 个条件分支、41 行。

- 莱纳斯不会去姜岛的 海滩度假村 。
- 下面显示的是莱纳斯的日程表，从上到下按优先顺序排列。例如下雨时优先采用雨天日程表。

##### 春季16日（巴士站已修复）

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:50 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:20 | 站在 卡利科三花蛋商人 后方的一个垃圾桶旁。 |
| 01:40 | 乘坐巴士返回星露谷。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 站在他的 帐篷 南侧的悬崖处。 |
| 12:00 | 走到并站在他的帐篷西侧的悬崖处。 |
| 17:00 | 站在帐篷外的营火旁。 |
| 22:00 | 回到他的帐篷上床睡觉。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 帐篷 内。 |
| 09:30 | 离开帐篷，站在帐篷西侧的灌木丛后面。 |
| 10:10 | 回到帐篷。 |
| 15:00 | 离开帐篷，站在帐篷西侧的一棵树下。 |
| 19:00 | 回到帐篷。 |
| 23:30 | 上床睡觉。 |

##### 冬季15日

###### 冬季15日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 帐篷 内。 |
| 11:00 | 离开帐篷, 站在帐篷外的篝火西侧。 |
| 16:00 | 走向海滩，参加 夜市 。 |
| 23:30 | 回到帐篷过夜。 |

##### 春季

###### 春季

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 帐篷 内。 |
| 06:30 | 离开帐篷，站在帐篷西侧的灌木丛后面。 |
| 07:00 | 走向帐篷外的篝火。 |
| 09:30 | 离开帐篷，走向湖泊西侧。 |
| 14:00 | 回到帐篷外的篝火边。 |
| 19:00 | 回到帐篷。 |
| 23:00 | 上床睡觉。 |

##### 夏季

###### 夏季

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 帐篷 内。 |
| 06:30 | 走向帐篷东侧，从峭壁上眺望湖泊。 |
| 09:40 | 走向湖西侧的围栏南端，并在附近踱步。 |
| 13:00 | 在湖的西侧，往南再走一点。 |
| 16:00 | 回到帐篷前的篝火。 |
| 20:00 | 走向帐篷旁的灌木丛后面。 |
| 20:20 | 回到帐篷过夜。 |

##### 秋季

###### 秋季

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 帐篷 内。 |
| 07:00 | 离开帐篷，站在帐篷西侧的灌木丛后面。 |
| 07:40 | 走向帐篷外的篝火。 |
| 09:00 | 走向 温泉 ，站在建筑东侧。 |
| 14:00 | 走向湖的西侧，并在那站着。 |
| 18:00 | 回到帐篷过夜。 |

##### 冬季

###### 冬季

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 帐篷 内。 |
| 11:00 | 离开帐篷, 站在帐篷外的篝火西侧。 |
| 14:00 | 走向 温泉 , 站在入口处。 |
| 18:00 | 回到帐篷过夜。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个分区、8 个条件分支、41 行。

- Linus never visits the Beach Resort on Ginger Island.
- Shown below are Linus' schedules prioritized highest to lowest within each season. For example, if it is raining, that schedule overrides all others below it.

##### Spring 16 (Bus Service Restored)

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:50 AM | Takes the bus to Calico Desert to attend the Desert Festival . |
| 10:20 AM | Stands by a trash can behind the Calico Egg merchant. |
| 1:40 AM | Heads back to the bus. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Stands at the cliff south of his tent . |
| 12:00 PM | Moves to the cliff west of his tent. |
| 5:00 PM | Stands by the campfire. |
| 10:00 PM | Goes inside his tent to sleep. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Inside his tent . |
| 9:30 AM | Exits tent, stands behind bush west of his tent. |
| 10:10 AM | Returns to his tent. |
| 3:00 PM | Exits tent, stands under tree west of his tent. |
| 7:00 PM | Returns to his tent. |
| 11:30 PM | Goes to bed. |

##### Winter 15

###### Winter 15

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Inside his tent . |
| 11:00 AM | Exits tent, stands west of campfire in front of his tent. |
| 4:00 PM | Walks to beach to attend Night Market . |
| 11:30 PM | Returns to his tent for the night. |

##### Spring

###### Spring

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Inside his tent . |
| 6:30 AM | Exits tent, stands behind bush west of his tent. |
| 7:00 AM | Walks to west of campfire in front of his tent. |
| 9:30 AM | Walks to west side of lake. |
| 2:00 PM | Walks to west of campfire in front of his tent. |
| 7:00 PM | Returns to his tent. |
| 11:00 PM | Goes to bed. |

##### Summer

###### Summer

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Inside his tent . |
| 6:30 AM | Walks to cliff overlooking lake, east of his tent. |
| 9:40 AM | Walks to south of fence, west of lake. |
| 1:00 PM | Walks further south, west of lake. |
| 4:00 PM | Walks to west of campfire in front of his tent. |
| 8:00 PM | Walks behind bush west of his tent. |
| 8:20 PM | Returns to his tent for the night. |

##### Fall

###### Fall

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Inside his tent . |
| 7:00 AM | Exits tent, stands behind bush west of his tent. |
| 7:40 AM | Walks to west of campfire in front of his tent. |
| 9:00 AM | Walks to Spa , stands at east side of building. |
| 2:00 PM | Walks to west side of lake. |
| 6:00 PM | Returns to his tent for the night. |

##### Winter

###### Winter

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Inside his tent . |
| 11:00 AM | Exits tent, stands west of campfire in front of his tent. |
| 2:00 PM | Walks to Spa , stands inside entrance. |
| 6:00 PM | Returns to his tent for the night. |

<a id="npc-schedule-marnie"></a>

### 27. 玛妮（Marnie）

> 来源：中文 revision 55084；英文 revision 191544
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 10 个分区、10 个条件分支、47 行。

- 姜岛的海滩度假村 解锁后，玛妮有时会在星期一或星期二去那儿度假。18:00离开姜岛后，玛妮会立即回家上床睡觉。玛妮不会在秋季18日（她的体检日）或节日当天去姜岛。
- 以下是玛妮的日程安排，优先度从高到低排序。例如，如果当天下雨，雨天的时间表会比它下方的优先级更高。

##### 春季17日（巴士站已修复）

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:50 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:10 | 站在 沙漠商人 旁的巴士站牌处。 |
| 23:40 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 秋季18日

###### 秋季18日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 玛妮的牧场 ，她的房间里。 |
| 10:30 | 离开 玛妮的牧场 并走去 哈维的诊所 。 |
| 12:00 | 到达 哈维的诊所 ，站在候诊室中。 |
| 13:30 | 走进 哈维的诊所 的检查室。 |
| 16:00 | 离开 哈维的诊所 并走回 玛妮的牧场 。 |
| 17:30 | 到达 玛妮的牧场 并站在厨房里。 |
| 21:00 | 离开厨房，走回自己的房间并睡觉。 |

##### 冬季16日

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 玛妮的牧场 ，她的房间里。 |
| 09:00 | 站在 玛妮的牧场 的柜台后面。 |
| 16:00 | 参加 夜市 。 |
| 23:40 | 走回家睡觉。 |

##### 冬季18日

###### 冬季18日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在 玛妮的牧场 ，她的房间里。 |
| 11:00 | 离开 玛妮的牧场 带着 贾斯 到 哈维的诊所 。 |
| 12:00 | 站在诊所的候诊室。 |
| 13:40 | 走进诊所的检查室。 |
| 16:00 | 离开 哈维的诊所 并走回 玛妮的牧场 。 |
| 18:00 | 到达 玛妮的牧场 并站在厨房里。 |
| 21:00 | 离开厨房，走回自己的房间并睡觉。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 家 里的厨房。 |

##### 雨天 或 星期四

###### 雨天 或 星期四

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 玛妮的牧场 ，她的房间里。 |
| 09:00 | 站在 玛妮的牧场 的柜台后面。 |
| 16:00 | 关闭商店，走到厨房。 |
| 18:00 | 离开厨房，走进她的房间。站在梳妆台前。 |
| 21:00 | 上床睡觉。 |

##### 星期一

###### 星期一

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 玛妮的牧场 ，她的房间里。 |
| 08:10 | 离开 玛妮的牧场 走向 皮埃尔的杂货店 。 |
| 12:00 | 离开 皮埃尔的杂货店 并走回 玛妮的牧场 。 |
| 13:30 | 到达 玛妮的牧场 并站在厨房里。 |
| 21:00 | 离开厨房，走回自己的房间并睡觉。 |

##### 星期二

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 玛妮的牧场 ，她的房间里。 |
| 10:00 | 离开 玛妮的牧场 并走向 皮埃尔的杂货店 。 |
| 12:00 | 到达 皮埃尔的杂货店 ，和 卡洛琳 、 乔迪 、 艾米丽 、 罗宾 一起锻炼身体。 |
| 16:00 | 锻炼结束后，和大家一起聊天。 |
| 18:10 | 离开 皮埃尔的杂货店 并走回 玛妮的牧场 。 |
| 20:00 | 到达 玛妮的牧场 并站在厨房里。 |
| 21:00 | 离开厨房，走回自己的房间并睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在 玛妮的牧场 ，她的房间里。 |
| 09:00 | 站在 玛妮的牧场 的柜台后面。 |
| 16:00 | 关闭 玛妮的牧场 并走到她的房间。 |
| 17:00 | 离开 玛妮的牧场 并走到 星之果实酒吧 。 |
| 23:00 | 离开 星之果实酒吧 并走回 玛妮的牧场 。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 10 个分区、10 个条件分支、47 行。

- After the Beach Resort on Ginger Island is unlocked, Marnie may randomly spend Monday and/or Tuesday there. After leaving the Island at 6pm, Marnie will immediately go home to bed. Marnie never visits the Resort on Festival days.
- Shown below is Marnie's schedule, prioritized from the top down. For example, if it is raining, that schedule overrides all schedules below it.

##### Spring 17 (Bus Service Restored)

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:50 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:10 AM | Stands at the bus stop next to the Desert Trader . |
| 11:40 PM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Fall 18

###### Fall 18

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home in her room. |
| 10:30 AM | Leaves her house and walks to Harvey's Clinic . |
| 12:00 PM | Arrives at Harvey's Clinic , stands in the waiting room. |
| 1:30 PM | Walks into the exam room at Harvey's Clinic . |
| 4:00 PM | Leaves Harvey's Clinic and walks back to her house . |
| 5:30 PM | Arrives home and stands in the kitchen. |
| 9:00 PM | Walks to her room and goes to sleep. |

##### Winter 16

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home in her room. |
| 9:00 AM | Stands behind the counter of her shop. |
| 4:00 PM | Attends the Night Market . |
| 11:40 PM | Walks back to her house to go to bed. |

##### Winter 18

###### Winter 18

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | At home in her room. |
| 11:00 AM | Leaves her house to take Jas to Harvey's Clinic . |
| 12:00 PM | Stands in clinic waiting room. |
| 1:40 PM | Walks into clinic examination room. |
| 4:00 PM | Leaves clinic and walks back to her house. |
| 6:00 PM | Arrives at home and stands in the kitchen. |
| 9:00 PM | Walks to her room and goes to bed. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the kitchen. |

##### Rain and Thursday

###### Rain and Thursday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home in her room. |
| 9:00 AM | Stands behind the counter of her shop. |
| 4:00 PM | Closes her shop and walks to the kitchen. |
| 6:00 PM | Leaves the kitchen and walks to her room. Stands in front of her dresser. |
| 9:00 PM | Goes to bed. |

##### Monday

###### Monday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home in her room. |
| 8:10 AM | Leaves her house and walks to Pierre's General Store . |
| 12:00 PM | Leaves Pierre's General Store and walks back to her house. |
| 1:30 PM | Arrives at home and stands in the kitchen. |
| 9:00 PM | Walks to her room and goes to bed. |

##### Tuesday

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home in her room. |
| 10:00 AM | Leaves her house and walks to Pierre's General Store . |
| 12:00 PM | Arrives at Pierre's General Store to exercise with Caroline , Jodi , Emily , and Robin . |
| 4:00 PM | Chats with the other ladies after exercise class. |
| 6:10 PM | Leaves Pierre's General Store and walks back to her house. |
| 8:00 PM | Arrives home and stands in the kitchen. |
| 9:00 PM | Walks to her room and goes to bed. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | At home in her room. |
| 9:00 AM | Stands behind the counter of her shop. |
| 4:00 PM | Closes her shop and walks to her room. |
| 5:00 PM | Leaves her house and walks to The Stardrop Saloon . |
| 11:00 PM | Leaves the Saloon and walks back to her house to go to bed. |

<a id="npc-schedule-pam"></a>

### 28. 潘姆（Pam）

> 来源：中文 revision 55017；英文 revision 191550
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 8 个分区、8 个条件分支、25 行。

- 姜岛的海滩度假村 解锁后，潘姆有时会去那儿。18:00离开姜岛后，潘姆会立即回家上床睡觉。潘姆不会在 春季 25日（她的体检日）、 秋季 15日（ 桑迪 的生日）或 节日 当天去姜岛。
- 以下是潘姆的日程安排，优先度从高到低排序。例如，春季25日时公交车已修复，优先执行春季25日的时间表。

##### 春季16日（巴士站已修复）

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:30 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:50 | 站在其中一个村民 商店摊位 前。 |
| 00:40 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 春季15日和17日（巴士站已修复）

###### 春季15日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 07:20 | 离开 拖车 。 |
| 08:50 | 到达 巴士站 。 |
| 00:50 | 回 家 。 |

##### 春季25日

###### 春季25日

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 坐在 家 里的沙发上。 |
| 11:30 | 离 家 出门，前往 哈维的诊所 体检。 |
| 13:30 | 继续在 诊所 体检。 |
| 16:00 | 离开 诊所 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 酒吧 回家睡觉。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

##### 冬季12日和13日

###### 冬季12日和13日

| 时间 | 地点/行动 |
|------|------|
| 全天 | 在 沙滩 , 观看 鱿鱼节 。 |

##### 日常时间表（巴士站未修复）

###### 日常时间表（巴士站未修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 坐在 家 里沙发上。 |
| 12:00 | 离 家 出门，前往 Joja超市 。 |
| 16:00 | 离开 Joja超市 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 酒吧 回家睡觉。 |

##### 日常时间表（巴士站已修复）

###### 日常时间表（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:00 | 坐在 家 里沙发上。 |
| 08:30 | 离 家 出门，前往 农场 东边的 巴士站 。 |
| 10:00 | 到达 巴士站 。 |
| 17:00 | 离开 巴士站 ，前往 星之果实酒吧 。 |
| 00:00 | 离开 酒吧 回家睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个分区、8 个条件分支、25 行。

- After the Beach Resort on Ginger Island is unlocked, Pam may randomly spend the day there. After leaving the Island at 6pm, Pam will immediately go home to bed. Pam never visits the Resort on Fall 15, Festival days, or her checkup day at Harvey's Clinic .
- Shown below are Pam's schedules prioritized highest to lowest. For example, if Pam has been selected as a vendor at the desert festival, that schedule overrides all others.

##### Spring 16 (Bus Service Restored)

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:30 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:50 AM | Stands in front of one of the villager shops. |
| 12:40 AM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes bus back to the Valley. |

##### Spring 15 and 17 (Bus Service Restored)

###### Spring 15 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 7:20 AM | Leaves her trailer . |
| 8:50 AM | Arrives at the Bus Stop . |
| 12:50 AM | Heads home. |

##### Spring 25

###### Spring 25

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Lounges on her couch in the trailer . |
| 11:30 AM | Leaves her trailer and heads to the medical clinic for her annual checkup. |
| 1:30 PM | Continues her checkup at the clinic . |
| 4:00 PM | Leaves the clinic and heads to the saloon . |
| 12:00 AM | Leaves the saloon and heads home for the night. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In The Stardrop Saloon . |

##### Winter 12 and 13

###### Winter 12 and 13

| 时间 | 地点/行动 |
|------|------|
| All day | On The Beach , watching the SquidFest . |

##### Regular Schedule (No Bus Service)

###### Regular Schedule (No Bus Service)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Lounges on her couch in the trailer . |
| 12:00 PM | Leaves the trailer and heads to JojaMart . |
| 4:00 PM | Leaves JojaMart and heads to the saloon . |
| 12:00 AM | Leaves the saloon and heads home. |

##### Regular Schedule (Bus Service Restored)

###### Regular Schedule (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:00 AM | Lounges on her couch in the trailer . |
| 8:30 AM | Leaves the trailer to head to the bus stop just east of the farm . |
| 10:00 AM | Arrives at the bus stop for the afternoon. |
| 5:00 PM | Leaves the bus stop and heads to the saloon . |
| 12:00 AM | Leaves the saloon and back home for the night. |

<a id="npc-schedule-pierre"></a>

### 29. 皮埃尔（Pierre）

> 来源：中文 revision 55086；英文 revision 192883
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 6 个分区、6 个条件分支、29 行。

- 每天9:00至17:00，都可以在 皮埃尔的杂货店 中找到皮埃尔（但星期三时商店会关门）。周五晚上下班后，他会到 星之果实酒吧 犒劳自己。其他时间下班后，他离开商店柜台，在家里走动。
- 社区中心 重建后， 皮埃尔的杂货店 不再在周三休息，即一周中的每一天都会营业。
- 姜岛的海滩度假村 解锁后，皮埃尔可能会前往姜岛。他会在杂货店里留下一个钱箱，所以玩家仍然能够进行购物。18:00离开姜岛后，皮埃尔会立刻回家上床睡觉。皮埃尔不会在 节日 当天前往姜岛。
- 以下是皮埃尔的日程安排，优先度从高到低排序。

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于家里的客厅。 |

##### 春季15日（巴士站已修复）

###### 春季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 站在杂货店的柜台后方。 |
| 07:00 | 走向杂货店的货架。 |
| 08:30 | 回到杂货店的柜台后方。 |
| 18:00 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 18:50 | 站在 绿洲 门外。 |
| 01:40 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 站在杂货店的柜台后方。 |
| 07:00 | 走向杂货店的货架。 |
| 08:30 | 回到杂货店的柜台后方。 |
| 17:00 | 离开柜台，走向杂货店的货架。 |
| 19:00 | 走向家中的厨房。 |
| 21:00 | 走进他的卧室，站在书架前。 |
| 23:00 | 上床睡觉。 |

##### 星期五

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 站在杂货店的柜台后方。 |
| 07:00 | 走向杂货店的货架。 |
| 08:30 | 回到杂货店的柜台后方。 |
| 17:00 | 走向 星之果实酒吧 ，站在酒吧柜台前。 |
| 22:50 | 回家睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 站在杂货店的柜台后方。 |
| 07:00 | 走向杂货店的货架。 |
| 08:30 | 回到杂货店的柜台后方。 |
| 17:00 | 离开柜台，走向杂货店的货架。 |
| 19:00 | 走向家中的厨房。 |
| 21:00 | 走进他的卧室，站在书架前。 |
| 23:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 6 个分区、6 个条件分支、29 行。

- Pierre can be found running his general store each day between 9am and 5pm (except Wednesday when the store is closed). After the Community Center has been fully restored his store will be open every day of the week.
- After the Beach Resort on Ginger Island is unlocked, Pierre may randomly spend the day there. (He will leave a cash box on the counter of the store , so the player is still able to make purchases.) After leaving the Island at 6pm, Pierre will immediately go home to bed. Pierre never visits the Resort on Festival days.

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the living room. |

##### Spring 15 (Bus Service Restored)

###### Spring 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Stands behind the counter of the general store. |
| 7:00 AM | In the aisles of the general store. |
| 8:30 AM | Goes to stand behind the counter of the general store. |
| 6:00 PM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 6:50 PM | Stands outside the Oasis . |
| 1:40 AM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and boards bus back to the Valley. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Stands behind the counter of the general store. |
| 7:00 AM | In the aisles of the general store. |
| 8:30 AM | Goes to stand behind the counter of the general store. |
| 5:00 PM | Leaves the counter and stands in the aisles again. |
| 7:00 PM | Goes to the kitchen in his house. |
| 9:00 PM | Goes to his room and stands in front of the bookcase. |
| 11:00 PM | Goes to sleep. |

##### Friday

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Stands behind the counter of the general store. |
| 7:00 AM | In the aisles of the general store. |
| 8:30 AM | Goes to stand behind the counter of the general store. |
| 5:00 PM | Goes to the Stardrop Saloon and stands in front of the counter. |
| 10:50 PM | Returns home to sleep. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | Stands behind the counter of the general store. |
| 7:00 AM | In the aisles of the general store. |
| 8:30 AM | Goes to stand behind the counter of the general store. |
| 5:00 PM | Leaves the counter and stands in the aisles again. |
| 7:00 PM | Goes to the kitchen in his house. |
| 9:00 PM | Goes to his room and stands in front of the bookcase. |
| 11:00 PM | Goes to sleep. |

<a id="npc-schedule-robin"></a>

### 30. 罗宾（Robin）

> 来源：中文 revision 55090；英文 revision 191769
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 10 个分区、10 个条件分支、43 行。

- 通常情况下，罗宾在08:00起床并走向 木匠的商店 的柜台，8:20即开始营业。商店在17:00结束营业，她通常在19:30左右回到卧室，并在21:00上床睡觉。星期五晚上，她会在16:00提前结束营业，然后和 德米特里厄斯 一起去 星之果实酒吧 跳舞。
- 罗宾每周二会去 皮埃尔的杂货店 和 乔迪 、 卡洛琳 、 艾米丽 、 玛妮 一起健身，因此， 木匠的商店 每周二不营业。不过，如果玩家在她经过柜台时（9:40左右）点击柜台，仍可暂时访问商店页面。
- 罗宾通常不会在雨天离开 木匠的商店 ，除非她需要建造 农场建筑 。当她在玩家的 农场 上建造或升级建筑物时，她的商店暂停营业。
- 姜岛的海滩度假村 解锁后，罗宾有时会在周二去那儿。18:00离开姜岛后，罗宾会立即回家上床睡觉。罗宾不会在 节日 当天去姜岛。
- 以下是她的日程安排，优先级从高到低（例如，如果当天下雨，雨天的时间表会比下方的优先级更高）。

##### 春季16日（巴士站已修复）

###### 春季16日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 11:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 11:40 | 在探险家工会挑战摊位与 马龙 和 吉尔 交谈。 |
| 00:20 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达她的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 塞巴斯蒂安 的房间。 |

##### 夏季18日

###### 夏季18日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 07:00 | 走向 木匠的商店 的柜台。 |
| 08:00 | 离开柜台，前往 哈维的诊所 。 |
| 16:00 | 离开哈维的诊所，回 家 。 |
| 21:00 | 上床睡觉。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 08:00 | 走向 木匠的商店 的柜台。 |
| 17:00 | 离开商店的柜台，前往家中的厨房。 |
| 19:30 | 进入她的卧室。 |
| 21:00 | 上床睡觉。 |

##### 星期一（社区中心已修复）

###### 星期一（社区中心已修复）

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 08:00 | 走向 木匠的商店 的柜台。 |
| 17:00 | 离开 木匠的商店 ，前往 社区中心 。 |
| 19:30 | 离开社区中心，回 家 。 |
| 22:00 | 上床睡觉。 |

##### 冬季16日

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 08:00 | 走向 木匠的商店 的柜台。 |
| 17:00 | 离开木匠的商店，参加 夜市 。 |
| 23:30 | 离开夜市，回家睡觉。 |

##### 星期二

###### 星期二

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 09:30 | 走向 皮埃尔的杂货店 。 |
| 13:00 | 开始锻炼。 |
| 16:00 | 结束锻炼，与 乔迪 、 卡洛琳 、 玛妮 一起聊天。 |
| 18:00 | 离开皮埃尔的杂货店，回到 自己家的厨房 。 |
| 19:30 | 离开厨房，走到卧室。 |
| 21:00 | 上床睡觉。 |

##### 星期五

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 08:00 | 走向 木匠的商店 的柜台。 |
| 16:00 | 离开木匠的商店，前往 星之果实酒吧 。 |
| 19:20 | 在星之果实酒吧中，与 德米特里厄斯 跳舞。 |
| 21:00 | 离开 星之果实酒吧 ，回 家 睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 06:00 | 在她的卧室里。 |
| 08:00 | 走向 木匠的商店 的柜台。 |
| 17:00 | 离开木匠的商店，站在 深山 西南部的悬崖前。 |
| 19:30 | 走回她的卧室。 |
| 21:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 10 个分区、10 个条件分支、43 行。

- Robin's shop is closed on Tuesday while she has a weekly exercise class at Caroline 's home. However, if you stand in her path on her way out (near the cash register at 9:40am), you can use her shop momentarily. You can also access her shop when she is returning around 8pm, by clicking the register while she is right behind you.
- Robin won't leave her home on days when it's raining unless she has been hired to construct a farm building . Her shop will be closed for the days that she is on the Farm completing the construction.
- After the Beach Resort on Ginger Island is unlocked, Robin may randomly spend Tuesday there. After leaving the Island at 6pm, Robin will immediately go home to bed. Robin never visits the Resort on Festival days.
- Shown below are Robin's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring 16 (Bus Service Restored)

###### Spring 16 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 11:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 11:40 AM | Chats with Marlon and Gil at the Adventurer's Guild challenge booth. |
| 12:20 AM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at her booth . |
| 12:00 AM | Leaves booth and takes bus back to the Valley. |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In Sebastian 's room. |

##### Summer 18

###### Summer 18

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 7:00 AM | Walks to the counter of her shop . |
| 8:00 AM | Leaves home and walks to Harvey's Clinic . |
| 4:00 PM | Leaves Harvey's Clinic and walks home . |
| 9:00 PM | Goes to bed. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 8:00 AM | Walks to the counter of her shop . |
| 5:00 PM | Leaves the counter of her shop and walks to the kitchen. |
| 7:30 PM | Walks to her bedroom. |
| 9:00 PM | Goes to bed. |

##### Monday (Community Center Restored)

###### Monday (Community Center Restored)

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 8:00 AM | Walks to the counter of her shop . |
| 5:00 PM | Leaves her shop and walks to the Community Center . |
| 7:30 PM | Leaves Community Center to return home . |
| 10:00 PM | Goes to bed. |

##### Winter 16

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 8:00 AM | Walks to the counter of her shop . |
| 5:00 PM | Leaves her shop to attend Night Market . |
| 11:30 PM | Leaves Night Market to return home. |

##### Tuesday

###### Tuesday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 9:30 AM | Walks towards Pierre's General Store . |
| 1:00 PM | Starts to exercise. |
| 4:00 PM | Finishes the exercise, talks with Jodi , Caroline , and Marnie . |
| 6:00 PM | Leaves Pierre's General Store and walks back to the kitchen . |
| 7:30 PM | Leaves the kitchen and walks to her bedroom. |
| 9:00 PM | Goes to bed. |

##### Friday

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 8:00 AM | Walks to the counter of her shop . |
| 4:00 PM | Leaves her shop and walks to the Stardrop Saloon . |
| 7:20 PM | At the Stardrop Saloon , dancing with Demetrius . |
| 9:00 PM | Leaves the Stardrop Saloon and walks home to go to bed. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 6:00 AM | In her bedroom at home . |
| 8:00 AM | Walks to the counter of her shop . |
| 5:00 PM | Leaves her shop and heads outside to the Mountain area. |
| 7:30 PM | Leaves the Mountain and walks into her bedroom. |
| 9:00 PM | Goes to bed. |

<a id="npc-schedule-sandy"></a>

### 31. 桑迪（Sandy）

> 来源：中文 revision 55081；英文 revision 191345
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 3 个分区、3 个条件分支、15 行。

- 桑迪通常不会离开 绿洲 ，除了在她生日（秋季15日）那天。其他时间只要在商店营业时间内（09:00到23:50），都可以在 绿洲 找到她。
- 如果 巴士站 已修复，在秋季15日这一天，绿洲会在上午营业，但在13:00，桑迪会离开商店，与艾米丽一起在沙漠中散步。
- 桑迪不会去 姜岛的海滩度假村 。

##### 春季15日、16日和17日（巴士站已修复）

###### 春季15日、16日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 08:30 | 离开 绿洲 ，站在 艾米丽 的 服装服务 小屋前。 |
| 00:00 | 返回绿洲。 |

##### 秋季15日（巴士站已修复）

###### 秋季15日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 在 绿洲 的柜台后方。 |
| 12:00 | 在柜台后方，侧身与 艾米丽 聊天。 |
| 13:00 | 离开绿洲商店，和艾米丽一起站在绿洲前的长椅旁。 |
| 15:00 | 从绿洲走到沙漠西北方的池塘旁。 |
| 17:00 | 从池塘走到 沙之巨龙 旁。 |
| 18:00 | 从沙之巨龙走到沙漠中的巴士旁。 |
| 19:00 | 从巴士走到 沙漠商人 旁。 |
| 20:00 | 返回 绿洲 门口。 |
| 22:50 | 离开 绿洲 门口。 |
| 23:30 | 到达巴士旁的长椅处。 |
| 00:00 | 送别 艾米丽 。 |
| 00:10 | 返回 绿洲 。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 全天 | 在 绿洲 的柜台后方。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 3 个分区、3 个条件分支、15 行。

- Sandy does not leave the Oasis , and can be found there when the store is open, from 9am to 11:50pm except on her birthday, Fall 15. On Fall 15, the Oasis is open in the morning but at 1pm Sandy leaves to walk around the desert with Emily.
- Sandy never visits the Beach Resort on Ginger Island.

##### Spring 15, 16 and 17 (Bus Service Restored)

###### Spring 15, 16 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 8:30 AM | Exits the Oasis to stand at Emily's outfit services . |
| 12:00 AM | Returns to the Oasis. |

##### Fall 15 (Bus Service Restored)

###### Fall 15 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Stands behind the counter in the Oasis . |
| 12:00 PM | Chats sideways with Emily behind the counter. |
| 1:00 PM | Leaves the Oasis and stands next to the bench on the left. |
| 3:00 PM | Goes to the pond in the northwest section. |
| 5:00 PM | Leaves and then stands next to the Sand Dragon . |
| 6:00 PM | Goes to the side of the bus. |
| 7:00 PM | Moves to the front of the Desert Trader . |
| 8:00 PM | Returns to the front of the Oasis . |
| 10:50 PM | Leaves the front of the Oasis . |
| 11:30 PM | Arrives by the bench next to the bus. |
| 12:00 AM | Says goodbye to Emily . |
| 12:10 AM | Goes back to the Oasis . |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| All day | Behind the counter at the Oasis . |

<a id="npc-schedule-vincent"></a>

### 32. 文森特（Vincent）

> 来源：中文 revision 55079；英文 revision 193876
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 11 个分区、11 个条件分支、49 行。

- 大多数日子文森特在9:00醒来，然后前往 镇 上玩几个小时。他通常晚上七点左右回家。星期二，星期三和星期五他会和 贾斯 、 潘妮 一起在 博物馆 里度过下午。 夏季 期间潘妮不给孩子上课，这时文森特常常在 沙滩 上。
- 当下雨时，文森特不会离开 家 ，除非当天是春季的11号。
- 姜岛 海滩度假村 修复后，文森特偶尔会去度个假，18:00离开小岛后，文森特将立即回家睡觉。文森特不会在星期二、星期三、星期五、节日或诊所预约日当天去度假。文森特也不会在没有成年人陪同的情况下前往度假村。
- 下面展示的是文森特的日程表，从上到下优先级逐次下降。例如，下雨时，雨天的行程安排优先级会比其下方的更高。

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 在 家 里的客厅。 |

##### 每个季节9日和23日

###### 每个季节9日和23日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床。 |
| 11:00 | 在 家 玩。 |
| 14:00 | 离开家 家 前往 镇上的广场 。 |
| 17:00 | 离开 小镇 回 家 。 |
| 19:00 | 在 家 玩。 |
| 22:00 | 上床睡觉。 |

##### 春季11日

###### 春季11日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床，对看 医生 感到忧虑。 |
| 11:30 | 离开 家 前往 诊所 ，之后进入候诊室。 |
| 13:30 | 进入 诊所 检查室。 |
| 16:00 | 离开 诊所 后回 家 ，然后一直在家玩耍。 |
| 22:00 | 上床睡觉。 |

##### 春季17日（巴士站已修复）

###### 春季17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 10:20 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 10:30 | 与他的 母亲 一起站在其中一个村民 商店摊位 前。 |
| 00:10 | 乘坐巴士返回星露谷。 |

##### 沙漠节（作为商店摊主）

###### 沙漠节（作为商店摊主）

| 时间 | 地点/行动 |
|------|------|
| 11:10 | 乘坐巴士前往 沙漠 。 |
| 11:30 | 到达他的 商店摊位 。 |
| 00:00 | 离开摊位并乘坐巴士返回星露谷。 |

##### 冬季16日

###### 冬季16日

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床。 |
| 11:00 | 在 家 玩。 |
| 14:00 | 离开家 家 前往 镇上的广场 。 |
| 16:30 | 前往 沙滩 参加 夜市 。 |
| 23:30 | 回家睡觉。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床。 |
| 11:00 | 在 家 玩。 |
| 14:00 | 在 家 里闲逛。 |
| 17:00 | 在 家 里闲逛。 |
| 19:00 | 在 家 玩。 |
| 22:00 | 上床睡觉。 |

##### 夏季

###### 夏季

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床。 |
| 11:00 | 在 家 玩。 |
| 13:40 | 离开 家 前往 沙滩 。 |
| 19:00 | 离开 沙滩 回 家 。 |
| 23:00 | 上床睡觉。 |

##### 星期二、星期三、星期五

###### 星期二、星期三、星期五

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 离开 家 前往 博物馆 ， 潘妮 会给他上课。 |
| 14:00 | 离开 博物馆 回到 鹈鹕镇 。 |
| 16:20 | 在 鹈鹕镇 闲逛。 |
| 17:40 | 回 家 。 |
| 22:00 | 上床睡觉。 |

##### 星期六

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 10:10 | 离开 家 前往 鹈鹕镇 。 |
| 12:00 | 前往 镇上的广场 。 |
| 17:00 | 离开 镇广场 ，在 鹈鹕镇 闲逛。 |
| 22:00 | 离开 镇广场 回家睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 起床。 |
| 11:00 | 在 家 玩。 |
| 14:00 | 离开 家 前往 鹈鹕镇 。 |
| 17:00 | 离开 鹈鹕镇 回 家 。 |
| 19:00 | 在 家 玩。 |
| 22:00 | 上床睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 11 个分区、11 个条件分支、49 行。

- On Tuesday, Wednesday and Friday, Vincent and Jas spend the afternoon with Penny being tutored at the museum . During Summer , Vincent is often at the beach .
- Vincent won't leave his home on rainy days, unless it's Spring 11, when he visits Harvey's Clinic .
- After the Beach Resort on Ginger Island is unlocked, Vincent may randomly spend the day there. After leaving the Island at 6pm, Vincent will immediately go home to bed. Vincent never visits the Resort on Tuesdays, Wednesdays, Fridays, Festival days or his checkup day at Harvey's Clinic . Vincent also never visits the Resort without an adult accompanying him.
- Shown below are Vincent's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In the living room. |

##### Tuesday the 9th and Tuesday the 23rd

###### Tuesday the 9th and Tuesday the 23rd

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up for the day. |
| 11:00 AM | Plays inside his home . |
| 2:00 PM | Leaves his home and heads outside to the town square . |
| 5:00 PM | Leaves town and walks home . |
| 7:00 PM | Plays inside his home . |
| 10:00 PM | Goes to bed for the night. |

##### Spring 11

###### Spring 11

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up, concerned about having to go to the doctor . "*sob*... I have to get my shots today." |
| 11:30 AM | Leaves home to travel to the clinic for his annual checkup. "*gulp*... Mommy, don't make me do it." |
| 1:30 PM | Continues checkup at the clinic . "Do I get a lollipop for being so brave?" |
| 4:00 PM | Leaves the clinic to walk home , once there he plays inside. |
| 10:00 PM | Goes to bed for the night. |

##### Spring 17 (Bus Service Restored)

###### Spring 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 10:20 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 10:30 AM | With his mom by one of the villager shops. |
| 12:10 AM | Boards the bus back to the Valley. |

##### Desert Festival (As Vendor)

###### Desert Festival (As Vendor)

| 时间 | 地点/行动 |
|------|------|
| 11:10 AM | Boards the bus to Calico Desert . |
| 11:30 AM | Arrives at his booth . |
| 12:00 AM | Leaves booth and takes the bus back to the Valley. |

##### Winter 16

###### Winter 16

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up for the day. |
| 11:00 AM | Plays inside his home . |
| 2:00 PM | Leaves his home and heads outside to the town square . |
| 4:30 PM | Attends the Night Market . |
| 11:30 PM | Goes to bed for the night. |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up for the day. |
| 11:00 AM | Plays inside his home . |
| 2:00 PM | Moves around inside his home . |
| 5:00 PM | Moves around inside his home . |
| 7:00 PM | Plays inside his home . |
| 10:00 PM | Goes to bed for the night. |

##### Summer

###### Summer

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up for the day. |
| 11:00 AM | Plays inside his home . |
| 1:40 PM | Leaves his home and heads to The Beach . |
| 7:00 PM | Leaves The Beach and walks back home . |
| 11:00 PM | Goes to bed for the night. |

##### Tuesday, Wednesday and Friday

###### Tuesday, Wednesday and Friday

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Leaves his home and walks to the Museum to be tutored by Penny . |
| 2:00 PM | Leaves the Museum , walks back to Pelican Town . |
| 4:20 PM | Walks around Pelican Town . |
| 5:40 PM | Leaves town to go home . |
| 10:00 PM | Goes to bed for the night. |

##### Saturday

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 10:10 AM | Leaves his home and heads outside to Pelican Town . |
| 12:00 PM | Heads to the town square . |
| 5:00 PM | Leaves the town square and walks around Pelican Town . |
| 10:00 PM | Leaves town to go home to bed for the night. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Wakes up for the day. |
| 11:00 AM | Plays inside his home . |
| 2:00 PM | Leaves his home and heads outside to the town square . |
| 5:00 PM | Leaves town and walks home . |
| 7:00 PM | Plays inside his home . |
| 10:00 PM | Goes to bed for the night. |

<a id="npc-schedule-willy"></a>

### 33. 威利（Willy）

> 来源：中文 revision 55075；英文 revision 192689
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 11 个分区、11 个条件分支、44 行。

- 大多数时候，威利都会在6:10左右起床，随后在 沙滩 上钓几个小时的鱼。接着在09:00到17:00之间，他都会在 鱼店 里营业。鱼店打烊后，他通常会继续在 沙滩 再钓会儿鱼，直到22:00。冬季时，他会在鱼店打烊后去 星之果实酒吧 而不是 沙滩 。
- 如果星期六不下雨，威利会把鱼店关了然后出门钓鱼，只有下雨时 鱼店 才会继续营业。
- 威利不会前往姜岛的 海滩度假村 。
- 下面显示的是威利的行程表，从上到下优先级逐次下降，比如下雨时行程安排的优先级就会比它下面的高。如果是一个下雨的星期五，那么威利会按照下雨时的行程表行动。

##### 春季9日

###### 春季9日

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 09:00 | 开始在 鱼店 的柜台前工作，此时玩家可以在他那里购买物品。 |
| 10:10 | 离开 鱼店 ，前往 哈维的诊所 的候诊室。 |
| 13:30 | 前往诊所的检查室体检。 |
| 17:00 | 离开 哈维的诊所 ，前往 星之果实酒吧 。 |
| 23:20 | 回家睡觉。 |

##### 春季15日、16日和17日（巴士站已修复）

###### 春季15日、16日和17日（巴士站已修复）

| 时间 | 地点/行动 |
|------|------|
| 09:00 | 乘坐巴士前往 沙漠 参加 沙漠节 。 |
| 09:10 | 站在他的 钓鱼挑战板 前。 |

##### 夏季20日和21日

###### 夏季20日和21日

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 10:00 | 离开 沙滩 前往 煤矿森林 ，在 莉亚的农舍 西南方的河边钓鱼参与 鳟鱼大赛 。 |
| 23:20 | 离开 煤矿森林 ，回家睡觉。 |

##### 冬季12日和13日

###### 冬季12日和13日

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 12:00 | 前往 沙滩 ，在 鱼店 外钓鱼参与 鱿鱼节 。 |
| 23:20 | 离开 沙滩 ，回家睡觉。 |

##### 冬季15日、16日和17日

###### 冬季15日、16日和17日

| 时间 | 地点/行动 |
|------|------|
| 16:30 | 前往 星之果实酒吧 。 |
| 00:20 | 回家睡觉。 |

##### 绿雨（第一年）

###### 绿雨（第一年）

| 时间 | 地点/行动 |
|------|------|
| 全天 | 位于 星之果实酒吧 。 |

##### 雨天

###### 雨天

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 09:00 | 开始在 鱼店 的柜台前工作，此时玩家可以在他那里购买物品。 |
| 17:00 | 离开 鱼店 ，前往 星之果实酒吧 。 |
| 23:20 | 离开酒吧，回家睡觉。 |

##### 星期五

###### 星期五

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 09:00 | 开始在 鱼店 的柜台前工作，此时玩家可以在他那里购买物品。 |
| 17:00 | 离开 鱼店 ，前往 星之果实酒吧 。 |
| 23:20 | 离开酒吧，回家睡觉。 |

##### 星期六

###### 星期六

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，沿着小镇去 莉亚的农舍 外的河边钓鱼。 |
| 14:00 | 离开 河边 朝 鹈鹕镇 走，去河边垂钓。 |
| 19:00 | 前往 星之果实酒吧 。 |
| 23:00 | 离开酒吧，回家睡觉。 |

##### 冬季

###### 冬季

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 09:00 | 开始在 鱼店 的柜台前工作，此时玩家可以在他那里购买物品。 |
| 17:00 | 离开 鱼店 ，前往 星之果实酒吧 。 |
| 23:20 | 离开酒吧，回家睡觉。 |

##### 日常时间表

###### 日常时间表

| 时间 | 地点/行动 |
|------|------|
| 06:10 | 起床，在 鱼店 外钓鱼。 |
| 08:50 | 从 沙滩 回到 鱼店 里。 |
| 09:00 | 开始在 鱼店 的柜台前工作，此时玩家可以在他那里购买物品。 |
| 17:00 | 离开 鱼店 ，出门去 沙滩 钓鱼。 |
| 22:00 | 回家睡觉。 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 11 个分区、11 个条件分支、44 行。

- Most days Willy fishes at the beach for a few hours before operating his fish shop between 9am and 5pm. During winter he'll go to the saloon after work.
- Willy's shop is closed on Saturday while he's out fishing unless it's raining. Willy never visits the Beach Resort on Ginger Island, though he ferries other villagers to and from the Island.
- Shown below are Willy's schedules prioritized highest to lowest. For example, if it is raining, that schedule overrides all others below it.

##### Spring 9

###### Spring 9

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Goes back inside fish shop from the beach . |
| 9:00 AM | Starts working at the counter in the fish shop , goods are available for sale. "I have a doctor's appointment today, so if you need to buy anything you'd better hurry." |
| 10:10 AM | Leaves the fish shop , walks over to the Harvey's Clinic . "Eh, I got a fish hook stuck in my thumb... the Doctor's gonna cut it out." |
| 1:30 PM | Continues checkup at the Harvey's Clinic . "Yowch! That hurt, Doc!" |
| 5:00 PM | Leaves the Harvey's Clinic , walks over to the saloon . "I need a little warm-me-up to be ready for another cold night on the ocean." |
| 11:20 PM | Leaves the saloon to head home for the night. |

##### Spring 15, 16 and 17 (Bus Service Restored)

###### Spring 15, 16 and 17 (Bus Service Restored)

| 时间 | 地点/行动 |
|------|------|
| 9:00 AM | Boards the bus to Calico Desert to attend the Desert Festival . |
| 9:10 AM | Stands at his fishing challenge. |

##### Summer 20 and 21

###### Summer 20 and 21

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Returns to the fish shop . |
| 10:00 AM | Leaves the beach , goes to Cindersap Forest to fish in the Trout Derby in the river to the southwest of Leah's Cottage . |
| 11:20 PM | Leaves Cindersap Forest to head home for the night. |

##### Winter 12 and 13

###### Winter 12 and 13

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Returns to the fish shop . |
| 12:00 PM | Heads out to the beach to fish in the SquidFest . |
| 11:20 PM | Leaves the beach to head home for the night. |

##### Winter 15, 16 and 17

###### Winter 15, 16 and 17

| 时间 | 地点/行动 |
|------|------|
| 4:30 PM | At The Stardrop Saloon . |
| 12:20 AM | Returns to the fish shop . |

##### Green Rain (Year 1)

###### Green Rain (Year 1)

| 时间 | 地点/行动 |
|------|------|
| All day | In The Stardrop Saloon . |

##### Rain

###### Rain

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Goes back inside fish shop from the beach . |
| 9:00 AM | Starts working at the counter in the fish shop , goods are available for sale. |
| 5:00 PM | Leaves the fish shop , walks over to the saloon . "I need a little warm-me-up to be ready for another cold night on the ocean." |
| 11:20 PM | Leaves the saloon to head home for the night. |

##### Friday

###### Friday

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Goes back inside fish shop from the beach . |
| 9:00 AM | Starts working at the counter in the fish shop , goods are available for sale. |
| 5:00 PM | Leaves the fish shop , walks over to the saloon . "Handling salty fish all day makes me real thirsty." |
| 11:20 PM | Leaves the saloon to head home for the night. |

##### Saturday

###### Saturday

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, walks through town to go fishing at the river outside Leah's cottage . |
| 2:00 PM | Leaves the river and heads into Pelican Town for more river fishing. |
| 7:00 PM | Walks over to the saloon . "Ah... Nothing's better than kicking back with a cold one after a relaxing day fishing." |
| 11:00 PM | Leaves the saloon to head home for the night. |

##### Winter

###### Winter

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Goes back inside fish shop from the beach . |
| 9:00 AM | Starts working at the counter in the fish shop , goods are available for sale. |
| 5:00 PM | Leaves the fish shop , walks over to the saloon . "I need a little warm-me-up to be ready for another cold night on the ocean." |
| 11:20 PM | Leaves the saloon to head home for the night. |

##### Regular Schedule

###### Regular Schedule

| 时间 | 地点/行动 |
|------|------|
| 6:10 AM | Wakes up for the day, goes fishing outside his fish shop . |
| 8:50 AM | Goes back inside fish shop from the beach . |
| 9:00 AM | Starts working at the counter in the fish shop , goods are available for sale. |
| 5:00 PM | Leaves the fish shop , goes out to fish on the beach . |
| 10:00 PM | Leaves the beach to head home for the night. |

<a id="npc-schedule-wizard"></a>

### 34. 法师（Wizard）

> 来源：中文 revision 55012；英文 revision 193912
>
> 结构判定：中英文分区、条件组和行数签名一致；两源仍完整并列

#### 中文记录源（完整保留）

> 0 个分区、0 个条件分支、0 行。

- 法师不会离开 法师塔 （除了节日)，随时可以在塔的开放时间（06:00至23:00）内找到他。在玩家解锁 女巫小屋 后，可以通过女巫小屋内的传送阵传送到法师塔，可以发现法师在23:00后仍呆在塔中。

源页没有分时表；以上文字即该源的完整日程说明。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 0 个分区、0 个条件分支、0 行。

- The Wizard does not leave the Wizard's Tower (except for certain Festival days), and can be found there when the tower is accessible (6am to 11pm). After the player has unlocked the Witch's Hut , he can be found in his tower after 11pm by using the warp spot in the Witch's Hut . The Wizard never visits the Beach Resort on Ginger Island.

源页没有分时表；以上文字即该源的完整日程说明。

## 来源与审计方法

- [Villagers — 官方 34 位可送礼居民名册](https://stardewvalleywiki.com/Villagers)
- [Modding:Schedule data — 日程键优先级与时间地点字段](https://stardewvalleywiki.com/Modding:Schedule_data)
- 每位居民的中英文固定 revision 链接见索引表。
- 生成器要求 34/34 人存在日程章节，并逐人比较中英文分区/分支/行数签名；所有中英文记录均进入本文。
- 任何居民缺页、缺日程章节、空条件表，或结构差异居民集合偏离已审计的 6 人基线，都会使生成失败。

---

[上一篇：NPC关系数值总览](./NPC关系数值总览.md) · [返回NPC数据总览](./NPC数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：作物数据总览](./作物数据总览.md)
