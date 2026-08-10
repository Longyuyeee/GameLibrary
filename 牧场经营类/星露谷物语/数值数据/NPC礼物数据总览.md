[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > [NPC数据总览](./NPC数据总览.md) > NPC礼物数据总览

# NPC礼物数据总览 — 星露谷物语

> 游戏版本：Stardew Valley PC v1.6.15
>
> 中文礼物表版本：revision 53455 (2025-10-14T01:20:22Z)
>
> 英文礼物表版本：revision 191782 (2026-03-16T18:33:04Z)
>
> v1.6.15 原始数据页：revision 189757 (2025-11-22T16:57:27Z)

## 数据覆盖声明

| 项目 | 内容 |
|------|------|
| 覆盖版本 | PC v1.6.15；其他当前平台按等价内容核对，旧平台差异另记 |
| 数据范围 | 34 位可送礼村民的生日与五档礼物偏好；采用“通用规则＋逐人覆盖项”表达完整结果 |
| 预计条目数 | 34 位可送礼村民 |
| 实际收录数 | 34 位 |
| 数量差异 | 0 |
| 每条规定字段 | 中文名、英文名、生日、最爱、喜欢、一般、不喜欢、讨厌 |
| 字段完整率 | 34 / 34 行均具有 7 个源字段，100% |
| 表达规则 | 每位村民的表格记录其对通用规则的覆盖项；未被覆盖的物品按通用规则判定；中文名后保留英文名用于消歧 |
| 来源裁定 | 英文 v1.6.15 表与原始数据优先；中文表用于译名，已人工裁定 2 处源差异 |
| 验收状态 | **礼物偏好子域已完成**；NPC 日程、事件与角色资料不在本文范围 |

## 一、如何读取这份全集

游戏使用两层规则计算礼物偏好：先应用通用五档规则，再应用村民个人覆盖项。本文完整保留这两层信息。例如某位村民的“喜欢”栏没有重复列出所有通用喜欢物品，不代表缺失；只有该村民覆盖通用结果的物品或类别才会出现在个人栏中。

星之果茶固定增加 250 好感，不受普通 +80 规则限制；生日或冬日星盛宴赠送时按游戏的特殊规则处理。

## 二、通用礼物规则

| 偏好 | 好感 | 全量规则（中文＋英文原名） |
|------|:--:|------|
| 最爱 | +80 | 黄金南瓜（Golden Pumpkin）<br>魔法糖冰棍（Magic Rock Candy）<br>珍珠（Pearl）<br>五彩碎片（Prismatic Shard）<br>兔子的脚（Rabbit's Foot）<br>星之果茶 （ +250 ）（Stardrop Tea ( +250 )） |
| 喜欢 | +45 | 所有 工匠物品 （除了 油 、 虚空蛋黄酱 ）（All Artisan Goods (except Oil & Void Mayonnaise )）<br>所有 料理 （除了 面包 、 煎鸡蛋 、 奇怪的小面包 、 海泡布丁 ）（All Cooking (except Bread , Fried Egg , Seafoam Pudding , & Strange Bun )）<br>所有 花 （除了 虞美人花 ）（All Flowers (except Poppy )）<br>所有 可采集矿物 （除了 石英 ）（All Foraged Minerals (except Quartz )）<br>所有 果树果实（All Fruit Tree Fruit）<br>所有 宝石（All Gems）<br>所有 蔬菜 （除了 啤酒花 、 小麦 、 茶叶 、 未碾米 ）（All Vegetables (except Hops , Tea Leaves , Unmilled Rice , & Wheat )）<br>生命药水（Life Elixir）<br>枫糖浆（Maple Syrup）<br>椰林飘香（Piña Colada）<br>彩虹贝壳（Rainbow Shell）<br>财宝箱（Treasure Chest） |
| 一般 | +20 | 所有 书 （除了 价格目录 ）（All Books (except Price Catalogue )）<br>面包（Bread）<br>珊瑚（Coral）<br>鸭毛（Duck Feather）<br>煎鸡蛋（Fried Egg）<br>啤酒花（Hops）<br>神秘糖浆（Mystic Syrup）<br>鹦鹉螺（Nautilus Shell）<br>鱼籽（Roe）<br>鱿鱼墨汁（Squid Ink）<br>宝石甜莓（Sweet Gem Berry）<br>茶叶（Tea Leaves）<br>松露（Truffle）<br>小麦（Wheat）<br>动物毛（Wool） |
| 不喜欢 | -20 | 全部建筑材料 —— 电池组 、 粘土 、 纤维 、 硬木 、 石头 、 木材（All Building Materials -- Battery Packs , Clay , Fiber , Hardwood , Moss , Stone , and Wood）<br>所有的古物（All Artifacts）<br>所有的炸弹（All Bombs）<br>所有的地板 & 小径（All Crafted Floors & Paths）<br>所有的围栏（All Fences）<br>所有的肥料（All Fertilizer）<br>所有的鱼 （其中 鲤鱼 和 蜗牛 是讨厌的）（All Fish (except for Carp and Snails , which are universally hated)）<br>所有的晶球矿物（All Geode Minerals）<br>所有的晶球（All Geodes）<br>所有的种子 包括 果树 树苗、 茶树 、 橡子 、 枫树种子 和 松果（All Seeds including Fruit Tree Saplings, Tea Saplings , and Tree seeds）<br>所有的洒水器（All Sprinklers）<br>所有的渔具（All Tackle）<br>所有的饰品（All Trinkets）<br>烟花 -- 红色 、 绿色 和 紫色（Fireworks -- Red , Green , and Purple）<br>多数金属制品 —— 骨头碎片 、 火山晶石 、 煤炭 、 铜锭 、 金锭 、 黄金矿石 、 铱锭 、 铱矿石 、 铁锭 和 精炼石英（Misc. Mined/Metal Goods -- Bone Fragment , Cinder Shard , Coal , Copper Bars , Gold Bars , Gold Ore , Iridium Bars , Iridium Ore , Iron Bars , and Refined Quartz） |
| 讨厌 | -40 | 所有古物（All Bait）<br>所有鱼饵（All Fossils）<br>所有的怪物战利品 （除了 太阳精华 和 虚空精华 是不喜欢的）（All Monster Loot (except Solar Essence and Void Essence , which are disliked)）<br>所有垃圾 （除了 浮木 是不喜欢的）（All Trash (except Driftwood , which is disliked)） |

个人覆盖项优先于本表。完整覆盖项见下方 34 位村民的逐人数据。

## 三、可送礼村民索引（34/34）

| # | 村民 | 英文名 | 生日 | 类型 |
|:--:|------|------|------|------|
| 1 | [亚历克斯](#01-亚历克斯-alex) | Alex | 夏季 13日 | 婚恋候选人 |
| 2 | [艾利欧特](#02-艾利欧特-elliott) | Elliott | 秋季 5日 | 婚恋候选人 |
| 3 | [哈维](#03-哈维-harvey) | Harvey | 冬季 14日 | 婚恋候选人 |
| 4 | [山姆](#04-山姆-sam) | Sam | 夏季 17日 | 婚恋候选人 |
| 5 | [塞巴斯蒂安](#05-塞巴斯蒂安-sebastian) | Sebastian | 冬季 10日 | 婚恋候选人 |
| 6 | [谢恩](#06-谢恩-shane) | Shane | 春季 20日 | 婚恋候选人 |
| 7 | [阿比盖尔](#07-阿比盖尔-abigail) | Abigail | 秋季 13日 | 婚恋候选人 |
| 8 | [艾米丽](#08-艾米丽-emily) | Emily | 春季 27日 | 婚恋候选人 |
| 9 | [海莉](#09-海莉-haley) | Haley | 春季 14日 | 婚恋候选人 |
| 10 | [莉亚](#10-莉亚-leah) | Leah | 冬季 23日 | 婚恋候选人 |
| 11 | [玛鲁](#11-玛鲁-maru) | Maru | 夏季 10日 | 婚恋候选人 |
| 12 | [潘妮](#12-潘妮-penny) | Penny | 秋季 2日 | 婚恋候选人 |
| 13 | [卡洛琳](#13-卡洛琳-caroline) | Caroline | 冬季 7日 | 非婚恋村民 |
| 14 | [克林特](#14-克林特-clint) | Clint | 冬季 26日 | 非婚恋村民 |
| 15 | [德米特里厄斯](#15-德米特里厄斯-demetrius) | Demetrius | 夏季 19日 | 非婚恋村民 |
| 16 | [矮人](#16-矮人-dwarf) | Dwarf | 夏季 22日 | 非婚恋村民 |
| 17 | [艾芙琳](#17-艾芙琳-evelyn) | Evelyn | 冬季 20日 | 非婚恋村民 |
| 18 | [乔治](#18-乔治-george) | George | 秋季 24日 | 非婚恋村民 |
| 19 | [格斯](#19-格斯-gus) | Gus | 夏季 8日 | 非婚恋村民 |
| 20 | [贾斯](#20-贾斯-jas) | Jas | 夏季 4日 | 非婚恋村民 |
| 21 | [乔迪](#21-乔迪-jodi) | Jodi | 秋季 11日 | 非婚恋村民 |
| 22 | [肯特](#22-肯特-kent) | Kent | 春季 4日 | 非婚恋村民 |
| 23 | [科罗布斯](#23-科罗布斯-krobus) | Krobus | 冬季 1日 | 非婚恋村民 |
| 24 | [雷欧](#24-雷欧-leo) | Leo | 夏季 26日 | 非婚恋村民 |
| 25 | [刘易斯](#25-刘易斯-lewis) | Lewis | 春季 7日 | 非婚恋村民 |
| 26 | [莱纳斯](#26-莱纳斯-linus) | Linus | 冬季 3日 | 非婚恋村民 |
| 27 | [玛妮](#27-玛妮-marnie) | Marnie | 秋季 18日 | 非婚恋村民 |
| 28 | [潘姆](#28-潘姆-pam) | Pam | 春季 18日 | 非婚恋村民 |
| 29 | [皮埃尔](#29-皮埃尔-pierre) | Pierre | 春季 26日 | 非婚恋村民 |
| 30 | [罗宾](#30-罗宾-robin) | Robin | 秋季 21日 | 非婚恋村民 |
| 31 | [桑迪](#31-桑迪-sandy) | Sandy | 秋季 15日 | 非婚恋村民 |
| 32 | [文森特](#32-文森特-vincent) | Vincent | 春季 10日 | 非婚恋村民 |
| 33 | [威利](#33-威利-willy) | Willy | 夏季 24日 | 非婚恋村民 |
| 34 | [法师](#34-法师-wizard) | Wizard | 冬季 17日 | 非婚恋村民 |

## 四、逐人礼物偏好覆盖项

### 01. 亚历克斯 (Alex)

> 生日：夏季 13日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 完美早餐（Complete Breakfast）<br>鲑鱼晚餐（Jack Be Nimble, Jack Be Thick）<br>铜墙铁壁（Salmon Dinner） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>恐龙蛋（Dinosaur Egg）<br>工作小食（Field Snack）<br>鹦鹉蛋（Parrot Egg） |
| 一般 | +20 | 所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>青蛙蛋（Frog Egg）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 所有 书 (除了 铜墙铁壁 )（All Books (except Jack Be Nimble, Jack Be Thick )）<br>美洲大树莓（Salmonberry）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 冬青树（Holly）<br>石英（Quartz） |

### 02. 艾利欧特 (Elliott)

> 生日：秋季 5日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 蟹黄糕（Crab Cakes）<br>鸭毛（Duck Feather）<br>龙虾（Lobster）<br>石榴（Pomegranate）<br>鱿鱼墨汁（Squid Ink）<br>椰汁汤（Tom Kha Soup） |
| 喜欢 | +45 | 所有 书（All Books）<br>所有 水果 （除了 石榴 、 美洲大树莓 ）（All Fruit (except Pomegranate & Salmonberry )）<br>章鱼（Octopus）<br>鱿鱼（Squid） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 鱼 （除了 鲤鱼 、 龙虾 、 章鱼 、 海参 、 蜗牛 、 鱿鱼 ）（All Fish (except Carp , Lobster , Octopus , Sea Cucumber , Snails & Squid )）<br>彩虹贝壳（Rainbow Shell）<br>海胆（Sea Urchin） |
| 不喜欢 | -20 | 所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>披萨（Pizza）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 苋菜（Amaranth）<br>石英（Quartz）<br>美洲大树莓（Salmonberry）<br>海参（Sea Cucumber）<br>大海参（Super Cucumber） |

### 03. 哈维 (Harvey)

> 生日：冬季 14日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 咖啡（Coffee）<br>腌菜（Pickles）<br>巨无霸餐（Super Meal）<br>松露油（Truffle Oil）<br>果酒（Wine） |
| 喜欢 | +45 | 所有 水果 （除了 美洲大树莓 、 香味浆果 ）（All Fruit (except Salmonberry & Spice Berry )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>鸭蛋（Duck Egg）<br>鸭毛（Duck Feather）<br>姜（Ginger）<br>羊奶（Goat Milk）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>大瓶羊奶（Large Goat Milk）<br>韭葱（Leek）<br>石英（Quartz）<br>雪山药（Snow Yam）<br>大葱（Spring Onion）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 一般 | +20 | 所有蛋（除了 鸭蛋 、 虚空蛋 ）（All Eggs (except Duck Egg & Void Egg )）<br>大壶牛奶（Large Milk）<br>牛奶（Milk） |
| 不喜欢 | -20 | 奶酪（Blueberry Tart）<br>山羊奶酪（Bread）<br>面包（Cheese）<br>蓝莓千层酥（Chocolate Cake）<br>巧克力蛋糕（Cookie）<br>饼干（Cranberry Sauce）<br>红莓酱（Fried Mushroom）<br>炒蘑菇（Glazed Yams）<br>琉璃山药（Goat Cheese）<br>薯饼（Hashbrowns）<br>冰淇淋（Ice Cream）<br>薄煎饼（Pancakes）<br>粉红蛋糕（Pink Cake）<br>披萨（Pizza）<br>大黄派（Rhubarb Pie）<br>大米布丁（Rice Pudding） |
| 讨厌 | -40 | 珊瑚（Coral）<br>鹦鹉螺（Nautilus Shell）<br>彩虹贝壳（Rainbow Shell）<br>美洲大树莓（Salmonberry）<br>香味浆果（Spice Berry） |

### 04. 山姆 (Sam)

> 生日：夏季 17日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 仙人掌果子（Cactus Fruit）<br>枫糖棒（Maple Bar）<br>披萨（Pizza）<br>虎眼石（Tigerseye） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>Joja可乐（Joja Cola） |
| 一般 | +20 | 所有 水果 （除了 仙人掌果子 、 果树果实 、 美洲大树莓 ）（All Fruit (except Cactus Fruit , Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk） |
| 不喜欢 | -20 | 所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>所有 蔬菜 （除了 茶叶 、 啤酒花 、 小麦 ）（All Vegetables (except Hops , Tea Leaves , & Wheat )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>石英（Quartz）<br>美洲大树莓（Salmonberry）<br>海草（Seaweed）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 骨头碎片（Bone Fragment）<br>火山晶石（Cinder Shard）<br>煤炭（Coal）<br>铜锭（Copper Bar）<br>鸭蛋黄酱（Duck Mayonnaise）<br>金锭（Gold Bar）<br>黄金矿石（Gold Ore）<br>铱锭（Iridium Bar）<br>铱矿石（Iridium Ore）<br>铁锭（Iron Bar）<br>蛋黄酱（Mayonnaise）<br>腌菜（Pickles）<br>精炼石英（Refined Quartz） |

### 05. 塞巴斯蒂安 (Sebastian)

> 生日：冬季 10日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 青蛙蛋（Frog Egg）<br>泪晶（Frozen Tear）<br>黑曜石（Obsidian）<br>南瓜汤（Pumpkin Soup）<br>生鱼片（Sashimi）<br>虚空蛋（Void Egg） |
| 喜欢 | +45 | 战斗季刊（Combat Quarterly）<br>比目鱼（Flounder）<br>怪物图鉴（Monster Compendium）<br>石英（Quartz） |
| 一般 | +20 | 所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fish (except Carp , Flounder , & Snail )）<br>所有 鱼 （除了 鲤鱼 、 蜗牛 、 比目鱼 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk） |
| 不喜欢 | -20 | 所有 花 （除了 虞美人花 ）（All Flowers (except Poppy )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>美洲大树莓（Salmonberry）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 所有 工匠物品 （除了 咖啡 、 绿茶 、 油 ）（All Artisan Goods (except Coffee , Green Tea , & Oil )）<br>所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>粘土（Clay）<br>完美早餐（Complete Breakfast）<br>农夫午餐（Farmer's Lunch）<br>煎蛋卷（Omelet）<br>椰林飘香（Piña Colada） |

### 06. 谢恩 (Shane)

> 生日：春季 20日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 啤酒（Beer）<br>辣椒（Hot Pepper）<br>爆炒青椒（Pepper Poppers）<br>披萨（Pizza） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 辣椒 ）（All Fruit (except Hot Pepper )） |
| 一般 | +20 | 所有奶类（All Milk）<br>奇怪的小面包（Strange Bun） |
| 不喜欢 | -20 | 所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>海草（Seaweed）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 腌菜（Pickles）<br>石英（Quartz） |

### 07. 阿比盖尔 (Abigail)

> 生日：秋季 13日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 紫水晶（Amethyst）<br>香蕉布丁（Banana Pudding）<br>黑莓脆皮饼（Blackberry Cobbler）<br>巧克力蛋糕（Chocolate Cake）<br>怪物图鉴（Monster Compendium）<br>河豚（Pufferfish）<br>南瓜（Pumpkin）<br>香辣鳗鱼（Spicy Eel） |
| 喜欢 | +45 | 古剑（Ancient Sword）<br>蜥怪的爪子（Basilisk Paw）<br>骨笛（Bone Flute）<br>战斗季刊（Combat Quarterly）<br>石英（Quartz） |
| 一般 | +20 | 所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>所有 水果 （除了 果树果实 ）（All Fruit (except Fruit Tree Fruit )）<br>所有 蔬菜 （除了 小麦 、 啤酒花 、 南瓜 、 茶叶 ）（All Vegetables (except Hops , Pumpkin , Tea Leaves , & Wheat )）<br>糖（Sugar）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 粘土（Clay）<br>冬青树（Holly） |

### 08. 艾米丽 (Emily)

> 生日：春季 27日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 紫水晶（Amethyst）<br>海蓝宝石（Aquamarine）<br>布料（Cloth）<br>绿宝石（Emerald）<br>翡翠（Jade）<br>鹦鹉蛋（Parrot Egg）<br>红宝石（Ruby）<br>救生汉堡（Survival Burger）<br>黄水晶（Topaz）<br>动物毛（Wool） |
| 喜欢 | +45 | 黄水仙（Daffodil）<br>石英（Quartz） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 炒鳗鱼（Fried Eel）<br>冰淇淋（Ice Cream）<br>大米布丁（Rice Pudding）<br>美洲大树莓（Salmonberry）<br>香辣鳗鱼（Spicy Eel） |
| 讨厌 | -40 | 鱼肉卷（Fish Taco）<br>冬青树（Holly）<br>生鱼寿司（Maki Roll）<br>鲑鱼晚餐（Salmon Dinner）<br>生鱼片（Sashimi） |

### 09. 海莉 (Haley)

> 生日：春季 14日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 椰子（Coconut）<br>水果沙拉（Fruit Salad）<br>粉红蛋糕（Pink Cake）<br>向日葵（Sunflower） |
| 喜欢 | +45 | 黄水仙（Daffodil） |
| 一般 | +20 | — |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>所有 水果 （除了 椰子 ）（All Fruit (except Coconut )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>所有 蔬菜 （除了 啤酒花 、 小麦 、 茶叶 ）（All Vegetables (except Hops , Tea Leaves , & Wheat )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>神秘糖浆（Mystic Syrup）<br>石英（Quartz）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 讨厌 | -40 | 所有 鱼（All Fish）<br>粘土（Clay）<br>五彩碎片（Prismatic Shard）<br>野山葵（Wild Horseradish） |

### 10. 莉亚 (Leah)

> 生日：冬季 23日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 山羊奶酪（Goat Cheese）<br>虞美人籽松糕（Poppyseed Muffin）<br>沙拉（Salad）<br>蔬菜什锦盖饭（Stir Fry）<br>松露（Truffle）<br>蔬菜杂烩（Vegetable Medley）<br>果酒（Wine） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果（All Fruit）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>浮木（Driftwood）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>大葱（Spring Onion）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 一般 | +20 | — |
| 不喜欢 | -20 | 所有 可采集矿物 （除了 地晶 ）（All Foraged Minerals (except Earth Crystal )）<br>所有 宝石 （除了 钻石 、 五彩碎片 ）（All Gems (except Diamond & Prismatic Shard )）<br>惊喜鲤鱼（Carp Surprise）<br>饼干（Cookie）<br>煎鸡蛋（Fried Egg）<br>冰淇淋（Ice Cream）<br>粉红蛋糕（Pink Cake）<br>大米布丁（Rice Pudding）<br>海草（Seaweed）<br>救生汉堡（Survival Burger）<br>墨西哥薄饼（Tortilla） |
| 讨厌 | -40 | 面包（Bread）<br>薯饼（Hashbrowns）<br>薄煎饼（Pancakes）<br>披萨（Pizza）<br>虚空蛋黄酱（Void Egg） |

### 11. 玛鲁 (Maru)

> 生日：夏季 10日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 电池组（Battery Pack）<br>花椰菜（Cauliflower）<br>乳酪花椰菜（Cheese Cauliflower）<br>钻石（Diamond）<br>矮人小工具（Dwarf Gadget）<br>金锭（Gold Bar）<br>铱锭（Iridium Bar）<br>矿工特供（Miner's Treat）<br>爆炒青椒（Pepper Poppers）<br>放射性矿锭（Radioactive Bar）<br>大黄派（Rhubarb Pie）<br>草莓（Strawberry） |
| 喜欢 | +45 | 所有蘑菇 （除了 普通蘑菇 、 红蘑菇 )（All Mushrooms (except Common & Red )）<br>铜锭（Copper Bar）<br>铁锭（Iron Bar）<br>橡树树脂（Oak Resin）<br>松焦油（Pine Tar）<br>石英（Quartz）<br>放射性矿石（Radioactive Ore） |
| 一般 | +20 | 所有蛋（除了虚空蛋）（All Eggs (except Void Egg )）<br>所有水果（除了黑莓、水晶果、果树果实、美洲大树莓、草莓）（All Fruit (except Blackberry , Crystal Fruit , Fruit Tree Fruit , Salmonberry & Strawberry )）<br>所有奶类（All Milk）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 黑莓（Blackberry）<br>普通蘑菇（Common Mushroom）<br>水晶果（Crystal Fruit）<br>枫糖浆（Maple Syrup）<br>美洲大树莓（Salmonberry） |
| 讨厌 | -40 | 冬青树（Holly）<br>蜂蜜（Honey）<br>腌菜（Pickles）<br>雪山药（Snow Yam）<br>松露（Truffle） |

### 12. 潘妮 (Penny)

> 生日：秋季 2日 | 类型：婚恋候选人

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 所有 书（All Books）<br>钻石（Diamond）<br>绿宝石（Emerald）<br>甜瓜（Melon）<br>虞美人花（Poppy）<br>虞美人籽松糕（Poppyseed Muffin）<br>红之盛宴（Red Plate）<br>块茎拼盘（Roots Platter）<br>沙鱼（Sandfish）<br>椰汁汤（Tom Kha Soup） |
| 喜欢 | +45 | 所有奶类（All Artifacts）<br>所有 古物（All Milk）<br>蒲公英（Dandelion）<br>韭葱（Leek） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 葡萄 、 甜瓜 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit , Grape , Melon & Salmonberry )）<br>所有蘑菇（除了 红蘑菇 、 紫蘑菇 ）（All Mushrooms (except Purple & Red )）<br>黄水仙（Daffodil）<br>姜（Ginger）<br>榛子（Hazelnut）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 海藻汤（Algae Soup）<br>鸭毛（Duck Feather）<br>清汤（Pale Broth）<br>紫蘑菇（Purple Mushroom）<br>石英（Quartz）<br>红蘑菇（Red Mushroom）<br>美洲大树莓（Salmonberry）<br>动物毛（Wool） |
| 讨厌 | -40 | 啤酒（Beer）<br>葡萄（Grape）<br>冬青树（Holly）<br>啤酒花（Hops）<br>蜜蜂酒（Mead）<br>淡啤酒（Pale Ale）<br>椰林飘香（Piña Colada）<br>兔子的脚（Rabbit's Foot）<br>果酒（Wine） |

### 13. 卡洛琳 (Caroline)

> 生日：冬季 7日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 鱼肉卷（Fish Taco）<br>夏季亮片（Green Tea）<br>绿茶（Summer Spangle）<br>热带咖喱（Tropical Curry） |
| 喜欢 | +45 | 黄水仙（Daffodil）<br>茶叶（Tea Leaves）<br>野山葵（Wild Horseradish） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk） |
| 不喜欢 | -20 | 所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>苋菜（Amaranth）<br>蒲公英（Dandelion）<br>鸭蛋黄酱（Duck Mayonnaise）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>蛋黄酱（Mayonnaise）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 讨厌 | -40 | 石英（Quartz）<br>美洲大树莓（Salmonberry） |

### 14. 克林特 (Clint)

> 生日：冬季 26日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 紫水晶（Amethyst）<br>海蓝宝石（Aquamarine）<br>水煮洋蓟（Artichoke Dip）<br>绿宝石（Emerald）<br>意式蕨菜炖饭（Fiddlehead Risotto）<br>金锭（Gold Bar）<br>铱锭（Iridium Bar）<br>翡翠（Jade）<br>万象晶球（Omni Geode）<br>红宝石（Ruby）<br>黄水晶（Topaz） |
| 喜欢 | +45 | 铜锭（Copper Bar）<br>铁锭（Iron Bar）<br>采矿月刊（Mining Monthly） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>煤炭（Coal）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>黄金矿石（Gold Ore）<br>榛子（Hazelnut）<br>铱矿石（Iridium Ore）<br>韭葱（Leek）<br>精炼石英（Refined Quartz）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 所有 花 （除了 虞美人花 ）（All Flowers (except Poppy )）<br>石英（Quartz）<br>美洲大树莓（Salmonberry）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 冬青树（Holly） |

### 15. 德米特里厄斯 (Demetrius)

> 生日：夏季 19日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 豆类火锅（Bean Hotpot）<br>冰淇淋（Ice Cream）<br>大米布丁（Rice Pudding）<br>草莓（Strawberry） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 草莓 ）（All Fruit (except Strawberry )）<br>紫蘑菇（Dinosaur Egg）<br>恐龙蛋（Purple Mushroom） |
| 一般 | +20 | 所有 鱼 （除了 鲤鱼 、 蜗牛 ）（All Fish (except Carp & Snail )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 、 紫蘑菇 ）（All Mushrooms (except Red & Purple )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 石英（Quartz） |
| 讨厌 | -40 | 冬青树（Holly） |

### 16. 矮人 (Dwarf)

> 生日：夏季 22日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 紫水晶（Amethyst）<br>海蓝宝石（Aquamarine）<br>绿宝石（Emerald）<br>翡翠（Jade）<br>岩浆鳗鱼（Lava Eel）<br>柠檬石（Lemon Stone）<br>万象晶球（Omni Geode）<br>红宝石（Ruby）<br>黄水晶（Topaz） |
| 喜欢 | +45 | 所有 古物（All Artifacts）<br>山洞萝卜（Cave Carrot）<br>石英（Quartz） |
| 一般 | +20 | 所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>太阳精华（Solar Essence）<br>虚空精华（Void Essence） |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>美洲大树莓（Salmonberry）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | — |

### 17. 艾芙琳 (Evelyn)

> 生日：冬季 20日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 甜菜（Beet）<br>巧克力蛋糕（Chocolate Cake）<br>钻石（Diamond）<br>玫瑰仙子（Fairy Rose）<br>葡萄干（Raisins）<br>塞料面包（Stuffing）<br>郁金香（Tulip） |
| 喜欢 | +45 | 所有奶类（All Milk）<br>破损的眼镜（Broken Glasses）<br>蛤（Clam）<br>鸟蛤（Cockle）<br>珊瑚（Coral）<br>黄水仙（Daffodil）<br>蚌（Mussel）<br>鹦鹉螺（Nautilus Shell）<br>牡蛎（Oyster）<br>海胆（Sea Urchin） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 、 香味浆果 ）（All Fruit (except Fruit Tree Fruit , Salmonberry & Spice Berry )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 石英（Quartz）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 所有 鱼 （除了 蛤 、 鸟蛤 、 蚌 和 牡蛎 ）（All Fish (except Clam , Cockle , Mussel , & Oyster )）<br>粘土（Clay）<br>炒鳗鱼（Fried Eel）<br>蒜（Garlic）<br>冬青树（Holly）<br>生鱼寿司（Maki Roll）<br>美洲大树莓（Salmonberry）<br>生鱼片（Sashimi）<br>香味浆果（Spice Berry）<br>香辣鳗鱼（Spicy Eel）<br>鳟鱼汤（Trout Soup） |

### 18. 乔治 (George)

> 生日：秋季 24日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 炒蘑菇（Fried Mushroom）<br>韭葱（Leek） |
| 喜欢 | +45 | 黄水仙（Daffodil） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 )（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>姜（Ginger）<br>榛子（Hazelnut）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 所有 花 （除了 虞美人花 ）（All Flowers (except Poppy )）<br>美洲大树莓（Salmonberry）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 粘土（Clay）<br>蒲公英（Dandelion）<br>冬青树（Holly）<br>石英（Quartz） |

### 19. 格斯 (Gus)

> 生日：夏季 8日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 钻石（Diamond）<br>法式田螺（Escargot）<br>鱼肉卷（Fish Taco）<br>橙子（Orange）<br>热带咖喱（Tropical Curry） |
| 喜欢 | +45 | 黄水仙（Daffodil）<br>松露（Truffle） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 美洲大树莓（Salmonberry）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 卷心菜沙拉（Coleslaw）<br>冬青树（Holly）<br>石英（Quartz） |

### 20. 贾斯 (Jas)

> 生日：夏季 4日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 古代玩偶（Ancient Doll）<br>仙女盒（Fairy Box）<br>玫瑰仙子（Fairy Rose）<br>粉红蛋糕（Pink Cake）<br>葡萄干布丁（Plum Pudding）<br>诡异玩偶（绿）（Strange Doll (green)）<br>诡异玩偶（黄）（Strange Doll (yellow)） |
| 喜欢 | +45 | 所有奶类（All Milk）<br>椰子（Coconut）<br>黄水仙（Daffodil） |
| 一般 | +20 | — |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>所有 水果 （除了 椰子 、 果树果实 ）（All Fruit (except Coconut & Fruit Tree Fruit )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>所有蔬菜（除了 啤酒花 、 小麦 、 茶叶 ）（All Vegetables (except Hops , Tea Leaves , & Wheat )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>石英（Quartz）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 讨厌 | -40 | 所有 工匠物品 （除了 蜂蜜 、 油 、 果酱 ）（All Artisan Goods (except Honey , Jelly , & Oil )）<br>粘土（Clay）<br>野山葵（Piña Colada）<br>三倍浓缩咖啡（Triple Shot Espresso）<br>椰林飘香（Wild Horseradish） |

### 21. 乔迪 (Jodi)

> 生日：秋季 11日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 巧克力蛋糕（Chocolate Cake）<br>香酥鲈鱼（Crispy Bass）<br>钻石（Diamond）<br>帕尔玛奶酪茄子（Eggplant Parmesan）<br>炒鳗鱼（Fried Eel）<br>薄煎饼（Pancakes）<br>大黄派（Rhubarb Pie）<br>蔬菜杂烩（Vegetable Medley） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果 （除了 香味浆果 ）（All Fruit (except Spice Berry )）<br>所有奶类（All Milk） |
| 一般 | +20 | — |
| 不喜欢 | -20 | 所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒜（Garlic）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>石英（Quartz）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>香味浆果（Spice Berry） |

### 22. 肯特 (Kent)

> 生日：春季 4日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 意式蕨菜炖饭（Fiddlehead Risotto）<br>烤榛子（Roasted Hazelnuts） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 水果（All Fruit）<br>黄水仙（Daffodil）<br>矮人安全手册（Dwarvish Safety Manual） |
| 一般 | +20 | 所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 椰林飘香（Piña Colada）<br>石英（Quartz）<br>雪山药（Snow Yam） |
| 讨厌 | -40 | 所有奶类（All Milk）<br>海藻汤（Algae Soup）<br>冬青树（Holly）<br>生鱼片（Sashimi）<br>墨西哥薄饼（Tortilla） |

### 23. 科罗布斯 (Krobus)

> 生日：冬季 1日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 钻石（Diamond）<br>铱锭（Iridium Bar）<br>怪物图鉴（Monster Compendium）<br>怪兽香水（Monster Musk）<br>南瓜（Pumpkin）<br>虚空蛋（Void Egg）<br>虚空蛋黄酱（Void Mayonnaise）<br>野山葵（Wild Horseradish） |
| 喜欢 | +45 | 金锭（Gold Bar）<br>石英（Quartz）<br>海泡布丁（Seafoam Pudding）<br>奇怪的小面包（Strange Bun） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有奶类（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Milk） |
| 不喜欢 | -20 | 所有 料理 （除了 面包 、 煎鸡蛋 、 奇怪的小面包 、 海泡布丁 ）（All Cooking (except Bread , Fried Egg , Seafoam Pudding & Strange Bun )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>生命药水（Life Elixir）<br>美洲大树莓（Salmonberry）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 讨厌 | -40 | — |

### 24. 雷欧 (Leo)

> 生日：夏季 26日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 鸭毛（Duck Feather）<br>芒果（Mango）<br>鸵鸟蛋（Ostrich Egg）<br>鹦鹉蛋（Parrot Egg）<br>夏威夷芋泥（Poi） |
| 喜欢 | +45 | 龙牙（Dragon Tooth）<br>鹦鹉螺（Nautilus Shell）<br>石英（Quartz）<br>海胆（Sea Urchin）<br>香味浆果（Spice Berry） |
| 一般 | +20 | 所有蛋（除了 鸵鸟蛋 和 虚空蛋 ）（All Eggs (except Ostrich Egg & Void Egg )）<br>所有 鱼（All Fish (except Carp & Snail )）<br>所有 水果 （除了 果树果实 、 芒果 、 美洲大树莓 、 香味浆果 ）（All Fruit (except Fruit Tree Fruit , Mango , Salmonberry , & Spice Berry )）<br>所有奶类（All Milk）<br>咖啡（Coffee） |
| 不喜欢 | -20 | 所有 料理 （除了 面包 、 煎鸡蛋 、 芒果糯米饭 、 夏威夷芋泥 、 三倍浓缩咖啡 ）（All Cooking (except Bread , Fried Egg , Mango Sticky Rice , Poi & Triple Shot Espresso )）<br>所有蘑菇（除了 羊肚菌 和 红蘑菇 ）（All Mushrooms (except Morel & Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>生命药水（Life Elixir）<br>腌菜（Pickles）<br>美洲大树莓（Salmonberry）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 啤酒（Beer）<br>冬青树（Holly）<br>啤酒花（Hops）<br>蜜蜂酒（Mead）<br>羊肚菌（Morel）<br>油（Oil）<br>淡啤酒（Pale Ale）<br>椰林飘香（Piña Colada）<br>三倍浓缩咖啡（Triple Shot Espresso）<br>未碾米（Unmilled Rice）<br>果酒（Wine） |

### 25. 刘易斯 (Lewis)

> 生日：春季 7日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 秋日恩赐（Autumn's Bounty）<br>琉璃山药（Glazed Yams）<br>辣椒（Green Tea）<br>蔬菜杂烩（Hot Pepper）<br>绿茶（Vegetable Medley） |
| 喜欢 | +45 | 蓝莓（Blueberry）<br>仙人掌果子（Cactus Fruit）<br>椰子（Coconut） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有水果（除了 蓝莓 、 仙人掌果子 、 椰子 、 果树果实 、 辣椒 、 美洲大树莓 ）（All Fruit (except Blueberry , Cactus Fruit , Coconut , Fruit Tree Fruit , Hot Pepper , & Salmonberry )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 所有奶类（All Milk）<br>美洲大树莓（Salmonberry）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 冬青树（Holly）<br>石英（Quartz） |

### 26. 莱纳斯 (Linus)

> 生日：冬季 3日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 蓝莓千层酥（Blueberry Tart）<br>仙人掌果子（Cactus Fruit）<br>椰子（Coconut）<br>海之菜肴（Dish O' The Sea）<br>小巷自助餐（The Alleyway Buffet）<br>山药（Yam） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有奶类（All Fruit (except Cactus Fruit & Coconut )）<br>所有 水果 （除了 仙人掌果子 、 椰子 ）（All Milk）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>大葱（Spring Onion）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 一般 | +20 | 所有 鱼 （除了 蜗牛 ）（All Fish (except Snail )） |
| 不喜欢 | -20 | 所有 可采集矿物（All Foraged Minerals）<br>所有 宝石 （除了 钻石 、 五彩碎片 ）（All Gems (except Diamond & Prismatic Shard )）<br>财宝箱（Treasure Chest） |
| 讨厌 | -40 | — |

### 27. 玛妮 (Marnie)

> 生日：秋季 18日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 钻石（Diamond）<br>农夫午餐（Farmer's Lunch）<br>粉红蛋糕（Pink Cake）<br>南瓜派（Pumpkin Pie） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有奶类（All Milk）<br>星露谷年历（Stardew Valley Almanac）<br>石英（Quartz） |
| 一般 | +20 | 所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 美洲大树莓（Salmonberry）<br>海草（Seaweed）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 粘土（Clay）<br>冬青树（Holly） |

### 28. 潘姆 (Pam)

> 生日：春季 18日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 啤酒（Beer）<br>仙人掌果子（Cactus Fruit）<br>琉璃山药（Glazed Yams）<br>蜜蜂酒（Mead）<br>淡啤酒（Pale Ale）<br>防风草（Parsnip）<br>防风草汤（Parsnip Soup）<br>椰林飘香（Piña Colada） |
| 喜欢 | +45 | 所有 水果 （除了 仙人掌果子 ）（All Fruit (except Cactus Fruit )）<br>所有奶类（All Milk）<br>黄水仙（Daffodil） |
| 一般 | +20 | 所有 鱼 （除了 鲤鱼 、 章鱼 、 蜗牛 、 鱿鱼 ）（All Fish (except Carp , Octopus , Snail & Squid )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>Joja可乐（Joja Cola）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>石英（Quartz）<br>野山葵（Wild Horseradish） |
| 讨厌 | -40 | 冬青树（Holly）<br>章鱼（Octopus）<br>鱿鱼（Squid） |

### 29. 皮埃尔 (Pierre)

> 生日：春季 26日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 炸鱿鱼（Fried Calamari）<br>价格目录（Price Catalogue） |
| 喜欢 | +45 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有奶类（All Milk）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion） |
| 一般 | +20 | 所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )） |
| 不喜欢 | -20 | 所有 可采集矿物（All Foraged Minerals）<br>所有 宝石 （除了 钻石 、 五彩碎片 ）（All Gems (except Diamond & Prismatic Shard )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>美洲大树莓（Salmonberry）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | 所有 鱼（All Fish）<br>玉米（Corn）<br>蒜（Garlic）<br>防风草汤（Parsnip Soup）<br>墨西哥薄饼（Tortilla） |

### 30. 罗宾 (Robin)

> 生日：秋季 21日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 山羊奶酪（Goat Cheese）<br>桃子（Peach）<br>意大利面（Spaghetti）<br>伐木秘事（Woody's Secret） |
| 喜欢 | +45 | 所有奶类（All Fruit (except Peach )）<br>所有 水果 （除了 桃子 ）（All Milk）<br>硬木（Hardwood）<br>石英（Quartz）<br>樵夫周刊（Woodcutter's Weekly） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>韭葱（Leek）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 不喜欢 | -20 | 野山葵（Wild Horseradish） |
| 讨厌 | -40 | 冬青树（Holly） |

### 31. 桑迪 (Sandy)

> 生日：秋季 15日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 番红花（Crocus）<br>黄水仙（Daffodil）<br>芒果糯米饭（Mango Sticky Rice）<br>甜豌豆（Sweet Pea） |
| 喜欢 | +45 | 所有 水果（All Fruit）<br>羊奶（Goat Milk）<br>大瓶羊奶（Large Goat Milk）<br>石英（Quartz）<br>动物毛（Wool） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>大壶牛奶（Large Milk）<br>韭葱（Leek）<br>牛奶（Milk）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 不喜欢 | -20 | — |
| 讨厌 | -40 | 冬青树（Holly） |

### 32. 文森特 (Vincent)

> 生日：春季 10日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 蔓越莓糖果（Cranberry Candy）<br>青蛙蛋（Frog Egg）<br>姜汁汽水（Ginger Ale）<br>葡萄（Grape）<br>粉红蛋糕（Pink Cake）<br>蜗牛（Snail） |
| 喜欢 | +45 | 所有奶类（All Milk）<br>椰子（Coconut）<br>黄水仙（Daffodil） |
| 一般 | +20 | — |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>所有 水果 （除了 椰子 、 葡萄 、 果树果实 ）（All Fruit (except Coconut , Grape & Fruit Tree Fruit )）<br>所有 蔬菜 （除了 啤酒花 、 小麦 、 茶叶 ）（All Vegetables (except Hops , Tea Leaves , & Wheat )）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>石英（Quartz）<br>雪山药（Snow Yam）<br>冬根（Winter Root） |
| 讨厌 | -40 | 所有 工匠物品 （除了 蜂蜜 、 油 、 果酱 ）（All Artisan Goods (except Honey , Jelly , & Oil )）<br>粘土（Clay）<br>野山葵（Piña Colada）<br>三倍浓缩咖啡（Triple Shot Espresso）<br>椰林飘香（Wild Horseradish） |

### 33. 威利 (Willy)

> 生日：夏季 24日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 鲶鱼（Catfish）<br>钻石（Diamond）<br>金锭（Gold Bar）<br>铱锭（Iridium Bar）<br>海之宝石（Jewels Of The Sea）<br>蜜蜂酒（Mead）<br>章鱼（Octopus）<br>南瓜（Pumpkin）<br>海参（Sea Cucumber）<br>鲟鱼（Sturgeon）<br>捕蟹秘籍（The Art O' Crabbing） |
| 喜欢 | +45 | 鱼饵和浮漂（Bait And Bobber）<br>蛇齿单线鱼（Lingcod）<br>石英（Quartz）<br>海泡布丁（Seafoam Pudding）<br>虎纹鳟鱼（Tiger Trout） |
| 一般 | +20 | 所有蛋（除了 虚空蛋 ）（All Eggs (except Void Egg )）<br>所有 鱼 （除了 鲤鱼 、 鲶鱼 、 蛇齿单线鱼 、 章鱼 、 海参 、 蜗牛 、 鲟鱼 、 虎纹鳟鱼 ）（All Fish (except Carp , Catfish , Lingcod , Octopus , Sea Cucumber , Snail , Sturgeon & Tiger Trout )）<br>所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )）<br>所有奶类（All Milk）<br>海之菜肴（Dish O' The Sea）<br>生鱼寿司（Maki Roll）<br>生鱼片（Sashimi） |
| 不喜欢 | -20 | 所有 料理 （除了 烤鱼 、 面包 、 惊喜鲤鱼 、 海鲜杂烩汤 、 蟹黄糕 、 香酥鲈鱼 、 烩鱼汤 、 鱼肉卷 、 炸鱿鱼 、 炒鳗鱼 、 煎鸡蛋 、 龙虾浓汤 、 鲑鱼晚餐 、 奇怪的小面包 、 鳟鱼汤 、 海之菜肴 、 生鱼寿司 、 生鱼片 、 海泡布丁 、 法式田螺 ）（All Cooking except for Bread , Fried Egg , Strange Bun ; the fish dishes he is neutral towards: Dish O' The Sea , Maki Roll , & Sashimi ; and the fish dishes he likes: Baked Fish , Carp Surprise , Chowder , Crab Cakes , Crispy Bass , Escargot , Fish Stew , Fish Taco , Fried Calamari , Fried Eel , Lobster Bisque , Salmon Dinner , Seafoam Pudding , & Trout Soup）<br>所有蘑菇（除了 红蘑菇 ）（All Mushrooms (except Red )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>生命药水（Life Elixir）<br>美洲大树莓（Salmonberry）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | — |

### 34. 法师 (Wizard)

> 生日：冬季 17日 | 类型：非婚恋村民

| 偏好 | 好感 | 对通用规则的完整覆盖项 |
|------|:--:|------|
| 最爱 | +80 | 谜之书（Book of Mysteries）<br>紫蘑菇（Purple Mushroom）<br>太阳精华（Solar Essence）<br>大海参（Super Cucumber）<br>虚空精华（Void Essence） |
| 喜欢 | +45 | 所有 晶球矿物（All Geode Minerals）<br>所有 饰品（All Trinkets）<br>铱锭（Iridium Bar）<br>石英（Quartz） |
| 一般 | +20 | 所有 水果 （除了 果树果实 、 美洲大树莓 ）（All Fruit (except Fruit Tree Fruit & Salmonberry )） |
| 不喜欢 | -20 | 所有蛋（All Eggs）<br>所有奶类（All Milk）<br>所有蘑菇（除了 红蘑菇 、 紫蘑菇 ）（All Mushrooms (except Red & Purple )）<br>黄水仙（Daffodil）<br>蒲公英（Dandelion）<br>姜（Ginger）<br>榛子（Hazelnut）<br>冬青树（Holly）<br>韭葱（Leek）<br>美洲大树莓（Salmonberry）<br>史莱姆泥（Slime）<br>雪山药（Snow Yam）<br>野山葵（Wild Horseradish）<br>冬根（Winter Root） |
| 讨厌 | -40 | — |

## 五、来源与对账

- [中文 Stardew Valley Wiki — 礼物列表](https://zh.stardewvalleywiki.com/%E7%A4%BC%E7%89%A9%E5%88%97%E8%A1%A8)
- [英文 Stardew Valley Wiki — List of All Gifts](https://stardewvalleywiki.com/List_of_All_Gifts)
- [中文 Stardew Valley Wiki — 友谊](https://zh.stardewvalleywiki.com/%E5%8F%8B%E8%B0%8A)
- [英文 Stardew Valley Wiki — Friendship](https://stardewvalleywiki.com/Friendship)
- [英文 Stardew Valley Wiki — v1.6.15 NPCGiftTastes 原始数据](https://stardewvalleywiki.com/Modding:Gift_taste_data)

生成审计：中英文礼物表均为 35 行，其中 1 行通用规则、34 行可送礼村民；34 位村民英文名及顺序完全一致；每行均为 7 个字段。

来源差异裁定：中文 revision 53455 比英文表旧。玛鲁“一般”栏移除中文表额外的蘑菇类别；雷欧“喜欢”栏移除中文表额外的彩虹贝壳。两处均以英文 1.6.15 表和原始数据为准。

---

[上一篇：NPC数据总览](./NPC数据总览.md) · [返回游戏概览](../游戏概览.md) · [下一篇：作物数据总览](./作物数据总览.md)
