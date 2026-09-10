# Evolution run 20260910-100748

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.11 h · candidates evaluated this run: 8 · games 1,058 (9,628/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 1 | 2 |
| dead_pattern | 0 | 0 |
| dead_smoke | 1 | 8 |
| alive | 4 | 432 |
| held_fail | 2 | 616 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 301 · held-out evaluated: 14 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `db61805ecfa9` | M2 | mutate | **+3,427** | 3.2 | 17-3 | -28,163 | +2,910 | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 20 (gap -3,060 -> final -43,282); days 18-25 drivers: sales_rev -43,924, work_turns -118, water_hour +0.9. Hands 11 vs 13, animals 9 vs 11, plants 60 vs 62. |
| `b78610c183a0` | wide | crossover | **+3,072** | 2.0 | 17-3 | -26,162 | +4,886 | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,254 -> final -9,989); days 15-22 drivers: sales_rev -11,173, work_turns -225. Hands 13 vs 14, animals 7 vs 11, plants 67 vs 85. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `935becadf7d7` | queue | archive_crossover:crossover_g000025_20260910-094825_0 | **+1,563** | 1.6 | 14-6 | -25,481 | +2,260 | open_melons 8→10, open_wheat 7→6, early_hire_days 5→7, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -1,626 -> final -37,310); days 15-22 drivers: sales_rev -24,138, work_turns -183, feed_hour +0.89, reversals +7. Hands 14 vs 14, animals 11 vs 11, plants 57 vs 85 |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `db3b23dc5179` | H32 | paired | **+1,034** | 0.8 | 10-10 | -26,253 | +2,217 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→19, wheat_cap 22→18, labor_reserve_buffer 92→59, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→91, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -5,180 -> final -20,540); days 21-28 drivers: sales_rev -26,416, work_turns -171, weeds_new +4, idle_turns +18. Hands 7 vs 9, animals 8 vs 11, plants 23 vs 33. |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |
| `ffbf75678458` | M2 | paired | **+59** | 0.1 | 10-10 | -27,551 | +2,170 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 22 (gap -4,389 -> final -18,581); days 20-27 drivers: sales_rev -21,759, work_turns -185, weeds_new +2, reversals +5. Hands 11 vs 11, animals 8 vs 11, plants 42 vs 47. |
| `71af3ce6e1eb` | queue | mutate | **-176** | -0.2 | 9-11 | -23,259 | +1,942 | melon_floor 0→150, load_per_hand 20→19, open_melons 8→10, max_animals 17→18, wheat_water_tier 0→1, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→16, SPREAD_W 1.25→1.0 |  | cand falls behind C1 from day 20 (gap -2,908 -> final -21,056); days 18-25 drivers: sales_rev -15,990, work_turns -147, feed_hour +0.99, water_hour +0.83. Hands 12 vs 13, animals 11 vs 11, plants 52 v |
| `a82c355f4ada` | queue | mutate | **-304** | -0.3 | 13-7 | -26,016 | +1,642 | melon_floor 0→150, load_per_hand 20→21, open_melons 8→10, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 5→3, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,723 -> final -7,677); days 14-21 drivers: sales_rev -17,098, work_turns -288, weeds_new +1. Hands 6 vs 14, animals 7 vs 11, plants 66 vs 84. |
| `af8e5e34dea8` | queue | mutate | **-488** | -0.5 | 7-13 | -22,576 | +1,881 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, wheat_water_tier 0→1, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_W 1.25→1.0 |  | cand falls behind C1 from day 20 (gap -2,908 -> final -21,009); days 18-25 drivers: sales_rev -15,157, work_turns -147, feed_hour +0.99, water_hour +0.83. Hands 12 vs 13, animals 11 vs 11, plants 52 v |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `b78610c183a0` | wide | crossover | +4,886 | 2.9 | 8-2 | -25,073 | held_fail | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `bfe4bb8d3609` | v312 | migrate | +4,008 | 1.6 | 7-3 | -21,783 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_sell_price 30→29, labor_reserve_buffer 92→95, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `57c65535c63e` | M2 | paired | +3,091 | 1.6 | 6-4 | -28,471 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |
| `d4c21300a453` | wide | mutate | +3,069 | 1.7 | 7-3 | -23,207 | alive | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12, FERT_RADIUS 3→1 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `89822c12eba2` | wide | crossover | +3,032 | 1.6 | 8-2 | -22,099 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→4, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `71f26bab2993` | v312 | mutate | +2,962 | 1.6 | 7-3 | -24,707 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, open_wheat 7→6, demand_share 0.55→0.45, max_animals 17→19, wheat_water_tier 0→1, setup_capital_share 0.25→0.45, labor_reserve_buffer 92→102, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→27, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4 |
| `db61805ecfa9` | M2 | mutate | +2,910 | 2.2 | 8-2 | -22,620 | held_fail | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |
| `cb1783cdaf15` | queue | archive_crossover:crossover_g000025_20260910-101244_1 | +2,759 | 1.7 | 7-3 | -25,472 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ef9bb31c7a35` | c1 | mutate | +2,574 | 1.6 | 8-2 | -24,298 | alive | melon_floor 0→150, open_melons 8→10, open_wheat 7→3, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→102 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=38
- M2: best +3,091 (`57c65535c63e`), n=30
- c1: best +2,683 (`5fd05605827b`), n=51
- queue: best +4,836 (`7ec902ce836b`), n=90
- v312: best +4,008 (`bfe4bb8d3609`), n=44
- wide: best +4,886 (`b78610c183a0`), n=48

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +7,448 | 91 | 100 | 26 | 289 | 10.38 | 91: +839 (n=2), 84: +336 (n=2), 74: -125 (n=2), 102: -375 (n=14), 115: -403 (n=3), 85: -1,124 (n=9), 83: -1,174 (n=3), 90: -1,291 (n=2), 100: -1,423 (n=235), 71: -2,386 (n=2), 114: -3,075 (n=2), 92: -3,202 (n=7), 110: -3,785 (n=4), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,196 | 27 | 38 | 17 | 298 | 3.74 | 27: +744 (n=3), 39: +287 (n=28), 33: -996 (n=2), 35: -1,032 (n=41), 32: -1,047 (n=6), 34: -1,458 (n=101), 28: -1,927 (n=2), 38: -1,987 (n=94), 43: -3,008 (n=10), 41: -3,113 (n=2), 25: -3,320 (n=2), 42: -4,467 (n=2), 46: -5,356 (n=3), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,926 | 13 | 14 | 7 | 301 | 3.72 | 13: +129 (n=26), 12: -788 (n=44), 14: -1,698 (n=203), 11: -2,042 (n=6), 15: -2,476 (n=13), 16: -3,013 (n=5), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +5,882 | 12 | 22 | 11 | 301 | 5.54 | 12: +1,958 (n=6), 13: -778 (n=31), 25: -1,358 (n=41), 21: -1,542 (n=2), 22: -1,542 (n=179), 19: -1,650 (n=2), 20: -2,006 (n=10), 17: -2,111 (n=3), 18: -2,483 (n=16), 24: -3,679 (n=5), 23: -3,923 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,540 | 6 | 8 | 8 | 301 | 2.46 | 6: -149 (n=3), 10: -1,049 (n=127), 9: -1,388 (n=14), 11: -1,700 (n=18), 8: -1,830 (n=130), 7: -2,008 (n=3), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,339 | 2 | 3 | 3 | 301 | 1.45 | 2: +9 (n=39), 3: -1,519 (n=246), 4: -5,330 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,172 | 2 | 2 | 4 | 301 | 2.48 | 2: -1,299 (n=262), 1: -2,693 (n=33), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +4,729 | 6 | 7 | 8 | 301 | 4.71 | 6: -4 (n=14), 9: -709 (n=5), 3: -728 (n=17), 4: -840 (n=40), 7: -1,731 (n=215), 10: -1,893 (n=3), 5: -3,711 (n=2), 8: -4,733 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,645 | 19 | 20 | 9 | 300 | 4.09 | 19: -1,093 (n=52), 20: -1,343 (n=191), 18: -1,656 (n=11), 22: -1,696 (n=4), 17: -2,506 (n=3), 21: -2,616 (n=29), 23: -2,740 (n=8), 24: -5,738 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +4,335 | 19 | 17 | 8 | 300 | 4.34 | 19: +999 (n=4), 18: -744 (n=13), 14: -992 (n=3), 17: -1,396 (n=229), 15: -1,754 (n=23), 16: -1,758 (n=5), 20: -3,336 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +4,104 | frontier | frontier | 2 | 301 | 0.86 | frontier: -1,237 (n=280), v312: -5,341 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +3,954 | 2 | 2 | 3 | 301 | 1.83 | 2: -1,318 (n=284), 1: -4,676 (n=9), 3: -5,272 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +3,931 | 58 | 92 | 28 | 289 | 10.13 | 58: +148 (n=14), 124: +10 (n=6), 121: +6 (n=2), 95: -37 (n=4), 107: -755 (n=7), 102: -803 (n=4), 88: -1,408 (n=2), 59: -1,461 (n=3), 16: -1,522 (n=2), 92: -1,593 (n=201), 73: -1,731 (n=2), 11: -1,812 (n=26), 94: -2,049 (n=2), 0: -2,153 (n=2), 150: -2,267 (n=10), 76: -3,783 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,566 | 0.65 | 0.55 | 9 | 299 | 3.28 | 0.65: -474 (n=21), 0.6: -756 (n=21), 0.45: -871 (n=27), 0.55: -1,507 (n=183), 0.5: -2,359 (n=37), 0.75: -2,732 (n=2), 0.3: -4,040 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,426 | 0.45 | 0.25 | 10 | 300 | 5.45 | 0.45: -1,041 (n=16), 0.4: -1,134 (n=30), 0.25: -1,280 (n=215), 0.2: -1,513 (n=5), 0.15: -1,761 (n=4), 0.3: -2,029 (n=3), 0.5: -3,672 (n=3), 0.35: -4,190 (n=22), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +3,265 | 31 | 30 | 11 | 299 | 3.55 | 31: -1,149 (n=3), 30: -1,358 (n=151), 25: -1,405 (n=93), 34: -1,432 (n=3), 26: -1,853 (n=26), 28: -1,913 (n=7), 29: -2,014 (n=9), 36: -2,913 (n=4), 27: -4,415 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,252 | 8 | 5 | 8 | 300 | 4.27 | 8: -599 (n=5), 4: -727 (n=11), 7: -863 (n=13), 3: -1,487 (n=35), 5: -1,550 (n=226), 0: -3,055 (n=6), 6: -3,851 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,238 | 16 | 17 | 8 | 300 | 2.69 | 16: -8 (n=5), 18: -1,097 (n=12), 19: -1,423 (n=100), 17: -1,506 (n=158), 22: -1,587 (n=13), 20: -3,144 (n=3), 14: -3,246 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| feed_spare_poor | +2,350 | 1 | 0 | 4 | 301 | 2.1 | 1: -940 (n=50), 0: -1,532 (n=233), 3: -2,534 (n=6), 2: -3,290 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +2,341 | 1 | 0 | 3 | 301 | 1.88 | 1: -156 (n=9), 0: -1,556 (n=289), 2: -2,497 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +4,886 (n=29)
- (8, 3, 4): +4,836 (n=19)
- (16, 3, 6): +4,008 (n=2)
- (10, 3, 5): +3,091 (n=12)
- (14, 3, 6): +3,066 (n=6)
- (7, 3, 3): +3,032 (n=15)
- (9, 3, 4): +2,962 (n=21)
- (9, 3, 3): +2,910 (n=5)
- (11, 3, 5): +2,663 (n=13)
- (11, 3, 6): +2,574 (n=12)
- (9, 3, 5): +2,565 (n=8)
- (6, 3, 3): +2,391 (n=6)
- (8, 3, 5): +2,298 (n=11)
- (6, 3, 5): +2,260 (n=2)
- (15, 3, 6): +2,143 (n=5)

_Generated 2026-09-10 10:14. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 133 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=133); harvest_min=1–3 (n=133); wheat_tiles=0–5 (n=133); wheat_stock=0–19 (n=133); min_hands=3–6 (n=133); load_per_hand=12–26 (n=133); geese=0–2 (n=133); open_melons=4–12 (n=133)
- **Evidence:** 133 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 10:14. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._