# Evolution run 20260908-063135

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.01 h · candidates evaluated this run: 1263 · games 25,086 (12,498/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 412 | 824 |
| dead_pattern | 211 | 422 |
| dead_smoke | 172 | 1376 |
| alive | 468 | 22464 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 10388 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1139
- M2: best -16,461 (`0c25e1226b27`), n=1185
- c1: best -16,310 (`23734cef4da1`), n=1935
- queue: best -15,412 (`fe4745b56024`), n=2660
- v312: best -15,275 (`52b3d5cc236e`), n=1832
- wide: best -16,047 (`512e53fe15bc`), n=1637

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +15,196 | 141 | 50 | 142 | 10375 | 62.36 | 141: -24,735 (n=4), 118: -25,349 (n=2), 143: -26,636 (n=2), 19: -27,075 (n=13), 8: -27,428 (n=2), 72: -27,761 (n=5), 35: -27,782 (n=7), 112: -28,098 (n=12), 71: -28,163 (n=18), 5: -28,837 (n=41), 27: -29,195 (n=34), 92: -29,243 (n=221), 26: -29,341 (n=6), 58: -29,465 (n=71), 49: -29,650 (n=59), 56: -29,717 (n=11), 18: -29,829 (n=566), 63: -29,929 (n=136), 61: -30,263 (n=88), 74: -30,400 (n=102), 89: -30,424 (n=20), 65: -30,504 (n=103), 51: -30,565 (n=12), 80: -30,569 (n=10), 50: -30,686 (n=5096), 150: -30,729 (n=82), 14: -30,741 (n=9), 48: -30,783 (n=465), 33: -30,789 (n=18), 86: -30,882 (n=7), 66: -30,927 (n=141), 42: -31,120 (n=627), 144: -31,182 (n=2), 85: -31,279 (n=9), 60: -31,316 (n=25), 70: -31,388 (n=24), 40: -31,514 (n=84), 45: -31,599 (n=99), 57: -31,735 (n=82), 96: -31,788 (n=6), 52: -32,111 (n=8), 9: -32,131 (n=11), 39: -32,172 (n=50), 69: -32,264 (n=18), 84: -32,266 (n=11), 110: -32,277 (n=4), 59: -32,292 (n=14), 25: -32,369 (n=7), 136: -32,464 (n=28), 94: -32,464 (n=14), 36: -32,475 (n=84), 93: -32,538 (n=6), 103: -32,559 (n=8), 73: -32,619 (n=13), 76: -32,628 (n=10), 24: -32,730 (n=13), 115: -32,792 (n=6), 109: -32,844 (n=3), 21: -32,882 (n=6), 62: -32,965 (n=16), 13: -33,052 (n=6), 83: -33,226 (n=86), 31: -33,261 (n=10), 104: -33,266 (n=4), 90: -33,267 (n=6), 0: -33,285 (n=160), 6: -33,331 (n=10), 55: -33,331 (n=446), 119: -33,340 (n=2), 95: -33,358 (n=3), 4: -33,399 (n=36), 88: -33,480 (n=8), 23: -33,511 (n=11), 43: -33,549 (n=17), 78: -33,580 (n=6), 38: -33,610 (n=16), 111: -33,648 (n=6), 98: -33,653 (n=7), 97: -33,700 (n=17), 7: -33,733 (n=5), 22: -33,829 (n=14), 28: -33,832 (n=18), 30: -33,882 (n=12), 46: -33,900 (n=25), 68: -33,901 (n=9), 81: -33,955 (n=22), 82: -34,040 (n=33), 41: -34,047 (n=27), 44: -34,096 (n=17), 79: -34,199 (n=11), 10: -34,299 (n=13), 102: -34,320 (n=4), 99: -34,322 (n=67), 1: -34,413 (n=5), 134: -34,464 (n=2), 54: -34,796 (n=12), 34: -34,887 (n=50), 107: -34,996 (n=4), 100: -35,098 (n=33), 87: -35,123 (n=7), 91: -35,175 (n=7), 77: -35,202 (n=203), 32: -35,252 (n=7), 20: -35,382 (n=5), 16: -35,406 (n=11), 53: -35,485 (n=19), 11: -35,563 (n=13), 47: -35,882 (n=17), 129: -35,931 (n=72), 113: -36,036 (n=4), 106: -36,115 (n=2), 101: -36,126 (n=10), 37: -36,131 (n=9), 15: -36,232 (n=6), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 64: -36,707 (n=15), 145: -36,990 (n=7), 12: -37,240 (n=9), 114: -37,370 (n=3), 29: -37,516 (n=16), 67: -37,742 (n=15), 17: -38,455 (n=2), 140: -38,489 (n=3), 108: -38,546 (n=2), 75: -38,761 (n=6), 131: -38,847 (n=2), 132: -39,931 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +13,417 | 3 | 3 | 4 | 10388 | 2.61 | 3: -30,719 (n=9375), 2: -35,968 (n=724), 4: -36,695 (n=278), 5: -44,135 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,126 | 25 | 30 | 25 | 10384 | 8.99 | 25: -30,627 (n=4942), 30: -30,777 (n=3328), 26: -30,923 (n=308), 31: -31,611 (n=90), 29: -31,995 (n=92), 27: -32,554 (n=177), 28: -33,661 (n=937), 35: -34,709 (n=163), 32: -34,807 (n=101), 38: -35,300 (n=15), 33: -35,658 (n=97), 37: -36,073 (n=20), 34: -36,134 (n=50), 39: -36,508 (n=9), 44: -37,771 (n=4), 36: -38,291 (n=28), 40: -38,324 (n=9), 46: -39,707 (n=2), 50: -40,579 (n=6), 43: -42,029 (n=4), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +12,730 | 6 | 6 | 8 | 10388 | 6.08 | 6: -30,627 (n=9193), 5: -34,686 (n=476), 7: -36,184 (n=306), 4: -37,216 (n=248), 3: -37,845 (n=94), 8: -38,295 (n=50), 9: -41,174 (n=16), 10: -43,357 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +12,608 | 14 | 20 | 11 | 10388 | 5.32 | 14: -30,566 (n=91), 17: -30,663 (n=3007), 16: -31,107 (n=244), 18: -31,316 (n=499), 19: -31,388 (n=463), 13: -31,402 (n=24), 20: -31,521 (n=5965), 11: -32,310 (n=3), 15: -32,837 (n=79), 12: -37,278 (n=8), 10: -43,175 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,792 | 138 | 100 | 100 | 10387 | 61.34 | 138: -28,049 (n=2), 130: -28,802 (n=10), 92: -28,949 (n=12), 69: -29,128 (n=4), 62: -29,494 (n=4), 80: -29,665 (n=58), 85: -29,983 (n=80), 86: -29,999 (n=412), 65: -30,099 (n=5), 94: -30,170 (n=24), 113: -30,212 (n=15), 81: -30,252 (n=57), 93: -30,295 (n=268), 91: -30,563 (n=65), 100: -30,594 (n=6541), 120: -30,726 (n=13), 111: -30,738 (n=30), 66: -30,750 (n=10), 114: -30,784 (n=20), 115: -30,905 (n=21), 132: -31,067 (n=7), 70: -31,108 (n=14), 125: -31,136 (n=81), 141: -31,181 (n=2), 136: -31,307 (n=5), 78: -31,354 (n=41), 83: -31,397 (n=101), 147: -31,580 (n=5), 64: -31,589 (n=8), 133: -31,605 (n=8), 84: -31,606 (n=43), 82: -31,609 (n=16), 129: -31,735 (n=13), 99: -31,872 (n=27), 63: -31,882 (n=9), 102: -31,911 (n=35), 57: -31,969 (n=5), 109: -32,108 (n=21), 149: -32,176 (n=3), 101: -32,265 (n=25), 53: -32,281 (n=4), 105: -32,291 (n=61), 123: -32,404 (n=23), 103: -32,416 (n=21), 68: -32,513 (n=7), 87: -32,517 (n=15), 95: -32,539 (n=25), 67: -32,542 (n=6), 104: -32,578 (n=437), 71: -32,590 (n=18), 128: -32,669 (n=13), 107: -32,707 (n=15), 122: -32,804 (n=30), 56: -32,821 (n=2), 90: -33,017 (n=43), 127: -33,107 (n=22), 112: -33,119 (n=187), 97: -33,232 (n=46), 76: -33,313 (n=15), 88: -33,376 (n=56), 89: -33,517 (n=129), 98: -33,536 (n=26), 135: -33,642 (n=402), 119: -33,644 (n=12), 96: -33,693 (n=34), 79: -33,728 (n=33), 116: -33,835 (n=45), 59: -33,898 (n=4), 124: -34,000 (n=20), 143: -34,012 (n=11), 121: -34,263 (n=9), 74: -34,400 (n=25), 110: -34,415 (n=17), 134: -34,482 (n=7), 117: -34,491 (n=38), 108: -34,640 (n=21), 144: -34,772 (n=2), 55: -34,785 (n=2), 126: -34,796 (n=18), 75: -34,866 (n=51), 106: -35,120 (n=32), 150: -35,283 (n=148), 137: -35,375 (n=3), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 77: -36,373 (n=12), 50: -36,399 (n=28), 148: -36,528 (n=3), 58: -36,674 (n=4), 73: -36,783 (n=7), 131: -36,786 (n=11), 51: -37,500 (n=2), 118: -37,501 (n=12), 72: -37,976 (n=8), 140: -38,416 (n=3), 54: -39,448 (n=3), 60: -39,580 (n=7), 145: -39,842 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +11,773 | 1 | 0 | 33 | 10385 | 25.14 | 1: -30,753 (n=461), 0: -30,968 (n=9050), 9: -31,330 (n=75), 2: -32,474 (n=90), 6: -32,672 (n=55), 19: -32,857 (n=3), 4: -33,491 (n=61), 8: -33,744 (n=53), 17: -33,865 (n=9), 5: -34,107 (n=92), 11: -34,635 (n=49), 3: -34,831 (n=136), 13: -35,558 (n=26), 7: -35,871 (n=55), 12: -36,118 (n=21), 28: -36,361 (n=2), 16: -36,564 (n=7), 15: -36,571 (n=18), 18: -36,585 (n=17), 14: -36,586 (n=16), 23: -36,694 (n=6), 20: -36,836 (n=5), 10: -37,148 (n=34), 24: -37,504 (n=4), 21: -38,157 (n=5), 39: -39,673 (n=7), 26: -40,268 (n=3), 40: -41,262 (n=6), 29: -41,445 (n=15), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,622 | 0.0 | 0.0 | 13 | 10388 | 9.99 | 0.0: -30,806 (n=8783), 0.1: -32,969 (n=808), 0.2: -33,912 (n=492), 0.5: -34,488 (n=38), 0.4: -34,492 (n=63), 0.3: -34,822 (n=120), 1.1: -35,241 (n=6), 0.7: -36,679 (n=15), 0.6: -36,965 (n=25), 1.0: -37,910 (n=22), 0.9: -38,511 (n=3), 1.2: -39,109 (n=8), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,501 | 20 | 20 | 15 | 10388 | 6.64 | 20: -30,321 (n=5289), 19: -30,999 (n=3599), 18: -31,711 (n=244), 17: -34,197 (n=598), 21: -36,429 (n=213), 16: -36,695 (n=100), 23: -37,130 (n=48), 15: -37,215 (n=49), 22: -37,777 (n=99), 14: -38,260 (n=25), 25: -38,533 (n=15), 24: -38,829 (n=54), 26: -38,921 (n=30), 13: -40,050 (n=14), 12: -41,822 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +10,358 | 14 | 13 | 9 | 10388 | 4.48 | 14: -30,234 (n=1292), 13: -31,261 (n=6322), 11: -31,377 (n=612), 12: -31,394 (n=1578), 15: -31,701 (n=291), 16: -33,392 (n=167), 10: -34,093 (n=83), 9: -37,246 (n=30), 8: -40,592 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,191 | 14 | 18 | 21 | 10388 | 8.96 | 14: -29,940 (n=16), 21: -30,307 (n=1641), 6: -30,539 (n=13), 22: -30,689 (n=4928), 20: -31,104 (n=544), 23: -31,386 (n=471), 25: -32,318 (n=917), 17: -32,329 (n=600), 18: -32,801 (n=467), 16: -32,859 (n=61), 12: -33,209 (n=9), 24: -33,219 (n=333), 19: -33,807 (n=137), 9: -33,807 (n=43), 15: -34,121 (n=39), 13: -34,158 (n=18), 10: -34,521 (n=63), 5: -36,455 (n=33), 11: -36,828 (n=31), 7: -36,889 (n=20), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,183 | 10 | 8 | 11 | 10388 | 8.12 | 10: -30,515 (n=8612), 7: -32,638 (n=311), 9: -34,831 (n=409), 8: -34,864 (n=771), 6: -35,406 (n=126), 5: -36,829 (n=11), 12: -38,407 (n=36), 4: -38,581 (n=18), 11: -38,941 (n=50), 14: -39,191 (n=25), 13: -40,698 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +10,128 | 0.55 | 0.5 | 15 | 10388 | 6.31 | 0.55: -29,901 (n=5059), 0.65: -31,703 (n=1041), 0.5: -31,907 (n=3009), 0.75: -32,058 (n=69), 0.7: -32,114 (n=175), 0.6: -32,790 (n=258), 0.8: -33,412 (n=33), 0.45: -34,700 (n=325), 0.9: -34,927 (n=9), 0.85: -35,798 (n=11), 0.35: -36,130 (n=118), 0.4: -36,294 (n=119), 0.95: -37,209 (n=3), 1.0: -39,813 (n=6), 0.3: -40,028 (n=153) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +9,859 | 7 | 7 | 8 | 10388 | 6.05 | 7: -30,526 (n=9151), 6: -36,427 (n=663), 5: -36,507 (n=58), 8: -36,776 (n=325), 10: -36,978 (n=91), 9: -37,361 (n=65), 4: -38,314 (n=28), 3: -40,385 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,766 | 0 | 0 | 9 | 10388 | 7.1 | 0: -30,892 (n=9345), 1: -34,105 (n=564), 2: -34,618 (n=220), 3: -34,944 (n=176), 4: -35,902 (n=48), 5: -36,586 (n=17), 7: -36,592 (n=4), 6: -37,762 (n=11), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +9,601 | 30 | 40 | 30 | 10388 | 7.51 | 30: -29,517 (n=41), 38: -29,937 (n=1964), 33: -30,270 (n=43), 49: -30,426 (n=317), 43: -30,500 (n=2945), 34: -30,632 (n=177), 37: -30,978 (n=327), 39: -31,089 (n=321), 45: -31,103 (n=340), 26: -31,216 (n=24), 44: -31,247 (n=244), 47: -31,393 (n=150), 28: -31,551 (n=12), 32: -31,757 (n=51), 31: -32,014 (n=30), 46: -32,169 (n=63), 25: -32,322 (n=3), 27: -32,492 (n=7), 35: -32,638 (n=166), 40: -32,688 (n=2369), 42: -33,101 (n=174), 36: -33,107 (n=159), 29: -33,212 (n=11), 50: -33,227 (n=274), 41: -33,371 (n=69), 20: -34,792 (n=25), 48: -35,362 (n=54), 24: -35,630 (n=22), 23: -36,850 (n=4), 22: -39,119 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +9,186 | 2 | 2 | 4 | 10388 | 2.84 | 2: -30,992 (n=9964), 1: -37,005 (n=342), 3: -38,756 (n=31), 0: -40,179 (n=51) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,915 | frontier | frontier | 2 | 10388 | 0.91 | frontier: -30,915 (n=9937), v312: -38,830 (n=451) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,487 | 2 | 2 | 3 | 10388 | 1.82 | 2: -30,861 (n=9770), 1: -37,490 (n=580), 3: -38,348 (n=38) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,478 | 14 | 12 | 10 | 10388 | 7.45 | 14: -30,954 (n=8775), 13: -31,683 (n=699), 12: -33,063 (n=478), 11: -33,144 (n=160), 6: -34,434 (n=3), 9: -35,295 (n=23), 10: -35,531 (n=216), 7: -35,898 (n=8), 8: -36,937 (n=24), 5: -38,432 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=1966)
- (10, 3, 6): -16,840 (n=1609)
- (8, 3, 5): -16,866 (n=211)
- (9, 3, 6): -16,959 (n=1199)
- (12, 4, 6): -17,899 (n=374)
- (10, 4, 6): -17,975 (n=1415)
- (8, 3, 6): -18,139 (n=578)
- (11, 3, 6): -18,175 (n=375)
- (11, 4, 6): -19,867 (n=420)
- (17, 3, 6): -20,013 (n=47)
- (8, 4, 6): -21,051 (n=513)
- (13, 4, 6): -21,868 (n=124)
- (8, 3, 4): -22,126 (n=61)
- (13, 3, 6): -22,174 (n=199)
- (10, 3, 5): -22,188 (n=44)

_Generated 2026-09-08 08:32. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 1845 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=1845); harvest_min=1–3 (n=1845); wheat_tiles=0–8 (n=1845); wheat_stock=0–40 (n=1845); min_hands=3–6 (n=1845); load_per_hand=12–26 (n=1845); geese=0–2 (n=1845); open_melons=4–14 (n=1845)
- **Evidence:** 1845 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 19 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=19); harvest_min=1–3 (n=19); wheat_tiles=0–2 (n=19); wheat_stock=0–4 (n=19); min_hands=3–6 (n=19); load_per_hand=19–21 (n=19); geese=0–2 (n=19); open_melons=7–13 (n=19)
- **Evidence:** 19 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 8 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–150 (n=8); harvest_min=1–3 (n=8); wheat_tiles=0; wheat_stock=0–6 (n=8); min_hands=3–6 (n=8); load_per_hand=15–20 (n=8); geese=0–1 (n=8); open_melons=9–10 (n=8)
- **Evidence:** 8 candidates, multiple seeds. Confidence: moderate

### LABOR_FAILURE (observed in 8 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=8); harvest_min=1–3 (n=8); wheat_tiles=0–6 (n=8); wheat_stock=0–20 (n=8); min_hands=3–6 (n=8); load_per_hand=12–17 (n=8); geese=0–2 (n=8); open_melons=8–14 (n=8)
- **Evidence:** 8 candidates, multiple seeds. Confidence: moderate

### None (observed in 4 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=150–200 (n=4); harvest_min=1–2 (n=4); wheat_tiles=0; wheat_stock=0–7 (n=4); min_hands=3–5 (n=4); load_per_hand=12–18 (n=4); geese=0–2 (n=4); open_melons=10–14 (n=4)
- **Evidence:** 4 candidates, multiple seeds. Confidence: low

_Generated 2026-09-08 08:32. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._