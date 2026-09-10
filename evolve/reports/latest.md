# Evolution run 20260910-081957

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 1.58 h · candidates evaluated this run: 153 · games 14,100 (8,938/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 10 | 20 |
| dead_pattern | 24 | 48 |
| dead_smoke | 16 | 128 |
| alive | 100 | 12800 |
| held_fail | 3 | 1104 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 259 · held-out evaluated: 11 · held-out PASS: 0

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
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `935becadf7d7` | queue | archive_crossover:crossover_g000025_20260910-094825_0 | **+1,563** | 1.6 | 14-6 | -25,481 | +2,260 | open_melons 8→10, open_wheat 7→6, early_hire_days 5→7, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -1,626 -> final -37,310); days 15-22 drivers: sales_rev -24,138, work_turns -183, feed_hour +0.89, reversals +7. Hands 14 vs 14, animals 11 vs 11, plants 57 vs 85 |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |
| `ffbf75678458` | M2 | paired | **+59** | 0.1 | 10-10 | -27,551 | +2,170 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 22 (gap -4,389 -> final -18,581); days 20-27 drivers: sales_rev -21,759, work_turns -185, weeds_new +2, reversals +5. Hands 11 vs 11, animals 8 vs 11, plants 42 vs 47. |
| `a82c355f4ada` | queue | mutate | **-304** | -0.3 | 13-7 | -26,016 | +1,642 | melon_floor 0→150, load_per_hand 20→21, open_melons 8→10, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 5→3, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,723 -> final -7,677); days 14-21 drivers: sales_rev -17,098, work_turns -288, weeds_new +1. Hands 6 vs 14, animals 7 vs 11, plants 66 vs 84. |
| `af8e5e34dea8` | queue | mutate | **-488** | -0.5 | 7-13 | -22,576 | +1,881 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, wheat_water_tier 0→1, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_W 1.25→1.0 |  | cand falls behind C1 from day 20 (gap -2,908 -> final -21,009); days 18-25 drivers: sales_rev -15,157, work_turns -147, feed_hour +0.99, water_hour +0.83. Hands 12 vs 13, animals 11 vs 11, plants 52 v |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `bfe4bb8d3609` | v312 | migrate | +4,008 | 1.6 | 7-3 | -21,783 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_sell_price 30→29, labor_reserve_buffer 92→95, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `57c65535c63e` | M2 | paired | +3,091 | 1.6 | 6-4 | -28,471 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `89822c12eba2` | wide | crossover | +3,032 | 1.6 | 8-2 | -22,099 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→4, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `db61805ecfa9` | M2 | mutate | +2,910 | 2.2 | 8-2 | -22,620 | held_fail | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ef9bb31c7a35` | c1 | mutate | +2,574 | 1.6 | 8-2 | -24,298 | alive | melon_floor 0→150, open_melons 8→10, open_wheat 7→3, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→102 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `961ab6fb4730` | M2 | mutate | +2,342 | 1.8 | 6-4 | -19,878 | alive | melon_floor 0→150, harvest_min 1→3, wheat_tiles 0→1, load_per_hand 20→21, open_melons 8→9, open_wheat 7→6, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |
| `935becadf7d7` | queue | archive_crossover:crossover_g000025_20260910-094825_0 | +2,260 | 3.4 | 9-1 | -24,511 | held_fail | open_melons 8→10, open_wheat 7→6, early_hire_days 5→7, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |
| `b05e5cf9d360` | queue | mutate | +2,216 | 2.0 | 9-1 | -24,767 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→32, MELON_PRICE_CUSHION 100→102 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=31
- M2: best +3,091 (`57c65535c63e`), n=24
- c1: best +2,683 (`5fd05605827b`), n=47
- queue: best +4,836 (`7ec902ce836b`), n=80
- v312: best +4,008 (`bfe4bb8d3609`), n=37
- wide: best +3,032 (`89822c12eba2`), n=40

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +7,372 | 102 | 100 | 21 | 250 | 9.08 | 102: +763 (n=10), 74: -125 (n=2), 85: -1,046 (n=7), 83: -1,174 (n=3), 90: -1,291 (n=2), 115: -1,408 (n=2), 100: -1,554 (n=210), 71: -2,386 (n=2), 114: -3,075 (n=2), 110: -3,429 (n=3), 92: -4,998 (n=5), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +6,831 | 12 | 22 | 11 | 258 | 5.2 | 12: +2,137 (n=3), 13: -651 (n=25), 25: -1,214 (n=32), 21: -1,542 (n=2), 22: -1,602 (n=160), 20: -1,868 (n=9), 18: -2,797 (n=15), 24: -3,679 (n=5), 17: -4,255 (n=2), 23: -4,694 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +5,661 | 39 | 38 | 14 | 256 | 2.61 | 39: +208 (n=25), 35: -840 (n=36), 33: -996 (n=2), 32: -1,047 (n=6), 34: -1,535 (n=84), 38: -2,179 (n=84), 43: -3,008 (n=10), 41: -3,113 (n=2), 42: -4,467 (n=2), 46: -5,356 (n=3), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,434 | 6 | 8 | 8 | 258 | 2.12 | 6: -255 (n=2), 9: -872 (n=12), 10: -1,209 (n=109), 11: -1,886 (n=14), 8: -1,898 (n=115), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,086 | 2 | 2 | 4 | 259 | 2.49 | 2: -1,385 (n=226), 1: -2,896 (n=27), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,830 | 19 | 20 | 9 | 258 | 4.15 | 19: -907 (n=44), 18: -1,350 (n=8), 20: -1,547 (n=166), 17: -2,506 (n=3), 21: -2,561 (n=25), 22: -2,577 (n=3), 23: -2,685 (n=7), 24: -5,738 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +4,722 | 2 | 3 | 3 | 259 | 1.55 | 2: -743 (n=25), 3: -1,479 (n=220), 4: -5,465 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +4,545 | 58 | 92 | 24 | 249 | 8.84 | 58: +763 (n=10), 121: +6 (n=2), 95: -37 (n=4), 124: -423 (n=5), 107: -755 (n=7), 88: -1,408 (n=2), 11: -1,662 (n=24), 92: -1,707 (n=175), 73: -1,731 (n=2), 94: -2,049 (n=2), 102: -2,058 (n=3), 150: -2,532 (n=9), 59: -3,300 (n=2), 76: -3,783 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,636 | 0.45 | 0.25 | 10 | 258 | 5.49 | 0.45: -831 (n=13), 0.25: -1,316 (n=186), 0.2: -1,513 (n=5), 0.4: -1,583 (n=23), 0.15: -2,387 (n=3), 0.3: -3,075 (n=2), 0.5: -3,672 (n=3), 0.35: -4,179 (n=21), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,594 | frontier | frontier | 2 | 259 | 0.87 | frontier: -1,388 (n=242), v312: -4,982 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,590 | 0.6 | 0.55 | 9 | 256 | 2.8 | 0.6: -450 (n=16), 0.65: -607 (n=20), 0.45: -721 (n=21), 0.55: -1,599 (n=162), 0.5: -2,901 (n=29), 0.3: -4,040 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +3,469 | 6 | 7 | 8 | 259 | 4.78 | 6: -242 (n=11), 9: -407 (n=3), 3: -578 (n=12), 4: -887 (n=38), 7: -1,871 (n=187), 10: -3,113 (n=2), 8: -3,116 (n=4), 5: -3,711 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +3,349 | 13 | 14 | 7 | 259 | 3.84 | 13: -170 (n=21), 12: -662 (n=36), 14: -1,827 (n=179), 11: -2,042 (n=6), 10: -2,730 (n=2), 15: -3,122 (n=11), 16: -3,519 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +3,299 | 1.3 | 1.4 | 7 | 259 | 3.84 | 1.3: -544 (n=40), 1.6: -1,530 (n=2), 1.4: -1,642 (n=179), 1.2: -2,264 (n=16), 1.0: -2,422 (n=9), 1.5: -3,280 (n=11), 1.1: -3,842 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +3,265 | 31 | 30 | 10 | 258 | 3.43 | 31: -1,149 (n=3), 34: -1,432 (n=3), 30: -1,460 (n=127), 25: -1,563 (n=80), 26: -1,843 (n=25), 28: -1,913 (n=7), 29: -1,999 (n=6), 36: -2,913 (n=4), 27: -4,415 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,261 | 8 | 5 | 8 | 258 | 4.32 | 8: -599 (n=5), 4: -933 (n=7), 3: -1,258 (n=31), 7: -1,469 (n=11), 5: -1,670 (n=196), 6: -2,961 (n=3), 0: -3,861 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,238 | 16 | 17 | 8 | 258 | 2.69 | 16: -8 (n=5), 19: -1,291 (n=84), 18: -1,319 (n=11), 17: -1,655 (n=136), 22: -2,803 (n=10), 20: -3,144 (n=3), 14: -3,246 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +3,068 | 14 | 14 | 5 | 259 | 3.19 | 14: -1,369 (n=217), 12: -1,660 (n=9), 11: -2,539 (n=4), 13: -3,271 (n=26), 10: -4,437 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +2,961 | 2 | 2 | 3 | 259 | 1.84 | 2: -1,464 (n=245), 1: -4,414 (n=7), 3: -4,425 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +2,950 | 3 | 0 | 4 | 259 | 2.68 | 3: -204 (n=2), 0: -1,566 (n=238), 1: -2,255 (n=14), 2: -3,154 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=17)
- (16, 3, 6): +4,008 (n=2)
- (7, 3, 4): +3,920 (n=24)
- (10, 3, 5): +3,091 (n=10)
- (14, 3, 6): +3,066 (n=6)
- (7, 3, 3): +3,032 (n=12)
- (9, 3, 3): +2,910 (n=3)
- (9, 3, 4): +2,683 (n=16)
- (11, 3, 5): +2,663 (n=13)
- (11, 3, 6): +2,574 (n=11)
- (9, 3, 5): +2,565 (n=6)
- (6, 3, 3): +2,293 (n=4)
- (6, 3, 5): +2,260 (n=2)
- (15, 3, 6): +2,143 (n=4)
- (10, 4, 6): +2,033 (n=19)

_Generated 2026-09-10 09:54. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 121 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=121); harvest_min=1–3 (n=121); wheat_tiles=0–5 (n=121); wheat_stock=0–19 (n=121); min_hands=3–6 (n=121); load_per_hand=12–25 (n=121); geese=0–1 (n=121); open_melons=4–12 (n=121)
- **Evidence:** 121 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 09:54. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._