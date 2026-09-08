# Evolution run 20260908-145001

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1279 · games 24,324 (12,153/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 427 | 854 |
| dead_pattern | 231 | 462 |
| dead_smoke | 170 | 1360 |
| alive | 451 | 21648 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 12224 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1442
- M2: best -16,461 (`0c25e1226b27`), n=1497
- c1: best -16,310 (`23734cef4da1`), n=2222
- queue: best -15,412 (`fe4745b56024`), n=3043
- v312: best -15,275 (`52b3d5cc236e`), n=2102
- wide: best -16,047 (`512e53fe15bc`), n=1918

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +21,602 | 120 | 50 | 143 | 12213 | 64.3 | 120: -18,328 (n=3), 141: -24,735 (n=4), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,428 (n=2), 35: -27,894 (n=8), 19: -28,045 (n=14), 112: -28,098 (n=12), 5: -28,572 (n=45), 72: -28,800 (n=7), 27: -29,195 (n=34), 56: -29,255 (n=13), 71: -29,378 (n=25), 92: -29,636 (n=301), 89: -29,662 (n=28), 58: -29,700 (n=87), 26: -29,760 (n=7), 18: -29,927 (n=688), 74: -29,997 (n=164), 49: -30,080 (n=67), 63: -30,228 (n=186), 61: -30,457 (n=92), 51: -30,565 (n=12), 50: -30,748 (n=6042), 48: -30,753 (n=495), 80: -30,851 (n=12), 65: -30,900 (n=120), 40: -31,175 (n=88), 60: -31,180 (n=28), 144: -31,182 (n=2), 42: -31,183 (n=695), 150: -31,273 (n=132), 85: -31,279 (n=9), 33: -31,322 (n=21), 45: -31,322 (n=107), 66: -31,405 (n=195), 9: -31,680 (n=12), 2: -31,685 (n=2), 14: -31,692 (n=17), 86: -31,717 (n=8), 57: -31,735 (n=82), 93: -31,753 (n=7), 96: -31,788 (n=6), 73: -31,853 (n=15), 36: -31,919 (n=99), 97: -32,013 (n=24), 70: -32,076 (n=30), 84: -32,162 (n=12), 39: -32,172 (n=50), 62: -32,220 (n=17), 59: -32,251 (n=15), 76: -32,272 (n=11), 110: -32,277 (n=4), 95: -32,333 (n=4), 25: -32,369 (n=7), 69: -32,403 (n=22), 115: -32,512 (n=8), 94: -32,527 (n=15), 103: -32,559 (n=8), 38: -32,804 (n=17), 52: -32,811 (n=12), 88: -32,815 (n=9), 109: -32,844 (n=3), 113: -32,956 (n=10), 21: -32,959 (n=7), 55: -33,140 (n=499), 31: -33,145 (n=12), 0: -33,249 (n=182), 41: -33,252 (n=35), 108: -33,264 (n=5), 104: -33,266 (n=4), 68: -33,293 (n=12), 83: -33,312 (n=94), 6: -33,331 (n=10), 119: -33,340 (n=2), 4: -33,399 (n=36), 78: -33,423 (n=9), 24: -33,425 (n=18), 111: -33,451 (n=7), 13: -33,499 (n=7), 23: -33,511 (n=11), 98: -33,608 (n=16), 43: -33,691 (n=18), 90: -33,822 (n=7), 22: -33,829 (n=14), 81: -33,835 (n=24), 30: -33,916 (n=15), 82: -34,131 (n=40), 136: -34,146 (n=34), 54: -34,180 (n=17), 44: -34,233 (n=20), 10: -34,299 (n=13), 102: -34,320 (n=4), 28: -34,350 (n=19), 1: -34,413 (n=5), 134: -34,464 (n=2), 99: -34,475 (n=69), 46: -34,622 (n=29), 15: -34,699 (n=8), 7: -34,718 (n=6), 79: -34,751 (n=12), 107: -34,996 (n=4), 77: -35,117 (n=215), 34: -35,155 (n=56), 101: -35,278 (n=11), 100: -35,363 (n=40), 20: -35,382 (n=5), 53: -35,433 (n=22), 16: -35,535 (n=12), 11: -35,563 (n=13), 64: -35,634 (n=17), 106: -35,704 (n=5), 32: -35,711 (n=8), 91: -35,821 (n=9), 47: -35,882 (n=17), 87: -35,931 (n=9), 129: -35,954 (n=74), 37: -36,198 (n=10), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 67: -36,875 (n=17), 145: -36,990 (n=7), 75: -37,220 (n=8), 114: -37,370 (n=3), 12: -37,385 (n=10), 29: -37,450 (n=21), 140: -38,489 (n=3), 17: -38,658 (n=4), 131: -38,847 (n=2), 124: -39,372 (n=2), 132: -39,931 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,067 | 25 | 30 | 25 | 12222 | 10.05 | 25: -30,686 (n=5871), 26: -30,710 (n=394), 30: -30,877 (n=3933), 31: -31,717 (n=107), 29: -31,925 (n=104), 27: -32,434 (n=201), 28: -33,555 (n=1046), 32: -34,693 (n=118), 35: -34,714 (n=170), 38: -35,335 (n=16), 41: -35,551 (n=2), 33: -35,613 (n=107), 37: -35,850 (n=21), 34: -36,028 (n=56), 39: -36,523 (n=10), 36: -37,906 (n=32), 40: -38,012 (n=10), 46: -38,521 (n=3), 44: -38,790 (n=5), 47: -39,384 (n=2), 50: -40,198 (n=7), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,455 | 3 | 3 | 4 | 12224 | 2.61 | 3: -30,733 (n=11027), 2: -35,946 (n=853), 4: -36,545 (n=328), 5: -43,188 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,214 | 1 | 0 | 33 | 12222 | 25.64 | 1: -30,312 (n=672), 0: -31,008 (n=10504), 9: -31,312 (n=83), 22: -31,539 (n=2), 2: -32,390 (n=115), 6: -33,345 (n=67), 8: -33,358 (n=64), 4: -33,388 (n=72), 17: -33,465 (n=11), 5: -34,135 (n=115), 11: -34,383 (n=54), 19: -34,546 (n=5), 3: -34,621 (n=150), 7: -35,657 (n=70), 13: -35,917 (n=35), 14: -36,236 (n=19), 28: -36,361 (n=2), 16: -36,379 (n=8), 12: -36,402 (n=25), 18: -36,506 (n=19), 23: -36,694 (n=6), 20: -36,836 (n=5), 15: -36,882 (n=25), 10: -37,294 (n=42), 24: -37,504 (n=4), 21: -38,756 (n=6), 39: -38,995 (n=8), 26: -40,268 (n=3), 40: -41,262 (n=6), 29: -41,603 (n=21), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,924 | 61 | 100 | 101 | 12223 | 62.35 | 61: -27,918 (n=2), 138: -28,049 (n=2), 69: -28,538 (n=7), 130: -28,649 (n=12), 80: -29,330 (n=112), 92: -29,918 (n=16), 85: -30,054 (n=83), 65: -30,099 (n=5), 93: -30,144 (n=335), 86: -30,244 (n=535), 91: -30,253 (n=74), 94: -30,259 (n=27), 81: -30,412 (n=65), 129: -30,419 (n=15), 100: -30,674 (n=7743), 114: -30,689 (n=21), 120: -30,726 (n=13), 111: -30,860 (n=31), 62: -30,897 (n=5), 84: -30,956 (n=58), 113: -30,977 (n=17), 115: -31,107 (n=24), 133: -31,210 (n=9), 78: -31,231 (n=59), 125: -31,291 (n=83), 107: -31,391 (n=20), 141: -31,447 (n=3), 83: -31,462 (n=107), 123: -31,509 (n=33), 64: -31,589 (n=8), 147: -31,607 (n=7), 102: -31,693 (n=39), 70: -31,724 (n=16), 95: -31,772 (n=32), 103: -31,813 (n=22), 63: -31,882 (n=9), 82: -31,935 (n=21), 57: -31,969 (n=5), 109: -32,019 (n=24), 105: -32,062 (n=75), 149: -32,176 (n=3), 87: -32,233 (n=17), 99: -32,241 (n=30), 128: -32,273 (n=16), 53: -32,281 (n=4), 66: -32,339 (n=13), 90: -32,340 (n=62), 132: -32,428 (n=9), 67: -32,542 (n=6), 104: -32,553 (n=494), 55: -32,666 (n=3), 68: -32,715 (n=9), 71: -32,801 (n=19), 56: -32,821 (n=2), 101: -32,878 (n=29), 119: -33,009 (n=14), 136: -33,061 (n=6), 112: -33,142 (n=192), 127: -33,168 (n=25), 122: -33,252 (n=34), 88: -33,414 (n=59), 97: -33,417 (n=49), 76: -33,459 (n=17), 134: -33,531 (n=8), 89: -33,676 (n=136), 117: -33,679 (n=59), 135: -33,769 (n=422), 79: -33,837 (n=37), 96: -33,887 (n=38), 59: -33,898 (n=4), 116: -33,926 (n=51), 124: -34,000 (n=20), 143: -34,012 (n=11), 98: -34,019 (n=34), 121: -34,025 (n=11), 110: -34,145 (n=19), 74: -34,399 (n=29), 108: -34,468 (n=24), 75: -34,479 (n=58), 126: -34,517 (n=21), 144: -34,772 (n=2), 137: -34,809 (n=4), 106: -35,027 (n=38), 150: -35,457 (n=160), 77: -35,916 (n=14), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 131: -36,462 (n=12), 148: -36,528 (n=3), 58: -36,674 (n=4), 50: -37,060 (n=38), 73: -37,196 (n=10), 118: -37,259 (n=13), 51: -37,500 (n=2), 72: -37,554 (n=9), 140: -38,416 (n=3), 60: -39,446 (n=8), 54: -39,448 (n=3), 145: -39,842 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,571 | 0.0 | 0.0 | 13 | 12224 | 10.14 | 0.0: -30,858 (n=10477), 0.1: -32,992 (n=868), 0.2: -33,865 (n=526), 0.4: -34,057 (n=73), 0.3: -34,614 (n=141), 0.5: -35,137 (n=44), 1.1: -35,241 (n=6), 0.7: -36,163 (n=16), 0.9: -37,063 (n=4), 0.6: -37,533 (n=33), 1.0: -37,910 (n=22), 1.2: -39,081 (n=9), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +11,400 | 13 | 20 | 11 | 12224 | 5.07 | 13: -30,488 (n=29), 17: -30,785 (n=3786), 14: -30,963 (n=104), 16: -31,077 (n=279), 19: -31,236 (n=582), 18: -31,363 (n=569), 20: -31,520 (n=6749), 15: -32,147 (n=104), 11: -32,310 (n=3), 12: -34,934 (n=12), 10: -41,889 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,920 | 6 | 6 | 8 | 12224 | 6.12 | 6: -30,664 (n=10877), 5: -34,684 (n=536), 7: -36,321 (n=334), 4: -37,226 (n=292), 3: -37,860 (n=109), 8: -38,376 (n=52), 9: -40,800 (n=18), 10: -41,585 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,773 | 20 | 20 | 15 | 12224 | 7.08 | 20: -30,410 (n=6584), 19: -30,974 (n=3936), 18: -31,724 (n=280), 17: -34,304 (n=633), 21: -36,236 (n=256), 16: -36,485 (n=115), 23: -37,202 (n=56), 15: -37,262 (n=57), 22: -37,790 (n=129), 14: -38,118 (n=30), 26: -38,726 (n=35), 25: -38,834 (n=18), 24: -39,119 (n=63), 13: -39,412 (n=17), 12: -41,183 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,683 | 6 | 18 | 21 | 12224 | 9.18 | 6: -29,449 (n=15), 14: -29,940 (n=16), 21: -30,437 (n=2010), 22: -30,727 (n=5926), 20: -31,172 (n=599), 23: -31,359 (n=559), 25: -32,371 (n=1045), 16: -32,403 (n=73), 17: -32,459 (n=649), 18: -32,886 (n=515), 24: -33,120 (n=372), 19: -33,641 (n=166), 12: -33,771 (n=10), 15: -33,782 (n=42), 13: -33,955 (n=22), 9: -33,973 (n=44), 10: -34,521 (n=63), 5: -36,010 (n=41), 7: -36,441 (n=21), 11: -36,584 (n=32), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,179 | 7 | 7 | 8 | 12224 | 6.08 | 7: -30,571 (n=10821), 6: -36,456 (n=735), 5: -36,485 (n=60), 8: -36,646 (n=387), 10: -36,859 (n=98), 9: -37,154 (n=82), 4: -38,562 (n=33), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +10,118 | 14 | 13 | 9 | 12224 | 4.41 | 14: -30,474 (n=1722), 13: -31,264 (n=7353), 11: -31,278 (n=679), 12: -31,442 (n=1761), 15: -31,465 (n=358), 16: -33,301 (n=207), 10: -34,030 (n=92), 9: -37,086 (n=39), 8: -40,592 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,057 | 10 | 8 | 11 | 12224 | 8.24 | 10: -30,591 (n=10268), 7: -32,683 (n=364), 8: -34,843 (n=818), 9: -34,881 (n=454), 6: -35,457 (n=144), 5: -35,849 (n=16), 12: -38,130 (n=41), 4: -38,259 (n=21), 11: -38,641 (n=53), 14: -39,191 (n=25), 13: -40,648 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,891 | 0.55 | 0.5 | 15 | 12224 | 6.79 | 0.55: -30,082 (n=6351), 0.65: -31,622 (n=1097), 0.5: -31,893 (n=3299), 0.75: -32,095 (n=87), 0.7: -32,230 (n=202), 0.6: -32,760 (n=292), 0.8: -33,051 (n=38), 0.45: -34,642 (n=376), 0.9: -35,286 (n=10), 0.85: -35,798 (n=11), 0.35: -36,046 (n=138), 0.4: -36,313 (n=134), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,974 (n=179) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,735 | 0 | 0 | 9 | 12224 | 7.13 | 0: -30,923 (n=11047), 1: -34,050 (n=633), 2: -34,613 (n=243), 3: -34,998 (n=199), 4: -35,623 (n=62), 5: -36,586 (n=17), 7: -36,592 (n=4), 6: -37,397 (n=16), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,625 | 2 | 2 | 4 | 12224 | 2.84 | 2: -31,017 (n=11741), 1: -36,974 (n=391), 3: -38,515 (n=35), 0: -39,642 (n=57) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,996 | 14 | 12 | 10 | 12224 | 7.48 | 14: -31,024 (n=10367), 13: -31,361 (n=838), 12: -32,894 (n=543), 11: -32,974 (n=183), 6: -34,434 (n=3), 9: -35,199 (n=24), 10: -35,411 (n=228), 7: -35,898 (n=8), 8: -37,161 (n=27), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,811 | frontier | frontier | 2 | 12224 | 0.92 | frontier: -30,939 (n=11707), v312: -38,750 (n=517) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,572 | 2 | 2 | 3 | 12224 | 1.82 | 2: -30,877 (n=11503), 1: -37,459 (n=677), 3: -38,450 (n=44) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,401 | 38 | 40 | 30 | 12224 | 7.49 | 38: -30,164 (n=2503), 34: -30,388 (n=207), 43: -30,526 (n=3461), 49: -30,529 (n=359), 33: -30,734 (n=49), 30: -30,869 (n=57), 44: -31,015 (n=306), 37: -31,139 (n=424), 39: -31,145 (n=410), 47: -31,243 (n=192), 45: -31,250 (n=431), 27: -31,389 (n=8), 28: -31,698 (n=14), 32: -31,993 (n=57), 26: -32,040 (n=36), 29: -32,205 (n=14), 46: -32,273 (n=80), 31: -32,383 (n=34), 35: -32,624 (n=188), 40: -32,721 (n=2494), 42: -33,033 (n=197), 36: -33,121 (n=173), 50: -33,133 (n=316), 41: -33,374 (n=84), 25: -34,003 (n=5), 48: -35,021 (n=61), 20: -35,089 (n=31), 24: -35,533 (n=23), 23: -36,212 (n=6), 22: -37,564 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2306)
- (10, 3, 6): -16,840 (n=1936)
- (8, 3, 5): -16,866 (n=235)
- (9, 3, 6): -16,959 (n=1486)
- (8, 3, 6): -17,552 (n=649)
- (12, 4, 6): -17,899 (n=414)
- (10, 4, 6): -17,975 (n=1709)
- (11, 3, 6): -18,175 (n=433)
- (11, 4, 6): -19,867 (n=454)
- (17, 3, 6): -20,013 (n=53)
- (8, 4, 6): -21,051 (n=588)
- (13, 4, 6): -21,868 (n=161)
- (8, 3, 4): -22,126 (n=64)
- (13, 3, 6): -22,174 (n=232)
- (10, 3, 5): -22,188 (n=51)

_Generated 2026-09-08 16:50. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 3288 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=3288); harvest_min=1–3 (n=3288); wheat_tiles=0–8 (n=3288); wheat_stock=0–40 (n=3288); min_hands=3–6 (n=3288); load_per_hand=12–26 (n=3288); geese=0–2 (n=3288); open_melons=4–14 (n=3288)
- **Evidence:** 3288 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 42 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=42); harvest_min=1–3 (n=42); wheat_tiles=0–2 (n=42); wheat_stock=0–4 (n=42); min_hands=3–6 (n=42); load_per_hand=19–21 (n=42); geese=0–2 (n=42); open_melons=7–13 (n=42)
- **Evidence:** 42 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 24 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=24); harvest_min=1–3 (n=24); wheat_tiles=0; wheat_stock=0–39 (n=24); min_hands=3–6 (n=24); load_per_hand=12–20 (n=24); geese=0–1 (n=24); open_melons=9–13 (n=24)
- **Evidence:** 24 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 13 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=13); harvest_min=1–3 (n=13); wheat_tiles=0–8 (n=13); wheat_stock=0–39 (n=13); min_hands=3–6 (n=13); load_per_hand=12–17 (n=13); geese=0–2 (n=13); open_melons=8–14 (n=13)
- **Evidence:** 13 candidates, multiple seeds. Confidence: moderate

### None (observed in 8 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=8); harvest_min=1–2 (n=8); wheat_tiles=0; wheat_stock=0–11 (n=8); min_hands=3–6 (n=8); load_per_hand=12–18 (n=8); geese=0–2 (n=8); open_melons=10–14 (n=8)
- **Evidence:** 8 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 16:50. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._