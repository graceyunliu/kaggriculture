# Evolution run 20260913-103155

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_pensukesan_107199477.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.03 h · candidates evaluated this run: 80 · games 27,998 (13,813/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 19 | 38 |
| dead_pattern | 8 | 16 |
| dead_smoke | 1 | 8 |
| alive | 4 | 672 |
| held_fail | 0 | 0 |
| held_exploit | 0 | 0 |
| held_pass | 48 | 27264 |
| error | 0 | 0 |

Population (all runs, reached dev): 297 · held-out evaluated: 228 · held-out PASS: 227

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | +6,918 | 6.2 | 28-2 | -5,975 | +9,000 | 6.3 | 18-2 |
| chassis + C1 params (seed row) | +6,918 | 6.2 | 28-2 | -5,975 | +9,000 | 6.3 | 18-2 |
| C1.py (file) vs O15_SALE_PRIORITY.py | -21,945 | -16.8 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O15_SALE_PRIORITY.py | -25,061 | -10.2 | 0-10 | — | — | — | — |
| O15_SALE_PRIORITY.py own panel (dev / held) | — | — | — | -16,635 / -23,287 | — | — | — |

Measurement mode: `KAGG_FIXED_SHOPS=1` (shop unlocks policy-independent; panel margins comparable at ±$3k/opponent).

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `39ac3d97c0b8` | best | ablate:NEAR_RADIUS | **+13,992** | 9.3 | 19-1 | -13,308 | +10,530 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, MAX_HANDS 14→13, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -3,436 -> final -3,436); days 27-29 drivers: work_turns -35, water_hour +1.93, sales_rev -478, travel_per_task +0.09. Hands 4 vs 5, animals 10 vs 11, plants 4 vs  |
| `313a1744dfa4` | queue | crossover | **+13,961** | 10.2 | 19-1 | -12,486 | +11,941 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,121 -> final -1,755); days 23-29 drivers: sales_rev -3,691, missed_water +11, work_turns -28, water_hour +0.39. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `b631ee86f5f0` | best | crossover | **+13,844** | 9.7 | 19-1 | -12,308 | +11,012 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | wheat_stock -315, demand_share +89, HERD_LAST_DAY -18, OPP_GROWTH ?, FERT_RADIUS ?, MELON_MORNING_LAST_HOUR ? | cand falls behind C1 from day 25 (gap -3,362 -> final -5,064); days 23-29 drivers: sales_rev -7,804, work_turns -172, water_hour +2.49. Hands 3 vs 5, animals 9 vs 11, plants 2 vs 5. |
| `7be2cfe703c1` | best | ablate:HERD_LAST_DAY | **+13,844** | 9.7 | 19-1 | -12,267 | +11,030 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,362 -> final -5,064); days 23-29 drivers: sales_rev -7,804, work_turns -172, water_hour +2.49. Hands 3 vs 5, animals 9 vs 11, plants 2 vs 5. |
| `f70383b38bc1` | best | ablate:demand_share | **+13,728** | 10.4 | 19-1 | -12,614 | +10,923 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,362 -> final -5,064); days 23-29 drivers: sales_rev -7,804, work_turns -172, water_hour +2.49. Hands 3 vs 5, animals 9 vs 11, plants 2 vs 5. |
| `41d34d27b102` | best | mutate | **+13,600** | 9.4 | 19-1 | -13,021 | +10,383 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |  | cand falls behind C1 from day 25 (gap -2,489 -> final -4,508); days 23-29 drivers: sales_rev -7,226, work_turns -162, water_hour +1.39, travel_per_task +0.06. Hands 4 vs 5, animals 9 vs 11, plants 4 v |
| `91aa2b2655cb` | best | ablate:fert_buy | **+13,158** | 8.4 | 19-1 | -13,097 | +10,688 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 18 (gap -1,697 -> final -2,673); days 16-23 drivers: sales_rev -2,036, work_turns -30, reversals +17, water_hour +0.85. Hands 12 vs 12, animals 10 vs 11, plants 51 vs 56. |
| `b910f3621a2f` | queue | mutate | **+13,121** | 8.4 | 19-1 | -13,480 | +10,512 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→114, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→6, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | CROP_SWEEP_LEN ?, MELON_PRICE_CUSHION ?, SPREAD_CAP ? | cand falls behind C1 from day 25 (gap -2,488 -> final -4,507); days 23-29 drivers: sales_rev -7,226, work_turns -162, water_hour +1.39, travel_per_task +0.06. Hands 4 vs 5, animals 9 vs 11, plants 4 v |
| `e920953119d2` | queue | migrate | **+13,113** | 9.4 | 19-1 | -12,408 | +10,959 | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,388 -> final -5,273); days 23-29 drivers: sales_rev -7,218, work_turns -171, water_hour +2.31, travel_per_task +0.07. Hands 4 vs 5, animals 9 vs 11, plants 3 v |
| `152620c1f6b5` | queue | archive_crossover:crossover_g000050_20260913-080130_1 | **+13,064** | 9.7 | 20-0 | -12,205 | +10,597 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 18 (gap -1,702 -> final -2,682); days 16-23 drivers: sales_rev -1,946, work_turns -30, reversals +17, water_hour +0.85. Hands 12 vs 12, animals 10 vs 11, plants 51 vs 56. |
| `cac9814edfe3` | best | paired | **+13,063** | 9.1 | 19-1 | -12,759 | +10,335 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | fert_buy -352, NEAR_RADIUS +831 | cand falls behind C1 from day 18 (gap -1,552 -> final -2,334); days 16-23 drivers: sales_rev -3,474, work_turns -39, reversals +17, idle_turns +6. Hands 12 vs 12, animals 10 vs 11, plants 47 vs 56. |
| `0fb60800f0b8` | queue | archive_crossover:crossover_g000025_20260913-071603_0 | **+13,028** | 8.8 | 19-1 | -12,244 | +10,892 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,939 -> final -4,855); days 23-29 drivers: sales_rev -6,702, work_turns -158, water_hour +2.29, travel_per_task +0.07. Hands 4 vs 5, animals 9 vs 11, plants 5 v |
| `59f341ad73c8` | best | ablate:wheat_stock | **+12,987** | 8.5 | 19-1 | -12,209 | +11,327 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,387 -> final -5,284); days 23-29 drivers: sales_rev -7,219, work_turns -170, water_hour +2.31, travel_per_task +0.06. Hands 4 vs 5, animals 9 vs 11, plants 3 v |
| `50c5957841ac` | best | ablate:MAX_HANDS | **+12,894** | 8.6 | 18-2 | -13,060 | +9,982 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -1,511 -> final -1,384); days 23-29 drivers: missed_water +11, sales_rev -1,592, water_hour +0.87. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `5f24e87aab07` | queue | archive_crossover:crossover_g000050_20260913-101837_0 | **+12,718** | 8.2 | 19-1 | -13,467 | +10,179 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, MAX_HANDS 14→13, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -3,074 -> final -3,074); days 27-29 drivers: work_turns -42, water_hour +2.25, sales_rev -389, travel_per_task +0.12. Hands 4 vs 5, animals 10 vs 11, plants 3 vs  |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `313a1744dfa4` | queue | crossover | +11,941 | 9.0 | 28-2 | -8,743 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `24f5e1b3f3bd` | best | crossover | +11,756 | 9.9 | 29-1 | -9,145 | held_pass | min_hands 3→4, load_per_hand 20→18, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `59f341ad73c8` | best | ablate:wheat_stock | +11,327 | 8.4 | 29-1 | -7,381 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `7be2cfe703c1` | best | ablate:HERD_LAST_DAY | +11,030 | 8.3 | 28-2 | -8,880 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `b631ee86f5f0` | best | crossover | +11,012 | 8.3 | 28-2 | -8,797 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `e920953119d2` | queue | migrate | +10,959 | 9.1 | 29-1 | -9,441 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `d8f30f7f520a` | queue | archive_crossover:crossover_g000050_20260913-122304_0 | +10,954 | 9.0 | 29-1 | -9,124 | held_pass | wheat_stock 0→1, load_per_hand 20→18, open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `f70383b38bc1` | best | ablate:demand_share | +10,923 | 9.9 | 29-1 | -9,287 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `0fb60800f0b8` | queue | archive_crossover:crossover_g000025_20260913-071603_0 | +10,892 | 8.1 | 28-2 | -8,764 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `477f0a2b2e14` | best | paired | +10,842 | 8.3 | 27-3 | -9,200 | held_pass | wheat_stock 0→1, load_per_hand 20→19, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, HIRE_MAX_MARGINAL 144→89, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `91aa2b2655cb` | best | ablate:fert_buy | +10,688 | 8.3 | 28-2 | -9,381 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `836e85c9003b` | best | crossover | +10,627 | 9.5 | 29-1 | -6,703 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `f97c4f0268f7` | best | block_pair | +10,607 | 8.4 | 29-1 | -7,816 | held_pass | open_melons 10→9, early_hire_days 3→5, fert_buy 4→2, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `152620c1f6b5` | queue | archive_crossover:crossover_g000050_20260913-080130_1 | +10,597 | 8.1 | 29-1 | -8,665 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `f8cb79a7a0d9` | queue | crossover | +10,562 | 8.4 | 28-2 | -8,224 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.4, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→4, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +11,756 (`24f5e1b3f3bd`), n=85
- o15: best +10,381 (`c00ac4f1d57e`), n=75
- queue: best +11,941 (`313a1744dfa4`), n=79
- wide: best +9,838 (`1920a874375b`), n=58

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| ROUTE_LEN | +16,811 | 2 | 3 | 4 | 297 | 2.04 | 2: +8,197 (n=64), 3: +4,856 (n=226), 4: +1,131 (n=5), 5: -8,614 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +13,370 | 19 | 20 | 14 | 294 | 7.04 | 19: +7,929 (n=9), 16: +6,611 (n=2), 18: +6,391 (n=14), 20: +6,212 (n=215), 14: +4,798 (n=3), 17: +3,114 (n=20), 13: +3,027 (n=3), 15: +807 (n=22), 24: +194 (n=2), 22: -364 (n=2), 23: -5,441 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +11,792 | 9 | 8 | 9 | 295 | 4.6 | 9: +9,382 (n=15), 8: +6,032 (n=236), 4: +3,481 (n=4), 11: +2,628 (n=5), 12: +621 (n=29), 7: -932 (n=2), 6: -2,409 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,000 | 16 | 17 | 7 | 296 | 4.13 | 16: +6,418 (n=7), 17: +6,146 (n=253), 15: +3,068 (n=3), 20: +1,725 (n=12), 18: -952 (n=18), 12: -3,582 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +9,690 | frontier | frontier | 2 | 297 | 0.76 | frontier: +6,597 (n=261), v312: -3,093 (n=36) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +9,637 | 20 | 22 | 11 | 293 | 2.25 | 20: +7,474 (n=3), 22: +6,362 (n=99), 21: +5,539 (n=136), 18: +5,170 (n=38), 25: +2,138 (n=9), 19: +550 (n=2), 15: -2,164 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +8,803 | 1.5 | 1.4 | 9 | 296 | 2.73 | 1.5: +9,618 (n=13), 1.0: +7,816 (n=6), 1.6: +6,710 (n=4), 1.2: +6,517 (n=47), 1.4: +5,853 (n=75), 1.3: +4,729 (n=138), 1.1: +2,081 (n=2), 1.7: +815 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +8,439 | 1 | 0 | 10 | 291 | 0.99 | 1: +5,943 (n=142), 2: +5,576 (n=2), 0: +5,089 (n=145), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +7,612 | 15 | 14 | 7 | 296 | 3.07 | 15: +7,829 (n=40), 13: +7,146 (n=13), 16: +5,947 (n=35), 14: +4,948 (n=201), 11: +4,914 (n=2), 12: +217 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +7,443 | 116 | 100 | 18 | 290 | 5.6 | 116: +6,301 (n=61), 131: +6,301 (n=3), 112: +6,296 (n=7), 100: +5,974 (n=174), 93: +5,956 (n=4), 128: +5,869 (n=8), 94: +2,821 (n=2), 84: +2,477 (n=2), 134: +1,890 (n=3), 107: +680 (n=24), 150: -1,142 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +7,416 | 2 | 3 | 8 | 296 | 4.75 | 2: +9,517 (n=2), 0: +6,707 (n=4), 6: +6,638 (n=2), 3: +5,814 (n=11), 8: +5,765 (n=30), 5: +5,383 (n=243), 7: +2,101 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +7,017 | 0.55 | 0.55 | 6 | 296 | 3.05 | 0.55: +5,798 (n=240), 0.45: +5,278 (n=4), 0.5: +4,824 (n=41), 0.65: +194 (n=2), 0.7: -1,219 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +6,418 | 19 | 19 | 4 | 296 | 1.65 | 19: +5,731 (n=261), 20: +3,496 (n=33), 18: -687 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,381 | 0.0 | 0.0 | 8 | 295 | 4.37 | 0.0: +5,716 (n=264), 0.2: +5,429 (n=16), 0.3: +3,918 (n=6), 0.6: +1,676 (n=2), 0.5: +1,546 (n=3), 0.1: -664 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +5,797 | 9 | 6 | 8 | 297 | 2.1 | 9: +7,899 (n=4), 8: +6,659 (n=115), 7: +6,050 (n=23), 3: +6,000 (n=38), 5: +5,397 (n=11), 6: +3,786 (n=96), 10: +2,515 (n=5), 4: +2,103 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +5,611 | 2 | 3 | 4 | 297 | 1.4 | 2: +6,057 (n=178), 3: +5,878 (n=69), 4: +4,797 (n=24), 1: +446 (n=26) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| feed_spare_poor | +5,606 | 0 | 0 | 4 | 296 | 1.85 | 0: +5,559 (n=281), 1: +4,136 (n=13), 2: -47 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HIRE_MAX_MARGINAL | +5,447 | 1000000000 | 144 | 6 | 297 | 3.93 | 1000000000: +7,558 (n=11), 377: +7,126 (n=11), 144: +5,468 (n=244), 233: +4,735 (n=9), 89: +3,821 (n=15), 55: +2,111 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_hold_days | +5,117 | 0 | 0 | 2 | 297 | 0.76 | 0: +6,042 (n=261), 1: +926 (n=36) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| min_hands | +4,987 | 5 | 3 | 4 | 297 | 2.57 | 5: +7,049 (n=3), 4: +6,454 (n=27), 3: +5,324 (n=265), 6: +2,061 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +11,941 (n=26)
- (10, 3, 4): +11,756 (n=34)
- (9, 2, 4): +11,327 (n=6)
- (9, 2, 3): +11,030 (n=4)
- (9, 3, 4): +10,954 (n=22)
- (9, 3, 5): +10,688 (n=13)
- (11, 3, 5): +10,627 (n=83)
- (10, 3, 6): +10,381 (n=11)
- (11, 3, 6): +10,275 (n=22)
- (11, 3, 4): +10,118 (n=64)
- (13, 3, 6): +4,882 (n=3)
- (9, 3, 6): +3,828 (n=1)
- (9, 3, 3): +2,012 (n=2)
- (14, 3, 5): +1,546 (n=2)
- (12, 3, 5): -239 (n=1)

## Remaining-horizon ROI (AGE-360)

`candidates/O17_ORCH_CAPITAL.py` | mode `cutoff+marginal` | 64 cells (4 tapes x 16 seeds) | fixed_shops=True | generated 2026-09-11T02:29:18

ROI = base final money - counterfactual final money, net of acquisition, operating and opportunity cost. **Read the intervention column before the number.** `class blocked` prices the whole subsystem and, for a class the policy replenishes continuously (labour, feed), is near-total ablation -- it does NOT estimate the value of the last unit. `-K unit/day` is the marginal experiment. The two can have opposite signs, and on this chassis HIRE does.

| investment | intervention | from day | n | ROI | t | 95% CI | cells + | payback |
|---|---|---:|---:|---:|---:|---|---:|---|
| BUY_ANIMAL | class blocked | 2 | 12 | +6,734 | 2.94 | [+2,243, +11,226] | 83% | 83% by day 15 |
| BUY_ANIMAL | class blocked | 4 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 5 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 6 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 7 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 8 | 24 | +3,350 | 1.01 | [-3,132, +9,831] | 29% | 29% by day 17 |
| BUY_ANIMAL | class blocked | 9 | 24 | -208 | -0.15 | [-2,983, +2,566] | 25% | 25% by day 23 |
| BUY_ANIMAL | class blocked | 10 | 12 | -1,008 | -2.03 | [-1,980, -36] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 2 | 12 | +3,019 | 1.93 | [-50, +6,088] | 75% | 75% by day 29 |
| BUY_ANIMAL:COW | class blocked | 6 | 12 | -1,042 | -1.00 | [-3,086, +1,003] | 50% | 50% by day 29 |
| BUY_ANIMAL:COW | class blocked | 10 | 12 | -917 | -1.82 | [-1,902, +69] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 2 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 6 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 10 | 12 | +2,218 | 2.24 | [+277, +4,159] | 33% | 33% by day 28 |
| BUY_LAND | class blocked | 14 | 12 | -302 | -1.00 | [-893, +290] | 0% | 0% never |
| BUY_LAND | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_PRODUCT | class blocked | 2 | 12 | +35,501 | 5.90 | [+23,717, +47,285] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 6 | 12 | +38,533 | 5.34 | [+24,396, +52,670] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 10 | 32 | +38,821 | 5.92 | [+25,960, +51,681] | 97% | 97% by day 13 |
| BUY_PRODUCT | class blocked | 14 | 32 | +22,151 | 4.29 | [+12,032, +32,269] | 78% | 78% by day 19 |
| BUY_PRODUCT | class blocked | 18 | 32 | +13,697 | 3.84 | [+6,709, +20,685] | 62% | 62% by day 22 |
| BUY_PRODUCT | class blocked | 22 | 32 | +10,598 | 4.44 | [+5,916, +15,279] | 81% | 81% by day 25 |
| BUY_PRODUCT | class blocked | 26 | 32 | +4,647 | 5.85 | [+3,090, +6,205] | 94% | 94% by day 29 |
| BUY_PRODUCT:FERTILIZER | class blocked | 16 | 32 | +105 | 0.40 | [-409, +620] | 38% | 38% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 18 | 32 | +332 | 1.20 | [-209, +873] | 53% | 53% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 20 | 32 | +274 | 1.06 | [-231, +779] | 47% | 47% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 22 | 32 | +201 | 1.42 | [-76, +479] | 44% | 44% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 24 | 32 | +156 | 1.20 | [-99, +411] | 25% | 25% by day 26 |
| BUY_PRODUCT:WHEAT | class blocked | 16 | 32 | +17,487 | 4.10 | [+9,124, +25,850] | 66% | 66% by day 20 |
| BUY_PRODUCT:WHEAT | class blocked | 18 | 32 | +13,145 | 3.91 | [+6,548, +19,742] | 59% | 59% by day 22 |
| BUY_PRODUCT:WHEAT | class blocked | 20 | 32 | +10,597 | 3.75 | [+5,059, +16,135] | 59% | 59% by day 24 |
| BUY_PRODUCT:WHEAT | class blocked | 22 | 32 | +9,922 | 4.13 | [+5,212, +14,632] | 72% | 72% by day 25 |
| BUY_PRODUCT:WHEAT | class blocked | 24 | 32 | +6,874 | 4.74 | [+4,033, +9,715] | 91% | 91% by day 27 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 8 | 32 | +1,300 | 1.88 | [-57, +2,658] | 53% | 53% by day 26 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 12 | 32 | +246 | 0.71 | [-430, +923] | 44% | 44% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 16 | 32 | +262 | 1.49 | [-82, +606] | 53% | 53% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 20 | 32 | +335 | 2.09 | [+20, +649] | 53% | 53% by day 28 |
| BUY_SEED | class blocked | 2 | 12 | +32,017 | 6.75 | [+22,721, +41,312] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 6 | 12 | +27,234 | 5.80 | [+18,025, +36,443] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 10 | 32 | +17,307 | 7.33 | [+12,677, +21,936] | 94% | 94% by day 22 |
| BUY_SEED | class blocked | 14 | 32 | +6,720 | 7.51 | [+4,966, +8,474] | 97% | 97% by day 24 |
| BUY_SEED | class blocked | 18 | 32 | +3,991 | 6.01 | [+2,689, +5,293] | 94% | 94% by day 26 |
| BUY_SEED | class blocked | 22 | 32 | +2,252 | 6.07 | [+1,525, +2,979] | 91% | 91% by day 29 |
| BUY_SEED | class blocked | 26 | 32 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED | -1 unit/day | 8 | 32 | +870 | 1.63 | [-179, +1,920] | 84% | 84% by day 26 |
| BUY_SEED | -1 unit/day | 12 | 32 | +825 | 3.29 | [+334, +1,316] | 91% | 91% by day 27 |
| BUY_SEED | -1 unit/day | 16 | 32 | +710 | 3.68 | [+331, +1,088] | 91% | 91% by day 28 |
| BUY_SEED | -1 unit/day | 20 | 32 | +444 | 4.11 | [+232, +656] | 84% | 84% by day 28 |
| BUY_SEED | -1 unit/day | 24 | 32 | +216 | 2.92 | [+71, +360] | 75% | 75% by day 29 |
| BUY_SEED:MELON | class blocked | 2 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 6 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 10 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 14 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 2 | 12 | +19,487 | 4.50 | [+10,992, +27,982] | 100% | 100% by day 21 |
| BUY_SEED:STRAWBERRY | class blocked | 6 | 12 | +12,168 | 2.35 | [+2,002, +22,334] | 67% | 67% by day 23 |
| BUY_SEED:STRAWBERRY | class blocked | 10 | 12 | +2,506 | 0.54 | [-6,564, +11,575] | 33% | 33% by day 25 |
| BUY_SEED:STRAWBERRY | class blocked | 14 | 12 | +1,510 | 2.08 | [+87, +2,933] | 58% | 58% by day 28 |
| BUY_SEED:STRAWBERRY | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| HIRE | class blocked | 2 | 12 | +60,467 | 8.28 | [+46,154, +74,780] | 100% | 100% by day 12 |
| HIRE | class blocked | 6 | 12 | +67,166 | 9.32 | [+53,044, +81,289] | 100% | 100% by day 11 |
| HIRE | class blocked | 10 | 12 | +65,554 | 9.34 | [+51,794, +79,315] | 100% | 100% by day 11 |
| HIRE | class blocked | 14 | 32 | +58,984 | 8.97 | [+46,102, +71,867] | 100% | 100% by day 15 |
| HIRE | class blocked | 18 | 32 | +44,291 | 9.10 | [+34,746, +53,835] | 100% | 100% by day 19 |
| HIRE | class blocked | 22 | 32 | +27,209 | 7.39 | [+19,990, +34,427] | 100% | 100% by day 23 |
| HIRE | class blocked | 26 | 32 | +12,805 | 9.78 | [+10,238, +15,371] | 100% | 100% by day 27 |
| HIRE | -1 unit/day | 8 | 32 | -1,907 | -2.64 | [-3,325, -489] | 28% | 28% by day 29 |
| HIRE | -1 unit/day | 12 | 64 | -2,108 | -6.31 | [-2,763, -1,453] | 12% | 12% by day 29 |
| HIRE | -1 unit/day | 16 | 32 | -832 | -3.82 | [-1,258, -405] | 19% | 19% by day 29 |
| HIRE | -1 unit/day | 20 | 64 | -1,178 | -10.36 | [-1,401, -955] | 8% | 8% by day 29 |
| HIRE | -1 unit/day | 24 | 32 | -361 | -3.34 | [-573, -150] | 9% | 9% by day 29 |
| HIRE | -2 unit/day | 12 | 32 | +153 | 0.24 | [-1,080, +1,385] | 59% | 59% by day 23 |
| HIRE | -2 unit/day | 20 | 32 | -531 | -1.77 | [-1,119, +58] | 22% | 22% by day 29 |

__Observational. Exact per-cell counterfactual against deterministic tapes; uncertainty is across tapes/seeds only. Downstream policy behaviour is held fixed, so a zero crossing is NOT an optimal cutoff day. Not wired to mutation weighting.__

A wide CI here is the measurement telling you the panel is too thin for that class, not that the class is worthless -- lumpy investments (animals, land) need more cells than the 12-cell margin panel provides. See `docs/AGE-360-horizon-roi.md`.

_Generated 2026-09-13 12:33. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 42 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–4 (n=42); wheat_stock=0–7 (n=42); min_hands=3–5 (n=42); load_per_hand=12–26 (n=42); open_melons=4–14 (n=42); open_cows=1–3 (n=42); open_sheep=0–3 (n=42); early_hire_days=0–7 (n=42)
- **Evidence:** 42 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**297 candidates** with action_table data, **40628 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,529 (n=4040) |         +5,422 (n=2079) |         +5,422 (n=2376) | 8495 |
| BUY_ANIMAL |         +5,281 (n=2057) |         +5,055 (n=404) |              — (n=0) | 2461 |
| BUY_SEED |         +5,680 (n=3297) |         +5,274 (n=1054) |         +5,286 (n=462) | 4813 |
| BUY_LAND |         +5,352 (n=1059) |         +5,075 (n=206) |              — (n=0) | 1265 |
| BUY_PRODUCT |         +5,423 (n=4448) |         +5,422 (n=2079) |         +5,414 (n=2045) | 8572 |
| HIRE |         +5,387 (n=2228) |         +5,473 (n=1036) |         +5,756 (n=720) | 3984 |
| WATER_MISSED |         +5,663 (n=3482) |         +5,422 (n=2079) |         +5,414 (n=2346) | 7907 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +5,295 (n=1869) |         +3,740 (n=550) |         +4,550 (n=712) | 3131 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,702 |      +5,434 |      +5,315 |      +5,963 |      +5,355 |      +5,373 |
| BUY_ANIMAL |      +4,528 |           — |           — |           — |      +6,597 |      +5,195 |
| BUY_SEED |      +5,393 |      +5,563 |      +3,053 |           — |      +6,702 |      +5,514 |
| BUY_LAND |           — |      -2,239 |      +5,495 |      -2,119 |      +6,281 |      +5,179 |
| BUY_PRODUCT |      +5,420 |           — |           — |           — |           — |           — |
| HIRE |      +5,476 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,422 |      +6,287 |      +5,422 |      +5,507 |
| FEED_MISSED |           — |      +5,444 |      +4,537 |           — |           — |      +4,795 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | HIRE | late | +5,756 | 720 | 1.22 |
| 2 | BUY_SEED | early | +5,680 | 3297 | 1.25 |
| 3 | WATER_MISSED | early | +5,663 | 3482 | 1.26 |
| 4 | SELL | early | +5,529 | 4040 | 1.21 |
| 5 | HIRE | mid | +5,473 | 1036 | 1.12 |
| 6 | BUY_PRODUCT | early | +5,423 | 4448 | 1.15 |
| 7 | SELL | mid | +5,422 | 2079 | 1.16 |
| 8 | SELL | late | +5,422 | 2376 | 1.16 |
| 9 | BUY_PRODUCT | mid | +5,422 | 2079 | 1.16 |
| 10 | WATER_MISSED | mid | +5,422 | 2079 | 1.16 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_LAND** in ('mid', 'low', 'mid', 'high'): +7,626 (n=20)
- **FEED_MISSED** in ('mid', 'low', 'mid', 'high'): +7,607 (n=19)
- **SELL** in ('mid', 'low', 'mid', 'high'): +7,359 (n=21)
- **BUY_ANIMAL** in ('mid', 'low', 'mid', 'high'): +7,359 (n=21)
- **BUY_SEED** in ('mid', 'low', 'mid', 'high'): +7,359 (n=21)
- **BUY_PRODUCT** in ('mid', 'low', 'mid', 'high'): +7,359 (n=21)
- **WATER_MISSED** in ('mid', 'low', 'mid', 'high'): +7,359 (n=21)
- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +7,224 (n=426)
- **BUY_SEED** in ('low', 'mid', 'high', 'high'): +6,862 (n=105)
- **WATER_MISSED** in ('low', 'mid', 'high', 'high'): +6,844 (n=115)
- **HIRE** in ('low', 'mid', 'high', 'high'): +6,832 (n=118)
- **SELL** in ('low', 'mid', 'high', 'high'): +6,804 (n=122)
- **SELL** in ('mid', 'low', 'high', 'low'): +6,804 (n=140)
- **BUY_PRODUCT** in ('low', 'mid', 'high', 'high'): +6,804 (n=122)
- **FEED_MISSED** in ('mid', 'low', 'high', 'low'): +6,804 (n=140)

## Remaining-horizon ROI (AGE-360)

`candidates/O17_ORCH_CAPITAL.py` | mode `cutoff+marginal` | 64 cells (4 tapes x 16 seeds) | fixed_shops=True | generated 2026-09-11T02:29:18

ROI = base final money - counterfactual final money, net of acquisition, operating and opportunity cost. **Read the intervention column before the number.** `class blocked` prices the whole subsystem and, for a class the policy replenishes continuously (labour, feed), is near-total ablation -- it does NOT estimate the value of the last unit. `-K unit/day` is the marginal experiment. The two can have opposite signs, and on this chassis HIRE does.

| investment | intervention | from day | n | ROI | t | 95% CI | cells + | payback |
|---|---|---:|---:|---:|---:|---|---:|---|
| BUY_ANIMAL | class blocked | 2 | 12 | +6,734 | 2.94 | [+2,243, +11,226] | 83% | 83% by day 15 |
| BUY_ANIMAL | class blocked | 4 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 5 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 6 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 7 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 8 | 24 | +3,350 | 1.01 | [-3,132, +9,831] | 29% | 29% by day 17 |
| BUY_ANIMAL | class blocked | 9 | 24 | -208 | -0.15 | [-2,983, +2,566] | 25% | 25% by day 23 |
| BUY_ANIMAL | class blocked | 10 | 12 | -1,008 | -2.03 | [-1,980, -36] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 2 | 12 | +3,019 | 1.93 | [-50, +6,088] | 75% | 75% by day 29 |
| BUY_ANIMAL:COW | class blocked | 6 | 12 | -1,042 | -1.00 | [-3,086, +1,003] | 50% | 50% by day 29 |
| BUY_ANIMAL:COW | class blocked | 10 | 12 | -917 | -1.82 | [-1,902, +69] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 2 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 6 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 10 | 12 | +2,218 | 2.24 | [+277, +4,159] | 33% | 33% by day 28 |
| BUY_LAND | class blocked | 14 | 12 | -302 | -1.00 | [-893, +290] | 0% | 0% never |
| BUY_LAND | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_PRODUCT | class blocked | 2 | 12 | +35,501 | 5.90 | [+23,717, +47,285] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 6 | 12 | +38,533 | 5.34 | [+24,396, +52,670] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 10 | 32 | +38,821 | 5.92 | [+25,960, +51,681] | 97% | 97% by day 13 |
| BUY_PRODUCT | class blocked | 14 | 32 | +22,151 | 4.29 | [+12,032, +32,269] | 78% | 78% by day 19 |
| BUY_PRODUCT | class blocked | 18 | 32 | +13,697 | 3.84 | [+6,709, +20,685] | 62% | 62% by day 22 |
| BUY_PRODUCT | class blocked | 22 | 32 | +10,598 | 4.44 | [+5,916, +15,279] | 81% | 81% by day 25 |
| BUY_PRODUCT | class blocked | 26 | 32 | +4,647 | 5.85 | [+3,090, +6,205] | 94% | 94% by day 29 |
| BUY_PRODUCT:FERTILIZER | class blocked | 16 | 32 | +105 | 0.40 | [-409, +620] | 38% | 38% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 18 | 32 | +332 | 1.20 | [-209, +873] | 53% | 53% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 20 | 32 | +274 | 1.06 | [-231, +779] | 47% | 47% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 22 | 32 | +201 | 1.42 | [-76, +479] | 44% | 44% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 24 | 32 | +156 | 1.20 | [-99, +411] | 25% | 25% by day 26 |
| BUY_PRODUCT:WHEAT | class blocked | 16 | 32 | +17,487 | 4.10 | [+9,124, +25,850] | 66% | 66% by day 20 |
| BUY_PRODUCT:WHEAT | class blocked | 18 | 32 | +13,145 | 3.91 | [+6,548, +19,742] | 59% | 59% by day 22 |
| BUY_PRODUCT:WHEAT | class blocked | 20 | 32 | +10,597 | 3.75 | [+5,059, +16,135] | 59% | 59% by day 24 |
| BUY_PRODUCT:WHEAT | class blocked | 22 | 32 | +9,922 | 4.13 | [+5,212, +14,632] | 72% | 72% by day 25 |
| BUY_PRODUCT:WHEAT | class blocked | 24 | 32 | +6,874 | 4.74 | [+4,033, +9,715] | 91% | 91% by day 27 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 8 | 32 | +1,300 | 1.88 | [-57, +2,658] | 53% | 53% by day 26 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 12 | 32 | +246 | 0.71 | [-430, +923] | 44% | 44% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 16 | 32 | +262 | 1.49 | [-82, +606] | 53% | 53% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 20 | 32 | +335 | 2.09 | [+20, +649] | 53% | 53% by day 28 |
| BUY_SEED | class blocked | 2 | 12 | +32,017 | 6.75 | [+22,721, +41,312] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 6 | 12 | +27,234 | 5.80 | [+18,025, +36,443] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 10 | 32 | +17,307 | 7.33 | [+12,677, +21,936] | 94% | 94% by day 22 |
| BUY_SEED | class blocked | 14 | 32 | +6,720 | 7.51 | [+4,966, +8,474] | 97% | 97% by day 24 |
| BUY_SEED | class blocked | 18 | 32 | +3,991 | 6.01 | [+2,689, +5,293] | 94% | 94% by day 26 |
| BUY_SEED | class blocked | 22 | 32 | +2,252 | 6.07 | [+1,525, +2,979] | 91% | 91% by day 29 |
| BUY_SEED | class blocked | 26 | 32 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED | -1 unit/day | 8 | 32 | +870 | 1.63 | [-179, +1,920] | 84% | 84% by day 26 |
| BUY_SEED | -1 unit/day | 12 | 32 | +825 | 3.29 | [+334, +1,316] | 91% | 91% by day 27 |
| BUY_SEED | -1 unit/day | 16 | 32 | +710 | 3.68 | [+331, +1,088] | 91% | 91% by day 28 |
| BUY_SEED | -1 unit/day | 20 | 32 | +444 | 4.11 | [+232, +656] | 84% | 84% by day 28 |
| BUY_SEED | -1 unit/day | 24 | 32 | +216 | 2.92 | [+71, +360] | 75% | 75% by day 29 |
| BUY_SEED:MELON | class blocked | 2 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 6 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 10 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 14 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 2 | 12 | +19,487 | 4.50 | [+10,992, +27,982] | 100% | 100% by day 21 |
| BUY_SEED:STRAWBERRY | class blocked | 6 | 12 | +12,168 | 2.35 | [+2,002, +22,334] | 67% | 67% by day 23 |
| BUY_SEED:STRAWBERRY | class blocked | 10 | 12 | +2,506 | 0.54 | [-6,564, +11,575] | 33% | 33% by day 25 |
| BUY_SEED:STRAWBERRY | class blocked | 14 | 12 | +1,510 | 2.08 | [+87, +2,933] | 58% | 58% by day 28 |
| BUY_SEED:STRAWBERRY | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| HIRE | class blocked | 2 | 12 | +60,467 | 8.28 | [+46,154, +74,780] | 100% | 100% by day 12 |
| HIRE | class blocked | 6 | 12 | +67,166 | 9.32 | [+53,044, +81,289] | 100% | 100% by day 11 |
| HIRE | class blocked | 10 | 12 | +65,554 | 9.34 | [+51,794, +79,315] | 100% | 100% by day 11 |
| HIRE | class blocked | 14 | 32 | +58,984 | 8.97 | [+46,102, +71,867] | 100% | 100% by day 15 |
| HIRE | class blocked | 18 | 32 | +44,291 | 9.10 | [+34,746, +53,835] | 100% | 100% by day 19 |
| HIRE | class blocked | 22 | 32 | +27,209 | 7.39 | [+19,990, +34,427] | 100% | 100% by day 23 |
| HIRE | class blocked | 26 | 32 | +12,805 | 9.78 | [+10,238, +15,371] | 100% | 100% by day 27 |
| HIRE | -1 unit/day | 8 | 32 | -1,907 | -2.64 | [-3,325, -489] | 28% | 28% by day 29 |
| HIRE | -1 unit/day | 12 | 64 | -2,108 | -6.31 | [-2,763, -1,453] | 12% | 12% by day 29 |
| HIRE | -1 unit/day | 16 | 32 | -832 | -3.82 | [-1,258, -405] | 19% | 19% by day 29 |
| HIRE | -1 unit/day | 20 | 64 | -1,178 | -10.36 | [-1,401, -955] | 8% | 8% by day 29 |
| HIRE | -1 unit/day | 24 | 32 | -361 | -3.34 | [-573, -150] | 9% | 9% by day 29 |
| HIRE | -2 unit/day | 12 | 32 | +153 | 0.24 | [-1,080, +1,385] | 59% | 59% by day 23 |
| HIRE | -2 unit/day | 20 | 32 | -531 | -1.77 | [-1,119, +58] | 22% | 22% by day 29 |

__Observational. Exact per-cell counterfactual against deterministic tapes; uncertainty is across tapes/seeds only. Downstream policy behaviour is held fixed, so a zero crossing is NOT an optimal cutoff day. Not wired to mutation weighting.__

A wide CI here is the measurement telling you the panel is too thin for that class, not that the class is worthless -- lumpy investments (animals, land) need more cells than the 12-cell margin panel provides. See `docs/AGE-360-horizon-roi.md`.

_Generated 2026-09-13 12:33. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._