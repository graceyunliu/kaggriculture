# Kaggriculture Replay Evidence Report

Extracted from 15 replay files in `Chatgpt Agents/Replay` (Kaggle episode JSON format). Each replay is a head-to-head match between grace's submitted agent and a real leaderboard opponent, 720 steps (30 in-game days) per game.

Record: **8 wins, 7 losses**.

## Per-game results, sorted by final money

| Episode | Result | Opponent | Your $ | Opp $ | Margin |
|---|---|---|---|---|---|
| 101674403 | WIN | Darsh Jilka | 32,154 | 4,112 | +28,042 |
| 101692391 | WIN | greySnow | 31,419 | 26,133 | +5,286 |
| 101694627 | WIN | Kian Maghsoodi | 31,410 | 26,068 | +5,342 |
| 101683350 | WIN | Ivan Jarp | 31,405 | 26,616 | +4,789 |
| 101678862 | WIN | BJ Kim | 31,031 | 14,286 | +16,745 |
| 101676639 | WIN | Siddardha Shayini | 30,936 | 8,573 | +22,363 |
| 101699145 | WIN | angusdddsa | 30,215 | 9,992 | +20,223 |
| 101701385 | WIN | DataSluts | 22,218 | 22,189 | +29 |
| 101732769 | LOSS | Ramón López | 26,070 | 41,707 | -15,637 |
| 101703632 | LOSS | Attack on Kaggle | 21,297 | 45,773 | -24,476 |
| 101687858 | LOSS | Dhananjai1729 | 19,504 | 28,380 | -8,876 |
| 101690097 | LOSS | miyawakiayaka | 19,024 | 44,388 | -25,364 |
| 101866814 | LOSS | Shuaib ayad Jasim Jasim | 15,651 | 31,515 | -15,864 |
| 101696875 | LOSS | Shailaja J | 12,860 | 32,589 | -19,729 |
| 101681112 | LOSS | Riyaz Ur Rehman | 11,540 | 39,446 | -27,906 |

## What grace's agent sells, by outcome

| Item | Total units in wins | Total units in losses |
|---|---|---|
| MELON | 2,194 | 1,603 |
| WHEAT | 225 | 264 |
| CARROT | 190 | 440 |

Grace's agent sells the same three-item mix every game (MELON/WHEAT/CARROT), win or lose — it never sells STRAWBERRY, TOMATO, MILK, WOOL, EGG, FERTILIZER, or animal units in any of the 15 replays.

## What opponents sell, by outcome (from grace's seat)

| Item | Total units when we WIN | Total units when we LOSE |
|---|---|---|
| WHEAT | 2,110 | 2,649 |
| CARROT | 426 | 708 |
| MELON | 166 | 860 |
| FERTILIZER | 303 | 460 |
| EGG | 212 | 506 |
| MILK | 346 | 208 |
| WOOL | 164 | 198 |
| SHEEP | 138 | 0 |
| TOMATO | 112 | 43 |
| STRAWBERRY | 100 | 174 |
| COW | 69 | 0 |

## Key observations

Opponents that beat grace's agent sell far more MELON (860 vs 166 units) and far more CARROT (708 vs 426) than opponents grace beats — i.e., the losing opponents in this sample are the ones directly competing for the same crops grace's agent specializes in, likely driving down the price grace can get or out-producing her on volume.

Every opponent, regardless of whether they win or lose, sells substantially more WHEAT than grace's agent does (2,000+ units vs ~250). Grace's agent essentially ignores WHEAT as a volume crop.

The two biggest wins (Darsh Jilka +$28k, Siddardha Shayini +$22k, angusdddsa +$20k) came against opponents who barely sold anything — likely under-developed or buggy agents, not strong competitors. The margin in these blowout wins says more about weak opponents than about grace's own strategy.

The losses are steep (-$15k to -$28k), and in the worst loss (vs Riyaz Ur Rehman) the opponent matched grace's MELON volume (262 vs 232 units) while also adding FERTILIZER, MILK, and other diversified income — suggesting the losing pattern is opponents replicating grace's core crop strategy and then adding extra income streams grace's agent doesn't use at all.

## Files

Full transaction-level data (2,204 individual SELL events, one row per event with day/hour/item/quantity/buyer) is in `sell_transactions.jsonl` and `replay_summary.jsonl` in the same folder, if deeper analysis is needed later.
