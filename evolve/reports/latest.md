# Evolution run 20260911-172641

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.01 h · candidates evaluated this run: 111 · games 28,134 (13,967/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 14 | 28 |
| dead_pattern | 5 | 10 |
| dead_smoke | 6 | 48 |
| alive | 15 | 1920 |
| held_fail | 6 | 2208 |
| held_pass | 65 | 23920 |
| error | 0 | 0 |

Population (all runs, reached dev): 612 · held-out evaluated: 416 · held-out PASS: 377

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
| `67924b68c4e5` | orch | crossover | **+10,454** | 8.4 | 20-0 | -16,968 | +8,588 | harvest_min 1→3, geese 0→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,927 -> final +5,568); days 16-23 drivers: sales_rev +5,449, work_turns +119, missed_water -20, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `d7eec7135f06` | queue | mutate | **+10,140** | 7.2 | 19-1 | -16,966 | +8,831 | melon_floor 0→100, harvest_min 1→3, geese 0→2, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→94, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,640 -> final +6,963); days 16-23 drivers: sales_rev +5,689, work_turns +140, missed_water -12, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 57 vs  |
| `ad621af0852e` | orch | migrate | **+10,100** | 9.9 | 20-0 | -16,287 | +8,812 | harvest_min 1→3, load_per_hand 20→21, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→93, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +2,751 -> final +9,033); days 17-24 drivers: missed_water -35, work_turns +53, idle_turns -39, sales_rev +1,137. Hands 12 vs 14, animals 9 vs 11, plants 62 vs 5 |
| `369ac717437c` | queue | mutate | **+10,014** | 8.0 | 20-0 | -16,804 | +9,070 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, CROP_SWEEP_RADIUS -91, STRAW_CUTOFF ?, MELON_PRICE_CUSHION ?, FERT_RADIUS ? | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `fb4e3411021e` | queue | ablate:CROP_SWEEP_RADIUS | **+9,894** | 8.1 | 20-0 | -16,815 | +9,160 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `38c6d83e6927` | o15 | paired | **+9,891** | 8.4 | 20-0 | -17,834 | +9,432 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→18, early_hire_days 3→1, wheat_cap 22→25, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→2.0, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +1,723 -> final +8,969); days 14-21 drivers: sales_rev +5,040, missed_water -20, work_turns +89, feed_hour -1.51. Hands 11 vs 8, animals 9 vs 11, plants 65 vs 5 |
| `12de989c6c68` | queue | archive_crossover:crossover_g000025_20260911-181614_1 | **+9,853** | 9.5 | 20-0 | -15,808 | +8,822 | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +1,926 -> final +2,817); days 14-21 drivers: work_turns +126, missed_water -24, sales_rev +2,022, idle_turns -38. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | **+9,843** | 9.4 | 20-0 | -16,899 | +10,107 | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,771 -> final +3,317); days 16-23 drivers: missed_water -30, work_turns +96, idle_turns -29, feed_hour -1.45. Hands 13 vs 8, animals 10 vs 11, plants 58 vs 57 |
| `4df8b6c50970` | orch | ablate:wheat_tiles | **+9,820** | 8.5 | 20-0 | -16,440 | +9,692 | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,541 -> final +8,772); days 14-21 drivers: missed_water -20, work_turns +67, idle_turns -54, feed_hour -1.5. Hands 11 vs 8, animals 9 vs 11, plants 64 vs 57. |
| `819e3fd9b57b` | orch | mutate | **+9,811** | 8.0 | 20-0 | -18,790 | +8,982 | harvest_min 1→3, open_melons 10→12, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 11 (gap +3,919 -> final +8,642); days 9-16 drivers: missed_water -9, sales_rev +1,746, idle_turns -39, feed_hour -1.64. Hands 8 vs 12, animals 9 vs 11, plants 59 vs 60. |
| `a141ecf7c8cc` | wide | crossover | **+9,789** | 7.6 | 20-0 | -16,435 | +10,071 | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |  | cand pulls ahead of C1 from day 16 (gap +1,841 -> final +5,832); days 14-21 drivers: missed_water -31, work_turns +112, sales_rev +2,171, idle_turns -34. Hands 11 vs 8, animals 11 vs 11, plants 60 vs  |
| `71e000cd20cf` | o15 | ablate:animal_routing | **+9,684** | 7.8 | 20-0 | -16,285 | +9,245 | melon_floor 0→200, early_hire_days 3→5, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |  | cand pulls ahead of C1 from day 16 (gap +1,786 -> final +5,458); days 14-21 drivers: missed_water -27, work_turns +101, sales_rev +1,796, feed_hour -1.32. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `054925826fd0` | orch | crossover | **+9,643** | 9.0 | 20-0 | -16,486 | +8,658 | melon_floor 0→100, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→105, OPP_GROWTH 1.4→1.6, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.25, ORCH_P_PLANT 1.0→2.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→10 |  | cand pulls ahead of C1 from day 16 (gap +1,962 -> final +4,469); days 14-21 drivers: work_turns +109, missed_water -20, sales_rev +2,405, idle_turns -57. Hands 11 vs 8, animals 11 vs 11, plants 58 vs  |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `508ceae58587` | orch | ablate:ORCH_COMMIT | +10,405 | 6.4 | 10-0 | -6,287 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `53b40a96cac7` | queue | archive_crossover:crossover_g000050_20260911-185026_0 | +10,332 | 4.6 | 10-0 | -8,543 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | +10,107 | 5.9 | 10-0 | -6,749 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a141ecf7c8cc` | wide | crossover | +10,071 | 5.8 | 10-0 | -6,073 | held_pass | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |
| `933e21488445` | orch | paired | +10,055 | 7.6 | 10-0 | -6,750 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `5e7410992135` | queue | crossover | +9,970 | 4.7 | 10-0 | -7,264 | held_pass | harvest_min 1→2, wheat_per_animal 0.0→0.1, wheat_cap 22→21, setup_capital_share 0.25→0.1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→4.5, ORCH_SLACK_HOUR 14→15 |
| `cbeff72fd1ca` | queue | ablate:ORCH_SLACK_HOUR | +9,946 | 6.0 | 10-0 | -7,031 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `df547f34fca3` | o15 | paired | +9,940 | 6.3 | 10-0 | -6,598 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `40d8d9e50b7f` | queue | archive_crossover:crossover_g000075_20260911-192036_0 | +9,935 | 6.0 | 10-0 | -6,557 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `32230d7d021c` | wide | crossover | +9,823 | 4.6 | 10-0 | -8,590 | held_pass | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.0, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `39e0a837384d` | o15 | paired | +9,780 | 5.8 | 10-0 | -7,822 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→109, OPP_GROWTH 1.4→1.7, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→1.0, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→11 |
| `a9e2da40d2b1` | orch | ablate:open_cows | +9,761 | 5.3 | 10-0 | -7,117 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `c929dedaf4c7` | orch | crossover | +9,716 | 6.5 | 10-0 | -6,734 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `2bcc9334a840` | orch | migrate | +9,696 | 5.3 | 10-0 | -13,946 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `4df8b6c50970` | orch | ablate:wheat_tiles | +9,692 | 7.3 | 10-0 | -6,598 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +9,940 (`df547f34fca3`), n=116
- orch: best +10,405 (`508ceae58587`), n=161
- queue: best +10,332 (`53b40a96cac7`), n=180
- wide: best +10,071 (`a141ecf7c8cc`), n=133

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| demand_share | +11,693 | 0.6 | 0.55 | 12 | 611 | 8.24 | 0.6: +5,341 (n=58), 0.75: +4,733 (n=5), 0.55: +4,516 (n=513), 0.5: +3,141 (n=6), 0.8: +2,766 (n=7), 0.7: +2,753 (n=4), 0.65: +153 (n=4), 0.4: +126 (n=2), 0.45: -1,525 (n=3), 0.9: -4,198 (n=2), 0.3: -6,353 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,457 | 2 | 3 | 3 | 612 | 1.12 | 2: +5,731 (n=433), 3: +986 (n=177), 4: -5,726 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +11,373 | 132 | 92 | 36 | 591 | 10.85 | 132: +8,639 (n=2), 81: +6,098 (n=31), 110: +5,473 (n=26), 111: +5,320 (n=22), 119: +4,963 (n=8), 99: +4,363 (n=11), 92: +4,289 (n=467), 63: +3,619 (n=3), 54: +2,856 (n=5), 82: +2,781 (n=2), 96: +1,931 (n=3), 91: +1,573 (n=2), 150: +963 (n=3), 121: -1,255 (n=2), 125: -2,734 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,832 | 18 | 20 | 12 | 609 | 5.61 | 18: +5,387 (n=106), 17: +5,328 (n=6), 20: +4,237 (n=447), 19: +3,868 (n=11), 21: +3,611 (n=23), 16: +3,297 (n=5), 22: +2,843 (n=5), 14: -765 (n=4), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,102 | 2 | 0 | 17 | 605 | 8.19 | 2: +8,459 (n=3), 0: +4,642 (n=556), 7: +3,007 (n=2), 6: +2,980 (n=3), 1: +2,557 (n=5), 11: +1,588 (n=7), 10: +616 (n=6), 14: +42 (n=3), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_SLACK | +8,723 | 3.5 | 6.0 | 14 | 612 | 9.02 | 3.5: +8,211 (n=2), 4.5: +7,601 (n=5), 9.5: +6,768 (n=10), 4.0: +6,744 (n=3), 5.5: +5,114 (n=7), 7.0: +4,947 (n=81), 5.0: +4,672 (n=15), 6.5: +4,570 (n=13), 7.5: +4,498 (n=15), 8.0: +4,472 (n=16), 6.0: +4,081 (n=438), 2.0: +3,180 (n=3), 9.0: +755 (n=2), 8.5: -512 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +8,521 | 7 | 3 | 8 | 612 | 5.04 | 7: +5,991 (n=4), 5: +5,611 (n=20), 4: +5,056 (n=9), 1: +4,622 (n=88), 3: +4,338 (n=462), 0: +2,446 (n=13), 2: +2,132 (n=13), 6: -2,530 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +8,422 | 17 | 17 | 8 | 611 | 5.27 | 17: +4,490 (n=547), 18: +4,148 (n=19), 16: +3,561 (n=28), 15: +2,199 (n=2), 19: +856 (n=10), 20: +542 (n=3), 10: -3,932 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +8,306 | 0.3 | 0.0 | 9 | 610 | 5.58 | 0.3: +5,215 (n=5), 0.0: +4,471 (n=573), 0.4: +3,165 (n=4), 0.1: +2,947 (n=15), 0.2: +1,031 (n=9), 0.6: -912 (n=2), 0.7: -3,091 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,964 | 10 | 14 | 8 | 611 | 5.16 | 10: +7,778 (n=7), 9: +5,143 (n=9), 13: +4,749 (n=46), 12: +4,572 (n=6), 14: +4,278 (n=538), 8: +1,670 (n=2), 11: -186 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +7,789 | 2 | 3 | 4 | 612 | 2.07 | 2: +5,990 (n=125), 3: +4,015 (n=470), 1: +1,491 (n=12), 4: -1,799 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +7,495 | 93 | 100 | 38 | 592 | 10.4 | 93: +8,014 (n=2), 110: +7,460 (n=31), 135: +6,542 (n=3), 124: +6,478 (n=5), 109: +6,060 (n=29), 132: +5,944 (n=12), 117: +5,882 (n=2), 86: +5,197 (n=21), 67: +4,927 (n=4), 104: +4,853 (n=3), 150: +4,740 (n=74), 94: +4,387 (n=9), 87: +4,376 (n=4), 105: +4,150 (n=7), 100: +3,739 (n=375), 50: +3,008 (n=5), 68: +2,481 (n=2), 62: +519 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,339 | frontier | frontier | 2 | 612 | 0.84 | frontier: +4,897 (n=564), v312: -2,442 (n=48) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,219 | 28 | 30 | 17 | 607 | 8.39 | 28: +6,447 (n=25), 26: +6,124 (n=3), 27: +5,393 (n=30), 37: +4,645 (n=3), 34: +4,628 (n=17), 25: +4,594 (n=35), 30: +4,238 (n=475), 35: +2,947 (n=5), 29: +927 (n=3), 32: +411 (n=2), 31: -278 (n=7), 33: -772 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_FERT | +6,747 | 1.0 | 0.5 | 9 | 612 | 4.87 | 1.0: +5,978 (n=112), 0.75: +4,787 (n=55), 1.5: +4,587 (n=4), 0.25: +4,388 (n=18), 0.5: +3,970 (n=399), 0.0: +1,999 (n=15), 2.0: +1,199 (n=3), 1.25: -35 (n=2), 1.75: -768 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +6,350 | 1.25 | 1.5 | 19 | 606 | 7.8 | 1.25: +7,749 (n=7), 2.5: +6,528 (n=9), 3.0: +6,252 (n=34), 3.5: +5,963 (n=105), 4.0: +5,616 (n=2), 2.0: +4,284 (n=4), 0.0: +4,061 (n=11), 5.0: +3,972 (n=3), 1.5: +3,759 (n=410), 3.25: +3,698 (n=3), 0.5: +3,613 (n=5), 2.75: +2,003 (n=10), 1.75: +1,398 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,349 | 43 | 38 | 23 | 604 | 5.23 | 43: +7,038 (n=2), 44: +6,944 (n=2), 42: +6,845 (n=2), 24: +6,542 (n=3), 41: +5,999 (n=41), 32: +5,911 (n=8), 35: +5,508 (n=182), 20: +5,106 (n=2), 26: +5,052 (n=20), 50: +4,642 (n=13), 31: +4,580 (n=11), 38: +3,835 (n=251), 28: +3,544 (n=5), 39: +2,789 (n=3), 30: +689 (n=59) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +6,211 | 0.25 | 0.5 | 9 | 612 | 5.26 | 0.25: +6,244 (n=39), 0.0: +5,542 (n=66), 1.0: +5,306 (n=42), 1.25: +4,878 (n=2), 0.5: +4,111 (n=426), 2.0: +4,068 (n=3), 1.5: +3,621 (n=9), 0.75: +1,209 (n=5), 1.75: +33 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +6,140 | 19 | 22 | 13 | 610 | 6.93 | 19: +6,301 (n=2), 17: +5,129 (n=4), 21: +5,088 (n=44), 25: +4,972 (n=440), 23: +4,463 (n=31), 9: +3,385 (n=4), 24: +3,303 (n=7), 18: +2,861 (n=2), 12: +2,652 (n=2), 20: +942 (n=4), 22: +161 (n=70) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,913 | 9 | 10 | 8 | 612 | 5.09 | 9: +5,789 (n=83), 8: +5,559 (n=9), 12: +4,831 (n=4), 10: +4,314 (n=466), 11: +2,426 (n=31), 6: +2,273 (n=4), 7: +130 (n=8), 13: -124 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 4): +10,405 (n=129)
- (9, 3, 5): +10,332 (n=82)
- (10, 3, 5): +10,107 (n=98)
- (11, 3, 5): +10,071 (n=105)
- (11, 3, 6): +10,055 (n=71)
- (10, 3, 4): +9,940 (n=19)
- (10, 3, 6): +9,935 (n=8)
- (12, 3, 5): +9,160 (n=25)
- (12, 3, 6): +8,919 (n=36)
- (11, 3, 4): +8,559 (n=6)
- (14, 3, 6): +7,609 (n=7)
- (15, 3, 6): +6,377 (n=4)
- (13, 3, 6): +5,356 (n=8)
- (8, 3, 5): +1,791 (n=2)
- (8, 3, 4): +1,764 (n=1)

_Generated 2026-09-11 19:27. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 138 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=138); harvest_min=1–3 (n=138); wheat_tiles=0–7 (n=138); wheat_stock=0–40 (n=138); min_hands=3–6 (n=138); load_per_hand=12–26 (n=138); geese=0–2 (n=138); open_melons=6–14 (n=138)
- **Evidence:** 138 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**612 candidates** with action_table data, **80655 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,378 (n=8440) |         +4,321 (n=4284) |         +4,321 (n=4896) | 17620 |
| BUY_ANIMAL |         +3,873 (n=3462) |         +4,697 (n=741) |              — (n=0) | 4203 |
| BUY_SEED |         +4,375 (n=6293) |         +4,441 (n=2326) |         +3,927 (n=852) | 9471 |
| BUY_LAND |         +4,275 (n=2149) |         +4,852 (n=594) |              — (n=0) | 2743 |
| BUY_PRODUCT |         +4,321 (n=9176) |         +4,321 (n=4284) |         +4,321 (n=4284) | 17744 |
| HIRE |         +4,203 (n=3719) |         +4,132 (n=2114) |         +4,510 (n=1607) | 7440 |
| WATER_MISSED |         +4,330 (n=6863) |         +4,321 (n=4284) |         +4,320 (n=4894) | 16041 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,072 (n=3188) |         +4,051 (n=843) |         +3,840 (n=1362) | 5393 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +4,458 |      +4,321 |      +4,361 |      +4,445 |      +4,288 |      +4,308 |
| BUY_ANIMAL |      +3,785 |           — |           — |      +4,839 |      +4,426 |      +3,987 |
| BUY_SEED |      +3,837 |      +5,155 |      -3,985 |           — |      +2,666 |      +4,418 |
| BUY_LAND |      -1,785 |      -4,085 |      +4,377 |      -1,758 |      +4,987 |      +4,312 |
| BUY_PRODUCT |      +4,321 |           — |           — |           — |           — |           — |
| HIRE |      +4,249 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,321 |      +2,524 |      +4,321 |      +4,353 |
| FEED_MISSED |           — |      +4,324 |      +3,256 |           — |           — |      +3,984 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +4,852 | 594 | 1.19 |
| 2 | BUY_ANIMAL | mid | +4,697 | 741 | 1.15 |
| 3 | HIRE | late | +4,510 | 1607 | 1.09 |
| 4 | BUY_SEED | mid | +4,441 | 2326 | 1.04 |
| 5 | SELL | early | +4,378 | 8440 | 1.04 |
| 6 | BUY_SEED | early | +4,375 | 6293 | 1.04 |
| 7 | WATER_MISSED | early | +4,330 | 6863 | 1.03 |
| 8 | SELL | mid | +4,321 | 4284 | 1.02 |
| 9 | SELL | late | +4,321 | 4896 | 1.02 |
| 10 | BUY_PRODUCT | early | +4,321 | 9176 | 1.02 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **WATER_MISSED** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **FEED_MISSED** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,592 (n=54)
- **SELL** in ('low', 'mid', 'mid', 'mid'): +6,577 (n=223)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +6,577 (n=223)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +6,080 (n=63)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +6,080 (n=63)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,027 (n=324)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,015 (n=327)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +5,990 (n=335)
- **WATER_MISSED** in ('low', 'high', 'high', 'high'): -5,977 (n=34)
- **SELL** in ('low', 'high', 'high', 'high'): -5,948 (n=35)
- **BUY_PRODUCT** in ('low', 'high', 'high', 'high'): -5,948 (n=35)
- **SELL** in ('low', 'low', 'low', 'mid'): +5,904 (n=339)

_Generated 2026-09-11 19:27. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._