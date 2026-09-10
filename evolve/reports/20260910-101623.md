# Evolution run 20260910-101623

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.24 h · candidates evaluated this run: 26 · games 2,072 (8,733/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 1 | 2 |
| dead_pattern | 5 | 10 |
| dead_smoke | 3 | 24 |
| alive | 16 | 1728 |
| held_fail | 1 | 308 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 336 · held-out evaluated: 16 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `db61805ecfa9` | M2 | mutate | **+3,427** | 3.2 | 17-3 | -28,163 | +2,910 | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 20 (gap -3,060 -> final -43,282); days 18-25 drivers: sales_rev -43,924, work_turns -118, water_hour +0.9. Hands 11 vs 13, animals 9 vs 11, plants 60 vs 62. |
| `b78610c183a0` | wide | crossover | **+3,072** | 2.0 | 17-3 | -26,162 | +4,886 | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,254 -> final -9,989); days 15-22 drivers: sales_rev -11,173, work_turns -225. Hands 13 vs 14, animals 7 vs 11, plants 67 vs 85. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `935becadf7d7` | queue | archive_crossover:crossover_g000025_20260910-094825_0 | **+1,563** | 1.6 | 14-6 | -25,481 | +2,260 | open_melons 8→10, open_wheat 7→6, early_hire_days 5→7, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -1,626 -> final -37,310); days 15-22 drivers: sales_rev -24,138, work_turns -183, feed_hour +0.89, reversals +7. Hands 14 vs 14, animals 11 vs 11, plants 57 vs 85 |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `db3b23dc5179` | H32 | paired | **+1,034** | 0.8 | 10-10 | -26,253 | +2,217 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→19, wheat_cap 22→18, labor_reserve_buffer 92→59, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→91, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -5,180 -> final -20,540); days 21-28 drivers: sales_rev -26,416, work_turns -171, weeds_new +4, idle_turns +18. Hands 7 vs 9, animals 8 vs 11, plants 23 vs 33. |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `cfdd30201794` | queue | mutate | **+489** | 0.5 | 12-8 | -24,095 | +3,486 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→40 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,052 -> final -14,771); days 14-21 drivers: sales_rev -18,016, work_turns -278, idle_turns +8, travel_per_task +0.18. Hands 10 vs 14, animals 7 vs 11, plants 68 |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |
| `ffbf75678458` | M2 | paired | **+59** | 0.1 | 10-10 | -27,551 | +2,170 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 22 (gap -4,389 -> final -18,581); days 20-27 drivers: sales_rev -21,759, work_turns -185, weeds_new +2, reversals +5. Hands 11 vs 11, animals 8 vs 11, plants 42 vs 47. |
| `71af3ce6e1eb` | queue | mutate | **-176** | -0.2 | 9-11 | -23,259 | +1,942 | melon_floor 0→150, load_per_hand 20→19, open_melons 8→10, max_animals 17→18, wheat_water_tier 0→1, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→16, SPREAD_W 1.25→1.0 |  | cand falls behind C1 from day 20 (gap -2,908 -> final -21,056); days 18-25 drivers: sales_rev -15,990, work_turns -147, feed_hour +0.99, water_hour +0.83. Hands 12 vs 13, animals 11 vs 11, plants 52 v |
| `a82c355f4ada` | queue | mutate | **-304** | -0.3 | 13-7 | -26,016 | +1,642 | melon_floor 0→150, load_per_hand 20→21, open_melons 8→10, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 5→3, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,723 -> final -7,677); days 14-21 drivers: sales_rev -17,098, work_turns -288, weeds_new +1. Hands 6 vs 14, animals 7 vs 11, plants 66 vs 84. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `b78610c183a0` | wide | crossover | +4,886 | 2.9 | 8-2 | -25,073 | held_fail | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `bfe4bb8d3609` | v312 | migrate | +4,008 | 1.6 | 7-3 | -21,783 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_sell_price 30→29, labor_reserve_buffer 92→95, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `aade4d85f6fe` | queue | mutate | +3,787 | 3.2 | 8-2 | -21,617 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |
| `cfdd30201794` | queue | mutate | +3,486 | 4.2 | 10-0 | -20,077 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→40 · blocks: hiring |
| `57c65535c63e` | M2 | paired | +3,091 | 1.6 | 6-4 | -28,471 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |
| `d4c21300a453` | wide | mutate | +3,069 | 1.7 | 7-3 | -23,207 | alive | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12, FERT_RADIUS 3→1 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `89822c12eba2` | wide | crossover | +3,032 | 1.6 | 8-2 | -22,099 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→4, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `71f26bab2993` | v312 | mutate | +2,962 | 1.6 | 7-3 | -24,707 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, open_wheat 7→6, demand_share 0.55→0.45, max_animals 17→19, wheat_water_tier 0→1, setup_capital_share 0.25→0.45, labor_reserve_buffer 92→102, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→27, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4 |
| `db61805ecfa9` | M2 | mutate | +2,910 | 2.2 | 8-2 | -22,620 | held_fail | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |
| `cb1783cdaf15` | queue | archive_crossover:crossover_g000025_20260910-101244_1 | +2,759 | 1.7 | 7-3 | -25,472 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `68ec0d9dd54c` | queue | archive_crossover:crossover_g000025_20260910-102949_0 | +2,682 | 1.6 | 8-2 | -24,985 | alive | melon_floor 0→100, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, fert_keep 0→1, demand_share 0.55→0.6, wheat_sell_price 30→25, wheat_hold_days 0→1, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, FERT_RADIUS 3→1 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=44
- M2: best +3,091 (`57c65535c63e`), n=34
- c1: best +2,683 (`5fd05605827b`), n=56
- queue: best +4,836 (`7ec902ce836b`), n=102
- v312: best +4,008 (`bfe4bb8d3609`), n=46
- wide: best +4,886 (`b78610c183a0`), n=54

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +7,448 | 91 | 100 | 29 | 322 | 11.2 | 91: +839 (n=2), 84: +336 (n=2), 90: +33 (n=3), 74: -125 (n=2), 102: -241 (n=15), 115: -403 (n=3), 85: -1,041 (n=10), 83: -1,174 (n=3), 100: -1,420 (n=262), 82: -2,202 (n=2), 71: -2,386 (n=2), 92: -2,833 (n=8), 114: -3,075 (n=2), 110: -3,785 (n=4), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,939 | 40 | 38 | 18 | 333 | 4.0 | 40: +1,486 (n=3), 39: +453 (n=34), 27: -42 (n=4), 32: -663 (n=7), 35: -944 (n=45), 33: -996 (n=2), 34: -1,636 (n=111), 41: -1,895 (n=3), 28: -1,927 (n=2), 38: -1,955 (n=102), 42: -2,924 (n=3), 43: -3,008 (n=10), 25: -3,320 (n=2), 46: -5,356 (n=3), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,242 | 95 | 92 | 30 | 327 | 13.13 | 95: +507 (n=5), 58: +247 (n=15), 124: +10 (n=6), 121: -131 (n=4), 107: -755 (n=7), 106: -780 (n=2), 102: -811 (n=5), 118: -1,081 (n=2), 88: -1,408 (n=2), 59: -1,461 (n=3), 92: -1,497 (n=220), 16: -1,522 (n=2), 73: -1,731 (n=2), 72: -1,999 (n=3), 11: -2,007 (n=29), 94: -2,049 (n=2), 0: -2,153 (n=2), 150: -2,267 (n=10), 76: -3,783 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,960 | 13 | 14 | 7 | 336 | 3.65 | 13: +164 (n=31), 12: -795 (n=48), 14: -1,636 (n=223), 11: -2,042 (n=6), 15: -2,603 (n=18), 16: -2,663 (n=6), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,540 | 6 | 8 | 9 | 336 | 2.86 | 6: -149 (n=3), 10: -1,054 (n=140), 7: -1,291 (n=6), 9: -1,363 (n=16), 11: -1,626 (n=19), 8: -1,747 (n=144), 14: -2,589 (n=2), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,206 | 2 | 2 | 4 | 336 | 2.49 | 2: -1,265 (n=293), 1: -2,550 (n=36), 0: -4,123 (n=5), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +5,059 | 19 | 20 | 10 | 334 | 4.08 | 19: -950 (n=56), 20: -1,286 (n=212), 22: -1,465 (n=6), 17: -1,646 (n=4), 18: -1,958 (n=12), 21: -2,566 (n=33), 23: -2,740 (n=8), 24: -6,009 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +4,943 | 2 | 3 | 3 | 336 | 1.38 | 2: -123 (n=52), 3: -1,512 (n=267), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +4,749 | 12 | 22 | 13 | 335 | 5.99 | 12: +826 (n=9), 5: -125 (n=2), 13: -460 (n=36), 25: -1,281 (n=45), 21: -1,542 (n=2), 22: -1,560 (n=195), 20: -2,017 (n=11), 17: -2,111 (n=3), 18: -2,237 (n=18), 19: -2,721 (n=3), 24: -3,679 (n=5), 23: -3,923 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +4,365 | 6 | 7 | 8 | 336 | 4.67 | 6: -368 (n=17), 4: -541 (n=46), 3: -728 (n=17), 9: -1,070 (n=8), 7: -1,711 (n=238), 10: -1,893 (n=3), 5: -3,711 (n=2), 8: -4,733 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +4,029 | frontier | frontier | 2 | 336 | 0.87 | frontier: -1,213 (n=314), v312: -5,242 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +4,018 | 0.65 | 0.55 | 10 | 334 | 3.81 | 0.65: -85 (n=25), 0.6: -594 (n=25), 0.45: -830 (n=30), 0.55: -1,500 (n=201), 0.8: -2,202 (n=2), 0.5: -2,252 (n=39), 0.75: -2,732 (n=2), 0.3: -4,103 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,003 | 2 | 2 | 3 | 336 | 1.81 | 2: -1,269 (n=315), 1: -4,165 (n=13), 3: -5,272 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +3,617 | 9 | 0 | 9 | 333 | 4.15 | 9: -313 (n=5), 0: -1,431 (n=286), 7: -1,463 (n=2), 1: -1,595 (n=2), 4: -1,793 (n=36), 6: -3,930 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,438 | 0.45 | 0.25 | 10 | 335 | 5.42 | 0.45: -1,029 (n=17), 0.3: -1,235 (n=4), 0.25: -1,246 (n=239), 0.2: -1,303 (n=7), 0.4: -1,327 (n=36), 0.15: -1,761 (n=4), 0.5: -2,713 (n=4), 0.35: -4,190 (n=22), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,408 | 4 | 5 | 8 | 335 | 4.35 | 4: -443 (n=12), 7: -1,027 (n=14), 8: -1,168 (n=7), 3: -1,414 (n=36), 5: -1,497 (n=256), 0: -3,055 (n=6), 6: -3,851 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +3,359 | 19 | 17 | 8 | 336 | 4.93 | 19: +228 (n=7), 18: -842 (n=16), 14: -992 (n=3), 17: -1,362 (n=249), 15: -1,670 (n=27), 16: -1,758 (n=5), 13: -1,877 (n=2), 20: -3,131 (n=27) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,212 | 16 | 17 | 9 | 334 | 2.69 | 16: -8 (n=5), 18: -1,001 (n=13), 17: -1,354 (n=176), 19: -1,507 (n=113), 22: -1,920 (n=14), 20: -3,144 (n=3), 14: -3,221 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +2,452 | 31 | 30 | 11 | 334 | 3.58 | 31: -903 (n=4), 30: -1,217 (n=170), 34: -1,432 (n=3), 25: -1,500 (n=104), 26: -1,853 (n=26), 28: -1,913 (n=7), 29: -2,014 (n=9), 36: -2,913 (n=4), 27: -3,355 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| feed_spare_poor | +2,255 | 1 | 0 | 4 | 336 | 2.01 | 1: -773 (n=63), 0: -1,552 (n=253), 3: -2,214 (n=7), 2: -3,028 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +4,886 (n=33)
- (8, 3, 4): +4,836 (n=21)
- (16, 3, 6): +4,008 (n=2)
- (7, 3, 3): +3,486 (n=16)
- (10, 3, 5): +3,091 (n=14)
- (14, 3, 6): +3,066 (n=7)
- (9, 3, 4): +2,962 (n=23)
- (9, 3, 3): +2,910 (n=5)
- (11, 3, 5): +2,663 (n=14)
- (11, 3, 6): +2,574 (n=14)
- (9, 3, 5): +2,565 (n=9)
- (6, 3, 3): +2,391 (n=7)
- (8, 3, 5): +2,386 (n=12)
- (6, 3, 5): +2,260 (n=2)
- (15, 3, 6): +2,143 (n=6)

_Generated 2026-09-10 10:30. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 149 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=149); harvest_min=1–3 (n=149); wheat_tiles=0–5 (n=149); wheat_stock=0–19 (n=149); min_hands=3–6 (n=149); load_per_hand=12–26 (n=149); geese=0–2 (n=149); open_melons=4–12 (n=149)
- **Evidence:** 149 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 10:30. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._