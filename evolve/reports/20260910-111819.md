# Evolution run 20260910-111819

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.37 h · candidates evaluated this run: 27 · games 3,426 (9,331/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 1 | 2 |
| dead_pattern | 4 | 8 |
| dead_smoke | 1 | 8 |
| alive | 18 | 2304 |
| held_fail | 3 | 1104 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 454 · held-out evaluated: 43 · held-out PASS: 1

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
| `28fca2943584` | queue | archive_crossover:crossover_g000075_20260910-113243_0 | **+2,718** | 2.0 | 18-2 | -25,815 | +4,876 | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→6, feed_spare_poor 0→1, fert_keep 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,727 -> final -24,949); days 14-21 drivers: sales_rev -17,219, work_turns -237, water_hour +0.46. Hands 8 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `1019eca510ac` | wide | paired | **+2,593** | 1.9 | 15-5 | -29,280 | +5,473 | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,647 -> final -14,317); days 14-21 drivers: sales_rev -15,740, work_turns -238, travel_per_task +0.06. Hands 11 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `d5fdd7605657` | queue | archive_crossover:crossover_g000050_20260910-111312_1 | **+2,576** | 2.1 | 13-7 | -28,823 | +5,411 | melon_floor 0→200, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,761 -> final -17,078); days 14-21 drivers: sales_rev -16,651, work_turns -211, water_hour +0.29, travel_per_task +0.02. Hands 13 vs 14, animals 7 vs 11, plants |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `1019eca510ac` | wide | paired | +5,473 | 2.3 | 8-2 | -24,553 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `8d73168f191f` | wide | paired | +5,425 | 2.7 | 9-1 | -28,015 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→27, wheat_hold_days 0→2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `d5fdd7605657` | queue | archive_crossover:crossover_g000050_20260910-111312_1 | +5,411 | 2.6 | 8-2 | -23,346 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `bcf4dbd52f8d` | queue | mutate | +5,330 | 3.5 | 9-1 | -20,888 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |
| `2757e6c92f26` | queue | mutate | +5,290 | 5.1 | 10-0 | -18,243 | held_fail | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `c06c14efa4e0` | queue | archive_crossover:crossover_g000050_20260910-111312_0 | +5,132 | 3.4 | 9-1 | -23,025 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, fert_keep 0→1, demand_share 0.55→0.7, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |
| `cc8718994c22` | wide | block_pair | +5,046 | 2.1 | 9-1 | -24,840 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.2, wheat_sell_price 30→27, wheat_hold_days 0→2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `e05397e4510f` | v312 | migrate | +4,992 | 2.6 | 8-2 | -23,981 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.2, wheat_sell_price 30→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→37, HERD_LAST_DAY 17→18, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `b78610c183a0` | wide | crossover | +4,886 | 2.9 | 8-2 | -25,073 | held_fail | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `28fca2943584` | queue | archive_crossover:crossover_g000075_20260910-113243_0 | +4,876 | 3.9 | 10-0 | -22,949 | held_fail | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→6, feed_spare_poor 0→1, fert_keep 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `f5e71682ea28` | c1 | migrate | +4,572 | 2.5 | 8-2 | -20,162 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `c45dceed4bc0` | queue | migrate | +4,549 | 3.8 | 9-1 | -23,362 | held_fail | min_hands 3→4, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_cap 22→25, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→20, MAX_SHEEP 14→10 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=59
- M2: best +4,110 (`2521e3906eb6`), n=49
- c1: best +4,572 (`f5e71682ea28`), n=75
- queue: best +6,527 (`edd7288369ba`), n=141
- v312: best +4,992 (`e05397e4510f`), n=64
- wide: best +5,473 (`1019eca510ac`), n=66

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +10,675 | 61 | 100 | 35 | 438 | 13.71 | 61: +4,066 (n=3), 91: +839 (n=2), 78: +287 (n=4), 84: +137 (n=5), 74: -125 (n=2), 115: -141 (n=4), 102: -624 (n=24), 124: -740 (n=2), 100: -892 (n=339), 90: -950 (n=5), 83: -1,174 (n=3), 85: -1,380 (n=16), 82: -2,202 (n=2), 92: -2,219 (n=13), 71: -2,386 (n=2), 114: -3,075 (n=2), 104: -3,341 (n=2), 110: -4,472 (n=6), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +8,756 | 0.7 | 0.55 | 12 | 453 | 5.34 | 0.7: +4,561 (n=4), 0.65: +364 (n=35), 0.45: -461 (n=44), 0.6: -699 (n=34), 0.55: -929 (n=261), 0.5: -2,110 (n=49), 0.8: -2,572 (n=3), 0.75: -2,922 (n=5), 0.3: -3,931 (n=13), 0.85: -4,162 (n=2), 0.35: -4,194 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,661 | 40 | 38 | 21 | 451 | 4.59 | 40: +2,208 (n=22), 37: +830 (n=2), 39: +745 (n=53), 27: +660 (n=8), 50: +235 (n=2), 33: -247 (n=3), 41: -499 (n=8), 32: -714 (n=9), 35: -789 (n=60), 31: -1,204 (n=3), 34: -1,409 (n=140), 25: -1,798 (n=3), 38: -1,896 (n=115), 28: -1,927 (n=2), 46: -2,903 (n=6), 42: -2,924 (n=3), 43: -3,008 (n=10), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,962 | 134 | 92 | 40 | 440 | 16.08 | 134: +1,226 (n=2), 102: +861 (n=11), 95: +803 (n=7), 87: +688 (n=3), 124: -40 (n=7), 58: -144 (n=24), 121: -689 (n=6), 106: -780 (n=2), 107: -785 (n=9), 92: -875 (n=289), 81: -1,046 (n=2), 118: -1,081 (n=2), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 16: -1,522 (n=2), 73: -1,731 (n=2), 11: -1,789 (n=38), 72: -1,999 (n=3), 150: -2,267 (n=10), 0: -2,575 (n=3), 76: -3,783 (n=2), 115: -3,837 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,511 | 0.1 | 0.0 | 7 | 453 | 3.03 | 0.1: +416 (n=13), 0.2: -249 (n=28), 0.0: -905 (n=304), 0.3: -1,549 (n=103), 0.6: -3,949 (n=3), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,861 | 2 | 3 | 3 | 454 | 1.16 | 2: +795 (n=110), 3: -1,406 (n=327), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,835 | 13 | 14 | 7 | 454 | 3.66 | 13: +39 (n=47), 12: -930 (n=60), 14: -996 (n=302), 11: -1,360 (n=8), 15: -1,966 (n=26), 16: -2,642 (n=7), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,813 | 6 | 8 | 10 | 454 | 3.27 | 6: +125 (n=4), 10: -559 (n=194), 14: -756 (n=4), 11: -806 (n=36), 9: -908 (n=22), 8: -1,392 (n=178), 7: -1,453 (n=8), 12: -4,033 (n=2), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +5,782 | 18 | 20 | 10 | 453 | 4.3 | 18: +75 (n=22), 19: +64 (n=93), 15: -715 (n=3), 20: -1,042 (n=267), 22: -1,465 (n=6), 17: -1,808 (n=7), 21: -2,608 (n=41), 23: -2,815 (n=9), 24: -5,706 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,676 | 2 | 2 | 4 | 454 | 2.54 | 2: -796 (n=402), 1: -2,335 (n=45), 0: -4,123 (n=5), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,215 | 0.3 | 0.25 | 10 | 453 | 5.48 | 0.3: +749 (n=7), 0.4: -195 (n=56), 0.45: -501 (n=22), 0.25: -974 (n=326), 0.2: -1,303 (n=7), 0.5: -1,613 (n=5), 0.15: -1,761 (n=4), 0.35: -3,794 (n=24), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +4,577 | 5 | 22 | 15 | 451 | 5.57 | 5: +1,471 (n=8), 13: +249 (n=59), 12: +122 (n=12), 22: -1,021 (n=247), 25: -1,261 (n=66), 21: -1,542 (n=2), 19: -1,595 (n=5), 20: -1,999 (n=14), 17: -2,111 (n=3), 18: -2,236 (n=22), 24: -2,671 (n=6), 23: -3,105 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +4,519 | 3 | 0 | 12 | 449 | 5.11 | 3: +589 (n=2), 7: -237 (n=3), 9: -407 (n=6), 0: -937 (n=392), 4: -1,773 (n=41), 1: -2,141 (n=3), 6: -3,930 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,400 | 2 | 2 | 3 | 454 | 1.83 | 2: -824 (n=429), 1: -3,619 (n=16), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +4,374 | frontier | frontier | 2 | 454 | 0.88 | frontier: -750 (n=427), v312: -5,124 (n=27) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +3,563 | 1 | 0 | 3 | 454 | 1.77 | 1: +1,506 (n=31), 0: -1,186 (n=419), 2: -2,057 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,011 | 22 | 17 | 9 | 453 | 3.03 | 22: +293 (n=28), 16: +260 (n=7), 18: -195 (n=19), 17: -1,038 (n=228), 19: -1,221 (n=147), 20: -1,427 (n=8), 14: -2,248 (n=14), 21: -2,718 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +2,916 | 4 | 5 | 8 | 454 | 5.03 | 4: -139 (n=18), 6: -289 (n=12), 8: -779 (n=10), 5: -1,020 (n=342), 7: -1,043 (n=18), 2: -1,168 (n=2), 3: -1,228 (n=46), 0: -3,055 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +2,875 | 19 | 17 | 8 | 454 | 4.8 | 19: +667 (n=11), 16: +454 (n=9), 18: -677 (n=24), 14: -935 (n=5), 17: -975 (n=329), 15: -1,180 (n=38), 13: -1,877 (n=2), 20: -2,208 (n=36) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_CAP | +2,871 | 5 | 3 | 3 | 454 | 1.69 | 5: +1,821 (n=5), 3: -1,040 (n=407), 4: -1,051 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +6,527 (n=48)
- (9, 3, 3): +6,108 (n=7)
- (12, 4, 6): +5,330 (n=12)
- (8, 3, 5): +5,290 (n=16)
- (7, 3, 3): +4,876 (n=18)
- (8, 3, 4): +4,836 (n=23)
- (7, 3, 5): +4,572 (n=6)
- (16, 3, 6): +4,008 (n=3)
- (9, 3, 4): +3,671 (n=28)
- (14, 3, 6): +3,652 (n=9)
- (6, 3, 3): +3,350 (n=8)
- (9, 3, 5): +3,238 (n=14)
- (10, 3, 5): +3,207 (n=18)
- (6, 3, 4): +2,790 (n=8)
- (11, 3, 5): +2,663 (n=16)

_Generated 2026-09-10 11:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 213 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=213); harvest_min=1–3 (n=213); wheat_tiles=0–5 (n=213); wheat_stock=0–19 (n=213); min_hands=3–6 (n=213); load_per_hand=12–26 (n=213); geese=0–2 (n=213); open_melons=4–14 (n=213)
- **Evidence:** 213 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 11:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._