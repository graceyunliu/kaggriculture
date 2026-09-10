# Evolution run 20260910-020807

Frontier opponent: `H32.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1265 · games 22,264 (11,131/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 496 | 992 |
| dead_pattern | 200 | 400 |
| dead_smoke | 161 | 1288 |
| alive | 408 | 19584 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 19424 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2579
- M2: best -16,102 (`8b77b3e994bc`), n=2640
- c1: best -16,235 (`18fc0546be4a`), n=3417
- queue: best -15,412 (`fe4745b56024`), n=4535
- v312: best -15,275 (`52b3d5cc236e`), n=3158
- wide: best -16,047 (`512e53fe15bc`), n=3095

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +17,948 | 120 | 50 | 147 | 19417 | 66.89 | 120: -23,820 (n=11), 118: -25,349 (n=2), 138: -25,750 (n=2), 141: -28,023 (n=6), 5: -28,764 (n=59), 143: -28,964 (n=3), 112: -29,479 (n=14), 8: -29,645 (n=7), 26: -30,065 (n=10), 27: -30,093 (n=41), 89: -30,272 (n=33), 97: -30,318 (n=45), 106: -30,386 (n=47), 19: -30,408 (n=20), 18: -30,432 (n=1353), 74: -30,507 (n=436), 63: -30,516 (n=346), 70: -30,525 (n=88), 92: -30,526 (n=527), 35: -30,680 (n=18), 58: -30,690 (n=163), 48: -30,704 (n=574), 60: -30,728 (n=39), 150: -30,737 (n=310), 117: -30,761 (n=3), 49: -30,898 (n=104), 65: -30,930 (n=173), 50: -30,970 (n=9416), 80: -31,060 (n=19), 14: -31,104 (n=40), 56: -31,136 (n=25), 44: -31,246 (n=54), 61: -31,354 (n=127), 72: -31,449 (n=15), 86: -31,454 (n=10), 30: -31,479 (n=63), 42: -31,505 (n=971), 40: -31,524 (n=118), 94: -31,527 (n=22), 108: -31,642 (n=10), 66: -31,652 (n=381), 85: -31,657 (n=15), 73: -31,689 (n=22), 53: -31,712 (n=110), 104: -31,742 (n=6), 71: -31,786 (n=34), 36: -31,787 (n=158), 38: -31,829 (n=29), 45: -31,847 (n=128), 51: -31,851 (n=26), 144: -32,005 (n=12), 9: -32,055 (n=20), 57: -32,144 (n=90), 59: -32,226 (n=25), 33: -32,365 (n=27), 113: -32,418 (n=15), 55: -32,481 (n=790), 84: -32,503 (n=17), 25: -32,506 (n=12), 115: -32,512 (n=8), 39: -32,529 (n=62), 87: -32,535 (n=20), 28: -32,568 (n=23), 41: -32,597 (n=59), 96: -32,630 (n=8), 54: -32,637 (n=29), 62: -32,741 (n=24), 134: -32,782 (n=3), 17: -32,829 (n=12), 52: -32,865 (n=24), 109: -32,944 (n=4), 95: -32,957 (n=7), 125: -33,009 (n=2), 43: -33,057 (n=23), 110: -33,072 (n=7), 4: -33,111 (n=40), 122: -33,131 (n=2), 20: -33,148 (n=14), 98: -33,151 (n=21), 68: -33,247 (n=19), 6: -33,253 (n=15), 0: -33,284 (n=255), 93: -33,297 (n=10), 78: -33,339 (n=17), 21: -33,400 (n=13), 88: -33,411 (n=14), 2: -33,419 (n=4), 69: -33,518 (n=31), 103: -33,542 (n=11), 83: -33,580 (n=117), 22: -33,631 (n=18), 102: -33,689 (n=6), 119: -33,699 (n=3), 24: -33,703 (n=25), 47: -33,787 (n=38), 76: -33,828 (n=20), 31: -33,907 (n=20), 81: -33,909 (n=30), 13: -33,976 (n=8), 82: -33,994 (n=51), 32: -34,010 (n=14), 90: -34,046 (n=8), 15: -34,073 (n=13), 111: -34,111 (n=8), 135: -34,236 (n=2), 79: -34,292 (n=26), 64: -34,299 (n=26), 99: -34,315 (n=77), 1: -34,445 (n=10), 10: -34,451 (n=15), 11: -34,452 (n=20), 140: -34,453 (n=4), 46: -34,592 (n=40), 12: -34,899 (n=15), 101: -34,931 (n=14), 7: -35,071 (n=11), 107: -35,073 (n=7), 37: -35,173 (n=17), 16: -35,226 (n=20), 77: -35,263 (n=245), 34: -35,405 (n=75), 136: -35,491 (n=54), 3: -35,585 (n=8), 100: -35,654 (n=62), 91: -35,887 (n=10), 23: -35,936 (n=25), 129: -36,184 (n=98), 67: -36,238 (n=22), 75: -36,461 (n=15), 128: -36,508 (n=3), 105: -36,563 (n=3), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,511 (n=66), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,852 | 25 | 30 | 25 | 19424 | 11.2 | 25: -30,901 (n=9477), 26: -30,924 (n=706), 30: -31,134 (n=6354), 31: -31,867 (n=154), 29: -32,135 (n=158), 27: -32,316 (n=288), 28: -33,388 (n=1482), 32: -33,783 (n=195), 41: -34,307 (n=3), 35: -35,090 (n=201), 45: -35,319 (n=2), 33: -35,571 (n=156), 37: -35,857 (n=31), 34: -35,919 (n=82), 39: -36,046 (n=13), 38: -36,301 (n=27), 36: -36,887 (n=45), 42: -36,946 (n=4), 46: -38,521 (n=3), 40: -38,534 (n=17), 43: -38,819 (n=7), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,586 (n=9), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,240 | 1 | 0 | 35 | 19420 | 24.25 | 1: -30,286 (n=1835), 9: -30,936 (n=112), 0: -31,181 (n=15817), 22: -31,572 (n=3), 2: -32,639 (n=223), 6: -32,991 (n=148), 8: -33,091 (n=96), 4: -33,559 (n=140), 3: -34,354 (n=224), 19: -34,452 (n=9), 11: -34,800 (n=78), 17: -34,967 (n=19), 20: -34,967 (n=8), 5: -35,310 (n=219), 13: -35,358 (n=58), 7: -35,383 (n=116), 12: -35,562 (n=40), 28: -35,676 (n=3), 14: -35,930 (n=32), 16: -36,007 (n=22), 15: -36,357 (n=36), 23: -36,568 (n=8), 10: -36,838 (n=63), 18: -36,999 (n=24), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -37,938 (n=14), 26: -40,268 (n=3), 29: -40,739 (n=40), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,846 | 3 | 3 | 4 | 19424 | 2.61 | 3: -30,902 (n=17534), 2: -35,671 (n=1342), 4: -36,347 (n=527), 5: -42,748 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,270 | 6 | 6 | 8 | 19424 | 6.13 | 6: -30,798 (n=17316), 5: -34,668 (n=857), 7: -36,687 (n=468), 4: -37,562 (n=517), 3: -37,680 (n=157), 8: -38,143 (n=75), 9: -40,277 (n=26), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,460 | 13 | 20 | 11 | 19424 | 4.61 | 13: -30,568 (n=45), 16: -30,925 (n=420), 17: -31,064 (n=6613), 19: -31,247 (n=1059), 18: -31,355 (n=1017), 11: -31,405 (n=4), 14: -31,589 (n=149), 20: -31,621 (n=9904), 15: -32,287 (n=183), 12: -33,699 (n=22), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,124 | 10 | 8 | 11 | 19424 | 8.36 | 10: -30,819 (n=16532), 7: -32,293 (n=661), 8: -34,731 (n=1090), 9: -35,135 (n=656), 6: -35,285 (n=201), 5: -35,659 (n=33), 12: -38,004 (n=61), 11: -38,030 (n=84), 4: -38,147 (n=30), 14: -39,724 (n=33), 13: -40,943 (n=43) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +10,028 | 130 | 100 | 101 | 19424 | 61.87 | 130: -29,418 (n=15), 66: -29,609 (n=29), 80: -29,970 (n=459), 138: -30,059 (n=5), 93: -30,207 (n=448), 120: -30,329 (n=22), 81: -30,439 (n=97), 91: -30,512 (n=111), 50: -30,606 (n=231), 86: -30,627 (n=1076), 85: -30,667 (n=104), 62: -30,676 (n=9), 78: -30,927 (n=189), 123: -30,933 (n=57), 63: -30,948 (n=14), 100: -30,998 (n=12091), 90: -31,000 (n=197), 59: -31,163 (n=6), 125: -31,190 (n=95), 107: -31,246 (n=30), 111: -31,285 (n=45), 129: -31,300 (n=22), 61: -31,371 (n=3), 65: -31,453 (n=8), 115: -31,483 (n=36), 92: -31,526 (n=34), 147: -31,607 (n=7), 117: -31,687 (n=133), 133: -31,740 (n=10), 83: -31,769 (n=129), 99: -31,775 (n=47), 94: -31,834 (n=40), 103: -31,837 (n=34), 113: -31,924 (n=26), 87: -31,948 (n=25), 64: -31,993 (n=16), 84: -32,084 (n=110), 71: -32,191 (n=22), 102: -32,246 (n=47), 132: -32,285 (n=12), 95: -32,362 (n=47), 149: -32,426 (n=4), 110: -32,447 (n=32), 88: -32,448 (n=78), 70: -32,455 (n=21), 104: -32,471 (n=672), 53: -32,538 (n=6), 109: -32,558 (n=56), 105: -32,563 (n=142), 127: -32,669 (n=39), 114: -32,689 (n=34), 98: -32,694 (n=72), 119: -32,778 (n=24), 82: -32,862 (n=24), 67: -32,961 (n=12), 128: -33,010 (n=37), 76: -33,107 (n=25), 112: -33,122 (n=227), 97: -33,298 (n=60), 89: -33,305 (n=193), 57: -33,366 (n=7), 122: -33,424 (n=41), 68: -33,466 (n=12), 141: -33,486 (n=4), 69: -33,501 (n=14), 116: -33,583 (n=81), 96: -33,717 (n=56), 101: -33,730 (n=50), 55: -33,777 (n=5), 135: -33,822 (n=523), 126: -33,849 (n=30), 108: -34,015 (n=32), 74: -34,234 (n=37), 143: -34,383 (n=13), 75: -34,408 (n=62), 72: -34,412 (n=15), 134: -34,415 (n=10), 124: -34,455 (n=28), 136: -34,572 (n=8), 106: -34,604 (n=50), 121: -34,838 (n=20), 79: -34,957 (n=76), 137: -35,119 (n=6), 139: -35,190 (n=10), 144: -35,500 (n=3), 150: -35,867 (n=186), 56: -35,940 (n=6), 131: -35,981 (n=19), 52: -36,201 (n=4), 142: -36,242 (n=8), 118: -36,780 (n=18), 77: -37,054 (n=30), 73: -37,334 (n=16), 148: -37,549 (n=4), 51: -37,583 (n=6), 58: -37,802 (n=7), 140: -38,416 (n=3), 54: -38,470 (n=4), 146: -38,706 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +9,617 | 7 | 7 | 8 | 19424 | 6.14 | 7: -30,763 (n=17335), 6: -36,385 (n=1007), 5: -36,466 (n=84), 10: -36,631 (n=133), 8: -36,649 (n=649), 9: -37,320 (n=126), 4: -37,669 (n=80), 3: -40,380 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,602 | 20 | 20 | 15 | 19424 | 7.88 | 20: -30,731 (n=11501), 19: -30,912 (n=5420), 18: -31,606 (n=448), 17: -34,351 (n=776), 16: -36,379 (n=177), 21: -36,708 (n=413), 15: -37,300 (n=92), 23: -37,824 (n=111), 22: -37,886 (n=218), 26: -38,369 (n=50), 14: -38,699 (n=43), 13: -38,948 (n=21), 25: -39,194 (n=26), 24: -39,281 (n=105), 12: -40,333 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,524 | 0.0 | 0.0 | 13 | 19424 | 10.37 | 0.0: -31,058 (n=16984), 0.1: -33,142 (n=1172), 0.4: -33,669 (n=116), 0.2: -33,806 (n=701), 0.3: -33,962 (n=243), 0.5: -34,816 (n=68), 1.1: -34,978 (n=7), 0.7: -35,518 (n=19), 0.6: -36,870 (n=65), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -38,901 (n=10), 0.8: -40,582 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,235 | 0.55 | 0.5 | 15 | 19424 | 7.7 | 0.55: -30,466 (n=11269), 0.5: -31,757 (n=4433), 0.65: -31,815 (n=1356), 0.75: -32,353 (n=145), 0.7: -32,532 (n=345), 0.6: -33,396 (n=473), 0.45: -34,676 (n=572), 0.8: -34,710 (n=74), 0.9: -35,790 (n=13), 0.35: -35,872 (n=188), 0.4: -36,111 (n=225), 0.85: -36,532 (n=16), 0.95: -36,836 (n=4), 1.0: -38,742 (n=9), 0.3: -39,701 (n=302) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,503 | 2 | 2 | 4 | 19424 | 2.83 | 2: -31,129 (n=18609), 1: -37,020 (n=672), 3: -38,403 (n=50), 0: -39,632 (n=93) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +8,338 | 0 | 0 | 9 | 19424 | 7.18 | 0: -31,094 (n=17660), 1: -34,000 (n=917), 2: -34,246 (n=383), 3: -34,910 (n=288), 4: -35,064 (n=109), 5: -35,394 (n=26), 7: -35,571 (n=8), 6: -37,848 (n=28), 8: -39,432 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,177 | 13 | 12 | 11 | 19424 | 8.25 | 13: -30,843 (n=1640), 14: -31,286 (n=16325), 11: -32,204 (n=254), 12: -32,482 (n=803), 9: -32,792 (n=35), 6: -34,639 (n=5), 7: -34,770 (n=11), 10: -35,341 (n=310), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,097 | 14 | 13 | 9 | 19424 | 4.23 | 14: -31,073 (n=3477), 11: -31,166 (n=885), 13: -31,351 (n=11279), 12: -31,420 (n=2569), 15: -31,727 (n=617), 10: -32,965 (n=155), 16: -33,450 (n=357), 9: -36,819 (n=62), 8: -39,170 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,560 | frontier | frontier | 2 | 19424 | 0.91 | frontier: -31,063 (n=18578), v312: -38,623 (n=846) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 19424 | 9.58 | 6: -30,481 (n=23), 21: -30,839 (n=3618), 22: -30,925 (n=9785), 23: -31,341 (n=858), 14: -31,397 (n=30), 20: -31,426 (n=748), 16: -31,727 (n=123), 13: -32,285 (n=38), 17: -32,329 (n=920), 25: -32,643 (n=1501), 18: -32,954 (n=694), 24: -33,174 (n=487), 19: -33,237 (n=242), 15: -33,530 (n=65), 12: -34,065 (n=16), 9: -34,337 (n=57), 10: -34,840 (n=70), 11: -36,305 (n=39), 7: -36,543 (n=22), 5: -36,977 (n=82), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,170 | 2 | 2 | 3 | 19424 | 1.83 | 2: -31,020 (n=18337), 1: -37,638 (n=1017), 3: -38,189 (n=70) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,600 | 34 | 40 | 31 | 19424 | 7.74 | 34: -30,294 (n=362), 21: -30,358 (n=2), 49: -30,627 (n=515), 33: -30,758 (n=69), 38: -30,776 (n=4605), 43: -30,782 (n=5474), 44: -30,819 (n=570), 47: -30,890 (n=341), 45: -31,285 (n=869), 30: -31,296 (n=78), 37: -31,448 (n=771), 39: -31,669 (n=736), 26: -31,899 (n=70), 27: -31,953 (n=13), 25: -32,256 (n=9), 50: -32,269 (n=544), 28: -32,296 (n=22), 29: -32,324 (n=20), 32: -32,683 (n=70), 40: -32,782 (n=2988), 42: -32,943 (n=251), 41: -32,969 (n=163), 36: -33,103 (n=223), 31: -33,271 (n=50), 35: -33,302 (n=271), 46: -33,372 (n=147), 48: -33,969 (n=86), 20: -34,587 (n=64), 23: -35,631 (n=7), 24: -36,135 (n=26), 22: -36,894 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3596)
- (9, 3, 6): -16,461 (n=2548)
- (12, 4, 6): -16,525 (n=594)
- (10, 3, 6): -16,840 (n=3174)
- (8, 3, 5): -16,866 (n=334)
- (8, 3, 6): -17,253 (n=915)
- (10, 4, 6): -17,975 (n=2820)
- (11, 3, 6): -18,175 (n=674)
- (11, 4, 6): -19,867 (n=648)
- (17, 3, 6): -20,013 (n=71)
- (8, 4, 6): -21,051 (n=876)
- (13, 3, 6): -21,440 (n=372)
- (13, 4, 6): -21,564 (n=256)
- (14, 3, 6): -21,679 (n=286)
- (8, 3, 4): -22,126 (n=96)

_Generated 2026-09-10 04:08. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 9636 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=9636); harvest_min=1–3 (n=9636); wheat_tiles=0–8 (n=9636); wheat_stock=0–40 (n=9636); min_hands=3–6 (n=9636); load_per_hand=12–26 (n=9636); geese=0–2 (n=9636); open_melons=4–14 (n=9636)
- **Evidence:** 9636 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 122 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=122); harvest_min=1–3 (n=122); wheat_tiles=0–2 (n=122); wheat_stock=0–6 (n=122); min_hands=3–6 (n=122); load_per_hand=15–23 (n=122); geese=0–2 (n=122); open_melons=7–13 (n=122)
- **Evidence:** 122 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 70 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=70); harvest_min=1–3 (n=70); wheat_tiles=0–3 (n=70); wheat_stock=0–40 (n=70); min_hands=3–6 (n=70); load_per_hand=12–26 (n=70); geese=0–2 (n=70); open_melons=4–13 (n=70)
- **Evidence:** 70 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 49 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=49); harvest_min=1–3 (n=49); wheat_tiles=0–8 (n=49); wheat_stock=0–39 (n=49); min_hands=3–6 (n=49); load_per_hand=12–23 (n=49); geese=0–2 (n=49); open_melons=6–14 (n=49)
- **Evidence:** 49 candidates, multiple seeds. Confidence: high

### None (observed in 23 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=23); harvest_min=1–3 (n=23); wheat_tiles=0; wheat_stock=0–11 (n=23); min_hands=3–6 (n=23); load_per_hand=12–18 (n=23); geese=0–2 (n=23); open_melons=7–14 (n=23)
- **Evidence:** 23 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 04:08. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._