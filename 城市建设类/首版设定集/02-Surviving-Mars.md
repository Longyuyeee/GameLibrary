# 火星求生（Surviving Mars）｜GameDocs 城市建设档案

> **首版，未通过 v2.9 全量验收。** 以 Haemimont Games 开发、Paradox Interactive 发行的 2018 年 PC 原版为对象。以 2018 年 9 月 26 日 **Sagan 免费更新**作为灾害、仓储与电网规则的明示基线，发售前日志只用来说明设计目标。2019 年 Green Planet / Armstrong 和后来的 Surviving Mars: Relaunched 另列，不并入基线。没有执行游戏或读取具体存档。[原版发售公告](https://www.paradoxinteractive.com/media/press-releases/press-release/paradox-and-haemimont-start-six-week-countdown-to-surviving-mars) · [Sagan 公告归档](https://store.steampowered.com/news/posts/?appids=464920&enddate=1541428350&feed=steam_community_announcements)

## 一、核心循环：先把需求做出来，再把人接过来

开局通过地球赞助获得资金与补给，建起无人施工体系；机器人能准备设施，但较复杂的生产、地下矿产开采和科研需要居民。联系地球与培养本地供应同时存在，区别不是简单的产量大小：地球补给有外部依赖，火星本地闭环又要求先投入基建和人力。开发者把无人阶段明确定位为给首批定居者铺路，而不是把自动化阶段当成殖民目标本身。[Paradox 原版介绍](https://www.paradoxinteractive.com/media/press-releases/paradox-interactive/surviving-mars-touches-down-on-the-mac-app-store) · [2017 开发日志《Dome, Sweet Dome!》](https://store.steampowered.com/news/posts/?appids=464920&enddate=1513858705)

| 阶段 | 要接通的流 | 推进信号 | 未达标时的结果（设计分析） |
| --- | --- | --- | --- |
| 部署 | 地球补给 → 登陆点 → 无人机工作区 | 建材已运抵作业点，非全图总量看似足够 | 工具有但送不到，建设、维修和防灾会一起卡住 |
| 预运营 | 电网、氧和水的管网、储备与食物 | 在接人前，生命保障可操作并能应付正常波动 | 有穹顶不等于有宜居区域，首次入住会暴露此前被掩盖的断点 |
| 首批居民 | 住房、岗位、生活条件和服务 | 有人住、有可用岗位，维持食物、供电、水和氧 | 缺居民，高级资源/研究无力展开；过早增员又扩大供给缺口 |
| 扩张 | 研究与建造、多个局部物流区、地球或本地补给 | 一处设施维护停机时，人口仍可获取必要资源 | 总量增长不能弥补配给和维修无法到场 |
| 转向自给 | 用本地设施替代部分外来采购 | 按物资逐项记录进口频率和维护需求 | “不进口”不是定义良好的总量指标，可能只是把消耗转嫁给储备 |

## 二、基础系统：看得到产量，也要看得到连通

| 层 | 事实及版本 | 可借鉴的排障方法 |
| --- | --- | --- |
| 电 | Sagan 允许相邻生产/消耗设施直接相连而不用电缆；同一更新明示尘暴关闭太阳能板。 | 先区分发电不足与某段网络失联；保留非太阳能支撑，不能把正常日的峰值当作灾时下限。 |
| 水和氧 | Haemimont 发布的原版游戏内百科说明两者共用管线系统；MOXIE 从大气取氧，水汽收集器与 MOXIE 在尘暴中失效。 | 为不同失效类别保留可用储备与联通途径；不能把两台同类设施视为应对同一灾害的独立冗余。 |
| 无人机 | Sagan 可为仓库设置目标库存，无人机尝试调拨到该目标；建造位置不在无人机指挥覆盖时，建造提示会标出风险。 | 检查故障位置附近是否真的有维修材料及可达无人机；需要目标库存，不是只需要一座仓库。 |
| 居民 | 早期原版设计日志将高级生产、矿业及科研列为人类岗位；不能只依赖无人阶段的成功来预判人口阶段。 | 看各穹顶是否兼有住房、岗位、补给与服务，而不只优化单栋建筑产出。 |
| 其他灾害 | Sagan 公告将电缆故障/管线泄漏与尘暴、尘卷风及陨石撞击联系；低温对停电设施另有风险。 | 先写清灾种再比较；不要在所有地图固定采用同一个停机时长。 |

来源：[Sagan 开发与更新公告](https://store.steampowered.com/news/posts/?appgroupname=Surviving+Mars%3A+First+Colony+Edition&appids=464920%2C801710%2C802700&enddate=1538676641&feed=steam_community_announcements) · [开发商公布的原版百科源文件](https://github.com/HaemimontGames/SurvivingMars/blob/master/Data/EncyclopediaArticle.lua) · [早期居民开发日志](https://store.steampowered.com/news/posts/?appids=464920&enddate=1513858705)。百科是开发商存档的原版资料，并非 Sagan 二进制快照，因此对照使用，不从该文件的主分支反推 Sagan 的建筑参数。

## 三、演练：尘暴如何让两个“丰收”指标一起失效

**构造案例，不是实机结果：** 某穹顶平日由太阳能和储能供电，主要靠 MOXIE 供氧、水汽收集器供水，维修库存设在远端。这是多路基础负载共用少数故障点的布局；正常日有电有水，不代表可以安全招募更多人口。下面的演练应用 Sagan 公告的太阳能停机与电网损坏条件，并用开发商原版百科识别氧水设施、穿梭机等并发变化，不将任何假设容量写成游戏参数。

| 时段 | 应主动观察 | 依次验证的动作 |
| --- | --- | --- |
| 灾前 | 电、水、氧、食物的独立储备；穹顶端有没有及时收到 | 先记录地图、赞助方与种子、已启用的游戏规则、各种设施和连接；截图定位储备实际所在网络 |
| 中断第一段 | 太阳能关闭时，储能与非太阳能发电实际支撑哪些用电端 | 保持居民负载可控；若某段供给归零，区分储备耗尽与路径失联 |
| 中断持续 | 发生氧/水减少时看本地储备与管线维护，确认维修物资是否在指挥覆盖 | 保护通向穹顶的优先路径；避免只检查生产建筑的标称能力 |
| 灾后 | 设施陆续恢复、库存低位与积压维护任务是否迅速消化 | 记录从事故首次可见到供给恢复的窗口；补回储备后再解除扩张限制 |

**复盘计算法。** 对每类可消耗物资，若净消耗 U－P 大于零，在纯算术假设下估算储备 R 能支撑 R／(U－P) 个记录时间单位；这里的 R 只计算穹顶可实际取得的储备，P 是灾中实际到达量。若 U－P 不大于零，不能用该公式推断能无限撑住，因为仍可能断电、断管、维护或物流受阻。无需假定具体储罐容量。指标用作同一存档两种布局的对照，不直接换算任何地图的致死时钟。[Sagan 灾害规则](https://store.steampowered.com/news/posts/?appgroupname=Surviving+Mars%3A+First+Colony+Edition&appids=464920%2C801710%2C802700&enddate=1538676641&feed=steam_community_announcements) · [原版百科中的尘暴条目](https://github.com/HaemimontGames/SurvivingMars/blob/master/Data/EncyclopediaArticle.lua)

**设计对照。** 方案 A 给同一种发电方式新增设备，只提高平时余量；方案 B 为灾时保留不同工作原理的电源，并将可用维修物资移入需要它的指挥范围。复盘用相同灾种与同一居民数比较最低储备、停机时间和恢复量，避免因为案例规模不同而误把多建当作冗余。

## 四、版本隔离：哪些功能是后来的

| 内容 | 可确认来源 | 本档归类 |
| --- | --- | --- |
| 原版发行与早期免费补丁 | 2018 年发行；Sagan 明示补给库存目标与多项灾害变更。 | 原版可复盘基线，不能标成首发全有。 |
| Green Planet 扩展、Armstrong 免费更新 | 2019 年官方公告把大气、温度、水和植被四项改造参数放在 Green Planet；同公告另列全体原版玩家可下载的 Armstrong 更新。 | 不用四项改造参数衡量原版 Sagan 生存期。 |
| Relaunched | 官方把 Martian Assembly 定位为原版没有的新残局挑战，法律、独立及翻新的列车整合均按该产品归属。 | 议会及独立不倒灌至 2018 原版；不假定现行稳定版的研究与服务逻辑等于原版。 |

来源：[原版 Sagan 公告](https://store.steampowered.com/news/posts/?appids=464920&enddate=1541428350&feed=steam_community_announcements) · [Green Planet 与 Armstrong 官方发布稿](https://www.paradoxinteractive.com/media/press-releases/paradox-interactive/surviving-mars-green-planet-and-project-laika-now-available) · [Relaunched 官方介绍](https://www.paradoxinteractive.com/games/surviving-mars-relaunched/about)。

## 五、横向比较与后续核查

- 对照 [Frostpunk](https://store.steampowered.com/app/323190/Frostpunk/)：两者将安全基础设施视作持续开销；Frostpunk 商品页强调热源和社会法令，火星求生原版的特点是电、水、氧与有覆盖边界的机器人维护网络，需要分层排故而不是把所有危险化为同一个温度指标。
- 对照 [Tropico 6](https://www.kalypsomedia.com/product-page/tropico-6)：两者都依赖一次次外部往来，但火星求生的补给行为服务临时建材和生存需求，不能像岛屿经济那样用选举和长期贸易谈判替代断供后的实体储备。
- 首版未验收全部赞助方、神秘事件、难度与地图组合、维护精确周期、矿藏精确产出、穹顶容量和地产售价。下一轮应在可明确识别的 Sagan 存档各观察一场晴转尘暴与其他灾种；给设备、储备、连通、事故时间逐项截证，再按 DLC 或新版分表。
