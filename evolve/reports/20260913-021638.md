# Evolution run 20260913-021638

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_pensukesan_107199477.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.03 h · candidates evaluated this run: 94 · games 29,126 (14,355/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 27 | 54 |
| dead_pattern | 4 | 8 |
| dead_smoke | 1 | 8 |
| alive | 15 | 2520 |
| held_fail | 1 | 408 |
| held_exploit | 0 | 0 |
| held_pass | 46 | 26128 |
| error | 0 | 0 |

Population (all runs, reached dev): 62 · held-out evaluated: 47 · held-out PASS: 46

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
| `3c3e3fde03a7` | best | ablate:HIRE_MAX_MARGINAL | **+12,550** | 8.4 | 19-1 | -13,214 | +10,247 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -1,512 -> final -1,385); days 23-29 drivers: missed_water +11, sales_rev -1,592, water_hour +0.87. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `daf68d6d17e5` | o15 | mutate | **+11,342** | 10.1 | 20-0 | -14,195 | +9,498 | open_melons 10→11, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→128, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand pulls ahead of C1 from day 24 (gap +2,361 -> final +1,931); days 22-29 drivers: sales_rev +1,155, idle_turns -15, work_turns +12, feed_hour -0.11. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `f2bf74946332` | best | block_pair | **+10,419** | 8.1 | 20-0 | -12,033 | +7,617 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 25 (gap -2,773 -> final -3,664); days 23-29 drivers: sales_rev -5,508, work_turns -73, missed_water +10, weeds_new +1. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `19ab6fc743ad` | wide | mutate | **+10,135** | 7.9 | 20-0 | -12,223 | +7,508 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -2,738 -> final -2,738); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `55aee088b1f5` | best | crossover | **+10,072** | 7.3 | 20-0 | -12,135 | +7,418 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, CROP_SWEEP_LEN 6→8, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | opening +10,071, CROP_SWEEP_LEN ? | cand falls behind C1 from day 29 (gap -2,738 -> final -2,738); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `6abb364c586c` | o15 | ablate:wheat_stock | **+10,071** | 7.3 | 20-0 | -12,138 | +7,456 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand falls behind C1 from day 29 (gap -2,739 -> final -2,739); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `a8cd98e17af1` | o15 | ablate:wheat_sell_price | **+9,812** | 7.1 | 19-1 | -12,601 | +9,753 | open_melons 10→9, early_hire_days 3→5, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |  | cand falls behind C1 from day 29 (gap -2,187 -> final -2,187); days 27-29 drivers: water_hour +2.25, sales_rev -1,123, work_turns -13, reversals +4. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `9c750e2fa0d1` | best | crossover | **+9,778** | 7.3 | 19-1 | -12,297 | +9,356 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→21, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 26 (gap -1,516 -> final -1,467); days 24-29 drivers: sales_rev -2,975, idle_turns +22, water_hour +0.92. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `f5e7b504ecb2` | queue | crossover | **+9,664** | 6.3 | 19-1 | -12,615 | +7,357 | wheat_tiles 0→2, wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→20, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→3, MELON_PRICE_CUSHION 100→116, OPP_GROWTH 1.4→1.3, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 26 (gap -1,708 -> final -2,694); days 24-29 drivers: sales_rev -3,606, missed_water +3, work_turns -3, travel_per_task +0.06. Hands 5 vs 5, animals 11 vs 11, plants 5 vs  |
| `859e448b3f02` | queue | archive_crossover:crossover_g000025_20260913-031123_1 | **+9,647** | 6.7 | 19-1 | -12,221 | +7,667 | wheat_stock 0→1, open_melons 10→9, wheat_sell_price 30→29, MELON_MORNING 1→0 |  | cand falls behind C1 from day 29 (gap -2,739 -> final -2,739); days 27-29 drivers: sales_rev -2,478, work_turns -44, feed_hour +1.0, water_hour +0.95. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `491359a7a7e5` | o15 | crossover | **+9,554** | 6.5 | 18-2 | -12,601 | +10,107 | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 | wheat_stock +2,651, wheat_cap ?, wheat_sell_price +354, OPP_GROWTH ?, FERT_RADIUS ?, SPREAD_CAP ?, MELON_MORNING_MIN_YIELD ? | cand falls behind C1 from day 29 (gap -2,188 -> final -2,188); days 27-29 drivers: water_hour +2.25, sales_rev -1,123, work_turns -13, reversals +4. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `58c7a5c6dad1` | best | ablate:wheat_water_tier | **+9,537** | 6.0 | 18-2 | -12,404 | +7,759 | wheat_tiles 0→2, wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→18, CROP_SWEEP_LEN 6→3, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.0, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -2,557 -> final -2,557); days 27-29 drivers: sales_rev -2,305, missed_water +6, work_turns -24, water_hour +1.3. Hands 5 vs 5, animals 11 vs 11, plants 4 vs 5. |
| `4dc0ec6eb5c2` | best | ablate:wheat_tiles | **+9,502** | 8.4 | 20-0 | -12,361 | +9,062 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→18, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→3, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.0, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 29 (gap -3,253 -> final -3,253); days 27-29 drivers: sales_rev -2,912, work_turns -47, water_hour +1.5, idle_turns +4. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |
| `5655187e65b4` | best | paired | **+9,475** | 5.4 | 18-2 | -15,530 | +5,590 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, HIRE_MAX_MARGINAL 144→55, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 | ROUTE_LEN +1,319, HIRE_MAX_MARGINAL -4,657 | cand falls behind C1 from day 27 (gap -1,778 -> final -1,426); days 25-29 drivers: weeds_new +4, missed_water +7, water_hour +1.5, sales_rev -720. Hands 5 vs 5, animals 10 vs 11, plants 4 vs 5. |
| `a1f1a81e96de` | queue | archive_crossover:crossover_g000050_20260913-034732_0 | **+9,405** | 7.7 | 20-0 | -12,172 | +8,112 | wheat_tiles 0→1, wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, CROP_SWEEP_LEN 6→3, HERD_LAST_DAY 17→20, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |  | cand falls behind C1 from day 24 (gap -2,113 -> final -3,798); days 22-29 drivers: sales_rev -4,127, work_turns -36, weeds_new +1, water_hour +0.49. Hands 4 vs 5, animals 11 vs 11, plants 1 vs 5. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `3c3e3fde03a7` | best | ablate:HIRE_MAX_MARGINAL | +10,247 | 7.4 | 26-4 | -9,464 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→21, ROUTE_LEN 3→2, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `491359a7a7e5` | o15 | crossover | +10,107 | 9.5 | 28-2 | -6,968 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `a8cd98e17af1` | o15 | ablate:wheat_sell_price | +9,753 | 8.8 | 28-2 | -6,913 | held_pass | open_melons 10→9, early_hire_days 3→5, CROP_SWEEP_LEN 6→8, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `daf68d6d17e5` | o15 | mutate | +9,498 | 8.2 | 27-3 | -9,087 | held_pass | open_melons 10→11, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→128, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `9c750e2fa0d1` | best | crossover | +9,356 | 8.4 | 29-1 | -7,714 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→21, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `4dc0ec6eb5c2` | best | ablate:wheat_tiles | +9,062 | 8.1 | 29-1 | -7,189 | held_pass | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→18, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→3, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.0, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `e600fb77a4c5` | o15 | mutate | +8,841 | 7.7 | 27-3 | -7,075 | held_pass | wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→5, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→10, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `4d8c90d8ff71` | o15 | mutate | +8,721 | 8.5 | 28-2 | -7,362 | held_pass | wheat_stock 0→2, load_per_hand 20→18, open_melons 10→9, max_animals 17→16, MAX_HANDS 14→15, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→112, OPP_GROWTH 1.4→1.2 |
| `ea773a3c29d6` | queue | mutate | +8,289 | 6.6 | 27-3 | -8,170 | held_pass | wheat_tiles 0→2, wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→18, wheat_water_tier 0→1, wheat_hold_days 0→1, CROP_SWEEP_LEN 6→3, MELON_PRICE_CUSHION 100→116, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `05cab2216927` | o15 | mutate | +8,278 | 7.3 | 28-2 | -6,451 | held_pass | open_melons 10→9, max_animals 17→16, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→112 |
| `ace4c3231e54` | queue | mutate | +8,272 | 7.2 | 27-3 | -8,950 | held_pass | wheat_tiles 0→2, wheat_stock 0→1, load_per_hand 20→19, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→18, wheat_water_tier 0→1, wheat_hold_days 0→1, CROP_SWEEP_LEN 6→3, MELON_PRICE_CUSHION 100→116, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `12e7460e994e` | o15 | crossover | +8,179 | 6.1 | 25-5 | -8,700 | held_pass | open_melons 10→9, early_hire_days 3→5, wheat_per_animal 0.0→0.2, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→8, SPREAD_W 1.25→1.0, SPREAD_CAP 3→7, MELON_MORNING 1→0 |
| `a1f1a81e96de` | queue | archive_crossover:crossover_g000050_20260913-034732_0 | +8,112 | 6.5 | 27-3 | -7,472 | held_pass | wheat_tiles 0→1, wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, CROP_SWEEP_LEN 6→3, HERD_LAST_DAY 17→20, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `a56c9adce164` | best | paired | +7,940 | 7.3 | 28-2 | -8,367 | held_pass | wheat_tiles 0→2, wheat_stock 0→1, open_melons 10→9, early_hire_days 3→5, wheat_cap 22→18, CROP_SWEEP_LEN 6→5, MELON_PRICE_CUSHION 100→116, HERD_LAST_DAY 17→20, OPP_GROWTH 1.4→1.1, FERT_RADIUS 3→2, SPREAD_CAP 3→5, ORCH_SLACK_HOUR 14→15, MELON_MORNING 1→0, MELON_MORNING_MIN_YIELD 6→5 |
| `1aafaab52393` | o15 | paired | +7,884 | 6.3 | 25-5 | -7,098 | held_pass | open_melons 10→9, early_hire_days 3→5, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→6, SPREAD_CAP 3→7 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +10,247 (`3c3e3fde03a7`), n=22
- o15: best +10,107 (`491359a7a7e5`), n=17
- queue: best +8,289 (`ea773a3c29d6`), n=12
- wide: best +7,508 (`19ab6fc743ad`), n=11

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| FERT_RADIUS | +12,021 | 3 | 3 | 3 | 62 | 0.98 | 3: +7,442 (n=18), 2: +4,037 (n=41), 1: -4,579 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +11,126 | 3 | 3 | 4 | 62 | 2.23 | 3: +7,771 (n=5), 8: +5,926 (n=5), 5: +4,479 (n=50), 7: -3,356 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,682 | 16 | 17 | 4 | 62 | 2.29 | 16: +8,089 (n=3), 20: +5,292 (n=2), 17: +5,224 (n=51), 18: -2,593 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +10,682 | 112 | 100 | 7 | 59 | 1.17 | 112: +8,089 (n=3), 116: +7,240 (n=18), 100: +4,275 (n=32), 107: -2,593 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +10,665 | frontier | frontier | 2 | 62 | 0.68 | frontier: +6,329 (n=52), v312: -4,336 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +9,632 | 1.2 | 1.4 | 6 | 61 | 1.79 | 1.2: +8,592 (n=3), 1.0: +8,015 (n=4), 1.4: +7,234 (n=16), 1.3: +3,188 (n=34), 1.7: -1,040 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +8,111 | 8 | 8 | 3 | 61 | 0.8 | 8: +5,517 (n=55), 12: -2,593 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +7,576 | 0 | 0 | 6 | 59 | 0.98 | 0: +5,080 (n=18), 1: +4,698 (n=39), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +7,499 | 20 | 20 | 8 | 57 | 1.63 | 20: +5,463 (n=50), 17: +5,292 (n=2), 15: -2,036 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +7,383 | 2 | 3 | 4 | 61 | 1.8 | 2: +7,918 (n=2), 3: +4,819 (n=57), 4: +535 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +6,446 | 1.0 | 1.25 | 3 | 62 | 1.66 | 1.0: +7,414 (n=3), 1.25: +4,720 (n=55), 1.5: +968 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +6,393 | 18 | 22 | 5 | 62 | 1.34 | 18: +7,481 (n=11), 20: +7,474 (n=3), 22: +7,427 (n=17), 21: +1,813 (n=29), 15: +1,088 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +6,332 | 9 | 14 | 5 | 60 | 1.7 | 9: +5,292 (n=2), 14: +5,095 (n=54), 10: -1,040 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +5,069 | 0.2 | 0.0 | 4 | 61 | 1.8 | 0.2: +6,373 (n=2), 0.0: +4,642 (n=57), 0.1: +1,304 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +4,985 | 3 | 6 | 8 | 59 | 1.37 | 3: +7,486 (n=13), 7: +7,274 (n=2), 8: +5,612 (n=14), 5: +2,564 (n=2), 6: +2,500 (n=28) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_hold_days | +4,836 | 0 | 0 | 2 | 62 | 0.61 | 0: +5,545 (n=50), 1: +708 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +4,432 | 15 | 14 | 2 | 36 | 0.17 | 15: +6,800 (n=21), 14: +2,368 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_CAP | +4,131 | 3 | 3 | 3 | 62 | 0.84 | 3: +7,771 (n=5), 5: +4,677 (n=38), 7: +3,640 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_MIN_YIELD | +3,908 | 6 | 6 | 2 | 62 | 0.35 | 6: +7,256 (n=20), 5: +3,348 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +3,710 | 2 | 0 | 3 | 62 | 1.18 | 2: +7,372 (n=14), 1: +5,919 (n=3), 0: +3,662 (n=45) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +10,247 (n=4)
- (11, 3, 4): +10,107 (n=19)
- (11, 3, 5): +8,841 (n=24)
- (11, 3, 6): +8,721 (n=4)
- (9, 3, 4): +7,556 (n=3)
- (10, 3, 4): +5,871 (n=3)
- (10, 3, 6): +4,566 (n=1)
- (9, 3, 3): +804 (n=1)
- (14, 3, 6): -5,381 (n=1)
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

_Generated 2026-09-13 04:19. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 6 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0; harvest_min=1; wheat_tiles=0; wheat_stock=0–1 (n=6); min_hands=3; load_per_hand=14–21 (n=6); geese=0; open_melons=4–10 (n=6)
- **Evidence:** 6 candidates, multiple seeds. Confidence: moderate

## Action timing patterns (AGE-359: observational — correlations, not causes)

**62 candidates** with action_table data, **8532 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,821 (n=845) |         +4,609 (n=434) |         +4,609 (n=496) | 1775 |
| BUY_ANIMAL |         +4,414 (n=432) |         +3,693 (n=85) |              — (n=0) | 517 |
| BUY_SEED |         +5,011 (n=687) |         +4,001 (n=232) |         +4,533 (n=104) | 1023 |
| BUY_LAND |         +4,698 (n=220) |         +3,578 (n=37) |              — (n=0) | 257 |
| BUY_PRODUCT |         +4,609 (n=929) |         +4,609 (n=434) |         +4,564 (n=427) | 1790 |
| HIRE |         +4,627 (n=467) |         +4,513 (n=225) |         +4,596 (n=156) | 848 |
| WATER_MISSED |         +5,000 (n=711) |         +4,609 (n=434) |         +4,586 (n=488) | 1633 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,387 (n=401) |         +1,824 (n=129) |         +3,444 (n=159) | 689 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,124 |      +4,598 |      +4,603 |      +5,302 |      +4,747 |      +4,524 |
| BUY_ANIMAL |      +3,425 |           — |           — |           — |      +6,329 |      +4,195 |
| BUY_SEED |      +4,530 |      +4,818 |      +5,292 |           — |      +6,658 |      +4,638 |
| BUY_LAND |           — |           — |      +4,940 |      -3,364 |      +6,463 |      +4,053 |
| BUY_PRODUCT |      +4,598 |           — |           — |           — |           — |           — |
| HIRE |      +4,591 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,609 |      +6,275 |      +4,609 |      +4,736 |
| FEED_MISSED |           — |      +4,609 |      +4,492 |           — |           — |      +3,590 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_SEED | early | +5,011 | 687 | 1.07 |
| 2 | WATER_MISSED | early | +5,000 | 711 | 1.09 |
| 3 | SELL | early | +4,821 | 845 | 1.01 |
| 4 | BUY_LAND | early | +4,698 | 220 | 0.97 |
| 5 | HIRE | early | +4,627 | 467 | 0.94 |
| 6 | SELL | mid | +4,609 | 434 | 0.94 |
| 7 | SELL | late | +4,609 | 496 | 0.94 |
| 8 | BUY_PRODUCT | early | +4,609 | 929 | 0.94 |
| 9 | BUY_PRODUCT | mid | +4,609 | 434 | 0.94 |
| 10 | WATER_MISSED | mid | +4,609 | 434 | 0.94 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +6,904 (n=92)
- **SELL** in ('low', 'low', 'mid', 'mid'): +6,523 (n=51)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +6,520 (n=46)
- **SELL** in ('mid', 'low', 'high', 'low'): +6,506 (n=32)
- **FEED_MISSED** in ('mid', 'low', 'high', 'low'): +6,506 (n=32)
- **WATER_MISSED** in ('mid', 'low', 'high', 'low'): +6,320 (n=29)
- **BUY_SEED** in ('mid', 'high', 'mid', 'high'): +6,196 (n=13)
- **WATER_MISSED** in ('low', 'mid', 'mid', 'high'): +6,078 (n=91)
- **FEED_MISSED** in ('mid', 'mid', 'mid', 'high'): +5,946 (n=49)
- **BUY_SEED** in ('low', 'low', 'mid', 'high'): +5,861 (n=64)
- **BUY_SEED** in ('low', 'mid', 'mid', 'high'): +5,839 (n=43)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'high'): +5,793 (n=102)
- **WATER_MISSED** in ('low', 'low', 'low', 'high'): +5,728 (n=98)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +5,672 (n=75)
- **HIRE** in ('mid', 'mid', 'mid', 'high'): +5,551 (n=51)

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

_Generated 2026-09-13 04:19. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._