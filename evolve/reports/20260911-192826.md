# Evolution run 20260911-192826

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.00 h · candidates evaluated this run: 130 · games 30,662 (15,327/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 18 | 36 |
| dead_pattern | 5 | 10 |
| dead_smoke | 5 | 40 |
| alive | 29 | 3712 |
| held_fail | 7 | 2576 |
| held_pass | 66 | 24288 |
| error | 0 | 0 |

Population (all runs, reached dev): 714 · held-out evaluated: 489 · held-out PASS: 443

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
| `33d973e44a24` | o15 | paired | **+10,471** | 8.8 | 20-0 | -16,658 | +10,015 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 | min_hands +147, ORCH_P_SLACK -275 | cand pulls ahead of C1 from day 18 (gap +2,562 -> final +3,705); days 16-23 drivers: missed_water -55, work_turns +105, sales_rev +3,264, idle_turns -60. Hands 11 vs 8, animals 12 vs 11, plants 59 vs  |
| `67924b68c4e5` | orch | crossover | **+10,454** | 8.4 | 20-0 | -16,968 | +8,588 | harvest_min 1→3, geese 0→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,927 -> final +5,568); days 16-23 drivers: sales_rev +5,449, work_turns +119, missed_water -20, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `0b037ebcf3fa` | queue | crossover | **+10,260** | 9.1 | 20-0 | -16,918 | +9,033 | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 19 (gap +1,809 -> final +4,428); days 17-24 drivers: missed_water -44, work_turns +114, idle_turns -35, sales_rev +999. Hands 13 vs 14, animals 11 vs 11, plants 60 vs 5 |
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `d7eec7135f06` | queue | mutate | **+10,140** | 7.2 | 19-1 | -16,966 | +8,831 | melon_floor 0→100, harvest_min 1→3, geese 0→2, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→94, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,640 -> final +6,963); days 16-23 drivers: sales_rev +5,689, work_turns +140, missed_water -12, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 57 vs  |
| `ad621af0852e` | orch | migrate | **+10,100** | 9.9 | 20-0 | -16,287 | +8,812 | harvest_min 1→3, load_per_hand 20→21, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→93, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +2,751 -> final +9,033); days 17-24 drivers: missed_water -35, work_turns +53, idle_turns -39, sales_rev +1,137. Hands 12 vs 14, animals 9 vs 11, plants 62 vs 5 |
| `2bf642462b16` | queue | archive_crossover:crossover_g000025_20260911-200819_1 | **+10,065** | 8.1 | 20-0 | -16,732 | +8,489 | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +1,553 -> final +4,539); days 14-21 drivers: work_turns +81, idle_turns -50, missed_water -5, feed_hour -1.16. Hands 13 vs 8, animals 11 vs 11, plants 60 vs 57. |
| `369ac717437c` | queue | mutate | **+10,014** | 8.0 | 20-0 | -16,804 | +9,070 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, CROP_SWEEP_RADIUS -91, STRAW_CUTOFF ?, MELON_PRICE_CUSHION ?, FERT_RADIUS ? | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `b37c45315f0b` | o15 | ablate:min_hands | **+9,931** | 9.2 | 20-0 | -16,904 | +9,867 | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,771 -> final +3,587); days 16-23 drivers: missed_water -38, work_turns +93, sales_rev +1,469, idle_turns -34. Hands 13 vs 8, animals 10 vs 11, plants 59 vs 5 |
| `bd87d13da95c` | wide | mutate | **+9,914** | 7.5 | 20-0 | -16,245 | +9,149 | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→3.0, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |  | cand pulls ahead of C1 from day 16 (gap +1,649 -> final +3,142); days 14-21 drivers: work_turns +75, missed_water -11, sales_rev +1,658, feed_hour -1.5. Hands 12 vs 8, animals 10 vs 11, plants 60 vs 5 |
| `fb4e3411021e` | queue | ablate:CROP_SWEEP_RADIUS | **+9,894** | 8.1 | 20-0 | -16,815 | +9,160 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `38c6d83e6927` | o15 | paired | **+9,891** | 8.4 | 20-0 | -17,834 | +9,432 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→18, early_hire_days 3→1, wheat_cap 22→25, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→2.0, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +1,723 -> final +8,969); days 14-21 drivers: sales_rev +5,040, missed_water -20, work_turns +89, feed_hour -1.51. Hands 11 vs 8, animals 9 vs 11, plants 65 vs 5 |
| `6c7e6434ea83` | o15 | ablate:ORCH_P_SLACK | **+9,886** | 7.4 | 20-0 | -16,564 | +10,290 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,432 -> final +5,068); days 16-23 drivers: missed_water -41, sales_rev +2,659, work_turns +55, idle_turns -21. Hands 11 vs 8, animals 10 vs 11, plants 61 vs 5 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `508ceae58587` | orch | ablate:ORCH_COMMIT | +10,405 | 6.4 | 10-0 | -6,287 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `53b40a96cac7` | queue | archive_crossover:crossover_g000050_20260911-185026_0 | +10,332 | 4.6 | 10-0 | -8,543 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `63bd49376d83` | queue | mutate | +10,320 | 4.5 | 10-0 | -8,617 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `6c7e6434ea83` | o15 | ablate:ORCH_P_SLACK | +10,290 | 6.4 | 10-0 | -7,259 | held_pass | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `7c3c00c7830d` | queue | archive_crossover:crossover_g000075_20260911-205656_0 | +10,254 | 5.5 | 10-0 | -6,593 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `64e5a7b2f56a` | wide | crossover | +10,209 | 4.9 | 10-0 | -8,314 | held_fail | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `b55411f71d8d` | orch | crossover | +10,109 | 7.3 | 10-0 | -6,781 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, max_animals 17→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | +10,107 | 5.9 | 10-0 | -6,749 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a141ecf7c8cc` | wide | crossover | +10,071 | 5.8 | 10-0 | -6,073 | held_pass | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |
| `933e21488445` | orch | paired | +10,055 | 7.6 | 10-0 | -6,750 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `33d973e44a24` | o15 | paired | +10,015 | 5.7 | 10-0 | -7,183 | held_pass | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `5e7410992135` | queue | crossover | +9,970 | 4.7 | 10-0 | -7,264 | held_pass | harvest_min 1→2, wheat_per_animal 0.0→0.1, wheat_cap 22→21, setup_capital_share 0.25→0.1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→4.5, ORCH_SLACK_HOUR 14→15 |
| `ae4ad3cda4bf` | orch | mutate | +9,960 | 5.4 | 10-0 | -7,193 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.2, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `cbeff72fd1ca` | queue | ablate:ORCH_SLACK_HOUR | +9,946 | 6.0 | 10-0 | -7,031 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `df547f34fca3` | o15 | paired | +9,940 | 6.3 | 10-0 | -6,598 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,290 (`6c7e6434ea83`), n=139
- orch: best +10,405 (`508ceae58587`), n=186
- queue: best +10,332 (`53b40a96cac7`), n=208
- wide: best +10,209 (`64e5a7b2f56a`), n=159

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,233 | 35 | 92 | 42 | 688 | 11.42 | 35: +9,499 (n=2), 132: +8,639 (n=2), 81: +5,702 (n=42), 111: +5,264 (n=23), 82: +5,109 (n=3), 110: +4,922 (n=38), 92: +4,449 (n=534), 99: +3,990 (n=12), 119: +3,849 (n=9), 63: +3,619 (n=3), 54: +2,856 (n=5), 150: +2,640 (n=4), 96: +1,931 (n=3), 91: +1,573 (n=2), 121: -1,255 (n=2), 125: -2,734 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,466 | 2 | 3 | 3 | 714 | 1.22 | 2: +5,740 (n=528), 3: +909 (n=184), 4: -5,726 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,120 | 0.6 | 0.55 | 12 | 714 | 8.65 | 0.6: +5,404 (n=81), 0.55: +4,708 (n=574), 0.65: +3,011 (n=9), 0.75: +2,814 (n=7), 0.8: +2,789 (n=11), 0.7: +2,753 (n=4), 0.5: +2,449 (n=7), 0.4: +1,426 (n=3), 0.45: +296 (n=4), 0.35: -1,635 (n=2), 0.9: -3,230 (n=3), 0.3: -5,716 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +10,911 | 2 | 0 | 17 | 708 | 9.15 | 2: +8,459 (n=3), 0: +4,779 (n=653), 6: +2,980 (n=3), 7: +2,509 (n=3), 1: +2,126 (n=6), 11: +1,588 (n=7), 10: +1,472 (n=7), 8: -473 (n=6), 35: -643 (n=14), 14: -1,234 (n=4), 5: -2,452 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,029 | 18 | 20 | 12 | 712 | 6.36 | 18: +5,583 (n=126), 17: +5,458 (n=7), 20: +4,362 (n=524), 19: +4,349 (n=13), 21: +3,456 (n=24), 16: +3,297 (n=5), 22: +2,843 (n=5), 24: +1,532 (n=2), 14: -765 (n=4), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +9,987 | 108 | 100 | 38 | 697 | 11.93 | 108: +8,353 (n=2), 93: +8,014 (n=2), 110: +6,811 (n=61), 135: +6,542 (n=3), 124: +6,478 (n=5), 126: +6,252 (n=2), 132: +6,167 (n=13), 109: +6,024 (n=35), 117: +5,882 (n=2), 86: +5,197 (n=21), 67: +4,927 (n=4), 104: +4,853 (n=3), 94: +4,740 (n=10), 150: +4,708 (n=78), 87: +4,376 (n=4), 105: +4,150 (n=7), 100: +3,896 (n=429), 50: +3,314 (n=8), 68: +2,481 (n=2), 62: +519 (n=4), 82: -1,635 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +9,702 | 0.25 | 0.5 | 11 | 712 | 6.76 | 0.25: +6,376 (n=3), 1.25: +6,117 (n=5), 1.75: +5,821 (n=6), 0.5: +4,568 (n=614), 0.0: +3,895 (n=65), 0.75: +3,465 (n=6), 1.0: +3,188 (n=6), 3.0: +2,555 (n=5), 2.75: -3,326 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +8,610 | 0.25 | 1.0 | 12 | 714 | 6.23 | 0.25: +6,908 (n=2), 0.75: +6,347 (n=3), 2.0: +5,862 (n=13), 0.5: +5,356 (n=18), 1.5: +5,162 (n=430), 1.25: +5,027 (n=70), 1.75: +2,953 (n=9), 2.25: +2,523 (n=3), 1.0: +2,375 (n=152), 2.5: +2,226 (n=4), 0.0: +1,114 (n=8), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +8,561 | 17 | 17 | 9 | 712 | 5.32 | 17: +4,630 (n=643), 18: +4,446 (n=20), 16: +3,328 (n=30), 15: +3,181 (n=3), 20: +2,169 (n=4), 19: +856 (n=10), 10: -3,932 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +8,186 | 0.3 | 0.0 | 9 | 712 | 5.57 | 0.3: +5,215 (n=5), 0.0: +4,631 (n=668), 0.4: +3,165 (n=4), 0.1: +2,720 (n=21), 0.2: +1,031 (n=9), 0.6: -912 (n=2), 0.7: -2,971 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,448 | 26 | 30 | 17 | 710 | 8.98 | 26: +6,676 (n=4), 28: +5,846 (n=32), 25: +5,294 (n=50), 27: +5,218 (n=31), 30: +4,413 (n=545), 34: +4,385 (n=18), 37: +3,940 (n=8), 35: +2,046 (n=6), 29: +927 (n=3), 32: +411 (n=2), 45: +241 (n=2), 31: -278 (n=7), 33: -772 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,295 | frontier | frontier | 2 | 714 | 0.83 | frontier: +5,066 (n=655), v312: -2,229 (n=59) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,175 | 10 | 14 | 8 | 713 | 5.16 | 10: +6,990 (n=12), 9: +6,269 (n=15), 13: +4,716 (n=47), 12: +4,572 (n=6), 14: +4,408 (n=627), 8: +873 (n=3), 11: -186 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_SLACK | +7,050 | 4.5 | 6.0 | 15 | 714 | 9.71 | 4.5: +7,601 (n=5), 4.0: +6,744 (n=3), 9.5: +6,150 (n=11), 3.5: +5,639 (n=4), 6.5: +5,284 (n=15), 5.0: +5,152 (n=19), 7.0: +4,925 (n=84), 7.5: +4,885 (n=18), 5.5: +4,634 (n=14), 6.0: +4,302 (n=510), 10.0: +4,119 (n=3), 8.0: +3,995 (n=19), 2.0: +2,204 (n=4), 9.0: +755 (n=2), 8.5: +551 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +6,424 | 0.25 | 0.5 | 9 | 714 | 5.32 | 0.25: +6,457 (n=54), 0.0: +5,498 (n=71), 1.0: +5,171 (n=46), 0.5: +4,282 (n=501), 1.5: +3,621 (n=9), 1.25: +3,498 (n=4), 2.0: +2,812 (n=4), 0.75: +1,209 (n=5), 1.75: +33 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +6,301 | 13 | 14 | 14 | 713 | 6.55 | 13: +6,077 (n=18), 11: +5,475 (n=34), 15: +5,166 (n=414), 10: +5,021 (n=12), 19: +4,724 (n=8), 16: +4,367 (n=6), 12: +3,282 (n=16), 14: +3,162 (n=177), 22: +2,182 (n=2), 18: +2,061 (n=3), 17: +1,590 (n=3), 8: +212 (n=17), 20: -224 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,223 | 44 | 38 | 25 | 704 | 4.8 | 44: +6,944 (n=2), 42: +6,845 (n=2), 24: +6,542 (n=3), 50: +6,484 (n=24), 32: +5,911 (n=8), 41: +5,832 (n=43), 35: +5,443 (n=241), 20: +5,106 (n=2), 26: +5,003 (n=21), 43: +4,778 (n=3), 31: +4,580 (n=11), 28: +4,378 (n=7), 38: +3,965 (n=272), 39: +2,789 (n=3), 30: +722 (n=62) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +6,199 | 2 | 3 | 4 | 714 | 2.03 | 2: +6,175 (n=154), 3: +4,098 (n=541), 1: +1,437 (n=13), 4: -25 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,876 | 2 | 2 | 4 | 714 | 2.6 | 2: +4,940 (n=642), 3: +3,998 (n=2), 1: +179 (n=65), 0: -936 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,851 | 8 | 10 | 10 | 712 | 5.26 | 8: +5,727 (n=10), 9: +5,720 (n=86), 10: +4,506 (n=557), 12: +4,165 (n=6), 11: +2,523 (n=33), 6: +2,273 (n=4), 7: +806 (n=9), 13: -124 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 4): +10,405 (n=148)
- (9, 3, 5): +10,332 (n=88)
- (10, 3, 5): +10,290 (n=117)
- (11, 3, 6): +10,254 (n=81)
- (11, 3, 5): +10,071 (n=116)
- (12, 3, 6): +10,015 (n=44)
- (10, 3, 4): +9,940 (n=23)
- (10, 3, 6): +9,935 (n=9)
- (9, 3, 6): +9,706 (n=1)
- (12, 3, 5): +9,598 (n=34)
- (11, 3, 4): +8,559 (n=7)
- (13, 3, 5): +7,918 (n=3)
- (14, 3, 6): +7,609 (n=10)
- (15, 3, 6): +6,377 (n=6)
- (13, 3, 6): +5,356 (n=11)

_Generated 2026-09-11 21:28. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 155 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=155); harvest_min=1–3 (n=155); wheat_tiles=0–7 (n=155); wheat_stock=0–40 (n=155); min_hands=3–6 (n=155); load_per_hand=12–26 (n=155); geese=0–2 (n=155); open_melons=6–14 (n=155)
- **Evidence:** 155 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**714 candidates** with action_table data, **94083 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,520 (n=9851) |         +4,463 (n=4998) |         +4,463 (n=5712) | 20561 |
| BUY_ANIMAL |         +3,973 (n=4034) |         +4,877 (n=868) |              — (n=0) | 4902 |
| BUY_SEED |         +4,512 (n=7329) |         +4,566 (n=2728) |         +4,044 (n=988) | 11045 |
| BUY_LAND |         +4,406 (n=2510) |         +4,946 (n=703) |              — (n=0) | 3213 |
| BUY_PRODUCT |         +4,462 (n=10705) |         +4,463 (n=4998) |         +4,463 (n=4998) | 20701 |
| HIRE |         +4,339 (n=4323) |         +4,271 (n=2473) |         +4,669 (n=1871) | 8667 |
| WATER_MISSED |         +4,466 (n=8000) |         +4,463 (n=4998) |         +4,462 (n=5710) | 18708 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,188 (n=3724) |         +4,215 (n=982) |         +3,975 (n=1580) | 6286 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +4,604 |      +4,463 |      +4,499 |      +4,519 |      +4,413 |      +4,456 |
| BUY_ANIMAL |      +3,889 |           — |           — |      +4,631 |      +4,582 |      +4,097 |
| BUY_SEED |      +3,939 |      +5,270 |      -3,167 |      -1,704 |      +2,673 |      +4,557 |
| BUY_LAND |      -1,974 |      -3,287 |      +4,521 |      -1,443 |      +5,182 |      +4,425 |
| BUY_PRODUCT |      +4,463 |           — |           — |           — |           — |           — |
| HIRE |      +4,391 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,463 |      +2,419 |      +4,463 |      +4,493 |
| FEED_MISSED |           — |      +4,467 |      +3,088 |           — |           — |      +4,114 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +4,946 | 703 | 1.19 |
| 2 | BUY_ANIMAL | mid | +4,877 | 868 | 1.19 |
| 3 | HIRE | late | +4,669 | 1871 | 1.11 |
| 4 | BUY_SEED | mid | +4,566 | 2728 | 1.06 |
| 5 | SELL | early | +4,520 | 9851 | 1.06 |
| 6 | BUY_SEED | early | +4,512 | 7329 | 1.06 |
| 7 | WATER_MISSED | early | +4,466 | 8000 | 1.05 |
| 8 | SELL | mid | +4,463 | 4998 | 1.04 |
| 9 | SELL | late | +4,463 | 5712 | 1.04 |
| 10 | BUY_PRODUCT | mid | +4,463 | 4998 | 1.04 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **WATER_MISSED** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **FEED_MISSED** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **SELL** in ('mid', 'mid', 'high', 'mid'): +6,931 (n=3)
- **WATER_MISSED** in ('mid', 'mid', 'high', 'mid'): +6,931 (n=3)
- **FEED_MISSED** in ('mid', 'mid', 'high', 'mid'): +6,931 (n=3)
- **SELL** in ('low', 'mid', 'mid', 'mid'): +6,836 (n=273)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +6,836 (n=273)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,625 (n=57)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,125 (n=396)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,113 (n=400)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,091 (n=409)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,019 (n=413)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +6,006 (n=68)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +6,006 (n=68)

_Generated 2026-09-11 21:28. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._