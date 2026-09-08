# Evolution run 20260908-103932

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.01 h · candidates evaluated this run: 1193 · games 24,674 (12,281/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 382 | 764 |
| dead_pattern | 203 | 406 |
| dead_smoke | 142 | 1136 |
| alive | 466 | 22368 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 11308 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1295
- M2: best -16,461 (`0c25e1226b27`), n=1348
- c1: best -16,310 (`23734cef4da1`), n=2075
- queue: best -15,412 (`fe4745b56024`), n=2847
- v312: best -15,275 (`52b3d5cc236e`), n=1968
- wide: best -16,047 (`512e53fe15bc`), n=1775

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +21,828 | 120 | 50 | 143 | 11297 | 64.02 | 120: -18,103 (n=2), 141: -24,735 (n=4), 118: -25,349 (n=2), 143: -26,636 (n=2), 19: -27,075 (n=13), 8: -27,428 (n=2), 35: -27,894 (n=8), 112: -28,098 (n=12), 72: -28,170 (n=6), 5: -28,572 (n=45), 71: -29,097 (n=21), 27: -29,195 (n=34), 26: -29,341 (n=6), 92: -29,351 (n=265), 58: -29,579 (n=78), 56: -29,717 (n=11), 49: -29,792 (n=62), 18: -29,967 (n=634), 63: -29,982 (n=154), 89: -30,198 (n=22), 74: -30,290 (n=128), 61: -30,358 (n=90), 65: -30,526 (n=110), 51: -30,565 (n=12), 50: -30,689 (n=5565), 48: -30,751 (n=479), 80: -30,851 (n=12), 150: -30,925 (n=111), 33: -31,069 (n=19), 66: -31,132 (n=170), 42: -31,151 (n=666), 144: -31,182 (n=2), 60: -31,213 (n=27), 14: -31,276 (n=14), 85: -31,279 (n=9), 45: -31,289 (n=106), 40: -31,414 (n=85), 9: -31,680 (n=12), 2: -31,685 (n=2), 86: -31,717 (n=8), 57: -31,735 (n=82), 93: -31,753 (n=7), 96: -31,788 (n=6), 70: -31,835 (n=26), 73: -31,870 (n=14), 36: -31,951 (n=92), 69: -32,072 (n=21), 84: -32,162 (n=12), 39: -32,172 (n=50), 59: -32,251 (n=15), 110: -32,277 (n=4), 95: -32,333 (n=4), 113: -32,348 (n=6), 25: -32,369 (n=7), 94: -32,527 (n=15), 103: -32,559 (n=8), 76: -32,628 (n=10), 24: -32,730 (n=13), 115: -32,792 (n=6), 38: -32,804 (n=17), 88: -32,815 (n=9), 52: -32,819 (n=11), 97: -32,830 (n=21), 109: -32,844 (n=3), 21: -32,959 (n=7), 62: -32,965 (n=16), 136: -33,034 (n=30), 98: -33,193 (n=12), 83: -33,226 (n=86), 55: -33,239 (n=465), 108: -33,264 (n=5), 104: -33,266 (n=4), 6: -33,331 (n=10), 119: -33,340 (n=2), 31: -33,344 (n=11), 4: -33,399 (n=36), 111: -33,451 (n=7), 0: -33,459 (n=171), 13: -33,499 (n=7), 23: -33,511 (n=11), 41: -33,525 (n=29), 43: -33,691 (n=18), 30: -33,744 (n=14), 90: -33,822 (n=7), 22: -33,829 (n=14), 28: -33,832 (n=18), 81: -33,835 (n=24), 68: -33,901 (n=9), 82: -34,009 (n=38), 44: -34,063 (n=19), 78: -34,070 (n=8), 46: -34,088 (n=26), 54: -34,180 (n=17), 10: -34,299 (n=13), 102: -34,320 (n=4), 99: -34,411 (n=68), 1: -34,413 (n=5), 134: -34,464 (n=2), 7: -34,718 (n=6), 79: -34,751 (n=12), 34: -34,989 (n=52), 107: -34,996 (n=4), 77: -35,138 (n=208), 91: -35,175 (n=7), 32: -35,252 (n=7), 100: -35,306 (n=39), 20: -35,382 (n=5), 16: -35,406 (n=11), 53: -35,427 (n=20), 11: -35,563 (n=13), 87: -35,609 (n=8), 106: -35,704 (n=5), 129: -35,876 (n=73), 47: -35,882 (n=17), 101: -36,126 (n=10), 37: -36,131 (n=9), 15: -36,386 (n=7), 64: -36,496 (n=16), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 75: -37,220 (n=8), 114: -37,370 (n=3), 12: -37,385 (n=10), 67: -37,399 (n=16), 29: -37,559 (n=19), 140: -38,489 (n=3), 17: -38,658 (n=4), 131: -38,847 (n=2), 124: -39,372 (n=2), 132: -39,931 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +13,180 | 3 | 3 | 4 | 11308 | 2.61 | 3: -30,707 (n=10201), 2: -35,896 (n=795), 4: -36,604 (n=300), 5: -43,888 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,119 | 25 | 30 | 25 | 11306 | 10.0 | 25: -30,634 (n=5408), 26: -30,799 (n=341), 30: -30,805 (n=3640), 31: -31,487 (n=99), 29: -31,885 (n=96), 27: -32,383 (n=190), 28: -33,602 (n=991), 35: -34,727 (n=169), 32: -34,808 (n=107), 38: -35,335 (n=16), 41: -35,551 (n=2), 33: -35,725 (n=102), 34: -36,064 (n=54), 37: -36,073 (n=20), 39: -36,508 (n=9), 44: -37,771 (n=4), 40: -38,012 (n=10), 36: -38,389 (n=30), 46: -38,521 (n=3), 47: -39,384 (n=2), 50: -40,579 (n=6), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +12,727 | 6 | 6 | 8 | 11308 | 6.11 | 6: -30,630 (n=10044), 5: -34,625 (n=500), 7: -36,200 (n=315), 4: -37,178 (n=270), 3: -37,910 (n=106), 8: -38,309 (n=51), 9: -40,973 (n=17), 10: -43,357 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +12,491 | 14 | 20 | 11 | 11308 | 5.18 | 14: -30,684 (n=96), 17: -30,715 (n=3411), 16: -30,977 (n=260), 13: -31,069 (n=25), 19: -31,213 (n=521), 18: -31,234 (n=530), 20: -31,516 (n=6357), 11: -32,310 (n=3), 15: -32,380 (n=90), 12: -35,464 (n=10), 10: -43,175 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +11,980 | 1 | 0 | 33 | 11305 | 24.97 | 1: -30,547 (n=560), 0: -30,974 (n=9788), 9: -31,114 (n=80), 2: -32,275 (n=103), 19: -32,857 (n=3), 6: -32,878 (n=58), 4: -33,228 (n=66), 8: -33,481 (n=59), 17: -33,644 (n=10), 5: -34,068 (n=100), 11: -34,345 (n=53), 3: -34,646 (n=146), 7: -35,615 (n=65), 13: -35,682 (n=30), 12: -36,258 (n=23), 28: -36,361 (n=2), 16: -36,379 (n=8), 18: -36,506 (n=19), 14: -36,586 (n=16), 15: -36,670 (n=20), 23: -36,694 (n=6), 20: -36,836 (n=5), 10: -37,032 (n=38), 24: -37,504 (n=4), 21: -38,157 (n=5), 39: -38,995 (n=8), 26: -40,268 (n=3), 40: -41,262 (n=6), 29: -41,395 (n=17), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,792 | 138 | 100 | 100 | 11307 | 61.58 | 138: -28,049 (n=2), 130: -28,802 (n=10), 92: -28,949 (n=12), 80: -29,651 (n=85), 86: -30,043 (n=475), 85: -30,054 (n=83), 69: -30,090 (n=6), 65: -30,099 (n=5), 81: -30,103 (n=61), 94: -30,112 (n=26), 113: -30,212 (n=15), 93: -30,276 (n=296), 100: -30,600 (n=7147), 91: -30,601 (n=69), 120: -30,726 (n=13), 111: -30,738 (n=30), 114: -30,784 (n=20), 62: -30,897 (n=5), 78: -31,087 (n=48), 84: -31,139 (n=55), 115: -31,166 (n=22), 141: -31,181 (n=2), 125: -31,267 (n=82), 83: -31,307 (n=102), 66: -31,331 (n=11), 123: -31,435 (n=28), 64: -31,589 (n=8), 133: -31,605 (n=8), 107: -31,707 (n=18), 70: -31,714 (n=15), 129: -31,735 (n=13), 147: -31,811 (n=6), 103: -31,813 (n=22), 132: -31,873 (n=8), 63: -31,882 (n=9), 109: -31,962 (n=23), 102: -31,968 (n=36), 57: -31,969 (n=5), 82: -32,036 (n=19), 149: -32,176 (n=3), 90: -32,230 (n=57), 99: -32,241 (n=30), 128: -32,258 (n=15), 53: -32,281 (n=4), 87: -32,396 (n=16), 68: -32,513 (n=7), 67: -32,542 (n=6), 104: -32,569 (n=467), 101: -32,632 (n=28), 105: -32,700 (n=67), 122: -32,768 (n=31), 95: -32,793 (n=29), 71: -32,801 (n=19), 56: -32,821 (n=2), 136: -33,061 (n=6), 112: -33,153 (n=191), 127: -33,194 (n=24), 88: -33,265 (n=57), 76: -33,413 (n=16), 97: -33,417 (n=49), 79: -33,581 (n=35), 119: -33,644 (n=12), 89: -33,664 (n=135), 135: -33,708 (n=411), 98: -33,726 (n=31), 96: -33,746 (n=35), 116: -33,841 (n=49), 59: -33,898 (n=4), 124: -34,000 (n=20), 143: -34,012 (n=11), 117: -34,023 (n=48), 121: -34,260 (n=10), 110: -34,415 (n=17), 74: -34,442 (n=27), 126: -34,456 (n=19), 134: -34,482 (n=7), 75: -34,730 (n=54), 108: -34,741 (n=22), 144: -34,772 (n=2), 55: -34,785 (n=2), 106: -35,109 (n=35), 150: -35,336 (n=154), 137: -35,375 (n=3), 77: -35,916 (n=14), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 50: -36,668 (n=32), 58: -36,674 (n=4), 131: -36,786 (n=11), 73: -37,212 (n=8), 118: -37,259 (n=13), 51: -37,500 (n=2), 72: -37,976 (n=8), 140: -38,416 (n=3), 54: -39,448 (n=3), 60: -39,580 (n=7), 145: -39,842 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,617 | 0.0 | 0.0 | 13 | 11308 | 10.07 | 0.0: -30,811 (n=9629), 0.1: -32,953 (n=839), 0.2: -33,894 (n=512), 0.4: -34,323 (n=68), 0.5: -34,759 (n=40), 0.3: -34,766 (n=133), 1.1: -35,241 (n=6), 0.6: -36,667 (n=27), 0.7: -36,679 (n=15), 0.9: -37,063 (n=4), 1.0: -37,910 (n=22), 1.2: -39,109 (n=8), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,683 | 6 | 18 | 21 | 11308 | 9.05 | 6: -29,449 (n=15), 14: -29,940 (n=16), 21: -30,402 (n=1828), 22: -30,673 (n=5412), 20: -31,184 (n=571), 23: -31,306 (n=526), 16: -32,290 (n=66), 17: -32,321 (n=623), 25: -32,321 (n=988), 18: -32,858 (n=490), 24: -33,129 (n=350), 12: -33,771 (n=10), 15: -33,782 (n=42), 19: -33,794 (n=154), 9: -33,807 (n=43), 13: -34,515 (n=20), 10: -34,521 (n=63), 5: -36,199 (n=36), 11: -36,828 (n=31), 7: -36,889 (n=20), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,602 | 20 | 20 | 15 | 11308 | 6.9 | 20: -30,351 (n=5955), 19: -30,982 (n=3763), 18: -31,651 (n=263), 17: -34,246 (n=607), 21: -36,350 (n=236), 16: -36,470 (n=106), 23: -37,083 (n=54), 15: -37,385 (n=54), 22: -37,697 (n=111), 14: -38,237 (n=27), 25: -38,485 (n=16), 24: -38,850 (n=56), 26: -39,026 (n=32), 13: -39,668 (n=15), 12: -40,953 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,233 | 7 | 7 | 8 | 11308 | 6.06 | 7: -30,517 (n=9974), 6: -36,455 (n=705), 5: -36,507 (n=58), 8: -36,706 (n=361), 10: -36,736 (n=95), 9: -37,251 (n=76), 4: -38,578 (n=31), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +10,227 | 14 | 13 | 9 | 11308 | 4.45 | 14: -30,365 (n=1514), 13: -31,241 (n=6843), 11: -31,339 (n=638), 12: -31,399 (n=1663), 15: -31,422 (n=327), 16: -33,211 (n=189), 10: -34,197 (n=87), 9: -37,455 (n=34), 8: -40,592 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,117 | 10 | 8 | 11 | 11308 | 8.18 | 10: -30,531 (n=9441), 7: -32,585 (n=339), 8: -34,853 (n=797), 9: -34,890 (n=429), 6: -35,467 (n=131), 5: -36,086 (n=14), 12: -38,206 (n=39), 4: -38,638 (n=20), 11: -38,641 (n=53), 14: -39,191 (n=25), 13: -40,648 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,965 | 0.55 | 0.5 | 15 | 11308 | 6.58 | 0.55: -29,980 (n=5716), 0.65: -31,671 (n=1069), 0.5: -31,887 (n=3147), 0.75: -31,934 (n=76), 0.7: -32,100 (n=186), 0.6: -32,740 (n=278), 0.8: -33,283 (n=37), 0.45: -34,612 (n=352), 0.9: -34,927 (n=9), 0.85: -35,798 (n=11), 0.35: -36,071 (n=124), 0.4: -36,303 (n=128), 0.95: -37,209 (n=3), 1.0: -39,813 (n=6), 0.3: -39,945 (n=166) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,776 | 0 | 0 | 9 | 11308 | 7.11 | 0: -30,883 (n=10194), 1: -34,091 (n=598), 2: -34,626 (n=231), 3: -34,964 (n=190), 4: -35,601 (n=56), 5: -36,586 (n=17), 7: -36,592 (n=4), 6: -37,392 (n=15), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +9,134 | 30 | 40 | 30 | 11308 | 7.51 | 30: -29,949 (n=49), 38: -30,065 (n=2230), 33: -30,378 (n=45), 34: -30,448 (n=189), 43: -30,483 (n=3206), 49: -30,534 (n=334), 44: -30,906 (n=280), 37: -31,062 (n=378), 39: -31,111 (n=369), 45: -31,174 (n=388), 47: -31,216 (n=170), 26: -31,421 (n=32), 28: -31,698 (n=14), 32: -31,729 (n=54), 31: -32,070 (n=33), 46: -32,319 (n=71), 29: -32,367 (n=13), 27: -32,492 (n=7), 35: -32,553 (n=177), 40: -32,700 (n=2427), 42: -33,109 (n=182), 50: -33,133 (n=295), 36: -33,134 (n=166), 41: -33,181 (n=75), 25: -34,303 (n=4), 20: -35,006 (n=30), 48: -35,059 (n=60), 24: -35,630 (n=22), 23: -36,048 (n=5), 22: -39,083 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,800 | 2 | 2 | 4 | 11308 | 2.84 | 2: -30,983 (n=10856), 1: -37,027 (n=364), 3: -38,625 (n=33), 0: -39,783 (n=55) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,055 | 14 | 12 | 10 | 11308 | 7.47 | 14: -30,966 (n=9580), 13: -31,588 (n=765), 12: -32,921 (n=511), 11: -33,009 (n=170), 6: -34,434 (n=3), 9: -35,295 (n=23), 10: -35,437 (n=221), 7: -35,898 (n=8), 8: -36,937 (n=24), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,858 | frontier | frontier | 2 | 11308 | 0.91 | frontier: -30,908 (n=10826), v312: -38,766 (n=482) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,507 | 2 | 2 | 3 | 11308 | 1.82 | 2: -30,850 (n=10642), 1: -37,454 (n=625), 3: -38,358 (n=41) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2144)
- (10, 3, 6): -16,840 (n=1768)
- (8, 3, 5): -16,866 (n=223)
- (9, 3, 6): -16,959 (n=1351)
- (8, 3, 6): -17,804 (n=616)
- (12, 4, 6): -17,899 (n=389)
- (10, 4, 6): -17,975 (n=1572)
- (11, 3, 6): -18,175 (n=403)
- (11, 4, 6): -19,867 (n=432)
- (17, 3, 6): -20,013 (n=48)
- (8, 4, 6): -21,051 (n=544)
- (13, 4, 6): -21,868 (n=145)
- (8, 3, 4): -22,126 (n=62)
- (13, 3, 6): -22,174 (n=213)
- (10, 3, 5): -22,188 (n=51)

_Generated 2026-09-08 12:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 2553 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=2553); harvest_min=1–3 (n=2553); wheat_tiles=0–8 (n=2553); wheat_stock=0–40 (n=2553); min_hands=3–6 (n=2553); load_per_hand=12–26 (n=2553); geese=0–2 (n=2553); open_melons=4–14 (n=2553)
- **Evidence:** 2553 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 29 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=29); harvest_min=1–3 (n=29); wheat_tiles=0–2 (n=29); wheat_stock=0–4 (n=29); min_hands=3–6 (n=29); load_per_hand=19–21 (n=29); geese=0–2 (n=29); open_melons=7–13 (n=29)
- **Evidence:** 29 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 19 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=19); harvest_min=1–3 (n=19); wheat_tiles=0; wheat_stock=0–29 (n=19); min_hands=3–6 (n=19); load_per_hand=12–20 (n=19); geese=0–1 (n=19); open_melons=9–13 (n=19)
- **Evidence:** 19 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 13 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=13); harvest_min=1–3 (n=13); wheat_tiles=0–8 (n=13); wheat_stock=0–39 (n=13); min_hands=3–6 (n=13); load_per_hand=12–17 (n=13); geese=0–2 (n=13); open_melons=8–14 (n=13)
- **Evidence:** 13 candidates, multiple seeds. Confidence: moderate

### None (observed in 7 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=7); harvest_min=1–2 (n=7); wheat_tiles=0; wheat_stock=0–11 (n=7); min_hands=3–6 (n=7); load_per_hand=12–18 (n=7); geese=0–2 (n=7); open_melons=10–14 (n=7)
- **Evidence:** 7 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 12:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._