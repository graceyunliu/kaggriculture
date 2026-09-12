# Evolution run 20260911-212926

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.01 h · candidates evaluated this run: 137 · games 30,898 (15,390/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 20 | 40 |
| dead_pattern | 13 | 26 |
| dead_smoke | 6 | 48 |
| alive | 22 | 2816 |
| held_fail | 15 | 5520 |
| held_pass | 61 | 22448 |
| error | 0 | 0 |

Population (all runs, reached dev): 812 · held-out evaluated: 565 · held-out PASS: 504

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | +3,605 | 3.6 | 9-1 | -13,427 | +4,376 | 7.2 | 18-2 |
| chassis + C1 params (seed row) | +0 | 0.0 | not evaluated (no-op) | -16,635 | — | — | —-— |
| C1.py (file) vs O15_SALE_PRIORITY.py | -21,945 | -16.8 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O15_SALE_PRIORITY.py | -25,061 | -10.2 | 0-10 | — | — | — | — |
| O15_SALE_PRIORITY.py own panel (dev / held) | — | — | — | -11,387 / -20,836 | — | — | — |

Measurement mode: `KAGG_FIXED_SHOPS=1` (shop unlocks policy-independent; panel margins comparable at ±$3k/opponent).

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `4dac8845ebc8` | wide | crossover | **+11,121** | 9.1 | 20-0 | -16,794 | +8,469 | melon_floor 0→150, open_melons 10→11, early_hire_days 3→1, feed_spare_poor 0→2, wheat_water_tier 0→1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPENING_MELONS 14→6, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 13 (gap +1,703 -> final +6,758); days 11-18 drivers: missed_water -25, work_turns +53, idle_turns -38, feed_hour -1.35. Hands 12 vs 14, animals 11 vs 11, plants 61 vs 6 |
| `de988febe942` | o15 | paired | **+10,757** | 7.7 | 20-0 | -17,354 | +7,450 | harvest_min 1→3, open_melons 10→11, early_hire_days 3→5, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +3,607 -> final +3,476); days 16-23 drivers: missed_water -33, work_turns +107, sales_rev +2,925, feed_hour -1.16. Hands 11 vs 8, animals 12 vs 11, plants 52 vs |
| `1b7641b11a93` | orch | crossover | **+10,492** | 8.2 | 20-0 | -16,430 | +9,624 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 | wheat_sell_price ?, CROP_SWEEP_LEN -173, STRAW_CUTOFF ?, NEAR_RADIUS +214, OPP_GROWTH ?, ORCH_P_WEEDS -121 | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,400); days 16-23 drivers: missed_water -44, work_turns +122, sales_rev +3,509, idle_turns -44. Hands 13 vs 8, animals 12 vs 11, plants 59 vs  |
| `33d973e44a24` | o15 | paired | **+10,471** | 8.8 | 20-0 | -16,658 | +10,015 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 | min_hands +147, ORCH_P_SLACK -275 | cand pulls ahead of C1 from day 18 (gap +2,562 -> final +3,705); days 16-23 drivers: missed_water -55, work_turns +105, sales_rev +3,264, idle_turns -60. Hands 11 vs 8, animals 12 vs 11, plants 59 vs  |
| `67924b68c4e5` | orch | crossover | **+10,454** | 8.4 | 20-0 | -16,968 | +8,588 | harvest_min 1→3, geese 0→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,927 -> final +5,568); days 16-23 drivers: sales_rev +5,449, work_turns +119, missed_water -20, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `69f9eaac2d61` | orch | ablate:ORCH_P_WEEDS | **+10,383** | 7.5 | 20-0 | -16,425 | +9,745 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,404); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |
| `0b037ebcf3fa` | queue | crossover | **+10,260** | 9.1 | 20-0 | -16,918 | +9,033 | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 19 (gap +1,809 -> final +4,428); days 17-24 drivers: missed_water -44, work_turns +114, idle_turns -35, sales_rev +999. Hands 13 vs 14, animals 11 vs 11, plants 60 vs 5 |
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `f25e784d65ee` | queue | mutate | **+10,227** | 8.3 | 20-0 | -16,406 | +10,406 | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +1,739 -> final +7,620); days 17-24 drivers: missed_water -36, sales_rev +2,327, work_turns +50, idle_turns -37. Hands 12 vs 14, animals 9 vs 11, plants 57 vs 5 |
| `d7eec7135f06` | queue | mutate | **+10,140** | 7.2 | 19-1 | -16,966 | +8,831 | melon_floor 0→100, harvest_min 1→3, geese 0→2, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→94, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,640 -> final +6,963); days 16-23 drivers: sales_rev +5,689, work_turns +140, missed_water -12, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 57 vs  |
| `ad621af0852e` | orch | migrate | **+10,100** | 9.9 | 20-0 | -16,287 | +8,812 | harvest_min 1→3, load_per_hand 20→21, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→93, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +2,751 -> final +9,033); days 17-24 drivers: missed_water -35, work_turns +53, idle_turns -39, sales_rev +1,137. Hands 12 vs 14, animals 9 vs 11, plants 62 vs 5 |
| `2bf642462b16` | queue | archive_crossover:crossover_g000025_20260911-200819_1 | **+10,065** | 8.1 | 20-0 | -16,732 | +8,489 | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +1,553 -> final +4,539); days 14-21 drivers: work_turns +81, idle_turns -50, missed_water -5, feed_hour -1.16. Hands 13 vs 8, animals 11 vs 11, plants 60 vs 57. |
| `3384644b3adb` | orch | ablate:CROP_SWEEP_LEN | **+10,041** | 7.9 | 20-0 | -16,312 | +9,797 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,329); days 16-23 drivers: missed_water -44, work_turns +122, sales_rev +3,509, idle_turns -44. Hands 13 vs 8, animals 12 vs 11, plants 59 vs  |
| `369ac717437c` | queue | mutate | **+10,014** | 8.0 | 20-0 | -16,804 | +9,070 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, CROP_SWEEP_RADIUS -91, STRAW_CUTOFF ?, MELON_PRICE_CUSHION ?, FERT_RADIUS ? | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `dd461fc9be4c` | o15 | crossover | **+9,994** | 7.9 | 20-0 | -17,014 | +9,912 | harvest_min 1→3, min_hands 3→6, early_hire_days 3→6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.7, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→11 |  | cand pulls ahead of C1 from day 19 (gap +1,836 -> final +6,091); days 17-24 drivers: missed_water -49, work_turns +112, sales_rev +3,233, idle_turns -45. Hands 13 vs 14, animals 11 vs 11, plants 60 vs |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `4abd19f6a514` | o15 | mutate | +10,905 | 5.1 | 10-0 | -6,092 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `d40162bbeaa3` | orch | crossover | +10,545 | 6.0 | 10-0 | -6,551 | held_pass | melon_floor 0→150, harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→15 |
| `f25e784d65ee` | queue | mutate | +10,406 | 5.5 | 10-0 | -6,883 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `508ceae58587` | orch | ablate:ORCH_COMMIT | +10,405 | 6.4 | 10-0 | -6,287 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `53b40a96cac7` | queue | archive_crossover:crossover_g000050_20260911-185026_0 | +10,332 | 4.6 | 10-0 | -8,543 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `63bd49376d83` | queue | mutate | +10,320 | 4.5 | 10-0 | -8,617 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `6c7e6434ea83` | o15 | ablate:ORCH_P_SLACK | +10,290 | 6.4 | 10-0 | -7,259 | held_pass | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `8b03f1857f52` | queue | migrate | +10,263 | 4.9 | 10-0 | -8,584 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `7c3c00c7830d` | queue | archive_crossover:crossover_g000075_20260911-205656_0 | +10,254 | 5.5 | 10-0 | -6,593 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `64e5a7b2f56a` | wide | crossover | +10,209 | 4.9 | 10-0 | -8,314 | held_fail | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `b55411f71d8d` | orch | crossover | +10,109 | 7.3 | 10-0 | -6,781 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, max_animals 17→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | +10,107 | 5.9 | 10-0 | -6,749 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a141ecf7c8cc` | wide | crossover | +10,071 | 5.8 | 10-0 | -6,073 | held_pass | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |
| `1e700a8702a2` | queue | archive_crossover:crossover_g000025_20260911-221232_0 | +10,061 | 4.7 | 10-0 | -8,340 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5 |
| `933e21488445` | orch | paired | +10,055 | 7.6 | 10-0 | -6,750 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,905 (`4abd19f6a514`), n=160
- orch: best +10,545 (`d40162bbeaa3`), n=212
- queue: best +10,406 (`f25e784d65ee`), n=236
- wide: best +10,209 (`64e5a7b2f56a`), n=182

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,326 | 35 | 92 | 44 | 786 | 12.69 | 35: +9,592 (n=3), 102: +8,944 (n=2), 132: +8,639 (n=2), 81: +5,236 (n=50), 110: +5,124 (n=52), 111: +5,057 (n=26), 92: +4,653 (n=598), 99: +4,310 (n=13), 119: +3,803 (n=10), 63: +3,619 (n=3), 82: +3,549 (n=5), 54: +2,856 (n=5), 150: +2,640 (n=4), 96: +1,931 (n=3), 91: +1,573 (n=2), 121: -1,255 (n=2), 0: -1,278 (n=2), 125: -2,734 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,304 | 0.6 | 0.55 | 12 | 812 | 8.31 | 0.6: +5,931 (n=110), 0.55: +4,777 (n=630), 0.7: +3,630 (n=5), 0.5: +3,197 (n=8), 0.65: +3,011 (n=9), 0.75: +2,689 (n=8), 0.4: +2,297 (n=7), 0.8: +2,125 (n=14), 0.45: +296 (n=4), 0.35: +40 (n=3), 0.9: -3,198 (n=4), 0.3: -5,373 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,583 | 2 | 3 | 3 | 812 | 1.29 | 2: +5,751 (n=621), 3: +949 (n=188), 4: -4,832 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,075 | 1.25 | 0.5 | 12 | 809 | 6.74 | 1.25: +6,750 (n=6), 0.25: +6,728 (n=12), 1.75: +5,821 (n=6), 0.5: +4,711 (n=696), 0.0: +3,724 (n=68), 0.75: +3,465 (n=6), 1.0: +3,319 (n=8), 3.0: +2,555 (n=5), 2.75: -3,326 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,059 | 18 | 20 | 14 | 809 | 7.1 | 18: +5,614 (n=142), 17: +5,511 (n=8), 19: +5,073 (n=15), 20: +4,528 (n=596), 21: +3,800 (n=26), 16: +3,297 (n=5), 22: +2,964 (n=6), 24: +1,532 (n=2), 13: +284 (n=3), 14: -765 (n=4), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +9,987 | 108 | 100 | 43 | 791 | 12.29 | 108: +8,353 (n=2), 93: +8,014 (n=2), 135: +6,542 (n=3), 124: +6,478 (n=5), 110: +6,469 (n=89), 132: +6,202 (n=15), 99: +6,125 (n=2), 117: +5,882 (n=2), 109: +5,825 (n=39), 86: +5,433 (n=22), 94: +5,095 (n=11), 87: +5,023 (n=5), 67: +4,927 (n=4), 104: +4,853 (n=3), 150: +4,612 (n=83), 105: +4,150 (n=7), 100: +4,126 (n=478), 50: +3,314 (n=8), 126: +3,135 (n=3), 68: +2,481 (n=2), 62: +519 (n=4), 82: -1,635 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,229 | 4 | 0 | 18 | 806 | 10.08 | 4: +8,585 (n=2), 2: +6,484 (n=4), 0: +4,900 (n=744), 1: +3,030 (n=7), 6: +2,980 (n=3), 7: +1,940 (n=4), 11: +1,588 (n=7), 10: +1,472 (n=7), 5: +745 (n=3), 14: -309 (n=5), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +8,695 | 18 | 17 | 10 | 809 | 5.33 | 18: +4,763 (n=22), 17: +4,761 (n=732), 15: +4,254 (n=4), 16: +3,302 (n=33), 19: +1,313 (n=11), 20: +1,115 (n=5), 10: -3,932 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +8,049 | 0.75 | 1.0 | 14 | 810 | 5.99 | 0.75: +6,347 (n=3), 2.0: +5,862 (n=13), 0.5: +5,356 (n=18), 1.5: +5,227 (n=472), 1.25: +4,951 (n=81), 0.25: +4,872 (n=4), 1.75: +4,448 (n=16), 1.0: +2,980 (n=185), 2.25: +2,523 (n=3), 2.5: +1,968 (n=5), 0.0: +1,114 (n=8), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,472 | 9 | 14 | 8 | 811 | 5.02 | 9: +6,057 (n=30), 10: +5,762 (n=17), 13: +4,690 (n=52), 14: +4,589 (n=697), 12: +4,572 (n=6), 8: -271 (n=4), 11: -1,414 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,469 | frontier | frontier | 2 | 812 | 0.84 | frontier: +5,188 (n=748), v312: -2,280 (n=64) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,448 | 26 | 30 | 17 | 808 | 8.73 | 26: +6,676 (n=4), 28: +6,573 (n=45), 25: +5,460 (n=70), 27: +5,110 (n=36), 30: +4,472 (n=605), 34: +4,385 (n=18), 37: +3,940 (n=8), 35: +2,046 (n=6), 29: +927 (n=3), 32: +411 (n=2), 45: +241 (n=2), 31: -278 (n=7), 33: -772 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,803 | 9 | 10 | 11 | 810 | 6.12 | 9: +5,740 (n=89), 8: +5,505 (n=11), 10: +4,700 (n=641), 12: +4,080 (n=7), 11: +2,875 (n=37), 6: +2,273 (n=4), 7: +943 (n=11), 13: -124 (n=7), 4: -1,063 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,762 | 0.3 | 0.0 | 9 | 810 | 5.57 | 0.3: +5,427 (n=6), 0.0: +4,750 (n=760), 0.1: +3,190 (n=24), 0.4: +3,044 (n=5), 0.2: +1,031 (n=9), 0.6: -912 (n=2), 0.7: -1,335 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +6,638 | 1.5 | 1.25 | 5 | 812 | 3.55 | 1.5: +5,360 (n=33), 1.25: +4,670 (n=739), 0.75: +3,571 (n=2), 1.0: +2,852 (n=36), 0.5: -1,278 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| min_hands | +6,488 | 6 | 3 | 4 | 812 | 2.39 | 6: +7,355 (n=5), 4: +5,329 (n=113), 3: +4,493 (n=688), 5: +866 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_SLACK | +6,323 | 4.5 | 6.0 | 15 | 812 | 9.53 | 4.5: +6,875 (n=12), 4.0: +6,744 (n=3), 6.5: +6,266 (n=21), 9.5: +6,242 (n=12), 5.5: +6,072 (n=26), 3.5: +5,639 (n=4), 5.0: +5,083 (n=21), 7.0: +4,955 (n=88), 7.5: +4,606 (n=20), 6.0: +4,397 (n=570), 8.0: +3,850 (n=21), 2.0: +2,204 (n=4), 10.0: +1,982 (n=4), 9.0: +1,635 (n=3), 8.5: +551 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,278 | 42 | 38 | 26 | 803 | 5.2 | 42: +6,845 (n=2), 24: +6,542 (n=3), 50: +6,261 (n=41), 32: +5,911 (n=8), 33: +5,900 (n=2), 35: +5,702 (n=293), 41: +5,678 (n=45), 27: +5,621 (n=2), 20: +5,106 (n=2), 44: +5,076 (n=3), 26: +4,952 (n=26), 43: +4,778 (n=3), 31: +4,610 (n=15), 28: +4,378 (n=7), 38: +3,905 (n=284), 39: +2,789 (n=3), 30: +567 (n=64) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +6,268 | 13 | 14 | 14 | 811 | 6.92 | 13: +6,045 (n=19), 11: +5,733 (n=38), 15: +5,238 (n=494), 10: +5,021 (n=12), 19: +4,724 (n=8), 16: +3,882 (n=8), 18: +3,794 (n=4), 12: +3,300 (n=20), 14: +3,252 (n=183), 22: +2,182 (n=2), 17: +1,590 (n=3), 8: +212 (n=17), 20: -224 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +6,264 | 6 | 7 | 8 | 811 | 5.13 | 6: +5,094 (n=25), 7: +4,780 (n=710), 8: +3,984 (n=31), 5: +3,533 (n=14), 10: +2,716 (n=12), 9: +1,413 (n=13), 4: -1,169 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +10,905 (n=135)
- (9, 3, 4): +10,545 (n=158)
- (9, 3, 5): +10,406 (n=101)
- (11, 3, 6): +10,254 (n=89)
- (11, 3, 5): +10,071 (n=127)
- (12, 3, 6): +10,015 (n=54)
- (10, 3, 4): +9,940 (n=26)
- (10, 3, 6): +9,935 (n=12)
- (9, 3, 6): +9,706 (n=3)
- (12, 3, 5): +9,598 (n=42)
- (11, 3, 4): +8,559 (n=9)
- (13, 3, 5): +7,918 (n=3)
- (14, 3, 6): +7,609 (n=10)
- (15, 3, 6): +6,377 (n=8)
- (8, 3, 4): +6,048 (n=6)

_Generated 2026-09-11 23:29. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 189 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=189); harvest_min=1–3 (n=189); wheat_tiles=0–7 (n=189); wheat_stock=0–40 (n=189); min_hands=3–6 (n=189); load_per_hand=12–26 (n=189); geese=0–2 (n=189); open_melons=6–14 (n=189)
- **Evidence:** 189 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**812 candidates** with action_table data, **106874 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,656 (n=11210) |         +4,600 (n=5684) |         +4,600 (n=6496) | 23390 |
| BUY_ANIMAL |         +4,095 (n=4563) |         +5,005 (n=985) |              — (n=0) | 5548 |
| BUY_SEED |         +4,643 (n=8327) |         +4,694 (n=3087) |         +4,233 (n=1137) | 12551 |
| BUY_LAND |         +4,565 (n=2866) |         +5,127 (n=784) |              — (n=0) | 3650 |
| BUY_PRODUCT |         +4,600 (n=12174) |         +4,600 (n=5684) |         +4,599 (n=5683) | 23541 |
| HIRE |         +4,471 (n=4897) |         +4,431 (n=2809) |         +4,782 (n=2117) | 9823 |
| WATER_MISSED |         +4,600 (n=9086) |         +4,600 (n=5684) |         +4,600 (n=6493) | 21263 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,314 (n=4218) |         +4,365 (n=1110) |         +4,136 (n=1780) | 7108 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +4,740 |      +4,600 |      +4,642 |      +4,629 |      +4,544 |      +4,594 |
| BUY_ANIMAL |      +4,006 |           — |      +1,809 |      +4,940 |      +4,719 |      +4,217 |
| BUY_SEED |      +4,046 |      +5,394 |      -2,939 |      -3,329 |      +2,676 |      +4,698 |
| BUY_LAND |      -1,974 |      -3,426 |      +4,663 |        -940 |      +5,365 |      +4,581 |
| BUY_PRODUCT |      +4,600 |           — |           — |           — |           — |           — |
| HIRE |      +4,527 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,600 |      +2,323 |      +4,600 |      +4,631 |
| FEED_MISSED |           — |      +4,605 |      +2,926 |           — |      +1,809 |      +4,257 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +5,127 | 784 | 1.25 |
| 2 | BUY_ANIMAL | mid | +5,005 | 985 | 1.21 |
| 3 | HIRE | late | +4,782 | 2117 | 1.13 |
| 4 | BUY_SEED | mid | +4,694 | 3087 | 1.08 |
| 5 | SELL | early | +4,656 | 11210 | 1.09 |
| 6 | BUY_SEED | early | +4,643 | 8327 | 1.09 |
| 7 | SELL | mid | +4,600 | 5684 | 1.07 |
| 8 | SELL | late | +4,600 | 6496 | 1.07 |
| 9 | BUY_PRODUCT | early | +4,600 | 12174 | 1.07 |
| 10 | BUY_PRODUCT | mid | +4,600 | 5684 | 1.07 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +6,936 (n=330)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +6,936 (n=330)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,544 (n=60)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,260 (n=465)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,236 (n=467)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,218 (n=479)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,156 (n=483)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,127 (n=485)
- **SELL** in ('low', 'low', 'high', 'mid'): -6,032 (n=5)
- **WATER_MISSED** in ('low', 'low', 'high', 'mid'): -6,032 (n=5)
- **FEED_MISSED** in ('low', 'low', 'high', 'mid'): -6,032 (n=5)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +5,869 (n=73)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +5,869 (n=73)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +5,481 (n=633)
- **SELL** in ('low', 'mid', 'low', 'mid'): +5,421 (n=9)

_Generated 2026-09-11 23:29. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._