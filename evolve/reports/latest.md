# Evolution run 20260911-152501

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.01 h · candidates evaluated this run: 128 · games 29,908 (14,870/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 19 | 38 |
| dead_pattern | 7 | 14 |
| dead_smoke | 6 | 48 |
| alive | 23 | 2944 |
| held_fail | 5 | 1840 |
| held_pass | 68 | 25024 |
| error | 0 | 0 |

Population (all runs, reached dev): 526 · held-out evaluated: 345 · held-out PASS: 312

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
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | **+9,843** | 9.4 | 20-0 | -16,899 | +10,107 | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,771 -> final +3,317); days 16-23 drivers: missed_water -30, work_turns +96, idle_turns -29, feed_hour -1.45. Hands 13 vs 8, animals 10 vs 11, plants 58 vs 57 |
| `4df8b6c50970` | orch | ablate:wheat_tiles | **+9,820** | 8.5 | 20-0 | -16,440 | +9,692 | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,541 -> final +8,772); days 14-21 drivers: missed_water -20, work_turns +67, idle_turns -54, feed_hour -1.5. Hands 11 vs 8, animals 9 vs 11, plants 64 vs 57. |
| `a141ecf7c8cc` | wide | crossover | **+9,789** | 7.6 | 20-0 | -16,435 | +10,071 | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |  | cand pulls ahead of C1 from day 16 (gap +1,841 -> final +5,832); days 14-21 drivers: missed_water -31, work_turns +112, sales_rev +2,171, idle_turns -34. Hands 11 vs 8, animals 11 vs 11, plants 60 vs  |
| `71e000cd20cf` | o15 | ablate:animal_routing | **+9,684** | 7.8 | 20-0 | -16,285 | +9,245 | melon_floor 0→200, early_hire_days 3→5, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |  | cand pulls ahead of C1 from day 16 (gap +1,786 -> final +5,458); days 14-21 drivers: missed_water -27, work_turns +101, sales_rev +1,796, feed_hour -1.32. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `054925826fd0` | orch | crossover | **+9,643** | 9.0 | 20-0 | -16,486 | +8,658 | melon_floor 0→100, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→105, OPP_GROWTH 1.4→1.6, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.25, ORCH_P_PLANT 1.0→2.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→10 |  | cand pulls ahead of C1 from day 16 (gap +1,962 -> final +4,469); days 14-21 drivers: work_turns +109, missed_water -20, sales_rev +2,405, idle_turns -57. Hands 11 vs 8, animals 11 vs 11, plants 58 vs  |
| `94a200092138` | queue | crossover | **+9,642** | 10.8 | 20-0 | -16,617 | +8,905 | early_hire_days 3→2, max_animals 17→18, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→18, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→1.25, ORCH_P_SLACK 6.0→5.0, ORCH_SLACK_HOUR 14→13 |  | cand pulls ahead of C1 from day 16 (gap +2,440 -> final +10,248); days 14-21 drivers: missed_water -29, work_turns +71, idle_turns -63, feed_hour -1.54. Hands 9 vs 8, animals 9 vs 11, plants 65 vs 57. |
| `0f7d909f4ef7` | o15 | paired | **+9,561** | 8.3 | 20-0 | -16,083 | +9,675 | melon_floor 0→200, early_hire_days 3→5, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 | melon_floor ?, early_hire_days ? | cand pulls ahead of C1 from day 16 (gap +1,778 -> final +5,744); days 14-21 drivers: missed_water -31, work_turns +112, sales_rev +2,171, idle_turns -34. Hands 11 vs 8, animals 11 vs 11, plants 60 vs  |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | +10,107 | 5.9 | 10-0 | -6,749 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a141ecf7c8cc` | wide | crossover | +10,071 | 5.8 | 10-0 | -6,073 | held_pass | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |
| `933e21488445` | orch | paired | +10,055 | 7.6 | 10-0 | -6,750 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `5e7410992135` | queue | crossover | +9,970 | 4.7 | 10-0 | -7,264 | held_pass | harvest_min 1→2, wheat_per_animal 0.0→0.1, wheat_cap 22→21, setup_capital_share 0.25→0.1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→4.5, ORCH_SLACK_HOUR 14→15 |
| `cbeff72fd1ca` | queue | ablate:ORCH_SLACK_HOUR | +9,946 | 6.0 | 10-0 | -7,031 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a9e2da40d2b1` | orch | ablate:open_cows | +9,761 | 5.3 | 10-0 | -7,117 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `c929dedaf4c7` | orch | crossover | +9,716 | 6.5 | 10-0 | -6,734 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `2bcc9334a840` | orch | migrate | +9,696 | 5.3 | 10-0 | -13,946 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `4df8b6c50970` | orch | ablate:wheat_tiles | +9,692 | 7.3 | 10-0 | -6,598 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `0f7d909f4ef7` | o15 | paired | +9,675 | 5.7 | 10-0 | -5,509 | held_pass | melon_floor 0→200, early_hire_days 3→5, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |
| `249c9825c232` | wide | block_pair | +9,635 | 6.9 | 10-0 | -6,448 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `25f7a412756d` | orch | mutate | +9,594 | 5.2 | 10-0 | -7,384 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, setup_capital_share 0.25→0.5, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_SLACK_HOUR 14→15 |
| `d5885e3a3a52` | queue | archive_crossover:crossover_g000050_20260911-122309_0 | +9,545 | 5.5 | 10-0 | -8,447 | held_pass | harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `20aecc07a779` | orch | migrate | +9,540 | 6.6 | 10-0 | -6,904 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `72888332678b` | queue | mutate | +9,517 | 6.0 | 10-0 | -8,678 | held_pass | harvest_min 1→2, wheat_cap 22→25, wheat_sell_price 30→34, setup_capital_share 0.25→0.2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, CROP_SWEEP_RADIUS 5→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→0.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→1.0 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +9,675 (`0f7d909f4ef7`), n=92
- orch: best +10,055 (`933e21488445`), n=141
- queue: best +10,107 (`a45b4a44d86f`), n=155
- wide: best +10,071 (`a141ecf7c8cc`), n=116

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| demand_share | +11,605 | 0.6 | 0.55 | 11 | 526 | 8.52 | 0.6: +4,847 (n=34), 0.55: +4,261 (n=455), 0.75: +4,101 (n=4), 0.5: +3,141 (n=6), 0.8: +2,766 (n=7), 0.7: +1,886 (n=3), 0.65: +153 (n=4), 0.4: +126 (n=2), 0.45: -1,525 (n=3), 0.9: -4,198 (n=2), 0.3: -6,758 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +11,373 | 132 | 92 | 34 | 507 | 11.13 | 132: +8,639 (n=2), 99: +5,768 (n=9), 110: +5,541 (n=17), 111: +5,527 (n=21), 81: +5,137 (n=18), 119: +4,879 (n=6), 92: +3,971 (n=410), 63: +3,619 (n=3), 54: +2,856 (n=5), 82: +2,781 (n=2), 96: +1,931 (n=3), 91: +1,573 (n=2), 150: +963 (n=3), 121: -1,255 (n=2), 125: -2,734 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,329 | 2 | 3 | 3 | 526 | 0.99 | 2: +5,604 (n=349), 3: +955 (n=175), 4: -5,726 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,211 | 17 | 20 | 12 | 523 | 5.66 | 17: +6,766 (n=5), 18: +4,947 (n=88), 20: +3,912 (n=387), 21: +3,895 (n=19), 19: +3,381 (n=10), 16: +3,297 (n=5), 22: +2,843 (n=5), 14: -2,284 (n=2), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +9,393 | 5 | 3 | 7 | 526 | 4.22 | 5: +6,446 (n=15), 4: +5,056 (n=9), 1: +4,616 (n=86), 3: +3,919 (n=392), 2: +2,132 (n=13), 0: +1,567 (n=9), 6: -2,947 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,102 | 2 | 0 | 15 | 520 | 7.2 | 2: +8,459 (n=3), 0: +4,318 (n=474), 7: +3,007 (n=2), 6: +2,980 (n=3), 1: +2,557 (n=5), 11: +1,588 (n=7), 10: +616 (n=6), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_SLACK | +8,909 | 4.5 | 6.0 | 13 | 526 | 8.44 | 4.5: +8,396 (n=3), 3.5: +8,211 (n=2), 9.5: +7,031 (n=9), 4.0: +6,744 (n=3), 7.5: +5,203 (n=11), 5.0: +4,672 (n=15), 7.0: +4,669 (n=66), 8.0: +4,472 (n=16), 5.5: +4,310 (n=6), 6.0: +3,717 (n=382), 2.0: +3,180 (n=3), 6.5: +3,107 (n=8), 8.5: -512 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,881 | 28 | 30 | 16 | 522 | 8.4 | 28: +7,109 (n=18), 26: +6,892 (n=2), 27: +5,545 (n=29), 37: +4,645 (n=3), 34: +4,416 (n=16), 25: +4,269 (n=26), 30: +3,869 (n=409), 35: +2,947 (n=5), 29: +927 (n=3), 32: +411 (n=2), 31: -278 (n=7), 33: -772 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,551 | 17 | 22 | 12 | 524 | 6.25 | 17: +7,379 (n=3), 21: +4,828 (n=29), 25: +4,706 (n=380), 23: +4,381 (n=29), 9: +3,385 (n=4), 24: +3,279 (n=4), 18: +2,861 (n=2), 12: +2,652 (n=2), 20: +942 (n=4), 22: -172 (n=67) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +7,495 | 93 | 100 | 34 | 509 | 10.42 | 93: +8,014 (n=2), 110: +7,178 (n=16), 50: +7,121 (n=2), 135: +6,542 (n=3), 132: +5,940 (n=8), 117: +5,882 (n=2), 109: +5,124 (n=20), 86: +5,017 (n=19), 67: +4,927 (n=4), 104: +4,853 (n=3), 87: +4,376 (n=4), 150: +4,369 (n=63), 105: +4,150 (n=7), 94: +4,147 (n=8), 100: +3,597 (n=342), 68: +2,481 (n=2), 62: +519 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +7,349 | 2 | 3 | 4 | 526 | 2.16 | 2: +5,550 (n=96), 3: +3,786 (n=415), 1: +1,638 (n=10), 4: -1,799 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,254 | frontier | frontier | 2 | 526 | 0.84 | frontier: +4,607 (n=483), v312: -2,647 (n=43) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +6,822 | 9 | 14 | 8 | 524 | 4.39 | 9: +6,636 (n=3), 13: +4,745 (n=40), 14: +4,002 (n=471), 12: +3,849 (n=5), 8: +1,670 (n=2), 11: -186 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_FERT | +6,494 | 1.0 | 0.5 | 9 | 526 | 5.02 | 1.0: +5,726 (n=98), 1.5: +4,587 (n=4), 0.75: +4,094 (n=43), 0.5: +3,725 (n=352), 0.25: +3,638 (n=11), 2.0: +1,199 (n=3), 0.0: +447 (n=9), 1.25: -35 (n=2), 1.75: -768 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +6,350 | 1.25 | 1.5 | 19 | 520 | 8.35 | 1.25: +7,749 (n=7), 3.0: +6,723 (n=22), 4.0: +5,616 (n=2), 3.5: +5,316 (n=75), 0.0: +4,061 (n=11), 2.5: +4,022 (n=3), 5.0: +3,972 (n=3), 2.0: +3,926 (n=3), 3.25: +3,698 (n=3), 1.5: +3,634 (n=374), 0.5: +2,701 (n=4), 2.75: +2,003 (n=10), 1.75: +1,398 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,349 | 43 | 38 | 23 | 516 | 4.69 | 43: +7,038 (n=2), 42: +6,845 (n=2), 24: +6,542 (n=3), 41: +6,257 (n=33), 35: +5,383 (n=148), 26: +5,118 (n=19), 31: +4,579 (n=10), 32: +4,296 (n=2), 50: +4,161 (n=7), 38: +3,465 (n=226), 28: +1,280 (n=3), 39: +915 (n=2), 30: +689 (n=59) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +6,108 | 0.5 | 0.5 | 8 | 523 | 3.41 | 0.5: +4,064 (n=461), 0.0: +4,025 (n=53), 1.75: +3,906 (n=3), 0.75: +3,692 (n=4), 1.0: -2,044 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +5,797 | 0.3 | 0.0 | 8 | 524 | 4.66 | 0.3: +4,884 (n=4), 0.0: +4,153 (n=494), 0.1: +2,971 (n=13), 0.4: +2,020 (n=3), 0.2: +204 (n=8), 0.6: -912 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,754 | 2 | 2 | 4 | 525 | 1.62 | 2: +4,595 (n=459), 1: -15 (n=62), 0: -1,159 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| NEAR_RADIUS | +5,742 | 4 | 2 | 3 | 526 | 1.49 | 4: +7,792 (n=2), 2: +4,393 (n=436), 3: +2,050 (n=88) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +10,107 (n=88)
- (11, 3, 5): +10,071 (n=90)
- (11, 3, 6): +10,055 (n=62)
- (9, 3, 4): +9,970 (n=115)
- (9, 3, 5): +9,946 (n=71)
- (10, 3, 4): +9,462 (n=16)
- (10, 3, 6): +9,276 (n=5)
- (12, 3, 5): +9,160 (n=20)
- (12, 3, 6): +8,919 (n=27)
- (11, 3, 4): +8,559 (n=4)
- (14, 3, 6): +7,609 (n=6)
- (15, 3, 6): +6,377 (n=4)
- (8, 3, 4): +1,764 (n=1)
- (13, 3, 5): +1,174 (n=2)
- (13, 3, 6): +950 (n=6)

_Generated 2026-09-11 17:25. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 121 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=121); harvest_min=1–3 (n=121); wheat_tiles=0–7 (n=121); wheat_stock=0–40 (n=121); min_hands=3–6 (n=121); load_per_hand=12–26 (n=121); geese=0–2 (n=121); open_melons=7–14 (n=121)
- **Evidence:** 121 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**526 candidates** with action_table data, **69426 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,072 (n=7250) |         +4,014 (n=3682) |         +4,014 (n=4208) | 15140 |
| BUY_ANIMAL |         +3,570 (n=2996) |         +4,367 (n=638) |              — (n=0) | 3634 |
| BUY_SEED |         +4,064 (n=5408) |         +4,142 (n=2013) |         +3,626 (n=734) | 8155 |
| BUY_LAND |         +3,952 (n=1848) |         +4,539 (n=512) |              — (n=0) | 2360 |
| BUY_PRODUCT |         +4,014 (n=7887) |         +4,014 (n=3682) |         +4,014 (n=3682) | 15251 |
| HIRE |         +3,904 (n=3217) |         +3,842 (n=1821) |         +4,205 (n=1386) | 6424 |
| WATER_MISSED |         +4,020 (n=5895) |         +4,014 (n=3682) |         +4,012 (n=4206) | 13783 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +3,759 (n=2754) |         +3,662 (n=735) |         +3,495 (n=1190) | 4679 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +4,156 |      +4,014 |      +4,044 |      +4,148 |      +3,982 |      +4,001 |
| BUY_ANIMAL |      +3,452 |           — |           — |      +4,652 |      +4,121 |      +3,682 |
| BUY_SEED |      +3,507 |      +4,866 |      -3,985 |           — |      +2,384 |      +4,114 |
| BUY_LAND |      -1,073 |      -4,113 |      +4,076 |      -1,758 |      +4,685 |      +3,974 |
| BUY_PRODUCT |      +4,014 |           — |           — |           — |           — |           — |
| HIRE |      +3,951 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,014 |      +2,134 |      +4,014 |      +4,045 |
| FEED_MISSED |           — |      +3,998 |      +2,731 |           — |           — |      +3,653 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +4,539 | 512 | 1.1 |
| 2 | BUY_ANIMAL | mid | +4,367 | 638 | 1.05 |
| 3 | HIRE | late | +4,205 | 1386 | 1.01 |
| 4 | BUY_SEED | mid | +4,142 | 2013 | 0.96 |
| 5 | SELL | early | +4,072 | 7250 | 0.96 |
| 6 | BUY_SEED | early | +4,064 | 5408 | 0.96 |
| 7 | WATER_MISSED | early | +4,020 | 5895 | 0.94 |
| 8 | SELL | mid | +4,014 | 3682 | 0.94 |
| 9 | SELL | late | +4,014 | 4208 | 0.94 |
| 10 | BUY_PRODUCT | early | +4,014 | 7887 | 0.94 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **WATER_MISSED** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **FEED_MISSED** in ('low', 'low', 'high', 'mid'): -6,970 (n=4)
- **WATER_MISSED** in ('low', 'high', 'high', 'high'): -6,662 (n=31)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,619 (n=42)
- **SELL** in ('low', 'high', 'high', 'high'): -6,609 (n=32)
- **BUY_PRODUCT** in ('low', 'high', 'high', 'high'): -6,609 (n=32)
- **HIRE** in ('low', 'high', 'high', 'high'): -6,394 (n=19)
- **SELL** in ('low', 'mid', 'mid', 'mid'): +6,281 (n=177)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +6,281 (n=177)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +6,012 (n=50)
- **BUY_SEED** in ('low', 'high', 'high', 'high'): -6,012 (n=11)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +6,012 (n=50)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +5,771 (n=270)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +5,769 (n=275)

_Generated 2026-09-11 17:25. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._