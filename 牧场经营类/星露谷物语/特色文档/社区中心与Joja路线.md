[项目首页](../../../README.md) > [牧场经营类](../../_index.md) > [星露谷物语概览](../游戏概览.md) > 社区中心与Joja路线

# 社区中心与 Joja 路线 — PC v1.6.15 全集

> 本页是标准收集包、混合收集包候选池、社区中心修复、Joja 社区开发项目和两条路线电影院解锁的唯一专题数据源。

## 一、数据覆盖声明

| 项目 | 对账结果 |
|------|------|
| 目标版本 | PC v1.6.15 |
| 固定来源 | 预计 5 / 实际 5 |
| 域内源表 | 预计 95 / 实际 95；表体记录预计 440 / 实际 440 |
| 规则事实块 | 预计 68 / 实际 68 |
| 标准房间收集包 | 预计 30 / 实际 30 |
| 遗失收集包 | 预计 1 / 实际 1 |
| 混合模式候选包 | 预计 47 / 实际 47 |
| 数量差异 | 0 |
| 未知或待核实字段 | 0 |
| 验收状态 | **已完成** |

### 范围边界

- 标准模式保留 6 个房间的 30 个收集包、房间奖励、旅行货车一年完成保证及遗失收集包的全部固定源记录。
- 混合模式不是固定的 30 张表，而是按房间槽位从 47 个候选包中抽取；候选表、随机选取数量、物品、品质、数量、来源和奖励均完整保留。
- Joja 路线保留会员/开发项目、费用、完成后果与电影院解锁；电影排片、零食、抓娃娃机奖池属于电影院内容域，不在路线文档做节选。
- History、Trivia、Gallery、Bugs、References、纯对白和外部导航不属于本域。

## 二、结构关系

| 路线 | 完整数据入口 |
|------|------|
| 社区中心标准模式 | [标准收集包固定源](#source-bundles) |
| 社区中心混合模式 | [混合收集包固定源](#source-remixed-bundles) |
| 社区中心修复与完成后果 | [社区中心固定源](#source-community-center) |
| Joja 社区开发项目 | [Joja 开发表固定源](#source-joja-community-development-form) |
| 两条路线的电影院位置与解锁 | [电影院固定源](#source-movie-theater) |

## 三、固定来源完整记录

<a id="source-bundles"></a>
## 1. 标准收集包与遗失收集包（Bundles）

固定来源：[revision 193528](https://stardewvalleywiki.com/mediawiki/index.php?title=Bundles&oldid=193528)；保留数据表 39 张、数据行 176、规则事实块 23。

### 1.1 Traveling Cart Availability

| Any / starred (silver or higher quality) item / Aged Roe / Aged Roe / * / Amethyst / Amethyst / * / Ancient Doll / Ancient Doll / * / Ancient Fruit / Ancient Fruit / Aquamarine / Aquamarine / Blobfish / Blobfish / * / Bone Fragment / Bone Fragment / * / Diamond / Diamond / * | Dinosaur Mayonnaise / Dinosaur Mayonnaise / Earth Crystal / Earth Crystal / Emerald / Emerald / * / Fire Quartz / Fire Quartz / Frozen Geode / Frozen Geode / Frozen Tear / Frozen Tear / Hay / Hay / Lava Eel / Lava Eel / * / Prismatic Shard / Prismatic Shard | Quartz / Quartz / Roe / Roe / * / Ruby / Ruby / * / Squid Ink / Squid Ink / * / Sweet Gem Berry / Sweet Gem Berry / * / Topaz / Topaz / * / Void Salmon / Void Salmon / Wheat Flour / Wheat Flour / * / White Algae / White Algae / * |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.2 Crafts Room — Bundle Complete Balloon

| Bundle Complete Balloon | Crafts / Room / Reward | Bridge Repair |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.3 Crafts Room — Bundle Green / Spring Foraging Bundle

| Bundle Green / Spring Foraging Bundle | Bundle Green / Spring Foraging Bundle | Bundle Green / Spring Foraging Bundle | Bundle Green / Spring Foraging Bundle |
|---|---|---|---|
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wild Horseradish / Wild Horseradish | Spring / Foraging |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Daffodil / Daffodil | Spring / Foraging / , buy from / Pierre / at / Flower Dance |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Leek / Leek | Spring / Foraging |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Dandelion / Dandelion | Spring / Foraging / , buy from / Pierre / at / Flower Dance |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Spring Seeds / Spring Seeds / (30) | Spring Seeds / Spring Seeds / (30) |

### 1.4 Crafts Room — Bundle Yellow / Summer Foraging Bundle

| Bundle Yellow / Summer Foraging Bundle | Bundle Yellow / Summer Foraging Bundle | Bundle Yellow / Summer Foraging Bundle | Bundle Yellow / Summer Foraging Bundle | —（固定源空白） |
|---|---|---|---|---|
| Summer Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Grape / Grape | Summer / Foraging / , / Fall / Farming | —（固定源空白） |
| Summer Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Spice Berry / Spice Berry | Summer / Foraging / , / The Farm Cave / (fruit bat option) | —（固定源空白） |
| Summer Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Sweet Pea / Sweet Pea | Summer / Foraging | —（固定源空白） |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Summer Seeds / Summer Seeds / (30) | Summer Seeds / Summer Seeds / (30) | Summer Seeds / Summer Seeds / (30) |

### 1.5 Crafts Room — Bundle Orange / Fall Foraging Bundle

| Bundle Orange / Fall Foraging Bundle | Bundle Orange / Fall Foraging Bundle | Bundle Orange / Fall Foraging Bundle | Bundle Orange / Fall Foraging Bundle |
|---|---|---|---|
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Common Mushroom / Common Mushroom | Fall / Foraging / , / Spring / & / Fall / Foraging / in the / Secret Woods / , / The Farm Cave / (mushroom option), / Tapping / a / Mushroom Tree |
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wild Plum / Wild Plum | Fall / Foraging / , / The Farm Cave / (fruit bat option) |
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Hazelnut / Hazelnut | Fall / Foraging |
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Blackberry / Blackberry | Fall / Foraging / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Fall Seeds / Fall Seeds / (30) | Fall Seeds / Fall Seeds / (30) |

### 1.6 Crafts Room — Bundle Teal / Winter Foraging Bundle

| Bundle Teal / Winter Foraging Bundle | Bundle Teal / Winter Foraging Bundle | Bundle Teal / Winter Foraging Bundle | Bundle Teal / Winter Foraging Bundle |
|---|---|---|---|
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Winter Root / Winter Root | Tilling / soil or / Artifact Spots / in / Winter / , dropped by Blue / Slimes / on floors 41-79 of / The Mines |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crystal Fruit / Crystal Fruit | Winter / Foraging / , dropped by / Dust Sprites / on floors 41-79 of / The Mines |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Snow Yam / Snow Yam | Tilling / soil or / Artifact Spots / in / Winter |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crocus / Crocus | Winter / Foraging |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Winter Seeds / Winter Seeds / (30) | Winter Seeds / Winter Seeds / (30) |

### 1.7 Crafts Room — Bundle Red / Construction Bundle

| Bundle Red / Construction Bundle | Bundle Red / Construction Bundle | Bundle Red / Construction Bundle | Bundle Red / Construction Bundle |
|---|---|---|---|
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wood / Wood / (99) | Chopping / Trees / or branches with an / Axe / , / Carpenter's Shop |
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wood / Wood / (99) | Chopping / Trees / or branches with an / Axe / , / Carpenter's Shop |
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Stone / Stone / (99) | Smashing stones with a / Pickaxe / , / Carpenter's Shop |
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Hardwood / Hardwood / (10) | Chopping / Large Stumps / or / Large Logs / with an upgraded / Axe / , smashing crates in / The Mines / , chopping / Mahogany Trees |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Charcoal Kiln / Charcoal Kiln / (1) | Charcoal Kiln / Charcoal Kiln / (1) |

### 1.8 Crafts Room — Bundle Purple / Exotic Foraging Bundle

| Bundle Purple / Exotic Foraging Bundle | Bundle Purple / Exotic Foraging Bundle | Bundle Purple / Exotic Foraging Bundle | Bundle Purple / Exotic Foraging Bundle |
|---|---|---|---|
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Coconut / Coconut | Desert / Foraging / , / Oasis / , shaking a / Palm Tree / in / the Desert / and on / Ginger Island |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cactus Fruit / Cactus Fruit | Desert / Foraging / , / Oasis |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cave Carrot / Cave Carrot | The Mines / , either smashing boxes or / tilling / soil |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Mushroom / Red Mushroom | Foraging / in / The Mines / , / Summer / or / Fall / Foraging / in the / Secret Woods / , / The Farm Cave / (mushroom option), / Tapping / a / Mushroom Tree / , / Forest Farm Map / in / Fall |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Purple Mushroom / Purple Mushroom | The Mines / , / The Farm Cave / (mushroom option), / Forest Farm Map / Foraging / in / Fall |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Maple Syrup / Maple Syrup | Tapped / Maple Tree |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Oak Resin / Oak Resin | Tapped / Oak Tree / , / Haunted Skull |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pine Tar / Pine Tar | Tapped / Pine Tree |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Morel / Morel | Foraging / in the / Secret Woods / or / Forest Farm Map / in / Spring / , / The Farm Cave / (mushroom option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Autumn's Bounty / Autumn's Bounty / (5) | Autumn's Bounty / Autumn's Bounty / (5) |

### 1.9 Pantry — Bundle Complete Balloon

| Bundle Complete Balloon | Pantry / Reward | Greenhouse |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.10 Pantry — Bundle Green / Spring Crops Bundle

| Bundle Green / Spring Crops Bundle | Bundle Green / Spring Crops Bundle | Bundle Green / Spring Crops Bundle | Bundle Green / Spring Crops Bundle |
|---|---|---|---|
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Parsnip / Parsnip | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Green Bean / Green Bean | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cauliflower / Cauliflower | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Potato / Potato | Spring / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Speed-Gro / Speed-Gro / (20) | Speed-Gro / Speed-Gro / (20) |

### 1.11 Pantry — Bundle Yellow / Summer Crops Bundle

| Bundle Yellow / Summer Crops Bundle | Bundle Yellow / Summer Crops Bundle | Bundle Yellow / Summer Crops Bundle | Bundle Yellow / Summer Crops Bundle |
|---|---|---|---|
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tomato / Tomato | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Hot Pepper / Hot Pepper | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Blueberry / Blueberry | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Melon / Melon | Summer / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Quality Sprinkler / Quality Sprinkler / (1) | Quality Sprinkler / Quality Sprinkler / (1) |

### 1.12 Pantry — Bundle Orange / Fall Crops Bundle

| Bundle Orange / Fall Crops Bundle | Bundle Orange / Fall Crops Bundle | Bundle Orange / Fall Crops Bundle | Bundle Orange / Fall Crops Bundle |
|---|---|---|---|
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Corn / Corn | Summer / Fall / Crops |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Eggplant / Eggplant | Fall / Crops |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pumpkin / Pumpkin | Fall / Crops |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Yam / Yam | Fall / Crops / , dropped by / Duggies / on floors 6-29 of / The Mines / (3%) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Bee House / Bee House / (1) | Bee House / Bee House / (1) |

### 1.13 Pantry — Bundle Teal / Quality Crops Bundle

| Bundle Teal / Quality Crops Bundle | Bundle Teal / Quality Crops Bundle | Bundle Teal / Quality Crops Bundle | Bundle Teal / Quality Crops Bundle |
|---|---|---|---|
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Parsnip / Gold Quality Icon / Parsnip / (5) | Gold quality / Spring / Crops |
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Melon / Gold Quality Icon / Melon / (5) | Gold quality / Summer / Crops |
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Pumpkin / Gold Quality Icon / Pumpkin / (5) | Gold quality / Fall / Crops |
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Corn / Gold Quality Icon / Corn / (5) | Gold quality / Summer / Fall / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Preserves Jar / Preserves Jar / (1) | Preserves Jar / Preserves Jar / (1) |

### 1.14 Pantry — Bundle Red / Animal Bundle

| Bundle Red / Animal Bundle | Bundle Red / Animal Bundle | Bundle Red / Animal Bundle | Bundle Red / Animal Bundle |
|---|---|---|---|
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Milk / Large Milk | Cows |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Brown Egg / Large Egg / (Brown) | Brown / Chickens |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Egg / Large Egg | White / Chickens |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Goat Milk / Large Goat Milk | Goats |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wool / Wool | Sheep / , / Rabbits |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Duck Egg / Duck Egg | Ducks |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Cheese Press / Cheese Press / (1) | Cheese Press / Cheese Press / (1) |

### 1.15 Pantry — Bundle Purple / Artisan Bundle

| Bundle Purple / Artisan Bundle | Bundle Purple / Artisan Bundle | Bundle Purple / Artisan Bundle | Bundle Purple / Artisan Bundle |
|---|---|---|---|
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Truffle Oil / Truffle Oil | Made from / Truffles / using an / Oil Maker |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cloth / Cloth | Loom / , / Recycling / a / Soggy Newspaper / , / Desert Trader / , dropped by / Mummies / in / Skull Cavern |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Goat Cheese / Goat Cheese | Cheese Press |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cheese / Cheese | Cheese Press / , / Desert Trader |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Honey / Honey | Bee House / , / Oasis |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Jelly / Jelly | Preserves Jar |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Apple / Apple | Apple Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Apricot / Apricot | Apricot Trees / during / Spring / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Orange / Orange | Orange Trees / during / Summer / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Peach / Peach | Peach Trees / during / Summer / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pomegranate / Pomegranate | Pomegranate Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cherry / Cherry | Cherry Trees / during / Spring / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Keg / Keg / (1) | Keg / Keg / (1) |

### 1.16 Fish Tank — Bundle Complete Balloon

| Bundle Complete Balloon | Fish / Tank / Reward | Glittering Boulder / Removed |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.17 Fish Tank — Bundle Teal / River Fish Bundle

| Bundle Teal / River Fish Bundle | Bundle Teal / River Fish Bundle | Bundle Teal / River Fish Bundle | Bundle Teal / River Fish Bundle |
|---|---|---|---|
| All River Fish can be found in the / Riverlands Farm / , / Hill-Top Farm / , or / Forest Farm / . | All River Fish can be found in the / Riverlands Farm / , / Hill-Top Farm / , or / Forest Farm / . | All River Fish can be found in the / Riverlands Farm / , / Hill-Top Farm / , or / Forest Farm / . | All River Fish can be found in the / Riverlands Farm / , / Hill-Top Farm / , or / Forest Farm / . |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sunfish / Sunfish | Found in Rivers, 6am – 7pm, / Spring / and / Summer / during sunny weather |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Catfish / Catfish | Found in Rivers and / Secret Woods / , 6am – midnight, / Spring / and / Fall / . Only when raining / Can be found in / Summer / during rain in the / Secret Woods / and / Witch's Swamp / , / Winter / with a / Rain Totem |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Shad / Shad | Found in Rivers, 9am – 2am, / Spring / , / Summer / , and / Fall / . Only when raining |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tiger Trout / Tiger Trout | Found in Rivers, 6am – 7pm, / Fall / and / Winter / . Can be found in any / weather |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Deluxe Bait / Deluxe Bait / (30) | Deluxe Bait / Deluxe Bait / (30) |

### 1.18 Fish Tank — Bundle Green / Lake Fish Bundle

| Bundle Green / Lake Fish Bundle | Bundle Green / Lake Fish Bundle | Bundle Green / Lake Fish Bundle | Bundle Green / Lake Fish Bundle |
|---|---|---|---|
| All Mountain Lake Fish can be found in any / weather / , and in the / Wilderness Farm / . | All Mountain Lake Fish can be found in any / weather / , and in the / Wilderness Farm / . | All Mountain Lake Fish can be found in any / weather / , and in the / Wilderness Farm / . | All Mountain Lake Fish can be found in any / weather / , and in the / Wilderness Farm / . |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Largemouth Bass / Largemouth Bass | Found in the Mountain Lake, 6am – 7pm, All Seasons |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Carp / Carp | Found in the Mountain Lake, Anytime, during / Spring / , / Summer / , or / Fall / Found in / Secret Woods / or / Sewer / , Anytime, All Seasons |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Bullhead / Bullhead | Found in the Mountain Lake, Anytime, All Seasons |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sturgeon / Sturgeon | Found in the Mountain Lake, 6am – 7pm, / Summer / and / Winter |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Dressed Spinner / Dressed Spinner / (1) | Dressed Spinner / Dressed Spinner / (1) |

### 1.19 Fish Tank — Bundle Blue / Ocean Fish Bundle

| Bundle Blue / Ocean Fish Bundle | Bundle Blue / Ocean Fish Bundle | Bundle Blue / Ocean Fish Bundle | Bundle Blue / Ocean Fish Bundle |
|---|---|---|---|
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sardine / Sardine | Found in the Ocean, 6am – 7pm, / Spring / , / Fall / , and / Winter |
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tuna / Tuna | Found in the Ocean, 6am – 7pm, / Summer / and / Winter |
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Snapper / Red Snapper | Found in the Ocean, 6am – 7pm, / Summer / and / Fall / . Only when raining |
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tilapia / Tilapia | Found in the Ocean, 6am – 2pm, / Summer / and / Fall |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Warp Totem Beach / Warp Totem: Beach / (5) | Warp Totem Beach / Warp Totem: Beach / (5) |

### 1.20 Fish Tank — Bundle Purple / Night Fishing Bundle

| Bundle Purple / Night Fishing Bundle | Bundle Purple / Night Fishing Bundle | Bundle Purple / Night Fishing Bundle | Bundle Purple / Night Fishing Bundle |
|---|---|---|---|
| Night Fishing Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Walleye / Walleye | Found in Rivers, the Mountain Lake, and Cindersap Forest Pond, 12pm – 2am, / Fall / ( / Winter / with / Rain Totem / .) Only when raining |
| Night Fishing Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Bream / Bream | Found in Rivers, 6pm – 2am, All Seasons |
| Night Fishing Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Eel / Eel | Found in the Ocean, 4pm – 2am, / Spring / or / Fall / . Only when raining |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Glow Ring / Glow Ring / (1) | Glow Ring / Glow Ring / (1) |

### 1.21 Fish Tank — Bundle Purple / Crab Pot Bundle

| Bundle Purple / Crab Pot Bundle | Bundle Purple / Crab Pot Bundle | Bundle Purple / Crab Pot Bundle | Bundle Purple / Crab Pot Bundle |
|---|---|---|---|
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Lobster / Lobster | Caught in / Crab Pots / (ocean) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crayfish / Crayfish | Caught in / Crab Pots / (freshwater) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crab / Crab | Caught in / Crab Pots / (ocean), drops from / Rock Crabs / or / Lava Crabs / in / The Mines |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cockle / Cockle | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Mussel / Mussel | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Shrimp / Shrimp | Caught in / Crab Pots / (ocean) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Snail / Snail | Caught in / Crab Pots / (freshwater) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Periwinkle / Periwinkle | Caught in / Crab Pots / (freshwater) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Oyster / Oyster | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Clam / Clam | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Crab Pot / Crab Pot / (3) | Crab Pot / Crab Pot / (3) |

### 1.22 Fish Tank — Bundle Red / Specialty Fish Bundle

| Bundle Red / Specialty Fish Bundle | Bundle Red / Specialty Fish Bundle | Bundle Red / Specialty Fish Bundle | Bundle Red / Specialty Fish Bundle |
|---|---|---|---|
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pufferfish / Pufferfish | Found in the Ocean, 12pm – 4pm, / Summer / during sunny weather |
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Ghostfish / Ghostfish | Found in ponds in / The Mines / floors 20 and 60, Anytime, All Seasons. May also be dropped by / Ghosts |
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sandfish / Sandfish | Found in the pond in / The Desert / , 6am – 8pm, All Seasons |
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Woodskip / Woodskip | Found in the / Secret Woods / and the / Forest Farm / , Anytime, All Seasons |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Dish O' The Sea / Dish O' The Sea / (5) | Dish O' The Sea / Dish O' The Sea / (5) |

### 1.23 Boiler Room — Bundle Complete Balloon

| Bundle Complete Balloon | Boiler / Room / Reward | Minecarts / Repaired |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.24 Boiler Room — Bundle Orange / Blacksmith's Bundle

| Bundle Orange / Blacksmith's Bundle | Bundle Orange / Blacksmith's Bundle | Bundle Orange / Blacksmith's Bundle | Bundle Orange / Blacksmith's Bundle |
|---|---|---|---|
| Blacksmith Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Copper Bar / Copper Bar | Smelting / Copper Ore / in the / Furnace |
| Blacksmith Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Iron Bar / Iron Bar | Smelting / Iron Ore / in the / Furnace / , / Crafting / the "Transmute (Fe)" recipe |
| Blacksmith Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Gold Bar / Gold Bar | Smelting / Gold Ore / in the / Furnace / , / Crafting / the "Transmute (Au)" recipe |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Furnace / Furnace / (1) | Furnace / Furnace / (1) |

### 1.25 Boiler Room — Bundle Purple / Geologist's Bundle

| Bundle Purple / Geologist's Bundle | Bundle Purple / Geologist's Bundle | Bundle Purple / Geologist's Bundle | Bundle Purple / Geologist's Bundle |
|---|---|---|---|
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Quartz / Quartz | Foraging / on all floors of / The Mines |
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Earth Crystal / Earth Crystal | Foraging / on floors 1-39 of / The Mines / , / Geodes / , / Omni Geodes / , drop from / Duggies / in the Mines (floors 6-29) |
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Frozen Tear / Frozen Tear | Foraging / on floors 41-79 of / The Mines / , / Frozen Geodes / , / Omni Geodes / , drop from / Dust Sprites / in the Mines (floors 41-79) |
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fire Quartz / Fire Quartz | Foraging / on floors 81-119 of / The Mines / , / Magma Geodes / , / Omni Geodes |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Omni Geode / Omni Geode / (5) | Omni Geode / Omni Geode / (5) |

### 1.26 Boiler Room — Bundle Purple / Adventurer's Bundle

| Bundle Purple / Adventurer's Bundle | Bundle Purple / Adventurer's Bundle | Bundle Purple / Adventurer's Bundle | Bundle Purple / Adventurer's Bundle |
|---|---|---|---|
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Slime / Slime / (99) | Dropped by / Slimes |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Bat Wing / Bat Wing / (10) | Dropped by / Bats / in / The Mines / or the / Skull Cavern |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Solar Essence / Solar Essence | Dropped by / Ghosts / , / Squid Kids / , or / Metal Heads / in / The Mines / , dropped by / Mummies / or / Iridium Bats / in the / Skull Cavern / ; produced by / Sunfish / in / Fish Ponds / ; buy from / Krobus |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Void Essence / Void Essence | Dropped by / Shadow Brutes / or / Shadow Shamans / in / The Mines / or / Serpents / in the / Skull Cavern / ; produced by / Void Salmon / in / Fish Ponds / ; buy from / Krobus |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Small Magnet Ring / Small Magnet Ring / (1) | Small Magnet Ring / Small Magnet Ring / (1) |

### 1.27 Bulletin Board — Bundle Complete Balloon

| Bundle Complete Balloon | Bulletin / Board / Reward | Friendship / ♡ |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.28 Bulletin Board — Bundle Red / Chef's Bundle

| Bundle Red / Chef's Bundle | Bundle Red / Chef's Bundle | Bundle Red / Chef's Bundle | Bundle Red / Chef's Bundle |
|---|---|---|---|
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Maple Syrup / Maple Syrup | Tapped / Maple Tree |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fiddlehead Fern / Fiddlehead Fern | Summer / Foraging / in the / Secret Woods / , Foraging on Prehistoric Floors at the / Skull Cavern / , Cutting down / Green Rain Trees |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Truffle / Truffle | Pigs |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Poppy / Poppy | Summer / Crops |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Maki Roll / Maki Roll | Cooking / (recipe sources: / The Queen of Sauce / , / The Saloon / ) |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fried Egg / Fried Egg | Cooking |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Pink Cake / Pink Cake / (3) | Pink Cake / Pink Cake / (3) |

### 1.29 Bulletin Board — Bundle Teal / Dye Bundle

| Bundle Teal / Dye Bundle | Bundle Teal / Dye Bundle | Bundle Teal / Dye Bundle | Bundle Teal / Dye Bundle |
|---|---|---|---|
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Mushroom / Red Mushroom | Foraging / in / The Mines / , / Summer / or / Fall / Foraging / in the / Secret Woods / , / The Farm Cave / (mushroom option), / Tapping / a / Mushroom Tree |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sea Urchin / Sea Urchin | Beach / Foraging / , after using 300 / wood / to fix the bridge to the right side of / The Beach / or any side of the beach during / crab mating season / ; foraging in the Beach Farm |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sunflower / Sunflower | Summer / Fall / Crops |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Duck Feather / Duck Feather | Ducks |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Aquamarine / Aquamarine | Aquamarine Nodes / , boxes in / The Mines / , / Fishing Treasure Chests |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Cabbage / Red Cabbage | Summer / Crops / ( / Red Cabbage Seeds / are available at / Pierre's General Store / in year 2+, at the / Traveling Cart / , or dropped by / Serpents / , / Mummies / , and / Purple Slimes / ) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Seed Maker / Seed Maker / (1) | Seed Maker / Seed Maker / (1) |

### 1.30 Bulletin Board — Bundle Blue / Field Research Bundle

| Bundle Blue / Field Research Bundle | Bundle Blue / Field Research Bundle | Bundle Blue / Field Research Bundle | Bundle Blue / Field Research Bundle |
|---|---|---|---|
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Purple Mushroom / Purple Mushroom | The Mines / , / The Farm Cave / (mushroom option), / Forest Farm Map / Foraging / in / Fall |
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Nautilus Shell / Nautilus Shell | Winter / Beach / Foraging / , / Beach Farm Map / Foraging / during any season, Random gift from / Demetrius / (Note: NOT the / Nautilus Fossil / artifact) |
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Chub / Chub | Can be found in the mountain lake and river during all seasons, any time |
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Frozen Geode / Frozen Geode | The Mines / floors 41-79 |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Recycling Machine / Recycling Machine / (1) | Recycling Machine / Recycling Machine / (1) |

### 1.31 Bulletin Board — Bundle Yellow / Fodder Bundle

| Bundle Yellow / Fodder Bundle | Bundle Yellow / Fodder Bundle | Bundle Yellow / Fodder Bundle | Bundle Yellow / Fodder Bundle |
|---|---|---|---|
| Fodder Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Wheat / Wheat / (10) | Summer / Fall / Crops |
| Fodder Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Hay / Hay / (10) | Purchase at / Marnie's Ranch / or / Desert Trader / , or harvest from / Grass / or / Wheat / . |
| Fodder Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Apple / Apple / (3) | Apple Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Heater / Heater / (1) | Heater / Heater / (1) |

### 1.32 Bulletin Board — Bundle Purple / Enchanter's Bundle

| Bundle Purple / Enchanter's Bundle | Bundle Purple / Enchanter's Bundle | Bundle Purple / Enchanter's Bundle | Bundle Purple / Enchanter's Bundle |
|---|---|---|---|
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Oak Resin / Oak Resin | Tapped / Oak Tree |
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wine / Wine | Keg |
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Rabbit's Foot / Rabbit's Foot | Rabbits / , / Serpent / drop in / Skull Cavern / (0.8%), / Cat / (1.7%) |
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pomegranate / Pomegranate | Pomegranate Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Gold Bar / Gold Bar / (5) | Gold Bar / Gold Bar / (5) |

### 1.33 Vault — Bundle Complete Balloon

| Bundle Complete Balloon | Vault / Reward | Bus Repair |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.34 Vault — Bundle Red / 2,500 Bundle

| Bundle Red / 2,500 Bundle | Bundle Red / 2,500 Bundle |
|---|---|
| 2500 Bundle | Bundle Purchase / Gold / 2,500g |
| Bundle Reward / Reward: | Chocolate Cake / Chocolate Cake / (3) |

### 1.35 Vault — Bundle Orange / 5,000 Bundle

| Bundle Orange / 5,000 Bundle | Bundle Orange / 5,000 Bundle |
|---|---|
| 5000 Bundle | Bundle Purchase / Gold / 5,000g |
| Bundle Reward / Reward: | Quality Fertilizer / Quality Fertilizer / (30) |

### 1.36 Vault — Bundle Yellow / 10,000 Bundle

| Bundle Yellow / 10,000 Bundle | Bundle Yellow / 10,000 Bundle |
|---|---|
| 10000 Bundle | Bundle Purchase / Gold / 10,000g |
| Bundle Reward / Reward: | Lightning Rod / Lightning Rod / (1) |

### 1.37 Vault — Bundle Purple / 25,000 Bundle

| Bundle Purple / 25,000 Bundle | Bundle Purple / 25,000 Bundle |
|---|---|
| 25000 Bundle | Bundle Purchase / Gold / 25,000g |
| Bundle Reward / Reward: | Crystalarium / Crystalarium / (1) |

### 1.38 Abandoned JojaMart — Bundle Complete Balloon

| Bundle Complete Balloon | Missing / Bundle / Reward | Movie Theater |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 1.39 Abandoned JojaMart — Bundle Purple / The Missing Bundle

| Bundle Purple / The Missing Bundle | Bundle Purple / The Missing Bundle | Bundle Purple / The Missing Bundle | Bundle Purple / The Missing Bundle |
|---|---|---|---|
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | —（固定源空白） | —（固定源空白） |
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wine / Silver Quality Icon / Silver or better quality / Wine / (any) | Cask / , / Ginger Island / resort |
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Dinosaur Mayonnaise / Dinosaur Mayonnaise | Mayonnaise Machine |
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Prismatic Shard / Prismatic Shard | Mining |
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Ancient Fruit / Gold Quality Icon / Gold quality / Ancient Fruit / (5) | Crops |
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Void Salmon / Gold Quality Icon / Gold or Iridium quality / Void Salmon | Fishing / in the / Witch's Swamp |
| The Missing Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Caviar / Caviar | Preserves Jar / product from / Sturgeon / roe |

### 1.40 非表格规则事实

| 来源章节 | 完整规则事实 |
|---|---|
| Introduction | For remixed bundles chosen at game start via / advanced options / , see / Remixed Bundles / . |
| Introduction | Bundles / are donations to the / Junimos / given via golden scrolls inside the / Community Center / . When a bundle is complete, the Junimos offer the player a reward. When all bundles for a particular room in the Community Center are complete, the Junimos grant a special reward that sometimes benefits the entire community. |
| Introduction | Bundle rewards are given immediately, but rewards for completing all bundles in a room are given at the end of the day via a cutscene depicting the Junimos fulfilling the reward. If two rooms are completed on the same day, only one of the cutscenes is shown. Note that if the player does not collect individual bundle rewards before completing the room, the rewards can be found in a small brown bag to the left of the Junimo Hut after the golden scroll disappears. This bag persists after the / Community Center / completion ceremony, until all items are retrieved from it. |
| Introduction | A few bundles display more items than there are slots to fill ( / e.g., / Artisan Bundle: 12 items, 6 slots to fill). In this case, the player can choose which of the shown items they want to use to fill the bundle. They do / not / have to use / all / shown items, only enough to fill the slots. |
| Introduction | Completing all bundles restores the Community Center to its condition when it was brand new and unlocks the / "Local Legend" / Steam achievement. That night, the game also unlocks a cut scene that shows the grand re-opening of the Community Center. This scene is triggered by entering / Pelican Town / Square any time thereafter on a sunny day, unless a festival is to be held in the town that day. Mayor Lewis announces that the player has won the Stardew Hero award and gives the player a trophy. |
| Introduction | If the player opts to purchase a / JojaMart / Membership, the Community Center is turned into a / Joja Warehouse / instead. After this happens, the bundles will be completed by the Joja Corporation for a fee given to / Morris / , the local JojaMart manager, through the / Joja Community Development Form / . |
| Introduction | There is a total of 6 rooms and 30 bundles to complete in the Community Center. In the Joja Warehouse, there are 5 rewards to purchase (the "Friendship" reward is not available). |
| Introduction | Bundle Progress can be checked at any time / by clicking on the Golden Scroll icon at the top right of the Player Menu (above the Garbage Can and "organize" icons). Selecting or hovering the mouse pointer over an inventory item that is needed for a bundle makes the Golden Scroll icon pulsate. |
| Introduction | Bundles that do not specify quality will accept items of any quality. / For bundles that need multiple items, multiple stacks of different qualities are acceptable as long as they add up to the required amount. For bundles that do specify a quality, a better quality is also acceptable. |
| Traveling Cart Availability | All items required for bundles have a small chance of appearing in the / Traveling Cart / , except for the items listed below. These items will never be sold at the Traveling Cart: |
| Traveling Cart Availability | *Used only in / Remixed Bundles |
| Crafts Room | The Crafts Room contains the first group of bundles available. Completing all Crafts Room bundles repairs the bridge east of / The Mines / , unlocking the / Quarry / . |
| Pantry | The Pantry appears after completing one bundle. Completing all Pantry bundles will restore the dilapidated / Greenhouse / on the farm, making it available to grow / Crops / , / Fruit Trees / , and / Trees / year-round. |
| Fish Tank | The Fish Tank appears after completing one bundle. Completing all Fish Tank bundles will remove the Glittering Boulder to the left of / The Mines / entrance. / Willy / will also give the player a / Copper Pan / that can be used to collect metal ores and other items from bodies of water. Upon completion, the broken fish tank will turn into an / actual Fish Tank / , containing 1 / Catfish / , 1 / Sunfish / , and 1 / Snail / . Players can then add up to 5 bottom creatures and 5 swimming creatures into the tank and 1 of each decoration type: / Seaweed / , / Coral / , / Stone / , / Anchor / , / Treasure Chest / , / Pineapple / , / Ancient Sword / , / Hardwood / , / Nautilus Shell / , / Rainbow Shell / , / Joja Cola / , / Lucky Purple Shorts / , / Clay / , and / Pearl / , similarly to other fish tanks like the / Deluxe Fish Tank / and the / Aquatic Sanctuary / . The appearance and location of / Seaweed / , / Coral / , and other stationary objects in the tank can't be changed because the tank can't be moved by players. |
| Fish Tank | Note: / Access to / the Desert / is required to get a / Sandfish / . Therefore, unless it becomes available at the / Traveling Cart / , it is not possible to finish the Specialty Fish Bundle before finishing the entire Vault section. |
| Boiler Room | The Boiler Room appears after completing two bundles. Completing all Boiler Room bundles repairs the / Minecarts / , allowing the player to fast travel between distant locations. The Locations are / Bus Stop / , / Mines / , / Quarry / and / Town / . |
| Bulletin Board | The Bulletin Board appears after completing three bundles. |
| Bulletin Board | Completing all Bulletin Board bundles improves the player's / friendship / rating with every / non-datable villager / by two hearts (500 points). Note that this applies only to non-datable villagers whom the player has met in person. Villagers who do not show on the "Social" tab of the player menu and villagers whose names appear as "???' will not receive 500 points. If the player completes all the bundles before / Kent / arrives on 1 Spring, Year 2, he will not benefit from the friendship increase, and will start at 0 hearts. The / Dwarf / 's friendship will be unaffected if the player does not have the / Dwarvish Translation Guide / . |
| Bulletin Board | The morning after, Mayor / Lewis / will send a letter saying that packages containing items posted about "years ago" on the community center bulletin board have been appearing in villagers' homes. He says the packages are all addressed from "your farm". He expresses his gratitude and says "all of us in town are delighted!" The / friendship / bonus is applied when the Player opens the letter. |
| Vault | The Vault becomes available after completing four bundles. Pressing the large "purchase" button will purchase the bundle and deduct the gold from the total. |
| Vault | Completing all Vault bundles costs / Gold / 42,500g / , and repairs the / Bus Stop / . Taking the Bus grants access to / The Calico Desert / . |
| Abandoned JojaMart | After completing the / Community Center / , the first night before a rainy or stormy day, a cutscene will trigger in which a bolt of lightning strikes the abandoned / JojaMart / , opening its doors. Inside, the Missing Bundle can be found. |
| Remixed Bundles | Main article: / Remixed Bundles |

<a id="source-remixed-bundles"></a>
## 2. 混合收集包候选池（Remixed Bundles）

固定来源：[revision 191838](https://stardewvalleywiki.com/mediawiki/index.php?title=Remixed_Bundles&oldid=191838)；保留数据表 53 张、数据行 251、规则事实块 18。

### 2.1 Crafts Room — Bundle Complete Balloon

| Bundle Complete Balloon | Crafts / Room / Reward | Bridge Repair |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 2.2 Bundle 1 — Bundle Green / Spring Foraging Bundle (4 items chosen at random)

| Bundle Green / Spring Foraging Bundle (4 items chosen at random) | Bundle Green / Spring Foraging Bundle (4 items chosen at random) | Bundle Green / Spring Foraging Bundle (4 items chosen at random) | Bundle Green / Spring Foraging Bundle (4 items chosen at random) |
|---|---|---|---|
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wild Horseradish / Wild Horseradish | Spring / Foraging |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Daffodil / Daffodil | Spring / Foraging / , buy from / Pierre / at / Flower Dance |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Leek / Leek | Spring / Foraging |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Dandelion / Dandelion | Spring / Foraging / , buy from / Pierre / at / Flower Dance |
| Spring Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Spring Onion / Spring Onion | Spring / Foraging |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Spring Seeds / Spring Seeds / (30) | Spring Seeds / Spring Seeds / (30) |

### 2.3 Bundle 2 — Bundle Yellow / Summer Foraging Bundle

| Bundle Yellow / Summer Foraging Bundle | Bundle Yellow / Summer Foraging Bundle | Bundle Yellow / Summer Foraging Bundle | Bundle Yellow / Summer Foraging Bundle | —（固定源空白） |
|---|---|---|---|---|
| Summer Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Grape / Grape | Summer / Foraging / , / Fall / Farming | —（固定源空白） |
| Summer Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Spice Berry / Spice Berry | Summer / Foraging / , / The Farm Cave / (fruit bat option) | —（固定源空白） |
| Summer Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Sweet Pea / Sweet Pea | Summer / Foraging | —（固定源空白） |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Summer Seeds / Summer Seeds / (30) | Summer Seeds / Summer Seeds / (30) | Summer Seeds / Summer Seeds / (30) |

### 2.4 Bundle 3 — Bundle Orange / Fall Foraging Bundle

| Bundle Orange / Fall Foraging Bundle | Bundle Orange / Fall Foraging Bundle | Bundle Orange / Fall Foraging Bundle | Bundle Orange / Fall Foraging Bundle |
|---|---|---|---|
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Common Mushroom / Common Mushroom | Fall / Foraging / , / Spring / & / Fall / Foraging / in the / Secret Woods / , / The Farm Cave / (mushroom option), / Tapping / a / Mushroom Tree / , / Mushroom Log |
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wild Plum / Wild Plum | Fall / Foraging / , / The Farm Cave / (fruit bat option) |
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Hazelnut / Hazelnut | Fall / Foraging |
| Fall Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Blackberry / Blackberry | Fall / Foraging / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Fall Seeds / Fall Seeds / (30) | Fall Seeds / Fall Seeds / (30) |

### 2.5 Bundle 4 — Bundle Teal / Winter Foraging Bundle (4 items chosen at random)

| Bundle Teal / Winter Foraging Bundle (4 items chosen at random) | Bundle Teal / Winter Foraging Bundle (4 items chosen at random) | Bundle Teal / Winter Foraging Bundle (4 items chosen at random) | Bundle Teal / Winter Foraging Bundle (4 items chosen at random) |
|---|---|---|---|
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Winter Root / Winter Root | Tilling / soil or / Artifact Spots / in / Winter / , dropped by Blue / Slimes / on floors 41-79 of / The Mines |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crystal Fruit / Crystal Fruit | Winter / Foraging / , dropped by / Dust Sprites / on floors 41-79 of / The Mines |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Snow Yam / Snow Yam | Tilling / soil or / Artifact Spots / in / Winter |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crocus / Crocus | Winter / Foraging |
| Winter Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Holly / Holly | Winter / Foraging |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Winter Seeds / Winter Seeds / (30) | Winter Seeds / Winter Seeds / (30) |

### 2.6 Bundle 5 — Bundle Red / Construction Bundle

| Bundle Red / Construction Bundle | Bundle Red / Construction Bundle | Bundle Red / Construction Bundle | Bundle Red / Construction Bundle |
|---|---|---|---|
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wood / Wood / (99) | Chopping / Trees / or branches with an / Axe |
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wood / Wood / (99) | Chopping / Trees / or branches with an / Axe |
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Stone / Stone / (99) | Smashing stones with a / Pickaxe |
| Construction Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Hardwood / Hardwood / (10) | Chopping / Large Stumps / or / Large Logs / with an upgraded / Axe / , smashing crates in / The Mines / , cutting down / Mahogany trees |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Charcoal Kiln / Charcoal Kiln / (1) | Charcoal Kiln / Charcoal Kiln / (1) |

### 2.7 Bundle 5 — Bundle Yellow / Sticky Bundle

| Bundle Yellow / Sticky Bundle | Bundle Yellow / Sticky Bundle | Bundle Yellow / Sticky Bundle | Bundle Yellow / Sticky Bundle |
|---|---|---|---|
| Sticky Bundle | —（固定源空白） | —（固定源空白） | —（固定源空白） |
| Sticky Bundle | Bundle Slot | Sap / Sap / (500) | Chopping / Trees / , drop from / Slimes |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Charcoal Kiln / Charcoal Kiln / (1) | Charcoal Kiln / Charcoal Kiln / (1) |

### 2.8 Bundle 5 — Bundle Green / Forest Bundle (3 items chosen at random)

| Bundle Green / Forest Bundle (3 items chosen at random) | Bundle Green / Forest Bundle (3 items chosen at random) | Bundle Green / Forest Bundle (3 items chosen at random) | Bundle Green / Forest Bundle (3 items chosen at random) |
|---|---|---|---|
| Forest Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Moss / Moss / (10) | Chopping / Trees |
| Forest Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Fiber / Fiber / (200) | Destroying / Weeds / or harvesting / Fiber Seeds |
| Forest Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Acorn / Acorn / (10) | Shaking/Chopping / Oak Trees |
| Forest Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Maple Seed / Maple Seed / (10) | Shaking/Chopping / Maple Trees |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Charcoal Kiln / Charcoal Kiln / (1) | Charcoal Kiln / Charcoal Kiln / (1) |

### 2.9 Bundle 6 — Bundle Purple / Exotic Foraging Bundle

| Bundle Purple / Exotic Foraging Bundle | Bundle Purple / Exotic Foraging Bundle | Bundle Purple / Exotic Foraging Bundle | Bundle Purple / Exotic Foraging Bundle |
|---|---|---|---|
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Coconut / Coconut | Desert / Foraging |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cactus Fruit / Cactus Fruit | Desert / Foraging |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cave Carrot / Cave Carrot | The Mines / , either smashing boxes or / tilling / soil |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Mushroom / Red Mushroom | Foraging / in / The Mines / , / Summer / or / Fall / Foraging / in the / Secret Woods / , / The Farm Cave / (mushroom option), / Tapping / a / Mushroom Tree / , / Forest Farm Map / in / Fall / , / Mushroom Log |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Purple Mushroom / Purple Mushroom | The Mines / , / The Farm Cave / (mushroom option), / Forest Farm Map / , / Foraging / in / Fall / , / Mushroom Log |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Maple Syrup / Maple Syrup | Tapped / Maple Tree |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Oak Resin / Oak Resin | Tapped / Oak Tree |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pine Tar / Pine Tar | Tapped / Pine Tree |
| Exotic Foraging Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Morel / Morel | Foraging / in the / Secret Woods / or / Forest Farm Map / in / Spring / , / The Farm Cave / (mushroom option), / Mushroom Log |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Autumn's Bounty / Autumn's Bounty / (5) | Autumn's Bounty / Autumn's Bounty / (5) |

### 2.10 Bundle 6 — Bundle Green / Wild Medicine Bundle

| Bundle Green / Wild Medicine Bundle | Bundle Green / Wild Medicine Bundle | Bundle Green / Wild Medicine Bundle | Bundle Green / Wild Medicine Bundle |
|---|---|---|---|
| Wild Medicine Bundle | —（固定源空白） | —（固定源空白） | —（固定源空白） |
| Wild Medicine Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Purple Mushroom / Purple Mushroom / (5) | The Mines / , / The Farm Cave / (mushroom option), / Forest Farm Map / Foraging / in / Fall / , / Mushroom Log |
| Wild Medicine Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Fiddlehead Fern / Fiddlehead Fern / (5) | Summer / forage in the / Secret Woods / , Prehistoric levels in / Skull Cavern / , / Green Rain Trees |
| Wild Medicine Bundle | Bundle Slot / Bundle Slot / Bundle Slot | White Algae / White Algae / (5) | Fishing / , / Monster / drops |
| Wild Medicine Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Hops / Hops / (5) | Summer / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Cookout Kit / Cookout Kit / (2) | Cookout Kit / Cookout Kit / (2) |

### 2.11 Pantry — Bundle Complete Balloon

| Bundle Complete Balloon | Pantry / Reward | Greenhouse |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 2.12 Bundle 1 — Bundle Green / Spring Crops Bundle (4 items chosen at random)

| Bundle Green / Spring Crops Bundle (4 items chosen at random) | Bundle Green / Spring Crops Bundle (4 items chosen at random) | Bundle Green / Spring Crops Bundle (4 items chosen at random) | Bundle Green / Spring Crops Bundle (4 items chosen at random) |
|---|---|---|---|
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Parsnip / Parsnip | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Green Bean / Green Bean | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cauliflower / Cauliflower | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Potato / Potato | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Kale / Kale | Spring / Crops |
| Spring Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Carrot / Carrot | Spring / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Speed-Gro / Speed-Gro / (20) | Speed-Gro / Speed-Gro / (20) |

### 2.13 Bundle 2 — Bundle Yellow / Summer Crops Bundle (4 items chosen at random)

| Bundle Yellow / Summer Crops Bundle (4 items chosen at random) | Bundle Yellow / Summer Crops Bundle (4 items chosen at random) | Bundle Yellow / Summer Crops Bundle (4 items chosen at random) | Bundle Yellow / Summer Crops Bundle (4 items chosen at random) |
|---|---|---|---|
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tomato / Tomato | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Hot Pepper / Hot Pepper | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Blueberry / Blueberry | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Melon / Melon | Summer / Crops |
| Summer Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Summer Squash / Summer Squash | Summer / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Quality Sprinkler / Quality Sprinkler / (1) | Quality Sprinkler / Quality Sprinkler / (1) |

### 2.14 Bundle 3 — Bundle Orange / Fall Crops Bundle (4 items chosen at random)

| Bundle Orange / Fall Crops Bundle (4 items chosen at random) | Bundle Orange / Fall Crops Bundle (4 items chosen at random) | Bundle Orange / Fall Crops Bundle (4 items chosen at random) | Bundle Orange / Fall Crops Bundle (4 items chosen at random) |
|---|---|---|---|
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Corn / Corn | Summer / Fall / Crops |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Eggplant / Eggplant | Fall / Crops |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pumpkin / Pumpkin | Fall / Crops |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Yam / Yam | Fall / Crops / , dropped by / Duggies / on floors 6-29 of / The Mines / (3%) |
| Fall Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Broccoli / Broccoli | Fall / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Bee House / Bee House / (1) | Bee House / Bee House / (1) |

### 2.15 Bundle 4 — Bundle Teal / Quality Crops Bundle

| Bundle Teal / Quality Crops Bundle | Bundle Teal / Quality Crops Bundle | Bundle Teal / Quality Crops Bundle | Bundle Teal / Quality Crops Bundle |
|---|---|---|---|
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Parsnip / Gold Quality Icon / Parsnip / (5) / Green Bean / Gold Quality Icon / Green Bean / (5) / Potato / Gold Quality Icon / Potato / (5) / Cauliflower / Gold Quality Icon / Cauliflower / (5) | Gold quality / Spring / Crops |
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Melon / Gold Quality Icon / Melon / (5) / Blueberry / Gold Quality Icon / Blueberry / (5) / Hot Pepper / Gold Quality Icon / Hot Pepper / (5) | Gold quality / Summer / Crops |
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Pumpkin / Gold Quality Icon / Pumpkin / (5) / Yam / Gold Quality Icon / Yam / (5) / Eggplant / Gold Quality Icon / Eggplant / (5) | Gold quality / Fall / Crops |
| Quality Crops Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Corn / Gold Quality Icon / Corn / (5) | Gold quality / Summer / Fall / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Preserves Jar / Preserves Jar / (1) | Preserves Jar / Preserves Jar / (1) |

### 2.16 Bundle 4 — Bundle Teal / Rare Crops Bundle

| Bundle Teal / Rare Crops Bundle | Bundle Teal / Rare Crops Bundle | Bundle Teal / Rare Crops Bundle | Bundle Teal / Rare Crops Bundle |
|---|---|---|---|
| Rare Crops Bundle | Bundle Slot | Ancient Fruit / Ancient Fruit | Spring / Summer / Fall / Crops / ; seed obtained from / Ancient Seed artifact |
| Rare Crops Bundle | Bundle Slot | Sweet Gem Berry / Sweet Gem Berry | Fall / Crops / ; / Rare Seed / purchased from / Traveling Cart |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Preserves Jar / Preserves Jar / (1) | Preserves Jar / Preserves Jar / (1) |

### 2.17 Bundle 5 — Bundle Red / Animal Bundle

| Bundle Red / Animal Bundle | Bundle Red / Animal Bundle | Bundle Red / Animal Bundle | Bundle Red / Animal Bundle |
|---|---|---|---|
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Milk / Large Milk | Cows |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Brown Egg / Large Egg / (Brown) | Chickens |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Egg / Large Egg | Chickens |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Large Goat Milk / Large Goat Milk | Goats |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wool / Wool | Sheep / , / Rabbits |
| Animal Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Duck Egg / Duck Egg | Ducks |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Cheese Press / Cheese Press / (1) | Cheese Press / Cheese Press / (1) |

### 2.18 Bundle 5 — Bundle Blue / Fish Farmer's Bundle

| Bundle Blue / Fish Farmer's Bundle | Bundle Blue / Fish Farmer's Bundle | Bundle Blue / Fish Farmer's Bundle | Bundle Blue / Fish Farmer's Bundle |
|---|---|---|---|
| Fish Farmer's Bundle | Bundle Slot / Bundle Slot | Roe / Roe / (15) | Fish Pond / product from many / Fish / , / Fishing Treasure Chests |
| Fish Farmer's Bundle | Bundle Slot / Bundle Slot | Aged Roe / Aged Roe / (15) | Preserves Jar / product from / Roe |
| Fish Farmer's Bundle | Bundle Slot / Bundle Slot | Squid Ink / Squid Ink | Squid Kid / drop; / Fish Pond / product from / Squid / and / Midnight Squid |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Worm Bin / Worm Bin / (1) | Worm Bin / Worm Bin / (1) |

### 2.19 Bundle 5 — Bundle Red / Garden Bundle

| Bundle Red / Garden Bundle | Bundle Red / Garden Bundle | Bundle Red / Garden Bundle | Bundle Red / Garden Bundle |
|---|---|---|---|
| Garden Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tulip / Tulip | Spring / Crops |
| Garden Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Blue Jazz / Blue Jazz | Spring / Crops |
| Garden Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Summer Spangle / Summer Spangle | Summer / Crops |
| Garden Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sunflower / Sunflower | Summer / Fall / Crops |
| Garden Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fairy Rose / Fairy Rose | Fall / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Quality Sprinkler / Quality Sprinkler / (1) | Quality Sprinkler / Quality Sprinkler / (1) |

### 2.20 Bundle 6 — Bundle Purple / Artisan Bundle

| Bundle Purple / Artisan Bundle | Bundle Purple / Artisan Bundle | Bundle Purple / Artisan Bundle | Bundle Purple / Artisan Bundle |
|---|---|---|---|
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Truffle Oil / Truffle Oil | Oil Maker / product from / Truffle |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cloth / Cloth | Loom / , / Recycling / a / Soggy Newspaper / , / Desert Trader |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Goat Cheese / Goat Cheese | Cheese Press |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cheese / Cheese | Cheese Press / , / Desert Trader |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Honey / Honey | Bee House / , / Oasis |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Jelly / Jelly | Preserves Jar |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Apple / Apple | Apple Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Apricot / Apricot | Apricot Trees / during / Spring / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Orange / Orange | Orange Trees / during / Summer / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Peach / Peach | Peach Trees / during / Summer / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pomegranate / Pomegranate | Pomegranate Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Artisan Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cherry / Cherry | Cherry Trees / during / Spring / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Keg / Keg / (1) | Keg / Keg / (1) |

### 2.21 Bundle 6 — Bundle Orange / Brewer's Bundle

| Bundle Orange / Brewer's Bundle | Bundle Orange / Brewer's Bundle | Bundle Orange / Brewer's Bundle | Bundle Orange / Brewer's Bundle |
|---|---|---|---|
| Brewer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Mead / Mead | Keg / product from / Honey |
| Brewer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pale Ale / Pale Ale | Keg / product from / Hops |
| Brewer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wine / Wine | Keg / product from / Fruits |
| Brewer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Juice / Juice | Keg / product from / Vegetables |
| Brewer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Green Tea / Green Tea | Keg / product from / Tea Leaves |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Keg / Keg / (1) | Keg / Keg / (1) |

### 2.22 Fish Tank — Bundle Complete Balloon

| Bundle Complete Balloon | Fish / Tank / Reward | Glittering Boulder Removed |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 2.23 Bundle 1 — Bundle Teal / River Fish Bundle

| Bundle Teal / River Fish Bundle | Bundle Teal / River Fish Bundle | Bundle Teal / River Fish Bundle | Bundle Teal / River Fish Bundle |
|---|---|---|---|
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sunfish / Sunfish | Found in Rivers, 6am – 7pm, / Spring / , and / Summer / during sunny weather. / Found in the / Riverlands Farm / or in the / Wilderness Farm / pond during rainy weather. |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Catfish / Catfish | Found in Rivers and Secret Woods Pond 6am – midnight, / Spring / and / Fall / . Only when raining. |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Shad / Shad | Found in Rivers, 9am – 2am, / Spring / , / Summer / , and / Fall / . Only when raining. |
| River Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tiger Trout / Tiger Trout | Found in Rivers, 6am – 7pm, / Fall / and / Winter / . |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Deluxe Bait / Deluxe Bait / (30) | Deluxe Bait / Deluxe Bait / (30) |

### 2.24 Bundle 2 — Bundle Green / Lake Fish Bundle

| Bundle Green / Lake Fish Bundle | Bundle Green / Lake Fish Bundle | Bundle Green / Lake Fish Bundle | Bundle Green / Lake Fish Bundle |
|---|---|---|---|
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Largemouth Bass / Largemouth Bass | Found in the Mountain lake, 6am – 7pm, All Seasons. |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Carp / Carp | Found in the Mountain lake or / Cindersap Forest / pond, Anytime, during / Spring / , / Summer / , or / Fall / . / Found in / Secret Woods / or / Sewer / , Anytime, All Seasons. |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Bullhead / Bullhead | Found in the Mountain Lake, Anytime, All Seasons. |
| Lake Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sturgeon / Sturgeon | Found in the Mountain Lake, 6am – 7pm, / Summer / and / Winter / . |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Dressed Spinner / Dressed Spinner / (1) | Dressed Spinner / Dressed Spinner / (1) |

### 2.25 Bundle 3 — Bundle Blue / Ocean Fish Bundle

| Bundle Blue / Ocean Fish Bundle | Bundle Blue / Ocean Fish Bundle | Bundle Blue / Ocean Fish Bundle | Bundle Blue / Ocean Fish Bundle |
|---|---|---|---|
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sardine / Sardine | Found in the Ocean, 6am – 7pm, / Spring / , / Fall / , and / Winter / . |
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tuna / Tuna | Found in the Ocean, 6am – 7pm, / Summer / and / Winter / . |
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Snapper / Red Snapper | Found in the Ocean, 6am – 7pm, / Summer / and / Fall / . Only when raining. |
| Ocean Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tilapia / Tilapia | Found in the Ocean, 6am – 2pm, / Summer / and / Fall / . |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Warp Totem Beach / Warp Totem: Beach / (5) | Warp Totem Beach / Warp Totem: Beach / (5) |

### 2.26 Bundle 4 — Bundle Purple / Night Fishing Bundle

| Bundle Purple / Night Fishing Bundle | Bundle Purple / Night Fishing Bundle | Bundle Purple / Night Fishing Bundle | Bundle Purple / Night Fishing Bundle |
|---|---|---|---|
| Night Fishing Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Walleye / Walleye | Found in Rivers, Lakes and Forest Pond, 12pm – 2am, / Fall / ( / Winter / with / Rain Totem / ). Only when raining. |
| Night Fishing Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Bream / Bream | Found in Rivers, 6pm – 2am, All Seasons. |
| Night Fishing Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Eel / Eel | Found in the Ocean, 4pm – 2am, / Spring / or / Fall / . Only when raining. |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Glow Ring / Glow Ring / (1) | Glow Ring / Glow Ring / (1) |

### 2.27 Bundle 5 — Bundle Purple / Crab Pot Bundle

| Bundle Purple / Crab Pot Bundle | Bundle Purple / Crab Pot Bundle | Bundle Purple / Crab Pot Bundle | Bundle Purple / Crab Pot Bundle |
|---|---|---|---|
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Lobster / Lobster | Caught in / Crab Pots / (ocean) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crayfish / Crayfish | Caught in / Crab Pots / (freshwater) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Crab / Crab | Caught in / Crab Pots / (ocean), drops from / Rock Crabs / or / Lava Crabs / in / The Mines |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Cockle / Cockle | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Mussel / Mussel | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Shrimp / Shrimp | Caught in / Crab Pots / (ocean) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Snail / Snail | Caught in / Crab Pots / (freshwater) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Periwinkle / Periwinkle | Caught in / Crab Pots / (freshwater) |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Oyster / Oyster | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Crab Pot Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Clam / Clam | Caught in / Crab Pots / (ocean), / Beach / Foraging |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Crab Pot / Crab Pot / (3) | Crab Pot / Crab Pot / (3) |

### 2.28 Bundle 6 — Bundle Red / Specialty Fish Bundle

| Bundle Red / Specialty Fish Bundle | Bundle Red / Specialty Fish Bundle | Bundle Red / Specialty Fish Bundle | Bundle Red / Specialty Fish Bundle |
|---|---|---|---|
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pufferfish / Pufferfish | Found in the Ocean, 12pm – 4pm, / Summer / during sunny weather. |
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Ghostfish / Ghostfish | Found in ponds in / The Mines / floors 20 and 60, Anytime, All Seasons. May also be dropped by / Ghosts / . |
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sandfish / Sandfish | Found in the pond in / The Desert / , 6am – 8pm, All Seasons. |
| Specialty Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Woodskip / Woodskip | Found in the / Secret Woods / and the / Forest Farm / , Anytime, All Seasons. |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Dish O' The Sea / Dish O' The Sea / (5) | Dish O' The Sea / Dish O' The Sea / (5) |

### 2.29 Bundle 6 — Bundle Red / Quality Fish Bundle

| Bundle Red / Quality Fish Bundle | Bundle Red / Quality Fish Bundle | Bundle Red / Quality Fish Bundle | Bundle Red / Quality Fish Bundle | Bundle Red / Quality Fish Bundle | —（固定源空白） |
|---|---|---|---|---|---|
| Quality Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Largemouth Bass / Gold Quality Icon / Largemouth Bass | Largemouth Bass / Gold Quality Icon / Largemouth Bass | Mountain Lake or Wilderness Farm, all seasons | Mountain Lake or Wilderness Farm, all seasons |
| Quality Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Shad / Gold Quality Icon / Shad | Shad / Gold Quality Icon / Shad | River, when raining, all seasons except Winter | River, when raining, all seasons except Winter |
| Quality Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Tuna / Gold Quality Icon / Tuna | Tuna / Gold Quality Icon / Tuna | Ocean, Summer or Winter | Ocean, Summer or Winter |
| Quality Fish Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Walleye / Gold Quality Icon / Walleye | Walleye / Gold Quality Icon / Walleye | River, Mountain Lake, Forest Pond, or Forest Farm; when raining; Fall (or Winter w / Rain Totem / ) | River, Mountain Lake, Forest Pond, or Forest Farm; when raining; Fall (or Winter w / Rain Totem / ) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Dish O' The Sea / Dish O' The Sea / (5) | Dish O' The Sea / Dish O' The Sea / (5) | Dish O' The Sea / Dish O' The Sea / (5) | —（固定源空白） |

### 2.30 Bundle 6 — Bundle Red / Master Fisher's Bundle

| Bundle Red / Master Fisher's Bundle | Bundle Red / Master Fisher's Bundle | Bundle Red / Master Fisher's Bundle | Bundle Red / Master Fisher's Bundle |
|---|---|---|---|
| Master Fisher's Bundle | Bundle Slot / Bundle Slot | Lava Eel / Lava Eel | The Mines / on the 100th floor during all seasons |
| Master Fisher's Bundle | Bundle Slot / Bundle Slot | Scorpion Carp / Scorpion Carp | The Desert / during all seasons |
| Master Fisher's Bundle | Bundle Slot / Bundle Slot | Octopus / Octopus | Summer / in the / ocean / and (more rarely) in / Garbage Cans / , & submarine ride at the / Night Market / (≈2% chance). |
| Master Fisher's Bundle | Bundle Slot / Bundle Slot | Blobfish / Blobfish | Submarine ride at the / Night Market / ( / Winter / 15-17). |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Dish O' The Sea / Dish O' The Sea / (5) | Dish O' The Sea / Dish O' The Sea / (5) |

### 2.31 Boiler Room — Bundle Complete Balloon

| Bundle Complete Balloon | Boiler / Room / Reward | Minecarts / Repaired |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 2.32 Bundles — Bundle Orange / Blacksmith's Bundle

| Bundle Orange / Blacksmith's Bundle | Bundle Orange / Blacksmith's Bundle | Bundle Orange / Blacksmith's Bundle | Bundle Orange / Blacksmith's Bundle |
|---|---|---|---|
| Blacksmith Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Copper Bar / Copper Bar | Smelting / Copper Ore / in the / Furnace |
| Blacksmith Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Iron Bar / Iron Bar | Smelting / Iron Ore / in the / Furnace / , / Crafting / the "Transmute (Fe)" recipe |
| Blacksmith Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Gold Bar / Gold Bar | Smelting / Gold Ore / in the / Furnace / , / Crafting / the "Transmute (Au)" recipe |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Furnace / Furnace / (1) | Furnace / Furnace / (1) |

### 2.33 Bundles — Bundle Purple / Geologist's Bundle

| Bundle Purple / Geologist's Bundle | Bundle Purple / Geologist's Bundle | Bundle Purple / Geologist's Bundle | Bundle Purple / Geologist's Bundle |
|---|---|---|---|
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Quartz / Quartz | Foraging / on all floors of / The Mines |
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Earth Crystal / Earth Crystal | Foraging / on floors 1-39 of / The Mines / , / Geodes / , / Omni Geodes / , drop from / Duggies / in the Mines (floors 1-29) |
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Frozen Tear / Frozen Tear | Foraging / on floors 40-79 of / The Mines / , / Frozen Geodes / , / Omni Geodes / , drop from / Dust Sprites / in the Mines (floors 40-79) |
| Geologist's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fire Quartz / Fire Quartz | Foraging / on floors 80-120 of / The Mines / , / Magma Geodes / , / Omni Geodes |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Omni Geode / Omni Geode / (5) | Omni Geode / Omni Geode / (5) |

### 2.34 Bundles — Bundle Purple / Adventurer's Bundle (4 items chosen at random)

| Bundle Purple / Adventurer's Bundle (4 items chosen at random) | Bundle Purple / Adventurer's Bundle (4 items chosen at random) | Bundle Purple / Adventurer's Bundle (4 items chosen at random) | Bundle Purple / Adventurer's Bundle (4 items chosen at random) |
|---|---|---|---|
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Slime / Slime / (99) | Dropped by / Slimes |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Bat Wing / Bat Wing / (10) | Dropped by / Bats / in / The Mines / and the / Skull Cavern |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Solar Essence / Solar Essence | Dropped by / Ghosts / , / Squid Kids / , or / Metal Heads / in / The Mines / , or by / Mummies / in the / Skull Cavern / ; / Fish Pond / product from / Sunfish / ; buy from / Krobus |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Void Essence / Void Essence | Dropped by / Shadow Brutes / in / The Mines / or / Serpents / in the / Skull Cavern / ; / Fish Pond / product from / Void Salmon / ; buy from / Krobus |
| Adventurer's Bundle | Bundle Slot / Bundle Slot | Bone Fragment / Bone Fragment / (10) | Dropped by / Skeletons / in / The Mines / or crates and barrels in / Skull Cavern / , / Artifact Spots |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Small Magnet Ring / Small Magnet Ring / (1) | Small Magnet Ring / Small Magnet Ring / (1) |

### 2.35 Bundles — Bundle Yellow / Treasure Hunter's Bundle

| Bundle Yellow / Treasure Hunter's Bundle | Bundle Yellow / Treasure Hunter's Bundle | Bundle Yellow / Treasure Hunter's Bundle | Bundle Yellow / Treasure Hunter's Bundle |
|---|---|---|---|
| Treasure Hunter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Amethyst / Amethyst | Gem Node / or individual nodes for each gem type in / The Mines / ; / Panning / ; / Fishing Treasure Chests |
| Treasure Hunter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Aquamarine / Aquamarine | Gem Node / or individual nodes for each gem type in / The Mines / ; / Panning / ; / Fishing Treasure Chests |
| Treasure Hunter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Diamond / Diamond | Gem Node / or individual nodes for each gem type in / The Mines / ; / Panning / ; / Fishing Treasure Chests |
| Treasure Hunter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Emerald / Emerald | Gem Node / or individual nodes for each gem type in / The Mines / ; / Panning / ; / Fishing Treasure Chests |
| Treasure Hunter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Ruby / Ruby | Gem Node / or individual nodes for each gem type in / The Mines / ; / Panning / ; / Fishing Treasure Chests |
| Treasure Hunter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Topaz / Topaz | Gem Node / or individual nodes for each gem type in / The Mines / ; / Panning / ; / Fishing Treasure Chests |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Lucky Lunch / Lucky Lunch / (1) | Lucky Lunch / Lucky Lunch / (1) |

### 2.36 Bundles — Bundle Purple / Engineer's Bundle

| Bundle Purple / Engineer's Bundle | Bundle Purple / Engineer's Bundle | Bundle Purple / Engineer's Bundle | Bundle Purple / Engineer's Bundle |
|---|---|---|---|
| Engineer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Iridium Ore / Iridium Ore | Mines / , / Skull Cavern / , / Magma Geode / , / Omni Geode |
| Engineer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Battery Pack / Battery Pack | Lightning Rod / , purchase from / Traveling Cart |
| Engineer's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Refined Quartz / Refined Quartz / (5) | Furnace / product from / Quartz / or / Fire Quartz / , / Recycling Machine / product from / Broken Glasses / or / Broken CD |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Furnace / Furnace / (2) | Furnace / Furnace / (2) |

### 2.37 Bundles — Bundle Complete Balloon

| Bundle Complete Balloon | Bulletin / Board / Reward | Friendship / ♡ |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 2.38 Bundles — Bundle Red / Chef's Bundle

| Bundle Red / Chef's Bundle | Bundle Red / Chef's Bundle | Bundle Red / Chef's Bundle | Bundle Red / Chef's Bundle |
|---|---|---|---|
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Maple Syrup / Maple Syrup | Tapped / Maple Tree |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fiddlehead Fern / Fiddlehead Fern | Summer / Foraging / in the / Secret Woods |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Truffle / Truffle | Pigs |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Poppy / Poppy | Summer / Crops |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Maki Roll / Maki Roll | Cooking / (recipe sources: / The Queen of Sauce / , / The Saloon / ) |
| Chef's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Fried Egg / Fried Egg | Cooking |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Pink Cake / Pink Cake / (3) | Pink Cake / Pink Cake / (3) |

### 2.39 Bundles — Bundle Teal / Dye Bundle

| Bundle Teal / Dye Bundle | Bundle Teal / Dye Bundle | Bundle Teal / Dye Bundle | Bundle Teal / Dye Bundle |
|---|---|---|---|
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Mushroom / Red Mushroom / Beet / Beet | Foraging / in / The Mines / , / Summer / or / Fall / Foraging / in the / Secret Woods / , / The Farm Cave / (mushroom option), / Tapping / a / Mushroom Tree / , / Mushroom Log / Fall / Crops / , seeds purchased at / Oasis |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sea Urchin / Sea Urchin / Amaranth / Amaranth | Beach / Foraging / , after using 300 wood to fix the bridge to the right side of the beach / Fall / Crops |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Sunflower / Sunflower / Starfruit / Starfruit | Summer / Fall / Crops / Summer / Crops / , seeds purchased at / Oasis |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Duck Feather / Duck Feather / Cactus Fruit / Cactus Fruit | Ducks / Foraged in / Desert / ; Indoor-only / Crops / , seeds purchased at / Oasis |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Aquamarine / Aquamarine / Blueberry / Blueberry | Aquamarine Nodes / , boxes in / The Mines / , / Fishing Treasure Chests / Summer / Crops |
| Dye Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Red Cabbage / Red Cabbage / Iridium Bar / Iridium Bar | Summer / Crops / ( / Red Cabbage Seeds / are available at / Pierre's General Store / in year 2+) / Can be smelted in a furnace; Rarely obtained as a monster drop. |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Seed Maker / Seed Maker / (1) | Seed Maker / Seed Maker / (1) |

### 2.40 Bundles — Bundle Blue / Field Research Bundle

| Bundle Blue / Field Research Bundle | Bundle Blue / Field Research Bundle | Bundle Blue / Field Research Bundle | Bundle Blue / Field Research Bundle |
|---|---|---|---|
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Purple Mushroom / Purple Mushroom | The Mines / , / The Farm Cave / (mushroom option), / Forest Farm Map / Foraging / in / Fall / , / Mushroom Log |
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Nautilus Shell / Nautilus Shell | Winter / Beach / Foraging / (Note: NOT the / Nautilus Fossil / artifact) |
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Chub / Chub | Can be found in the mountain lake and river during all seasons, any time. |
| Field Research Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Frozen Geode / Frozen Geode | The Mines / floors 40-79 |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Recycling Machine / Recycling Machine / (1) | Recycling Machine / Recycling Machine / (1) |

### 2.41 Bundles — Bundle Yellow / Fodder Bundle

| Bundle Yellow / Fodder Bundle | Bundle Yellow / Fodder Bundle | Bundle Yellow / Fodder Bundle | Bundle Yellow / Fodder Bundle |
|---|---|---|---|
| Fodder Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Wheat / Wheat / (10) | Summer / Fall / Crops |
| Fodder Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Hay / Hay / (10) | Purchase at / Marnie's Ranch / or / Desert Trader / , or harvest from / Grass / or / Wheat / . |
| Fodder Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Apple / Apple / (3) | Apple Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Heater / Heater / (1) | Heater / Heater / (1) |

### 2.42 Bundles — Bundle Purple / Enchanter's Bundle

| Bundle Purple / Enchanter's Bundle | Bundle Purple / Enchanter's Bundle | Bundle Purple / Enchanter's Bundle | Bundle Purple / Enchanter's Bundle |
|---|---|---|---|
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Oak Resin / Oak Resin | Tapped / Oak Tree |
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Wine / Wine | Keg |
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Rabbit's Foot / Rabbit's Foot | Rabbits / , / Serpent / drop in / Skull Cavern / (0.8%) |
| Enchanter's Bundle | Bundle Slot / Bundle Slot / Bundle Slot / Bundle Slot | Pomegranate / Pomegranate | Pomegranate Trees / during / Fall / , / The Farm Cave / (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Gold Bar / Gold Bar / (5) | Gold Bar / Gold Bar / (5) |

### 2.43 Bundles — Bundle Green / Children's Bundle

| Bundle Green / Children's Bundle | Bundle Green / Children's Bundle | Bundle Green / Children's Bundle | Bundle Green / Children's Bundle |
|---|---|---|---|
| Children's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Salmonberry / Salmonberry / (10) | Spring / forage, days 15-18 only, Farm Cave (fruit bat option) |
| Children's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Cookie / Cookie | Cooking / recipe; random gift in mail from the player's mother or / Evelyn |
| Children's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Ancient Doll / Ancient Doll | Artifact / dug up from Mountain, Bus Stop, Forest, or Town; / Fishing Treasure Chests |
| Children's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Ice Cream / Ice Cream | Cooking / recipe; purchase from / Ice Cream Stand / during / Summer / , or from the / Oasis / on Sundays |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Battery Pack / Battery Pack / (3) | Battery Pack / Battery Pack / (3) |

### 2.44 Bundles — Bundle Orange / Forager's Bundle

| Bundle Orange / Forager's Bundle | Bundle Orange / Forager's Bundle | Bundle Orange / Forager's Bundle | Bundle Orange / Forager's Bundle |
|---|---|---|---|
| Forager's Bundle | Bundle Slot / Bundle Slot | Salmonberry / Salmonberry / (50) | Spring / forage, days 15-18 only, Farm Cave (fruit bat option) |
| Forager's Bundle | Bundle Slot / Bundle Slot | Blackberry / Blackberry / (50) | Fall / forage, especially days 8-11; / Fall Seeds |
| Forager's Bundle | Bundle Slot / Bundle Slot | Wild Plum / Wild Plum / (15) | Fall / forage, / Fall Seeds / , Farm Cave (fruit bat option) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Tapper / Tapper / (3) | Tapper / Tapper / (3) |

### 2.45 Bundles — Bundle Yellow / Home Cook's Bundle

| Bundle Yellow / Home Cook's Bundle | Bundle Yellow / Home Cook's Bundle | Bundle Yellow / Home Cook's Bundle | Bundle Yellow / Home Cook's Bundle |
|---|---|---|---|
| Home Cook's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Egg / Egg / (10) / ("any" - includes Duck, Void, and Ostrich, but not Dinosaur.) | Chicken |
| Home Cook's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Milk / Milk / (10) / ("any" - any size, including Goat) | Cow / , / Goat |
| Home Cook's Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Wheat Flour / Wheat Flour / (100) | Mill / product from / Wheat / , purchase from / Pierre's General Store |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Complete Breakfast / Complete Breakfast / (5) | Complete Breakfast / Complete Breakfast / (5) |

### 2.46 Bundles — Bundle Red / Helper's Bundle

| Bundle Red / Helper's Bundle | Bundle Red / Helper's Bundle | Bundle Red / Helper's Bundle | Bundle Red / Helper's Bundle |
|---|---|---|---|
| Helper's Bundle | Bundle Slot / Bundle Slot | Prize Ticket / Prize Ticket / (1) | Reward for / Help Wanted Quests |
| Helper's Bundle | Bundle Slot / Bundle Slot | Mystery Box / Mystery Box / (5) | Found through various means ( / Fishing / , / Mining / , chopping / Trees / ) |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Stardrop Tea / Stardrop Tea / (1) | Stardrop Tea / Stardrop Tea / (1) |

### 2.47 Bundles — Bundle Purple / Spirit's Eve Bundle

| Bundle Purple / Spirit's Eve Bundle | Bundle Purple / Spirit's Eve Bundle | Bundle Purple / Spirit's Eve Bundle | Bundle Purple / Spirit's Eve Bundle |
|---|---|---|---|
| Spirit's Eve Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Jack-O-Lantern / Jack-O-Lantern / (1) | Purchasable on / Spirit's Eve |
| Spirit's Eve Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Corn / Corn / (10) | Summer / Fall / Crops |
| Spirit's Eve Bundle | Bundle Slot / Bundle Slot / Bundle Slot | Bat Wing / Bat Wing / (10) | Dropped by / Bats / in / The Mines / or / Skull Cavern |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Complete Breakfast / Complete Breakfast / (5) | Complete Breakfast / Complete Breakfast / (5) |

### 2.48 Bundles — Bundle Red / Winter Star Bundle

| Bundle Red / Winter Star Bundle | Bundle Red / Winter Star Bundle | Bundle Red / Winter Star Bundle | Bundle Red / Winter Star Bundle |
|---|---|---|---|
| Winter Star Bundle | Bundle Slot / Bundle Slot | Holly / Holly / (5) | Winter / Foraging |
| Winter Star Bundle | Bundle Slot / Bundle Slot | Plum Pudding / Plum Pudding / (1) | Cooking / recipe from / Queen of Sauce |
| Winter Star Bundle | Bundle Slot / Bundle Slot | Stuffing / Stuffing / (1) | Cooking / recipe from / Pam's 7 Heart Event |
| Winter Star Bundle | Bundle Slot / Bundle Slot | Powdermelon / Powdermelon / (5) | Winter / Crops |
| Bundle Reward / Reward: | Bundle Reward / Reward: | Mystery Box / Mystery Box / (3) | Mystery Box / Mystery Box / (3) |

### 2.49 Bundles — Bundle Complete Balloon

| Bundle Complete Balloon | Vault / Reward | Bus Repair |
|---|---|---|
| —（固定源无独立表头） | —（固定源无独立表头） | —（固定源无独立表头） |

### 2.50 Bundles — Bundle Red / 2,500 Bundle

| Bundle Red / 2,500 Bundle | Bundle Red / 2,500 Bundle |
|---|---|
| 2500 Bundle | Bundle Purchase / Gold / 2,500g |
| Bundle Reward / Reward: | Chocolate Cake / Chocolate Cake / (3) |

### 2.51 Bundles — Bundle Orange / 5,000 Bundle

| Bundle Orange / 5,000 Bundle | Bundle Orange / 5,000 Bundle |
|---|---|
| 5000 Bundle | Bundle Purchase / Gold / 5,000g |
| Bundle Reward / Reward: | Quality Fertilizer / Quality Fertilizer / (30) |

### 2.52 Bundles — Bundle Yellow / 10,000 Bundle

| Bundle Yellow / 10,000 Bundle | Bundle Yellow / 10,000 Bundle |
|---|---|
| 10000 Bundle | Bundle Purchase / Gold / 10,000g |
| Bundle Reward / Reward: | Lightning Rod / Lightning Rod / (1) |

### 2.53 Bundles — Bundle Purple / 25,000 Bundle

| Bundle Purple / 25,000 Bundle | Bundle Purple / 25,000 Bundle |
|---|---|
| 25000 Bundle | Bundle Purchase / Gold / 25,000g |
| Bundle Reward / Reward: | Crystalarium / Crystalarium / (1) |

### 2.54 非表格规则事实

| 来源章节 | 完整规则事实 |
|---|---|
| Introduction | This page is about remixed bundles. For normal bundles, see / Bundles / . |
| Introduction | When creating a new game, there is an / option / to / remix / the Community Center / bundles / . A room can have a mix of permanent and random bundles. Permanent bundles will always be present, though the items may vary slightly from their standard counterparts. Random bundles may or may not be present. |
| Introduction | A few bundles display more items than there are slots to fill. In this case, the player can choose which of the shown items they want to use to fill the bundle. They do not have to use all shown items, only enough to fill the slots. |
| Crafts Room | The Crafts Room contains the first group of bundles available. Completing all Crafts Room bundles repairs the bridge east of / The Mines / , unlocking the / Quarry / . |
| Bundle 5 | or |
| Bundle 6 | or |
| Pantry | The Pantry appears after completing one bundle. Completing all Pantry bundles will restore the dilapidated / Greenhouse / on the farm, making it available to grow / Crops / and / Fruit Trees / year-round. |
| Bundle 4 | or |
| Fish Tank | The Fish Tank appears after completing one bundle. Completing all Fish Tank bundles will remove the Glittering Boulder to the left of / The Mines / entrance. / Willy / will also give the player a / Copper Pan / that can be used to collect metal ores and other items from bodies of water. |
| Fish Tank | Notes: It may not be possible to finish the Specialty Fish Bundle before finishing the entire Vault section, as access to / The Desert / is required to get a / Sandfish / , unless it becomes available at the / Traveling Cart / . For the Quality Fish Bundle, iridium quality fish can be used as well as gold quality fish. |
| Boiler Room | The Boiler Room appears after completing two bundles. Completing all Boiler Room bundles repairs the / Minecarts / , allowing the player to fast travel between distant locations. The Locations are / Bus Stop / , / Mines / , / Quarry / and / Town / . |
| Bundles | (3 chosen at random) |
| Bulletin Board | The Bulletin Board appears after completing three bundles. |
| Bulletin Board | Completing all Bulletin Board bundles improves the player's / friendship / rating with every / non-datable villager / by two hearts (500 points). Note that this applies only to non-datable villagers whom the player has met in person. Villagers who do not show on the "Social" tab of the player menu and villagers whose names appear as "???' will not receive 500 points. If the player completes all the bundles before / Kent / arrives on 1 Spring, Year 2 -- possible by buying a / Red Cabbage / from the / Traveling Cart / -- he will not benefit from the friendship increase, and will start at 0 hearts. The / Dwarf / 's friendship will be unaffected if the player does not have the / Dwarvish Translation Guide / . |
| Bulletin Board | The morning after, Mayor / Lewis / will send a letter saying that packages containing items posted about "years ago" on the / Community Center / bulletin board have been appearing in villagers' homes. He says the packages are all addressed from "your farm". He expresses his gratitude and says "all of us in town are delighted!" |
| Bundles | (5 chosen at random) |
| Vault | The Vault becomes available after completing four bundles. Pressing the large "purchase" button will purchase the bundle and deduct the gold from the total. |
| Vault | Completing all Vault bundles costs / Gold / 42,500g / , and repairs the / Bus Stop / . Taking the Bus grants access to / The Calico Desert / . |

<a id="source-community-center"></a>
## 3. 社区中心修复与完成后果（Community Center）

固定来源：[revision 193096](https://stardewvalleywiki.com/mediawiki/index.php?title=Community_Center&oldid=193096)；保留数据表 2 张、数据行 7、规则事实块 12。

### 3.1 Introduction — Community Center

| Community Center | Community Center |
|---|---|
| Community Center | Community Center |
| Maplocation / Map | Maplocation / Map |
| Open Hours: | Always |
| Closed: | Never |
| Occupants: | Junimo Icon / Junimos |

### 3.2 Restoring the Community Center — Ceremony Details

| Ceremony Details |
|---|
| The grand opening event begins by showing the entire town at the Community Center. Everyone has balloons and is celebrating and taking a look at the refurbished Center. Inside, the mayor shows off the Center to everyone exploring it. Entering the Center, the player can talk to / Lewis / , who will exclaim how happy he and the rest of the town are. On behalf of the whole town, he awards them with the / Stardew Hero Trophy / in thanks. / Soon after, a voice grumbles, and the manager of / JojaMart / , / Morris / , comes into the Center. He asks where all his customers went as he looks around the building. Angrily, / Pierre / walks over and asks Morris how it feels. There are two choices to choose from to calm the situation or escalate it. / "Let's be reasonable." / "Let's settle this the old-fashioned way." / If choosing "Let's be reasonable.": / Morris / then boasts that he will put on a 75% off sale to get his customers back and laughs off the event. Pierre then tells him he's wrong and asks everyone to gather around. He begins to talk about when he first moved to the / Pelican Town / , reminiscing about how the town had a real sense of being a family and a community, talking to different people about how they enjoyed and connected with each other in the Center and that / JojaMart / took that away from them. Now that the Center is finished, Pierre asks everyone to boycott JojaMart in order to take advantage of the second chance that the player has given them. / Morris / jumps in shock and everyone takes a second to soak it in. / Everyone agrees with Pierre to boycott Joja. Morris then exclaims that his business is ruined and will rush out of the Center. / If choosing "Let's settle this the old-fashioned way.": / Morris then boasts that he will put on a 75% off sale to get his customers back and laugh in Pierre's face. Pierre will then say that he will not get his way this time and proposes that they settle this once and for all. Morris asks how they would do so and Pierre will then start to threaten to fight Morris. Morris will scoff at Pierre and begin to walk off. Pierre will then try to goad Morris with a threat of all Joja Mart employees being cowards. Morris will become infuriated at the slander of his employer, Joja. He will walk back to Pierre and begin fighting with him. / Caroline / will scream Pierre's name as / George / laughs and enjoys the fight as Lewis and Robin jump in surprise from the fight. Morris and Pierre will start to insult each other as they continue to fight. Pierre will then punch Morris so hard that he flies out of the community center's ceiling. Pierre is so proud of his winning punch he smiles and poses with sunglasses. |

### 3.3 非表格规则事实

| 来源章节 | 完整规则事实 |
|---|---|
| Introduction | For Community Center Bundles, see / Bundles / . / For the furniture item, see / 'Community Center' / . |
| Introduction | The Pelican Town / Community Center / is located in / Pelican Town / , on the screen north of / Pierre's General Store / . Initially, it appears as a dilapidated building, and is locked to the community. |
| Introduction | To open the Community Center, the player must enter Pelican Town from the / Bus Stop / on a day when it is not raining, from Spring 5th onward, between 8:00 am and 1:00 pm. Entering town from another direction, at another time, or on a rainy day, will not trigger the cutscene. In multiplayer, the host must trigger the cutscene. |
| Introduction | During the cutscene, / Mayor Lewis / unlocks the building and leads the player inside, where strange creatures called / Junimos / appear and quickly disappear before Lewis can see them. Lewis says he wouldn't be surprised if the place was "full of rats". The cutscene ends with Lewis informing the player that he will leave the Community Center unlocked in the future. Viewing the cut-scene unlocks the / "Rat Problem" quest / . |
| Introduction | To fulfill the "Rat Problem" quest, the player must re-enter the Community Center and interact with a / Golden Scroll / Golden Scroll located in the lower left room. The scroll contains strange writing that can't be deciphered. |
| Introduction | The morning after reading the scroll, the player will receive a letter from the / Wizard / saying he has information about the "rat problem" and that the player should pay him a visit. Reading this letter unlocks the / "Meet the Wizard" quest / . Visiting the Wizard at / his tower / in the west of / Cindersap Forest / will trigger a cutscene during which the Wizard gives the player a potion that grants the / Forest Magic / power, allowing the player to read the language of the Junimos. |
| Introduction | Thereafter, all Golden Scrolls at the Community Center can be read by the player. Each scroll asks for specific offerings in the form of / Bundles / . Completing all the bundles restores the Community Center. |
| Introduction | Alternatively, if the player purchases a / JojaMart / membership from / Morris / for / Gold / 5,000g / , the Community Center is permanently replaced with a / Joja Warehouse / . Instead of completing Bundles, the player will then purchase community upgrades through the / Joja Community Development Form / . |
| Restoring the Community Center | After completing all / bundles / , the / Junimos / restore the Community Center, and say good-bye before leaving. The next sunny day after completing the last bundle, the player can attend the Community Center reopening ceremony cutscene, triggered by entering / Pelican Town / at any time. The ceremony is delayed if it is raining or a festival is to be held in town. Completing the ceremony unlocks the "Local Legend" / Achievement / and awards the player the / Stardew Hero Trophy / . |
| Restoring the Community Center | After the ceremony, / JojaMart / goes out of business. The building becomes abandoned and falls into disrepair. / Pierre's General Store / is no longer closed on Wednesdays and is open every day of the week. The / Blacksmith / shop is closed on Fridays, since / Clint / spends all day at the Community Center. However, the shop can still be entered. |
| Willy's Boat | Main article: / Fish Shop#Willy's Boat |
| Willy's Boat | After reaching certain progress on the Community Center / Bundles / , cutscenes about Willy's boat can be triggered. |

<a id="source-joja-community-development-form"></a>
## 4. Joja 社区开发项目（Joja Community Development Form）

固定来源：[revision 187019](https://stardewvalleywiki.com/mediawiki/index.php?title=Joja_Community_Development_Form&oldid=187019)；保留数据表 0 张、数据行 0、规则事实块 10。

### 4.1 非表格规则事实

| 来源章节 | 完整规则事实 |
|---|---|
| Introduction | The / Joja Community Development Form / is the / JojaMart / equivalent to the / Community Center / Bundles / . It can be accessed the day after paying / Gold / 5,000g / for a JojaMart membership to / Morris / , through which the Community Center gets turned into a / Joja Warehouse / . The player is able to complete town restoration projects ("developments") by individually purchasing them via the Joja Community Development Form located at Morris' counter inside JojaMart. |
| Introduction | After each purchase, Morris and his JojaMart crew will complete the project after the player goes to sleep. Only one development can be purchased per day, even if the player has the funds to purchase multiple at once. |
| Developments | Gold / 40,000g / Bus / to / the Desert / Gold / 25,000g / Bridge to the / Quarry / Gold / 20,000g / Removes the glittering boulder, allowing / panning / Gold / 15,000g / Minecarts / Gold / 35,000g / Greenhouse |
| Developments | It costs / Gold / 135,000g / to complete all developments ( / Gold / 140,000g / including the membership purchase). There are no "Friendship" rewards associated with the Joja Community Development Form like there are with the Community Center Bundles. |
| Developments | If the player completes all the bundles in a room in the Community Center that unlocks a development before purchasing a membership, the development will remain in place and show as already completed after purchasing a membership. However, no discount is given for partially completed rooms. The Joja cost for a development is the same regardless of prior community center progress. |
| Completion | Starting the day following the completion of the development form, the first time the player walks into / Pelican Town / on a sunny day (at any time of day), a completion ceremony is held in front of the warehouse. The ceremony is delayed if it is raining or a / festival / is held in town. |
| Completion | Morris / gives the following speech: |
| Completion | The player then receives the / Soda Machine / . At JojaMart, the / Auto-Petter / becomes available for purchase for / Gold / 50,000g / and Morris will present the player with an " / entertainment opportunity / ." |
| Completion | The day after viewing the completion ceremony, a letter will arrive from / Willy / inviting the player into his / back room / . The closing ceremony does not need to be seen to trigger the letter. |
| Notes | Until the player has the funds for both a Joja membership and a development, a good strategy can be to put off buying a membership until ready and meanwhile receiving rewards for bundles that are easy to complete, such as the Spring Foraging Bundle or Crab Pot Bundle. / If the player plans to buy the bus first, it may be more "rewarding" to complete the Community Center bundles instead for a total cost of / Gold / 42,500g / (vs Joja's price of / Gold / 40,000g / ) and receive 3 / Chocolate Cakes / , 30 / Quality Fertilizers / , a / Lightning Rod / , and a / Crystalarium / . / Curiously, / Lewis / , / Robin / , / Willy / , and the other villagers are mystified by the source of the community improvements, implying Joja does not publicize its actions or that villagers do not notice an entire crew coming from out of town to make repairs. |

<a id="source-movie-theater"></a>
## 5. 两条路线的电影院解锁（Movie Theater）

固定来源：[revision 193933](https://stardewvalleywiki.com/mediawiki/index.php?title=Movie_Theater&oldid=193933)；保留数据表 1 张、数据行 6、规则事实块 5。

### 5.1 Introduction — Movie Theater

| Movie Theater | Movie Theater |
|---|---|
| Movie Theater | Movie Theater |
| Maplocation / Map | Maplocation / Map |
| Open Hours: | 9:00am to 9:00pm |
| Closed: | Most / festival / days |
| Address: | Abandoned / JojaMart / or / Joja Warehouse |

### 5.2 非表格规则事实

| 来源章节 | 完整规则事实 |
|---|---|
| Introduction | The / Movie Theater / is a building that allows players to watch movies, alone or with a guest, once every week. It is unlocked either by completing the / Community Center / or all / community upgrades / offered by / Morris / . |
| Introduction | If players choose to restore the Community Center, the night before the first rainy or stormy day after restoring the Center, there is a cutscene of a lightning bolt striking the doors to the abandoned / JojaMart / . Afterwards, the player may enter the abandoned JojaMart and find / the Missing Bundle / . The night after completing the Missing Bundle, the / Junimos / will build a Movie Theater. |
| Introduction | If players choose the Joja route, they can purchase the Movie Theater from Morris for / Gold / 500,000g / after completing all other / community upgrades / . The / Joja Warehouse / will then become a Movie Theater. |
| Introduction | Players must purchase a / Movie Ticket / for / Gold / 1,000g / to enter the Movie Theater. A second Movie Ticket can also be purchased for / Gold / 1,000g / and given to a villager in the same way a gift is given. This will invite the villager to attend the movie with the player. To see the movie with the villager, enter the theater on the same day the ticket is gifted; otherwise, the ticket is forgotten. |
| Introduction | In a / Multiplayer / game, it is possible to watch a movie with other players. To do this, all participating players must gather in the lobby before the movie starts. A message suggesting you will watch the movie by yourself still displays when entering the building, regardless of other players being present. |

## 四、审计结论

- 旧稿只维护标准收集包，遗漏混合模式 47 个候选包；本轮已经补齐并固定来源。
- 旧稿将社区中心开放写成雨天触发，并在剧情页混淆工艺室/锅炉房奖励；旧手写口径不再作为数据源。
- 收集物品本身的价格、产地和对象属性继续归属各对象数据域；本页只完整维护路线要求与奖励关系。

---

[上一篇：爷爷评价与完美追踪](./爷爷评价与完美追踪.md) · [返回游戏概览](../游戏概览.md) · [下一篇：齐先生的挑战与姜岛](./齐先生的挑战与姜岛.md)
