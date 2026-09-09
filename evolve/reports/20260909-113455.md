# Evolution run 20260909-113455

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1280 · games 22,894 (11,442/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 466 | 932 |
| dead_pattern | 205 | 410 |
| dead_smoke | 192 | 1536 |
| alive | 417 | 20016 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 16549 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2112
- M2: best -16,102 (`8b77b3e994bc`), n=2196
- c1: best -16,310 (`23734cef4da1`), n=2963
- queue: best -15,412 (`fe4745b56024`), n=3938
- v312: best -15,275 (`52b3d5cc236e`), n=2741
- wide: best -16,047 (`512e53fe15bc`), n=2599

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 146 | 16539 | 65.75 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 5: -28,740 (n=53), 143: -28,964 (n=3), 106: -29,265 (n=29), 19: -29,285 (n=17), 8: -29,345 (n=5), 112: -29,479 (n=14), 27: -29,534 (n=37), 18: -30,086 (n=1074), 89: -30,144 (n=31), 58: -30,262 (n=134), 92: -30,279 (n=444), 63: -30,324 (n=276), 80: -30,353 (n=16), 97: -30,383 (n=37), 26: -30,432 (n=8), 74: -30,447 (n=330), 49: -30,577 (n=89), 71: -30,666 (n=30), 48: -30,673 (n=550), 108: -30,721 (n=8), 56: -30,810 (n=16), 35: -30,835 (n=16), 50: -30,872 (n=8117), 65: -30,913 (n=150), 150: -30,961 (n=236), 61: -31,063 (n=112), 70: -31,241 (n=55), 30: -31,259 (n=46), 14: -31,314 (n=28), 60: -31,365 (n=31), 42: -31,378 (n=857), 40: -31,384 (n=105), 86: -31,454 (n=10), 94: -31,527 (n=22), 85: -31,546 (n=13), 51: -31,555 (n=21), 66: -31,567 (n=317), 25: -31,648 (n=9), 72: -31,710 (n=11), 45: -31,770 (n=122), 9: -31,785 (n=18), 33: -31,832 (n=25), 57: -31,917 (n=85), 62: -31,937 (n=20), 53: -31,952 (n=66), 144: -32,007 (n=8), 36: -32,084 (n=126), 113: -32,147 (n=14), 73: -32,194 (n=19), 110: -32,277 (n=4), 39: -32,343 (n=58), 38: -32,416 (n=20), 44: -32,430 (n=31), 103: -32,462 (n=9), 84: -32,465 (n=16), 115: -32,512 (n=8), 54: -32,622 (n=26), 96: -32,630 (n=8), 59: -32,632 (n=24), 104: -32,639 (n=5), 55: -32,803 (n=662), 109: -32,844 (n=3), 98: -32,926 (n=20), 69: -32,979 (n=27), 87: -32,981 (n=17), 4: -33,017 (n=39), 41: -33,060 (n=53), 88: -33,112 (n=12), 76: -33,214 (n=16), 68: -33,247 (n=19), 31: -33,271 (n=15), 78: -33,288 (n=16), 93: -33,297 (n=10), 0: -33,302 (n=220), 52: -33,375 (n=22), 95: -33,449 (n=5), 13: -33,499 (n=7), 83: -33,566 (n=112), 21: -33,604 (n=12), 43: -33,659 (n=21), 1: -33,664 (n=8), 119: -33,699 (n=3), 24: -33,712 (n=23), 28: -33,719 (n=20), 81: -33,724 (n=28), 2: -33,749 (n=3), 90: -33,822 (n=7), 22: -33,894 (n=17), 6: -34,026 (n=12), 20: -34,074 (n=8), 111: -34,111 (n=8), 102: -34,126 (n=5), 11: -34,164 (n=17), 17: -34,168 (n=8), 82: -34,211 (n=50), 64: -34,259 (n=22), 47: -34,265 (n=28), 99: -34,384 (n=74), 15: -34,394 (n=12), 46: -34,449 (n=39), 10: -34,451 (n=15), 140: -34,453 (n=4), 134: -34,464 (n=2), 107: -34,481 (n=6), 37: -34,598 (n=14), 7: -34,904 (n=9), 101: -34,988 (n=12), 136: -34,994 (n=46), 79: -35,034 (n=16), 32: -35,077 (n=10), 77: -35,209 (n=237), 34: -35,291 (n=68), 16: -35,335 (n=18), 100: -35,505 (n=53), 23: -35,508 (n=15), 12: -35,552 (n=13), 91: -35,887 (n=10), 129: -35,956 (n=87), 128: -36,508 (n=3), 75: -36,535 (n=12), 3: -36,563 (n=6), 105: -36,563 (n=3), 117: -36,604 (n=2), 67: -36,770 (n=19), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,571 (n=46), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,010 | 26 | 30 | 25 | 16549 | 11.2 | 26: -30,743 (n=582), 25: -30,796 (n=8079), 30: -31,043 (n=5369), 31: -31,704 (n=139), 29: -32,246 (n=139), 27: -32,425 (n=249), 28: -33,483 (n=1298), 32: -34,108 (n=155), 41: -34,307 (n=3), 35: -34,838 (n=183), 45: -35,319 (n=2), 33: -35,486 (n=136), 37: -35,762 (n=28), 38: -35,963 (n=23), 39: -36,046 (n=13), 34: -36,088 (n=68), 42: -36,946 (n=4), 36: -36,973 (n=40), 46: -38,521 (n=3), 40: -38,691 (n=13), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,351 | 1 | 0 | 34 | 16546 | 24.8 | 1: -30,176 (n=1304), 9: -31,057 (n=101), 0: -31,105 (n=13769), 22: -31,539 (n=2), 2: -32,540 (n=177), 6: -33,005 (n=118), 4: -33,094 (n=107), 8: -33,120 (n=88), 17: -34,084 (n=15), 3: -34,271 (n=192), 19: -34,273 (n=7), 11: -34,865 (n=70), 5: -34,990 (n=177), 7: -35,467 (n=100), 16: -35,482 (n=15), 28: -35,676 (n=3), 13: -35,734 (n=51), 12: -35,786 (n=35), 14: -36,080 (n=25), 20: -36,357 (n=6), 15: -36,496 (n=32), 18: -36,728 (n=20), 23: -36,978 (n=7), 24: -37,048 (n=7), 10: -37,150 (n=51), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,996 (n=10), 26: -40,268 (n=3), 29: -41,186 (n=31), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,809 | 3 | 3 | 4 | 16549 | 2.61 | 3: -30,819 (n=14932), 2: -35,715 (n=1147), 4: -36,368 (n=450), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 16549 | 62.5 | 61: -27,918 (n=2), 138: -27,990 (n=3), 80: -29,658 (n=298), 120: -29,850 (n=16), 130: -29,880 (n=14), 93: -30,037 (n=422), 81: -30,320 (n=86), 85: -30,459 (n=100), 86: -30,541 (n=867), 91: -30,637 (n=98), 92: -30,793 (n=28), 100: -30,877 (n=10405), 129: -31,008 (n=20), 90: -31,109 (n=131), 123: -31,156 (n=52), 125: -31,171 (n=93), 113: -31,180 (n=20), 111: -31,208 (n=40), 50: -31,226 (n=108), 107: -31,262 (n=27), 94: -31,336 (n=35), 99: -31,340 (n=42), 78: -31,348 (n=128), 55: -31,425 (n=4), 65: -31,427 (n=7), 117: -31,436 (n=114), 141: -31,447 (n=3), 115: -31,483 (n=36), 119: -31,499 (n=18), 62: -31,557 (n=8), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,651 (n=118), 87: -31,688 (n=23), 103: -31,723 (n=31), 133: -31,740 (n=10), 67: -31,763 (n=10), 84: -31,869 (n=83), 114: -31,963 (n=30), 70: -32,127 (n=19), 95: -32,141 (n=42), 105: -32,173 (n=119), 132: -32,285 (n=12), 53: -32,306 (n=5), 109: -32,315 (n=42), 63: -32,321 (n=11), 102: -32,323 (n=44), 66: -32,337 (n=14), 149: -32,426 (n=4), 104: -32,500 (n=604), 71: -32,523 (n=21), 57: -32,552 (n=6), 82: -32,585 (n=23), 127: -32,621 (n=35), 110: -32,680 (n=25), 88: -32,875 (n=72), 128: -33,003 (n=30), 97: -33,103 (n=56), 76: -33,119 (n=19), 69: -33,122 (n=10), 112: -33,175 (n=216), 122: -33,237 (n=39), 98: -33,241 (n=60), 101: -33,246 (n=41), 89: -33,441 (n=169), 68: -33,455 (n=11), 134: -33,531 (n=8), 126: -33,677 (n=28), 116: -33,722 (n=75), 135: -33,782 (n=487), 59: -33,898 (n=4), 96: -34,020 (n=45), 124: -34,105 (n=25), 74: -34,107 (n=34), 121: -34,131 (n=14), 136: -34,218 (n=7), 75: -34,489 (n=59), 108: -34,512 (n=27), 79: -34,559 (n=50), 143: -34,578 (n=12), 137: -34,596 (n=5), 144: -34,772 (n=2), 72: -34,820 (n=13), 106: -34,948 (n=46), 150: -35,774 (n=173), 131: -35,807 (n=15), 56: -35,940 (n=6), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 77: -36,490 (n=26), 148: -36,528 (n=3), 118: -36,915 (n=15), 58: -37,611 (n=6), 146: -37,838 (n=2), 73: -38,056 (n=12), 51: -38,207 (n=4), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,332 | 6 | 6 | 8 | 16549 | 6.14 | 6: -30,735 (n=14761), 5: -34,659 (n=731), 7: -36,425 (n=409), 4: -37,460 (n=419), 3: -37,777 (n=135), 8: -38,040 (n=62), 9: -40,202 (n=24), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,391 | 13 | 20 | 11 | 16549 | 4.72 | 13: -30,636 (n=38), 17: -30,936 (n=5537), 16: -30,969 (n=366), 14: -31,141 (n=126), 19: -31,307 (n=874), 18: -31,353 (n=828), 20: -31,563 (n=8607), 15: -32,291 (n=144), 11: -32,310 (n=3), 12: -33,410 (n=18), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +10,198 | 0.0 | 0.0 | 13 | 16549 | 10.31 | 0.0: -30,966 (n=14399), 0.1: -33,109 (n=1040), 0.2: -33,815 (n=627), 0.4: -34,038 (n=96), 0.3: -34,039 (n=203), 0.5: -34,533 (n=58), 1.1: -34,978 (n=7), 0.7: -35,656 (n=18), 0.6: -36,747 (n=54), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -39,081 (n=9), 0.8: -41,164 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,189 | 7 | 7 | 8 | 16549 | 6.13 | 7: -30,675 (n=14739), 5: -36,260 (n=72), 6: -36,395 (n=906), 8: -36,627 (n=537), 10: -36,768 (n=123), 9: -37,226 (n=107), 4: -37,953 (n=56), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,150 | 20 | 20 | 15 | 16549 | 7.65 | 20: -30,598 (n=9539), 19: -30,934 (n=4839), 18: -31,496 (n=386), 17: -34,357 (n=718), 16: -36,391 (n=153), 21: -36,612 (n=341), 15: -37,329 (n=74), 23: -37,601 (n=89), 22: -37,932 (n=184), 14: -38,330 (n=37), 26: -38,582 (n=41), 24: -39,206 (n=89), 25: -39,407 (n=22), 13: -39,593 (n=18), 12: -40,748 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,090 | 10 | 8 | 11 | 16549 | 8.34 | 10: -30,718 (n=14057), 7: -32,564 (n=518), 8: -34,688 (n=984), 9: -35,050 (n=567), 6: -35,295 (n=181), 5: -36,429 (n=25), 12: -37,763 (n=53), 4: -38,022 (n=25), 11: -38,117 (n=72), 14: -39,871 (n=31), 13: -40,807 (n=36) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,646 | 0 | 0 | 9 | 16549 | 7.17 | 0: -31,012 (n=15028), 1: -34,026 (n=793), 2: -34,387 (n=331), 3: -34,795 (n=248), 7: -35,103 (n=7), 4: -35,199 (n=92), 5: -35,653 (n=22), 6: -37,663 (n=25), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,529 | 0.55 | 0.5 | 15 | 16549 | 7.44 | 0.55: -30,310 (n=9311), 0.65: -31,771 (n=1250), 0.5: -31,789 (n=3984), 0.75: -32,213 (n=122), 0.7: -32,332 (n=281), 0.6: -33,218 (n=399), 0.8: -34,324 (n=56), 0.45: -34,630 (n=504), 0.9: -35,465 (n=11), 0.4: -36,078 (n=188), 0.35: -36,121 (n=163), 0.85: -36,511 (n=15), 0.95: -37,209 (n=3), 1.0: -38,525 (n=8), 0.3: -39,840 (n=254) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,459 | 14 | 13 | 9 | 16549 | 4.29 | 14: -30,881 (n=2787), 11: -31,247 (n=808), 13: -31,289 (n=9728), 12: -31,382 (n=2215), 15: -31,677 (n=521), 10: -33,131 (n=133), 16: -33,525 (n=284), 9: -36,779 (n=52), 8: -39,340 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,315 | 2 | 2 | 4 | 16549 | 2.84 | 2: -31,072 (n=15890), 1: -37,013 (n=541), 3: -38,431 (n=42), 0: -39,387 (n=76) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,286 | 13 | 12 | 11 | 16549 | 8.26 | 13: -30,735 (n=1334), 14: -31,187 (n=13934), 11: -32,537 (n=226), 12: -32,681 (n=699), 6: -34,388 (n=4), 9: -34,437 (n=29), 10: -35,326 (n=274), 7: -35,686 (n=10), 8: -36,793 (n=34), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,192 | 6 | 18 | 21 | 16549 | 9.46 | 6: -30,437 (n=21), 21: -30,672 (n=2989), 14: -30,829 (n=25), 22: -30,833 (n=8241), 20: -31,312 (n=691), 23: -31,316 (n=744), 16: -31,862 (n=104), 17: -32,428 (n=798), 25: -32,544 (n=1311), 18: -32,917 (n=631), 24: -33,138 (n=440), 15: -33,378 (n=55), 19: -33,404 (n=213), 13: -33,638 (n=26), 9: -34,016 (n=52), 12: -34,505 (n=12), 10: -34,816 (n=68), 11: -36,130 (n=35), 5: -36,522 (n=66), 7: -36,543 (n=22), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,533 | frontier | frontier | 2 | 16549 | 0.92 | frontier: -31,006 (n=15852), v312: -38,540 (n=697) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,466 | 2 | 2 | 3 | 16549 | 1.83 | 2: -30,940 (n=15599), 1: -37,564 (n=894), 3: -38,407 (n=56) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +6,690 | 0.05 | 0.25 | 11 | 16549 | 4.95 | 0.05: -30,389 (n=2363), 0.2: -30,839 (n=1962), 0.4: -30,891 (n=359), 0.15: -30,947 (n=952), 0.0: -31,122 (n=578), 0.25: -31,518 (n=8947), 0.1: -31,800 (n=589), 0.3: -32,772 (n=301), 0.35: -33,421 (n=369), 0.45: -34,344 (n=68), 0.5: -37,079 (n=61) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3082)
- (9, 3, 6): -16,578 (n=2119)
- (10, 3, 6): -16,840 (n=2722)
- (8, 3, 5): -16,866 (n=290)
- (12, 4, 6): -17,058 (n=511)
- (8, 3, 6): -17,552 (n=809)
- (10, 4, 6): -17,975 (n=2402)
- (11, 3, 6): -18,175 (n=556)
- (11, 4, 6): -19,867 (n=565)
- (17, 3, 6): -20,013 (n=65)
- (8, 4, 6): -21,051 (n=769)
- (14, 3, 6): -21,679 (n=238)
- (13, 3, 6): -21,783 (n=312)
- (13, 4, 6): -21,868 (n=211)
- (8, 3, 4): -22,126 (n=85)

_Generated 2026-09-09 13:34. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 7105 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=7105); harvest_min=1–3 (n=7105); wheat_tiles=0–8 (n=7105); wheat_stock=0–40 (n=7105); min_hands=3–6 (n=7105); load_per_hand=12–26 (n=7105); geese=0–2 (n=7105); open_melons=4–14 (n=7105)
- **Evidence:** 7105 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 83 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=83); harvest_min=1–3 (n=83); wheat_tiles=0–2 (n=83); wheat_stock=0–4 (n=83); min_hands=3–6 (n=83); load_per_hand=15–22 (n=83); geese=0–2 (n=83); open_melons=7–13 (n=83)
- **Evidence:** 83 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 45 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=45); harvest_min=1–3 (n=45); wheat_tiles=0; wheat_stock=0–39 (n=45); min_hands=3–6 (n=45); load_per_hand=12–26 (n=45); geese=0–2 (n=45); open_melons=4–13 (n=45)
- **Evidence:** 45 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 32 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=32); harvest_min=1–3 (n=32); wheat_tiles=0–8 (n=32); wheat_stock=0–39 (n=32); min_hands=3–6 (n=32); load_per_hand=12–23 (n=32); geese=0–2 (n=32); open_melons=8–14 (n=32)
- **Evidence:** 32 candidates, multiple seeds. Confidence: high

### None (observed in 16 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=16); harvest_min=1–3 (n=16); wheat_tiles=0; wheat_stock=0–11 (n=16); min_hands=3–6 (n=16); load_per_hand=12–18 (n=16); geese=0–2 (n=16); open_melons=7–14 (n=16)
- **Evidence:** 16 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 13:34. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._