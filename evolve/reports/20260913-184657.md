# Evolution run 20260913-184657

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_pensukesan_107199477.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.02 h · candidates evaluated this run: 83 · games 27,068 (13,406/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 21 | 42 |
| dead_pattern | 5 | 10 |
| dead_smoke | 1 | 8 |
| alive | 12 | 2016 |
| held_fail | 0 | 0 |
| held_exploit | 0 | 0 |
| held_pass | 44 | 24992 |
| error | 0 | 0 |

Population (all runs, reached dev): 510 · held-out evaluated: 412 · held-out PASS: 408

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
| `1841df5abdd8` | best | paired | **+14,055** | 9.9 | 19-1 | -12,300 | +12,225 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, max_animals 17→15, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→68, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand vs C1: net worth never diverged by >$1,500 (final -59). |
| `39ac3d97c0b8` | best | ablate:NEAR_RADIUS | **+13,992** | 9.3 | 19-1 | -13,308 | +10,530 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, MAX_HANDS 14→13, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -3,436 -> final -3,436); days 27-29 drivers: work_turns -35, water_hour +1.93, sales_rev -478, travel_per_task +0.09. Hands 4 vs 5, animals 10 vs 11, plants 4 vs  |
| `313a1744dfa4` | queue | crossover | **+13,961** | 10.2 | 19-1 | -12,486 | +11,941 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,121 -> final -1,755); days 23-29 drivers: sales_rev -3,691, missed_water +11, work_turns -28, water_hour +0.39. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `ee8e05d20ed6` | best | paired | **+13,958** | 9.9 | 19-1 | -12,313 | +12,217 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, max_animals 17→15, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, MELON_PRICE_CUSHION 100→68, HERD_LAST_DAY 17→18, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand vs C1: net worth never diverged by >$1,500 (final +86). |
| `e118bd7b0321` | queue | ablate:wheat_tiles | **+13,900** | 10.6 | 19-1 | -12,654 | +12,209 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→68, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand vs C1: net worth never diverged by >$1,500 (final +516). |
| `b631ee86f5f0` | best | crossover | **+13,844** | 9.7 | 19-1 | -12,308 | +11,012 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | wheat_stock -315, demand_share +89, HERD_LAST_DAY -18, OPP_GROWTH ?, FERT_RADIUS ?, MELON_MORNING_LAST_HOUR ? | cand falls behind C1 from day 25 (gap -3,362 -> final -5,064); days 23-29 drivers: sales_rev -7,804, work_turns -172, water_hour +2.49. Hands 3 vs 5, animals 9 vs 11, plants 2 vs 5. |
| `7be2cfe703c1` | best | ablate:HERD_LAST_DAY | **+13,844** | 9.7 | 19-1 | -12,267 | +11,030 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,362 -> final -5,064); days 23-29 drivers: sales_rev -7,804, work_turns -172, water_hour +2.49. Hands 3 vs 5, animals 9 vs 11, plants 2 vs 5. |
| `f70383b38bc1` | best | ablate:demand_share | **+13,728** | 10.4 | 19-1 | -12,614 | +10,923 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,362 -> final -5,064); days 23-29 drivers: sales_rev -7,804, work_turns -172, water_hour +2.49. Hands 3 vs 5, animals 9 vs 11, plants 2 vs 5. |
| `852a80c5a2cd` | o15 | crossover | **+13,648** | 7.9 | 19-1 | -12,891 | +9,512 | min_hands 3→4, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→5, HIRE_MAX_MARGINAL 144→89, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand vs C1: net worth never diverged by >$1,500 (final +663). |
| `41d34d27b102` | best | mutate | **+13,600** | 9.4 | 19-1 | -13,021 | +10,383 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |  | cand falls behind C1 from day 25 (gap -2,489 -> final -4,508); days 23-29 drivers: sales_rev -7,226, work_turns -162, water_hour +1.39, travel_per_task +0.06. Hands 4 vs 5, animals 9 vs 11, plants 4 v |
| `c49b60cd642e` | queue | ablate:ROUTE_LEN | **+13,579** | 9.2 | 19-1 | -12,611 | +11,037 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,777 -> final -4,623); days 23-29 drivers: sales_rev -7,041, work_turns -163, water_hour +2.11, travel_per_task +0.08. Hands 4 vs 5, animals 9 vs 11, plants 3 v |
| `b4cb1c42bbf1` | best | ablate:wheat_hold_days | **+13,559** | 8.7 | 19-1 | -11,813 | +10,906 | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,219 -> final -5,175); days 23-29 drivers: sales_rev -7,027, work_turns -162, water_hour +2.07, travel_per_task +0.04. Hands 4 vs 5, animals 9 vs 11, plants 5 v |
| `d2daf1e0ea76` | queue | archive_crossover:crossover_g000050_20260913-182626_0 | **+13,463** | 9.6 | 19-1 | -12,873 | +11,079 | load_per_hand 20→18, open_melons 10→9, early_hire_days 3→2, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand vs C1: net worth never diverged by >$1,500 (final -461). |
| `228b0aa36b2a` | queue | ablate:ROUTE_LEN | **+13,396** | 9.9 | 19-1 | -13,117 | +10,040 | open_melons 10→11, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand falls behind C1 from day 24 (gap -2,400 -> final -3,202); days 22-29 drivers: sales_rev -5,291, weeds_new +4, missed_water +11, water_hour +1.26. Hands 5 vs 5, animals 11 vs 11, plants 3 vs 5. |
| `67de8cb9a0f5` | best | paired | **+13,382** | 7.8 | 19-1 | -12,425 | +10,688 | min_hands 3→4, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | min_hands ?, HERD_LAST_DAY ? | cand falls behind C1 from day 26 (gap -1,751 -> final -957); days 24-29 drivers: missed_water +10, water_hour +1.37, idle_turns +19, weeds_new +1. Hands 4 vs 5, animals 10 vs 11, plants 4 vs 5. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `e10bb85f9628` | queue | archive_crossover:crossover_g000025_20260913-174858_1 | +12,542 | 9.4 | 29-1 | -7,599 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `5ad3ef14718a` | o15 | paired | +12,511 | 9.3 | 28-2 | -7,617 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `1841df5abdd8` | best | paired | +12,225 | 9.0 | 28-2 | -8,821 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, max_animals 17→15, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→68, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `ee8e05d20ed6` | best | paired | +12,217 | 9.1 | 28-2 | -8,671 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, max_animals 17→15, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, MELON_PRICE_CUSHION 100→68, HERD_LAST_DAY 17→18, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `e118bd7b0321` | queue | ablate:wheat_tiles | +12,209 | 9.0 | 28-2 | -9,136 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→68, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `313a1744dfa4` | queue | crossover | +11,941 | 9.0 | 28-2 | -8,743 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `1e3e1c9cde5c` | o15 | mutate | +11,785 | 9.4 | 29-1 | -8,297 | held_pass | min_hands 3→4, open_melons 10→8, early_hire_days 3→6, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→12, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `24f5e1b3f3bd` | best | crossover | +11,756 | 9.9 | 29-1 | -9,145 | held_pass | min_hands 3→4, load_per_hand 20→18, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `61a12172c108` | queue | crossover | +11,427 | 8.6 | 29-1 | -7,334 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→1, SPREAD_CAP 3→4, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `8d0ca1414f62` | queue | archive_crossover:crossover_g000025_20260913-195520_0 | +11,400 | 8.6 | 29-1 | -7,376 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `c9a25601ec1b` | queue | ablate:NEAR_RADIUS | +11,367 | 8.4 | 28-2 | -9,328 | held_pass | load_per_hand 20→18, open_melons 10→9, early_hire_days 3→2, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→4, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `56d939a91e51` | best | ablate:demand_share | +11,366 | 8.7 | 29-1 | -8,354 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, wheat_hold_days 0→1, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `6fcc9aa61ae2` | queue | archive_crossover:crossover_g000050_20260913-143209_1 | +11,333 | 8.2 | 28-2 | -9,154 | held_pass | load_per_hand 20→18, open_melons 10→9, early_hire_days 3→2, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→4, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `59f341ad73c8` | best | ablate:wheat_stock | +11,327 | 8.4 | 29-1 | -7,381 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.5, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `c47269413727` | queue | archive_crossover:crossover_g000050_20260913-143209_0 | +11,295 | 8.5 | 29-1 | -7,378 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +12,225 (`1841df5abdd8`), n=147
- o15: best +12,511 (`5ad3ef14718a`), n=124
- queue: best +12,542 (`e10bb85f9628`), n=140
- wide: best +10,862 (`3c3019342df8`), n=99

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| ROUTE_LEN | +16,937 | 2 | 3 | 4 | 510 | 1.37 | 2: +8,324 (n=199), 3: +5,154 (n=302), 4: +1,262 (n=7), 5: -8,614 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,458 | 82 | 100 | 29 | 499 | 10.94 | 82: +10,316 (n=3), 101: +10,215 (n=10), 111: +9,174 (n=7), 68: +9,029 (n=11), 100: +6,822 (n=331), 112: +6,296 (n=7), 116: +6,191 (n=63), 99: +6,108 (n=3), 131: +6,008 (n=4), 93: +5,956 (n=4), 128: +5,869 (n=8), 136: +4,005 (n=2), 94: +2,821 (n=2), 90: +2,614 (n=2), 84: +2,477 (n=2), 134: +1,992 (n=4), 107: +1,104 (n=34), 150: -1,142 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +11,353 | 9 | 0 | 11 | 505 | 2.4 | 9: +8,856 (n=2), 1: +6,685 (n=211), 0: +6,124 (n=286), 2: +5,576 (n=2), 3: +2,016 (n=2), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,337 | 0.4 | 0.55 | 10 | 509 | 6.09 | 0.4: +9,871 (n=2), 0.6: +7,762 (n=9), 0.55: +6,604 (n=401), 0.5: +6,127 (n=72), 0.45: +5,278 (n=4), 0.3: +4,005 (n=2), 0.75: +3,869 (n=2), 0.65: +963 (n=4), 0.7: -1,465 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,138 | 19 | 20 | 14 | 509 | 8.22 | 19: +8,147 (n=21), 18: +7,042 (n=37), 20: +6,923 (n=361), 14: +4,798 (n=3), 16: +4,568 (n=3), 22: +4,508 (n=10), 21: +3,949 (n=2), 17: +3,919 (n=29), 13: +3,027 (n=3), 23: +2,794 (n=5), 15: +1,920 (n=31), 24: +194 (n=2), 12: -2,992 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +11,119 | 5 | 8 | 9 | 510 | 5.62 | 5: +8,710 (n=3), 9: +8,342 (n=62), 10: +8,026 (n=5), 8: +6,691 (n=375), 4: +6,668 (n=9), 12: +1,215 (n=43), 7: +1,101 (n=3), 11: +1,040 (n=6), 6: -2,409 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,615 | 24 | 22 | 13 | 506 | 4.14 | 24: +9,483 (n=2), 21: +6,806 (n=289), 22: +6,540 (n=134), 18: +5,405 (n=47), 20: +4,652 (n=7), 23: +4,168 (n=2), 25: +3,131 (n=15), 19: +550 (n=2), 15: -1,133 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,473 | 17 | 17 | 10 | 507 | 5.09 | 17: +6,891 (n=441), 15: +6,575 (n=11), 14: +6,100 (n=6), 16: +5,906 (n=9), 20: +1,094 (n=13), 18: -237 (n=24), 12: -3,582 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +9,071 | frontier | frontier | 2 | 510 | 0.76 | frontier: +7,351 (n=450), v312: -1,720 (n=60) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,862 | 2 | 2 | 4 | 510 | 2.65 | 2: +6,446 (n=466), 1: +5,841 (n=36), 0: +59 (n=4), 3: -2,416 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +8,358 | 1.5 | 1.4 | 9 | 510 | 3.25 | 1.5: +9,137 (n=57), 1.2: +7,004 (n=65), 1.6: +6,225 (n=7), 1.4: +6,218 (n=109), 1.3: +5,897 (n=241), 1.0: +5,110 (n=9), 1.1: +3,937 (n=4), 1.8: +3,334 (n=4), 1.7: +779 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +7,610 | 1 | 0 | 3 | 510 | 1.98 | 1: +8,213 (n=2), 0: +6,299 (n=506), 2: +603 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +7,391 | 15 | 14 | 8 | 508 | 2.27 | 15: +8,623 (n=131), 13: +6,643 (n=23), 12: +6,617 (n=15), 16: +6,599 (n=59), 14: +5,221 (n=277), 11: +1,232 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +6,067 | 13 | 14 | 8 | 508 | 4.39 | 13: +6,795 (n=14), 14: +6,661 (n=456), 9: +3,268 (n=18), 12: +2,460 (n=2), 11: +782 (n=2), 10: +728 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +5,853 | 38 | 30 | 12 | 508 | 2.72 | 38: +8,245 (n=3), 26: +8,065 (n=53), 42: +7,593 (n=11), 25: +7,030 (n=86), 29: +7,005 (n=150), 27: +5,789 (n=6), 35: +5,766 (n=2), 30: +4,935 (n=189), 43: +4,114 (n=5), 40: +2,392 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +5,711 | 12 | 14 | 3 | 146 | 0.48 | 12: +11,128 (n=4), 15: +7,454 (n=72), 14: +5,417 (n=70) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +5,383 | 0.0 | 0.0 | 9 | 507 | 4.48 | 0.0: +6,561 (n=463), 0.2: +5,053 (n=25), 0.3: +4,903 (n=8), 0.6: +1,676 (n=2), 0.5: +1,546 (n=3), 0.1: +1,178 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| min_hands | +5,139 | 5 | 3 | 4 | 510 | 2.59 | 5: +7,200 (n=5), 4: +7,132 (n=45), 3: +6,209 (n=458), 6: +2,061 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +4,744 | 6 | 10 | 11 | 509 | 6.82 | 6: +7,602 (n=7), 11: +6,978 (n=14), 10: +6,794 (n=18), 7: +6,667 (n=3), 9: +6,396 (n=398), 5: +6,235 (n=5), 8: +6,040 (n=41), 12: +5,770 (n=7), 13: +3,083 (n=2), 4: +2,858 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +4,510 | 2 | 3 | 8 | 510 | 5.34 | 2: +8,040 (n=27), 6: +7,667 (n=8), 3: +6,360 (n=22), 5: +6,202 (n=404), 8: +6,065 (n=33), 0: +6,023 (n=7), 4: +5,223 (n=4), 7: +3,530 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 4): +12,542 (n=47)
- (9, 3, 5): +12,225 (n=18)
- (10, 3, 5): +11,941 (n=44)
- (10, 3, 4): +11,785 (n=64)
- (9, 2, 4): +11,427 (n=13)
- (10, 3, 6): +11,333 (n=18)
- (11, 3, 6): +11,266 (n=42)
- (9, 2, 3): +11,030 (n=7)
- (11, 3, 4): +11,011 (n=88)
- (11, 3, 5): +10,862 (n=135)
- (12, 3, 6): +10,094 (n=3)
- (12, 3, 5): +9,637 (n=7)
- (10, 3, 3): +7,686 (n=2)
- (13, 3, 6): +5,671 (n=6)
- (9, 3, 3): +5,166 (n=3)

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

_Generated 2026-09-13 20:48. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 90 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–4 (n=90); wheat_stock=0–7 (n=90); min_hands=3–5 (n=90); load_per_hand=12–26 (n=90); open_melons=4–14 (n=90); open_cows=1–3 (n=90); open_sheep=0–3 (n=90); early_hire_days=0–7 (n=90)
- **Evidence:** 90 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**510 candidates** with action_table data, **69616 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +6,346 (n=6895) |         +6,284 (n=3570) |         +6,284 (n=4080) | 14545 |
| BUY_ANIMAL |         +6,093 (n=3477) |         +6,094 (n=731) |              — (n=0) | 4208 |
| BUY_SEED |         +6,517 (n=5664) |         +6,266 (n=1862) |         +6,083 (n=744) | 8270 |
| BUY_LAND |         +6,269 (n=1832) |         +5,977 (n=358) |              — (n=0) | 2190 |
| BUY_PRODUCT |         +6,285 (n=7642) |         +6,284 (n=3570) |         +6,293 (n=3520) | 14732 |
| HIRE |         +6,268 (n=3821) |         +6,400 (n=1817) |         +6,624 (n=1215) | 6853 |
| WATER_MISSED |         +6,498 (n=6011) |         +6,284 (n=3570) |         +6,283 (n=4029) | 13610 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +6,115 (n=3125) |         +4,978 (n=912) |         +5,585 (n=1171) | 5208 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +6,452 |      +6,295 |      +6,090 |      +6,796 |      +6,191 |      +6,250 |
| BUY_ANIMAL |      +5,446 |           — |           — |           — |      +7,351 |      +6,042 |
| BUY_SEED |      +6,245 |      +6,556 |      +2,989 |        +927 |      +7,492 |      +6,386 |
| BUY_LAND |           — |        -276 |      +6,356 |      -1,113 |      +6,769 |      +6,204 |
| BUY_PRODUCT |      +6,286 |           — |           — |           — |           — |           — |
| HIRE |      +6,366 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +6,284 |      +7,016 |      +6,284 |      +6,363 |
| FEED_MISSED |           — |      +6,297 |      +4,673 |           — |           — |      +5,755 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | HIRE | late | +6,624 | 1215 | 1.47 |
| 2 | BUY_SEED | early | +6,517 | 5664 | 1.49 |
| 3 | WATER_MISSED | early | +6,498 | 6011 | 1.5 |
| 4 | HIRE | mid | +6,400 | 1817 | 1.38 |
| 5 | SELL | early | +6,346 | 6895 | 1.43 |
| 6 | BUY_PRODUCT | late | +6,293 | 3520 | 1.39 |
| 7 | BUY_PRODUCT | early | +6,285 | 7642 | 1.39 |
| 8 | SELL | mid | +6,284 | 3570 | 1.39 |
| 9 | SELL | late | +6,284 | 4080 | 1.39 |
| 10 | BUY_PRODUCT | mid | +6,284 | 3570 | 1.39 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **FEED_MISSED** in ('mid', 'low', 'mid', 'high'): +9,416 (n=63)
- **BUY_LAND** in ('mid', 'low', 'mid', 'high'): +9,394 (n=65)
- **SELL** in ('mid', 'low', 'mid', 'high'): +9,282 (n=66)
- **BUY_ANIMAL** in ('mid', 'low', 'mid', 'high'): +9,282 (n=66)
- **BUY_SEED** in ('mid', 'low', 'mid', 'high'): +9,282 (n=66)
- **BUY_PRODUCT** in ('mid', 'low', 'mid', 'high'): +9,282 (n=66)
- **WATER_MISSED** in ('mid', 'low', 'mid', 'high'): +9,282 (n=66)
- **WATER_MISSED** in ('low', 'mid', 'high', 'high'): +7,823 (n=238)
- **BUY_SEED** in ('low', 'mid', 'high', 'high'): +7,793 (n=219)
- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +7,786 (n=743)
- **HIRE** in ('low', 'mid', 'high', 'high'): +7,665 (n=248)
- **SELL** in ('low', 'mid', 'high', 'high'): +7,577 (n=256)
- **BUY_PRODUCT** in ('low', 'mid', 'high', 'high'): +7,577 (n=256)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +7,519 (n=37)
- **SELL** in ('low', 'low', 'low', 'mid'): +7,455 (n=40)

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

_Generated 2026-09-13 20:48. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._