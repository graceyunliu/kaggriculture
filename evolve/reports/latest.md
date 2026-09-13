# Evolution run 20260913-062740

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_pensukesan_107199477.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.01 h · candidates evaluated this run: 93 · games 28,164 (14,035/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 22 | 44 |
| dead_pattern | 8 | 16 |
| dead_smoke | 3 | 24 |
| alive | 15 | 2520 |
| held_fail | 0 | 0 |
| held_exploit | 0 | 0 |
| held_pass | 45 | 25560 |
| error | 0 | 0 |

Population (all runs, reached dev): 187 · held-out evaluated: 136 · held-out PASS: 135

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
| `41d34d27b102` | best | mutate | **+13,600** | 9.4 | 19-1 | -13,021 | +10,383 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |  | cand falls behind C1 from day 25 (gap -2,489 -> final -4,508); days 23-29 drivers: sales_rev -7,226, work_turns -162, water_hour +1.39, travel_per_task +0.06. Hands 4 vs 5, animals 9 vs 11, plants 4 v |
| `91aa2b2655cb` | best | ablate:fert_buy | **+13,158** | 8.4 | 19-1 | -13,097 | +10,688 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 18 (gap -1,697 -> final -2,673); days 16-23 drivers: sales_rev -2,036, work_turns -30, reversals +17, water_hour +0.85. Hands 12 vs 12, animals 10 vs 11, plants 51 vs 56. |
| `e920953119d2` | queue | migrate | **+13,113** | 9.4 | 19-1 | -12,408 | +10,959 | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,388 -> final -5,273); days 23-29 drivers: sales_rev -7,218, work_turns -171, water_hour +2.31, travel_per_task +0.07. Hands 4 vs 5, animals 9 vs 11, plants 3 v |
| `152620c1f6b5` | queue | archive_crossover:crossover_g000050_20260913-080130_1 | **+13,064** | 9.7 | 20-0 | -12,205 | +10,597 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 18 (gap -1,702 -> final -2,682); days 16-23 drivers: sales_rev -1,946, work_turns -30, reversals +17, water_hour +0.85. Hands 12 vs 12, animals 10 vs 11, plants 51 vs 56. |
| `cac9814edfe3` | best | paired | **+13,063** | 9.1 | 19-1 | -12,759 | +10,335 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | fert_buy -352, NEAR_RADIUS +831 | cand falls behind C1 from day 18 (gap -1,552 -> final -2,334); days 16-23 drivers: sales_rev -3,474, work_turns -39, reversals +17, idle_turns +6. Hands 12 vs 12, animals 10 vs 11, plants 47 vs 56. |
| `0fb60800f0b8` | queue | archive_crossover:crossover_g000025_20260913-071603_0 | **+13,028** | 8.8 | 19-1 | -12,244 | +10,892 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,939 -> final -4,855); days 23-29 drivers: sales_rev -6,702, work_turns -158, water_hour +2.29, travel_per_task +0.07. Hands 4 vs 5, animals 9 vs 11, plants 5 v |
| `5d74b7fca2be` | best | mutate | **+12,707** | 8.6 | 19-1 | -12,249 | +10,446 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,940 -> final -4,856); days 23-29 drivers: sales_rev -6,702, work_turns -158, water_hour +2.29, travel_per_task +0.07. Hands 4 vs 5, animals 9 vs 11, plants 5 v |
| `3c3e3fde03a7` | best | ablate:HIRE_MAX_MARGINAL | **+12,550** | 8.4 | 19-1 | -13,214 | +10,247 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -1,512 -> final -1,385); days 23-29 drivers: missed_water +11, sales_rev -1,592, water_hour +0.87. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `f1c0964659ce` | best | ablate:NEAR_RADIUS | **+12,221** | 8.6 | 19-1 | -13,230 | +9,504 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,771 -> final -1,857); days 23-29 drivers: water_hour +0.83, missed_water +2, sales_rev -203. Hands 4 vs 5, animals 10 vs 11, plants 3 vs 5. |
| `d8d74dd5996f` | queue | archive_crossover:crossover_g000050_20260913-060347_1 | **+12,063** | 7.9 | 19-1 | -12,624 | +10,050 | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |  | cand falls behind C1 from day 25 (gap -1,750 -> final -1,404); days 23-29 drivers: missed_water +9, weeds_new +2, sales_rev -1,087, water_hour +0.94. Hands 4 vs 5, animals 10 vs 11, plants 3 vs 5. |
| `b28ae97d6a33` | o15 | crossover | **+11,765** | 7.3 | 19-1 | -11,730 | +10,198 | min_hands 3→4, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7 |  | cand vs C1: net worth never diverged by >$1,500 (final +885). |
| `ba8386bf93f9` | best | ablate:HIRE_MAX_MARGINAL | **+11,400** | 8.6 | 19-1 | -12,235 | +8,270 | wheat_stock 0→1, open_melons 10→6, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, CROP_SWEEP_LEN 6→8, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0 |  | cand vs C1: net worth never diverged by >$1,500 (final +305). |
| `daf68d6d17e5` | o15 | mutate | **+11,342** | 10.1 | 20-0 | -14,195 | +9,498 | open_melons 10→11, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→128, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand pulls ahead of C1 from day 24 (gap +2,361 -> final +1,931); days 22-29 drivers: sales_rev +1,155, idle_turns -15, work_turns +12, feed_hour -0.11. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `f427aab69e55` | best | mutate | **+11,218** | 7.5 | 19-1 | -14,060 | +9,292 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→138, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, HIRE_MAX_MARGINAL 144→1000000000, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -3,343 -> final -3,057); days 23-29 drivers: idle_turns +25, missed_water +4, water_hour +0.89, sales_rev -513. Hands 4 vs 5, animals 10 vs 11, plants 3 vs 5. |
| `9915090a999f` | best | crossover | **+11,183** | 9.3 | 20-0 | -11,963 | +8,716 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, CROP_SWEEP_LEN 6→8, MELON_PRICE_CUSHION 100→116, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 24 (gap -2,451 -> final -4,119); days 22-29 drivers: sales_rev -4,938, work_turns -63, weeds_new +3, water_hour +0.89. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `e920953119d2` | queue | migrate | +10,959 | 9.1 | 29-1 | -9,441 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `0fb60800f0b8` | queue | archive_crossover:crossover_g000025_20260913-071603_0 | +10,892 | 8.1 | 28-2 | -8,764 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `91aa2b2655cb` | best | ablate:fert_buy | +10,688 | 8.3 | 28-2 | -9,381 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `152620c1f6b5` | queue | archive_crossover:crossover_g000050_20260913-080130_1 | +10,597 | 8.1 | 29-1 | -8,665 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `1687696c5756` | queue | archive_crossover:crossover_g000025_20260913-071603_1 | +10,548 | 8.8 | 28-2 | -6,435 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_cap 22→21, wheat_sell_price 30→29, MAX_HANDS 14→16, CROP_SWEEP_LEN 6→8, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `5d74b7fca2be` | best | mutate | +10,446 | 7.7 | 28-2 | -8,562 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `41d34d27b102` | best | mutate | +10,383 | 7.7 | 28-2 | -9,122 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |
| `c00ac4f1d57e` | o15 | crossover | +10,381 | 9.6 | 29-1 | -5,965 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_sell_price 30→29, MAX_HANDS 14→16, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→4, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `5714118c4c80` | o15 | paired | +10,342 | 9.6 | 28-2 | -6,222 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_sell_price 30→29, MAX_HANDS 14→16, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→6, OPENING_MELONS 14→13, FERT_RADIUS 3→4, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `cac9814edfe3` | best | paired | +10,335 | 8.6 | 28-2 | -8,233 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `bcd1ba95e530` | o15 | migrate | +10,291 | 9.6 | 29-1 | -6,299 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→4, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `3c3e3fde03a7` | best | ablate:HIRE_MAX_MARGINAL | +10,247 | 7.4 | 26-4 | -9,464 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `b28ae97d6a33` | o15 | crossover | +10,198 | 8.3 | 27-3 | -7,804 | held_pass | min_hands 3→4, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7 |
| `491359a7a7e5` | o15 | crossover | +10,107 | 9.5 | 28-2 | -6,968 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `d8d74dd5996f` | queue | archive_crossover:crossover_g000050_20260913-060347_1 | +10,050 | 7.3 | 27-3 | -8,983 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +10,688 (`91aa2b2655cb`), n=55
- o15: best +10,381 (`c00ac4f1d57e`), n=49
- queue: best +10,959 (`e920953119d2`), n=52
- wide: best +9,838 (`1920a874375b`), n=31

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| ROUTE_LEN | +16,348 | 2 | 3 | 4 | 187 | 2.32 | 2: +7,734 (n=27), 3: +4,520 (n=155), 4: +1,108 (n=3), 5: -8,614 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +16,023 | 9 | 8 | 6 | 186 | 3.22 | 9: +10,637 (n=4), 8: +5,606 (n=157), 11: +2,628 (n=5), 12: -1,290 (n=17), 6: -5,386 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +13,272 | 19 | 20 | 13 | 183 | 6.18 | 19: +7,831 (n=4), 16: +6,611 (n=2), 20: +5,581 (n=146), 18: +5,232 (n=6), 17: +4,130 (n=8), 13: +1,795 (n=2), 24: +194 (n=2), 15: -1,341 (n=11), 23: -5,441 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +10,742 | 13 | 14 | 6 | 186 | 3.14 | 13: +7,159 (n=3), 15: +6,390 (n=15), 14: +4,899 (n=154), 16: +3,987 (n=11), 12: -3,582 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +9,780 | 16 | 17 | 6 | 187 | 4.01 | 16: +6,198 (n=6), 17: +5,629 (n=156), 20: +2,853 (n=6), 15: -405 (n=2), 18: -1,811 (n=14), 12: -3,582 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +9,580 | frontier | frontier | 2 | 187 | 0.69 | frontier: +6,275 (n=158), v312: -3,305 (n=29) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +9,159 | 20 | 22 | 9 | 184 | 1.51 | 20: +7,474 (n=3), 22: +6,197 (n=62), 18: +5,412 (n=35), 21: +4,109 (n=77), 25: +3,592 (n=2), 15: -1,686 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +8,904 | 3 | 3 | 4 | 187 | 1.31 | 3: +6,001 (n=49), 2: +5,286 (n=108), 4: +4,022 (n=17), 1: -2,903 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +8,852 | 8 | 3 | 6 | 185 | 2.22 | 8: +5,496 (n=25), 3: +5,327 (n=9), 5: +4,762 (n=149), 7: -3,356 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +8,416 | 131 | 100 | 14 | 183 | 4.3 | 131: +6,301 (n=3), 116: +6,204 (n=49), 112: +6,055 (n=6), 128: +5,878 (n=7), 100: +5,098 (n=97), 94: +2,821 (n=2), 84: +2,477 (n=2), 134: +1,890 (n=3), 150: -1,142 (n=2), 107: -2,116 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +8,255 | 12 | 14 | 3 | 187 | 1.87 | 12: +7,749 (n=6), 14: +4,749 (n=179), 13: -507 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +8,217 | 1.0 | 1.4 | 7 | 185 | 1.49 | 1.0: +7,816 (n=6), 1.4: +5,805 (n=49), 1.2: +5,649 (n=30), 1.3: +4,163 (n=92), 1.7: -401 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +8,073 | 2 | 0 | 8 | 183 | 1.08 | 2: +5,576 (n=2), 1: +5,159 (n=95), 0: +4,584 (n=84), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,647 | 0.2 | 0.0 | 7 | 185 | 3.51 | 0.2: +6,982 (n=6), 0.0: +5,075 (n=167), 0.3: +3,693 (n=5), 0.5: +1,546 (n=3), 0.1: -664 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +7,551 | 0.55 | 0.55 | 5 | 187 | 3.17 | 0.55: +5,320 (n=156), 0.45: +5,278 (n=4), 0.5: +3,024 (n=19), 0.65: +194 (n=2), 0.7: -2,230 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_hold_days | +5,980 | 0 | 0 | 2 | 187 | 0.71 | 0: +5,652 (n=160), 1: -327 (n=27) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +5,675 | 19 | 19 | 3 | 187 | 1.7 | 19: +4,988 (n=168), 20: +3,470 (n=17), 18: -687 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +5,329 | 15 | 14 | 2 | 72 | 0.31 | 15: +7,044 (n=47), 14: +1,715 (n=25) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| feed_spare_poor | +5,048 | 0 | 0 | 4 | 186 | 1.89 | 0: +5,001 (n=179), 1: +1,161 (n=5), 2: -47 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_RADIUS | +4,943 | 5 | 5 | 4 | 186 | 1.29 | 5: +4,968 (n=142), 6: +4,785 (n=41), 4: +25 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 2, 4): +10,959 (n=4)
- (9, 3, 5): +10,688 (n=3)
- (10, 3, 4): +10,548 (n=16)
- (10, 3, 6): +10,381 (n=8)
- (9, 3, 4): +10,335 (n=12)
- (10, 3, 5): +10,247 (n=14)
- (11, 3, 4): +10,107 (n=51)
- (11, 3, 6): +9,823 (n=16)
- (11, 3, 5): +9,255 (n=53)
- (9, 3, 6): +3,828 (n=1)
- (13, 3, 6): +2,841 (n=1)
- (9, 3, 3): +2,012 (n=2)
- (14, 3, 5): +1,546 (n=2)
- (12, 3, 5): -239 (n=1)
- (14, 3, 6): -5,381 (n=1)

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

_Generated 2026-09-13 08:28. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 25 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–2 (n=25); wheat_stock=0–7 (n=25); min_hands=3–5 (n=25); load_per_hand=14–23 (n=25); open_melons=4–10 (n=25); open_cows=2–3 (n=25); open_sheep=0–3 (n=25); early_hire_days=3–7 (n=25)
- **Evidence:** 25 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**187 candidates** with action_table data, **25602 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,941 (n=2539) |         +4,789 (n=1309) |         +4,789 (n=1496) | 5344 |
| BUY_ANIMAL |         +4,632 (n=1302) |         +4,283 (n=249) |              — (n=0) | 1551 |
| BUY_SEED |         +5,079 (n=2068) |         +4,475 (n=674) |         +4,655 (n=295) | 3037 |
| BUY_LAND |         +4,739 (n=677) |         +4,097 (n=128) |              — (n=0) | 805 |
| BUY_PRODUCT |         +4,790 (n=2801) |         +4,789 (n=1309) |         +4,768 (n=1284) | 5394 |
| HIRE |         +4,742 (n=1392) |         +4,761 (n=652) |         +4,979 (n=477) | 2521 |
| WATER_MISSED |         +5,096 (n=2170) |         +4,789 (n=1309) |         +4,785 (n=1481) | 4960 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,648 (n=1186) |         +2,711 (n=353) |         +3,789 (n=451) | 1990 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,168 |      +4,790 |      +4,756 |      +5,344 |      +4,766 |      +4,731 |
| BUY_ANIMAL |      +3,819 |           — |           — |           — |      +6,275 |      +4,499 |
| BUY_SEED |      +4,755 |      +4,819 |      +3,347 |           — |      +6,178 |      +4,859 |
| BUY_LAND |           — |      -1,945 |      +4,898 |      -2,705 |      +6,140 |      +4,377 |
| BUY_PRODUCT |      +4,784 |           — |           — |           — |           — |           — |
| HIRE |      +4,792 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,789 |      +5,916 |      +4,789 |      +4,899 |
| FEED_MISSED |           — |      +4,787 |      +4,821 |           — |           — |      +4,030 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | WATER_MISSED | early | +5,096 | 2170 | 1.08 |
| 2 | BUY_SEED | early | +5,079 | 2068 | 1.06 |
| 3 | HIRE | late | +4,979 | 477 | 0.99 |
| 4 | SELL | early | +4,941 | 2539 | 1.02 |
| 5 | BUY_PRODUCT | early | +4,790 | 2801 | 0.97 |
| 6 | SELL | mid | +4,789 | 1309 | 0.97 |
| 7 | SELL | late | +4,789 | 1496 | 0.97 |
| 8 | BUY_PRODUCT | mid | +4,789 | 1309 | 0.97 |
| 9 | WATER_MISSED | mid | +4,789 | 1309 | 0.97 |
| 10 | WATER_MISSED | late | +4,785 | 1481 | 0.96 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +6,844 (n=264)
- **BUY_LAND** in ('mid', 'low', 'mid', 'high'): +6,549 (n=10)
- **SELL** in ('mid', 'low', 'high', 'low'): +6,511 (n=90)
- **FEED_MISSED** in ('mid', 'low', 'high', 'low'): +6,511 (n=90)
- **WATER_MISSED** in ('mid', 'low', 'high', 'low'): +6,438 (n=84)
- **FEED_MISSED** in ('mid', 'low', 'mid', 'high'): +6,390 (n=9)
- **WATER_MISSED** in ('low', 'mid', 'high', 'high'): +6,336 (n=59)
- **BUY_SEED** in ('low', 'mid', 'high', 'high'): +6,319 (n=54)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +6,305 (n=124)
- **SELL** in ('low', 'mid', 'high', 'high'): +6,271 (n=64)
- **BUY_PRODUCT** in ('low', 'mid', 'high', 'high'): +6,271 (n=64)
- **SELL** in ('low', 'low', 'mid', 'mid'): +6,247 (n=150)
- **HIRE** in ('low', 'mid', 'high', 'high'): +6,192 (n=61)
- **SELL** in ('mid', 'low', 'mid', 'high'): +6,137 (n=11)
- **BUY_ANIMAL** in ('mid', 'low', 'mid', 'high'): +6,137 (n=11)

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

_Generated 2026-09-13 08:28. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._