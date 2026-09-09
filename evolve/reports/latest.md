# Evolution run 20260909-072436

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1239 · games 23,340 (11,662/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 443 | 886 |
| dead_pattern | 199 | 398 |
| dead_smoke | 165 | 1320 |
| alive | 432 | 20736 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 15703 · held-out evaluated: 0 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | -37,097 | -9.3 | 0-10 | -27,047 | — | — | —-— |

## Held-out results (the only numbers that count)

None reached held-out this run.

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `0c3989f7d742` | H32 | crossover | -15,269 | -3.2 | 2-8 | -16,318 | alive | melon_floor 150→0, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, labor_reserve_buffer 50→92, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25, SPREAD_CAP 5→3 |
| `52b3d5cc236e` | v312 | crossover | -15,275 | -3.0 | 3-7 | -28,470 | alive | harvest_min 2→3, geese 0→1, open_melons 8→10, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→45, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 |
| `fe4745b56024` | queue | archive_crossover:crossover_g000675_20260905-224724_0 | -15,412 | -3.3 | 2-8 | -17,273 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `d62b0acfe68b` | queue | archive_crossover:crossover_g001100_20260907-023009_1 | -15,495 | -2.9 | 3-7 | -15,324 | alive | open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, setup_capital_share 0.25→0.2, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `9d926b677e93` | H32 | mutate | -15,512 | -3.2 | 2-8 | -16,318 | alive | melon_floor 150→0, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, labor_reserve_buffer 50→66, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→39, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25, SPREAD_CAP 5→3 |
| `a3436012d4f9` | queue | archive_crossover:crossover_g000725_20260906-214654_0 | -15,590 | -3.3 | 2-8 | -16,712 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `667332b39bf5` | queue | archive_crossover:crossover_g000850_20260905-205857_1 | -15,738 | -3.0 | 3-7 | -27,827 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `97e03be128cb` | queue | archive_crossover:crossover_g000400_20260906-211828_1 | -15,791 | -3.5 | 2-8 | -16,760 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `7056bf4454ac` | queue | archive_crossover:crossover_g000600_20260907-014214_1 | -15,811 | -3.0 | 3-7 | -15,804 | alive | harvest_min 2→1, open_melons 8→10, early_hire_days 5→8, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `2286322870c4` | v312 | mutate | -15,854 | -3.0 | 3-7 | -14,497 | alive | harvest_min 2→3, open_melons 8→10, early_hire_days 5→8, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→42, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5 |
| `a442a9ceb68e` | queue | archive_crossover:crossover_g000075_20260906-225544_1 | -15,885 | -3.6 | 2-8 | -17,122 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, SPREAD_W 1.0→1.25 |
| `5b63d512ad81` | queue | archive_crossover:crossover_g000775_20260906-215507_0 | -15,896 | -3.3 | 2-8 | -15,996 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `081b43704bb8` | queue | archive_crossover:crossover_g000125_20260905-215729_0 | -15,916 | -3.1 | 2-8 | -28,354 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→7, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `165447af42cc` | queue | mutate | -15,936 | -3.5 | 2-8 | -16,892 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→0, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3 |
| `512e53fe15bc` | wide | paired | -16,047 | -3.7 | 1-9 | -15,964 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→37, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |

## Islands (best dev margin, population size)

- H32: best -15,269 (`0c3989f7d742`), n=1979
- M2: best -16,461 (`0c25e1226b27`), n=2049
- c1: best -16,310 (`23734cef4da1`), n=2829
- queue: best -15,412 (`fe4745b56024`), n=3769
- v312: best -15,275 (`52b3d5cc236e`), n=2609
- wide: best -16,047 (`512e53fe15bc`), n=2468

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,168 | 120 | 50 | 145 | 15694 | 66.04 | 120: -22,600 (n=9), 118: -25,349 (n=2), 19: -27,891 (n=15), 141: -28,023 (n=6), 5: -28,740 (n=53), 35: -28,917 (n=13), 143: -28,964 (n=3), 8: -29,345 (n=5), 112: -29,479 (n=14), 106: -29,495 (n=24), 27: -29,531 (n=36), 108: -29,670 (n=7), 89: -30,005 (n=30), 18: -30,053 (n=983), 92: -30,071 (n=409), 58: -30,090 (n=130), 80: -30,353 (n=16), 63: -30,358 (n=259), 26: -30,432 (n=8), 49: -30,485 (n=86), 48: -30,645 (n=541), 74: -30,654 (n=288), 71: -30,666 (n=30), 56: -30,810 (n=16), 50: -30,835 (n=7736), 65: -30,848 (n=143), 61: -30,861 (n=108), 97: -30,886 (n=33), 150: -30,959 (n=214), 33: -31,120 (n=23), 42: -31,307 (n=831), 51: -31,357 (n=19), 66: -31,375 (n=289), 40: -31,414 (n=101), 70: -31,427 (n=54), 60: -31,435 (n=30), 86: -31,454 (n=10), 85: -31,513 (n=11), 14: -31,618 (n=25), 25: -31,648 (n=9), 45: -31,663 (n=119), 72: -31,710 (n=11), 9: -31,785 (n=18), 57: -31,948 (n=84), 62: -31,963 (n=19), 94: -32,037 (n=21), 36: -32,121 (n=120), 113: -32,147 (n=14), 73: -32,194 (n=19), 53: -32,264 (n=57), 110: -32,277 (n=4), 39: -32,284 (n=56), 30: -32,396 (n=37), 103: -32,462 (n=9), 115: -32,512 (n=8), 84: -32,610 (n=15), 59: -32,612 (n=22), 54: -32,622 (n=26), 96: -32,630 (n=8), 104: -32,639 (n=5), 41: -32,776 (n=48), 55: -32,837 (n=633), 44: -32,839 (n=25), 109: -32,844 (n=3), 98: -32,926 (n=20), 69: -32,939 (n=26), 4: -33,088 (n=38), 68: -33,109 (n=18), 88: -33,112 (n=12), 38: -33,155 (n=19), 144: -33,156 (n=5), 31: -33,271 (n=15), 93: -33,297 (n=10), 76: -33,355 (n=15), 0: -33,383 (n=213), 95: -33,449 (n=5), 13: -33,499 (n=7), 6: -33,522 (n=11), 83: -33,572 (n=110), 52: -33,573 (n=20), 43: -33,575 (n=20), 21: -33,604 (n=12), 1: -33,664 (n=8), 119: -33,699 (n=3), 87: -33,711 (n=14), 28: -33,719 (n=20), 81: -33,724 (n=28), 2: -33,749 (n=3), 24: -33,760 (n=22), 90: -33,822 (n=7), 22: -33,894 (n=17), 32: -33,992 (n=9), 20: -34,074 (n=8), 111: -34,111 (n=8), 102: -34,126 (n=5), 17: -34,168 (n=8), 82: -34,185 (n=47), 10: -34,204 (n=14), 78: -34,276 (n=13), 11: -34,302 (n=16), 99: -34,384 (n=74), 140: -34,453 (n=4), 134: -34,464 (n=2), 15: -34,489 (n=10), 37: -34,598 (n=14), 46: -34,798 (n=36), 16: -34,876 (n=17), 64: -34,931 (n=21), 107: -34,965 (n=5), 7: -34,968 (n=8), 101: -34,988 (n=12), 136: -35,029 (n=45), 79: -35,034 (n=16), 47: -35,037 (n=24), 77: -35,202 (n=235), 34: -35,289 (n=65), 100: -35,405 (n=52), 23: -35,508 (n=15), 12: -35,769 (n=12), 129: -35,788 (n=84), 91: -35,887 (n=10), 128: -36,508 (n=3), 3: -36,531 (n=5), 105: -36,563 (n=3), 75: -36,596 (n=11), 117: -36,604 (n=2), 145: -36,990 (n=7), 67: -37,049 (n=18), 114: -37,341 (n=4), 127: -38,268 (n=2), 29: -38,584 (n=41), 131: -38,847 (n=2), 132: -39,931 (n=2), 124: -39,994 (n=3), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,083 | 26 | 30 | 25 | 15702 | 10.68 | 26: -30,670 (n=547), 25: -30,792 (n=7639), 30: -30,982 (n=5098), 31: -31,593 (n=134), 29: -32,248 (n=129), 27: -32,363 (n=240), 28: -33,515 (n=1250), 32: -34,073 (n=148), 41: -34,307 (n=3), 35: -34,814 (n=180), 33: -35,503 (n=129), 39: -35,574 (n=12), 37: -35,771 (n=26), 38: -35,963 (n=23), 34: -36,180 (n=63), 36: -36,945 (n=39), 42: -36,946 (n=4), 46: -38,521 (n=3), 40: -39,180 (n=12), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,272 | 1 | 0 | 34 | 15700 | 24.96 | 1: -30,254 (n=1149), 0: -31,068 (n=13150), 9: -31,118 (n=100), 22: -31,539 (n=2), 2: -32,368 (n=162), 4: -33,021 (n=103), 6: -33,070 (n=109), 8: -33,120 (n=88), 17: -34,084 (n=15), 19: -34,158 (n=6), 3: -34,373 (n=183), 11: -34,807 (n=67), 5: -34,947 (n=167), 16: -35,444 (n=14), 7: -35,491 (n=92), 12: -35,786 (n=35), 13: -35,879 (n=48), 14: -36,218 (n=23), 20: -36,357 (n=6), 28: -36,361 (n=2), 15: -36,507 (n=30), 18: -36,728 (n=20), 23: -36,978 (n=7), 24: -37,048 (n=7), 10: -37,276 (n=50), 39: -37,445 (n=11), 21: -37,766 (n=7), 40: -38,996 (n=10), 26: -40,268 (n=3), 29: -41,445 (n=30), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,835 | 3 | 3 | 4 | 15703 | 2.61 | 3: -30,793 (n=14170), 2: -35,776 (n=1092), 4: -36,413 (n=421), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 15703 | 62.71 | 61: -27,918 (n=2), 138: -27,990 (n=3), 80: -29,819 (n=255), 120: -29,850 (n=16), 130: -29,880 (n=14), 93: -30,021 (n=400), 85: -30,207 (n=96), 81: -30,227 (n=83), 91: -30,378 (n=92), 62: -30,511 (n=7), 86: -30,539 (n=790), 92: -30,693 (n=27), 100: -30,818 (n=9905), 123: -30,951 (n=48), 129: -31,008 (n=20), 114: -31,017 (n=27), 125: -31,090 (n=92), 115: -31,141 (n=34), 90: -31,162 (n=114), 113: -31,180 (n=20), 111: -31,233 (n=39), 78: -31,250 (n=111), 94: -31,336 (n=35), 55: -31,425 (n=4), 65: -31,427 (n=7), 141: -31,447 (n=3), 107: -31,458 (n=26), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,622 (n=115), 117: -31,636 (n=107), 67: -31,660 (n=9), 133: -31,740 (n=10), 103: -31,763 (n=30), 99: -31,813 (n=38), 109: -31,938 (n=39), 84: -31,944 (n=76), 132: -31,971 (n=11), 87: -32,013 (n=21), 95: -32,032 (n=40), 70: -32,127 (n=19), 149: -32,176 (n=3), 105: -32,215 (n=115), 50: -32,246 (n=83), 119: -32,280 (n=17), 53: -32,306 (n=5), 63: -32,321 (n=11), 102: -32,323 (n=44), 66: -32,337 (n=14), 71: -32,523 (n=21), 82: -32,550 (n=22), 57: -32,552 (n=6), 104: -32,552 (n=587), 110: -32,680 (n=25), 127: -32,823 (n=34), 128: -32,857 (n=28), 88: -33,015 (n=66), 122: -33,107 (n=37), 76: -33,119 (n=19), 97: -33,119 (n=55), 69: -33,122 (n=10), 112: -33,210 (n=213), 101: -33,396 (n=40), 68: -33,455 (n=11), 89: -33,477 (n=163), 98: -33,497 (n=51), 134: -33,531 (n=8), 135: -33,693 (n=474), 116: -33,853 (n=71), 96: -33,897 (n=43), 59: -33,898 (n=4), 126: -33,965 (n=26), 124: -34,105 (n=25), 74: -34,107 (n=34), 121: -34,131 (n=14), 136: -34,218 (n=7), 79: -34,475 (n=47), 75: -34,489 (n=59), 108: -34,512 (n=27), 143: -34,578 (n=12), 137: -34,596 (n=5), 144: -34,772 (n=2), 72: -34,832 (n=12), 106: -35,055 (n=44), 56: -35,056 (n=5), 150: -35,802 (n=172), 139: -36,068 (n=8), 131: -36,082 (n=14), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 77: -36,730 (n=25), 118: -36,824 (n=14), 58: -37,611 (n=6), 146: -37,838 (n=2), 73: -38,056 (n=12), 51: -38,207 (n=4), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,391 | 13 | 20 | 11 | 15703 | 4.78 | 13: -30,636 (n=38), 17: -30,908 (n=5191), 16: -30,943 (n=349), 14: -31,160 (n=122), 19: -31,281 (n=816), 18: -31,449 (n=771), 20: -31,536 (n=8257), 15: -32,178 (n=132), 11: -32,310 (n=3), 12: -34,105 (n=16), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,356 | 6 | 6 | 8 | 15703 | 6.13 | 6: -30,711 (n=14000), 5: -34,665 (n=691), 7: -36,494 (n=394), 4: -37,427 (n=397), 3: -37,744 (n=133), 8: -38,147 (n=61), 9: -40,522 (n=20), 10: -41,067 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,352 | 20 | 20 | 15 | 15703 | 7.56 | 20: -30,561 (n=8961), 19: -30,925 (n=4663), 18: -31,576 (n=361), 17: -34,338 (n=706), 16: -36,405 (n=144), 21: -36,573 (n=326), 15: -37,246 (n=69), 23: -37,518 (n=82), 22: -37,902 (n=174), 14: -38,242 (n=36), 26: -38,524 (n=40), 24: -39,180 (n=84), 25: -39,340 (n=21), 13: -39,593 (n=18), 12: -40,913 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +10,224 | 0.0 | 0.0 | 13 | 15703 | 10.29 | 0.0: -30,939 (n=13640), 0.1: -33,097 (n=1007), 0.2: -33,797 (n=603), 0.4: -34,082 (n=93), 0.3: -34,213 (n=185), 0.5: -34,608 (n=57), 1.1: -34,978 (n=7), 0.7: -35,656 (n=18), 0.6: -37,045 (n=47), 0.9: -37,320 (n=6), 1.0: -37,756 (n=24), 1.2: -39,081 (n=9), 0.8: -41,164 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,211 | 7 | 7 | 8 | 15703 | 6.12 | 7: -30,653 (n=13975), 6: -36,391 (n=870), 5: -36,419 (n=70), 8: -36,593 (n=508), 10: -36,667 (n=121), 9: -37,133 (n=101), 4: -37,927 (n=49), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,090 | 10 | 8 | 11 | 15703 | 8.32 | 10: -30,685 (n=13309), 7: -32,519 (n=483), 8: -34,695 (n=950), 9: -35,036 (n=550), 6: -35,352 (n=178), 5: -36,429 (n=25), 12: -37,789 (n=51), 4: -38,022 (n=25), 11: -38,355 (n=68), 14: -39,816 (n=30), 13: -40,774 (n=34) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,673 | 0 | 0 | 9 | 15703 | 7.17 | 0: -30,985 (n=14255), 1: -34,036 (n=755), 2: -34,447 (n=316), 3: -34,898 (n=236), 7: -35,103 (n=7), 4: -35,509 (n=84), 5: -35,653 (n=22), 6: -37,663 (n=25), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,628 | 0.55 | 0.5 | 15 | 15703 | 7.35 | 0.55: -30,263 (n=8738), 0.65: -31,760 (n=1219), 0.5: -31,786 (n=3853), 0.75: -32,001 (n=111), 0.7: -32,267 (n=261), 0.6: -33,240 (n=375), 0.8: -34,400 (n=52), 0.45: -34,601 (n=481), 0.9: -35,286 (n=10), 0.4: -36,111 (n=176), 0.35: -36,141 (n=160), 0.85: -37,161 (n=14), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,891 (n=243) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,863 | 14 | 13 | 9 | 15703 | 4.33 | 14: -30,841 (n=2550), 13: -31,260 (n=9293), 11: -31,276 (n=788), 12: -31,385 (n=2123), 15: -31,640 (n=487), 10: -33,279 (n=126), 16: -33,582 (n=268), 9: -36,901 (n=48), 8: -39,704 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,660 | 6 | 18 | 21 | 15703 | 9.41 | 6: -29,969 (n=20), 21: -30,618 (n=2796), 14: -30,652 (n=24), 22: -30,801 (n=7785), 20: -31,315 (n=674), 23: -31,358 (n=708), 16: -32,177 (n=96), 17: -32,433 (n=771), 25: -32,525 (n=1259), 18: -32,911 (n=611), 24: -33,128 (n=429), 15: -33,312 (n=52), 12: -33,342 (n=11), 19: -33,443 (n=201), 13: -33,638 (n=26), 9: -33,993 (n=50), 10: -34,716 (n=67), 11: -36,049 (n=34), 5: -36,164 (n=62), 7: -36,543 (n=22), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,347 | 2 | 2 | 4 | 15703 | 2.84 | 2: -31,058 (n=15083), 1: -36,944 (n=504), 3: -38,375 (n=41), 0: -39,405 (n=75) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,262 | 13 | 12 | 11 | 15702 | 7.43 | 13: -30,758 (n=1245), 14: -31,155 (n=13234), 11: -32,568 (n=215), 12: -32,784 (n=663), 6: -34,388 (n=4), 9: -34,839 (n=28), 10: -35,243 (n=266), 7: -35,686 (n=10), 8: -36,793 (n=34), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,591 | frontier | frontier | 2 | 15703 | 0.92 | frontier: -30,984 (n=15038), v312: -38,575 (n=665) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,534 | 2 | 2 | 3 | 15703 | 1.83 | 2: -30,917 (n=14793), 1: -37,562 (n=857), 3: -38,451 (n=53) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,368 | 34 | 40 | 31 | 15702 | 7.5 | 34: -30,222 (n=286), 33: -30,413 (n=60), 38: -30,476 (n=3504), 49: -30,585 (n=443), 27: -30,617 (n=11), 43: -30,654 (n=4447), 44: -30,720 (n=432), 47: -30,850 (n=280), 30: -31,212 (n=67), 45: -31,223 (n=635), 37: -31,311 (n=583), 39: -31,490 (n=563), 32: -31,859 (n=60), 26: -32,103 (n=53), 46: -32,501 (n=107), 28: -32,715 (n=17), 40: -32,742 (n=2774), 29: -32,779 (n=17), 35: -32,856 (n=227), 31: -32,860 (n=43), 50: -32,878 (n=401), 42: -32,996 (n=224), 41: -33,027 (n=117), 36: -33,169 (n=192), 25: -33,175 (n=7), 20: -34,713 (n=43), 48: -34,734 (n=72), 24: -36,089 (n=25), 23: -36,212 (n=6), 22: -37,589 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2938)
- (9, 3, 6): -16,578 (n=1994)
- (10, 3, 6): -16,840 (n=2575)
- (8, 3, 5): -16,866 (n=275)
- (12, 4, 6): -17,058 (n=490)
- (8, 3, 6): -17,552 (n=778)
- (10, 4, 6): -17,975 (n=2256)
- (11, 3, 6): -18,175 (n=529)
- (11, 4, 6): -19,867 (n=538)
- (17, 3, 6): -20,013 (n=64)
- (8, 4, 6): -21,051 (n=735)
- (13, 3, 6): -21,783 (n=299)
- (13, 4, 6): -21,868 (n=205)
- (14, 3, 6): -21,872 (n=218)
- (8, 3, 4): -22,126 (n=82)

_Generated 2026-09-09 09:24. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 6342 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=6342); harvest_min=1–3 (n=6342); wheat_tiles=0–8 (n=6342); wheat_stock=0–40 (n=6342); min_hands=3–6 (n=6342); load_per_hand=12–26 (n=6342); geese=0–2 (n=6342); open_melons=4–14 (n=6342)
- **Evidence:** 6342 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 77 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=77); harvest_min=1–3 (n=77); wheat_tiles=0–2 (n=77); wheat_stock=0–4 (n=77); min_hands=3–6 (n=77); load_per_hand=15–22 (n=77); geese=0–2 (n=77); open_melons=7–13 (n=77)
- **Evidence:** 77 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 41 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=41); harvest_min=1–3 (n=41); wheat_tiles=0; wheat_stock=0–39 (n=41); min_hands=3–6 (n=41); load_per_hand=12–26 (n=41); geese=0–1 (n=41); open_melons=4–13 (n=41)
- **Evidence:** 41 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 28 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=28); harvest_min=1–3 (n=28); wheat_tiles=0–8 (n=28); wheat_stock=0–39 (n=28); min_hands=3–6 (n=28); load_per_hand=12–23 (n=28); geese=0–2 (n=28); open_melons=8–14 (n=28)
- **Evidence:** 28 candidates, multiple seeds. Confidence: high

### None (observed in 14 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=14); harvest_min=1–3 (n=14); wheat_tiles=0; wheat_stock=0–11 (n=14); min_hands=3–6 (n=14); load_per_hand=12–18 (n=14); geese=0–2 (n=14); open_melons=7–14 (n=14)
- **Evidence:** 14 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-09 09:24. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._