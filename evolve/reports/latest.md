# Evolution run 20260910-110022

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.26 h · candidates evaluated this run: 17 · games 2,524 (9,591/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 2 | 4 |
| dead_smoke | 3 | 24 |
| alive | 8 | 1024 |
| held_fail | 4 | 1472 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 413 · held-out evaluated: 35 · held-out PASS: 1

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `2757e6c92f26` | queue | mutate | **+5,444** | 4.3 | 18-2 | -25,327 | +5,290 | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,317 -> final -13,211); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `b3324e9b7110` | queue | mutate | **+4,961** | 3.3 | 19-1 | -29,707 | +6,108 | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -6,908 -> final -18,802); days 22-29 drivers: sales_rev -23,772, weeds_new +9, work_turns -103, reversals +2. Hands 3 vs 6, animals 9 vs 11, plants 0 vs 17. |
| `da68944524c1` | v312 | mutate | **+4,758** | 4.6 | 18-2 | -25,433 | +2,514 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 22 (gap -3,186 -> final -29,992); days 20-27 drivers: sales_rev -36,606, work_turns -73, water_hour +1.41. Hands 10 vs 11, animals 10 vs 11, plants 42 vs 47. |
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `4da7ca753338` | queue | mutate | **+4,083** | 3.5 | 16-4 | -23,668 | +4,086 | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,249 -> final -24,602); days 14-21 drivers: sales_rev -16,963, work_turns -270, weeds_new +2, water_hour +0.96. Hands 7 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `cf9f405831de` | v312 | crossover | **+4,014** | 5.4 | 18-2 | -24,787 | +2,332 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, max_animals 17→19, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -9,334 -> final -20,201); days 21-28 drivers: sales_rev -21,532, work_turns -65, weeds_new +3, water_hour +1.41. Hands 7 vs 9, animals 13 vs 11, plants 14 vs 33. |
| `3e744f448178` | v312 | mutate | **+3,805** | 3.6 | 16-4 | -24,664 | +3,207 | melon_floor 0→200, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -3,487 -> final -12,279); days 21-28 drivers: sales_rev -16,154, work_turns -87, idle_turns +39, weeds_new +1. Hands 9 vs 9, animals 10 vs 11, plants 22 vs 33. |
| `db61805ecfa9` | M2 | mutate | **+3,427** | 3.2 | 17-3 | -28,163 | +2,910 | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 20 (gap -3,060 -> final -43,282); days 18-25 drivers: sales_rev -43,924, work_turns -118, water_hour +0.9. Hands 11 vs 13, animals 9 vs 11, plants 60 vs 62. |
| `bcf4dbd52f8d` | queue | mutate | **+3,075** | 2.0 | 12-8 | -23,822 | +5,330 | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand pulls ahead of C1 from day 26 (gap +5,036 -> final +8,642); days 24-29 drivers: sales_rev +17,235, work_turns +68, feed_hour -1.9, idle_turns -16. Hands 6 vs 6, animals 12 vs 11, plants 27 vs 17. |
| `b78610c183a0` | wide | crossover | **+3,072** | 2.0 | 17-3 | -26,162 | +4,886 | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,254 -> final -9,989); days 15-22 drivers: sales_rev -11,173, work_turns -225. Hands 13 vs 14, animals 7 vs 11, plants 67 vs 85. |
| `bb47f6f0b3ef` | queue | archive_crossover:crossover_g000025_20260910-102949_1 | **+2,737** | 2.8 | 16-4 | -25,920 | +3,291 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, MAX_SHEEP 14→12 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,781 -> final -34,668); days 15-22 drivers: sales_rev -16,255, work_turns -235, water_hour +0.63. Hands 14 vs 14, animals 7 vs 11, plants 66 vs 85. |
| `1019eca510ac` | wide | paired | **+2,593** | 1.9 | 15-5 | -29,280 | +5,473 | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,647 -> final -14,317); days 14-21 drivers: sales_rev -15,740, work_turns -238, travel_per_task +0.06. Hands 11 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `2521e3906eb6` | M2 | migrate | **+2,378** | 2.2 | 13-7 | -28,392 | +4,110 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, max_animals 17→16, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→12, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,742 -> final -20,054); days 15-22 drivers: sales_rev -13,764, work_turns -255, water_hour +0.41. Hands 14 vs 14, animals 7 vs 11, plants 67 vs 85. |
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | **+2,328** | 1.5 | 13-7 | -26,820 | +6,527 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,255 -> final -4,859); days 14-21 drivers: sales_rev -16,071, work_turns -227. Hands 10 vs 14, animals 7 vs 11, plants 66 vs 84. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `1019eca510ac` | wide | paired | +5,473 | 2.3 | 8-2 | -24,553 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `8d73168f191f` | wide | paired | +5,425 | 2.7 | 9-1 | -28,015 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→27, wheat_hold_days 0→2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `d5fdd7605657` | queue | archive_crossover:crossover_g000050_20260910-111312_1 | +5,411 | 2.6 | 8-2 | -23,346 | alive | melon_floor 0→200, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `bcf4dbd52f8d` | queue | mutate | +5,330 | 3.5 | 9-1 | -20,888 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |
| `2757e6c92f26` | queue | mutate | +5,290 | 5.1 | 10-0 | -18,243 | held_fail | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `c06c14efa4e0` | queue | archive_crossover:crossover_g000050_20260910-111312_0 | +5,132 | 3.4 | 9-1 | -23,025 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, fert_keep 0→1, demand_share 0.55→0.7, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |
| `b78610c183a0` | wide | crossover | +4,886 | 2.9 | 8-2 | -25,073 | held_fail | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `f5e71682ea28` | c1 | migrate | +4,572 | 2.5 | 8-2 | -20,162 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `c45dceed4bc0` | queue | migrate | +4,549 | 3.8 | 9-1 | -23,362 | held_fail | min_hands 3→4, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_cap 22→25, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→20, MAX_SHEEP 14→10 · blocks: hiring |
| `150b6a4263d7` | queue | archive_crossover:crossover_g000050_20260910-103203_0 | +4,249 | 3.1 | 8-2 | -20,451 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→12, FERT_RADIUS 3→4 · blocks: hiring |
| `2521e3906eb6` | M2 | migrate | +4,110 | 3.2 | 8-2 | -19,934 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, max_animals 17→16, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→12, FERT_RADIUS 3→4 · blocks: hiring |
| `4da7ca753338` | queue | mutate | +4,086 | 2.7 | 9-1 | -19,685 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=54
- M2: best +4,110 (`2521e3906eb6`), n=43
- c1: best +4,572 (`f5e71682ea28`), n=69
- queue: best +6,527 (`edd7288369ba`), n=126
- v312: best +4,008 (`bfe4bb8d3609`), n=57
- wide: best +5,473 (`1019eca510ac`), n=64

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +10,675 | 61 | 100 | 32 | 400 | 13.82 | 61: +4,066 (n=3), 84: +1,257 (n=3), 91: +839 (n=2), 78: +287 (n=4), 74: -125 (n=2), 102: -347 (n=21), 115: -403 (n=3), 124: -740 (n=2), 90: -950 (n=5), 100: -1,030 (n=312), 83: -1,174 (n=3), 85: -1,611 (n=12), 92: -2,134 (n=12), 82: -2,202 (n=2), 71: -2,386 (n=2), 114: -3,075 (n=2), 104: -3,341 (n=2), 110: -4,472 (n=6), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +10,235 | 0.7 | 0.55 | 11 | 413 | 5.61 | 0.7: +5,231 (n=2), 0.65: +192 (n=32), 0.6: -482 (n=29), 0.45: -758 (n=34), 0.55: -1,044 (n=248), 0.5: -2,102 (n=45), 0.8: -2,572 (n=3), 0.75: -2,707 (n=4), 0.3: -3,924 (n=12), 0.85: -4,162 (n=2), 0.35: -5,004 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +8,224 | 40 | 38 | 20 | 410 | 4.47 | 40: +2,772 (n=15), 39: +655 (n=49), 50: +235 (n=2), 27: -236 (n=5), 33: -247 (n=3), 41: -441 (n=6), 32: -462 (n=8), 35: -799 (n=54), 34: -1,436 (n=132), 38: -1,898 (n=109), 28: -1,927 (n=2), 31: -2,709 (n=2), 46: -2,903 (n=6), 42: -2,924 (n=3), 43: -3,008 (n=10), 25: -3,320 (n=2), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,538 | 95 | 92 | 33 | 403 | 14.24 | 95: +803 (n=7), 87: +688 (n=3), 102: +500 (n=8), 124: -40 (n=7), 58: -219 (n=21), 107: -542 (n=8), 121: -689 (n=6), 106: -780 (n=2), 92: -1,049 (n=267), 118: -1,081 (n=2), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 16: -1,522 (n=2), 73: -1,731 (n=2), 11: -1,820 (n=36), 72: -1,999 (n=3), 150: -2,267 (n=10), 0: -2,575 (n=3), 76: -3,783 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,326 | 0.1 | 0.0 | 6 | 413 | 3.01 | 0.1: +231 (n=11), 0.0: -968 (n=276), 0.2: -1,309 (n=21), 0.3: -1,513 (n=101), 0.6: -1,828 (n=2), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,907 | 13 | 14 | 7 | 413 | 3.69 | 13: +111 (n=41), 12: -887 (n=53), 14: -1,139 (n=277), 11: -1,616 (n=7), 15: -2,074 (n=24), 16: -2,642 (n=7), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,842 | 2 | 3 | 3 | 413 | 1.23 | 2: +776 (n=89), 3: -1,445 (n=307), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,813 | 6 | 8 | 10 | 412 | 2.89 | 6: +125 (n=4), 10: -688 (n=178), 14: -756 (n=4), 9: -1,023 (n=18), 11: -1,061 (n=29), 7: -1,109 (n=7), 8: -1,463 (n=166), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,569 | 2 | 2 | 4 | 413 | 2.53 | 2: -902 (n=364), 1: -2,351 (n=42), 0: -4,123 (n=5), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +5,409 | 5 | 22 | 14 | 411 | 5.74 | 5: +1,485 (n=6), 12: +426 (n=11), 13: +128 (n=50), 22: -1,149 (n=231), 25: -1,329 (n=58), 21: -1,542 (n=2), 19: -1,887 (n=4), 20: -2,011 (n=13), 17: -2,111 (n=3), 18: -2,159 (n=21), 24: -2,671 (n=6), 23: -3,923 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,215 | 0.3 | 0.25 | 10 | 412 | 5.44 | 0.3: +749 (n=7), 0.4: -213 (n=51), 0.45: -913 (n=18), 0.25: -1,057 (n=295), 0.2: -1,303 (n=7), 0.15: -1,761 (n=4), 0.5: -2,713 (n=4), 0.35: -3,794 (n=24), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +5,043 | 19 | 20 | 10 | 412 | 4.5 | 19: -43 (n=80), 18: -539 (n=17), 15: -1,043 (n=2), 20: -1,085 (n=252), 22: -1,465 (n=6), 17: -2,638 (n=5), 21: -2,743 (n=37), 23: -2,815 (n=9), 24: -5,086 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +4,332 | frontier | frontier | 2 | 413 | 0.87 | frontier: -843 (n=387), v312: -5,175 (n=26) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,307 | 2 | 2 | 3 | 413 | 1.82 | 2: -917 (n=388), 1: -3,619 (n=16), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +3,693 | 7 | 0 | 11 | 408 | 4.25 | 7: -237 (n=3), 9: -407 (n=6), 0: -1,060 (n=357), 1: -1,595 (n=2), 4: -1,676 (n=38), 6: -3,930 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_CAP | +3,532 | 5 | 3 | 3 | 413 | 1.69 | 5: +2,291 (n=4), 3: -1,139 (n=371), 4: -1,241 (n=38) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +3,400 | 1 | 0 | 3 | 413 | 1.78 | 1: +1,342 (n=26), 0: -1,273 (n=383), 2: -2,057 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +2,915 | 4 | 7 | 8 | 413 | 4.56 | 4: -11 (n=57), 6: -448 (n=19), 10: -763 (n=5), 3: -916 (n=24), 9: -1,086 (n=11), 7: -1,343 (n=287), 5: -2,706 (n=4), 8: -2,926 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +2,877 | 19 | 17 | 8 | 413 | 4.85 | 19: +491 (n=8), 16: +87 (n=7), 18: -566 (n=23), 14: -935 (n=5), 17: -1,081 (n=302), 15: -1,202 (n=34), 13: -1,877 (n=2), 20: -2,386 (n=32) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +2,757 | 16 | 17 | 9 | 411 | 2.51 | 16: +509 (n=6), 22: +396 (n=25), 18: -813 (n=16), 20: -1,091 (n=7), 17: -1,160 (n=206), 19: -1,288 (n=137), 14: -2,248 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +6,527 (n=45)
- (9, 3, 3): +6,108 (n=7)
- (12, 4, 6): +5,330 (n=9)
- (8, 3, 5): +5,290 (n=15)
- (8, 3, 4): +4,836 (n=23)
- (7, 3, 5): +4,572 (n=6)
- (16, 3, 6): +4,008 (n=2)
- (14, 3, 6): +3,652 (n=9)
- (7, 3, 3): +3,486 (n=17)
- (10, 3, 5): +3,207 (n=15)
- (9, 3, 4): +2,962 (n=26)
- (11, 3, 5): +2,663 (n=16)
- (11, 3, 6): +2,574 (n=17)
- (9, 3, 5): +2,565 (n=11)
- (10, 3, 4): +2,514 (n=13)

_Generated 2026-09-10 11:16. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 195 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=195); harvest_min=1–3 (n=195); wheat_tiles=0–5 (n=195); wheat_stock=0–19 (n=195); min_hands=3–6 (n=195); load_per_hand=12–26 (n=195); geese=0–2 (n=195); open_melons=4–14 (n=195)
- **Evidence:** 195 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 11:16. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._