# Evolution run 20260913-042057

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_pensukesan_107199477.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.09 h · candidates evaluated this run: 94 · games 28,578 (13,670/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 21 | 42 |
| dead_pattern | 8 | 16 |
| dead_smoke | 0 | 0 |
| alive | 21 | 3528 |
| held_fail | 0 | 0 |
| held_exploit | 0 | 0 |
| held_pass | 44 | 24992 |
| error | 0 | 0 |

Population (all runs, reached dev): 127 · held-out evaluated: 91 · held-out PASS: 90

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
| `cac9814edfe3` | best | paired | **+13,063** | 9.1 | 19-1 | -12,759 | +10,335 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | fert_buy -352, NEAR_RADIUS +831 | cand falls behind C1 from day 18 (gap -1,552 -> final -2,334); days 16-23 drivers: sales_rev -3,474, work_turns -39, reversals +17, idle_turns +6. Hands 12 vs 12, animals 10 vs 11, plants 47 vs 56. |
| `5d74b7fca2be` | best | mutate | **+12,707** | 8.6 | 19-1 | -12,249 | +10,446 | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,940 -> final -4,856); days 23-29 drivers: sales_rev -6,702, work_turns -158, water_hour +2.29, travel_per_task +0.07. Hands 4 vs 5, animals 9 vs 11, plants 5 v |
| `3c3e3fde03a7` | best | ablate:HIRE_MAX_MARGINAL | **+12,550** | 8.4 | 19-1 | -13,214 | +10,247 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -1,512 -> final -1,385); days 23-29 drivers: missed_water +11, sales_rev -1,592, water_hour +0.87. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `f1c0964659ce` | best | ablate:NEAR_RADIUS | **+12,221** | 8.6 | 19-1 | -13,230 | +9,504 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,771 -> final -1,857); days 23-29 drivers: water_hour +0.83, missed_water +2, sales_rev -203. Hands 4 vs 5, animals 10 vs 11, plants 3 vs 5. |
| `d8d74dd5996f` | queue | archive_crossover:crossover_g000050_20260913-060347_1 | **+12,063** | 7.9 | 19-1 | -12,624 | +10,050 | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |  | cand falls behind C1 from day 25 (gap -1,750 -> final -1,404); days 23-29 drivers: missed_water +9, weeds_new +2, sales_rev -1,087, water_hour +0.94. Hands 4 vs 5, animals 10 vs 11, plants 3 vs 5. |
| `daf68d6d17e5` | o15 | mutate | **+11,342** | 10.1 | 20-0 | -14,195 | +9,498 | open_melons 10→11, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→128, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand pulls ahead of C1 from day 24 (gap +2,361 -> final +1,931); days 22-29 drivers: sales_rev +1,155, idle_turns -15, work_turns +12, feed_hour -0.11. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `239b8ee3af09` | best | paired | **+11,087** | 8.5 | 19-1 | -14,397 | +9,061 | open_melons 10→11, early_hire_days 3→5, feed_spare_poor 0→1, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→128, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand vs C1: net worth never diverged by >$1,500 (final -1,304). |
| `f2bf74946332` | best | block_pair | **+10,419** | 8.1 | 20-0 | -12,033 | +7,617 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,773 -> final -3,664); days 23-29 drivers: sales_rev -5,508, work_turns -73, missed_water +10, weeds_new +1. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `daafdfe5833a` | best | ablate:min_hands | **+10,249** | 7.6 | 20-0 | -11,643 | +8,332 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→15, CROP_SWEEP_LEN 6→8, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -1,600 -> final -2,266); days 23-29 drivers: sales_rev -3,789, weeds_new +4, work_turns -49, water_hour +0.96. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `19ab6fc743ad` | wide | mutate | **+10,135** | 7.9 | 20-0 | -12,223 | +7,508 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -2,738 -> final -2,738); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `55aee088b1f5` | best | crossover | **+10,072** | 7.3 | 20-0 | -12,135 | +7,418 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, CROP_SWEEP_LEN 6→8, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | opening +10,071, CROP_SWEEP_LEN ? | cand falls behind C1 from day 29 (gap -2,738 -> final -2,738); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `6abb364c586c` | o15 | ablate:wheat_stock | **+10,071** | 7.3 | 20-0 | -12,138 | +7,456 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand falls behind C1 from day 29 (gap -2,739 -> final -2,739); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `c00ac4f1d57e` | o15 | crossover | **+10,057** | 7.3 | 20-0 | -11,865 | +10,381 | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_sell_price 30→29, MAX_HANDS 14→16, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→4, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand vs C1: net worth never diverged by >$1,500 (final -1,420). |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `91aa2b2655cb` | best | ablate:fert_buy | +10,688 | 8.3 | 28-2 | -9,381 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `5d74b7fca2be` | best | mutate | +10,446 | 7.7 | 28-2 | -8,562 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `41d34d27b102` | best | mutate | +10,383 | 7.7 | 28-2 | -9,122 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |
| `c00ac4f1d57e` | o15 | crossover | +10,381 | 9.6 | 29-1 | -5,965 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_sell_price 30→29, MAX_HANDS 14→16, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→4, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `cac9814edfe3` | best | paired | +10,335 | 8.6 | 28-2 | -8,233 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `bcd1ba95e530` | o15 | migrate | +10,291 | 9.6 | 29-1 | -6,299 | held_pass | open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→4, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `3c3e3fde03a7` | best | ablate:HIRE_MAX_MARGINAL | +10,247 | 7.4 | 26-4 | -9,464 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `491359a7a7e5` | o15 | crossover | +10,107 | 9.5 | 28-2 | -6,968 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `d8d74dd5996f` | queue | archive_crossover:crossover_g000050_20260913-060347_1 | +10,050 | 7.3 | 27-3 | -8,983 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→26, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0 |
| `a8cd98e17af1` | o15 | ablate:wheat_sell_price | +9,753 | 8.8 | 28-2 | -6,913 | held_pass | open_melons 10→9, early_hire_days 3→5, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `d43a6c30c331` | o15 | paired | +9,707 | 8.5 | 28-2 | -7,121 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, MAX_HANDS 14→13, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→20, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `f1c0964659ce` | best | ablate:NEAR_RADIUS | +9,504 | 7.0 | 26-4 | -8,763 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, fert_buy 4→3, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `daf68d6d17e5` | o15 | mutate | +9,498 | 8.2 | 27-3 | -9,087 | held_pass | open_melons 10→11, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→128, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `9c750e2fa0d1` | best | crossover | +9,356 | 8.4 | 29-1 | -7,714 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→21, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `30c6caf977f8` | o15 | mutate | +9,133 | 7.8 | 28-2 | -7,347 | held_pass | load_per_hand 20→17, open_melons 10→9, early_hire_days 3→5, demand_share 0.55→0.5, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→16, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +10,688 (`91aa2b2655cb`), n=40
- o15: best +10,381 (`c00ac4f1d57e`), n=36
- queue: best +10,050 (`d8d74dd5996f`), n=30
- wide: best +7,508 (`19ab6fc743ad`), n=21

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| load_per_hand | +13,815 | 19 | 20 | 11 | 124 | 5.45 | 19: +8,374 (n=2), 17: +6,312 (n=4), 20: +5,596 (n=100), 18: +3,706 (n=3), 13: +1,795 (n=2), 24: +194 (n=2), 15: -1,995 (n=9), 23: -5,441 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,542 | 0.45 | 0.55 | 5 | 127 | 3.37 | 0.45: +7,870 (n=3), 0.55: +5,026 (n=111), 0.5: +2,770 (n=7), 0.65: +194 (n=2), 0.7: -3,672 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_RADIUS | +10,616 | 6 | 5 | 4 | 126 | 1.43 | 6: +5,174 (n=22), 5: +4,802 (n=102), 4: -5,441 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +10,504 | 4 | 3 | 4 | 127 | 1.46 | 4: +7,403 (n=4), 3: +6,685 (n=35), 2: +4,538 (n=78), 1: -3,101 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +10,486 | 128 | 100 | 11 | 122 | 2.25 | 128: +8,660 (n=4), 112: +6,055 (n=6), 116: +5,585 (n=33), 100: +5,288 (n=66), 84: +2,477 (n=2), 107: -1,826 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +10,053 | frontier | frontier | 2 | 127 | 0.7 | frontier: +6,122 (n=108), v312: -3,930 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +9,967 | 20 | 22 | 6 | 126 | 1.06 | 20: +7,474 (n=3), 22: +6,698 (n=41), 18: +5,223 (n=26), 21: +3,122 (n=52), 15: -2,493 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +9,720 | 3 | 3 | 4 | 127 | 2.09 | 3: +6,365 (n=8), 8: +5,077 (n=19), 5: +4,550 (n=98), 7: -3,356 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +8,577 | 16 | 17 | 5 | 126 | 2.3 | 16: +7,035 (n=5), 17: +5,409 (n=104), 20: +2,484 (n=4), 18: -1,542 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +8,415 | 1.0 | 1.4 | 6 | 126 | 1.66 | 1.0: +8,015 (n=4), 1.4: +7,197 (n=29), 1.2: +5,367 (n=18), 1.3: +3,648 (n=67), 1.7: -401 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +8,073 | 2 | 0 | 7 | 124 | 1.32 | 2: +5,576 (n=2), 0: +4,811 (n=48), 1: +4,735 (n=72), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +7,625 | 2 | 3 | 4 | 126 | 1.71 | 2: +8,733 (n=9), 3: +4,478 (n=114), 4: +1,108 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +7,407 | 8 | 8 | 5 | 125 | 1.59 | 8: +5,534 (n=108), 11: +2,277 (n=3), 12: -1,873 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,580 | 0.2 | 0.0 | 5 | 127 | 3.57 | 0.2: +6,774 (n=3), 0.3: +5,953 (n=3), 0.0: +4,698 (n=116), 0.1: +997 (n=3), 0.5: +194 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| NEAR_RADIUS | +5,899 | 4 | 2 | 3 | 127 | 1.76 | 4: +10,182 (n=5), 3: +6,904 (n=5), 2: +4,283 (n=117) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +5,679 | 15 | 14 | 2 | 52 | 0.15 | 15: +6,997 (n=30), 14: +1,318 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +5,536 | 19 | 19 | 3 | 127 | 1.65 | 19: +4,849 (n=112), 20: +3,445 (n=13), 18: -687 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_hold_days | +5,341 | 0 | 0 | 2 | 127 | 0.65 | 0: +5,544 (n=105), 1: +203 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +5,246 | 9 | 14 | 6 | 125 | 2.46 | 9: +5,635 (n=5), 14: +5,031 (n=108), 13: +2,437 (n=3), 10: +389 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +4,832 | 10 | 6 | 8 | 126 | 1.61 | 10: +7,070 (n=2), 8: +6,440 (n=44), 7: +5,858 (n=6), 4: +5,532 (n=2), 3: +5,509 (n=23), 5: +2,564 (n=2), 6: +2,238 (n=47) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +10,688 (n=1)
- (9, 2, 4): +10,446 (n=2)
- (10, 3, 6): +10,381 (n=6)
- (9, 3, 4): +10,335 (n=8)
- (10, 3, 5): +10,247 (n=8)
- (11, 3, 4): +10,107 (n=34)
- (10, 3, 4): +10,050 (n=9)
- (11, 3, 5): +8,841 (n=42)
- (11, 3, 6): +8,721 (n=11)
- (13, 3, 6): +2,841 (n=1)
- (9, 3, 3): +804 (n=1)
- (14, 3, 6): -5,381 (n=1)
- (14, 3, 5): -5,502 (n=1)
- (11, 3, 3): -5,872 (n=1)
- (8, 3, 6): -6,019 (n=1)

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

_Generated 2026-09-13 06:26. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 14 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–2 (n=14); wheat_stock=0–1 (n=14); min_hands=3–4 (n=14); load_per_hand=14–21 (n=14); open_melons=4–10 (n=14); open_cows=2–3 (n=14); open_sheep=0–3 (n=14); early_hire_days=3–6 (n=14)
- **Evidence:** 14 candidates, multiple seeds. Confidence: moderate

## Action timing patterns (AGE-359: observational — correlations, not causes)

**127 candidates** with action_table data, **17399 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,796 (n=1730) |         +4,618 (n=889) |         +4,618 (n=1016) | 3635 |
| BUY_ANIMAL |         +4,389 (n=879) |         +3,998 (n=170) |              — (n=0) | 1049 |
| BUY_SEED |         +4,926 (n=1419) |         +4,179 (n=447) |         +4,549 (n=210) | 2076 |
| BUY_LAND |         +4,591 (n=466) |         +3,914 (n=80) |              — (n=0) | 546 |
| BUY_PRODUCT |         +4,620 (n=1902) |         +4,618 (n=889) |         +4,582 (n=870) | 3661 |
| HIRE |         +4,598 (n=947) |         +4,698 (n=447) |         +4,647 (n=325) | 1719 |
| WATER_MISSED |         +4,928 (n=1465) |         +4,618 (n=889) |         +4,605 (n=1005) | 3359 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,409 (n=808) |         +2,578 (n=239) |         +3,700 (n=307) | 1354 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,048 |      +4,613 |      +4,594 |      +5,192 |      +4,731 |      +4,550 |
| BUY_ANIMAL |      +3,536 |           — |           — |           — |      +6,122 |      +4,233 |
| BUY_SEED |      +4,540 |      +4,749 |      +5,372 |           — |      +5,997 |      +4,669 |
| BUY_LAND |           — |      -2,070 |      +4,778 |      -4,068 |      +6,087 |      +4,215 |
| BUY_PRODUCT |      +4,611 |           — |           — |           — |           — |           — |
| HIRE |      +4,633 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,618 |      +5,700 |      +4,618 |      +4,728 |
| FEED_MISSED |           — |      +4,619 |      +4,238 |           — |           — |      +3,851 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | WATER_MISSED | early | +4,928 | 1465 | 1.05 |
| 2 | BUY_SEED | early | +4,926 | 1419 | 1.04 |
| 3 | SELL | early | +4,796 | 1730 | 1.0 |
| 4 | HIRE | mid | +4,698 | 447 | 0.93 |
| 5 | HIRE | late | +4,647 | 325 | 0.92 |
| 6 | BUY_PRODUCT | early | +4,620 | 1902 | 0.93 |
| 7 | SELL | mid | +4,618 | 889 | 0.93 |
| 8 | SELL | late | +4,618 | 1016 | 0.93 |
| 9 | BUY_PRODUCT | mid | +4,618 | 889 | 0.93 |
| 10 | WATER_MISSED | mid | +4,618 | 889 | 0.93 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +6,656 (n=191)
- **FEED_MISSED** in ('mid', 'low', 'mid', 'high'): +6,532 (n=4)
- **SELL** in ('mid', 'low', 'high', 'low'): +6,382 (n=62)
- **FEED_MISSED** in ('mid', 'low', 'high', 'low'): +6,382 (n=62)
- **SELL** in ('low', 'low', 'mid', 'mid'): +6,326 (n=105)
- **WATER_MISSED** in ('mid', 'low', 'high', 'low'): +6,321 (n=57)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +6,153 (n=92)
- **SELL** in ('mid', 'low', 'mid', 'high'): +6,139 (n=5)
- **BUY_ANIMAL** in ('mid', 'low', 'mid', 'high'): +6,139 (n=5)
- **BUY_SEED** in ('mid', 'low', 'mid', 'high'): +6,139 (n=5)
- **BUY_LAND** in ('mid', 'low', 'mid', 'high'): +6,139 (n=5)
- **BUY_PRODUCT** in ('mid', 'low', 'mid', 'high'): +6,139 (n=5)
- **WATER_MISSED** in ('mid', 'low', 'mid', 'high'): +6,139 (n=5)
- **SELL** in ('low', 'mid', 'high', 'high'): +5,978 (n=43)
- **BUY_PRODUCT** in ('low', 'mid', 'high', 'high'): +5,978 (n=43)

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

_Generated 2026-09-13 06:26. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._