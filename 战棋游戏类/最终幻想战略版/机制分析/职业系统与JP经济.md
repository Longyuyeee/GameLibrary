# 职业系统与JP经济 — 最终幻想战略版 (FFT)

> 游戏版本: FFT (PS1, 1997) / War of the Lions (PSP, 2007) | 数据来源: [松野泰己1997开发者访谈](https://web.archive.org/web/20160607155523/http://shmuplations.com/fft/), [FFT Wikia](https://finalfantasy.fandom.com/wiki/Final_Fantasy_Tactics), [IGN Job Guide](https://s.ign.com/wikis/final-fantasy-tactics-the-ivalice-chronicles/All_Jobs_and_Requirements_in_Final_Fantasy_Tactics), [GameFAQs JP系统详解](https://gamefaqs.gamespot.com/ps/197339-final-fantasy-tactics/faqs/82197)

## 一、JP系统——战棋品类最具深度的技能经济

FFT的职业系统核心是**JP(Job Points)**——一种独立的、与经验值(EXP)分离的"学习货币"。这是FFT对SRPG品类最大的设计贡献。

### 1.1 JP获取

| 来源 | JP量 | 说明 |
|------|:--:|------|
| **战斗中执行行动** | 基础JP (~10-30) | 任何成功的行动——攻击/技能/道具使用 |
| **JP Spillover（溢出）** | 队友JP的约25% | 自动获得——意为你需要此职业的JP但从未转过此职业 |
| **JP Boost（支援技能）** | ×1.5 | 侍从250JP习得——必学技能 |
| **派遣任务(Errands)** | 少量 | 第2章起可用 |
| **Focus（侍从技能）** | 每次+10JP | 无限使用——最安全的JP刷取方法 |

### 1.2 JP经济设计分析

每个职业有独立的JP池——战骑的JP不能用于学习白魔法的技能。但JP Spillover创造了"跨职业渗透"效应：如果你在战斗中使用战士，这些JP会**溢出**到你从未转过职的其他职业中。

松野设计JP系统的核心理念：
- **有限资源迫使选择**：你不能买下所有技能——早期必须优先选择重要的
- **Spillover作为"软解锁"**：不需要专门刷每个职业——战斗自然培养跨职业技能
- Focus是一个有意识的设计——一个永不失败、永远给JP的技能，被社区用作"JP刷取工具"。这不是漏洞——松野知道这会被这样使用

**与风花雪月技能系统的对比**：

| 维度 | FFT JP系统 | 风花雪月 |
|------|------|------|
| 学习货币 | JP——每种职业独立 | 角色属性+技能等级（统一） |
| 技能继承 | 学过的技能=永远拥用（跨职业装备） | 精通后的能力=可装备 |
| 获取方式 | 战斗中施放行动 | 授课（周间自动）+战斗 |
| 刷取可能 | 是——Focus无限刷 | 是——自由出击无限刷 |
| 技能槽 | 4槽（主+副+反应+支援+移动） | 5槽+1独特 |

## 二、22职业双树——战棋品类最深职业体系

FFT的20个通用职业+2个隐藏职业从两个起点（侍从/道具士）分为物理树和魔法树。

### 2.1 物理职业树（侍从→）

| 层 | 职业 | 解锁条件 | 核心价值 |
|:--:|------|------|------|
| **T1** | 侍从 (Squire) | 初始 | Focus（刷JP）、JP Boost、Move+1 |
| **T2** | 骑士 (Knight) | 侍从 Lv2 | 武器破坏/防具破坏——装备破坏即战术封锁 |
| **T2** | 弓箭手 (Archer) | 侍从 Lv2 | 蓄力(Charge)——远程狙击 |
| **T3** | 僧侣 (Monk) | 骑士 Lv3 | HP恢复(Chakra)、复活(Revive)——战士+奶妈合体 |
| **T3** | 盗贼 (Thief) | 弓箭手 Lv3 | 偷心(Steal Heart)、偷武器——招募+缴械 |
| **T4** | 风水士 (Geomancer) | 僧侣 Lv4 | 地形攻击(Elemental)——零消耗元素技 |
| **T4** | 龙骑士 (Dragoon) | 盗贼 Lv4 | Jump——飞行高度攻击、脱离地面回避 |
| **T5** | 侍(Samurai) | 骑士Lv4+僧侣Lv5+龙骑士Lv2 | 刀术(Iaidou)——范围/破防/石化解 |
| **T5** | 忍者 (Ninja) | 弓箭手Lv4+盗贼Lv5+风水士Lv2 | **Dual Wield（二刀流）——最强支援技能**、投掷 |
| **T5** | 舞者 (Dancer) ♀ | 风水士Lv5+龙骑士Lv5 | 范围Debuff/异常（女限定） |

### 2.2 魔法职业树（道具士→）

| 层 | 职业 | 解锁条件 | 核心价值 |
|:--:|------|------|------|
| **T1** | 道具士 (Chemist) | 初始 | 道具使用、Auto-Potion、Move-Find Item |
| **T2** | 白魔道士 (White Mage) | 道具士 Lv2 | 治疗/复活/Protect/Shell |
| **T2** | 黑魔道士 (Black Mage) | 道具士 Lv2 | Fire/Blizzard/Thunder三系 |
| **T3** | 时魔道士 (Time Mage) | 黑魔道士 Lv3 | Haste/Slow/Stop/**Teleport（瞬间传送）** |
| **T3** | 阴阳士 (Mystic) | 白魔道士 Lv3 | 阴阳术——Brave/Faith操作 |
| **T4** | 召唤士 (Summoner) | 时魔道士 Lv3 | 全屏大范围魔法——最强AOE |
| **T5** | 话术士 (Orator) | 阴阳士 Lv3 | Invite(劝说加入)/Praise/Preach——战中人形招募 |
| **T5** | 诗人 (Bard) ♂ | 召唤士Lv5+话术士Lv5 | 范围Buff/治疗（男限定） |
| **T5** | **算术士 (Arithmetician)** | 白魔Lv5+黑魔Lv5+时魔Lv4+阴阳Lv4 | **0 CT魔法——无视距离+无消耗——全地图范围**——游戏最强/最慢职业 |

### 2.3 隐藏职业

| 职业 | 解锁条件 | 特点 |
|------|------|------|
| **模仿士 (Mime)** | 侍从Lv8+道具士Lv8+召唤士Lv5+话术士Lv5+风水士Lv5+龙骑士Lv5 | 无自带技能——完全模仿队友行动 |

### 2.4 独有剧情职业

| 职业 | 角色 | 定位 |
|------|------|------|
| **Gallant Knight** | 拉姆扎 (Ramza) | 主角独有——侍从升级版 |
| **Holy Knight** | 阿格里亚斯 (Agrias) | 圣剑技——Stasis Sword等 |
| **Machinist** | 姆斯塔迪奥 (Mustadio) | 枪击——Snipe/Arm Shot/Leg Shot |
| **Sword Saint** | 奥兰多 (Orlandeau/Cid) | **游戏最强角色**——全剑技无咏唱 |
| **Templar** | 贝奥武夫 (Beowulf) | 破魔/吸魔/状态异常 |
| **Skyseer / Netherseer** | 拉法/玛拉克 (Rapha/Marach) | 随机范围魔法 |

## 三、4槽技能装备系统

每个角色的技能被装入4个槽位（与皇骑4槽的"全类型共享"不同——FFT的4槽是**分类独立**的）：

| 槽位 | 类型 | 可装备 | 说明 |
|:--:|------|------|------|
| **主技能** | Action | 当前职业技能 | 自动装备——不可更换 |
| **副技能** | Secondary | **任意已学职业的技能** | FFT核心自由度来源 |
| **反应技** | Reaction | 1个被动触发的反应技能 | Counter/Auto-Potion/Shirahadori等 |
| **支援技** | Support | 1个被动加成 | Dual Wield/JP Boost/Equip Sword等 |
| **移动技** | Movement | 1个移动加成 | Move+2/Teleport/Ignore Elevation |

**设计关键**：副技能槽可以装备**任何已学过的职业技能**——你可以让一个骑士副装备白魔法、让一个忍者副召唤士、让一个僧侣副道具士。这个自由组合是FFT"任何一个角色都可以成为任何存在"的设计核心。

## 四、设计特点分析

1. **JP作为"学习货币"而非"被动经验"**：JP需要你在战场上**主动施放技能**来赚取——这不是一个"挂机成长"的系统，是"只有做才能学"的主动驱动。
2. **Spillover是FTT最被低估的设计**：它让你在不需要刻意刷的情况下自然地获得跨职业技能——这是一种"软性的、不会被迫感到在刷"的获取方式。
3. **22职业×4槽=近乎无限的角色构建空间**：FFT的角色培育是一个"在22个职业的数百个技能中选择哪些组合适配你的风格"的过程。这是SRPG品类中至今仍未被超越的培养自由度。
4. **松野本人的设计理念**：松野说他希望创造"当不同职业的技能被组合时产生意想不到的协同效应"的系统——如"阴阳士的Move-MP Up + 时魔道士的MP Switch = 几乎不死的角色"。

---

*文档大小: ~5.5 KB | 采集质量: B级 | 数据来源: 4个独立来源*
