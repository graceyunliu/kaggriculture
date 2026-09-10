# Evolution run 20260910-000226

Frontier opponent: `H32.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1262 · games 22,182 (11,086/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 471 | 942 |
| dead_pattern | 208 | 416 |
| dead_smoke | 179 | 1432 |
| alive | 404 | 19392 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 19016 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2510
- M2: best -16,102 (`8b77b3e994bc`), n=2587
- c1: best -16,235 (`18fc0546be4a`), n=3357
- queue: best -15,412 (`fe4745b56024`), n=4449
- v312: best -15,275 (`52b3d5cc236e`), n=3097
- wide: best -16,047 (`512e53fe15bc`), n=3016

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 147 | 19007 | 65.85 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 5: -28,605 (n=57), 143: -28,964 (n=3), 112: -29,479 (n=14), 8: -29,645 (n=7), 19: -30,031 (n=19), 26: -30,065 (n=10), 27: -30,093 (n=41), 89: -30,259 (n=32), 97: -30,318 (n=45), 106: -30,386 (n=47), 18: -30,435 (n=1323), 63: -30,483 (n=339), 74: -30,504 (n=427), 92: -30,511 (n=517), 70: -30,614 (n=86), 35: -30,680 (n=18), 48: -30,690 (n=573), 150: -30,712 (n=296), 58: -30,728 (n=160), 60: -30,728 (n=39), 117: -30,761 (n=3), 65: -30,800 (n=168), 50: -30,943 (n=9208), 49: -30,992 (n=99), 44: -30,998 (n=50), 80: -31,115 (n=18), 56: -31,136 (n=25), 51: -31,223 (n=23), 71: -31,310 (n=32), 14: -31,315 (n=38), 61: -31,354 (n=127), 72: -31,449 (n=15), 144: -31,452 (n=10), 86: -31,454 (n=10), 30: -31,479 (n=63), 42: -31,482 (n=959), 40: -31,524 (n=118), 94: -31,527 (n=22), 53: -31,559 (n=107), 66: -31,620 (n=370), 108: -31,642 (n=10), 85: -31,657 (n=15), 73: -31,689 (n=22), 104: -31,742 (n=6), 36: -31,779 (n=156), 45: -31,865 (n=127), 110: -31,921 (n=6), 38: -31,931 (n=28), 9: -32,055 (n=20), 57: -32,144 (n=90), 59: -32,226 (n=25), 33: -32,365 (n=27), 113: -32,418 (n=15), 17: -32,418 (n=11), 84: -32,503 (n=17), 25: -32,506 (n=12), 115: -32,512 (n=8), 39: -32,529 (n=62), 55: -32,540 (n=768), 28: -32,568 (n=23), 96: -32,630 (n=8), 54: -32,651 (n=28), 41: -32,701 (n=58), 62: -32,741 (n=24), 87: -32,742 (n=19), 134: -32,782 (n=3), 52: -32,865 (n=24), 109: -32,944 (n=4), 125: -33,009 (n=2), 4: -33,017 (n=39), 103: -33,035 (n=10), 43: -33,057 (n=23), 98: -33,151 (n=21), 0: -33,200 (n=247), 68: -33,247 (n=19), 93: -33,297 (n=10), 20: -33,308 (n=13), 78: -33,339 (n=17), 6: -33,368 (n=14), 21: -33,400 (n=13), 2: -33,419 (n=4), 95: -33,425 (n=6), 47: -33,518 (n=37), 69: -33,518 (n=31), 83: -33,571 (n=116), 22: -33,631 (n=18), 102: -33,689 (n=6), 119: -33,699 (n=3), 24: -33,703 (n=25), 88: -33,782 (n=13), 76: -33,828 (n=20), 31: -33,907 (n=20), 81: -33,909 (n=30), 13: -33,976 (n=8), 64: -34,024 (n=25), 90: -34,046 (n=8), 15: -34,073 (n=13), 111: -34,111 (n=8), 82: -34,211 (n=50), 135: -34,236 (n=2), 1: -34,246 (n=9), 79: -34,292 (n=26), 32: -34,300 (n=13), 99: -34,315 (n=77), 10: -34,451 (n=15), 11: -34,452 (n=20), 140: -34,453 (n=4), 46: -34,592 (n=40), 101: -34,712 (n=13), 7: -34,821 (n=10), 12: -34,899 (n=15), 107: -35,073 (n=7), 37: -35,173 (n=17), 16: -35,226 (n=20), 77: -35,263 (n=245), 34: -35,375 (n=74), 136: -35,375 (n=52), 3: -35,585 (n=8), 100: -35,645 (n=61), 91: -35,887 (n=10), 129: -36,114 (n=94), 23: -36,171 (n=24), 67: -36,405 (n=21), 75: -36,461 (n=15), 128: -36,508 (n=3), 105: -36,563 (n=3), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,651 (n=62), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,877 | 26 | 30 | 25 | 19016 | 11.2 | 26: -30,875 (n=690), 25: -30,883 (n=9279), 30: -31,111 (n=6221), 31: -31,691 (n=151), 29: -31,955 (n=154), 27: -32,329 (n=283), 28: -33,407 (n=1447), 32: -33,821 (n=190), 41: -34,307 (n=3), 35: -35,070 (n=200), 45: -35,319 (n=2), 33: -35,549 (n=151), 37: -35,857 (n=31), 34: -35,865 (n=80), 39: -36,046 (n=13), 38: -36,301 (n=27), 36: -36,731 (n=44), 42: -36,946 (n=4), 46: -38,521 (n=3), 40: -38,534 (n=17), 43: -38,819 (n=7), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,586 (n=9), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,304 | 1 | 0 | 35 | 19012 | 24.32 | 1: -30,222 (n=1753), 9: -30,947 (n=111), 0: -31,165 (n=15530), 22: -31,572 (n=3), 2: -32,639 (n=219), 6: -32,992 (n=143), 8: -33,067 (n=95), 4: -33,512 (n=138), 3: -34,362 (n=219), 19: -34,452 (n=9), 11: -34,779 (n=76), 20: -34,967 (n=8), 17: -35,013 (n=18), 5: -35,215 (n=208), 13: -35,336 (n=56), 7: -35,383 (n=116), 12: -35,653 (n=39), 28: -35,676 (n=3), 16: -35,930 (n=21), 14: -35,930 (n=32), 15: -36,357 (n=36), 23: -36,568 (n=8), 10: -36,951 (n=61), 18: -36,999 (n=24), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -37,938 (n=14), 26: -40,268 (n=3), 29: -40,605 (n=39), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,868 | 3 | 3 | 4 | 19016 | 2.61 | 3: -30,880 (n=17166), 2: -35,687 (n=1311), 4: -36,327 (n=518), 5: -42,748 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,290 | 6 | 6 | 8 | 19016 | 6.13 | 6: -30,777 (n=16952), 5: -34,708 (n=842), 7: -36,645 (n=458), 4: -37,517 (n=500), 3: -37,681 (n=156), 8: -38,140 (n=74), 9: -40,277 (n=26), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,100 | 66 | 100 | 101 | 19016 | 61.98 | 66: -28,346 (n=24), 130: -29,880 (n=14), 80: -29,969 (n=443), 138: -30,059 (n=5), 93: -30,196 (n=444), 120: -30,212 (n=21), 81: -30,445 (n=95), 86: -30,577 (n=1048), 91: -30,590 (n=108), 85: -30,616 (n=102), 50: -30,644 (n=210), 62: -30,676 (n=9), 90: -30,848 (n=191), 123: -30,933 (n=57), 78: -30,961 (n=177), 100: -30,973 (n=11857), 59: -31,163 (n=6), 125: -31,190 (n=95), 107: -31,246 (n=30), 111: -31,285 (n=45), 129: -31,300 (n=22), 61: -31,371 (n=3), 65: -31,453 (n=8), 117: -31,470 (n=129), 115: -31,483 (n=36), 92: -31,526 (n=34), 147: -31,607 (n=7), 94: -31,629 (n=38), 133: -31,740 (n=10), 83: -31,766 (n=127), 99: -31,775 (n=47), 103: -31,837 (n=34), 113: -31,924 (n=26), 84: -31,930 (n=104), 87: -31,948 (n=25), 64: -31,993 (n=16), 71: -32,191 (n=22), 102: -32,238 (n=46), 95: -32,284 (n=46), 132: -32,285 (n=12), 63: -32,321 (n=11), 109: -32,417 (n=53), 149: -32,426 (n=4), 88: -32,448 (n=77), 104: -32,451 (n=667), 70: -32,455 (n=21), 53: -32,538 (n=6), 82: -32,585 (n=23), 105: -32,589 (n=138), 128: -32,634 (n=35), 127: -32,669 (n=39), 114: -32,689 (n=34), 119: -32,778 (n=24), 110: -32,812 (n=30), 98: -32,826 (n=71), 67: -32,961 (n=12), 112: -33,179 (n=226), 76: -33,193 (n=24), 97: -33,298 (n=60), 57: -33,366 (n=7), 89: -33,424 (n=188), 122: -33,424 (n=41), 68: -33,466 (n=12), 141: -33,486 (n=4), 69: -33,501 (n=14), 116: -33,583 (n=81), 126: -33,677 (n=28), 101: -33,730 (n=50), 55: -33,777 (n=5), 135: -33,798 (n=518), 108: -33,977 (n=31), 96: -34,132 (n=52), 74: -34,234 (n=37), 72: -34,325 (n=14), 143: -34,383 (n=13), 75: -34,408 (n=62), 134: -34,415 (n=10), 124: -34,455 (n=28), 136: -34,572 (n=8), 79: -34,653 (n=67), 106: -34,688 (n=49), 121: -34,821 (n=19), 137: -35,119 (n=6), 139: -35,190 (n=10), 144: -35,500 (n=3), 150: -35,843 (n=184), 56: -35,940 (n=6), 131: -35,981 (n=19), 52: -36,201 (n=4), 142: -36,242 (n=8), 118: -37,178 (n=17), 73: -37,334 (n=16), 77: -37,410 (n=29), 148: -37,549 (n=4), 51: -37,583 (n=6), 58: -37,802 (n=7), 140: -38,416 (n=3), 54: -38,470 (n=4), 146: -38,706 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,460 | 13 | 20 | 11 | 19016 | 4.62 | 13: -30,568 (n=45), 16: -30,946 (n=412), 17: -31,047 (n=6475), 19: -31,285 (n=1034), 18: -31,317 (n=986), 14: -31,562 (n=147), 20: -31,597 (n=9709), 15: -32,134 (n=175), 11: -32,310 (n=3), 12: -33,699 (n=22), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,152 | 10 | 8 | 11 | 19016 | 8.36 | 10: -30,791 (n=16175), 7: -32,364 (n=638), 8: -34,738 (n=1080), 9: -35,123 (n=647), 6: -35,285 (n=201), 5: -35,831 (n=32), 12: -37,822 (n=56), 11: -38,032 (n=82), 4: -38,095 (n=29), 14: -39,724 (n=33), 13: -40,943 (n=43) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,127 | 7 | 7 | 8 | 19016 | 6.14 | 7: -30,737 (n=16961), 6: -36,385 (n=993), 5: -36,427 (n=82), 10: -36,631 (n=133), 8: -36,677 (n=635), 9: -37,355 (n=125), 4: -37,654 (n=78), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,631 | 20 | 20 | 15 | 19016 | 7.86 | 20: -30,702 (n=11228), 19: -30,912 (n=5331), 18: -31,576 (n=440), 17: -34,332 (n=766), 16: -36,351 (n=176), 21: -36,668 (n=402), 15: -37,350 (n=91), 23: -37,800 (n=110), 22: -37,868 (n=211), 26: -38,369 (n=50), 14: -38,583 (n=42), 13: -38,948 (n=21), 25: -39,264 (n=25), 24: -39,357 (n=100), 12: -40,333 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,544 | 0.0 | 0.0 | 13 | 19016 | 10.36 | 0.0: -31,038 (n=16622), 0.1: -33,114 (n=1149), 0.4: -33,632 (n=114), 0.2: -33,806 (n=693), 0.3: -33,949 (n=237), 0.5: -34,588 (n=65), 1.1: -34,978 (n=7), 0.7: -35,518 (n=19), 0.6: -37,016 (n=61), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -38,901 (n=10), 0.8: -40,582 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,299 | 0.55 | 0.5 | 15 | 19016 | 7.68 | 0.55: -30,435 (n=11005), 0.5: -31,767 (n=4375), 0.65: -31,785 (n=1339), 0.75: -32,376 (n=141), 0.7: -32,507 (n=333), 0.6: -33,369 (n=460), 0.8: -34,611 (n=72), 0.45: -34,671 (n=555), 0.9: -35,790 (n=13), 0.35: -35,925 (n=182), 0.4: -36,076 (n=217), 0.85: -36,532 (n=16), 0.95: -36,836 (n=4), 1.0: -38,742 (n=9), 0.3: -39,734 (n=295) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +8,859 | 0 | 0 | 9 | 19016 | 7.18 | 0: -31,073 (n=17280), 1: -33,979 (n=903), 2: -34,244 (n=378), 3: -34,902 (n=285), 4: -35,072 (n=106), 7: -35,103 (n=7), 5: -35,394 (n=26), 6: -37,768 (n=27), 8: -39,932 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,532 | 14 | 13 | 9 | 19016 | 4.24 | 14: -31,011 (n=3381), 11: -31,150 (n=875), 13: -31,334 (n=11073), 12: -31,451 (n=2506), 15: -31,625 (n=600), 10: -33,021 (n=153), 16: -33,523 (n=345), 9: -36,758 (n=61), 8: -39,543 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,478 | 2 | 2 | 4 | 19016 | 2.83 | 2: -31,111 (n=18228), 1: -37,053 (n=647), 3: -38,403 (n=50), 0: -39,589 (n=91) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,173 | 13 | 12 | 11 | 19016 | 8.25 | 13: -30,848 (n=1597), 14: -31,261 (n=15988), 11: -32,261 (n=248), 12: -32,495 (n=788), 9: -32,792 (n=35), 6: -34,388 (n=4), 7: -34,770 (n=11), 10: -35,337 (n=304), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,568 | frontier | frontier | 2 | 19016 | 0.91 | frontier: -31,045 (n=18192), v312: -38,613 (n=824) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 19016 | 9.56 | 6: -30,481 (n=23), 21: -30,805 (n=3515), 22: -30,900 (n=9564), 23: -31,363 (n=847), 20: -31,397 (n=742), 14: -31,397 (n=30), 16: -31,685 (n=120), 17: -32,334 (n=901), 25: -32,600 (n=1477), 13: -32,670 (n=34), 18: -32,951 (n=692), 24: -33,161 (n=483), 19: -33,251 (n=238), 15: -33,498 (n=62), 12: -34,065 (n=16), 9: -34,279 (n=56), 10: -34,840 (n=70), 11: -36,305 (n=39), 7: -36,543 (n=22), 5: -36,906 (n=79), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,287 | 2 | 2 | 3 | 19016 | 1.83 | 2: -30,998 (n=17946), 1: -37,614 (n=1002), 3: -38,286 (n=68) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,641 | 34 | 40 | 31 | 19016 | 7.74 | 34: -30,252 (n=353), 21: -30,358 (n=2), 49: -30,593 (n=505), 38: -30,749 (n=4494), 43: -30,755 (n=5361), 33: -30,758 (n=69), 44: -30,800 (n=561), 47: -30,853 (n=338), 45: -31,279 (n=838), 30: -31,296 (n=78), 27: -31,404 (n=12), 37: -31,410 (n=750), 39: -31,655 (n=708), 26: -31,918 (n=68), 25: -32,256 (n=9), 28: -32,296 (n=22), 50: -32,316 (n=524), 29: -32,324 (n=20), 32: -32,620 (n=69), 40: -32,777 (n=2970), 42: -32,976 (n=248), 36: -33,045 (n=220), 31: -33,049 (n=48), 41: -33,080 (n=158), 35: -33,181 (n=262), 46: -33,205 (n=142), 48: -34,128 (n=85), 20: -34,458 (n=61), 23: -35,631 (n=7), 24: -36,135 (n=26), 22: -36,894 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3524)
- (9, 3, 6): -16,461 (n=2492)
- (12, 4, 6): -16,525 (n=582)
- (10, 3, 6): -16,840 (n=3115)
- (8, 3, 5): -16,866 (n=324)
- (8, 3, 6): -17,253 (n=899)
- (10, 4, 6): -17,975 (n=2757)
- (11, 3, 6): -18,175 (n=661)
- (11, 4, 6): -19,867 (n=636)
- (17, 3, 6): -20,013 (n=69)
- (8, 4, 6): -21,051 (n=855)
- (13, 4, 6): -21,564 (n=248)
- (14, 3, 6): -21,679 (n=276)
- (13, 3, 6): -21,783 (n=365)
- (8, 3, 4): -22,126 (n=95)

_Generated 2026-09-10 02:02. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 9290 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=9290); harvest_min=1–3 (n=9290); wheat_tiles=0–8 (n=9290); wheat_stock=0–40 (n=9290); min_hands=3–6 (n=9290); load_per_hand=12–26 (n=9290); geese=0–2 (n=9290); open_melons=4–14 (n=9290)
- **Evidence:** 9290 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 117 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=117); harvest_min=1–3 (n=117); wheat_tiles=0–2 (n=117); wheat_stock=0–6 (n=117); min_hands=3–6 (n=117); load_per_hand=15–23 (n=117); geese=0–2 (n=117); open_melons=7–13 (n=117)
- **Evidence:** 117 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 66 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=66); harvest_min=1–3 (n=66); wheat_tiles=0–3 (n=66); wheat_stock=0–40 (n=66); min_hands=3–6 (n=66); load_per_hand=12–26 (n=66); geese=0–2 (n=66); open_melons=4–13 (n=66)
- **Evidence:** 66 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 45 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=45); harvest_min=1–3 (n=45); wheat_tiles=0–8 (n=45); wheat_stock=0–39 (n=45); min_hands=3–6 (n=45); load_per_hand=12–23 (n=45); geese=0–2 (n=45); open_melons=6–14 (n=45)
- **Evidence:** 45 candidates, multiple seeds. Confidence: high

### None (observed in 21 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=21); harvest_min=1–3 (n=21); wheat_tiles=0; wheat_stock=0–11 (n=21); min_hands=3–6 (n=21); load_per_hand=12–18 (n=21); geese=0–2 (n=21); open_melons=7–14 (n=21)
- **Evidence:** 21 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 02:02. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._