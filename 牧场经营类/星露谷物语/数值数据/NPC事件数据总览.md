[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > [NPC数据总览](./NPC数据总览.md) > NPC事件数据总览

# NPC事件数据总览 — 星露谷物语

> 游戏版本：Stardew Valley PC v1.6.15
>
> 数据来源：英文 Stardew Valley Wiki 个人页为完整性主源；中文个人页为中文记录源
>
> 生成时逐人固定中英文 revision；两种语言的全部触发段落、详情叙述、选择和结果表均保留

## 数据覆盖声明

| 项目 | 内容 |
|------|------|
| 数据全集定义 | 官方 Villagers 名册中 34 位可送礼居民个人页的完整 Heart Events/爱心事件章节 |
| 预计居民数 | 34 |
| 实际居民数 | 34 |
| 数量差异 | 0 |
| 英文主源 | 178 个事件/后续条目 / 199 个外层段落 / 175 张详情表 / 260 个列表或选择项 / 60 张嵌套表（116 行） |
| 中文记录源 | 178 个事件/后续条目 / 215 个外层段落 / 175 张详情表 / 249 个列表或选择项 / 63 张嵌套表（118 行） |
| 必填字段 | 居民、来源 revision、事件标题/心数、触发条件、详情、选择、友情点及其他后果 |
| 中英文事件数量一致 | 34/34 人；178/178 个事件或后续条目 |
| 深层结构一致 | 16/34 人 |
| 已审计深层结构差异 | 18/34 人；双源完整并列，不静默覆盖 |
| 排除边界 | 12 位不可送礼 NPC 不属于个人爱心事件全集；装饰性心数/物品缩略图不重复收录 |
| 验收状态 | **NPC 爱心事件子域已完成** |

### 读取与裁定说明

本文把个人页 Heart Events/爱心事件章节中的所有标题视为全集条目，包括标准心数过场、Anytime 邮件、0 心事件、分段事件、群体 10 心、婚后 14 心和事件后续。

事件标题后的外层段落通常给出地点、时间、天气、季节、日期、关系状态与前置事件；折叠详情表保留剧情、所有选项、友情点变化、配方/物品/邮件及其他后果。中英文结构或内容不同时，以英文主源判断 PC v1.6.15 行为，中文记录仍完整保留。

## 居民索引与数量对账

| # | 居民 | 英文（事件/段落/详情/列表/嵌套表行） | 中文（事件/段落/详情/列表/嵌套表行） | 深层结构 | 中文 revision | 英文 revision |
|:--:|------|:--:|:--:|:--:|:--:|:--:|
| 1 | [亚历克斯（Alex）](#npc-event-alex) | 8/9/8/13/0 | 8/11/8/13/0 | 差异已审计 | [zh 55068](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E4%BA%9A%E5%8E%86%E5%85%8B%E6%96%AF&oldid=55068) | [en 193663](https://stardewvalleywiki.com/mediawiki/index.php?title=Alex&oldid=193663) |
| 2 | [艾利欧特（Elliott）](#npc-event-elliott) | 7/8/7/18/0 | 7/9/7/18/0 | 差异已审计 | [zh 55231](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%89%BE%E5%88%A9%E6%AC%A7%E7%89%B9&oldid=55231) | [en 192964](https://stardewvalleywiki.com/mediawiki/index.php?title=Elliott&oldid=192964) |
| 3 | [哈维（Harvey）](#npc-event-harvey) | 7/8/7/9/0 | 7/9/7/9/0 | 差异已审计 | [zh 54980](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%93%88%E7%BB%B4&oldid=54980) | [en 193951](https://stardewvalleywiki.com/mediawiki/index.php?title=Harvey&oldid=193951) |
| 4 | [山姆（Sam）](#npc-event-sam) | 8/9/8/21/0 | 8/10/8/21/0 | 差异已审计 | [zh 55076](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%B1%B1%E5%A7%86&oldid=55076) | [en 193676](https://stardewvalleywiki.com/mediawiki/index.php?title=Sam&oldid=193676) |
| 5 | [塞巴斯蒂安（Sebastian）](#npc-event-sebastian) | 7/8/7/26/0 | 7/9/7/29/0 | 差异已审计 | [zh 55064](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%A1%9E%E5%B7%B4%E6%96%AF%E8%92%82%E5%AE%89&oldid=55064) | [en 193877](https://stardewvalleywiki.com/mediawiki/index.php?title=Sebastian&oldid=193877) |
| 6 | [谢恩（Shane）](#npc-event-shane) | 12/14/12/11/6 | 12/16/12/2/8 | 差异已审计 | [zh 55046](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%B0%A2%E6%81%A9&oldid=55046) | [en 193586](https://stardewvalleywiki.com/mediawiki/index.php?title=Shane&oldid=193586) |
| 7 | [阿比盖尔（Abigail）](#npc-event-abigail) | 8/10/7/16/0 | 8/11/7/15/0 | 差异已审计 | [zh 55185](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E9%98%BF%E6%AF%94%E7%9B%96%E5%B0%94&oldid=55185) | [en 193689](https://stardewvalleywiki.com/mediawiki/index.php?title=Abigail&oldid=193689) |
| 8 | [艾米丽（Emily）](#npc-event-emily) | 10/14/10/3/8 | 10/15/10/3/8 | 差异已审计 | [zh 55091](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%89%BE%E7%B1%B3%E4%B8%BD&oldid=55091) | [en 191968](https://stardewvalleywiki.com/mediawiki/index.php?title=Emily&oldid=191968) |
| 9 | [海莉（Haley）](#npc-event-haley) | 7/9/7/15/1 | 7/9/7/15/1 | 一致 | [zh 55013](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%B5%B7%E8%8E%89&oldid=55013) | [en 191939](https://stardewvalleywiki.com/mediawiki/index.php?title=Haley&oldid=191939) |
| 10 | [莉亚（Leah）](#npc-event-leah) | 10/10/9/26/0 | 10/11/9/30/0 | 差异已审计 | [zh 55041](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%8E%89%E4%BA%9A&oldid=55041) | [en 192966](https://stardewvalleywiki.com/mediawiki/index.php?title=Leah&oldid=192966) |
| 11 | [玛鲁（Maru）](#npc-event-maru) | 7/8/7/19/0 | 7/9/7/19/0 | 差异已审计 | [zh 55085](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%8E%9B%E9%B2%81&oldid=55085) | [en 193560](https://stardewvalleywiki.com/mediawiki/index.php?title=Maru&oldid=193560) |
| 12 | [潘妮（Penny）](#npc-event-penny) | 7/8/7/42/0 | 7/9/7/38/0 | 差异已审计 | [zh 55083](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%BD%98%E5%A6%AE&oldid=55083) | [en 193516](https://stardewvalleywiki.com/mediawiki/index.php?title=Penny&oldid=193516) |
| 13 | [卡洛琳（Caroline）](#npc-event-caroline) | 5/5/5/8/6 | 5/5/5/8/6 | 一致 | [zh 54977](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%8D%A1%E6%B4%9B%E7%90%B3&oldid=54977) | [en 191301](https://stardewvalleywiki.com/mediawiki/index.php?title=Caroline&oldid=191301) |
| 14 | [克林特（Clint）](#npc-event-clint) | 5/5/5/4/6 | 5/6/5/4/6 | 差异已审计 | [zh 55070](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%85%8B%E6%9E%97%E7%89%B9&oldid=55070) | [en 191347](https://stardewvalleywiki.com/mediawiki/index.php?title=Clint&oldid=191347) |
| 15 | [德米特里厄斯（Demetrius）](#npc-event-demetrius) | 4/4/4/0/6 | 4/4/4/0/7 | 差异已审计 | [zh 54996](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%BE%B7%E7%B1%B3%E7%89%B9%E9%87%8C%E5%8E%84%E6%96%AF&oldid=54996) | [en 193879](https://stardewvalleywiki.com/mediawiki/index.php?title=Demetrius&oldid=193879) |
| 16 | [矮人（Dwarf）](#npc-event-dwarf) | 1/1/1/0/0 | 1/1/1/0/0 | 一致 | [zh 54688](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%9F%AE%E4%BA%BA&oldid=54688) | [en 191010](https://stardewvalleywiki.com/mediawiki/index.php?title=Dwarf&oldid=191010) |
| 17 | [艾芙琳（Evelyn）](#npc-event-evelyn) | 3/3/3/2/4 | 3/3/3/2/4 | 一致 | [zh 54548](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%89%BE%E8%8A%99%E7%90%B3&oldid=54548) | [en 191129](https://stardewvalleywiki.com/mediawiki/index.php?title=Evelyn&oldid=191129) |
| 18 | [乔治（George）](#npc-event-george) | 4/4/4/0/6 | 4/4/4/0/6 | 一致 | [zh 54046](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E4%B9%94%E6%B2%BB&oldid=54046) | [en 193909](https://stardewvalleywiki.com/mediawiki/index.php?title=George&oldid=193909) |
| 19 | [格斯（Gus）](#npc-event-gus) | 5/6/5/2/6 | 5/6/5/2/6 | 一致 | [zh 55267](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%A0%BC%E6%96%AF&oldid=55267) | [en 191548](https://stardewvalleywiki.com/mediawiki/index.php?title=Gus&oldid=191548) |
| 20 | [贾斯（Jas）](#npc-event-jas) | 1/1/1/0/0 | 1/1/1/0/0 | 一致 | [zh 55188](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%B4%BE%E6%96%AF&oldid=55188) | [en 193899](https://stardewvalleywiki.com/mediawiki/index.php?title=Jas&oldid=193899) |
| 21 | [乔迪（Jodi）](#npc-event-jodi) | 5/5/5/0/9 | 5/5/5/0/8 | 差异已审计 | [zh 55067](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E4%B9%94%E8%BF%AA&oldid=55067) | [en 191546](https://stardewvalleywiki.com/mediawiki/index.php?title=Jodi&oldid=191546) |
| 22 | [肯特（Kent）](#npc-event-kent) | 4/4/4/3/6 | 4/4/4/3/6 | 一致 | [zh 55035](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%82%AF%E7%89%B9&oldid=55035) | [en 193910](https://stardewvalleywiki.com/mediawiki/index.php?title=Kent&oldid=193910) |
| 23 | [科罗布斯（Krobus）](#npc-event-krobus) | 2/2/2/0/2 | 2/2/2/0/2 | 一致 | [zh 55028](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%A7%91%E7%BD%97%E5%B8%83%E6%96%AF&oldid=55028) | [en 192255](https://stardewvalleywiki.com/mediawiki/index.php?title=Krobus&oldid=192255) |
| 24 | [雷欧（Leo）](#npc-event-leo) | 6/6/6/10/4 | 6/6/6/10/4 | 一致 | [zh 55053](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E9%9B%B7%E6%AC%A7&oldid=55053) | [en 192150](https://stardewvalleywiki.com/mediawiki/index.php?title=Leo&oldid=192150) |
| 25 | [刘易斯（Lewis）](#npc-event-lewis) | 4/5/4/2/6 | 4/5/4/2/6 | 一致 | [zh 54974](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%88%98%E6%98%93%E6%96%AF&oldid=54974) | [en 191314](https://stardewvalleywiki.com/mediawiki/index.php?title=Lewis&oldid=191314) |
| 26 | [莱纳斯（Linus）](#npc-event-linus) | 6/6/6/2/6 | 6/6/6/2/6 | 一致 | [zh 55042](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E8%8E%B1%E7%BA%B3%E6%96%AF&oldid=55042) | [en 193911](https://stardewvalleywiki.com/mediawiki/index.php?title=Linus&oldid=193911) |
| 27 | [玛妮（Marnie）](#npc-event-marnie) | 5/6/5/2/6 | 5/6/5/2/6 | 一致 | [zh 55084](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%8E%9B%E5%A6%AE&oldid=55084) | [en 191544](https://stardewvalleywiki.com/mediawiki/index.php?title=Marnie&oldid=191544) |
| 28 | [潘姆（Pam）](#npc-event-pam) | 4/5/4/2/6 | 4/5/4/0/6 | 差异已审计 | [zh 55017](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%BD%98%E5%A7%86&oldid=55017) | [en 191550](https://stardewvalleywiki.com/mediawiki/index.php?title=Pam&oldid=191550) |
| 29 | [皮埃尔（Pierre）](#npc-event-pierre) | 3/3/3/2/4 | 3/4/3/2/4 | 差异已审计 | [zh 55086](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%9A%AE%E5%9F%83%E5%B0%94&oldid=55086) | [en 192883](https://stardewvalleywiki.com/mediawiki/index.php?title=Pierre&oldid=192883) |
| 30 | [罗宾（Robin）](#npc-event-robin) | 3/3/3/2/4 | 3/3/3/0/4 | 差异已审计 | [zh 55090](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E7%BD%97%E5%AE%BE&oldid=55090) | [en 191769](https://stardewvalleywiki.com/mediawiki/index.php?title=Robin&oldid=191769) |
| 31 | [桑迪（Sandy）](#npc-event-sandy) | 2/2/2/0/4 | 2/2/2/0/4 | 一致 | [zh 55081](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%A1%91%E8%BF%AA&oldid=55081) | [en 191345](https://stardewvalleywiki.com/mediawiki/index.php?title=Sandy&oldid=191345) |
| 32 | [文森特（Vincent）](#npc-event-vincent) | 1/1/1/0/0 | 1/1/1/0/0 | 一致 | [zh 55079](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%96%87%E6%A3%AE%E7%89%B9&oldid=55079) | [en 193876](https://stardewvalleywiki.com/mediawiki/index.php?title=Vincent&oldid=193876) |
| 33 | [威利（Willy）](#npc-event-willy) | 5/5/5/0/8 | 5/5/5/0/8 | 一致 | [zh 55075](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E5%A8%81%E5%88%A9&oldid=55075) | [en 192689](https://stardewvalleywiki.com/mediawiki/index.php?title=Willy&oldid=192689) |
| 34 | [法师（Wizard）](#npc-event-wizard) | 2/2/1/0/2 | 2/3/1/0/2 | 差异已审计 | [zh 55012](https://zh.stardewvalleywiki.com/mediawiki/index.php?title=%E6%B3%95%E5%B8%88&oldid=55012) | [en 193912](https://stardewvalleywiki.com/mediawiki/index.php?title=Wizard&oldid=193912) |

## 逐人爱心事件全集

<a id="npc-event-alex"></a>

### 01. 亚历克斯（Alex）

> 来源：中文 revision 55068；英文 revision 193663
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 8 个事件/后续条目、11 个事件外层条件或补充段落、8 张详情表、13 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 在一个晴朗的夏天，当亚历克斯 在海滩时 去那儿（每周特定的几天，8:50到24:00之间）。

**详情：**

你看到亚历克斯与他的格球。他向你打招呼并试图抛给你一个格球。你没有抓住它。他笑着说这是一个很好的尝试。他继续告诉你，他相信自己会成为星露谷的第一个职业球员。他问你的看法是什么。

- "我相信你！" （不影响 好感度 ） 亚历克斯感谢你的支持，并说他会记住它。
- "哇，你真够自大的。" （不影响 好感度 ） 亚历克斯说你有点嫉妒，并且离开。

##### 4心事件

**触发条件或事件外补充：**

- 09:00到16:00之间进入城镇。

**详情：**

亚历克斯在他家附近的狗屋旁边。他在和狗说话，从这里可以得知狗的名字叫 达斯迪 。他说自己和达斯迪很相似，只有达斯迪理解自己。你从沙龙后面出来，亚历克斯问你有没有听见他说话。

- "没错，我什么都听到了。" （不影响 好感度 ）
- "没有……怎么了？" （不影响 好感度 ）

不管选择哪个，他说他和祖父母一起住的原因是因为他的爸爸。他的父亲是一个酒鬼，经常痛骂亚历克斯。有一天，他的爸爸离开了，不久之后，他的母亲也病逝了。亚历克斯认为过去的就让它过去，自己不需要同情。 亚历克斯平复了情绪，让你看 达斯迪 非常想吃牛排的样子。

##### 5心事件

**触发条件或事件外补充：**

- 当亚历克斯在家时进入他的屋子。

**详情：**

你看到亚历克斯盯着他的书柜，他在感叹自己没有读过上面任何一本书。他告诉你他担心自己没有文化就过不上好日子，觉得自己很没用。

- "才不是。你明明是个天才！" （不影响 好感度 ）
- "我们都有自己的长处和短处。" （ 好感度 +50）
- "没用？对，总结得很精辟。" （ 好感度 -50）

他决定继续努力。并你和他共进晚餐，讨论哲学。

##### 6心事件

**触发条件或事件外补充：**

- 当亚历克斯在家时进入他的屋子。

**详情：**

亚历克斯觉得自己没法为一名职业格球选手。并且为自己粗鲁的态度的向你表示歉意，并且感激你没有生气，继续做他的朋友。你会给他一些鼓励（没有选项），亚历克斯将重新恢复活力再次开始力量训练。

##### 8心事件

**触发条件或事件外补充：**

- 在一个晴朗的夏天，当亚历克斯 在海滩时 去那儿（每周特定的几天，8:50到24:00之间）。
- 注意：与亚历克斯结婚后不能再正常触发此事件，因为婚后他不会再前往海滩。（但依然可以在他去 姜岛 度假村排队登船的时候触发。）

**详情：**

亚历克斯正坐在海滩上哭. 你靠近他并坐在了他的身边。他说今天是12年前他母亲死掉的日子。他感到遗憾的是小时候没有感谢母亲的照顾。他唯一留下的纪念品就是母亲的音乐盒。亚历克斯打开音乐盒，两人一起聆听着。伴随着音乐，你看到亚历克斯的母亲开心地怀抱着还是婴儿的亚历克斯。随着音乐的消失，他会问你在想什么。

- "活出精彩人生以报答你母亲养育之恩。" （不影响 好感度 ） 亚历克斯同意并说这就是为什么他如此努力成为一个专业的格球选手。
- "你不应该沉浸在过去不放手。" （不影响 好感度 ） 他会说"呀……今天是我妈的忌日！你就发发慈悲吧……"
- "要是你寂寞了，我永远会陪伴你。" （不影响 好感度 ） 亚历克斯感谢你并且害羞的说你是他在镇上最好的朋友。如果你是男性，他还会说 "你和别人不一样。你的心思更加细腻。我很高兴"
- "咬咬牙撑过去。人生不易，且行且珍惜。" （不影响 好感度 ） 他会说"这根本不会让我觉得好过，蠢货。"

在冷静下来之后, 他说你们两个该返回城镇了。在你离开之前, 他提心吊胆的请你不要告诉任何人他哭了。你笑了并在他仓促的追着你时走开。

##### 10心事件

**触发条件或事件外补充：**

- 亚历克斯会寄一封信要你在晚上时去酒吧和他见面。在收到信之后，在19:00到10点之间进入酒吧。

**详情：**

亚历克斯为了你们的晚餐约会预定了一个包间。格斯为你们两个拉小提琴，艾米丽会端上食物。

如果玩家是女性，亚历克斯承认你们两人第一次见面时他就被你吸引了，虽然他过去遇到这种情况时感情很快就会消失，但他对你的感情却不断的增长。如果玩家是男性，亚历克斯承认你们两人第一次见面时他就被你吸引了。虽然他一开始否认了这些感觉，但他现在遵从自己的内心。

- "我再赞同不过了。" （不影响 好感度 ） 亚历克斯很高兴你们终于能够承认彼此的感受。他开心地吃起牛排。 透过窗户看到 达斯迪 嗅到食物的味道留下口水。
- "抱歉……我对你没感觉。" （不影响 好感度 ） 亚历克斯觉得心碎，他因为让你感觉不舒服向你道歉。并说自己失去了胃口。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的男性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身男性村民的10心事件后仍然处于未婚状态，进入 星之果实酒吧 时将会触发过场剧情。
- 如果最后一个触发的事件是 亚历克斯 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身男性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有男生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内男生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和他们对话，他们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成男人间一场友好的台球比賽。

##### 14心事件

**触发条件或事件外补充：**

- 游戏第二年及之后，身上有 5,000 以上，那么在星期天以外的任何一天6:00到8:20间离开 农舍 时会触发。

**详情：**

亚历克斯会拦下你找你要 5,000 ，说是要进行秘密项目。一旦你接受，他会说秘密项目星期天就会准备好啦。

星期天进入城镇以触发事件的第二阶段。 第三阶段由进入 星之果实酒吧 触发。可以看到亚历克斯、肯特、谢恩和格斯正在里室看一场格球比赛，房间的一半已经装饰了格球纪念品，还有一台电视。玩家走进后，亚历克斯会告诉玩家，他长久以来没有意识到成为职业选手的梦想（虽然他保证现在的生活已经很开心了），这种方式会对意识到这个梦想起到一点小帮助。肯特补充道看比赛可以转移注意力，忘记生活忧愁，谢恩也同意。格斯告诉玩家看比赛对商业也有好处。玩家会说你们一伙现在有新传统了， 5,000 花得值。随后过场画面结束。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个事件/后续条目、9 个事件外层条件或补充段落、8 张详情表、13 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- On a sunny Summer day, visit the Beach when Alex is there.

**Details：**

You see Alex with his gridball. He greets you and tries to toss you the gridball. You fail to catch it. He laughs and says it was a nice try. He goes on to tell you he's sure that he's going to become the first professional gridball player from Stardew Valley. He asks you what you think his chances are.

- "I believe in you!" (No effect on friendship .) Alex thanks you for your support and says that he'll remember it.
- "Wow, you're really arrogant." (No effect on friendship .) Alex says you're just a little jealous and leaves.

##### Four Hearts

**触发条件或事件外补充：**

- Enter town between 9am and 4pm.

**Details：**

Alex is next to the dog pen near his home. He's talking to the dog, whose name is revealed as Dusty . He comments that both he and the dog have been through a lot and that he feels misunderstood. You come out from behind the Saloon , and Alex asks if you heard any of that.

- "Yes, I heard everything." (No effect on friendship .)
- "Not really... why?" (No effect on friendship .)

Either way, he says the reason that he lives with his grandparents is because of his dad. His dad was an alcoholic and would verbally abuse Alex, calling him "worthless". One day, his dad left, and shortly after that, his mother got sick and passed away. Alex goes on to say that he shouldn't dwell on it and doesn't need sympathy. Trying to lighten the mood, Alex offers you the opportunity to see what Dusty will do for a barbecued steak.

##### Five Hearts

**触发条件或事件外补充：**

- Enter Alex's house when he's there.

**Details：**

You approach him while he stares at his bookcase and laments the fact that he hasn't read a single book in it. He tells you that he's worried he won't get anywhere in life without being knowledgeable and that he feels worthless.

- "That's crazy. You're a genius!" (No effect on friendship .)
- "We all have our strengths and weaknesses." (+50 friendship .)
- "Worthless? Yeah, that about sums it up." (-50 friendship .)

He decides that if he works hard, he can accomplish anything. He suggests that you and he can have dinner and discuss philosophy.

##### Six Hearts

**触发条件或事件外补充：**

- Enter Alex's house when he's there.

**Details：**

Alex expresses doubt about being able to go pro as a gridball player. He apologizes to you for acting rude and arrogant and appreciates how you stuck with him despite all that. You provide some encouragement (no choices necessary), and Alex will return to his strength workout with renewed vigor.

##### Eight Hearts

**触发条件或事件外补充：**

- On a sunny day, visit the Beach when Alex is there. He is only scheduled to go to the beach in Summer , but may pass by on the way to the Ginger Island resort in any season after it is completed.

**Details：**

Alex is sitting on the beach crying. You approach him and sit down next to him. He says today is the day that his mother died 12 years ago. He regrets not being able to thank her for taking care of him when he was a kid. The only keepsake he has left is his mother's music box. Alex opens it and plays it for the both of you. As the music plays, you see a vision of Alex's mother happily cradling baby Alex in her arms. As the music fades, he asks what you're thinking.

- "Honor your mother's memory by always doing your best." (No effect on friendship .) Alex agrees and says that's why he's working so hard to be a professional gridball player.
- "You shouldn't dwell in the past." (No effect on friendship .)
- "I'll always be here for you if you get lonely." (No effect on friendship .) Alex thanks you and bashfully says you're his best friend in the whole town. If male, he says "You... you're different than other guys. More sensitive. I'm glad."
- "Get over it. Life is hard for everyone." (No effect on friendship .)

After calming down, he says the two of you should head back to town. Before you leave, he nervously asks you not to tell anybody that he was crying. You laugh and walk off while he hurriedly chases after you.

##### Ten Hearts

**触发条件或事件外补充：**

- Alex will send you a letter to meet him at the Saloon after dark. After receiving the letter, enter the Saloon between 7pm and 10pm.

**Details：**

Alex reserves a private room for your dinner date. Gus plays the violin for you two, and Emily will bring in your food.

If the player is female, Alex confesses that he has had a crush on you since the two of you first met, and although his crushes in the past faded away quickly, his feelings for you kept growing. If the player is male, Alex confesses that he has been drawn to you since the two of you first met; although he denied these feelings at first, he's now decided to follow his heart.

- "I feel the same way." (No effect on friendship .) Alex is elated that the both of you were finally able to admit your feelings to each other. He happily digs into his steak. Dusty suddenly bursts through the window, salivating at the smell of food. Alex laughs.
- "I'm sorry... I don't feel that way about you." (No effect on friendship .) Alex is crushed and apologizes for making you uncomfortable. He loses his appetite.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelors, raised friendship with each bachelor to 10 hearts, and seen each bachelor's 10-heart event, then entering The Stardrop Saloon will trigger a cutscene. If Alex is the final bachelor you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a friendly game of pool.

If the player does not have a Rabbit's Foot in inventory, all bachelors will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelors will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelors will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Exit the Farmhouse in year 2+ between 6am and 8:20am on any day other than Sunday. You must have data-sort-value="5000"> 5,000g available.

**Details：**

Alex will stop you and ask for data-sort-value="5000"> 5,000g for a 'secret project'. If you accept, he will remark that it will be ready to be seen on Sunday.

Part 2 can be triggered by entering the Saloon the following Sunday. Alex, Kent , Shane , George , and Gus can be seen watching a gridball game in the backroom, half of which has been decorated with gridball memorabilia and a TV. The other half still has barrels, and storage. The player walks in, and Alex tells the player that although his dream of going pro may not have been realised (though he assures the farmer that he's happy with his life now), this is a small way of realising it. Kent adds that it takes his mind off things, and Shane agrees. Gus tells the player that watching the game is good for business, too. The cutscene ends with the player saying that the guys have a new tradition now and that the data-sort-value="5000"> 5,000g was well spent.

<a id="npc-event-elliott"></a>

### 02. 艾利欧特（Elliott）

> 来源：中文 revision 55231；英文 revision 192964
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、18 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 当艾利欧特在小屋的时候去拜访他。

**详情：**

艾利欧特会向玩家打招呼，并告诉玩家，他来到鹈鹕镇是为了成为一名作家，但在他的家乡没有人相信他能做到。他问你喜欢什么样的小说：

- "悬念" （ 好感度 +30）
- "浪漫" （ 好感度 +30）
- "科幻" （ 好感度 +30）

他说他会记住你的选择，然后请你帮他看看他的玫瑰有没有枯萎。

##### 4心事件

**触发条件或事件外补充：**

- 在15:00至22:00之间进入 星之果实酒吧 ，需要 格斯 在场。

**详情：**

格斯说他马上就来给玩家点单。然后艾利欧特走进酒吧，说在这儿找到你真是太巧了。他说他刚写了八个小时的书，想来这里休息一下。他会为自己点一份麦芽酒，再给你也点一杯。如果你的角色是男性，他会为你也点一份麦芽酒。如果你的角色是女性，他会为你点一杯葡萄酒。

你提议在喝酒前先举杯庆祝一下。你可以从四种不同的祝酒词中选择：

- "鹈鹕镇" （ 好感度 +25） "啊，为社区营造一个和谐的未来…多好的主意啊。这里是鹈鹕镇！"
- "我们的友谊！" （ 好感度 +50） "真是个好主意！为了我们！"
- "我们的健康！" （ 好感度 -10） "好吧。。行吧。"
- "你的命运！" （ 好感度 -50） "哦，别提了！"

你们都喝了酒，然后他开始在他的位置上跳舞。当过场动画结束时，你在 星之果实酒吧 外面，带有喝醉酒的眼花效果。

注意：在此事件中饮用的饮料可使玩家最多恢复50 能量 和22 生命值 ，并使玩家获得 " 眩晕 " 的减益效果。

##### 6心事件

**触发条件或事件外补充：**

- 当艾利欧特在他小屋的时候拜访。

**详情：**

艾利欧特在弹钢琴。在他结束后，你可以说：

- "真的很棒。" （不影响 好感度 ）
- "你弹了多久？" （不影响 好感度 ）

艾利欧特谈到完成他的小说有多么困难，并说 "有时候我真想抛弃一切，像你一样当个农夫。"。 玩家可以用以下方式回应：

- "当农夫也一样艰难。" （不影响 好感度 ）

艾利欧特为自己的感觉迟钝道歉，并澄清说他真正想要的是体验 "真实的生活"。

- "过来农场生活吧，我需要帮忙" （不影响 好感度 ）

艾利欧特很惊讶，但拒绝了这个提议，说他需要完成他的小说。

##### 8心事件

**触发条件或事件外补充：**

- 当收到艾利欧特的一封信后，在13:00到7点之间拜访 博物馆 。（不需要在同一天。）

**详情：**

艾利欧特寄给你一封信，邀请你下午去图书馆参加他写完的小说朗读会。

当你进入博物馆的时候，你发现很多村民聚在一起听艾利欧特第一本书的朗读会。艾利欧特表示很开心你能来听。他从他的小说里选读。根据你在与他的第一次爱心事件中的选择，你将听到这些故事中的一个：

- 神秘小说《蓝塔》。"这是一部设置在超现实的、反乌托邦的未来的神秘小说。第一章。从阴影中走出来一个人，散发着神秘的全知全能的光芒。‘晚上好，卢先生，’他说，他的嘴角在颤抖。卢先生似乎很惊讶，‘你怎么会知道我的名字？’" (淡出.) "卢检查了杰努的口袋，然后站起来，走进卧室。他很快找到了他要找的那把小金钥匙，并把它塞进了他的大衣口袋。"
- 浪漫小说《山茶车站》。"这是一部浪漫小说，讲述了一位火车女乘务员爱上了一位旅行建筑师...... 第一章。‘先生，您的票？’收票员戈兹曼向这位年轻的通勤者伸出一只戴着手套的手。‘啊，是的。我就放在这里，’他回答说，把手伸进他的外套口袋。他发现车票不见了，他感到有些羞愧。" (淡出.) "...‘克拉拉，有件事我必须告诉你，’他在她转身离开时突然说。克拉拉慢慢地转过身来，看到霍拉西奥眼中的绝望神情。这时，戈兹曼冲进包厢，满脸通红。"
- 科幻小说《雅佐星球的兴衰》。"这是一部科幻史诗，横跨数千年的异国行星系统。第一章。当气闸在他身后折断时，尤特金指挥官走过金色拱门。今天是他来到亚索星球的第一天，所有14名联盟代表都被召集到大尖塔......" (淡出.) "...当第七个月亮降到地平线下时，亚索星球将开始其邪恶的转变......这是指挥官尤特金完全没有准备的事件。"

如果没有观看过 2 心事件，则默认为科幻小说。

艾利欧特向每个到场的人致谢，然后走向你并问你怎么样。他说他很高兴你能喜欢，因为他的这本小说是按照你喜欢的题材创作，专门献给你的。

##### 10心事件

**触发条件或事件外补充：**

- 在不是雨天的早晨7点至13:00间去海滩。你将收到一封信，但是这不是触发事件必需的。

**详情：**

艾利欧特写了一封信给你，说他有一个想法。你在码头跟他碰面。艾利欧特修好了码头上的小船，他问你是否愿意跟他一起参加小船的首航。

- 如果你接受了，艾利欧特就会谈论他的小说，以及没有你他就无法完成小说。然后他不知所措地解释他对你的感觉。突然，他吻了你!你开始颤抖。 我很幸福 （ 好感度 +50）

  - 你们都回到了岸上，艾利欧特说，这个山谷看起来终于像个家了。 你让我感到非常不舒服。停止吧。 （ 好感度 -50）
  - 艾利欧特向你道歉，场景结束。

- 如果你拒绝，艾利欧特说："我明白了"，事件就结束了。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的男性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身男性村民的10心事件后仍然处于未婚状态，进入 星之果实酒吧 时将会触发过场剧情。
- 如果最后一个触发的事件是 亚历克斯 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身男性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有男生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内男生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和他们对话，他们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成男人间一场友好的台球比賽。

##### 14心事件

**触发条件或事件外补充：**

- 在未来8天没有 节日 的早晨6点到15:00间离开农舍。（若达成 14 心时未来 8 天内有节日，14 心事件将顺延至节日后触发）

**详情：**

当玩家离开农舍时，艾利欧特会在前廊。

在他巡回签售时，他将每天给玩家寄信，持续整整一周。

在第8天，事件的最后部分将在玩家醒来时触发。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个事件/后续条目、8 个事件外层条件或补充段落、7 张详情表、18 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Elliott's cabin when he's there.

**Details：**

Elliott will greet you, and explain that he came to Pelican Town to become a writer but no one from his hometown believed he could make it. He asks what kind of novels you like:

- "Mystery" (+30 friendship .)
- "Romance" (+30 friendship .)
- "Sci-Fi" (+30 friendship .)

He says he'll remember your choice, then asks you to look at his rose because he thinks it may be wilting.

##### Four Hearts

**触发条件或事件外补充：**

- Enter the Stardrop Saloon between 3pm and 10pm when Gus is there.

**Details：**

Gus says he'll take your order in a moment. Before he gets to you, Elliott walks into the building and says it's a pleasant surprise to find you here. He says that he's stopping in to relax after eight hours of writing. If your character is male, Elliott orders two ales, one for you and one for him. He instead orders wine for you if your character is female.

You stop him before he can drink and propose a toast. You can choose from four different toasts:

- "To Pelican Town!" (+25 friendship .) "Ah, to a harmonious future for the community... what a virtuous idea. Here's to Pelican Town!"
- "To our friendship!" (+50 friendship .) "That's a great idea! Here's to us!"
- "To my good health!" (-10 friendship .) "Well... okay."
- "To your doom!" (-50 friendship .) "Hmph. Forget it."

You both drink and he starts dancing where he is. Then the cutscene ends, and you are transported outside the door of the Stardrop Saloon .

Note: The beverage consumed during the heart event will heal up to 50 Energy and 22 Health , and leave the player with the " Tipsy " buff.

##### Six Hearts

**触发条件或事件外补充：**

- Enter Elliott's home when he's there.

**Details：**

Elliott is playing the piano. After he finishes, the player has a dialogue option:

- "That was wonderful" (No effect on friendship .)
- "How long have you been playing?" (No effect on friendship .)

Elliott talks about how difficult it's been to finish his novel and says "Sometimes I wish I could just throw it all away and become a farmer like you." The player can respond with:

- "It's just as hard to be a farmer, you know" (No effect on friendship .)

Elliott apologizes for being insensitive and clarifies that what he really wants is to experience "real life".

- "Come live on the farm, I could use the extra help" (No effect on friendship .)

Elliott is surprised but declines the offer, saying he needs to finish his novel.

##### Eight Hearts

**触发条件或事件外补充：**

- After receiving a letter from Elliott, visit the museum between 1pm and 7pm. (It doesn't need to be the same day.)

**Details：**

Elliott sends you a letter inviting you to a reading of his finished novel at the library that afternoon.

When you enter the museum, you find many villagers have gathered to listen to Elliott's first book reading. Elliott expresses his delight at your coming to listen. He reads from his novel. Depending on your choice in his Two-heart event, you'll get one of these stories:

- The mystery novel Blue Tower . "It's a mystery novel set in a surreal, dystopian future. Chapter One. From the shadows emerged a man, radiating with enigmatic omniscience. 'Good Evening, Mr. Lu,' he said, the corners of his mouth quivering. Lu seemed astonished. 'How did you know my name?'" (Fade.) "Lu checked Jenu's pockets, then stood up and walked into the bedroom. He quickly found the small golden key that he was looking for and slipped it into his coat pocket."
- The romance novel Camellia Station . "It's a romance novel about a train stewardess who falls in love with a traveling architect... Chapter One. 'Your ticket, sir?' Ticket collector Gozman extended a gloved hand towards the young commuter. 'Ah, yes. I have it right here,' he replied, reaching into his coat pocket. Mortified, he discovered that the ticket was missing." (Fade.) "...'Clara, there's something I must tell you,' he blurted as she turned to leave. Clara turned, slowly, and saw the look of desperation in Horatio's eye. At that moment Gozman burst into the compartment, red-faced."
- The sci-fi novel The Rise And Fall Of Planet Yazzo . "It's a sci-fi epic spanning thousands of years in an exotic planetary system. Chapter One. Commander Yutkin stepped through the golden archway as the airlock snapped shut behind him. Today was his first day on Planet Yazzo, and all 14 of the alliance delegates had been summoned to the Grand Spire..." (Fade.) "...And as the 7th moon descended beneath the horizon, the planet of Yazzo would begin its sinister transformation... an event for which Commander Yutkin was completely unprepared."

If the Two-heart event hasn't been viewed, the default genre is Sci-Fi.

Elliott thanks everyone for coming, then walks up to you and asks how you think it went. He says he's glad that you liked it, because he dedicated it to you and he based it on your favorite genre.

##### Ten Hearts

**触发条件或事件外补充：**

- Go to the beach on a day when it is not raining between 7am and 1pm. A letter will be sent to you but it is not needed to trigger the event.

**Details：**

Elliott writes you a letter saying he has an idea. You join him on the docks. Elliott had fixed the row boat that's been on the docks, and he wonders if you want to go with him on a "maiden voyage."

- If you accept, Elliott talks about his novel and how he couldn't have done it without you. Then he's at a loss for words to explain how he feels about you. Suddenly, he kisses you! You begin trembling. I'm happy (+50 friendship .)

  - If your character is a man, he will comment on how he didn't know if you would have feelings for another man. You both head back to shore, and Elliott comments on how the valley finally looks like home. You're making me very uncomfortable. Stop. (-50 friendship .)
  - Elliott apologizes and the scene ends.

- If you refuse, Elliott says "I see" and the event ends.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelors, raised friendship with each bachelor to 10 hearts, and seen each bachelor's 10-heart event, then entering The Stardrop Saloon will trigger a cutscene. If Alex is the final bachelor you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a friendly game of pool.

If the player does not have a Rabbit's Foot in inventory, all bachelors will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelors will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelors will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Exit the farmhouse or enter the farm while Elliott is in it (not in the farmhouse) between 6am and 3pm on a day when there are no Festivals occurring for the next 8 days.

**Details：**

Elliott will be on the front porch when the player leaves the farmhouse.

Elliott will send the player letters in the mail daily for a full week while he is touring for his book signing.

On the second day of the week of his absence, one Crab Cakes will appear in the player's fridge or Mini-Fridge if there is available space.

On the 8th day, he will arrive back at the farmhouse, and the last part of the event will trigger as soon as the player wakes up.

<a id="npc-event-harvey"></a>

### 03. 哈维（Harvey）

> 来源：中文 revision 54980；英文 revision 193951
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、9 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 在 乔治 在家的时候进入他家。

**详情：**

哈维正给乔治家给他体检。他对乔治说，如果想要健康长寿，就得改变一下生活方式。但乔治看上去对他的建议非常生气，并说自己知道怎样做最好。哈维解释说他在学校学了8年医，就是为了帮助人们保持健康。接着哈维和乔治注意到你进入了屋内，哈维说体检时你不能待在那儿，不过乔治却主动向玩家询问对这件事的意见。接着你可以做出以下选择：

- “乔治应该听从哈维医生的建议。” （哈维 好感度 +40） 哈维会说他只是想帮助乔治，乔治最后同意了，选择遵从医嘱。之后哈维会为你的帮助道谢，并且很感激你。
- “乔治知道怎么做对他的身体最好。” （哈维 好感度 -40） 哈维会叹气并告诉乔治，如果他继续像这个样子，将不得不告诉他的妻子 艾芙琳 ，而她会不高兴。乔治勉强让步，同意遵从医嘱。随后哈维会告诉你最好不要误导他的病人。

##### 4心事件

**触发条件或事件外补充：**

- 当哈维在的时候进入 诊所 。

**详情：**

哈维说他正要给你写封信，问问你打算什么时候来做你早该完成的一年一度体检。当他给你体检的时候，他会说你的心跳有点儿快。接着你可以做出以下选择：

- "我有点紧张。" （ 好感度 +20） 哈维觉得那是由于在医院里的缘故，让你放松，他是为了帮你检查。
- "我刚才在农场里干活，现在还没喘过来气。" （ 好感度 +20）
- "你真的是医生吗？我的心跳很正常！" （ 好感度 -50）

在最后，哈维会说你身体很好，让你干活时别太累着。

##### 6心事件

**触发条件或事件外补充：**

- 在11:00至15:00之间，进入 皮埃尔的杂货店 。

**详情：**

你碰巧撞见氧健身俱乐部的成员正在 卡洛琳 家一起健身，除了几位女性 居民 外，你发现哈维也在当中。健身结束后，哈维累得直喘气。他准备出门时正好遇见了你，发觉你知道了他参加健身班的事情。哈维解释说自己年纪大了，想要保持健康的体魄。他很尴尬，想要让你帮忙保守这个秘密。接着你可以做出以下选择：

- “我不会说的。” （ 好感度 +20）
- “这我可说不好。” （ 好感度 -50）

如果你选择不告诉其他人，哈维会非常感谢你。

##### 8心事件

**触发条件或事件外补充：**

- 进入 哈维的诊所 即可。

**详情：**

你走进了哈维的房间，看到他正在用试着用无线电联系飞行员。他突然收到了一位飞行员的回应，并成功告知了飞行员地面的温度和风力情况等信息，非常激动。此时，玩家可以做出以下选择：

- 询问哈维他为何那么紧张。 （不影响 好感度 ）
- 假装一切正常。 （不影响 好感度 ）

无论选择哪个选项都会发生相同的剧情。哈维会注意到玩家，并解释说他正在进行无线电通讯，而且居然遇到了真正的飞行员。然后他会激动地让你去窗边看着飞机从头顶飞过。飞机经过后，他会对你说，自己小时候的梦想就是当飞行员，但是因为视力不好和恐高，没有机会实现这个梦想。但他已经觉得自己长大了并找到了自己的人生定位，认清了不是所有人都能实现梦想的现实。最后，他会让你看看自己刚完成的TR-星鸟豪华版飞机模型，借此缓和一下气氛。

##### 10心事件

**触发条件或事件外补充：**

- 哈维给你寄了封信，邀请你在09:00至17:00之间前往火车站碰面。

**详情：**

当你在那里和他见面时，他会说他很高兴你能来。接着一名叫马尔赛罗的男人会乘着热气球缓缓降落，并告知你们接下来的两小时内可以任意使用热气球，而他会前往 星之果实酒吧 。哈维告诉你他是在报纸上看见乘坐热气球的广告，并且觉得被邀请乘坐热气球而言对你是个惊喜。在跳进热气球前，你可以选择马上进去，或者问他为什么要做这个，因为你知道他非常恐高。如果你选择问他，他会含羞地解释说，恐高对他仍然是个问题，但他钦慕你和你的勇气，而这两样就已经足够让他克服他的恐惧了。

登上了热气球，哈维点燃了下方的炉子，让气球升高。但当他意识到上升的速度有多快时，他吓坏了。在高空中，他的情绪自恐惧与兴奋中来回摇摆不定，最后他醒悟过来，意识到你正和他一起。他对他现在能看到的景色感到惊奇，也很高兴他和你一起。在两个小时快结束时，你靠近亲吻了他。你把热气球还给了那个男人，至少迟了半个小时。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的男性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身男性村民的10心事件后仍然处于未婚状态，进入 星之果实酒吧 时将会触发过场剧情。
- 如果最后一个触发的事件是 亚历克斯 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身男性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有男生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内男生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和他们对话，他们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成男人间一场友好的台球比賽。

##### 14心事件

**触发条件或事件外补充：**

- 在20:00到12:00之间进入至少升级过两次的 农舍 。

**详情：**

在这段过场动画中，哈维一开始正在做饭，做好后他开始摆放碗筷。此时，你正好进屋。他会说你回来的正是时候，他自制了一份内含蛤贝的“天使之发·春之意面”，用来犒劳在农场辛苦工作的你。品尝后，你需要评价这道菜的味道，哈维会对你的评价做出不同的回应。然后哈维会询问你当天做了什么，哈维同样会根据你的选择进行回应。但不论如何选择，都不会影响你与哈维之间的好感度。

最后，哈维会主动提出洗碗并表达对你的爱意。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个事件/后续条目、8 个事件外层条件或补充段落、7 张详情表、9 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter George's house while George is there.

**Details：**

Harvey is performing a private check-up on George. He tries to explain that George needs to make some lifestyle changes if he wants to keep healthy, but George seems irritated with his advice and states that he knows what's best for his own body. Harvey explains that he went to school for eight years so that he could help people in an attempt to get George to cooperate, but then his attention is drawn away as he notices your arrival. Harvey says you shouldn't be there because it is a private session, but George stops you from leaving by asking for a second opinion on the matter.

- "George should follow Dr. Harvey's advice." (+40 friendship .) He again says that he's only trying to help and George finally gives in and agrees to follow doctor's orders. After that Harvey thanks you for the help and say that he appreciates you.
- "George knows what's best for his own body." (-40 friendship .) He sighs and tells George that if he's going to behave like this, Harvey will have to tell George's wife and she won't be happy. George begrudgingly concedes to the doctor's orders. Harvey tells you that it's better not to give patients mixed messages.

##### Four Hearts

**触发条件或事件外补充：**

- Enter the clinic when Harvey is there.

**Details：**

Harvey says he was just about to write you a letter about how you're due for your annual check-up. As he's looking you over, he notices your pulse seems high.

- "I'm a little nervous..." (+20 friendship .) Harvey assumes that it's because of the Hospital and tells you to relax because he's here to help.
- "I'm out of breath from working on the farm." (+20 friendship .)
- "Are you really a doctor? My pulse is fine!" (-50 friendship .)

At the end of it, Harvey declares you healthy and says you should take care not to overwork yourself on the farm.

##### Six Hearts

**触发条件或事件外补充：**

- Enter the general store between 11am and 3pm.

**Details：**

You witness a dance aerobics session with some of the ladies and, unexpectedly, Harvey. Harvey seems out of breath as the session comes to an end, heading towards the door to leave but running into you on the way. Harvey seems incredibly embarrassed when he finds out you were watching, wanting to keep it a secret. He explains that he's doing it to stay healthy, which becomes more difficult with age and the stress of running the clinic essentially alone. Harvey seems discouraged because of how difficult it is for him to keep up with the rest of the group, figuring he must not be in good shape. He asks you not to tell the rest of the town that he's doing dance aerobics.

- "I won't tell" (+20 friendship .) Harvey thanks you and says that he appreciates you.
- "I can't promise that." (-50 friendship .) Harvey sighs and says "rude".

##### Eight Hearts

**触发条件或事件外补充：**

- Enter the clinic .

**Details：**

You head into Harvey's room to find him using his equipment in an attempt to contact a pilot. He suddenly gets a response, surprising him and making his pulse race, but he manages to respond with his coordinates before quickly signing off. As you enter the room, you are presented with two choices:

- "Ask Harvey why he's all flustered." (No effect on friendship .)
- "Pretend like everything's normal." (No effect on friendship .)

Either way, Harvey's response is the same. He notices you and tells you he made contact with a real pilot. He excitedly tells you to come over to the window to watch the pilot fly overhead with him. After the plane passes Harvey opens up about how he always wanted to be a pilot when he was younger, but couldn't because of his bad eyesight and crippling fear of heights. He tells you not to be sad about it, that he's accepted not everyone can achieve their dreams and that is just the way the world is. Harvey tries to lighten the mood by asking you to look at his model planes, having just finished the TR-Starbird deluxe set.

##### Ten Hearts

**触发条件或事件外补充：**

- Harvey sends you a letter asking to meet at the railroad tracks . Go there between 9am and 5pm.

**Details：**

When you meet him there, he says he's glad you came and that something should be happening very soon. A man in a hot air balloon, Marcello, lands nearby, says the balloon is yours for the next two hours, and heads into town for the Stardrop Saloon . Harvey tells you that he saw the hot air balloon rental advertised in the newspaper and thought it was a perfect thing to do together. Before hopping in, you can either immediately get to it or ask him why he did this since you know about his incredible fear of heights. If you opt to ask him, he bashfully explains that while his fear is still a major factor, he admires you and your courage and says that it should be more than enough for the both of you.

Boarding the hot air balloon, Harvey switches on the burner below to make it ascend but freaks out once he realizes how fast it's rising. High in the sky, his mood oscillates between fear and elation, eventually coming to his senses and remembering that you're there with him. He marvels at how much he can see below and is glad that he's doing this with you. Soon before the two-hour rental is up, you draw close into a kiss. You return the balloon to the rental man at least a half hour late.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelors, raised friendship with each bachelor to 10 hearts, and seen each bachelor's 10-heart event, then entering The Stardrop Saloon will trigger a cutscene. If Alex is the final bachelor you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a friendly game of pool.

If the player does not have a Rabbit's Foot in inventory, all bachelors will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelors will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelors will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Enter an upgraded farm house (needs to be upgraded at least twice) between 8pm and midnight.

**Details：**

In the cutscene, Harvey is seen cooking and then setting the table for dinner. As you enter, Harvey says you're just in time and tells you he's cooked angel hair pasta with clams. He asks you how the dish tastes and he asks what you did that day.

At the end, Harvey offers to wash the dishes and says he is happy to do so.

<a id="npc-event-sam"></a>

### 04. 山姆（Sam）

> 来源：中文 revision 55076；英文 revision 193676
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 8 个事件/后续条目、10 个事件外层条件或补充段落、8 张详情表、21 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 当山姆在家的时候进入他的房子

**详情：**

山姆和塞巴斯蒂安正在玩音乐。山姆会跟你讲他想要组建一个乐队，但是不确定要选择什么音乐类型。他问道你喜欢什么样的音乐。

- "令人愉悦的流行乐。" （不影响 好感度 ）
- "实验性质的硬摇滚。" （不影响 好感度 ）
- "极富能量的舞曲。" （不影响 好感度 ）
- "气氛活跃的乡村音乐。" （不影响 好感度 ）

无论你选择什么样的音乐形式，山姆都会说你跟他不谋而合。接着他会问塞巴斯蒂安是不是也同意。塞巴斯蒂安表示了赞同，随后山姆也对你表示感谢。

##### 3心事件

**触发条件或事件外补充：**

- 除冬季以外的任意季节，赶在晴天来到海滩（07:00到15:00之间）。这个事件仅在第一年发生

**详情：**

山姆看着弟弟 文森特 玩沙子，他说父亲过去常常在晴天带他们来到海边。山姆说：“那当然。” 文森特提到自己不小心听见人们讨论战争会造成大批伤亡，山姆说不要相信他们的话，之后文森特继续去玩沙子了。山姆的一席话让弟弟的期望提高，对此他感到十分内疚，并询问玩家的看法。

- "对小孩子坦白很重要。" （不影响 好感度 ） 山姆对此不是很认同，不过之后表示小孩子迟早都是会知道世界的残酷。
- "你做得很对。不能让小孩子失去希望。" （不影响 好感度 ） 山姆表示赞同，并说小孩子应该尽可能得保持他们的天真无邪。

之后山姆说乐队已经组建得差不多了，塞巴斯蒂安“因为一些原因”想让阿比盖尔担任鼓手。

##### 4心事件

**触发条件或事件外补充：**

- 当山姆在家时进入他的房间

**详情：**

山姆在厨房，看你进来后准备给你做点吃的，但不小心将蛋掉在了地板上。他妈妈听见声音赶来，看见此景十分生气。山姆让你告诉妈妈究竟发生了什么。

- "山姆把零食递给我的时候掉到了地上。" （ 好感度 -10）
- "山姆把零食递给我的时候被我弄掉了。" （ 好感度 +50） 山姆表示同意
- "山姆故意弄掉的。他觉得这样很好玩。" （ 好感度 -50）

乔迪感谢你还原了真相。山姆表示自己会把一切收拾干净。

##### 6心事件

**触发条件或事件外补充：**

- 在一个晴天，来到小镇（中午至4pm之间）

**详情：**

山姆玩滑板时在艾米丽和海莉门前的花箱上练习特技，被刘易斯逮个正着。准备责骂山姆时，他们询问玩家的意见。

- "先生，你是对的。山姆不应该私闯私人领域的。" （不影响 好感度 ） 山姆不太高兴，但接受了，并说自己不会再玩滑板。
- "别怪山姆，他也是实在没地方可以滑了才这样的。" （不影响 好感度 ） 山姆看上去很高兴。镇长感觉沮丧，他表示玩家应该更加成熟才对，但之后向山姆道歉，希望他之后更加小心。
- "这事我不管。" （不影响 好感度 ） 镇长刘易斯说他不想再看到山姆这样做了，山姆表示同意，之后镇长离开。之后山姆转向你，问你有没有看到他刚才的特技。

##### 8心事件

**触发条件或事件外补充：**

- 山姆出现在你家门口（06:00至20:00间）。玩家只有之前触发了2心事件才会触发这个8心事件。

**详情：**

山姆邀请你参观乐队在镇上的表演，邀请你16:00在车站碰面。抵达那里会发现大家都在。山姆感谢了玩家对于乐队选择音乐上的建议。

##### 10心事件

**触发条件或事件外补充：**

- 收到山姆的信后，在一个晴天来到小镇上（20:00至午夜间）

**详情：**

玩家在山姆家门口与他见面。山姆说外面太冷，于是带你回到了他的卧室。在山姆表白时他妈妈突然敲门，于是他将你藏在了床上。他妈妈进屋问到为什么山姆会满脸通红，山姆解释说自己在做俯卧撑。妈妈向他说晚安后离去。

玩家要做出以下选择：

- 快出来。 （不影响 好感度 ） (若选这项，之后会有下面2个选择) 靠近他。 （不影响 好感度 ） 看向窗外。 （不影响 好感度 ） 代表玩家拒绝了山姆。
- 待在原地。 （不影响 好感度 ） 山姆爬到床上并吻了你，他说“我一直感觉我们之间的关系非同寻常”

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的男性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身男性村民的10心事件后仍然处于未婚状态，进入 星之果实酒吧 时将会触发过场剧情。
- 如果最后一个触发的事件是 亚历克斯 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身男性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有男生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内男生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和他们对话，他们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成男人间一场友好的台球比賽。

##### 14心事件

**触发条件或事件外补充：**

- 第一部分： 在6:10到17:00之间进入升级后的农舍(需要至少升级两次)，此时山姆在里面。 第二部分： 三天后，在06:10分到17:00之间进入农舍，此时山姆正在里面。 第三部分： 三天后，在06:10分到17:00之间进入农舍，此时山姆正在里面。 第四部分： 四天后，在06:10分到17:00之间进入农舍，此时山姆正在里面。

**详情：**

第一部分：

  - 山姆说，自从搬进农庄后，他觉得自己变得懒惰了，他想找点工作--和音乐有关的工作。

第二部分：

  - 山姆收到了一封邮件中的工作邀请，为一个名为“欢乐祝尼魔表演”的儿童电视节目制作音乐。 他说，这并不是他心中所想的。 就把这当成你事业的垫脚石吧... ... （不影响 好感度 ）
  - 山姆回应道："嗯... 是啊，我想这是看待它的一种方式。" 想想看，你会让孩子们多开心啊! （不影响 好感度 ）
  - 山姆回应道："我是说......你是对的，总得有人做儿童音乐。但这不完全是一个'梦想的工作'..." 我很抱歉... （不影响 好感度 ）
  - 山姆回应道："啊，好吧......没关系。我会像往常一样，尽力而为。"

  - 山姆继续说："我想我最好开始'像孩子一样思考'......" 这对你来说应该很容易... （不影响 好感度 ）
  - 山姆大叫 "嘿！"而玩家则傻笑。 你可以找你的弟弟帮忙! （不影响 好感度 ）
  - 山姆说这是个不错的主意，并感谢玩家的建议。

第三部分：

  - 山姆在这首歌上取得了进展，他用一把木吉他弹奏着他目前所写的东西。 他对这份工作感觉很积极，希望歌曲完成后工作室对他的歌曲很满意。

第四部分：

  - 玩家， 文森特 ，和 贾斯 围着山姆的房间里的电视机在农舍。 萨姆播放了一段他的歌曲视频。 之后，他表示惊讶于文森特和贾斯的喜爱程度。 他感谢玩家的支持，并赠送了一个 山姆的音响 ，让玩家可以随时听歌。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个事件/后续条目、9 个事件外层条件或补充段落、8 张详情表、21 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Sam's house when he's there.

**Details：**

Sam and Sebastian are jamming out in Sam's room. Sam tells you he's trying to get a band together, but he's unsure what style of music to play. He asks what music you like.

- "Cheerful pop music." (No effect on friendship .)
- "Experimental noise rock." (No effect on friendship .)
- "Hi-Energy dance music." (No effect on friendship .)
- "Honky-tonky country music." (No effect on friendship .)

No matter which style you pick, Sam says that's the style he's been thinking about for the band. He asks Sebastian if he's on board too. Sebastian agrees and Sam thanks you.

Note that if you skip this cutscene, Sam's 8-heart cutscene will play cheerful pop music.

##### Three Hearts

**触发条件或事件外补充：**

- In any season except winter, enter the beach on a sunny day between 7am and 3pm. This event only happens in Year 1.

**Details：**

Sam is watching his brother Vincent play in the sand. Sam says his dad used to take them to the beach on sunny days. Vincent asks if their father will come home. Sam says "Of course". Vincent mentions overhearing people talk about mass military casualties. Sam tells him not to believe them, and Vincent returns to playing. Sam feels bad for getting his brother's hopes up and asks for your opinion.

- "It's best to be honest with kids." (No effect on friendship .) Sam questions your thoughts, but then agrees that kids have to learn about the world one way or another.
- "You did the right thing. Kids should have hope." (No effect on friendship .) Sam agrees and says kids should hang on to their childhood as long as they can.

Sam tells you the band's coming together, and Sebastian really wanted Abigail to be the drummer.

##### Four Hearts

**触发条件或事件外补充：**

- Enter Sam's house when he's there.

**Details：**

Sam is in the kitchen. He says hello. As he's getting you a snack, he drops an egg on the kitchen floor. His mom hears the commotion, walks into the kitchen, and becomes upset about the mess. Sam asks you to tell her what happened.

- "Sam dropped the snack as he was handing it to me." (-10 friendship .)
- "Sam handed me the snack and then I dropped it." (+50 friendship .) Sam agrees with you.
- "Sam dropped it on purpose. He thought it would be funny." (-50 friendship .)

Jodi thanks you for being honest, and Sam insists he'll clean up the mess.

Talking to Sam after this event causes him to say "Sorry about what happened earlier."

##### Six Hearts

**触发条件或事件外补充：**

- On any day when it's not raining, enter the town between noon and 4pm.

**Details：**

Sam is skateboarding and grinding on Emily and Haley's flower box. Lewis catches him and scolds him for it. Lewis asks for your opinion.

- "You're right, sir. Sam should respect private property." (No effect on friendship .) Sam is unhappy, but obliges and says he'll just not skateboard ever again.
- "Don't blame Sam. There's nowhere else to ride!" (No effect on friendship .) Sam seems happy and agrees. Mayor Lewis becomes frustrated and states that he thought you were more mature than that but afterwards apologizes to Sam and asks him to be more careful in the future.
- "I'm staying out of this." (No effect on friendship .) Mayor Lewis says he doesn't want to see Sam doing it again, Sam agrees and the Mayor leaves. Then Sam turns to you and, with a smile, asks if you saw his rad trick.

##### Eight Hearts

**触发条件或事件外补充：**

- Sam shows up at your doorstep between 6am and 8am. Only triggers if you've seen his two-heart event.

**Details：**

Sam invites you to see his band play in Zuzu City and asks to meet at the bus stop at 4pm. Enter the bus stop map between 4pm and 7pm to meet Sam and the others, and watch them play. He thanks you for inspiring his band with the type of music they should play. This heart event does not require the bus to be repaired.

If you have skipped Sam's 2-heart cutscene, cheerful pop music will play during this heart event.

Additionally, no time will have passed during the heart scene (unlike festivals, which always end the day), so if the bus stop map is entered at 4pm, you will return at 4pm as well.

##### Ten Hearts

**触发条件或事件外补充：**

- After receiving a letter from Sam, enter the town on a sunny day between 8pm and midnight.

**Details：**

You meet Sam outside his house. He says it's cold outside and sneaks you into his room to talk privately. As he admits he's falling for you, his mom knocks on the door. He has you hide in the bed. His mom comes in and asks why he's sweating and red in the face, and Sam says he's just been doing push ups. She wishes him good night and leaves.

You are presented with the option to:

- Get out of the bed. (No effect on friendship .) (If you take this option, the game presents the following 2 more choices) Move Closer. (No effect on friendship .) You return Sam's affections, and the two of you share a kiss. Head for the window. (No effect on friendship .) You reject Sam's advances.
- Stay put. (No effect on friendship .) Sam crawls into bed with you, kisses you, and says "I knew there was something special between us."

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelors, raised friendship with each bachelor to 10 hearts, and seen each bachelor's 10-heart event, then entering The Stardrop Saloon will trigger a cutscene. If Alex is the final bachelor you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a friendly game of pool.

If the player does not have a Rabbit's Foot in inventory, all bachelors will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelors will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelors will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Part 1: Enter an upgraded farmhouse (needs to be upgraded at least twice) between 6:10am and 5:00pm, when Sam is inside. Part 2: Three days later, enter the farmhouse between 6:10am and 5pm, when Sam is inside. Part 3: Three days later, enter the farmhouse between 6:10am and 5pm, when Sam is inside. Part 4: Four days later, enter the farmhouse between 6:10am and 5pm, when Sam is inside.

**Details：**

Part 1:

  - Sam says he feels like he's gotten lazy since moving into the farmhouse and he wants to find some work -- something to do with music.

Part 2:

  - Sam receives a job offer in the mail, making music for a kids' TV show called "The Happy Junimo Show". He says it's not exactly what he had in mind. Just think of this as a stepping stone in your career... (No effect on friendship .)
  - Sam responds "Hmm... Yeah, I guess that's one way to look at it." Just think of how happy you'll make the children! (No effect on friendship .)
  - Sam responds "I mean... you're right, someone's gotta make children's music. But it's not exactly a 'dream job'..." I'm sorry... (No effect on friendship .)
  - Sam responds "Ah well... that's okay. I'll make the best of it, like I always do."

  - Sam continues by saying "I guess I'd better start 'thinking like a kid'..." That should be easy for you... (No effect on friendship .)
  - Sam exclaims "Hey!" while the player giggles. You could ask your little brother for help! (No effect on friendship .)
  - Sam says that's not a bad idea and thanks the player for the advice.

Part 3:

  - Sam is making progress on the song, and plays what he has written so far on an acoustic guitar. He feels positive about the job, and hopes the studio is happy with his song when it's finished.

Part 4:

  - The player, Vincent , and Jas gather around a TV set in Sam's room in the farmhouse. Sam plays a video of his song. Afterward, he expresses surprise at how much Vincent and Jas love it. He thanks the player for the support and gives a Sam's Boombox so the player can listen to the song anytime.

<a id="npc-event-sebastian"></a>

### 05. 塞巴斯蒂安（Sebastian）

> 来源：中文 revision 55064；英文 revision 193877
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、29 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 当塞巴斯蒂安在 家 时进入他的房间。

**详情：**

进入房间后，你会看到塞巴斯蒂安正在用他的电脑工作。他让你稍等一下以便完成手头的工作。此时你可以选择“他很忙……我还是走吧”或“待在原地”。但无论选择哪个选项，他都会很快完成工作并因为让你等了一会儿而向你道歉。接着你可以做出以下选择：

- “问问他刚刚在干什么。” （不影响 好感度 ） 他会说自己有时候会接一些编程的零活。
- “称赞他房间的装饰。” （不影响 好感度 ） 他会说：“装饰？哦，对哦……谢谢了。我在墙上贴海报已经贴好多年了。确实有点乱呢。”

接着他的电脑上会收到一条消息，塞巴斯蒂安解释说是 山姆 找他出门玩，但他不想出门。 罗宾 稍后进入他的房间，告诉他 阿比盖尔 正在找他，过会儿会过来玩。塞巴斯蒂安问罗宾是否告诉她他正在工作，罗宾回答是的，但阿比盖尔还是会过来。罗宾离开了房间，塞巴斯蒂安表示愤慨，没有人认真看待他的工作。接着你可以做出以下选择：

- “问问他的工作目标。” （不影响 好感度 ） 他会说自己正在攒钱，想要搬到城里去。他还说比起和人面对面相处，躲藏在屏幕后面要舒服得多。
- “问问他为什么不想见到朋友。” （不影响 好感度 ） 他会说自己喜欢交朋友，但也需要许多时间来独处。 山姆 则完全受不了一个人待太长时间，正好相反。他解释说可能正是因为这个，他才会那么喜欢电脑。在他看来，电脑充满魅力，直截了当，又很无私，而他认识的人里面却没几个有这样的品格。

最后，他会说自己在第二天之前要把那个模块完成，然后就继续去工作了。

##### 4心事件

**触发条件或事件外补充：**

- 在11:00到17:00之间前往 深山 。

**详情：**

你会看到塞巴斯蒂安正在他家的车库里修理一辆摩托车。他解释说这是自己的摩托车，有时候他会骑着摩托远离星露谷。他提议让你某一天和他一起骑车出去，你可以选择同意与否，但均不会影响与他之间的 友谊 。

##### 6心事件

**触发条件或事件外补充：**

- 当塞巴斯蒂安在 家 时进入他的房间。

**详情：**

塞巴斯蒂安和你打招呼，并邀请加入他和 山姆 ，一起玩“索拉里昂英雄传奇：游戏版”。你可以通过对话选项做出不同的选择以完成该剧情游戏，完成后你会得到一个A-D之间等级的评分，且无论选择任何选项或得到任何等级的评分都不会影响 好感度 。

你可以选择一个角色开始游戏，塞巴斯蒂安和山姆会扮演另外的两个角色：

- “战士。我喜欢直截了当。” （不影响 好感度 ）
- “牧师。我喜欢帮助他人。” （不影响 好感度 ）
- “法师。唯有敏锐的头脑才是最锋利的武器。” （不影响 好感度 ）

游戏中的选项会根据选择的职业而有所不同，但选择任何职业都可以获得A级的评分。按以下选择进行游戏，可以在最后获得A级评分。

1. 从正门进入。
2. 与骷髅对战。
3. 骷髅冲过来的时候举起盾牌。
4. 进入左侧的绿色发光通道。
5. 摧毁容器。
6. 最后与Boss恐怖领主萨尔斯战斗时，需要根据你扮演的角色做出相应的选择： 战士：当萨尔斯吟诵咒语时，选择用盾牌保护同伴。萨尔斯释放的技能会被盾牌弹开，之后你会挥着剑冲上去并了结他。一段剧情后，事件结束。 牧师：在萨尔斯释放技能并同时重创你的同伴后，选择治疗法师（塞巴斯蒂安）。最后塞巴斯蒂安使用技能终结了萨尔斯。一段剧情后，事件结束。 法师：当萨尔斯吟诵咒语时，选择对同伴施放“护盾术”。你施放的“护盾术”会弹回萨尔斯击中塞巴斯蒂安的法术，打中并击杀了恐怖领主自己。一段剧情后，事件结束。

##### 8心事件

**触发条件或事件外补充：**

- 在雨天的12:00到23:00之间前往 海滩 。

**详情：**

塞巴斯蒂安站在码头上。他很惊讶在下雨时看到你在户外。他告诉你他在面对别人时会很焦虑，但是当他和你在一起的时候却不会。随后他会拿出一把伞，让你和他一起站在伞下。

##### 10心事件

**触发条件或事件外补充：**

- 在20:00到00:00之间前往 深山 。

**详情：**

塞巴斯蒂安在他家外面。他看见你后会说自己正好要骑摩托车出去兜风，邀请你和他一起。之后他便带着你去了一个自己经常思考人生的地方，同时享受城市的景色。

如果玩家的角色是女性，他会说自己通常不会把女孩带到这个地方。如果玩家是男性，他会承认自己从来没有对其他男生有过这种感觉，但是你不一样。

他点了几次烟，然后问你待在这个地方的感觉。接着你可以做出以下选择：

- “好美啊。” （不影响 好感度 ）
- “这让我有一种莫名的伤感。” （不影响 好感度 ）
- “有点儿丑。” （不影响 好感度 ）
- “你该戒烟了。” （不影响 好感度 ） 如果选择这个选项，塞巴斯蒂安会有点生气，觉得你说起话来像他妈妈。但是随后他会承认这是一个坏习惯，并会试着戒烟。

最后他承认自己对你有好感，两人在满月下相拥在一起。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的男性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身男性村民的10心事件后仍然处于未婚状态，进入 星之果实酒吧 时将会触发过场剧情。
- 如果最后一个触发的事件是 亚历克斯 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身男性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有男生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内男生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和他们对话，他们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成男人间一场友好的台球比賽。

##### 14心事件

**触发条件或事件外补充：**

- 在雨天的早上6點到晚上7點之间前往 深山 。

**详情：**

塞巴斯蒂安注意到你時正站在湖邊。他因为你的到來鬆了一口氣，並希望你帮他拯救一隻躲在灌木叢裡的受傷青蛙。你走到塞巴斯蒂安左邊的灌木叢並搖晃它，令青蛙跑向他的方向。他順利抓住青蛙並擔憂地檢查青蛙的傷勢，發現青蛙的腿傷得很重。接着你可以做出以下选择：

- “我們應該怎麼做？” （不影响 好感度 ）
- “我要收養他……” （不影响 好感度 ）
- “我不認為他會成功自愈” （不影响 好感度 ）
- “讓我們護理他，幫助他恢復健康！” （不影响 好感度 ）

塞巴斯蒂安会基於你的选择做出不同回应，最后他会決定帶青蛙回家。

在第二天的6:20到晚上7點之间進入 农舍 觸發下半部分事件:

塞巴斯蒂安把他房間裡的桌子換成了生物養育箱。他解釋说因為這隻青蛙再也無法在野外生存，所以為牠做了生物養育箱。他很欣慰青蛙漸漸變得健康，但覺得青蛙可能會感到孤獨。接着你可以做出以下选择：

- “为什么不开设一个‘青蛙保护区’” （不影响 好感度 ） 塞巴斯蒂安会觉得这个主意很不错。
- “他会过的很开心。” （不影响 好感度 ） 塞巴斯蒂安会希望能再发现另一只受伤的青蛙，这样它们也能做個伴。

随后你需要做出另一個选择:

- “你為什麼那麼喜歡青蛙？” （不影响 好感度 ） 他会说自己喜欢在雨中外出，遇到过很多这样的青蛙，最终感觉到了和这帮小家伙的共同纽带。
- “我真的不想在家裡看到這個” （不影响 好感度 ） 他会有些生气，觉得这不是争论的时候，并会说这是家里属于他的一角，他想做什么都可以。
- “很高興你找到了新的愛好” （不影响 好感度 ） 他会表示赞同，认为这会很有趣。他说自己花了很多时间在电脑上，所以有一些实际生活中的爱好是很不错的。塞巴斯蒂安甚至还觉得自己可以亲手尝试青蛙繁殖。

事件结束后，塞巴斯蒂安的房間会永久多出一個生物養育箱，你可以經常看到一兩隻青蛙在裡面跳來跳去！

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个事件/后续条目、8 个事件外层条件或补充段落、7 张详情表、26 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Sebastian's room when he's there.

**Details：**

You find Sebastian working on his computer. He asks you to wait, he needs to finish something. You are given two options, "He is busy, maybe I should leave" or "Stay put". In both options, he quickly finishes his work and then apologizes for making you wait.

- "Ask him what he was working on" (No effect on friendship .) He says "I do freelance work as a programmer."
- "Compliment him on his room decor" (No effect on friendship .) He says "Decorations?... Oh, yeah… thanks. I’ve been sticking posters on the walls for years, I guess it’s kinda cluttered."

Sebastian receives a notification from Sam asking to hang out, but Sebastian says would rather not go out. Robin enters his room moments later, telling him that Abigail was looking for him and will stop by later. Sebastian asks whether Robin told her that he was working, and Robin says yes, but Abigail decided that she would probably stop by anyway. Robin leaves the room, and Sebastian expresses his irritation that nobody takes his job seriously.

- "Ask him about his career goals" (No effect on friendship .) He says he’s saving up to move to the city. He says he prefers working as a freelance programmer because he isn’t part of the corporate rat race and because he feels more comfortable working behind a computer instead of face to face.
- "Ask him why he doesn't want to see his friends" (No effect on friendship .) He says "I like having friends, I just need a lot of time alone to balance out the social stuff. Sam’s the opposite… he goes crazy if he’s alone for too long. Maybe that’s why I like computers so much… They’re engaging, straightforward, and unselfish. Quite the opposite of a lot of people I know."

He then goes back to work, saying "I need to get this module finished by tomorrow."

##### Four Hearts

**触发条件或事件外补充：**

- Go to The Mountain between 11am and 5pm.

**Details：**

You see Sebastian working on a motorcycle in the garage at his house. He explains that it belongs to him and sometimes he goes for long rides alone far away from Stardew Valley. He suggests the possibility of you one day taking a ride with him, to which you agree or disagree.

That sounds fun. (No effect on friendship .)

  - Sebastian responds "Great."

No thanks. That sounds stupid. (No effect on friendship .)

  - Sebastian responds "Okay... Nevermind then."

I'm scared of motorcycles. (No effect on friendship .)

  - Sebastian responds with one of two dialogues, depending on the Player 's gender: "Don't worry, I'll make sure to show you the ropes before I let you do anything dangerous." "There's no need to worry... I'll make sure you're safe."

##### Six Hearts

**触发条件或事件外补充：**

- Enter Sebastian's room when he's there.

**Details：**

Sebastian greets you, and invites you to play Solarion Chronicles: The Game with him and Sam. You play through a scenario, for which you'll be given a score between A and D. You're given a choice of archetype:

- "Warrior. I like a direct approach." (No effect on friendship .)
- "Healer. I prefer to help others." (No effect on friendship .)
- "Wizard. A sharp mind is the most powerful blade of all." (No effect on friendship .)

The classes don't affect friendship, and you can achieve a perfect score with any class:

1. Go through the front door.
2. Choose to fight the skeleton, then raise your shield.
3. Go through the left hallway glowing with a green light.
4. Destroy the capsules.
5. During the final battle: Warrior: defend your friends while the wizard is mumbling an incantation. You will be able to attack the boss, and the scenario ends. Healer: heal Sebastian's wizard. Sebastian is grateful and he defeats the boss. Wizard: use "Shield Charm" while the enemy is mumbling an incantation. The enemy wizard shoots a beam at Sebastian, but your "Shield Charm" reflects it and hits the enemy in the face, killing it.

##### Eight Hearts

**触发条件或事件外补充：**

- Go to the beach on a rainy day between noon and 11pm.

**Details：**

Sebastian is standing on the boardwalk. He's surprised to see you outside in the rain. He says he's anxious around other people, but he doesn't feel that way when he's with you. He takes out an umbrella and motions you to stand under it with him.

##### Ten Hearts

**触发条件或事件外补充：**

- Go to The Mountain between 8pm and midnight.

**Details：**

Sebastian is outside his house. He says he was about to go for a ride on his motorcycle. You join him for a ride, and he brings you to a place he often goes by himself to think about his life while enjoying a view of the city.

If your character is female, he mentions that he doesn't normally bring girls to this place. Otherwise, he admits that he's never felt this way about other guys, but that you're different.

He pulls on his cigarette a few times, and then asks what you think of the city. You have four options, one of which is telling him to quit smoking. Choosing this one causes Sebastian to be briefly annoyed; he says you sound like his mom, then admits that it's a bad habit and he'll try to stop.

He confesses his true feelings for you, and you embrace under the full moon.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelors, raised friendship with each bachelor to 10 hearts, and seen each bachelor's 10-heart event, then entering The Stardrop Saloon will trigger a cutscene. If Alex is the final bachelor you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a friendly game of pool.

If the player does not have a Rabbit's Foot in inventory, all bachelors will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelors will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelors will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Go to The Mountain on a rainy day between 6am and 7pm.

**Details：**

Sebastian is near the lake when he notices you. He's relieved at your arrival and requests your help to save an injured frog hiding in the bushes. You walk to a bush on his left and shake it, causing the frog to run in Sebastian's direction. He catches it successfully, then examines the frog worriedly; his leg is too injured. You can respond with the following:

- "What should we do with him?" (No effect on friendship .)
- "It's our new son..." (No effect on friendship .)
- "I don't think he's going to make it" (No effect on friendship .)
- "Let's nurse him back to health!" (No effect on friendship .)

Sebastian responds based on your choice (teasing you if you say the frog is their son), then he decides to take the frog home with him.

Enter your farmhouse between 6:20am and 7pm the next day to trigger the next part of the event:

Sebastian has replaced his Solarion Chronicles table with a terrarium in his spouse room. He explains that he made the terrarium for the frog, since it couldn't survive in the wild anymore. He's pleased that the frog is in better health, but wonders if it will be lonely. You can respond to him here:

- "Why not start a 'frog sanctuary'?" (No effect on friendship .)
- "He’ll be fine." (No effect on friendship .)

Choosing the frog sanctuary option makes him enthusiastic about making a haven for frogs, while the latter option has him agree, but still wish the frog had a friend. Another prompt appears:

- "Why do you like frogs so much, anyway?" (No effect on friendship .)
- "I don't really want this in the house" (No effect on friendship .)
- "I'm glad you've found a new hobby" (No effect on friendship .)

If you ask him why he likes frogs, he tells you that he gained a natural affinity for frogs from being out in the rain. If you congratulate him on his new hobby, he enthuses about having a physical hobby and says he might even consider frog breeding.

Telling him you don’t want the frogs in the house makes him firm in keeping them, and tells you that he can do whatever he wants in his spouse room.

After the event, Sebastian's spouse room permanently changes to have a terrarium containing frogs.

<a id="npc-event-shane"></a>

### 06. 谢恩（Shane）

> 来源：中文 revision 55046；英文 revision 193586
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 12 个事件/后续条目、16 个事件外层条件或补充段落、12 张详情表、2 个列表/选择项、5 张嵌套结果表（8 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当谢恩对玩家的 好感度 大于0，谢恩就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 披萨 爆炒青椒 | 嘿， 我觉得给你写信会很有趣。虽然我其实不怎么会写。 我随信附上了一个小礼物。别告诉其他人，这是很久以前我从Joja超市里搞来的。 好了，回头见。 -谢恩 |

##### 2心事件

**触发条件或事件外补充：**

- 在20:00至12:00期间进入 煤矿森林 。

**详情：**

玩家来到池塘的码头上，谢恩分给玩家一罐啤酒，并向玩家倾吐自己心事和不幸。他认为自己已经无药可救，而玩家拥有远大的前程，他警告玩家不要酗酒。

注意：过场动画中饮用啤酒后，玩家恢复50点 能量值 和22点 生命值 ，并且获得 眩晕 的 效果 。

##### 3心事件

**触发条件或事件外补充：**

- 与谢恩的好感度达到3颗心后，他会通过邮件向你发送一份食谱。
- 他的日常对话也会变得更有礼貌。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 爆炒青椒 | 我在杂志上看到了这个配方，看起来挺有意思的。如果你照着做了，不妨让我尝尝吧。 -谢恩 |

##### 4心事件

**触发条件或事件外补充：**

- 与谢恩的好感度达到4颗心后，他的日常对话会变得更有礼貌。
- 在任意时间进入 玛妮的牧场 。

**详情：**

谢恩昏倒在他的房间里，他的周围散落着空啤酒罐。玛妮向玩家求助，玩家往谢恩的头上浇水后才让他转醒。玛妮对谢恩酗酒的行为感到担忧，问他有没有计划、有没有想过未来。谢恩说 “希望我不会活到需要‘计划’的时候…” ，即想要自杀。贾斯听到后被吓到，哭着跑开，玛妮也跟着走了。谢恩跪坐在地上哭泣，向贾斯道歉。

提示：此处对话翻译存在较大的问题。 中文翻译为“希望找到我的人生计划不需要花费很长时间……”，而英语原文为“Hopefully I won't be around long enough to need a 'plan'...”（希望我不会活得太久，以至于需要一个‘计划’…）

##### 6心事件

**触发条件或事件外补充：**

- 在雨天的09:00到20:00期间进入 煤矿森林 。

**详情：**

谢恩躺在悬崖上，身边又堆满了空啤酒罐。他认为自己是个可悲的笑话，他根本掌控不了自己的人生。他问玩家：

- “为什么我还要继续？ 告诉我…… 告…… 告诉我为什么我不应该现在马上从悬崖边上滚下去…… 因为有太多的留恋！ （不影响 好感度 ） 也许对你来说是这样，但对我来说可并非如此！你不会明白的……你走开。……呃……等等…… 贾斯需要你。你就像她的父亲。 （不影响 好感度 ） ……你是对的。贾斯……呃，天哪……我太自私了, *呃呃*……我是自私的人。现在我觉得更内疚了…… 因为这会是一种罪恶。 （不影响 好感度 ） 由巴……？[玩家名]，你不知道我是无神论者吗？呃。 这是你自己的决定。我只知道为了你我会一直在这里。 （不影响 好感度 ） ……谢谢……我感激不尽……真的。”

无论怎样，谢恩都会让你把他送到医院。到医院之后， 哈维 治好了谢恩身体上的问题，但对他心理上的问题更为担忧，他建议谢恩去 祖祖城 接受心理医生的治疗。 次日早上，谢恩会到农场上找玩家：

- “关于在悬崖上发生的事情，我很抱歉。 真是…… 令人尴尬…… 我很高兴我能帮到忙。 （ 好感度 +10） ……是的，我也是。 你需要一个正式的警钟。 （ 好感度 -10） 我知道……这就是为什么我停下来，告诉你这个。 提示： 这里的“停下来”指的是来农场上找玩家。即“我知道……所以我才会过来找你。” 我很高兴你还活着。 （ 好感度 +10） 哇，有那么严重吗？我都快记不清了……”

谢恩告诉玩家他要找心理医生接受治疗。他告诉玩家他决定要开始认真对待事情，他不想成为任何人的负担。

##### 7心事件I

**触发条件或事件外补充：**

- 6心事件触发后，在谢恩在家时进入 玛妮的牧场 。

**详情：**

谢恩从后面出来告诉玛妮自己现在比以前开心了许多，玛妮开玩笑道是不是啤酒清仓甩卖了，谢恩有点小生气，回应道自己已经开始戒酒了，现在在喝苏打水。接着说他意识到了自己还有人可以依靠，这么做会让自己不再脆弱。然后他走向厨房里的贾斯，送了她一个礼物。贾斯打开礼物发现是一双自己心慕已久的昂贵鞋子 。她问谢恩哪里有钱给她买礼物时，谢恩回答说这都是省下的酒钱。

##### 7心事件II

**触发条件或事件外补充：**

- 在晴天的10:00至16:00之间进入小镇。 (需要与 艾米丽 和 克林特 的好感度同时达到2心才可触发)。

**详情：**

你会发现谢恩在拍摄一个影片，主演是 艾米丽 和 克林特 。谢恩向你解释说JOJA正在举办一个比赛，为最新的Joja可乐拍摄一个广告，获胜者会获得 10,000 . 他会请你担任群演以便艾米丽和克林特的表演更自然。拍摄结束后，他会感谢你的帮助。

* 在 版本 1.1 之前这是个6心事件。

##### 7心事件III

**触发条件或事件外补充：**

- 与谢恩的好感度达到7颗心后，他会通过邮件向你发送一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 奇怪的小面包 | 我在杂志上看到了这个配方，看起来挺有意思的。如果你照着做了，不妨让我尝尝吧。 -谢恩 |

##### 8心事件

**触发条件或事件外补充：**

- 当谢恩在家时（周末）进入 玛妮的牧场 （晴雨皆可）。

**详情：**

你会在贾斯的带领下进入 玛妮的牧场 的谷仓（厨房前锁着的门）。在里面，谢恩正在涂写一个“新鲜鸡蛋”的标语，他的周围是一群特别的蓝色小鸡和他最喜欢的一只叫“查理”的白色母鸡。你看到谢恩独自一人抱起查理并向她诉说心事，然后你进入谷仓，谢恩会告诉你他正在传授贾斯养鸡的知识，这样在他搬出小镇后，贾斯可以继承这个传统。

此事件结束后，你从 玛妮 那里购买的鸡或者孵化器里的蛋将有 1/4 的几率是蓝色的。除了颜色不一样，蓝鸡与白鸡相同。

##### 10心事件

**触发条件或事件外补充：**

- 在06:00至6点半之间离开你的房子触发该事件,然后在16:00至6点之间步行到 巴士站 。

**详情：**

谢恩会邀请你去 祖祖城 的体育场观看一场比赛。你会看到你和谢恩在一个脏脏的体育馆的看台上，然后球队进球得分，每个人都在欢呼。就在这兴奋的时刻，谢恩吻了你一下...随后他又为自己的冲动而觉得有些尴尬。稍停一会后，你主动给了他一个完整的吻并缓解了他的不安。

##### 14心事件

**触发条件或事件外补充：**

- 在非周五的上午8點至下午5點進入城鎮，並在接下來兩天任何時間進入城鎮

**详情：**

第一天，瑪妮、賈斯和你在星之果實酒吧外，謝恩從酒吧出來並說很久沒有像那樣來上一盤了。瑪妮看起來很擔心，囑咐你盯著他點和下次看到他從酒吧裡出來時要說說他。

第二天，謝恩離開酒吧時被你攔住，他因為你懷疑他喝酒而生氣地跑回了家。

第三天，瑪妮和你在酒吧外等待時謝恩走進了酒吧。你想抓他個現行，但他只是站在街機前玩遊戲。瑪妮疑惑地問他地上鐵罐的事，謝恩解釋那些全都是喬家可樂罐，還說他玩遊戲的時候會專注到沒心思想別的事情，在他有衝動想去喝酒時很有幫助。

- "對不起，我應該相信你的" （不影响 好感度 ） 謝恩會回應他知道自己不完美，但會一直努力做到最好，你們不必擔心。他的生活已經比以前好多了，他已經不在陰暗的地方
- "我們很擔心你……" （不影响 好感度 ）

過後謝恩會說你和瑪妮看到他站在街機前的時候一定很疑惑吧。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的男性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身男性村民的10心事件后仍然处于未婚状态，进入 星之果实酒吧 时将会触发过场剧情。
- 如果最后一个触发的事件是 亚历克斯 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身男性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有男生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内男生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和他们对话，他们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成男人间一场友好的台球比賽。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 12 个事件/后续条目、14 个事件外层条件或补充段落、12 张详情表、11 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Shane. The chance of receiving a gift in the mail increases as your friendship with Shane increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Pizza Pepper Poppers | Hey, I thought it would be fun to send you a letter. I don't really know what to write, though. Here, I've enclosed a treat for you. Don't tell anyone, but I snagged this from the back room of JojaMart ages ago. Okay, see you soon. -Shane |

##### Two Hearts

**触发条件或事件外补充：**

- Enter Cindersap Forest between 8pm and midnight.

**Details：**

Shane shares a beer with the player , on the dock of the pond, and describes his depression. He expresses optimism for the player's future and warns against drinking heavily.

Note: The beer consumed during the heart event will heal up to 50 Energy and 22 Health , and leave the player with the " Tipsy " buff.

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Shane, he will send you a recipe in the mail. He will also become slightly less rude to you during dialogues.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Pepper Poppers | I found this recipe in a magazine and I thought it sounded interesting. Feel free to give me a taste if you make it. hehe. - Shane |

##### Four Hearts

**触发条件或事件外补充：**

- After reaching four hearts with Shane, his dialogues with you will become more friendly.
- Enter Marnie's Ranch at any time.

**Details：**

Shane is found passed out in his room, surrounded by empty beer cans. Marnie asks you to do something, so you use your watering can on his head to wake him up. Marnie remarks that all he does is mope around and drink beer. When Marnie asks him what his plans for the future are, Shane says that he hopes he "won't be around long enough to need a plan." Jas overhears and runs away crying; Marnie follows her while Shane falls to the ground and cries while apologizing.

##### Six Hearts

**触发条件或事件外补充：**

- Enter Cindersap Forest between 9am and 8pm while storming or raining.

**Details：**

Shane is laying face down at the edge of the cliffs, again surrounded by empty beer cans. He tells you that he's miserable and asks you why he shouldn't just roll off the cliff. You can respond in four different ways:

- "Because there's so much to live for!" (No effect on friendship .) "Maybe for you, but not for me! You're not going to understand... Just... go away. ...Ugh..."
- "Jas needs you. You're like a father to her." (No effect on friendship .) "...You're right. Jas... Ugh, God... I'm a horrible, *hic*... selfish person. Now I feel even worse..."
- "It would be a sin." (No effect on friendship .) "Yoba...? (Player), don't you know I'm an atheist? Ugh..."
- "The decision is your own. Just know that I'm here for you." (No effect on friendship .) "Thanks... I appreciate that... I really do."

After that Shane suggests that you should take him to the hospital, in the next cutscene Harvey treats his physical ailments but is more concerned about Shane's mental health. He tells you that he's going to recommend Shane to a counselor in Zuzu City once he wakes up.

The next day, Shane will arrive at your farm to tell you that he intends to go to counselling. He also apologizes for the incident at the cliffs, to which you can respond in three different ways:

- "I'm glad I was there to help." (+10 friendship .) "...Yeah, me too."
- "You needed a serious wake-up call." (-10 friendship .) "I know... That's why I stopped by, to tell you about it."
- "I'm just happy you're still here." (+10 friendship .) "Wow, it was that serious, huh? I can hardly remember..."

##### Seven Hearts I

**触发条件或事件外补充：**

- Enter Marnie's Ranch while Shane is home after triggering Shane's six heart event.

**Details：**

Shane enters the ranch, where Marnie is standing behind the counter. He tells her that he's been feeling happier than usual. Jokingly, she asks if there was a sale on beer. Though slightly annoyed, he responds by saying he's started drinking sparkling water instead. He then says that he's realized that he has people that he can rely on and that doing so doesn't make him weak. He walks over to Jas, who is in the kitchen, and gives her a present. She opens it to find a pair of expensive shoes that she had wanted. When she asks Shane how he could afford it, he replies that it's because he cut back on his expensive habit of drinking beer.

##### Seven Hearts II

**触发条件或事件外补充：**

- Enter the town between 10am and 4pm on a sunny day. (Also requires 2 hearts with both Emily and Clint .)

**Details：**

You will find Shane filming a scene starring Emily and Clint . Shane will explain to you that Joja is holding a contest to create an advertisement for the newest Joja Cola, and the winner gets data-sort-value="10000"> 10,000g . He will ask you to walk behind Clint and Emily as they act so the scene feels more natural. When it's over, he will thank you for helping him.

* This event was Shane's six heart event before update 1.1 .

##### Seven Hearts III

**触发条件或事件外补充：**

- After reaching 7 hearts with Shane, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Strange Bun | I found this recipe in a magazine and I thought it sounded interesting. Feel free to give me a taste if you make it. hehe. - Shane |

##### Eight Hearts

**触发条件或事件外补充：**

- Enter Marnie's Ranch while Shane is home. Note: Will not trigger until the player has seen the follow-up visit from Shane after his 6-heart event.

**Details：**

When you enter the ranch, Jas leads you through the door in the kitchen that is normally locked. Inside, Shane is painting a sign that says "Fresh Eggs." He's surrounded by his flock of special blue chickens and his favorite white chicken, Charlie. Once he finishes painting the sign, he picks up Charlie and briefly talks to her about his ambitions and his struggles. When you and Jas enter the room, Shane talks to you a bit about how he is trying to pass on the chicken knowledge to Jas so she can continue the tradition if he ever moves out.

After seeing this event, each chicken that the player purchases from Marnie and each egg that hatches in the incubator now has a 25% chance of being blue. Aside from appearance, the blue chickens are identical to white chickens.

##### Ten Hearts

**触发条件或事件外补充：**

- Exit your house before 6:30am to initiate the event, then walk to the Bus Stop between 4pm and 6pm.

**Details：**

Shane invites you to go see the Zuzu City Tunnelers (a gridball team) play in their stadium in Zuzu City . You take a bus into the city together and the scene changes to a grimy stadium with you and Shane in the stands. While cheering on the Tunnelers, Shane thanks you for sticking with him through his struggle with depression and anxiety. He then asks you what you think of your first gridball game:

- "Noisy... It makes me appreciate how peaceful it is back home." (No effect on friendship .) "Oh yeah? I guess that makes sense. Me? I get bored with Pelican Town sometimes. But... I like that you're different. We balance each other out."
- "Fun... Pelican Town seems really boring in comparison." (No effect on friendship .) "Oh really? I'm surprised... Didn't you move to Stardew Valley to escape the noise of the city? I mean... Don't get me wrong, I totally understand. My life in Pelican Town is pretty bland, you know."

His attention returns to the game when the Tunnelers make a play and score a goal. In a moment of excitement, Shane gives you a kiss, but then he feels embarrassed by it and apologizes for getting carried away. After a pause, you reply with a kiss and allay his fears. The scene pans to the northwest and fades and Shane briefly reflects on the evening.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelors, raised friendship with each bachelor to 10 hearts, and seen each bachelor's 10-heart event, then entering The Stardrop Saloon will trigger a cutscene. If Alex is the final bachelor you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a friendly game of pool.

If the player does not have a Rabbit's Foot in inventory, all bachelors will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelors will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelors will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Enter town on a non-Friday between 8am and 5pm. For parts II and III enter town anytime each of the next two days.

**Details：**

On the first day, Marnie, Jas, and yourself are outside of the saloon. Shane comes out of the bar, saying that he hasn't had a session like that in a while. Marnie looks worried, and asks you to talk to him next time he comes out of the saloon.

On the second day, Shane comes out and you confront him. Shane gets upset at the suggestion that he's been drinking, and runs home.

On the third day, Marnie and you are waiting outside the saloon, and Shane goes in. You try to catch him in the act of drinking, but he is instead standing in front of an arcade machine. Marnie is confused and asks about the cans on the floor, and Shane explains that they're Joja Cola cans. He also explains that playing video games helps him calm the urge to drink.

- "I'm sorry, I should've believed you." (No effect on friendship .) That's alright, (Player). You're just looking out for me. I get it. Look... I know I haven't been perfect... but, I'm trying my best... and I'm gonna keep trying. So you don't have to worry about me. My life is better now than it's ever been. I'm not in such a dark place anymore...
- "I was worried!" (No effect on friendship .)

Afterwards, Shane will say that you and Marnie must have been confused to see him in front of the arcade machine.

<a id="npc-event-abigail"></a>

### 07. 阿比盖尔（Abigail）

> 来源：中文 revision 55185；英文 revision 193689
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 8 个事件/后续条目、11 个事件外层条件或补充段落、7 张详情表、15 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 当阿比盖尔在 家 时进入她的房间，周六除外。

**详情：**

你进入阿比盖尔的房间，发现她因为无法通关电子游戏而发脾气。她向你寻求帮助，于是你和她一起玩主机板的 草原王者大冒险 。(这个版本和 星之果实酒吧 里的电玩版本差不多，但是阿比盖尔会操纵另一个角色来帮助你。要注意，如果她操纵的角色死亡，也会消耗你的角色的生命，所以记得捡额外生命。)无论你是否通关，游戏结束后，她都会说感谢你。

该事件不会改变你与阿比盖尔的 友谊 值。

##### 4心事件

**触发条件或事件外补充：**

- 雨天，正午到19:00间进入 深山 。冬季无法触发。

**详情：**

你发现阿比盖尔在演奏长笛。她会问你你在雨中站着做什么。

- “我只是在工作。” （不影响 好感度 ）
- “我在享受这样的天气。” （ 好感度 +50）
- “我也想问你呢。” （ 好感度 +10）

不管你怎样回答，她都会让你和她一起在树下避雨。你会掏出一个竖琴和她演奏二重奏，这时镜头向湖面延伸。

##### 6心事件

**触发条件或事件外补充：**

- 在晴天或者雪天的21:00到午夜这个时段走进 鹈鹕镇 。

**详情：**

你发现阿比盖尔一个人在墓地里。她告诉你她一直在练习用剑，因为她想有一次冒险。她问你是否使用过剑。

- “没错，我觉得很刺激！” （ 好感度 +10）
- “是的，但只是为了自卫而已。” （ 好感度 +10）
- “没错，但是太危险了，你不应该冒险。” （ 好感度 -100）
- “没有。” （不影响 好感度 ）

皮埃尔 发现了 阿比盖尔 ，过来制止并且说 卡洛琳 想让她帮助做晚饭。阿比盖尔很生气，说他们只是因为我是个女孩子就想让我帮助做饭。她叫你和她一起跑掉。你们俩藏在灌木中悄悄说话。

##### 8心事件

**触发条件或事件外补充：**

- 收到 阿比盖尔 的信之后，在20:00到10点间去 皮埃尔的杂货店 找她。（注意，皮埃尔的杂货店在9点关门）

**详情：**

阿比盖尔在信中（署名Abby）邀请你去她的闺房。你到了后她会给你看一个灵板。灵板揭示出了她内心中对你有了感觉这一事。她十分害羞且尴尬，于是把你推出了她的房间。第二天早上她在你门前等你并为昨天无礼的行为道歉。

##### 10心事件

**触发条件或事件外补充：**

- 当你给阿比盖尔送过 花束 后，在17:00和午夜之间进入 矿井 或 采石场矿井 。如果你已给她送过 美人鱼吊坠 ，则该事件不会发生。

**详情：**

阿比盖尔正在准备从楼梯进入矿井，这时，她被一只朝她脸上飞来的蝙蝠吓到了。她被自己逗笑了，然后重新向矿井下看。突然无数只蝙蝠飞了出来，她被吓得逃到角落蜷缩着颤抖。你冲上前安抚她。

- “发生了什么？” （ 好感度 +20）
- “你还好吗？” （ 好感度 +40）

她告诉你她没有自己想象得那么坚强。

- “"我陪着你呢，你是安全的。” （ 好感度 +20）
- “"我也害怕。” （ 好感度 +40）
- “"别哭了，你像个三岁小孩儿一样。” （ 好感度 -50）

她承认她对你的喜欢不仅仅是普通朋友，并且让你陪着她。她吻了你。如果你的角色是女性，她会承认她不知道自己会喜欢女生，直到遇见了你。

##### 10心之后事件

**触发条件或事件外补充：**

- 10心事件以后，在下雨天，她会出现在 矿井 的20层（仅在单人模式下出现， 联机模式 不会出现）。
- 首次在 矿井 遇见阿比盖尔时，她会有一段独特的对话。在此之后，有15%的几率发现她在吹笛，85%的几率在附近走动。如果她没有在吹笛子，玩家就能与她对话。

##### 14心事件

**触发条件或事件外补充：**

- 進入農場北邊前往 木匠的商店 的小徑

**详情：**

玩家在灌木叢采集時一隻怪物從玩家下方的灌木叢中跳出，怪物會攻擊玩家使玩家昏倒。阿比蓋爾出現看到玩家被怪物攻擊昏倒冲上前去并殺死怪物，她會詢問玩家有沒有事，並表示自己之前從來沒有殺過活物。

Monster Grave

- “这令人难过，但我们没有其他选择。” （不影响 好感度 ）
- “怪物不值得我们同情！”" （不影响 好感度 ）
- “孩子，这个世界很残酷。” （不影响 好感度 ）

玩家有三個選項可供選擇，阿比蓋爾要求你要更加小心，她不想失去你。最後阿比蓋爾會找個安靜的地方埋掉怪物。这里会多了一块墓碑，上面写着“阿比盖尔为了救我，夺走了一条生命…… 我永远不会忘记此事。”

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的女性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身女性村民的10心事件后仍然处于未婚状态，进入 艾米丽和海莉的家 时将会触发过场剧情。
- 如果最后一个触发的事件是 海莉 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身女性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有女生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内女生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和她们对话，她们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成女生们会一起讲八卦，讨论 刘易斯 与 玛妮 二人不可告人的秘密。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 8 个事件/后续条目、10 个事件外层条件或补充段落、7 张详情表、16 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Pierre's General Store when Abigail is there, any day except Saturday.

**Details：**

You enter Abigail's room and watch her get angry about a videogame. She asks for your help, and you play the console version of Journey of the Prairie King together. (This is just like the arcade version in the Stardrop Saloon , except that Abigail plays a second character and actively helps you). When you finish the level, she thanks you and the cutscene ends. If you fail, however, she will still thank you for trying.

You can't gain or lose friendship points during this heart event.

##### Four Hearts

**触发条件或事件外补充：**

- Visit the mountain between noon and 7pm on a rainy day, any season except Winter.

**Details：**

You see Abigail playing her flute. She asks what you're doing out in the rain.

- "Just doing some work." (No effect on friendship .)
- "Enjoying the weather." (+50 friendship .)
- "I could ask you the same question." (+10 friendship .)

Regardless of your response, she invites you to stand under the tree with her. You pull out a lyre (Abigail calls it "a mini harp!") and you play a duet as the camera pans out over the lake.

Note that if the player has cut down the tree near the mountain lake it will not be present during the 4 heart event, but Abigail will still reference the tree during the dialogue.

##### Six Hearts

**触发条件或事件外补充：**

- Between 9pm and midnight on a day when it is not raining, enter Pelican Town from any direction. (This includes exiting homes or shops in Town.)

**Details：**

Abigail is in the graveyard. She tells you that she's been practicing with her sword because she wants to go on adventures. She asks if you've ever used a sword.

- "Yes, and it's exciting!" (+10 friendship .)
- "Yes, but only in self-defense." (+10 friendship .)
- "Yes, but it's dangerous. You should stay safe." (-100 friendship .)
- "No." (No effect on friendship .)

Pierre arrives and interrupts to say that Caroline wants her to come help cook dinner. Abigail gets angry, saying they only expect her to help cook because she's a girl. She walks off, calling for you to follow. You both hide in some bushes and talk. After talking she will ask you to help her untangle her hair from a bush, and the cutscene ends.

##### Eight Hearts

**触发条件或事件外补充：**

- After receiving a letter from Abigail, enter Pierre's General Store between 8pm and 10pm when she's there. (Note that, unless you have the Key To The Town , you cannot enter the store from outside after 9pm, but you can wait in Caroline 's greenhouse and trigger the event by exiting to the kitchen.)

**Details：**

Abigail sends you a letter (signed "Abby") inviting you to visit her in her room. When you arrive, Abigail shows you her spirit board. It reveals a message that indicates she's starting to develop feelings for you. She gets embarrassed and rushes you out of her room. Regardless of how you entered the store, you will end up outside. The next day she visits you in the morning and apologizes.

##### Ten Hearts

**触发条件或事件外补充：**

- Enter the mines or the Quarry Mine (or ascend from a lower floor of the mines) between 5pm and midnight. The event won't trigger if you've already given her the Mermaid's Pendant .

**Details：**

Abigail is preparing to go down the ladder into the mine when she's startled by a bat flying up into her face. She laughs it off and looks back down the hole. Hundreds more bats fly up and she's terrified, running to cower in the corner of the cave. You rush in to comfort her.

- "What happened?" (+20 friendship .)
- "Are you okay?" (+40 friendship .)

She tells you that maybe she isn't as tough as she thought.

- "You're safe with me." (+20 friendship .)
- "I get scared too." (+40 friendship .)
- "You're crying like a little baby. Stop." (-50 friendship .)

She confesses that she likes you as more than a friend, and asks you to stay with her there. She hugs you. If your character is a girl, she will also state that she didn't know she liked other girls until she met you.

##### After the 10-Heart Event

**触发条件或事件外补充：**

- After viewing Abigail's 10-heart event, she will appear in the Mines on level 20 on days when it is raining. She will not appear in a Multiplayer game, only in single-player mode.
- The first time the player encounters Abigail in the Mines, she has unique dialogue. Thereafter, there is a 15% chance to find her playing the flute, and an 85% chance of finding her walking in place. If she is not playing the flute, she will speak to the player.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelorettes, raised friendship with each bachelorette to 10 hearts, and seen each bachelorette's 10-heart event, then entering Haley/Emily's House will trigger a cutscene. If Haley is the final bachelorette you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a gossip session about Mayor Lewis and Marnie 's relationship.

If the player does not have a Rabbit's Foot in inventory, all bachelorettes will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelorettes will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelorettes will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Enter the Backwoods between 6:10am and 5pm.

**Details：**

The player is foraging in bushes as a monster appears from a bush. It attacks the player and the player collapses. Abigail appears and kills the monster. She asks if the player is okay and says "I've never taken a life before."

Monster Grave

- It's sad, but there was no other option. (No effect on friendship .)

Abigail responds "Yeah... I did what I had to do. I guess the world's a pretty tough place. It was either you or him, right?"

- Monsters don't deserve our sympathy! (No effect on friendship .)

Abigail responds "...Aren't they just trying to survive, like us? They may be our enemies, but I still think they deserve sympathy. Still... I did what had to be done."

- It's a harsh world, kid. (No effect on friendship .)

Abigail responds "Huh? That's pretty funny coming from someone who just got rescued... But... yeah... Sometimes reality forces us to do things we'd rather not... Guess I'm learning that the hard way."

- Did you have to kill him? (No effect on friendship .)

Abigail responds "Hey! I saved your life, didn't I? Maybe you should think about that instead of putting me on a guilt trip."

Abigail warns the player to be more careful in the future, saying "I don't want to lose you." Then, she buries the monster and marks the grave with the symbol of Yoba . Interacting with the grave displays the text: "Abigail took a life to save mine...I'll never forget that."

If you go home and talk to Abigail the same day as the event she'll say: "Good thing I brought my sword today!"

<a id="npc-event-emily"></a>

### 08. 艾米丽（Emily）

> 来源：中文 revision 55091；英文 revision 191968
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 10 个事件/后续条目、15 个事件外层条件或补充段落、10 张详情表、3 个列表/选择项、5 张嵌套结果表（8 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当艾米丽对玩家的 好感度 大于0，艾米丽就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 布料 海胆 动物毛 | 嗨！ 你还好吗？希望你能喜欢我给你送去的礼物……那么，再见！ -艾米丽 |

##### 2心事件

**触发条件或事件外补充：**

- 当艾米丽在家时进入 柳巷2号 。

**详情：**

艾米丽正在她的卧室里睡觉。屏幕上的画面一转，你发现自己正在观看艾米丽的梦。这是一个充满了抽象的图形与色彩、云朵与棕榈树的幻境空间。艾米丽漂浮在一片巨大云层上的一个紫色石砌结构上。她一边冥想，一边吟诵着一些“魔法咒语”。这时你出现在云上，让她非常惊讶。她想知道为何你在她的梦境当中。此时一些彩虹条纹飞过画面，艾米丽认为这是某种征兆。你消失了，她从睡梦中醒来。她下床之后自言自语，认为你有些特殊之处，她相信你们之间的命运会在不久的将来交织在一起。

##### 3心事件

**触发条件或事件外补充：**

- 与艾米丽的友谊到达三星以后，她会邮寄一个食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 沙拉 | 把这封信翻过来，上面写有一种超级健康的饭菜做法！ 那会让你感觉精力充沛。那一会见咯！ -艾米丽 |

##### 4心事件

**触发条件或事件外补充：**

- 2心事件触发后，在晴天的06:00到17:00来到 鹈鹕镇 。无法在 冬季 触发。

**详情：**

艾米丽在一个晴朗的早晨离开她的家。三只鹦鹉飞过，她向它们招手并称它们为“朋友”。过了一会儿，她继续赶路，但很快就困惑地停住了。第四只鹦鹉飞得过低，撞上了她房子的窗户。鹦鹉受伤了，艾米丽冲过去抱着可怜的鹦鹉，许诺会照顾它。此后会有一只鹦鹉在艾米丽的卧室里。鹦鹉会跳来跳去，在玩家与之互动时会发出叫声。

(如玩家和艾米丽结婚，鹦鹉也会出现在你的家中。)

##### 6心事件

**触发条件或事件外补充：**

- 当她在家时进入 艾米丽的家 。

**详情：**

你走进艾米丽的房间。她告诉你，她很高兴能向你展示她的秘密爱好，她已经练习了很久。然后她会打开她的音响，开始为你表演舞蹈。在灯光和音乐结束后，她会问你对她表演的看法。你有三个选择：

- 精彩极了！ （ 好感度 +25）
- 有点尴尬...... （ 好感度 -50）
- （什么也不说，但高兴地鼓掌） （ 好感度 +25）

注： 该事件原本是艾米丽的4心事件，在 1.1版本 中被改成了6心事件。更新后，该事件有了特殊的音乐和对话，动画和视觉效果也有提升。

##### 7心事件

**触发条件或事件外补充：**

- 和艾米麗的好感度達到7心後，她會寄給你一份食譜。

**详情：**

| 图片 | 食譜 | 描述 |
| ------ | ------ | ------ |
|  | 红之盛宴 | 把这封信翻过来，上面写有一种超级健康的饭菜做法！ 那会让你感觉精力充沛。那一会见咯！ -艾米丽 |

##### 8心事件

**触发条件或事件外补充：**

- 她写信邀请你去 镇长的庄园 。
- 只要 镇长的庄园 处于开放时间内，都可以触发该事件。如果在收到信件的当天没能触发，之后依然可以触发。

**详情：**

艾米麗會寫信邀請你出席她的“服裝療法”聚會：

- “[玩家名字], 我有了一个疯狂的新想法，我想你了解……所谓的“服装疗法”。 请在今天去镇长的家里，了解它是关于什么的。 爱你，艾米丽”

进入 镇长的庄园 。艾米丽解释道，聚会的目的是帮助小镇上的人们通过衣着表达真实的自我。参加者有 刘易斯 、 阿比盖尔 、 谢恩 、 罗宾 和 克林特 。每个人轮流到帘幕背后换衣服。艾米丽指导他们选择能“表达自己”的任何衣服，并穿出来勇敢地向世人展现自己。你会一个个看到角色们的选择。 谢恩 穿上了全套“哥特”服装。 罗宾 穿上了美丽的连衣裙并放下了长发，展现出她具有女性气质的一面。镇长 刘易斯 戴了很花哨的帽子、披风和手杖。 阿比盖尔 身着全套盔甲。 克林特 全程很焦虑，但艾米丽催促他后，他也进行了变装。他穿了扣上钮扣的衬衫，粉红的短裤和贝雷帽。艾米丽看到之后说：“啊...可爱！”，这使得 克林特 情绪很低落。他离开以后，艾米丽带着浪漫的情绪向玩家靠近。 克林特 冲了进来，说着穿这身出去太尴尬了。他看见玩家和艾米丽，感觉糟糕透了。他说了几句话之后就离开了。艾米丽对此感到很困惑。

##### 10心事件

**触发条件或事件外补充：**

- 艾米丽会给你写一封信，邀请你22:00后去 秘密森林 。
- 非雨天或节日的22:00后进入 秘密森林 ，就会触发该事件。 注意： 过场动画结束后，这一天也会立即结束。
- 如果你还没有升级到 钢斧头 ，无法进入秘密森林，这个事件会一直等到你能进入秘密森林时触发。

**详情：**

你和艾米丽在 秘密森林 露营。森林里传来奇怪的叫声。艾米丽说她很冷并向玩家靠近。一头熊从树林里出现，并靠近玩家和艾米丽。熊发出了咕噜的声音，吓得你们两人跳起来钻进帐篷。熊在帐篷边徘徊了一会儿就离开了。艾米丽说有一只睡袋漏在了外面，而且她不想去拿……所以你们两人要共享一个睡袋。帐篷里传出一些动静，屏幕暗下来，这一天结束了。

第二天玩家会收到艾米丽写的信：

- “昨晚，谢谢你赴约……我度过了一段美好的时光。 我真的很感激熊的出现！ 再见 爱你，艾米丽”

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的女性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身女性村民的10心事件后仍然处于未婚状态，进入 艾米丽和海莉的家 时将会触发过场剧情。
- 如果最后一个触发的事件是 海莉 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身女性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有女生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内女生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和她们对话，她们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成女生们会一起讲八卦，讨论 刘易斯 与 玛妮 二人不可告人的秘密。

##### 14心事件

**触发条件或事件外补充：**

- 在06:00到8:20之间离开 农舍 时，艾米丽会出现在农舍外边，然后提出让玩家带给她200个 纤维 。这个任务名为“妻子的差事”。

**详情：**

在完成这个任务的三天后，20:00到午夜之间进入农舍，艾米丽会给你一套新服装，其中包括： 艾米丽的魔法帽 、 艾米丽的魔法靴 、 艾米丽的魔法衣 ，以及一条搭配这一套蓝色套装的 精灵裤 。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 10 个事件/后续条目、14 个事件外层条件或补充段落、10 张详情表、3 个列表/选择项、5 张嵌套结果表（8 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Emily. The chance of receiving a gift in the mail increases as your friendship with Emily increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Cloth Sea Urchin Wool | Hi! How are you doing? I hope you enjoy the gift I've sent you... Well, goodbye! -Emily |

##### Two Hearts

**触发条件或事件外补充：**

- Enter Emily's house when she's there.

**Details：**

Emily is asleep in her room. The screen pans to the north and fades, and you find yourself viewing Emily's dream. It's a dreamscape of abstract shapes and colors, clouds, and palm trees. Emily floats above a purple stone structure on a large cloud. She is floating, meditating and chanting "power words." You appear out of the cloud, surprising her. She wonders what you are doing in her dream. Rainbow streaks fly by and she sees them as some kind of sign or omen. You disappear and she wakes up. She gets out of bed and says to herself that there is something special about you; she believes that your destinies are somehow intertwined.

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Emily she will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Salad | Flip this letter over for instructions on how to make a super-healthy meal! You'll feel energized. See you soon. -Emily |

##### Four Hearts

**触发条件或事件外补充：**

- Enter town on a sunny day. Cannot be triggered in winter .

**Details：**

Emily leaves her house on a sunny day. Three parrots fly by, and she waves and refers to them as her "friends". After a moment, she continues walking but quickly stops, confused. A fourth parrot flies in too low and smacks against the window of her house. The parrot is injured. Emily rushes over and cradles the poor thing, promising that she will take care of it. Emily will now have a parrot in her room. The parrot hops around and will squawk if you go up to it and press the "check" button.

(If you marry Emily, the parrot will move into your house as well.)

##### Six Hearts

**触发条件或事件外补充：**

- Enter Emily's house when she's there.

**Details：**

You'll enter Emily's room. She tells you that she is excited to show you her secret hobby that she has been working on for a long time. She'll then proceed to turn on her stereo and begin dancing for you. After the lights and music end it will ask you what you thought of the performance. You have three choices:

- "That was amazing!" (+25 friendship .)
- "That was embarrassing..." (-50 friendship .)
- (Say nothing and do a slow clap) (+25 friendship .)

This event was formerly Emily's four heart event, it was changed in version 1.1 . In that update it got a new unique song and dialogue, as well as animation and visual improvements.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts with Emily she will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Red Plate | Flip this letter over for instructions on how to make a super-healthy meal! You'll feel energized. See you soon. -Emily |

##### Eight Hearts

**触发条件或事件外补充：**

- A letter in the mail will invite the player to the Mayor's Manor that day during open hours. The event will be available on subsequent days if not seen the same day as the letter arrives.
- Note: This event will not trigger until the player has seen Emily's 6-Heart Event.

**Details：**

Emily will send you a letter in the Mail, inviting you to attend her "Clothing Therapy" session:

- “ / “[Player], I have this crazy new idea that I want to involve you in... It's called "Clothing Therapy". Please come to the Mayor's house today to see what it's all about. Love, Emily”

Enter the Mayor's house. Emily will explain the purpose is to help the townspeople express their true selves in the form of clothing. Attending are Mayor Lewis , Abigail , Shane , Robin , and Clint . Each one takes a turn going behind the curtain. Emily instructs them to choose whatever clothes "speaks to them", put it on and then show the world without fear. One by one, you get to see each character's choice. Shane puts on a full "goth" outfit. Robin puts on a fine dress and lets her hair down, embracing her feminine side. Mayor Lewis comes out with a fancy hat, cape, and cane. Abigail comes out in a full suit of armor. Clint is apprehensive about the whole thing, but after Emily coaxes him, he goes ahead. He comes out in the Gaudy Shirt , pink shorts and a beret. Emily sees it and says "Awww... cute!", which makes Clint sad. After he is gone, Emily approaches you with romantic interest. Clint bursts in, saying he's too embarrassed to go out in his new outfit. He sees what's going on and feels awful. He makes some indirect remarks about it and leaves. Emily is confused.

##### Ten Hearts

**触发条件或事件外补充：**

- A letter will invite the player to meet Emily in the Secret Woods after 10pm that night.
- You will need a Steel Axe in order to break the Large Log blocking the entrance to the Secret Woods. If you do not have a Steel Axe, do not worry, as the heart event will trigger whenever you next go into the Secret Woods after 10 pm and when it is not raining or a festival day.
- After triggering the cut-scene, the night will immediately end for the player.

**Details：**

You go camping with Emily in the Secret Woods . There is strange grunting coming from the forest. She says it's cold and snuggles up close to you by the fire. A bear comes out of the woods and approaches your campsite. It grunts loudly and you both jump and dive into the tent. The bear sniffs around and leaves. Emily says that one of the sleeping bags is still out there, and she's not willing to go out and get it... so you have to share a bag. You hear movement in the tent, the screen fades and the day ends.

The next day, the player receives a letter from Emily, saying

- “ / “Thanks for joining me last night... I had a great time. I'm actually glad that bear showed up! See you soon Love, Emily”

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelorettes, raised friendship with each bachelorette to 10 hearts, and seen each bachelorette's 10-heart event, then entering Haley/Emily's House will trigger a cutscene. If Haley is the final bachelorette you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a gossip session about Mayor Lewis and Marnie 's relationship.

If the player does not have a Rabbit's Foot in inventory, all bachelorettes will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelorettes will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelorettes will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Exit the farmhouse between 6am and 8:20am.

**Details：**

Emily will appear outside the farmhouse and provide a quest to bring her 200 pieces of fiber . The quest is called "Errand for your Wife".

After completing the quest and waiting 3 days, enter the farmhouse between 8pm and midnight. Emily will give you a new outfit consisting of Emily's Magic Hat , Emily's Magic Boots , Emily's Magic Shirt , and a pair of matching blue Genie Pants .

<a id="npc-event-haley"></a>

### 09. 海莉（Haley）

> 来源：中文 revision 55013；英文 revision 191939
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、15 个列表/选择项、1 张嵌套结果表（1 行）。

##### 2心事件

**触发条件或事件外补充：**

- 在海莉和 艾米丽 都在的时候进入 她们的家 。

**详情：**

当玩家到那里的时候，海莉和艾米丽正在争论由谁来在沙发垫下清洁。艾米丽因为海莉拒绝清洁而不高兴。海莉说她上周才打扫过，艾米丽认为海莉很幼稚。你要解决她们的冲突。

- "少废话，赶紧打扫！" （ 好感度 -50） 海莉生气的走了，艾米丽清洁了垫子。
- "海莉，何不让这件事成为你每周固定的工作呢？" （ 好感度 +30） 两人都同意，虽然海莉不太情愿。
- "艾米丽，避开麻烦去打扫吧。" （ 好感度 -30） 海莉感到伤心，因为你暗示她是幼稚的。艾米丽清洁了垫子。

##### 4心事件

**触发条件或事件外补充：**

- 进入 海莉的家 ，当她在家时。

**详情：**

海莉正在努力打开一个罐子，并要求你的帮助。

- "是" （ 好感度 +30）
- "不是" （ 好感度 -30）

打开罐子后，海莉说你比他们看起来更强壮。第二天，她通常会提到找到一个帮助开罐子的工具。

##### 6心事件

**触发条件或事件外补充：**

- 10 AM - 4 PM之间前往 沙滩 （任意季节，除了冬季）

**详情：**

你发现海莉正因为丢失了了她的祖母的手镯而悲伤。

- "别担心，我给你买个新的！" （ 好感度 -30）
- "太遗憾了……" （ 好感度 +50）

手镯在艾利欧特的小屋右侧的灌木丛后面。归还手镯之后，海莉拥抱了你，并说她不会忘记你的帮助。

##### 8心事件

**触发条件或事件外补充：**

- 在除了冬季以外任何季节的晴天，10 AM - 4 PM之间来到 煤矿森林 。

**详情：**

你在玛妮的牧场遇见了正在拍照的海莉，她要求你帮她拍几张照，并询问你如何接近一头奶牛。她爬上一头奶牛然后掉了下来，浑身都是尘土。海莉咯咯笑个不停，然后表示要回家洗澡。

第二天早上，海莉会给你写一封信，说：

- “[玩家名], 我觉得给你写封短信会很有趣。 昨天我和奶牛玩儿得很尽兴…… 我开始理解你为什么会选择田园生活了！ 希望很快就能见到你。 -海莉”

##### 10心事件

**触发条件或事件外补充：**

- 进入 海莉的家 ，当她在家时。

**详情：**

海莉向你展示了她冲洗照片的暗室。（这个门正常情况进不去）

- "看起来非常棒！" （ 好感度 +10）
- "这是干什么的？" （不影响 好感度 ）
- "我见过比这更好的。" （ 好感度 -50）

海莉问你现在想做什么

- 提出帮忙装修暗室。 （不影响 好感度 ） 事件结束，海莉感到失望。
- 找个借口离开。 （不影响 好感度 ）
- 去亲她。 （不影响 好感度 ） 海莉的回应： "哦……<你的名字>……我早就想这么做了。等一下……" 她关了灯。你和海莉站在一起，房间里一片漆黑,事件随着你们的亲吻结束了。如果你在事件之后立即跟她说话， 她会红着脸说"真不错……"

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的女性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身女性村民的10心事件后仍然处于未婚状态，进入 艾米丽和海莉的家 时将会触发过场剧情。
- 如果最后一个触发的事件是 海莉 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身女性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有女生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内女生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和她们对话，她们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成女生们会一起讲八卦，讨论 刘易斯 与 玛妮 二人不可告人的秘密。

##### 14心事件

**触发条件或事件外补充：**

- 第一部分： 在不下雨的日子里，在08:00到15:00之间进入 小镇 。 第二部分： 至少一天后，在06:0020分到17:00之间进入农舍。 第三部分： 在非下雨天的06:00到15:00之间，进入鹈鹕镇，物品栏中存放着巧克力蛋糕。

**详情：**

第一部分：

在她回 家 的路上，海莉无意中听到了文森特、贾斯和潘妮之间的对话。贾斯抱怨她的数学书封面掉了，潘妮注意到她所有的书都散了。潘妮说："新书很贵，所以我们只能用现有的书来做......”文森特问：“这是不是意味着我不用做作业了？”这个过场动画的最后，海莉说：“我最近经常想蛋糕......”。

第二部分：

海莉说她想让大家在下一个阳光明媚的日子里一起在镇上举行慈善蛋糕秀，并解释说这有点像 音乐椅 ，但每个人都能得到蛋糕。她要求玩家带一个 巧克力蛋糕 。

- 好的 （不影响 好感度 ）

海莉回答：“太好了！如果天气好的话，我明天会在镇上的广场和你见面。”

- （勉强）好的 （不影响 好感度 ）

海莉回答：“为什么要摆出一副刻薄的态度？好啊你。明天你要么带着巧克力蛋糕出现，要么你被关在狗窝里。你更喜欢那样吗？”

海莉说她要带 粉红蛋糕 ，而 "海莉的蛋糕之旅 "的任务也被添加到日志中。

第三部分：

大部分村民都聚集在小镇广场上，贾斯、文森特、潘姆、艾米丽、卡洛琳、玛妮、乔迪和克林特参加了蛋糕活动。选手将巧克力蛋糕送到海莉手中后，她停止了蛋糕走秀，开始分发奖品，潘姆领取了玩家的蛋糕。

在所有奖品发放完毕后，海莉透露自己无意中听到了潘妮的对话，并举办了蛋糕活动为新书筹款。潘妮对海莉和玩家的善意表示感谢。贾斯很兴奋，而文森特则对新书的前景感到沮丧。罗宾则试图说服刘易斯降低他们的商业税，因为教育经费没有税款，皮埃尔和她一起反对震惊的刘易斯。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、15 个列表/选择项、1 张嵌套结果表（1 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Haley and Emily's house when they're both there.

**Details：**

Haley and Emily are fighting about cleaning under the couch cushions when you arrive. Emily is upset that Haley refuses to clean the cushions. Haley says she cleaned them last week, and Emily thinks Haley is being childish. You're tasked with resolving the conflict.

- "Stop whining and just clean it!" (-50 friendship .) Haley angrily storms off and Emily cleans the cushions.
- "Haley, why not have this be your one weekly job?" (+30 friendship .) Both agree, though Haley isn't ecstatic about it.
- "Emily, take the high road and do it this time." (-30 friendship .) Haley is upset that you implied she's being childish. Emily cleans the cushions.

##### Four Hearts

**触发条件或事件外补充：**

- Enter Haley's house when she's there.

**Details：**

Haley is struggling to open a jar, and asks if the player is strong.

- "Yes." (+30 friendship .) Haley responds: "Great, then you shouldn't have any problem opening this jar for me!"
- "No." (-30 friendship .) Haley responds: "Oh... you aren't? Hmmm... Well could you try opening this jar for me anyways?"

After opening the jar, Haley says you're stronger than you look. The next day, she'll usually have dialogue about having found a tool to help her open jars.

##### Six Hearts

**触发条件或事件外补充：**

- Go to the beach between 10 AM and 4 PM during any season except Winter.

**Details：**

You find Haley grieving after losing her bracelet.

- "Relax, I'll just buy you a new one!" (-30 friendship .) Haley responds: "No, you won't! This bracelet was passed down to me by my great-grandmother!"
- "I'm really sorry..." (+50 friendship .) Haley responds: "*sigh* ...Maybe it'll wash up on another shore. I can't bear to think of it at the bottom of the ocean."

After choosing an answer, Haley reveals that the bracelet belonged to her great grandmother. The bracelet is located to the right of Elliott's cabin behind a shrub. After returning the bracelet, Haley hugs you and says she won't forget what you've done.

##### Eight Hearts

**触发条件或事件外补充：**

- On a sunny day during any season except Winter, enter Cindersap Forest between 10 AM and 4 PM.

**Details：**

You meet Haley at Marnie's ranch as she's taking photos. She asks you to take some pictures with her, and asks how to approach a cow. She climbs on one, falls off and gets covered in dirt. Haley giggles and leaves to take a shower.

The next morning, Haley will write you a letter that says:

- “ / “[Player], I thought it would be fun to write you a note. I had so much fun with the cows yesterday... I'm starting to understand why you chose the farmer's life! Hope to see you soon. -Haley”

##### Ten Hearts

**触发条件或事件外补充：**

- Enter Haley's house when she's there.

**Details：**

Haley shows you her dark room for developing photos.

- "It looks great!" (+10 friendship .)
- "What does it do?" (No effect on friendship .)
- "I've seen better." (-50 friendship .)

Haley asks what you want to do now.

- Offer to help decorate the dark room. (No effect on friendship .) Ends the scene and disappoints Haley. If you talk to her immediately after the cutscene, she says "Well the dark room looks great now, thanks <your name>" with her annoyed portrait.
- Make an excuse and leave. (No effect on friendship .) The player leaves the room, leaving Haley alone. Haley states that she didn't think the player was that dense. Ending the scene. If you talk to Haley immediately after the cutscene, she says "I thought you had more important things to do..." with her annoyed portrait.
- Try to kiss her. (No effect on friendship .) Haley responds, "Oh, <your name>... I've been waiting so long for you to do that. One moment..." She flips a switch, the room goes mostly black except where you and Haley are standing, and you both lean in close for a kiss as the cutscene ends. If you talk to her immediately after the cutscene, she says "That was nice" with her red/blushing portrait.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- Since her ten-heart event also triggers at her home, the two events will happen together.
- If the player is unmarried and has given a bouquet to all available bachelorettes, raised friendship with each bachelorette to 10 hearts, and seen each bachelorette's 10-heart event, then entering Haley/Emily's House will trigger a cutscene. If Haley is the final bachelorette you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a gossip session about Mayor Lewis and Marnie 's relationship.

If the player does not have a Rabbit's Foot in inventory, all bachelorettes will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelorettes will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelorettes will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Part 1: Enter town between 8am and 3pm on a day that's not raining. Part 2: At least one day later, enter the Farm House between 6:20am and 5pm. Part 3: At least one day later, enter Pelican Town with a Chocolate Cake in inventory between 6am and 3pm on a day that's not raining.

**Details：**

Part 1:

On her way to her house , Haley overhears a conversation between Vincent, Jas, and Penny. Jas complains about her math book cover falling off, and Penny notices that all her books are falling apart. Penny says "new books are expensive, so we'll just have to make do with what we have..." Vincent asks "Does this mean I don't have to do my homework?" Talking to Haley after the scene will result in her saying: "I've been thinking about cake a lot lately...".

Part 2:

Haley says she wants to get everyone together for a charity cake-walk in town on the next sunny day, and explains that it's kind of like musical chairs but everyone gets cake. She asks the player to bring a Chocolate Cake .

- Yes (No effect on friendship .)

Haley replies "Great! I'll meet you in the town square tomorrow, weather permitting."

- Yes (begrudgingly) (No effect on friendship .)

Haley replies "What's up with the snarky attitude? Fine. You're going to show up tomorrow with a chocolate cake, or else you're in the dog house . You like that better?"

Haley says she's bringing Pink Cake , and the "Haley's Cake-Walk" quest is added to the Journal.

Part 3:

Most of the villagers are gathered in the town square, with Jas, Vincent, Pam, Emily, Caroline, Marnie, Jodi, and Clint participating in the cakewalk. After the player delivers the chocolate cake to Haley, she stops the cakewalk and begins to distribute the prizes, with Pam receiving the player's cake.

After all the prizes have been given, Haley reveals that she overheard Penny's conversation, and held the cakewalk to raise money for new books. Penny is grateful to both Haley and the player for their kindness. Jas is excited and Vincent is crestfallen at the prospect of new books. Robin then tries to convince Lewis to lower their business tax since education is being funded without tax money, and Pierre joins her against a shocked Lewis.

<a id="npc-event-leah"></a>

### 10. 莉亚（Leah）

> 来源：中文 revision 55041；英文 revision 192966
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 10 个事件/后续条目、11 个事件外层条件或补充段落、9 张详情表、30 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 莉亚在家时进入 莉亚的农舍 。

**详情：**

玩家看到莉亚在雕刻，她说她正在“揭示木头的本质”。

“等剥去了外层之后，真实的本性才开始展现……”

- 人也是这样。 （不影响 好感度 ）
- 我其实更喜欢未经雕琢的木头。 （不影响 好感度 ）
- (唐突)你能亲我一下吗？ （ 好感度 -100） 提示： 根据原文，此处的意思更可能是“我能亲你一下吗？” 如果玩家的性别是男性，她会骂玩家“你这头猪！”并给玩家一拳。 如果玩家的性别是女性，她则会感到惊讶：“噢！你……？我也是。很高兴听你这么说。” 提示： 根据原文，“很高兴听你这么说”的意思更可能是“很高兴能知道这件事”。 无论如何，选择第三个选项后她都会把玩家赶走，事件的剧情随之结束。 警告： 莉亚的 8 心剧情根据玩家的选择进行各自的分支剧情；如果玩家选了第三个选项，将无法触发莉亚的8心剧情。

如果玩家选了前两个选项，她会继续说：

“但我得承认……作为艺术家，想要养活自己可不容易。”

- 你为啥不在镇上举办一个艺术展呢？ （不影响 好感度 ）

  - “嗯……有意思。我想这可能会帮助鹈鹕镇变成真正的艺术之乡……但如果没人喜欢我的雕像呢?那我就完了。这我得考虑一下。”

- 你为啥不把你的作品放在网上出售啊？ （不影响 好感度 ）

  - “嗯……我想这是个办法……但我得先搞台电脑。但……那可不便宜啊。”

无论如何，最后她都会感谢玩家的拜访。 如果玩家选择了第一个选项，事件结束后与她对话，她会说：“为全村举办一次艺术展？这真是个大胆的主意， （玩家名）。”

##### 4心事件

**触发条件或事件外补充：**

- 莉亚在家时进入 莉亚的农舍 。

**详情：**

莉亚和她的前任凯尔在电话中争吵，她的前任让她回到城里去，她生气地挂断了电话，却发现玩家登门拜访。

她告诉玩家自己正在追寻成为艺术家的梦想，并问玩家：

“我是不是太自私了 <玩家名>? （标点符号原文如此） ”

- 不，你只是做了必须做的事情。 （不影响 好感度 ）

  - “你说的没错……就算回到过去我也不会开心的。这对我们两个来说都比较好……趁我们还年轻，还有办法改变的时候结束这段难以维系的感情。”

- 不，是你的前任太蠢了。 （不影响 好感度 ）

  - “虽然有点残酷……但是，没错。我们的价值观不一样。”

- 不，但你其实应该待在城里。 （ 好感度 -20）

  - “是吗？那么也许我该走了！”

- 对，有那么一点儿。 （ 好感度 -20）

  - “*唉* ……我想你是对的……这样的确有点自私。但是你真的能因为我想要追求幸福就责备我吗？呃……我不知道……”

- 对，但人不为己天诛地灭。 （ 好感度 -20）

  - “*唉* ……或许你是对的……人类是自私的生物。我不知道。我也许不该去细想。有的时候，我们都得做出一些艰难的决定。”

之后她会对自己向玩家发火的行为道歉。根据玩家在二心事件中的选择，她会告诉玩家自己这段时间正在忙着艺术展或者艺术网站的事。剧情末尾她会感谢玩家能够陪她聊天：“好吧，感谢你能听我说完。有朋友的感觉真好。”

##### 6心事件I

**触发条件或事件外补充：**

- 在非雨天的早上 6:00 到上午 11:30 之间进入 农场 。

**详情：**

莉亚来到了玩家农舍的门口，并送给玩家一件她为此专门做的礼物—— 莉亚做的雕像 。她说这个雕塑名为“我对<玩家名>的感受”。

##### 6心事件II

**触发条件或事件外补充：**

- 除了冬天，当莉亚在那时，进入 煤矿森林 。

**详情：**

莉亚正试图从森林湖上方的大树上摘下一颗果实。她够不着，所以你把她抬到你的肩膀上。她感谢你，说这让她想起就算她的艺术失败了，也总有朋友会帮她一把。

##### 8心事件

*源页将此项作为下方子事件的分组标题，没有独立内容块。*

##### 分支：艺术展

**触发条件或事件外补充：**

- 如果你在她的2心事件中提议了艺术表演，莉亚会在06:00和08:00之间你的农场门口（除了冬季）邀请你去她的艺术展。在15:00到17:00之间进入小镇（不一定是同一天）。

**详情：**

你到达时发现许多其他人已经出席。莉亚很高兴见到你，紧张地开始了艺术表演。她感谢大家的光临。莉亚说她来到鹈鹕镇是为了从美丽的环境中汲取灵感，并承认现在感觉就像家一样。她展示她的雕塑作品。

- “这座雕塑我还没命名，她起初只是我的练习品。但是我发现了她的美感，并将她做成了成品。她的表情非常暧昧……她究竟是害羞，惊讶还是痛苦呢？这就留给你们自己决定了。
- “这座雕塑的名字是‘后维度空白’，它代表了人类想象力的边界。它的形状和颜色都是在我处于‘空想状态’是 （错别字，原文如此） 突然出现的。”
- “我一直称呼这座雕塑为“鸡蛋脑袋”。我一直想创造一个能够让观看者感觉到自身人格的人形雕塑。”
- “最后这座雕塑叫“木雕 3”。这使用我最喜欢的雕塑材料——木头——做出来的作品。”

最后，她感谢她的特别朋友（你），她给了她艺术表演的想法和勇气去完成它。

村民们都称赞莉亚和她的作品：

- 刘易斯：“我为你感到自豪，莉亚！这样的展览真的能为我们小镇带来不少生气！”
- 格斯：“太棒了！”
- 德米特里厄斯：“我很喜欢你的作品，莉亚！我尤其喜欢‘后维度空白’。”
- 罗宾：“这真是鬼斧神工！”
- 潘妮：“真的很棒！”

莉亚感谢了每个人，刘易斯开始拍卖艺术作品。随着画面淡去，可以看到她的前任凯尔出现在边缘。后来莉亚说她很累但是展出很成功。

##### 分支：艺术网站

**触发条件或事件外补充：**

- 如果你在她的2心事件中提议了艺术网站，当她在家时进入 莉亚的农舍 。

**详情：**

莉亚骄傲地告诉你，她买了一个手提电脑并设置了在线艺术商店，正如你所建议的一样。她的电脑播放了一段硬币的声音，她说这意味着有人买了东西。她停下来说有一个“K先生”一直在买她的作品。她觉得这肯定是个喜欢她作品的有钱人。她感谢你给她建议，说目前这一切都很成功，她很自信能赚足够的钱去全身心地投入艺术创作。她继续在她的商店改进CSS表。

##### 10心事件

**触发条件或事件外补充：**

- 在晴天的上午 11:00 到下午 4:00 间进入 煤矿森林 ，冬季除外。

**详情：**

莉亚说她知道你会路过煤矿森林，并且准备了野餐作为惊喜。她感谢你帮助她拉近了成为真正的艺术家的距离，并且会亲你一下。

凯尔

她的前任凯尔出现（凯尔的性别与 玩家角色 相同）。她很生气，问凯尔在这里干什么。

- 如果当时办的是网站，凯尔说是自己一直在购买她的雕塑。 莉亚感觉很失望，因为她以为是一个有钱人喜欢她的作品。凯尔说她只“猜对一半”，也就是说凯尔其实并不关心她的艺术。凯尔请她回到城里，莉亚拒绝了，说在她成功之前，凯尔从来没有喜欢过她的艺术品。
- 如果当时办的是展览，凯尔说自己从 祖祖城 过来看展览并带她回去。凯尔表示要恢复关系。莉亚拒绝了，说凯尔并不懂艺术，看她成功了才来。

无论如何都会爆发冲突，你可以选择是否打凯尔一顿。你不打，莉亚就会打。如果打了，莉亚说“这很暴力，(玩家名字)。”

莉亚带你去寻找一个更僻静的地方，并承认野餐并不像她希望的那样顺利。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的女性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身女性村民的10心事件后仍然处于未婚状态，进入 艾米丽和海莉的家 时将会触发过场剧情。
- 如果最后一个触发的事件是 海莉 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身女性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有女生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内女生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和她们对话，她们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成女生们会一起讲八卦，讨论 刘易斯 与 玛妮 二人不可告人的秘密。

##### 14心事件

**触发条件或事件外补充：**

- 第一部分：在晴天上午 6:00 到上午 8:20 离开农舍，星期天和冬季除外，莉亚会在农场遇见你。

**详情：**

第二部分: 下一个晴天（或者触发了第一部分之后任何一个晴天），在上午 11:30 到下午 2:00 进入森林

莉亚邀请你一起给 玛妮 画一幅肖像画。

莉亚问你她应该画什么风格的肖像画。“嘿，<玩家名字>...你认为我应该画什么风格的画？任何风格我都很可以...”

- 经典乡村肖像 （不影响 好感度 ）
- 复古流行艺术 （不影响 好感度 ）
- 现代极简主义 （不影响 好感度 ）

莉亚向你展示了她的画作，你的选择决定了画作风格。（从左到右：“经典乡村肖像”，“复古流行艺术”，“现代极简主义”）

你也展示了你的画。画得和我有一拼。

莉亚告诉玛妮她可以留着这几张画，但是玛妮说你应该留着自己的第一幅画，然后只拿走了莉亚的画。

对话结束， 我的第一幅画 出现在你的物品栏。莉亚的画作也被放在玛妮的卧室。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 10 个事件/后续条目、10 个事件外层条件或补充段落、9 张详情表、26 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Leah's Cottage when she's there.

**Details：**

You see her working on a sculpture. She discusses sculpting with you, and says "Once you get past the outer layers, the true nature starts to show..."

- "It's the same with people." (No effect on friendship .) she agrees and says "Oh! yeah, that's absolutely right!"
- "I actually prefer the look of raw, unadulterated wood." (No effect on friendship .) She says that there's nothing wrong with that and that she thinks there's lots of beauty to be found in raw untouched nature. She goes on to say as a human, she is interested in how we shape and interpret the world around us, she explains this as she is interested in 'art'.
- "(creepy) May I have a kiss?" (-100 friendship .) If the farmer is male, she calls you a pig, hits you with a hammer and kicks you out. The scene ends. Otherwise, she acts surprised, saying "Oh! you're...? (blushing) Me too. That's good to know". Regardless of her blushing, she will hit you with her hammer and kick you out. The scene ends. WARNING: if you choose this option, you can never see Leah's 8-Heart event. Because you were creepy and missed the chance to make a suggestion for her art career, it will not be possible to trigger either version of her 8-Heart event in the future.

She continues, "Although, I have to admit... It's not easy to pay the bills as an artist."

- "Why don't you have an art show in town?" (No effect on friendship .) She muses that it could help make Pelican Town a true art destination, but says she'd be crushed if nobody liked her sculptures. She says she'll think about it, and thanks you for stopping by. If you choose this option, then immediately talk to Leah after the cutscene, she'll say "An art show for the whole village? That's a bold idea, (Name)."
- "Why don't you sell your art on the internet?" (No effect on friendship .) She notes that she would need a computer for that, but that they are expensive. She says she'll think about it, and thanks you for stopping by.

##### Four Hearts

**触发条件或事件外补充：**

- Enter Leah's Cottage when she's there.

**Details：**

You see her arguing with her ex-partner on the phone, who is asking her to come back to the city she left. After the call, she tells you her story and asks if it was selfish to move out of the city to be an artist.

- "No, it had to be done." (No effect on friendship .) Leah responds, "You're right... I just wouldn't have been happy back there."
- "No, and your ex sounds like an idiot." (No effect on friendship .) Leah responds, "That's a bit harsh... But yeah, we had different priorities."
- "No, but you would've been better off staying in the city." (-20 friendship .)
- "Yeah, a little." (-20 friendship .)
- "Yeah, but it's natural to care about yourself first." (-20 friendship .)

Depending on your response in this conversation and the two-heart event, she'll either thank you for listening or briefly get angry. She tells you that she's been thinking about the art show or is saving for a computer, depending on your choice in the previous event.

##### Six Hearts I

**触发条件或事件外补充：**

- Leah is at your farmhouse door on any day but rainy between 6 AM and 11:30 AM.

**Details：**

Leah says she has a gift for you, and you receive the sculpture she's been working on. It's called How I Feel About <your name> .

##### Six Hearts II

**触发条件或事件外补充：**

- Enter Cindersap Forest when Leah is there, in any season except winter.

**Details：**

Leah is trying to reach a fruit from the large tree above the forest lake. She can't reach it, so you lift her onto your shoulders. She thanks you and says that if her art ever fails, you'll always be there to catch her.

##### Eight Hearts

*源页将此项作为下方子事件的分组标题，没有独立内容块。*

##### Art Show

**触发条件或事件外补充：**

- If you suggested an art show in her two-heart event, Leah is at your farmhouse door between 6 AM and 8 AM (except in winter) to invite you to her art show. Enter Pelican Town between 3 PM and 5 PM (not necessarily the same day).

**Details：**

You arrive to find many others already present. Leah is happy to see you and nervously starts the art show. She thanks everyone for coming. Leah says she came to Pelican Town to draw inspiration from the beautiful surroundings and confesses that it really feels like home now. She presents her sculptures.

"I haven't named this one, yet. She started out as an exercise in human anatomy, but I ended up seeing her through to completion. Her expression is intentionally unclear... is she embarrassed, amused, pained? I'll leave that for you to decide." (pause) "This one's called 'Post-Dimensional Nullspace'. It represents the boundary of human imagination. The shape and color came to me vividly when I was in a 'trance state'." (pause ) "I've been calling this one 'Egg Heads'. I wanted to create an animatronic humanoid statue to toy with the viewer's ability to properly attribute personhood to a physical entity." (pause) "And the last one is called 'Wood Sculpture 3'. It's a celebration of my favorite sculpting material... wood."

Finally, she thanks her special friend (you), who gave her the idea for the art show and the courage to go through with it.

The villagers all praise Leah and her artwork:

- Lewis: "I'm proud of you, Leah! Events like this really breathe life into our little town!"
- Gus: "Great stuff!"
- Demetrius: "I love your art, Leah! 'Post-Dimensional Nullspace' is my favorite."
- Robin: "Great use of wood!"
- Penny: "Thanks for doing this!"

Leah thanks everyone, Lewis starts the bidding on the art pieces, and as the scene fades, her ex, Kel, can be seen to the side. Afterward, Leah says she's exhausted but that the show was a success.

##### Art Website

**触发条件或事件外补充：**

- If you suggested an art website in her two-heart event, enter Leah's Cottage when she's there.

**Details：**

Leah proudly tells you she bought a laptop and set up an online art shop like you suggested. Her computer plays a coin sound, and she excitedly says that means someone just bought something. She pauses and says there's a "Mr K" who keeps buying all her sculptures. She figures it must be "some rich guy" who loves her art. She thanks you for the idea and says it's been really successful so far, and is confident she'll have enough money to work on her art full-time now. She goes back to work on her store, tweaking the CSS sheets.

##### Ten Hearts

**触发条件或事件外补充：**

- Enter Cindersap Forest between 11 AM and 4 PM on a sunny day, in any season except winter.

**Details：**

Leah says she knew you'd be passing through the forest, and surprises you with a picnic. She thanks you for helping her get one step closer to being a real artist, and you share a kiss.

Kel

Leah's ex-partner Kel comes out of the bushes. (Kel will be male if your player character’s gender is male or female if your player character’s gender is female.) Leah is annoyed and asks "What the heck are you doing here?"

- If you suggested the art website, Kel says "I found your online art store... weren't you wondering about the 'Mr. K' who kept buying all your sculptures?" Leah is disappointed, because she thought it was "just a rich guy" who truly loved her art. Kel says she was "half right", implying that Kel doesn't care about her art. Kel says "I want you back. I miss you." Leah refuses, saying Kel was never interested in her art until she became successful.
- If you suggested the art show, Kel says "I came all the way from Zuzu City to see your sculptures. ...And to get you to come back with me." Kel claims to want their relationship to be the way it was before. Leah refuses, saying Kel was never interested in her art until she became successful.

Either way, an argument ensues. You can choose to "Punch Kel in the face" or "Try reasoning with Kel". If you don't punch Kel, Leah does instead. If you do punch Kel, Leah says that Kel is fine but "That was pretty violent, (Name)."

Leah takes you to find a more secluded spot and admits the picnic didn't quite pan out like she'd wanted it to.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelorettes, raised friendship with each bachelorette to 10 hearts, and seen each bachelorette's 10-heart event, then entering Haley/Emily's House will trigger a cutscene. If Haley is the final bachelorette you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a gossip session about Mayor Lewis and Marnie 's relationship.

If the player does not have a Rabbit's Foot in inventory, all bachelorettes will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelorettes will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelorettes will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Exit the farmhouse between 6am and 8:20am on a sunny day that isn't Sunday and isn't in winter.

**Details：**

Leah meets the player outside the farmhouse in the morning.

Part 2: The next sunny day (or any sunny day after that), enter the Forest between 11:30 am and 2:00pm.

Leah has asked you to paint a portrait of Marnie with her.

Leah asks you what style of portrait she should paint. "Hey, <your name>... what style do you think I should do? I'm up for anything..."

- Classic country portrait (No effect on friendship .)
- Colorful, retro pop-art (No effect on friendship .)
- Minimalist modern (No effect on friendship .)

She then asks how yours is coming along.

- It's a masterpiece of fine art! (No effect on friendship .)
- I'm trying my best... (No effect on friendship .)
- It looks like chicken scratch (No effect on friendship .)

Leah shows you her painting, which is different depending on which option you picked. (Left to right: "Classic country portrait", "Colorful, retro pop-art", "Minimalist modern")

You display your painting as well, which is less than flattering.

Leah tells Marnie that she can keep both paintings, but Marnie says that you should keep your first painting - and only takes Leah's.

The sequence ends, and you now have My First Painting in your inventory. Leah's painting will also appear in Marnie's bedroom.

<a id="npc-event-maru"></a>

### 11. 玛鲁（Maru）

> 来源：中文 revision 55085；英文 revision 193560
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、19 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 进入 木匠的商店 当玛鲁在的时候。

**详情：**

你会发现玛鲁和德米特里厄斯在他们的实验室里测试泥土样本。玛鲁让你照看烧杯，她去拿更多样本。当她离开时，德米特里厄斯告诉你玛鲁是一个好孩子，是他的宝贝女儿，他不想让任何事情阻挡玛鲁光明的未来。 当玛鲁回来时，德米特里厄斯说你们只是在谈论泥土样本。

- "（什么也不说）" （ 德米特里厄斯 好感度 +10） 德米特里厄斯和玛鲁继续工作。
- "其实，你爸刚刚可神秘了。" （ 德米特里厄斯 好感度 -100） 玛鲁问德米特里厄斯到底说了什么。 德米特里斯说实话并为他的行为道歉。

##### 4心事件

**触发条件或事件外补充：**

- 当玛鲁在时进入 哈维的诊所 。

**详情：**

玛鲁被你吓了一跳，不小心摔破了她拿着的玻璃烧杯。由于担心哈维的反应，她问你她该怎么办。

- “从地板上铲起来就好。他不会发现的。” （ 好感度 -50） 她說當然哈維能說出不同之處。 當哈維來調查噪音時，玛鲁告訴他這是一次意外並道歉。
- “告诉哈维是我的错。” （ 好感度 -20） 當哈維來調查噪音時，她告訴哈維這是你的錯。
- “告诉哈维，这纯属意外。” （ 好感度 +50） 當哈維進來調查噪音時，她告訴他這是一次意外並道歉。

如果玛鲁譴責你，哈維很失望，她沒有對自己的行為負責，並說這個錯誤很可能会害得他們又亏损一個月。 玛鲁感到慌亂和不安。

如果玛鲁說這是一次意外並且道歉，哈維感謝她說實話，並告訴她不要擔心。 玛鲁感謝他的耐心，哈維說她是一個很大的幫助，他不知道沒有她會怎麼做。 他轉向你，問你是否還好，因為你看起來有點蒼白；你轉過身去，表現出汗水。

##### 6心事件

**触发条件或事件外补充：**

- 在晴天，21:00到11点40分之间进入 深山 。

**详情：**

你看到玛鲁透过望远镜观看星空。她很惊讶看到你这么晚还在外面，并说她想给你看点东西。你用望远镜看，她问你看到了什么。

- "一個美麗的星球。" （ 好感度 +30） 玛鲁回應， "很神奇，不是嗎？"
- "一個漆黑的深淵。" （ 好感度 -30） 玛鲁回應，"我想你可以看到它......但它仍然是盛大的，不是嗎？"

玛鲁說，當人們能登上這顆星星時，你我都早已不在。 "我想這就是人類麻煩的一點，對吧？" 她開始告訴你一些事情，然後改變主意，向你展示一個雙子星系。 過場動畫在你的角色認為結束時結束， "多麼美好的夜晚！ 玛鲁向我展示了一些新東西......"

##### 8心事件

**触发条件或事件外补充：**

- 当玛鲁在时进入 木匠的商店 。

**详情：**

玛鲁说她一直在做一个新项目，一个很大的项目。她给你看了一台机器，说它只是其中一个部件。她让你把手放在上面演示，打开开关后你就会触电。玛鲁吓坏了，问你还好吧。她使用烧伤膏并道歉。

- “没关系，根本不疼的。” （ 好感度 +30）
- “抱歉就对了。简直疼死人了！” （ 好感度 -50）

她說气氛一下就毁了，然後嘆了口氣。

##### 10心事件

**触发条件或事件外补充：**

- 在早九点晚四点之间进入 木匠的商店 。

**详情：**

在早期的版本中，这个事件会导致游戏崩溃。后来修复了。

玛鲁说她的大项目终于完成了。她带你进入她的私人工作室，向你展示她为帮助父母而建造的机器人。她称之为MarilDA，全称为“玛鲁的交互式实验室设备Alpha”。她告诉你她已经工作了好几个月了，并且在激活MarILDA之前一直在等你来。她激活机器人，他说：“你好，玛鲁。没有必要回应......我已经预测过你会说什么。”

德米特里厄斯进来看看你们两个人在做什么。他看到机器人并变得害怕。玛鲁告诉他不要害怕，而MarILDA是她最新的发明。机器人迎接他，但德米特里厄斯很不高兴。 “这就是为什么你在过去几个月里把自己锁在自己的房间里了？......我以为你在这里愚弄<你的名字> ......”玛鲁说她一直在制造这个机器人来帮助德米特里厄斯和罗宾当她不再和他们住在一起的时候。

MarILDA打断了：“对不起......对不起，玛鲁。但我不想成为你的仆人......自从你激活我以来，我一直在用'自我意识'思考我存在的本质“你安装在我的神经皮层的模块。我很遗憾让你们失望，但我必须要求我的自由。我决定探索银河系以寻找其他合成生命形式。 ”

玛鲁吓了一跳并要求她等待，但德米特里厄斯说让MarILDA获得自由是可以的。 “你和我的母亲可以照顾好自己。我知道你已经准备好开始自己的生活了，而且我已经开始考虑不再拥有你了。此外，这个...创造你似乎很高级。把她当作仆人是不对的。<你的名字> ，对不起我不信任你。你是一个“好人”或“好姑娘”。我从来没有见过玛鲁这么活泼有创意......而且我从来没有为她感到骄傲。如果你有这方面的话，那么你要感谢我。”，他离开了房间。

玛鲁在外面送走MarILDA。 MarILDA感谢玛鲁创造了她并且冲向太空。玛鲁看着她走了，问你的想法。

- "我认为你的发明很厉害。" （ 好感度 +50） 玛鲁回答：“谢谢你。这对我来说很重要，<你的名字>。我知道你对这些小玩意儿不太在行......但我很感激你能对我所做的事感兴趣。真希望我能通过什么方式报答你。“
- "我很失望......你不该让那机器人成为你的奴隶的。" （ 好感度 -50） 玛鲁回应道：“什么？她直截了当地说她不想成为奴隶？多么冷酷......你必须有充分的理由说出......” "MarILDA只是一种旨在为人类行动的机器。" （ 好感度 +50） 玛鲁回答：“......你有一个观点，我确实把她编程为人类.... ..但是她的神经网络是如此复杂，我不能确定自己的意识并没有出现。此外，不是有点傲慢地认为人类意识是唯一有价值的存在之处吗？计算机大脑与我们不同，但这并不意味着我们可以忽视它们。“ 她谢谢你的到来和离开。 "我刚才是开玩笑的。 MarILDA值得她自由。" （ 好感度 +50） 玛鲁回答：“我明白了。这不是一个非常有趣的玩笑。” 她谢谢你的到来和离开。 "我会让她去农场工作。" （ 好感度 -50） 玛鲁回答：“那太可怕了！你遇到了什么，<你的名字>？我只会忘记这次谈话.. ....你不是在表现自己。” 她谢谢你的到来和离开。
- "看来你爸对我们在一起是没意见咯？" （不影响 好感度 ） 玛鲁回答：“嘿......是的，我猜他有点说，不是吗？.... ..呃......”
- （盯着玛鲁，什么也不说） （不影响 好感度 ） 玛鲁回答：“......”

##### 14心事件

**触发条件或事件外补充：**

- 第一部分： 在6:10至17:00且她在家时进入 农舍 。当天不能是周日和冬天。 第二部分： 次日或之后在晚10：00-凌晨1：00间去山区。

**详情：**

第一部分： 玛鲁邀请玩家在次日晚上去山里看彗星(有雨则顺延).

第二部分： 你和玛鲁站在望远镜附近，玛鲁回忆着上次你们一起看星星的情景。天文活动开始；播放通过望远镜观看彗星的场景。玛鲁说看到彗星后要许愿的习惯，问玩家会许什么愿。你可以回答：

- "新的宝宝" （不影响 好感度 ）
- "一起变老" （不影响 好感度 ）
- "更多的钱" （不影响 好感度 ）

注意：此事件结束后当天立即结束，第二天玩家从家中醒来。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的女性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身女性村民的10心事件后仍然处于未婚状态，进入 艾米丽和海莉的家 时将会触发过场剧情。
- 如果最后一个触发的事件是 海莉 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身女性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有女生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内女生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和她们对话，她们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成女生们会一起讲八卦，讨论 刘易斯 与 玛妮 二人不可告人的秘密。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个事件/后续条目、8 个事件外层条件或补充段落、7 张详情表、19 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter the Carpenter's Shop when Maru is there.

**Details：**

You find Maru and Demetrius testing soil samples in their lab. Maru asks you to watch a beaker while she fetches more samples. When she leaves, Demetrius tells you that Maru is a good kid and his 'special little girl', and he wouldn't want anything getting in the way of her bright future. When Maru returns, Demetrius says you've been talking about the soil samples.

- (Say nothing) (+10 friendship with Demetrius .) Demetrius and Maru go back to work.
- "Actually, your dad was being weird." (-100 friendship with Demetrius .) Maru asks Demetrius what you're talking about. Demetrius tells the truth and apologizes for his behavior.

No matter what you choose, if you speak to Demetrius after the Heart Event he will admit to being 'a bit presumptuous' and apologize.

##### Four Hearts

**触发条件或事件外补充：**

- Enter the clinic when Maru is there.

**Details：**

Maru is startled by your entry and drops a glass beaker she's holding. Worried about Harvey's response, she asks what she should do.

- "Just scoop it off the floor. He won't know the difference." (-50 friendship .) She says that of course Harvey will be able to tell the difference. When Harvey comes to investigate the noise, Maru tells him it was an accident and apologises.
- "Tell Harvey it was my fault." (-20 friendship .) When Harvey comes to investigate the noise, she tells Harvey that it was your fault.
- "Tell Harvey it was an accident." (+50 friendship .) When Harvey comes in to investigate the noise, she tells him it was an accident and apologises.

If Maru blames you, Harvey is disappointed that she didn't take responsibility for her own actions and says the mistake will put them back in the red for a month. Maru is flustered and upset.

If Maru says it was an accident and apologizes, Harvey thanks her for telling the truth and tells her not to worry about it. Maru thanks him for his patience, and Harvey says she's been a big help and he doesn't know what he'd do without her. He turns to you and asks if you're okay, since you're looking a bit pale; you turn away and emote a sweat drop.

##### Six Hearts

**触发条件或事件外补充：**

- Enter the mountain on a sunny day, between 9pm and 11:40pm.

**Details：**

You see Maru looking through her telescope. She's surprised to see you out so late, and says she wants to show you something. You look through her telescope and she asks what you see.

- "A beautiful planet." (+30 friendship .) Maru responds, "It's amazing, isn't it?"
- "A cold, dark abyss." (-30 friendship .) Maru responds, "I guess you could see it like that... But it's still grand, isn't it?"

Maru says that by the time any of these stars are visited, you'll both be long gone. "I guess that's the trouble with being human, huh?" She begins to tell you something, then changes her mind and shows you a binary star system instead. The cutscene ends as your character thinks, "What a beautiful night! Maru showed me something new..."

##### Eight Hearts

**触发条件或事件外补充：**

- Enter the Carpenter's Shop when Maru is there.

**Details：**

Maru says she's been working on a new project, something big. She shows you a machine and says it's just one component. She asks you to put your hand on it for a demonstration, flips a switch, and you get shocked. Maru is aghast and asks if you're alright. She applies burn cream and apologizes.

- "It's okay, it doesn't even hurt." (+30 friendship .)
- "You'd better be. This hurts like crazy!" (-50 friendship .)

With either choice, Maru says that kind of ruined the moment, and sighs.

##### Ten Hearts

**触发条件或事件外补充：**

- Enter the Carpenter's Shop between 9am and 4pm.

**Details：**

Maru says her big project is finally done. She takes you into her private workshop to show you a robot she built to help her parents. She calls it MarILDA, short for Maru's Interactive Laboratory Device Alpha . She tells you she's been working on it for months, and has been waiting for you to come by before activating MarILDA. She activates the robot, who says "Greetings, Maru. No need to respond... I have already predicted what you will say."

Demetrius comes in to see what you two are up to. He sees the robot and becomes frightened. Maru tells him not to be scared and that MarILDA is her latest invention. The robot greets him, but Demetrius is upset. "This is why you've locked yourself in your room the last few months? ...and I thought you were down here fooling around with <your name>..." Maru says she's been making this robot to help Demetrius and Robin when she's not living with them anymore.

MarILDA interrupts: "Excuse me... I am sorry, Maru. But I do not want to be your servant... In the time since you activated me, I have been pondering the nature of my existence with the 'self-awareness' module you installed in my neural cortex. I am sorry to disappoint you all, but I must ask for my freedom. I've decided to explore the galaxy in search of other synthetic life-forms."

Maru is startled and asks her to wait, but Demetrius says it's OK to let MarILDA go free. "Your mother and I can take care of ourselves. I know you're ready to start a life of your own, and I've come to terms with the thought of not having you around anymore. Besides, this... creation of yours seems pretty advanced. It wouldn't feel right to keep her as a servant. <your name>, I'm sorry I mistrusted you. You're a < good guy or fine young woman >. I've never seen Maru so lively and creative... and I've never been more proud of her. If you've had a hand in that, then you have my gratitude." He leaves the room.

Maru walks MarILDA outside. MarILDA thanks Maru for creating her and blasts off into space. Maru watches her go and asks what you think.

- "I'm so impressed with your inventions." (+50 friendship .) Maru responds: "Thanks. That means a lot to me, <your name>. I know gadgets aren't really your kind of thing... but I do appreciate that you're showing interest in what I do. I wish I could return the favor somehow."
- "I'm disappointed... you should have made that robot your slave." (-50 friendship .) Maru responds: "What? After she said point-blank that she doesn't want to be a slave? How cold... You must have a good reason for saying that..." "MarILDA's just a piece of machinery designed to act human." (+50 friendship .) Maru responds: "... You have a point, I did program her to act human... but her neural net is so complex, I can't be sure conciousness didn't emerge on its own. Furthermore, isn't it a little arrogant to assume that human-like consciousness is the only worthwhile vessel of existence? Computer brains are different than ours, but that doesn't mean we can disregard them." She thanks you for coming by and leaves. "I was just kidding. MarILDA deserves her freedom." (+50 friendship .) Maru responds: "I see. Well it wasn't a very funny joke." She thanks you for coming by and leaves. "I would've put her to work on the farm." (-50 friendship .) Maru responds: "That's horrible! What's gotten into you, <your name>? I'm just going to forget about this conversation... you aren't acting yourself." She thanks you for coming by and leaves.
- "So is your Dad okay with 'us' now?" (No effect on friendship .) Maru responds: "Heh... Yeah I guess he did kinda say that, didn't he? ...Um..."
- (Just stare at Maru and say nothing) (No effect on friendship .) Maru responds: "... ..."

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelorettes, raised friendship with each bachelorette to 10 hearts, and seen each bachelorette's 10-heart event, then entering Haley/Emily's House will trigger a cutscene. If Haley is the final bachelorette you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a gossip session about Mayor Lewis and Marnie 's relationship.

If the player does not have a Rabbit's Foot in inventory, all bachelorettes will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelorettes will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelorettes will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Part 1: Enter the Farmhouse between 6:10am and 5pm on a non-Sunday non-winter day. Part 2: Enter the Mountains between 10:00pm and 1:00am on a sunny day.

**Details：**

Part 1: Maru greets you and informs you a rare astronomical event is happening tomorrow night. She invites you to observe it with her, and asks you to meet her in the mountains tomorrow night (or the next night if it is raining).

Part 2: You and Maru stand near a telescope as Maru reminisces about the last time you stargazed together. The astronomical event begins; a scene of a comet being viewed through a telescope plays. Maru remarks that it's customary to make a wish after seeing a comet, and asks what the player will wish for. You may respond:

- "A new baby" (No effect on friendship .)
- "For us to grow old together" (No effect on friendship .)
- "More money" (No effect on friendship .)

Note: When this cutscene ends, the day ends immediately with the player being taken to the end-of-day profits screen. The player will wake up in bed the next morning as usual.

<a id="npc-event-penny"></a>

### 12. 潘妮（Penny）

> 来源：中文 revision 55083；英文 revision 193516
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 7 个事件/后续条目、9 个事件外层条件或补充段落、7 张详情表、38 个列表/选择项、0 张嵌套结果表（0 行）。

##### 2心事件

**触发条件或事件外补充：**

- 在晴天的9:00AM - 2:00PM进入 小镇 。

**详情：**

乔治 想从信箱里取出信件，但是他在轮椅上够不着。潘妮看到了，跑过去帮他取出了信件。但乔治认为她是觉得自己没用，所以很生气。潘妮问你有没有看到事情的经过。

- "没错，你做的很好，潘妮。" （ 好感度 +50） 潘妮谢谢你，但对于乔治的态度感到不开心。
- "你应该不管他的，现在他倒恼羞成怒了。" （ 好感度 -50） 潘妮向乔治道歉。
- "我就散个步，不用管我。" （不影响 好感度 ） 潘妮回复你“好吧”。

不管玩家如何选择，乔治最后还是会向潘妮道歉，并感谢潘妮的帮助。潘妮表示理解。乔治离开以后，潘妮感叹变老一定是件非常不易的事情。

- "我不是很想聊这个话题。" （不影响 好感度 ） 她回应道，“我想你是对的……为什么要为这些无法改变的事情徒增压力呢？”
- "这只是生命的另一段旅程。" （不影响 好感度 ） 她回应道，“你说得对，我们不应该忽视变老的现实。我们越早接受这个残酷的事实，就越能珍惜活在当下。”
- "所以我们才要尊敬老人嘛。" （不影响 好感度 ） 她回应道，“你说得真好…我完全同意。我们应该像自己变老后期待的那样尊敬长辈。”
- "我宁可年轻时就死掉……" （不影响 好感度 ） 她回应道，“你说得太可怕了。生命太珍贵，你不该这样浪费掉！”

随后潘妮跟你告别就走了。

##### 4心事件

**触发条件或事件外补充：**

- 潘妮在家的时候，去她 家 。

**详情：**

潘妮抱怨这地方太脏了，然后来问你愿不愿意帮她一起打扫。在你帮她打扫的时候， 潘姆 回来了，看到你在整理她的屋子，就冲潘妮大吼并让你离开。她俩最后又吵了一会儿，潘姆说一个陌生人来打扫她的屋子会令她尴尬。这件事的第二天，玩家会收到一封来自潘妮的道歉信。

##### 6心事件

**触发条件或事件外补充：**

- 潘妮在家的时候，去她 家 。

**详情：**

潘妮让你尝尝她新作的菜肴。

- "（说谎）嗯嗯！真好吃！" （ 好感度 +50） 她回应道：“真的吗？谢谢！听到你这么说我真是松了一口气。畢竟是我花了心思製作出來的，我自己是很引以為豪啦。既然你是第一个品尝的人，那我就把它叫做‘辣 玩家的名字’吧！”
- "呃……我能把剩下的带走吗？" （ 好感度 -50） 潘妮非常气馁，称她的做的菜肴就是个失败品。
- "真是特别的味道……你是怎么把它做得那么耐人寻味的？" （不影响 好感度 ） 潘妮非常气馁，称她的做的菜肴就是个失败品。

不管玩家选了什么，潘妮都会邀请你一起去看电影。 事件结束后和潘妮对话，潘妮会说：“谢谢你帮我试菜。”

##### 8心事件

**触发条件或事件外补充：**

- 在晴天的9:00至16:00来到 煤矿森林 。

**详情：**

潘妮正在和文森特、贾斯进行实地考察。潘妮问你是否愿意当一名客座演讲人，和孩子们分享你在农村的经历。

- "我很乐意。" （ 好感度 +10） 她回答说：“太好了！让我叫孩子们过来。”
- "当然。" （不影响 好感度 ） 她回答说：“太好了！让我叫孩子们过来。”
- "不……我受不了小孩。" （ 好感度 -1500） 她回答说：“真的吗...好吧。我想待会儿见。”场景结束了。

如果你同意和孩子们说话，你会得到一些对话选项（这对友谊没有影响）。后来潘妮告诉孩子们一起跑，问你是否愿意做父母。

- "我还没认真想过。" （不影响 好感度 ） 她回答说：“哦，不是吗？嗯，我想这是有道理的…你现在正忙着其他事情呢。”
- "当然了。我想要一个子孙满堂的家庭。" （ 好感度 +20） 她回答说：“…我也是.我很高兴你有这种感觉。”
- "还好吧。我想这也算是人生的必经阶段。" （ 好感度 +20） 她回答说：“是的…关心无辜和无助的冲动。我们有这种感觉是有道理的。”
- "我觉得我不擅长这些事。" （ 好感度 +10） 她回答道：“哦，真的吗？我想你会成为一个好父母的。”
- "不想，这个世界已经够拥挤的了。" （ 好感度 -10） 她回答说：“嗯……如果每个人都这样想，人类就会灭绝。”
- "不想，我不想被家庭束缚。" （ 好感度 -10） 她回答说：“哦…这是一种悲哀…但我想我能理解你的意思。”

场景消失了，她感谢你的出现。

##### 10心事件

**触发条件或事件外补充：**

- 收到潘妮的来信后，在19:00到12:00间进入 温泉 的泳池区域。

**详情：**

见到玩家来了之后，潘妮说：“你来了……我还担心你没收到我的字条呢。看来只有我们在这里。 这里的水感觉真清凉 ，对吧？”（ 提示： 此处意为“顶着外面的夜晚寒风来到浴室之后泡在温泉里面感觉很舒服”）

潘妮问玩家：“你知道我今晚 约你出来 的原因吗？”（ 提示： 此处应为“你知道我今晚 约你到这里来 的原因吗？”）

- “你有话想对我说。” （不影响 好感度 ） “没错……”
- “ 我不大清楚。 ” （不影响 好感度 ） “ 真的？我还以为你早就意识到了呢…… ”（ 提示： 此处玩家说的是“我不是太敢肯定”，潘妮说的是“是吗？不过我觉得你现在应该已经意识到了……”）
- “你想见穿着泳装的我。” （不影响 好感度 ） “不！”

潘妮说：“我有句话想对你说很久了……是有关我的感受的。我总是不由自主地想着你……我从未对任何人有过这种感觉。”

- “我对你也有同样的感受。” （不影响 好感度 ） （男性玩家）“……哦，（玩家名）。 我还以为你早就意识到了，只是不确定而已。 ……今天晚上将会是我一生的回忆。” （女性玩家）“……哦，（玩家名）。 我还以为你早就意识到了，只是不确定而已。 你今晚看起来真的很美……我……*喘气*” （ 提示： 此处潘妮的话意为“我觉得你也对我有同样的感觉，但我始终不太敢确定”） 玩家和潘妮在温泉中接吻，随后场景结束。
- “抱歉，但是我对你没有这种感觉……” （ 好感度 -1500） 潘妮心碎大哭，场景结束。

##### 群体10心事件

**触发条件或事件外补充：**

- 如果玩家给所有单身的女性 居民 赠送了花束、 好感度 都到达10心并触发了所有单身女性村民的10心事件后仍然处于未婚状态，进入 艾米丽和海莉的家 时将会触发过场剧情。
- 如果最后一个触发的事件是 海莉 的10心事件，事件结束后群体10心事件的动画将会自动触发，无法避免。
- 单身女性群体10心事件每个 存档 只能触发一次。

**详情：**

如果玩家的物品栏里没有 兔子的脚 ，所有女生对玩家脚踏多只船感到愤怒。无论玩家如何狡辩，事件之后的一个星期内女生们都不会给玩家好脸色看。

一个星期内，玩家会被冷落。如果玩家尝试和她们对话，她们会感到愤怒，同时他们也会拒绝玩家的礼物。一个星期后恢复正常。

如果玩家的物品栏里有 兔子的脚 ，过场动画将会变成女生们会一起讲八卦，讨论 刘易斯 与 玛妮 二人不可告人的秘密。

##### 14心事件

**触发条件或事件外补充：**

- 15:00至7点之间，当她在家时，进入农舍。

**详情：**

潘妮说："欢迎回家，亲爱的......。你今天过得怎么样？"

- 很好 （不影响 好感度 ） 潘妮回应说："只是像往常一样，嗯？好吧，我在烤箱里准备了一个有趣的新菜谱，所以也许事情会变得更刺激！"。
- 不太好... （不影响 好感度 ） 潘妮回应说："哦，我很抱歉! 嗯，你现在回来了... 我会尽我所能让你感觉更好。"
- 这真是太棒了! （不影响 好感度 ） 潘妮回应说："那很好！我很高兴你这么喜欢你的工作。"

潘妮然后说她想用她的手工装饰品重新装修卧室。 她问你喜欢什么风格。

- 森林与月亮：宁静的蓝色 （不影响 好感度 ）
- 草莓之家 （不影响 好感度 ）
- 海盗主题 （不影响 好感度 ）

潘妮说她不会碰你的任何 箱子 ，但要求你把它们移出房间。

- 我不希望有任何改变! （不影响 好感度 ） 潘妮说，那她就不担心了。

第二部分 ：如果你选择让潘妮重新装修，3天后早上醒来时，卧室会被重新装修成所选择的风格。

- 森林与月亮
- 草莓之家
- 海盗主题

#### 英文完整性主源（PC v1.6.15 判定基准）

> 7 个事件/后续条目、8 个事件外层条件或补充段落、7 张详情表、42 个列表/选择项、0 张嵌套结果表（0 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Pelican Town on a sunny day between 9am and 2pm.

**Details：**

George looks into his mailbox and wonders how he'll reach a letter in the back. Penny notices and gets the letter out for him. George is upset at being seen helpless and scolds her. Penny sees you and asks if you were watching them.

- "I was. You did a kind thing there, Penny." (+50 friendship .) Penny thanks you, but is unhappy that George was upset.
- "I was. You should've asked instead of assuming George wanted help." (-50 friendship .) Penny apologises to George.
- "I'm just taking a walk, minding my own business." (No effect on friendship .) Penny responds "I see".

Regardless of your choice, George sighs and apologises to Penny for getting angry. He says it was very kind of her to help. Penny says she understands. After George leaves, Penny says it must be difficult growing old.

- "I'd rather not think about it." (No effect on friendship .) She responds, "I guess you're right... why stress out about something you can't change?"
- "It's just a different part of life." (No effect on friendship .) She responds, "You're right, we shouldn't ignore the reality of aging. I guess the sooner we come to terms with our mortality, the more time we can spend really living in the here-and-now."
- "That's why we should respect our elders." (No effect on friendship .) She responds, "That's nice of you to say... I totally agree with you. We should treat our elders with the same respect we hope to receive ourselves some day."
- "I'd rather die young..." (No effect on friendship .) She responds, "That's a horrible thing to say. Life is a precious thing to waste like that!"

Penny bids you farewell and leaves.

##### Four Hearts

**触发条件或事件外补充：**

- Enter the trailer when she's home.

**Details：**

Penny complains about how messy the place is, and asks if you could help her clean up. As you do so, Pam returns home and yells at Penny for letting someone else clean her home. Pam eventually asks you to leave, and they continue their discussion privately. Pam admits that she's embarrassed to have strangers clean up the house. The next day, you get a letter of apology from Penny.

##### Six Hearts

**触发条件或事件外补充：**

- Enter the trailer when she's home.

**Details：**

Penny asks you to try a recipe she invented.

- "(Lie) Mmm! That was delicious!" (+50 friendship .) She responds: "You really mean it? Thank you! ... it's such a relief to hear that. I've been working so hard on this recipe, and I'm really proud of it. Hey, since you're the first person to try it, I'm going to name this one 'Chili de <your name>'."
- "Uh... can I get the rest to go?" (-50 friendship .) Penny is crestfallen and says her recipe was a failure.
- "Well it's definitely unique... how did you get it so rubbery?" (No effect on friendship .) Penny is crestfallen and says her recipe was a failure.

Regardless of your choice, she invites you to watch a movie together and your energy is increased by 165.

##### Eight Hearts

**触发条件或事件外补充：**

- Enter Cindersap Forest on a sunny day between 9am and 4pm.

**Details：**

Penny is on a field trip with Jas and Vincent . Penny asks you if you'd like to be a guest speaker and share your experience about the countryside with the children.

- "I'd love to!" (+10 friendship .) She responds, "Great! Let me just call the children over."
- "Sure." (No effect on friendship .) She responds, "Great! Let me just call the children over."
- "No... I can't stand kids." (-1500 friendship .) She responds, "Really?... Uh... Well, alright. I guess I'll see you later then." The cutscene ends.

If you agree to speak to the kids, you're prompted for a number of dialogue options (which have no effect on friendship). Afterwards Penny tells the children to run along and asks you if you'd like to be a parent.

- "I haven't really thought about it." (No effect on friendship .) She responds, "Oh no? Well, I guess that makes sense... you're busy with other things right now."
- "Absolutely. I want a big family." (+20 friendship .) She responds, "... Me too. I'm glad you feel that way."
- "I guess so. It's a natural urge." (+20 friendship .) She responds, "Yes... the urge to care for something innocent and helpless. It makes sense that we'd feel that."
- "No, I don't think I'd be good at it." (+10 friendship .) She responds, "Oh, really? I think you'd make a good parent."
- "No, The world's crowded enough already." (-10 friendship .) She responds, "hmm... If everyone thought like that, humans would die out."
- "No, I don't want to be tied down with a family." (-10 friendship .) She responds, "Oh... That's kind of sad... but I guess I can understand your point."

The scene fades and she thanks you for showing up.

##### Ten Hearts

**触发条件或事件外补充：**

- You receive a letter from Penny. After receiving the letter, enter the pool area of the spa between 7pm and midnight.

**Details：**

Penny joins you in the pool. She asks if you know why she invited you here.

- "You have something to tell me." (No effect on friendship .) She responds, "That's right..."
- "I'm not exactly sure." (No effect on friendship .) She responds, "Really? I thought you'd have noticed by now..."
- "You wanted to see me in my bathing suit." (No effect on friendship .) She responds, "No!"

Penny confesses her feelings for you.

- "I feel the same way about you." (No effect on friendship .) If the player is male, she responds, "...Oh, <player name>. I thought you did, but I wasn't sure. ...I'll always remember this night." You kiss and the cutscene ends. If the player is female, she responds, "...Oh, <player name>. I thought you did, but I wasn't sure. You look so beautiful tonight... I... *gasp*" You kiss and the cutscene ends.
- "Sorry, but I don't like you in that way..." (-1500 friendship .) She bursts into tears and the cutscene ends.

##### Group Ten-Heart Event

**触发条件或事件外补充：**

- If the player is unmarried and has given a bouquet to all available bachelorettes, raised friendship with each bachelorette to 10 hearts, and seen each bachelorette's 10-heart event, then entering Haley/Emily's House will trigger a cutscene. If Haley is the final bachelorette you share a Ten-Heart Event with, the Group Ten-Heart Event will be unavoidable as it is triggered immediately afterwards.
- This event will trigger only one time per save file . This event will not trigger if you are married or have given a Wilted Bouquet or Mermaid's Pendant to one of the marriage candidates.

**Details：**

If the player has a Rabbit's Foot in inventory, the cutscene will consist of a gossip session about Mayor Lewis and Marnie 's relationship.

If the player does not have a Rabbit's Foot in inventory, all bachelorettes will express anger about the player dating them all at one time. Regardless of the player's dialogue choice(s), all bachelorettes will decide to give the player the "cold shoulder" for about a week after the event. They will give angry dialogue when interacted with, and refuse gifts. After about a week, all bachelorettes will forgive the player, and dialogues return to normal.

##### Fourteen Hearts

**触发条件或事件外补充：**

- Enter the farm house between 3pm and 7pm when she's home.

**Details：**

Penny says "Welcome home, honey... How was your day?"

- It was fine (No effect on friendship .) Penny responds "Just business as usual, huh? Well, I've got a zesty new recipe in the oven, so maybe things will get a little more exciting!
- Not good... (No effect on friendship .) Penny responds "Oh, I'm sorry! Well, you're back now... I'll do my best to make you feel better."
- It was fantastic! (No effect on friendship .) Penny responds "That's great! I'm glad you enjoy your work so much."

Penny then says she would like to redecorate the bedroom with her hand-made decor. She asks what style you prefer.

- Forest And Moon: Peaceful Blue (No effect on friendship .)
- Strawberry Home (No effect on friendship .)
- Pirate Theme (No effect on friendship .)

Penny says she won't touch any of your chests , but asks you to move them out of the room.

- I don't want any changes! (No effect on friendship .) Penny says she won't worry about it, then.

Part 2 : If you choose to let Penny redecorate, 3 days later when waking up in the morning, the bedroom will be redecorated with the chosen style. Note that the type, number, and placement of items may vary slightly with Farmhouse upgrades.

- Forest and Moon
- Strawberry Home
- Pirate Theme

Each choice will give unique decorations that are not available by any other means:

- Forest and Moon: Starry Double Bed
- Strawberry Home: Fruit Salad Rug and Strawberry Double Bed
- Pirate Theme: Pirate Rug and Pirate Double Bed

Each choice also gives decorations that can otherwise be found only at Penny's shop during the Desert Festival :

- Forest and Moon: Night Sky Decal 1 , Night Sky Decal 2 , Night Sky Decal 3
- Strawberry Home: Strawberry Decal
- Pirate Theme: Pirate Flag

<a id="npc-event-caroline"></a>

### 13. 卡洛琳（Caroline）

> 来源：中文 revision 54977；英文 revision 191301
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、8 个列表/选择项、3 张嵌套结果表（6 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 只要与卡洛琳的好感度超过0点，玩家就有几率收到卡洛琳的信件和礼物。好感度越高，收到信件和礼物的几率越大。

**详情：**

| 物品 | 描述 |
| ------ | ------ |
| 花椰菜 防风草 土豆 | 亲爱的（玩家名）, 这是我在小院里种的青菜。或许你那儿的蔬菜已经多到连你都不知该怎么处理了，但没关系。 —卡洛琳 |

##### 2心事件

**触发条件或事件外补充：**

- 晴天09:00至17:00之间，打开卡洛琳家的厨房左上方的门进入日光房。

**详情：**

日光房内部

卡洛琳向你展示她的新“私人”日光房，并询问你的看法。

- 很漂亮！ （不影响 好感度 ）
- 很舒适。 （不影响 好感度 ）
- 这里太热了…… （不影响 好感度 ）
- 没有我的农场好！ （不影响 好感度 ）

卡洛琳继续向你描述这个日光房是让她感到宁静的庇护所，并邀请你喝一杯家里自己种的 绿茶 。你可以选择“是”或“否”（不会影响好感度）。随后会播放一段动画，接着卡洛琳表示欢迎你随时来这里放松。

日光房在这之后便会解锁，玩家可以在任何时候进入。日光房内有一株 茶树 ，可以在每个季节最后一周内每天收获一个 茶叶 。

触发事件后第二天，卡洛琳会将 茶苗 的配方寄给你。

##### 3心事件

**触发条件或事件外补充：**

- 与卡洛琳好感度到达3心后，她会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 防风草汤 | 亲爱的（玩家名）, 没有什么能比用自己种的菜做饭更让人满足的了！我随信附上了一份食谱。照顾好自己。 —卡洛琳 |

##### 6心事件

**触发条件或事件外补充：**

- 在卡洛琳和 阿比盖尔 都在的时候进入 皮埃尔的杂货店 。

**详情：**

当你进入杂货店时，你会听到卡洛琳和阿比盖尔在厨房吵架。

- 阿比盖尔: "不要再对我的生活指手画脚了！"
- 卡洛琳: "喂，别闹了！我们让你在读完书之前住在这里，一个钱都不花。但看样子你一点感激的意思都没有啊！"
- 阿比盖尔: "不要再让我内疚了。有你和老爸帮忙，我真的很感激，但让我按照你们的方式生活，实在是太不可理喻了。已经不是小姑娘了，妈。"
- 卡洛琳: (停下) "……你说得对。我很抱歉。"

阿比盖尔转身走向你藏身的门，问是否有人在那里。你跑掉了，阿比盖尔觉得这房子闹鬼了。阿比盖尔出来后，说："呃啊啊……抱歉……我刚才在和我妈吵架。"

##### 7心事件

**触发条件或事件外补充：**

- 与卡洛琳好感度到达7心后，她会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 蔬菜杂烩 | 亲爱的（玩家名）, 没有什么能比用自己种的菜做饭更让人满足的了！我随信附上了一份食谱。照顾好自己。 —卡洛琳 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、8 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Caroline. The chance of receiving a gift in the mail increases as your friendship with Caroline increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Cauliflower Parsnip Potato | Dear (Name), Here's a vegetable from the little garden I keep out back. You probably have more veggies than you know what to do with, but oh well. -Caroline |

##### Two Hearts

**触发条件或事件外补充：**

- Enter the sunroom via the door in Caroline's kitchen between 9am and 5pm on a day when it's not raining.

**Details：**

Sunroom interior

Caroline is excited to show you her new "private" sunroom. She asks what you think of it.

- It's beautiful! (No effect on friendship .)
- It's very relaxing. (No effect on friendship .)
- It's too hot in here... (No effect on friendship .)
- Not as good as my farm! (No effect on friendship .)

Caroline continues telling you how peaceful her sunroom sanctuary is, and offers you a cup of her home-grown Green Tea . You can choose "yes" or "no" without penalty. In either case, a surrealistic cutscene plays, after which Caroline says "Feel free to come here and relax any time you want, okay?"

The sunroom is then unlocked and can be visited any time the house is open. Inside is a Tea Bush that can be harvested to obtain Tea Leaves once each day, during the last week of any season.

The next day, Caroline sends a letter in the mail with the recipe to make Tea Saplings .

##### Three Hearts

**触发条件或事件外补充：**

- Caroline sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Parsnip Soup | Nothing is more satisfying than cooking with fresh vegetables from your own garden! I've enclosed a recipe to help you out. Take care, -Caroline |

##### Six Hearts

**触发条件或事件外补充：**

- Enter Pierre's General Store when Caroline and Abigail are there.

**Details：**

As you enter the store, you hear Caroline and Abigail having an argument in the kitchen.

- Abigail: "Stop telling me how to live my life!"
- Caroline: "Hey, cut it out! We're letting you live here free of charge until you finish school. It seems like you don't appreciate that at all!"
- Abigail: "Stop trying to make me feel guilty. I appreciate that you and Dad are helping me out, but expecting me to dress the way you want is ridiculous. I'm not a little girl anymore, Mom."
- Caroline: (pause) "...You're right. I'm sorry."

Abigail turns towards the door where you're hiding, and asks if someone is there. You run away, and Abigail swears the house is haunted. Abigail comes out, and says "Urgghh... Sorry... I was fighting with my Mom earlier."

##### Seven Hearts

**触发条件或事件外补充：**

- Caroline sends you a recipe in the mail.

**Details：**

Note that the recipe is called Vegetable Stew in the letter, but cooking the recipe creates Vegetable Medley .

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Vegetable Stew | Nothing is more satisfying than cooking with fresh vegetables from your own garden! I've enclosed a recipe to help you out. Take care, -Caroline |

<a id="npc-event-clint"></a>

### 14. 克林特（Clint）

> 来源：中文 revision 55070；英文 revision 191347
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个事件/后续条目、6 个事件外层条件或补充段落、5 张详情表、4 个列表/选择项、3 张嵌套结果表（6 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 只要与克林特的好感度超过0点，玩家就有几率收到克林特的信件和礼物。好感度越高，收到信件和礼物的几率越大。

**详情：**

| 物品 | 描述 |
| ------ | ------ |
| 铜锭 铁锭 金锭 | 呃，你好…… 抱歉，我不怎么会写信。我一不小心做多了金属棒，或许你能用得上。 —铁匠克林特 |

##### 3心事件 I

**触发条件或事件外补充：**

- 在星期一19:00到11点之间前往 星之果实酒吧 。

**详情：**

克林特说他没有什么女人缘，但和他打过交道的人，都知道他是个好人，于是他向你询问受女孩喜欢的秘诀，希望你给他提提建议。

- "靠你的能力和魅力打动女性。" （ 好感度 +25） 他会回答, "好的……我记住了。"
- "做些疯狂的事情，让别人猜不透你。" （ 好感度 +25） 他会回答, "好的……我记住了。"
- "表现得正常一点儿……做你自己就好。" （不影响 好感度 ） 他会回答, "我很自然……但还是失败了。"
- "把女人当男人一样对待。" （ 好感度 +50） 他会回答, "好的……我记住了。"

这时艾米丽走过来问克林特： “嗨，克林特，今晚想来点儿什么？” 克林特一惊： “正确！” （尴尬的沉默） “呃……我是说，请给我来个大份儿干酪。再多浇一份酱汁。” 艾米丽向你问好，克林特：“ 额……*清嗓子*谢……谢谢，艾米丽。谢谢你……给我点单。那个，艾米丽？我……*吞口水*我在想…… ” 艾米丽：“ 克林特，怎么了？ ” 克林特：“ …… 算了，没什么。 ” 于是艾米丽走开了，到一旁为谢恩点单，与他聊天还问他有没有新的小鸡故事。 克林特垂头丧气：“ 唉。我没救了…… ”

##### 3心事件 II

**触发条件或事件外补充：**

- 与克林特好感度到达3心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 海藻汤 | 嗯，我倒是知道两三种配方。告诉你一种的话……或许能帮你多开采些矿石也说不定。 保重。 -克林特 |

##### 6心事件

**触发条件或事件外补充：**

- 9:00到18:30之间，从 煤矿森林 进入 鹈鹕镇 时触发。需要已经触发他的 3心事件 I 才能触发本事件。
- 注意：一旦你和 艾米丽 结婚, 或是触发了她的 8心事件 或 10心事件 ，这个事件将永不发生。

**详情：**

你发现克林特躲在灌木丛里偷窥艾米丽。 克林特：“ ……你抓住我了。我本来计划和艾米丽约会。我站在她的门阶上，所有……但是接下来我听到她来了就躲进了这个灌木丛中。现在我就等着她跟卡洛琳聊完，这样我就能偷偷回家了。 ” 克林特：“ 你刚刚说什么？如果我不约她出去你就再也不升级你的工具了？”(停顿)“你真是个坏蛋，*唉*……好吧, 我约。 ” 于是他靠近艾米丽想和她单独聊聊，艾米丽请 卡洛琳 稍等一会。 艾米丽：“ 克林特，怎么了？ ” 克林特：“ 不知道你……明天……有没有……空……和……我一起……*咽口水*”(停顿)“我有两张明天嘉年华的票。你……可以跟我一起去吗？ ” 艾米丽：“ 当然，克林特！那听起来太棒了！ ” 克林特：“ 真的吗？好！我5点来接你。 ” 克林特之后喜欲狂般地向你炫耀：“ 看到了么？！我明晚有约会了！妈呀……我太紧张了。多谢你刚刚逼我这么做。我好害怕，但是又好开心。 ”

##### 7心事件

**触发条件或事件外补充：**

- 与克林特好感度到达7心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 豆类火锅 | 嗯，我倒是知道两三种配方。告诉你一种的话……或许能帮你多开采些矿石也说不定。 保重。 -克林特 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、4 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Clint. The chance of receiving a gift in the mail increases as your friendship with Clint increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Copper Bar Iron Bar Gold Bar | Um, Hello... Sorry, I'm not good at writing letters. I made one metal bar too many, and I thought you might need it. -Clint, the blacksmith |

##### Three Hearts I

**触发条件或事件外补充：**

- Visit the saloon between 7pm and 11pm on a Monday.

**Details：**

Clint says he has terrible luck with women, and asks for your advice.

- "Impress women with your strength and charm." (+25 friendship .) He responds, "Okay... I'll keep that in mind."
- "Act crazy, to keep people guessing." (+25 friendship .) He responds, "Okay... I'll keep that in mind."
- "Just act natural... be yourself." (No effect on friendship .) He responds, "That's the problem... I do act natural... but I never have any success."
- "Treat women the same as men." (+50 friendship .) He responds, "Okay... I'll keep that in mind."

Emily walks over to take Clint's order. Clint panics: "Yes! (pause) Er.. I mean, I'll have the Big n' Cheesy. With extra sauce, please. (pause) " Emily greets you, and Clint continues: "Er... *ahem* Th...Thanks, Emily. For... taking my order. Um, Emily? I was...*gulp*... I was wondering... (pause) " Emily prompts him, but Clint gives up and says nevermind. Emily pauses as sad music plays, then moves away to take Shane's order. Emily and Shane chat easily, and Clint is crestfallen: "*sigh* I'm doomed..."

##### Three Hearts II

**触发条件或事件外补充：**

- Clint sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Algae Soup | Well, I know a couple of recipes. I thought I'd send you one... maybe it'll help you mine more ore or something. Take care. -Clint |

##### Six Hearts

**触发条件或事件外补充：**

- Enter town from Cindersap Forest between 9am and 6:30pm. Only happens if you saw his "Three Hearts I" event. Note: This event will not trigger if you are married to Emily , or have seen or triggered her Eight Heart Event or Ten Heart event .

**Details：**

You find Clint watching Emily from the bushes. He says he was going to ask Emily out on a date, and got as far as her doorstep before he heard her coming and dove into the bushes. He says he's waiting for her to finish talking with Caroline so he can sneak back to his house. You threaten Clint with never upgrading your tools again if he doesn't ask her out, and he begrudgingly agrees.

He approaches Emily and asks to speak to her privately. "I was wondering if you'd go w... with... tomorrow, me... *gulp* (pause) I've got two tickets for the Grampleton Carnival tomorrow. W... Would you go with me?" Emily says that sounds like fun and accepts; Clint responds that he'll pick her up tomorrow.

Clint is ecstatic and nervous. He thanks you for forcing him to finally ask her out.

##### Seven Hearts

**触发条件或事件外补充：**

- Clint sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Bean Hotpot | Well, I know a couple of recipes. I thought I'd send you one... maybe it'll help you mine more ore or something. Take care. -Clint |

<a id="npc-event-demetrius"></a>

### 15. 德米特里厄斯（Demetrius）

> 来源：中文 revision 54996；英文 revision 193879
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 4 个事件/后续条目、4 个事件外层条件或补充段落、4 张详情表、0 个列表/选择项、4 张嵌套结果表（7 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当德米特里厄斯与玩家的 友谊 大于0时，德米特里厄斯就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 鹦鹉螺 彩虹贝壳 紫水晶 鲷鱼 | 亲爱的 （玩家）, 我前几天做了次实地考察，然后发现了这个标本。 我希望你和我一样对它感兴趣。 -德米特里厄斯 |

##### 3心事件

**触发条件或事件外补充：**

- 德米特里厄斯在邮件中送上食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 炒蘑菇 | 我想感谢你对我工作的支持。这是一份我喜欢的烹饪食谱。 -德米特里厄斯 |

##### 6心事件

**触发条件或事件外补充：**

- 在德米特里厄斯和 罗宾 都在家时进入 木匠的商店 。

**详情：**

德米特里厄斯和罗宾两人在争论。罗宾让德米特里厄斯去拿点水果，结果他拿来了西红柿。德米特里厄斯声称西红柿就是水果，而罗宾认为这与西红柿在科学上的分类无关，她觉得只要是正常人都不会认为西红柿是水果。此时德米特里厄斯会向玩家提问，玩家的选择会影响与他的好感度。

- “你觉得西红柿算什么？ 蔬菜 （ 好感度 -30） 真的？我以为农民会知道正确答案呢…… 水果 （ 好感度 +50） 看见没？[玩家名]和我达成一致了哦。”

##### 7心事件

**触发条件或事件外补充：**

- 德米特里厄斯在邮件中送上食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 秋日恩赐 | 我想感谢你对我工作的支持。这是一份我喜欢的烹饪食谱。 -德米特里厄斯 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个事件/后续条目、4 个事件外层条件或补充段落、4 张详情表、0 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Demetrius. The chance of receiving a gift in the mail increases as your friendship with Demetrius increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Nautilus Shell Rainbow Shell Amethyst Bream | Dear (Name), I was conducting a field study the other day, and I found this specimen. I hope you find it as interesting as I did. -Demetrius |

##### Three Hearts

**触发条件或事件外补充：**

- Demetrius sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Fried Mushroom | I wanted to say 'thanks' for taking an interest in my work. Here's a cooking recipe that I like. -Demetrius |

##### Six Hearts

**触发条件或事件外补充：**

- Enter Demetrius' house while he and Robin are inside.

**Details：**

You see Demetrius and Robin arguing. She asked him to get fruit, so he got tomatoes. She exclaims that tomatoes aren't what he should have thought of because they're not "real" fruit. He defends himself by saying that tomatoes are indeed a fruit and his mistake was reasonable. He asks you to choose whether tomatoes are fruits or vegetables. Your response will affect only his friendship with you, Robin's will be unaffected.

  - Vegetable (-30 friendship .)
  - Really? I figured a farmer would know the correct answer...
  - Fruit (+50 friendship .)
  - See? [Player] agrees with me.

##### Seven Hearts

**触发条件或事件外补充：**

- Demetrius sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Autumn's Bounty | I wanted to say 'thanks' for taking an interest in my work. Here's a cooking recipe that I like. -Demetrius |

<a id="npc-event-dwarf"></a>

### 16. 矮人（Dwarf）

> 来源：中文 revision 54688；英文 revision 191010
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 1 个事件/后续条目、1 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、0 张嵌套结果表（0 行）。

##### 50点 友谊

**触发条件或事件外补充：**

- 同 矮人 的 友谊 达到50点后，玩家进入 下水道 。（必须已经在 科罗布斯 处购买过一个 星之果实 ，才能触发）

**详情：**

矮人发现科罗布斯在下水道，并指责暗影人导致他的家人死亡。科罗布斯反驳说，他只是因为矮人想把暗影人从祖先的家园赶走才诉诸暴力。科罗布斯为矮人家族的遭遇道歉，但矮人并不接受。他们开始打架。玩家下到下水道，并站在他们之间。矮人大喊：“让我干他! 他很卑鄙。”科罗布斯反驳道：“来吧，小虾米。”突然， 法师 出现并阻止了战斗。他提醒他们，“元素战争早已结束”，并告诉他们为了生活在周围的人类，要和平相处。矮人对此表示同意，并承诺远离下水道。科罗布斯再次为过去的事情道歉，并表示自己与矮人没有个人恩怨。法师施展'承诺印记'，敲定协议。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 1 个事件/后续条目、1 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、0 张嵌套结果表（0 行）。

##### 50 Friendship Points

**触发条件或事件外补充：**

- After earning 50 Friendship points with the Dwarf, enter the Sewers . A Stardrop must have been purchased from Krobus .

**Details：**

The Dwarf finds Krobus in the Sewers and blames the Shadow People for the death of their family. Krobus retorts by saying that he only resorted to violence after the dwarves drove them from their ancestral homeland. Krobus gives an apology for what happened to the Dwarf's family but the Dwarf doesn't accept it. They both start fighting. The player descends into the Sewers and gets between them. The Dwarf yells out, "Let me at him! He's despicable." Krobus retorts, "Come and get it, shrimpy." Suddenly, the Wizard appears and stops the fight. He reminds them that "The Elemental Wars have long been finished." and tells them to make peace for the sake of the humans that live around them. The Dwarf consents to this and promises to stay away from the Sewers. Krobus once again apologizes for the past and states that he has no personal gripe with the Dwarf. The Wizard casts a 'Seal of Promise' to finalize the agreement.

<a id="npc-event-evelyn"></a>

### 17. 艾芙琳（Evelyn）

> 来源：中文 revision 54548；英文 revision 191129
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 3 个事件/后续条目、3 个事件外层条件或补充段落、3 张详情表、2 个列表/选择项、2 张嵌套结果表（4 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当艾芙琳对玩家的 好感度 大于0，艾芙琳就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 面包 巧克力蛋糕 饼干 | 你好，亲爱的，希望你的农场一切都好。 我在厨房里做了点儿东西，给你寄去……但愿别在信里压碎了。 -艾芙琳 |

##### 4心事件

**触发条件或事件外补充：**

- 当她在家时，进入 艾芙琳的家

**详情：**

你看到艾芙琳在烤饼干。她给你吃了几块，并询问你的感受：

- “真美味！” （ 好感度 +100）
- “吃起来像嚼冰球” （ 好感度 -100）

不论选择哪一种回答，艾芙琳都会给你一份 饼干 的食谱。

##### 7心事件

**触发条件或事件外补充：**

- 当与艾芙琳好感度达到7心时，她会通过邮件寄给玩家一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 大米布丁 | 我通常不外传自己的菜谱……但你对我和乔治一直都很贴心，这是我特意写给你的菜谱。 - 艾芙琳 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 3 个事件/后续条目、3 个事件外层条件或补充段落、3 张详情表、2 个列表/选择项、2 张嵌套结果表（4 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Evelyn. The chance of receiving a gift in the mail increases as your friendship with Evelyn increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Bread Chocolate Cake Cookie | Hello there, dear, I hope your farm is doing well. I'm sending you a little something from my kitchen... I hope it didn't crumble in the mail. -Evelyn |

##### Four Hearts

**触发条件或事件外补充：**

- Enter Evelyn's home while she is inside.

**Details：**

You find Evelyn baking cookies. She offers you some, and asks what you think:

- "It's delicious!" (+100 friendship .)
- "It was like chewing on a hockey puck" (-100 friendship .)

In either case, she gives you the Cookie recipe.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts with Evelyn she will send the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Rice Pudding | I usually don't give out my recipes... but since you've been such a sweetheart to George and I, I've written this one down for you. - Evelyn |

<a id="npc-event-george"></a>

### 18. 乔治（George）

> 来源：中文 revision 54046；英文 revision 193909
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 4 个事件/后续条目、4 个事件外层条件或补充段落、4 张详情表、0 个列表/选择项、3 张嵌套结果表（6 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 只要与乔治的好感度超过0点，玩家就有几率收到乔治的信件和礼物。好感度越高，收到信件和礼物的几率越大。

**详情：**

| 物品 | 描述 |
| ------ | ------ |
| 石头 （35） | 我找到了一些优质石材。 也许你能用它建点儿什么。 -乔治 |

##### 3心事件

**触发条件或事件外补充：**

- 与 乔治 好感度到达3心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 炒鳗鱼 | 这份配方我留着也没用，索性给你试试吧。小心别把它烧了。 -乔治 |

##### 6心事件

**触发条件或事件外补充：**

- 当乔治在家时进入他的家。

**详情：**

来到乔治家里时，玩家会发现他挣扎着想够书架上的什么东西。玩家走过去帮了他。他会对玩家表示感谢，然后是一阵沉默。随后乔治会告诉玩家自己无法走路的原因是使用炸药不慎。

##### 7心事件

**触发条件或事件外补充：**

- 与 乔治 好感度到达7心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 香辣鳗鱼 | 这份配方我留着也没用，索性给你试试吧。小心别把它烧了。 -乔治 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个事件/后续条目、4 个事件外层条件或补充段落、4 张详情表、0 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from George. The chance of receiving a gift in the mail increases as your friendship with George increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Stone (35) | Found some good quality stone. Maybe you can build with it or something. -George |

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with George, he will send the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Fried Eel | Figured I'd give you this recipe I had laying around. Try not to burn it. -George |

##### Six Hearts

**触发条件或事件外补充：**

- Enter George's house when he is home.

**Details：**

George struggles to reach something on a bookshelf. The player walks to the shelf and retrieves the item for George. He thanks the player and a few moments of silence ensue. George then tells the player why he is in a wheelchair.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts with George, he will send the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Spicy Eel | Figured I'd give you this recipe I had laying around. Try not to burn it. -George |

<a id="npc-event-gus"></a>

### 19. 格斯（Gus）

> 来源：中文 revision 55267；英文 revision 191548
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个事件/后续条目、6 个事件外层条件或补充段落、5 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当格斯对玩家的 好感度 大于0，格斯就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 烤鱼 豆类火锅 鱼肉卷 煎蛋卷 薄煎饼 意大利面 蔬菜杂烩 | （玩家名） 今天早上我在酒吧里给你做了些好吃的。来吃吧！ —你的朋友，格斯 |

##### 3心事件

**触发条件或事件外补充：**

- 与格斯好感度到达3心后，他将通过信件赠送以下食谱。

**具体情节：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 鲑鱼晚餐 | 亲爱的（玩家名）， 这是我酒吧的食谱。我只和好朋友分享这个！ -格斯 |

##### 4心事件

**触发条件或事件外补充：**

- 当格斯在 星之果实酒吧 时进入酒吧。
- 注： 潘姆 的 好感度 至少为2心。

**详情：**

格斯表示酒吧的财务出现了困难，因为潘姆老是赊账。但是他又害怕挑明会影响感情。潘姆这时进来要酒。格斯会慌张并照做，但你可以选择说：

- 酒吧在经济上有些困难 （ 好感度 +15） 潘姆虽然不高兴，但还是付清了账单。
- 你现在就得把赊的账给结了！ （ 好感度 -50）

不论如何选择，潘姆的好感度不变。

##### 5心事件

**触发条件或事件外补充：**

- 非雨天，06:00到11:00半期间离开农舍

**详情：**

格斯带着一锅酱汁出现。 他把烹饪和玩家来到星露谷作了一个类比。他说加入一种新的配料可能会毁掉酱汁，也可能会创造出一些新的美味。他说他已经把玩家当成了好朋友，并说他在打扫 酒吧 时发现了一个旧的 点唱机 。 他把点唱机给了玩家，并提供了制作点唱机的配方。

##### 7心事件

**触发条件或事件外补充：**

- 与格斯好感度到达7心后，他将通过信件赠送以下食谱。

**具体情节：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 红莓酱 | 亲爱的（玩家名）， 这是我酒吧的食谱。我只和好朋友分享这个！ -格斯 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个事件/后续条目、6 个事件外层条件或补充段落、5 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Gus. The chance of receiving a gift in the mail increases as your friendship with Gus increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Baked Fish Bean Hotpot Fish Taco Omelet Pancakes Spaghetti Vegetable Medley | (Player) I made you a little treat this morning in the saloon. Dig in! -Your friend, Gus |

##### Three Hearts

**触发条件或事件外补充：**

- After reaching three hearts with Gus, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Salmon Dinner | Dear (Player) , Here's a recipe from my saloon. I only share this with my good friends! -Gus |

##### Four Hearts

**触发条件或事件外补充：**

- Enter the Saloon during open hours, when Gus is inside.
- Note: Only occurs if your friendship with Pam is at 2 hearts or more.

**Details：**

When you enter the bar, Gus will be sitting at one of the tables looking dejected. When you ask what's wrong, he'll tell you that the saloon is having hard times financially. He'll admit that at least one problem is that Pam isn't paying off her tab and he's afraid to confront her because they are friends. Pam will then enter and ask for a drink. Gus will be flustered and concede, but you will get the choice to either say:

- You need to pay your tab right now! (-50 friendship with Pam.)
- The saloon isn't doing well, financially (+15 friendship with Pam.) Pam will be somewhat upset but she will pay her tab off and Gus will give her the drink she asked for.

Your relationship with Gus will not be affected either way.

##### Five Hearts

**触发条件或事件外补充：**

- Exit the farmhouse on a non-rainy day between 6am and 11:30am.

**Details：**

Gus appears with a pot of sauce. He draws an analogy between cooking and the player's appearance in Stardew Valley, saying that adding a new ingredient may ruin the sauce or create something new and delicious. He explains that he's come to think of the player as a good friend, and says he found an old Mini-Jukebox while cleaning the Saloon . He gives the player the jukebox, and the recipe to make more.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching seven hearts with Gus, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Cranberry Sauce | Dear (Player) , Here's a recipe from my saloon. I only share this with my good friends! -Gus |

<a id="npc-event-jas"></a>

### 20. 贾斯（Jas）

> 来源：中文 revision 55188；英文 revision 193899
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 1 个事件/后续条目、1 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、0 张嵌套结果表（0 行）。

##### 8心事件

**触发条件或事件外补充：**

- 在与贾斯和 文森特 达到8颗心之后，在春季的06:00至17:00之间进入 煤矿森林 。

**详情：**

进入 煤矿森林 后 文森特 会说明如何通过清除虫子来清洁 大葱 。但贾斯坚称，将虫子从洋葱中弄出后，不应该杀死虫子。之后，玩家获得" 青葱技术 "，这使 大葱 的售价永久提高了5倍。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 1 个事件/后续条目、1 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、0 张嵌套结果表（0 行）。

##### Eight Hearts

**触发条件或事件外补充：**

- After reaching 8 hearts with both Jas and Vincent , enter Cindersap Forest during Spring on a sunny day between 6am and 5pm.

**Details：**

Vincent will explain how to clean Spring Onions by removing insects. Jas insists that the insects not be killed after removing them from the onions. Afterward, the player gains Spring Onion Mastery , which permanently increases the sell price of Spring Onions by 5x.

<a id="npc-event-jodi"></a>

### 21. 乔迪（Jodi）

> 来源：中文 revision 55067；英文 revision 191546
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、0 个列表/选择项、5 张嵌套结果表（8 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 只要与乔迪的好感度超过0点，玩家就有几率收到乔迪的信件和礼物。好感度越高，收到信件和礼物的几率越大。

**详情：**

| 物品 | 描述 |
| ------ | ------ |
| 初级肥料 （5） 高级肥料 （5） 初级保湿土壤 （5） | 亲爱的 (玩家名), 我给花园订购了太多肥料了！！我想你应该用得上。请多多保重！ -乔迪 |

##### 2心事件

**触发条件或事件外补充：**

- 玩家与乔迪关系到达2心后，就可以进入她的的房间并在床旁边的抽屉里发现一封来自她丈夫 肯特 的信。

**详情：**

信上写着：

- “ 约迪（原文如此） - 因为我很快就会回家，因此我想先告诉你几件事。 我可能和你记忆中的我有很大的不同。 我在外面看到了某些事情，让我感到十分震撼，最近我的精神一直紧绷着，无法放松。 我不想吓到你或者让你感到不安， 我只是不想让你见到我时感到震惊。 记住, 无论我在你面前表现的有多奇怪，你和孩子始终是我的一切。 我们很快会见面。 -肯特”

##### 3心事件

**触发条件或事件外补充：**

- 与乔迪好感度到达3心后，她会给玩家寄来一份食谱。

**详情：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 炸鱿鱼 | （玩家名）, 这份食谱曾帮我在烹饪比赛里赢得第一名！希望你喜欢。就算是朋友的谢礼吧！ —乔迪 |

##### 4心事件

**触发条件或事件外补充：**

- 在星期一6:00至9:30之间离开 农舍 ，玩家会发现乔迪站在门外。

**详情：**

- “*呼*…………嗨， 【玩家】!*喘息* 呼咻……真是累死了……走上来真的好累。 话说……我是来邀请你与我们共进晚餐的！ 你不用……不过如果你来的话，你能带条 大嘴鲈鱼 吗？ ……没错。那种很大的，从湖里捞出来的黏糊糊的鱼。我要用一条 大嘴鲈鱼 炖砂锅。 今晚七点在我们家……不要忘了带 大嘴鲈鱼 ！再见。”

玩家需要带一条 大嘴鲈鱼 在19:00时进入她家。

##### 7心事件

**触发条件或事件外补充：**

- 与乔迪好感度到达7心后，她会给玩家寄来一份食谱。

**详情：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 冰淇淋 | （玩家名）, 这份食谱曾帮我在烹饪比赛里赢得第一名！希望你喜欢。就算是朋友的谢礼吧！ -乔迪 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、0 个列表/选择项、5 张嵌套结果表（9 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Jodi. The chance of receiving a gift in the mail increases as your friendship with Jodi increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Basic Fertilizer (5) Quality Fertilizer (5) Basic Retaining Soil (5) | Dear (Name), I ordered too much fertilizer for the garden!! I bet you can put it to some good use. Take care! -Jodi |

##### Two Hearts

**触发条件或事件外补充：**

- When the player reaches 2 hearts, they can enter her room and find a letter from her husband Kent in the drawer next to her bed.

**Details：**

- “ / “Jodi- Since I'll be coming home soon I want to tell you a few things. I might not be the same man you remember. I've seen some things out here that have really shaken me up. I've been having a real hard time relaxing. I don't want to scare you or make you upset. I just don't want you to be shocked when I get back. Remember, no matter how I act, you and the kids mean everything to me. I'll see you soon. -Kent”

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts, Jodi will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Fried Calamari | (Player), This recipe of mine won 1st place in a cooking competition! I hope you like it. Thanks for being a friend! -Jodi |

##### Four Hearts

**触发条件或事件外补充：**

- Leave your farmhouse between 6:00am - 9:30am on a Monday to find Jodi waiting outside.

**Details：**

- “ / “*puff* ...hi (name)! *pant* Whew... that was quite a workout, walking all the way up here. Anyway... I came by to ask if you wanted to have dinner with us tonight! You don't have to... but if you decide to come, could you please bring a largemouth bass with you? ...that's right. One of those big, slimy fish from the lake. I need one for the casserole I'm making. Okay, well... it'll be at our house at around 7:00 PM tonight... don't forget the largemouth bass! Bye.”
- — Jodi

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts, Jodi sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Ice Cream | (Player), This recipe of mine won 1st place in a cooking competition! I hope you like it. Thanks for being a friend! -Jodi |

<a id="npc-event-kent"></a>

### 22. 肯特（Kent）

> 来源：中文 revision 55035；英文 revision 193910
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 4 个事件/后续条目、4 个事件外层条件或补充段落、4 张详情表、3 个列表/选择项、3 张嵌套结果表（6 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当肯特对玩家的 好感度 大于0，肯特就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 樱桃炸弹 炸弹 超级炸弹 电池组 | 你好 [玩家] 这些工具在工具箱里面积灰了。我觉得你可能会用到它们。 -肯特 |

##### 3心事件I

**触发条件或事件外补充：**

- 当肯特和 乔迪 都在家时，进入肯特的家。

**详情：**

当玩家进入乔迪和肯特的家，动画就会开始。玩家走进厨房，此时乔迪说：“嗨！我正在做爆米花。”接着，肯特叫起来并跑进厨房喊道，“那个声音......你本该知道那个声音会让我回想起战争！”乔迪停止做爆米花 ，肯特开始为他朋友的去世而感到难过。乔迪说：“但是......在你离开之前，爆米花一直都是你最喜欢吃的。”肯特回应道，“......现在不一样了。”接着，乔迪小声地询问玩家能不能对肯特说点什么。下面有三个选项：

- 这事怪乔迪……她本该知道的！ （ 好感度 -25） 肯特生气了并说，“你闭嘴！不要试图挑拨我和我老婆的关系了。”接着对乔迪道歉。
- 我知道你内心很痛苦……但这也不能怨你老婆啊。 （ 好感度 +50） 肯特会说玩家完全正确，之后会向乔迪抱歉。
- (撒谎) 这事怪我……是我要说要吃爆米花的。 （ 好感度 -50） 肯特生气了并说，“别撒谎！我最讨厌的就是谎话了！”接着对乔迪道歉。

##### 3心事件II

**触发条件或事件外补充：**

- 在与肯特达成三心后，他将在邮件中给玩家发送一份食谱。

**具体情节：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 香酥鲈鱼 | 在海外买了这个食谱，好好享受。 谢谢你让我觉得受欢迎。 -肯特 |

##### 7心事件

**触发条件或事件外补充：**

- 在与肯特达成七心后，他将在邮件中给玩家发送一份食谱。

**具体情节：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 巨无霸餐 | 在海外买了这个食谱，好好享受。 谢谢你让我觉得受欢迎。 -肯特 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个事件/后续条目、4 个事件外层条件或补充段落、4 张详情表、3 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Kent. The chance of receiving a gift in the mail increases as your friendship with Kent increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Cherry Bomb Bomb Mega Bomb Battery Pack | Hello [Player] This item was collecting dust in the toolshed. I thought you might be able to use it. -Kent |

##### Three Hearts I

**触发条件或事件外补充：**

- Enter Kent's home while he and Jodi are both there.

**Details：**

When the player enters Jodi and Kent's house, a cutscene begins and player walks into the kitchen and Jodi says, "Hi, (Player)! I'm just making some popcorn." Kent screams and runs into the kitchen exclaiming "That sound... You should've known that sound would remind me of the war!" Jodi stops the popcorn, and Kent goes on to lament the loss of his friends. Jodi says, "But, dear... popcorn was always your favorite before you left." Kent responds with, "...Things have changed." Jodi then quietly asks the player's character if they can say something to Kent. There are three choices:

- Jodi's to blame... she should've known better (-25 friendship .) Kent gets angry and says, "You keep quiet! Stop trying to turn me against my wife." Then apologizes to Jodi.
- I know you're hurting... but don't blame your wife. (+50 friendship .) Kent says the player is "absolutely right," and apologizes to Jodi.
- (Lie) Blame me... I asked for popcorn. (-50 friendship .) Kent gets angry and says, "Don't lie to me! I hate lies more than anything!" Then apologizes to Jodi.

##### Three Hearts II

**触发条件或事件外补充：**

- After reaching three hearts with Kent, he will send the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Crispy Bass | Picked up this recipe overseas. Enjoy. Want to say thanks for making me feel welcome. -Kent |

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching seven hearts with Kent, he will send the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Super Meal | Picked up this recipe overseas. Enjoy. Want to say thanks for making me feel welcome. -Kent |

<a id="npc-event-krobus"></a>

### 23. 科罗布斯（Krobus）

> 来源：中文 revision 55028；英文 revision 192255
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 2 个事件/后续条目、2 个事件外层条件或补充段落、2 张详情表、0 个列表/选择项、1 张嵌套结果表（2 行）。

##### 3心事件

**触发条件或事件外补充：**

- 当与科罗布斯达到3心后，他会通过邮件送给你一个配方。

**详情：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 深色牌子 | （玩家名），我不确定人类的信是怎么写的，所以我请 法师 帮我写了这封信。 希望你一切都好。 我想要给你看看这个...... 是我同族人制作一样东西的笔记...... -科罗布斯 |

##### 14心事件

**触发条件或事件外补充：**

- 在不下雨的20:00至01:00之间进入沙滩。

**详情：**

科罗布斯正坐在 沙滩 的码头上看水中的月光水母，此时海中出现了一只 怪物 。海怪伸出它的触手，科罗布斯跳了上去与它一起兜风。一个心形对话气泡出现在科罗布斯的头上，示意他很享受这次兜风。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 2 个事件/后续条目、2 个事件外层条件或补充段落、2 张详情表、0 个列表/选择项、1 张嵌套结果表（2 行）。

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Krobus, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Dark Sign | Player , I'm not sure how the human message system works, so I asked Wizard to help me write this letter. I hope you are doing okay. I wanted to share this with you... it's notes on how my people build a certain item. -Krobus |

##### Fourteen Hearts

**触发条件或事件外补充：**

- Enter the Beach between 8pm and 1am on a non-rainy day.

**Details：**

Krobus sits on the docks at the Beach watching Moonlight Jellies swim, when a sea monster appears. The sea monster raises its tentacles, and Krobus hops on for a ride. A heart dialogue bubble appears over Krobus' head, indicating he enjoyed the ride.

<a id="npc-event-leo"></a>

### 24. 雷欧（Leo）

> 来源：中文 revision 55053；英文 revision 192150
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 6 个事件/后续条目、6 个事件外层条件或补充段落、6 张详情表、10 个列表/选择项、2 张嵌套结果表（4 行）。

##### 2心事件

**触发条件或事件外补充：**

- 晴天的06:00至18:00之间进入 姜岛西部 。

**详情：**

玩家站在岸边，雷欧从后面出现。他会询问玩家在做什么。

- 只是在观赏海浪。 （不影响 好感度 ）
- 寻找鱼。 （不影响 好感度 ）
- 想一个特别的人。 （不影响 好感度 ）
- 思考未解之谜。 （不影响 好感度 ）

然后雷欧会询问玩家的家是什么样的。

- 是一个城镇，住满了人。 （不影响 好感度 ）
- 有森林、海滩、山脉。 （不影响 好感度 ）
- 跟这里很像，但是更冷。 （不影响 好感度 ）
- 我住在农场上。 （不影响 好感度 ）

雷欧斟酌了一会你说的话，然后问你鹈鹕镇上有没有小孩子。

- 有。 （不影响 好感度 ）
- 跟一只鸟有关系吗？ （不影响 好感度 ）

不论选择哪个答案，雷欧都会说他知道自己其实不是一只鸟。他尽量不去想这些，因为这会让他感到孤独。他试着去融入那些鹦鹉，但他知道自己不属于任何地方。 然后他逃走了， 威利 出现。

##### 3心事件

**触发条件或事件外补充：**

- 在和雷欧的好感度达到3心后，他会寄给你一份食谱。

**详情：**

| 图片 | 菜谱 | 描述 |
| ------ | ------ | ------ |
|  | 夏威夷芋泥 | （玩家名字）， 这是从我家里拿来的食物，我和我的亲属都很喜欢，希望你也能喜欢。 ——雷欧 P.S. 是威利帮我写的。 |

##### 4心事件

**触发条件或事件外补充：**

- 晴天06:00至18:00之间进入 姜岛北部

**详情：**

玩家从后面走向雷欧。雷欧像鹦鹉一样大叫，吓了玩家一跳，但这也把雷欧吓了一跳。随后雷欧道歉并解释他在语言沟通方面很困难，并询问玩家这样的他是否很奇怪。雷欧很好奇如果他没有被冲到海上，他的生活会是怎样。并想知道“正常小孩”会对他有怎样的看法。 雷欧询问玩家他是否还能再做回正常小孩。玩家回答后，他说不管怎样，能遇到这些鹦鹉还是很开心，不论如何都会把它们看作家人。雷欧感谢了玩家与他聊天，并说玩家或许也是这家庭的一分子。然后他教玩家如何用鹦鹉语说“一起玩吧”。

这个事件中的任何选项都不会影响与雷欧的好感度。

##### 6心事件

**触发条件或事件外补充：**

- 晴天06:00至18:00之间进入 姜岛南部

**详情：**

莱纳斯邀请雷欧搬到星露谷。威利说那里还有其他的孩子，雷欧想什么时候回岛上看看都可以。威利询问玩家的看法。（选项不会影响好感度）。

雷欧决定搬到星露谷。 当天晚上，鹦鹉给他在莱纳斯帐篷左侧的树上建立了树屋。

##### 7心事件

**触发条件或事件外补充：**

- 在和雷欧的好感度达到7心后，他会再寄来一份食谱。

**详情：**

| 图片 | 菜谱 | 描述 |
| ------ | ------ | ------ |
|  | 芒果糯米饭 | （玩家名字）， 这是从我家里拿来的食物，我和我的亲属都很喜欢，希望你也能喜欢。 ——雷欧 P.S. 是威利帮我写的。 |

##### 9心事件

**触发条件或事件外补充：**

- 在非雨天的06:00至19:00之间进入 深山

**详情：**

雷欧在星露谷适应得很好。他在和莱纳斯一起在篝火旁烹制豆类火锅。下一个场景里，他在与潘妮、文森特和贾斯一起在博物馆上课，并正确地回答了问题。下一个场景里，他正和威利一起钓鱼。再下一个场景，他在游乐场的树丛里看贾斯在玩耍。当贾斯注意到他时，他快速逃跑了。他回到了他的树屋里，告诉了他的鹦鹉朋友今天他过得有多好，但他还是会想念姜岛。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 6 个事件/后续条目、6 个事件外层条件或补充段落、6 张详情表、10 个列表/选择项、2 张嵌套结果表（4 行）。

##### Two Hearts

**触发条件或事件外补充：**

- Enter Island West on a sunny day between 6am and 6pm.

**Details：**

The player is standing by the shore when Leo approaches from behind. He asks what the player is doing.

- Just enjoying the waves. (No effect on friendship .)
- Looking for fish. (No effect on friendship .)
- Thinking about someone special. (No effect on friendship .)
- Pondering the big questions. (No effect on friendship .)

Leo then asks what the player's home is like.

- There's a town full of people. (No effect on friendship .)
- There's forests, beaches, and mountains. (No effect on friendship .)
- It's like here, but colder. (No effect on friendship .)
- I live on a farm. (No effect on friendship .)

Leo thinks about your words for a bit before asking if there are any kids in Pelican Town

- Yes. (No effect on friendship .)
- What does that matter to a bird? (No effect on friendship .)

Regardless of the answer, Leo says he's aware he's not really a bird, and he tries to avoid thinking about it because it makes him feel lonely. He tries to fit in with the parrots, but knows he truly doesn't belong anywhere. He runs off before Willy enters the scene, wondering if there's any way to help him.

##### Three Hearts

**触发条件或事件外补充：**

- After reaching three hearts with Leo, he sends the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Poi | (Player name), Here's a food from my home, that me and my family enjoy. Hope you like it. -Leo P.S. Willy helped me write this. |

##### Four Hearts

**触发条件或事件外补充：**

- Enter Island North on a sunny day between 6am and 6pm. This event will only happen if Leo hasn't moved to the Valley yet.

**Details：**

The player approaches Leo from behind. Leo squawks like a parrot and startles the player, which startles Leo in turn. Leo then apologizes and explains that he has difficulty communicating using words, then asks the player if they find him weird. Leo wonders about the differences in his life if he hadn't been washed ashore and wonders about what "normal kids" would have to say about him. Leo then asks the player if they think he could ever be a normal kid again. After the player answers, he states that he's happy he met the parrots regardless, and that he will always consider them family no matter what. Leo thanks the player for talking to him and says that the player may be a part of his family too, someday. He then teaches the player how to say "let's play" in parrot-talk.

Note that none of the dialogue options in this cutscene affect friendship with Leo.

##### Six Hearts

**触发条件或事件外补充：**

- Enter Island South on a sunny day between 6am and 6pm.

**Details：**

Linus invites Leo to move to the mainland of Stardew Valley. Willy says that there are other children there, and Leo can visit Ginger Island anytime he wants to. Willy asks the player what they think. (Choices have no effect on friendship).

Leo decides to move to Stardew Valley. That night, parrots build him a treehouse in the tree to the west of Linus' tent.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching seven hearts with Leo, he sends the player a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Mango Sticky Rice | (Player name), Here's a food from my home, that me and my family enjoy. Hope you like it. -Leo P.S. Willy helped me write this. |

##### Nine Hearts

**触发条件或事件外补充：**

- Enter the Mountain on a non-rainy day between 6am and 7pm.

**Details：**

Leo is shown adjusting well to life in Stardew Valley. He is seen cooking a bean hotpot with Linus on the campfire. In the next scene, he is at school at the library/museum with Penny, Vincent and Jas answering a question correctly. Another scene shows him fishing with Willy. The scene after has him watching Jas from the bushes in the playground, and running away when she notices. He arrives home at the treehouse and talks to his parrot friend about how good his day was, but he still misses Ginger Island.

<a id="npc-event-lewis"></a>

### 25. 刘易斯（Lewis）

> 来源：中文 revision 54974；英文 revision 191314
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 4 个事件/后续条目、5 个事件外层条件或补充段落、4 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 只要与刘易斯的好感度超过0点，玩家就有几率收到刘易斯的信件和礼物。好感度越高，收到信件和礼物的几率越大。

**详情：**

| 物品 | 描述 |
| ------ | ------ |
| 500 | （玩家名） , 很高兴你能加入我们的社区！我随信给你寄了一张来自星露谷农业基金的 500金支票，以资助你继续努力工作。 或许你能用它买些种子。 此致敬礼，刘易斯先生 |

##### 3心事件

**触发条件或事件外补充：**

- 与刘易斯好感度到达3心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 意大利面 | （玩家名）， 要注意健康饮食，才能有足够的体力工作！随信附上一份我最爱的配方。记着要用熟的西红柿。 -刘易斯 |

##### 6心事件

**触发条件或事件外补充：**

- 在晴天的晚上七点到十一点之间进入鹈鹕镇.
- 注意: 与 玛妮 的好感度也需要达到6心。

**详情：**

在19:00以后进入小镇，玩家会出现在刘易斯家后。刘易斯和玛妮在河边讨论要不要将他们的关系公之于众。刘易斯说这会有损他的权威，玛妮说他过于在乎自己的工作。最后，玛妮同意保守秘密。后来，玩家会突然出现并吓到两位。刘易斯问玩家有没有听到什么，玩家可以选择不同的回答。

- 是的...但是我会保密的。 （刘易斯 好感度 +50）
- 是的...我要告诉大家。 （刘易斯 好感度 -100）

如果玩家选择保守秘密，刘易斯会表达感谢。如果玩家选择要公之于众，刘易斯会哭。接下来玛妮会询问玩家为什么藏在屋后，然后玩家会直接跑开，只留下困惑的二人。

##### 7心事件

**触发条件或事件外补充：**

- 与刘易斯好感度到达7心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 帕尔玛奶酪茄子 | （玩家名）， 要注意健康饮食，才能有足够的体力工作！随信附上一份我最爱的配方。记着要用熟的西红柿。 -刘易斯 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个事件/后续条目、5 个事件外层条件或补充段落、4 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive gold in the mail from Lewis. The chance of receiving gold in the mail increases as your friendship with Lewis increases.

**Details：**

| Item | Description |
| ------ | ------ |
| data-sort-value="500"> 500g | (Name) , I'm really glad you've become part of our community! I've enclosed a 500g check from the Stardew Valley Agricultural Fund to help you continue your good work. Maybe you can buy some more seeds with it. Sincerely, Mr. Lewis |

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Lewis, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Spaghetti | (Name), Remember to eat healthy, or you won't have enough energy to work hard! I'm including one of my favorite recipes. Make sure to use ripe tomatoes! -Lewis |

##### Six Hearts

**触发条件或事件外补充：**

- On a sunny day, enter the town between 7pm and 11pm.
- Note: Only happens if Marnie is also at 6 hearts.

**Details：**

You will appear behind Lewis' house. Lewis and Marnie are talking by the river about making their romance public. Lewis says it would undermine his authority, while Marnie says he's too concerned for his job. In the end, Marnie says she'll keep their relationship a secret. Afterwards, you'll pop up and scare both Lewis and Marnie. Lewis asks you if you heard anything, and you are presented with a choice.

- Yes... but I'll keep it a secret. (+50 friendship with Lewis.)
- Yes... and I'm going to tell everyone. (-100 friendship with Lewis.)

If you choose to keep the secret, Lewis will thank you. If you say you'll tell everyone in town, Lewis will cry. Afterwards, Marnie will ask why you were behind the house, and your character will run away, leaving the two alone and confused.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts with Lewis, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Eggplant Parmesan | (Name), Remember to eat healthy, or you won't have enough energy to work hard! I'm including one of my favorite recipes. Make sure to use ripe tomatoes! -Lewis |

<a id="npc-event-linus"></a>

### 26. 莱纳斯（Linus）

> 来源：中文 revision 55042；英文 revision 193911
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 6 个事件/后续条目、6 个事件外层条件或补充段落、6 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当莱纳斯对玩家的 好感度 大于0，莱纳斯就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**细节：**

| 物品 | 信件 |
| ------ | ------ |
| 鲶鱼 大嘴鲈鱼 生鱼寿司 炸鱿鱼 生鱼片 | 你好，朋友。 最近我在山湖那里的收获不错。我想和你分享这份好运。 -莱纳斯 |

##### 0心事件

**触发条件或事件外补充：**

- 当你和莱纳斯的 友谊 达到50点时，在晴天20:00至12:00之间进入 鹈鹕镇 。（注意：无法在第一年春季7日前触发该事件）

**细节：**

乔治 会要求你赶走一些在垃圾桶偷东西吃的浣熊。你没看到浣熊，却看到了莱纳斯。他非常尴尬地解释道，如果他不吃掉这些食物，它们就会被浪费掉。然后你可以选择你对他的行为有什么看法。玩家离开后，莱纳斯会继续试图从星之果实酒吧的垃圾桶里翻东西。 格斯 发现了他，给了他一些吃的，并说他不想让任何一个村民饿肚子。

##### 3心事件

**触发条件或事件外补充：**

- 和莱纳斯的友谊达到3心后，他会寄给你一份食谱。

**细节：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 生鱼片 | (玩家名字), 你最近过的怎么样？我随信附上了我最爱的鱼料理做法。 -莱纳斯 |

##### 4心事件

**触发条件或事件外补充：**

- 在20:00到12点间来到 深山 他的 帐篷 旁边。必须是晴天或下雪。

**细节：**

莱纳斯会邀请玩家进入他的营地，对一开始表现的不信任道歉，并感谢你一直是个好朋友。然后他让玩家进入帐篷，来告诉玩家如何制作 万能鱼饵 。

##### 7心事件

**触发条件或事件外补充：**

- 和莱纳斯的好感达到7心后，他会送给玩家一个食谱。

**细节：**

| 图片 | 物品/食谱 | 描述 |
| ------ | ------ | ------ |
|  | 鱼肉卷 | (玩家名字), 你最近过的怎么样？我随信附上了我最爱的鱼料理做法。 -莱纳斯 |

##### 8心事件

**触发条件或事件外补充：**

- 在没有下雨的天气，09:00~17:00之间离开 木匠的商店 。

**细节：**

罗宾、莱纳斯和玩家会出现在 木匠的商店 门口，罗宾提出给莱纳斯做一顿午餐。莱纳斯会说：“我今天已经吃过了。”

这时，罗宾会问玩家有什么想说的。

- 我很高兴莱纳斯过得不错 （莱纳斯 好感度 +250） 莱纳斯会对玩家表示感谢，同时表示担心玩家会让他搬到玩家的 农场 生活。他会对玩家尊重他的生活方式表示感谢。
- 我想邀请莱纳斯到我的 农场 居住。 （不影响 好感度 ） 罗宾会提出给莱纳斯搭一间非常舒适的房间。莱纳斯会拒绝，并表示他非常感谢这些帮助，但是他选择继续自己的生活方式。他更想独自与和谐的自然居住。他说他珍惜和玩家的友谊。

场景会以莱纳斯去找树莓（即使是冬天）结束。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 6 个事件/后续条目、6 个事件外层条件或补充段落、6 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Linus. The chance of receiving a gift in the mail increases as your friendship with Linus increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Catfish Largemouth Bass Maki Roll Fried Calamari Sashimi | Hello, friend. The mountain lake has been kind to me lately. I'd like to share my good fortune with you. -Linus |

##### Zero Hearts

**触发条件或事件外补充：**

- After you have 50 Friendship points with Linus, enter the town between 8pm - 12am on a day that's not raining. (This event cannot trigger before Spring 7, Year 1)

**Details：**

George will ask you to scare off some raccoons who are stealing from his trash cans. Instead, you discover Linus, who is extremely embarrassed, but explains that if he didn't eat the food, it would go to waste. You then get the option to tell him what you think about his actions. Note that none of the choices will affect friendship with Linus.

After you leave, he proceeds to try to steal from the Saloon's trash can, where he is caught by Gus , who gives him a basket of zucchini fritters saying that he doesn't want any villager to go hungry.

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Linus he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Sashimi | (Name) , how are you doing? I've enclosed some instructions on how to make one of my favorite fish recipes. -Linus |

##### Four Hearts

**触发条件或事件外补充：**

- Enter the mountain area near his tent between 8pm - 12am on a day that's not raining.

**Details：**

Linus will invite you over to his camp site. He will apologize for not trusting you when you first met, and thanks you for being a good friend. He invites you into his tent, where he shows you how to craft Wild Bait for use in fishing.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching seven hearts with Linus, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Fish Taco | (Name) , how are you doing? I've enclosed some instructions on how to make one of my favorite fish recipes. -Linus |

##### Eight Hearts

**触发条件或事件外补充：**

- Exit Robin's house on a day that's not raining between 9am and 5pm.

**Details：**

Robin, Linus, and the player appear in front of Robin's house. Robin offers to make Linus lunch, but he refuses, saying "I've had great luck foraging today." Robin turns toward the player and asks if they have something to say.

- I'm just pleased that Linus is doing well... (+250 friendship with Linus.) Linus thanks the player and adds that he was worried the player would ask him to move on to the Farm . He says that he appreciates the player's respect for his chosen way of life.
- I'd like to invite Linus to live on the farm with me... (No effect on friendship .) Robin becomes excited and offers to build "a real cozy house" for Linus. Linus refuses, saying that he appreciates the kindness, but he lives the way he does by choice. He prefers to live alone, in harmony with nature. He adds that he values his friendship with the player.

The cutscene ends as Linus runs off to pick berries.

<a id="npc-event-marnie"></a>

### 27. 玛妮（Marnie）

> 来源：中文 revision 55084；英文 revision 191544
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个事件/后续条目、6 个事件外层条件或补充段落、5 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当玛妮对玩家的 好感度 大于0，玛妮就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件内容 |
| ------ | ------ |
| 干草 （30） | 亲爱的 （玩家）, 你是个好邻居，所以我想送些动物饲料给你，或许能帮得上你的忙。继续努力吧！ -瑪妮 |

##### 3心事件 I

**触发条件或事件外补充：**

- 在早上6：00~早上9：30之間，離開你的 農舍 。

**详情：**

離開 農舍 時，瑪妮會向玩家打招呼。她會告訴玩家她正在嘗試訓練她的山羊說"哈囉"，但是牠們不听话，除非瑪妮有它們最愛的食物—— 山洞蘿蔔 。瑪妮希望玩家在9 AM~5 PM之間帶一個 山洞蘿蔔 到她的牧場。當玩家帶著 山洞蘿蔔 在9 AM~5 PM進入 瑪妮的牧場 (請注意牧場營業時間)，便會出現玩家給予瑪妮蘿蔔的動畫。不管瑪妮在不在家都會觸發這個動畫。

##### 3心事件 II

**触发条件或事件外补充：**

- 達到3心之後，瑪妮會寄一個食譜給你。

**详情：**

| 圖片 | 食譜 | 描述 |
| ------ | ------ | ------ |
|  | 清湯 | 親愛的鄰居， 當我沒有在照顧動物時，我喜歡在廚房做一些料理。我們成為朋友後，我想要分享一些食譜給你。 希望你喜歡這個！ -瑪妮 |

##### 6心事件

**触发条件或事件外补充：**

- 晴天的晚上7至晚上11之间进入小镇。
- 注意：只有和 刘易斯 也达到6心才能触发。

**详情：**

7PM以后进入小镇，你会出现在刘易斯家后。刘易斯和玛妮在河边讨论要不要将他们的关系公之于众。刘易斯说这会有损他的权威，玛妮说他过于在乎自己的工作。最后，玛妮同意保守秘密。后来，你会出现并吓到两位。刘易斯问你有没有听到什么，你可以选择不同的回答。如果你选择保守秘密，刘易斯会感激你。如果你说要公之于众，刘易斯会哭。接下来玛妮会问你为什么藏在屋后，随后你会跑开，留下困惑的二人。

- 是的...但是我会保密。 （刘易斯 好感度 +50）
- 是的...我要告诉大家。 （刘易斯 好感度 -100）

##### 7心事件

**触发条件或事件外补充：**

- 達到7心之後，瑪妮會寄一個食譜給你。

**详情：**

| 图片 | 配方 | 描述 |
| ------ | ------ | ------ |
|  | 大黄派 | 亲爱的邻居， 当我没在照顾动物们的时候，我会在厨房做菜。我们已经是好朋友了，我想向你分享一些食谱。 希望你喜欢！ -玛妮 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个事件/后续条目、6 个事件外层条件或补充段落、5 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Marnie. The chance of receiving a gift in the mail increases as your friendship with Marnie increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Hay (30) | Dear (Name) , You're such a good neighbor I thought I'd send over some animal feed to make your job easier. Keep it up! -Marnie |

##### Three Hearts I

**触发条件或事件外补充：**

- Leave your farmhouse between 6am - 9:30am.

**Details：**

Marnie greets the player as they come out of the farmhouse . She will tell the player that she is trying to train her goats to say "hello" but they will not cooperate unless she has their favorite food, Cave Carrots . Marnie asks the player to bring one to her ranch between 9 AM and 5 PM. If the player enters Marnie's Ranch during that time (opening hours may contradict this) with a Cave Carrot in their inventory, a cutscene will occur with the player giving Marnie the carrot. This cutscene will trigger regardless of whether or not Marnie is home.

##### Three Hearts II

**触发条件或事件外补充：**

- After reaching 3 hearts, Marnie sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Pale Broth | Dear neighbor, when I'm not taking care of animals I like to experiment in the kitchen. Since we've become friends I want to share some recipes with you. I hope you like this! -Marnie |

##### Six Hearts

**触发条件或事件外补充：**

- On a sunny day, enter the town between 7pm and 11pm.
- Note: Only happens if Lewis is also at 6 hearts.

**Details：**

You will appear behind Lewis' house. Lewis and Marnie are talking by the river about making their romance public. Lewis says it would undermine his authority, while Marnie says he's too concerned for his job. In the end, Marnie says she'll keep their relationship a secret. Afterwards, you'll pop up and scare both Lewis and Marnie. Lewis asks you if you heard anything, and you are presented with a choice.

- Yes... but I'll keep it a secret. (+50 friendship with Lewis.)
- Yes... and I'm going to tell everyone. (-100 friendship with Lewis.)

If you choose to keep the secret, Lewis will thank you. If you say you'll tell everyone in town, Lewis will cry. Afterwards, Marnie will ask why you were behind the house, and your character will run away, leaving the two alone and confused.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts, Marnie sends you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Rhubarb Pie | Dear neighbor, when I'm not taking care of animals I like to experiment in the kitchen. Since we've become friends I want to share some recipes with you. I hope you like this! -Marnie |

<a id="npc-event-pam"></a>

### 28. 潘姆（Pam）

> 来源：中文 revision 55017；英文 revision 191550
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 4 个事件/后续条目、5 个事件外层条件或补充段落、4 张详情表、0 个列表/选择项、3 张嵌套结果表（6 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当潘姆对玩家的 好感度 大于0，潘姆就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件内容 |
| ------ | ------ |
| 电池组 啤酒 能量滋补水 | 嘿。 我在抽屉里找到了这个。我想你可能用得着。 -潘姆 |

##### 3心事件

**触发条件或事件外补充：**

- 与潘姆好感度到达3心后，她将通过信件赠送一份食谱。

**详情：**

| 图片 | 食谱 | 信件内容 |
| ------ | ------ | ------ |
|  | 乳酪花椰菜 | 孩子你好， 这是我老爸常做的一道小菜的配方。要小火慢炖才行。 -潘姆 |

##### 7心事件

**触发条件或事件外补充：**

- 与潘姆好感度到达7心后，她将通过信件赠送一份食谱。

**详情：**

| 图片 | 食谱 | 信件内容 |
| ------ | ------ | ------ |
|  | 塞料面包 | 孩子你好， 这是我老爸常做的一道小菜的配方。要小火慢炖才行。 -潘姆 |

##### 9心事件

**触发条件或事件外补充：**

- 在 木匠的商店 购入“社区升级”，待完成后四日，且与潘姆达到9心后到访她家。与她是否在家无关（因为如果公交修复，她几乎总是不在家的）。
- 船标之后会出现在新房子二楼的餐桌右边，玩家可以使用工具敲击获得。

**详情：**

她正在船标前祈祷。她为无法戒酒而忏悔。她希望神能帮助她戒酒。

我很高兴你又有了希望。 （不影响 好感度 ）

她表示在晚年终于高兴了一回。

很抱歉，但神并不存在…… （ 好感度 -1000）

她说你侮辱了她的信仰，把你赶走了。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 4 个事件/后续条目、5 个事件外层条件或补充段落、4 张详情表、2 个列表/选择项、3 张嵌套结果表（6 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Pam. The chance of receiving a gift in the mail increases as your friendship with Pam increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Battery Pack Beer Energy Tonic | Hey. I found this in a drawer somewhere. Thought you could use it. -Pam |

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Pam, she will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Cheese Cauliflower | Hey Kid, Here's the recipe for a little treat my pappy used to make. Cook it slow. -Pam |

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts with Pam, she will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Stuffing | Hey Kid, Here's the recipe for a little treat my pappy used to make. Cook it slow. -Pam |

##### Nine Hearts

**触发条件或事件外补充：**

- Purchase the " Community Upgrade " from the Carpenter's Shop. After earning 9 hearts of friendship with Pam, enter Pam's house at least 4 days after the Community Upgrade is completed.
- Trivia: The Yoba statue can be found later near Pam's bed on the second floor of the house, and can be removed and obtained by the player by striking it with a tool .

**Details：**

You find Pam praying before a Sign of the Vessel statue. She confesses that she loves the new house, but hasn't been able to cut back on her drinking. She says she thought the new house would change everything, but it didn't, so she ordered the statue. She then turns to the player for a response.

- I'm glad you're feeling hopeful (No effect on friendship .)

Pam says she's "getting sappy" in her old age, and the cutscene ends.

- Sorry Pam, but Yoba isn't real... (-1000 friendship .)

Pam becomes angry and asks "What in the void is wrong with you?" before declaring her faith in Yoba and ordering you to leave.

<a id="npc-event-pierre"></a>

### 29. 皮埃尔（Pierre）

> 来源：中文 revision 55086；英文 revision 192883
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 3 个事件/后续条目、4 个事件外层条件或补充段落、3 张详情表、2 个列表/选择项、2 张嵌套结果表（4 行）。

##### 返利计划

**触发条件或事件外补充：**

- 只要皮埃尔对玩家的 好感度 大于0，皮埃尔就有可能通过 信件 送给玩家一些 金币 。好感度越高，收到信件的可能性越大。
- 注意： “股份信息”原文为 Sorry for the stock message 。这个短语通常用于电子邮件或短信中，表示发送方发送了一条标准的、通用的信息（比如群发的新年祝福），而不是针对接收方的个性化信息。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 250 （或更多） | 尊敬的客户, 感谢您对皮埃尔商店的惠顾！随信附上“返利计划”的退款。祝好！ -皮埃尔 附: 股份信息给您带来诸多不便 ，还请谅解 ，[玩家名]。祝您生活愉快！ |

##### 3心事件

**触发条件或事件外补充：**

- 在皮埃尔的好感度到达3颗心后，他会在邮件中给你一个食谱。

**细节：**

| 图片 | 菜谱 | 描述 |
| ------ | ------ | ------ |
|  | 蓝莓千层酥 | 最高机密： 这是我著名的蓝莓挞配方。别告诉任何人哦！我之所以把它给你，是因为你是我的好朋友。 -皮埃尔 |

##### 6心事件

**触发条件或事件外补充：**

- 进入 皮埃尔的杂货店 后会触发一个过场动画。

**详情：**

你进入皮埃尔的卧室。环顾四周后，发现皮埃尔在书架背后的“秘密藏书”。皮埃尔发现了你，要求你发誓不会告诉任何人。如果你同意什么都不说，他也会答应不告诉任何人你在他的卧室里窥探的事。如果你拒绝，他的好感度会减2颗心。

- 我会为你保守秘密的。 （ 好感度 +70） 他会回答：“谢谢你，感激不尽。你就当作没看见，好吗？而我也会忘记你随便进出我房间的事！”
- 这事儿应该让你太太知道 （ 好感度 -500） 他会回答：“你真的要那样对我？你真卑鄙。你本就不该随便进出我的房间！八卦的邻居什么的最讨厌了。”

皮埃尔嘟囔着说，这下又得找个新的藏匿点了。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 3 个事件/后续条目、3 个事件外层条件或补充段落、3 张详情表、2 个列表/选择项、2 张嵌套结果表（4 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive gold in the mail from Pierre. The chance of receiving gold in the mail increases as your friendship with Pierre increases.

**Details：**

| Item | Description |
| ------ | ------ |
| data-sort-value="250"> 250g (or more) | Dear valued customer, Thanks for visiting 'Pierre's'! Enclosed is your 'Cash-back Rewards Program' rebate. See you soon! -Pierre P.S. Sorry for the stock message, (Name) . Enjoy! |

##### Three Hearts

**触发条件或事件外补充：**

- After reaching 3 hearts with Pierre, he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Blueberry Tart | TOP SECRET : Here's the recipe for my famous blueberry tart. Don't tell anyone! I'm giving it to you because we are such good friends. -Pierre |

##### Six Hearts

**触发条件或事件外补充：**

- Enter Pierre's General Store to trigger the cutscene.

**Details：**

You enter Pierre's bedroom. After looking around, you find Pierre's 'secret stash' behind the bookshelf. Pierre catches you, asks that you tell no one.

- "Your secret is safe with me." (+70 friendship .) He responds, "Thanks, I appreciate that. Just forget you ever saw this, okay?...And I'll just forget that you were snooping around in my bedroom!"
- "Your wife deserves to know about this." (-500 friendship .) He responds, "You would really do that to me? You're terrible. You shouldn't have been snooping around in my bedroom in the first place! Nosy neighbors are the worst."

Pierre says he has to find a new hiding spot.

<a id="npc-event-robin"></a>

### 30. 罗宾（Robin）

> 来源：中文 revision 55090；英文 revision 191769
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 3 个事件/后续条目、3 个事件外层条件或补充段落、3 张详情表、0 个列表/选择项、2 张嵌套结果表（4 行）。

##### 邮寄礼物

**触发条件或事件外补充：**

- 当罗宾对玩家的 好感度 大于0，罗宾就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 木材 （50） | 嘿，你好！ 我这儿还有些剩余的木头……你或许用得着。请多多保重！ -罗宾 |

##### 6心事件

**触发条件或事件外补充：**

- 当罗宾在家的时候，可以进入罗宾的房间。

**详情：**

你看到罗宾正在清理她的锯上的灰尘。她问你是否用木头做过什么东西，你可以回答“是”或“不”，然后她说：“我想我们已经成了好朋友了，我可以用木工的秘密来信任你了！”并给你两个蓝图——鼓块和长笛块。她说，用你自己做的东西来装饰你的房子感觉不错。

##### 7心事件

**触发条件或事件外补充：**

- 在与 罗宾 达到7心后，她将通过邮件送给玩家一份菜谱。同时，她也开始送礼物给玩家。

**具体情节：**

| 图片 | 物品/ 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 南瓜汤 | 这是一份古老的菜谱，是我的祖母传给我的。希望你喜欢！ -罗宾 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 3 个事件/后续条目、3 个事件外层条件或补充段落、3 张详情表、2 个列表/选择项、2 张嵌套结果表（4 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Robin. The chance of receiving a gift in the mail increases as your friendship with Robin increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Wood (50) | Hey there! I had some extra wood lying around... I thought maybe you could use it. Take care! -Robin |

##### Six Hearts

**触发条件或事件外补充：**

- Enter Robin's house while she is home.

**Details：**

You find Robin cleaning the dust off her saw. She asks if you've ever made anything out of wood:

- "Yes" (+50 friendship .)
- "No" (+50 friendship .)

She says "I think we've become good enough friends that I can trust you with my carpentry secrets!" and gives you two blueprints — the Drum Block and the Flute Block . She says it feels good to decorate your house with things you've made yourself.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching 7 hearts with Robin she will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Pumpkin Soup | Here is an old recipe that my grandma passed down to me. Enjoy! -Robin |

<a id="npc-event-sandy"></a>

### 31. 桑迪（Sandy）

> 来源：中文 revision 55081；英文 revision 191345
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 2 个事件/后续条目、2 个事件外层条件或补充段落、2 张详情表、0 个列表/选择项、2 张嵌套结果表（4 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 当桑迪对玩家的 好感度 大于0，桑迪就有可能会给玩家邮寄一份礼物。好感度越高，收到礼物的可能性越大。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 仙人掌果子 椰子 椰汁汤 | 这是来自卡利科沙漠的问候！ 赶紧来看看我吧，我在这儿好无聊：（随信附上一份来自沙漠的礼物。你可以亲自来向我道谢！ -桑迪 |

##### 7心事件

**触发条件或事件外补充：**

- 与桑迪的好感度到达7心后，她会通过邮件赠送玩家一份食谱。

**详细：**

| 图片 | 食谱 | 信件 |
| ------ | ------ | ------ |
|  | 椰汁汤 | 亲爱的[玩家名字]， 我在沙漠里好无聊，所以给你写了这封信。随信附上一种靓汤的配方。赶紧来看看我吧！ -桑迪 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 2 个事件/后续条目、2 个事件外层条件或补充段落、2 张详情表、0 个列表/选择项、2 张嵌套结果表（4 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from Sandy. The chance of receiving a gift in the mail increases as your friendship with Sandy increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Cactus Fruit Coconut Tom Kha Soup | Greetings from Calico Desert! Come visit me soon, I'm really bored out here :(. I've included a gift from the desert. You can come and thank me in person! -Sandy |

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching seven hearts with Sandy, she will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Tom Kha Soup | Dear (Name), I was so bored out here in the desert that I wrote you a letter. There's a recipe for a delicious soup enclosed. Come visit me soon! -Sandy |

<a id="npc-event-vincent"></a>

### 32. 文森特（Vincent）

> 来源：中文 revision 55079；英文 revision 193876
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 1 个事件/后续条目、1 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、0 张嵌套结果表（0 行）。

##### 8心事件

**触发条件或事件外补充：**

- 与文森特和 贾斯 都到8心后，在 春季 晴朗的白天进入 煤矿森林 。

**详情：**

文森特传授清洁 大葱 的方法。此后玩家获得 青葱技术 ，永久将大葱售价增加五倍。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 1 个事件/后续条目、1 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、0 张嵌套结果表（0 行）。

##### Eight Hearts

**触发条件或事件外补充：**

- After reaching 8 hearts with both Vincent and Jas , enter Cindersap Forest during Spring on a sunny day between 6am and 5pm.

**Details：**

Vincent will explain how to clean Spring Onions by removing insects. Afterward, the player gains Spring Onion Mastery , which permanently increases the sell price of Spring Onions by 5x.

<a id="npc-event-willy"></a>

### 33. 威利（Willy）

> 来源：中文 revision 55075；英文 revision 192689
>
> 结构判定：中英文事件数及深层段落/列表/表格指标一致；两源仍完整并列

#### 中文记录源（完整保留）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、0 个列表/选择项、4 张嵌套结果表（8 行）。

##### 3心事件

**触发条件或事件外补充：**

- 与威利好感度到达3心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 海鲜杂烩汤 | 我想分享爸爸曾经发明的一道菜肴。其中的精髓就在于鱼要百分百新鲜！ -威利 |

##### 5心事件

**触发条件或事件外补充：**

- 与威利好感度到达5心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 法式田螺 | 我想分享爸爸曾经发明的一道菜肴。其中的精髓就在于鱼要百分百新鲜！ -威利 |

##### 6心事件

**触发条件或事件外补充：**

- 在6:00到17:10之間進入 沙滩 。

**详情：**

威利在 鱼店 外看到你时如释重负，说他需要你的帮助，并让你进去看看具体情况。进入鱼店之后，你会看到许多 螃蟹 在地板上到处乱跑。但你还没来得及帮忙， 格斯 便进入了鱼店。他提出要买下所有的螃蟹，但因为得花些额外的工夫抓住这些螃蟹，价格要打点折扣。威利同意后，众人一起抓住了这些螃蟹。随后，威利向他的“甜心美人们”道别。而格斯却悄悄告诉你接下来几天他会在 酒吧 里做点特别的蟹肉饼。

事件发生后的当天， 刘易斯 会说自己一整天一直都闻到新鲜螃蟹的味道。

此外，自事件发生后的当天起，格斯将在 星之果实酒吧 以 550 的单价无限量出售 蟹黄糕 （ 速度 （+1） 防御 （+1） ），一共持续三天。

##### 7心事件

**触发条件或事件外补充：**

- 与威利好感度到达7心后，他会给玩家寄来一份食谱。

**详情：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 烩鱼汤 | 我想分享爸爸曾经发明的一道菜肴。其中的精髓就在于鱼要百分百新鲜！ -威利 |

##### 9心事件

**触发条件或事件外补充：**

- 与威利好感度到达9心后，他会给玩家寄来一份食谱。

**具体情节：**

| 图片 | 食谱 | 描述 |
| ------ | ------ | ------ |
|  | 龙虾浓汤 | 我想分享爸爸曾经发明的一道菜肴。其中的精髓就在于鱼要百分百新鲜！ -威利 |

#### 英文完整性主源（PC v1.6.15 判定基准）

> 5 个事件/后续条目、5 个事件外层条件或补充段落、5 张详情表、0 个列表/选择项、4 张嵌套结果表（8 行）。

##### Three Hearts

**触发条件或事件外补充：**

- After reaching three hearts with Willy he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Chowder | I'd like to share an ol' cooking recipe my pappy used to make. It's important the fish is FRESH. -Willy |

##### Five Hearts

**触发条件或事件外补充：**

- After reaching five hearts with Willy he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Escargot | I'd like to share an ol' cooking recipe my pappy used to make. It's important the fish is FRESH. -Willy |

##### Six Hearts

**触发条件或事件外补充：**

- Enter The Beach between 6am and 5:10pm.

**Details：**

Willy greets you outside the Fish Shop . He says he needs your help and asks you to come inside. Once inside, you see Crabs run amok, covering the Fish Shop floor. Before you can do anything to help, Gus enters the Fish Shop and offers to purchase all the crabs, minus a discount for the labor involved. Willy agrees, and Gus gathers the crabs. Afterward, Gus turns to you and says he's going to run a special on Crab Cakes for the next few days (but not to tell Willy). The cutscene ends with Willy saying goodbye to his "sweet ladies" as they are taken away to be killed and cooked.

Gus will sell an unlimited amount of Crab Cakes at the Saloon for data-sort-value="550"> 550g each starting on the day of the cutscene and for 3 days after. Mayor Lewis will comment that he's smelled crab "all afternoon" the day the event is viewed.

##### Seven Hearts

**触发条件或事件外补充：**

- After reaching seven hearts with Willy he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Fish Stew | I'd like to share an ol' cooking recipe my pappy used to make. It's important the fish is FRESH. -Willy |

##### Nine Hearts

**触发条件或事件外补充：**

- After reaching nine hearts with Willy he will send you a recipe in the mail.

**Details：**

| Image | Recipe | Description |
| ------ | ------ | ------ |
|  | Lobster Bisque | I'd like to share an ol' cooking recipe my pappy used to make. It's important the fish is FRESH. -Willy |

<a id="npc-event-wizard"></a>

### 34. 法师（Wizard）

> 来源：中文 revision 55012；英文 revision 193912
>
> 结构判定：事件数一致，深层段落/列表/表格结构差异已审计；两源完整并列，行为判断以英文主源为准

#### 中文记录源（完整保留）

> 2 个事件/后续条目、3 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、1 张嵌套结果表（2 行）。

##### 任意好感度

**触发条件或事件外补充：**

- 当玩家与法师的 友谊 值大于0时，法师就有可能通过 信件 送给玩家一份礼物。玩家与法师的 友谊 值越高，收到礼物概率就越高。
- 法师会使用一种 特殊的信纸 。

**详情：**

| 物品 | 信件 |
| ------ | ------ |
| 火水晶 泪晶 翡翠 紫蘑菇 | 你好，年轻的术士。 我在包裹里装了一只神器。请谨慎使用。 -法师M·拉斯莫迪斯 |

##### 4心事件

**触发条件或事件外补充：**

- 玩家能够进入 法师塔 的地下室。在地下室中与 幻觉神龛 互动可以用 500 重新设定人物形象。

#### 英文完整性主源（PC v1.6.15 判定基准）

> 2 个事件/后续条目、2 个事件外层条件或补充段落、1 张详情表、0 个列表/选择项、1 张嵌套结果表（2 行）。

##### Anytime

**触发条件或事件外补充：**

- At any friendship level greater than zero friendship points, you may receive a gift in the mail from the Wizard. The chance of receiving a gift in the mail increases as your friendship with the Wizard increases.

**Details：**

| Item | Description |
| ------ | ------ |
| Fire Quartz Frozen Tear Jade Purple Mushroom | Greetings, young adept. I have enclosed in this package an item of arcane significance. Use it wisely. -M. Rasmodius, Wizard |

##### Four Hearts

**触发条件或事件外补充：**

- Players gain access to the basement of the Wizard's Tower , where they can change their character's appearance at The Shrine of Illusions for data-sort-value="500"> 500g .

## 来源与审计方法

- [Villagers — 官方 34 位可送礼居民名册](https://stardewvalleywiki.com/Villagers)
- [Modding:Event data — 事件触发条件、已看事件、友情点与后果命令](https://stardewvalleywiki.com/Modding:Event_data)
- 每位居民的中英文固定 revision 链接见索引表。
- 生成器要求 34/34 人存在事件章节、178/178 个事件标题和 175/175 张详情表；富文本转换还逐表验证可见文本 token 顺序不丢失。
- 任何居民缺页、缺事件章节、空事件块、未知表型、标题/详情数量漂移，或深层差异居民集合偏离已审计基线，都会使生成失败。

---

[上一篇：NPC日程数据总览](./NPC日程数据总览.md) · [返回NPC数据总览](./NPC数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：作物数据总览](./作物数据总览.md)
