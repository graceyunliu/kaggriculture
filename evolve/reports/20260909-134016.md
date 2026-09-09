# Evolution run 20260909-134016

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1230 · games 22,732 (11,363/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 453 | 906 |
| dead_pattern | 185 | 370 |
| dead_smoke | 174 | 1392 |
| alive | 418 | 20064 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 16967 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2174
- M2: best -16,102 (`8b77b3e994bc`), n=2258
- c1: best -16,310 (`23734cef4da1`), n=3037
- queue: best -15,412 (`fe4745b56024`), n=4023
- v312: best -15,275 (`52b3d5cc236e`), n=2802
- wide: best -16,047 (`512e53fe15bc`), n=2673

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 146 | 16957 | 65.59 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 8: -28,491 (n=6), 5: -28,740 (n=53), 143: -28,964 (n=3), 19: -29,285 (n=17), 27: -29,422 (n=38), 112: -29,479 (n=14), 106: -29,901 (n=32), 18: -30,123 (n=1108), 89: -30,144 (n=31), 92: -30,312 (n=459), 80: -30,353 (n=16), 63: -30,362 (n=286), 74: -30,390 (n=346), 26: -30,432 (n=8), 58: -30,456 (n=137), 97: -30,508 (n=38), 49: -30,577 (n=89), 48: -30,642 (n=555), 71: -30,666 (n=30), 108: -30,721 (n=8), 35: -30,835 (n=16), 56: -30,835 (n=17), 72: -30,839 (n=13), 150: -30,870 (n=248), 50: -30,888 (n=8303), 65: -30,951 (n=157), 30: -31,168 (n=51), 61: -31,190 (n=115), 70: -31,271 (n=56), 14: -31,314 (n=28), 40: -31,329 (n=108), 60: -31,365 (n=31), 42: -31,392 (n=879), 86: -31,454 (n=10), 44: -31,454 (n=37), 94: -31,527 (n=22), 85: -31,546 (n=13), 51: -31,555 (n=21), 66: -31,560 (n=324), 25: -31,648 (n=9), 45: -31,770 (n=122), 53: -31,788 (n=68), 33: -31,832 (n=25), 57: -31,917 (n=85), 36: -31,931 (n=132), 62: -31,979 (n=21), 144: -32,007 (n=8), 113: -32,147 (n=14), 73: -32,194 (n=19), 59: -32,226 (n=25), 9: -32,230 (n=19), 110: -32,277 (n=4), 54: -32,394 (n=27), 38: -32,416 (n=20), 103: -32,462 (n=9), 84: -32,465 (n=16), 39: -32,493 (n=60), 115: -32,512 (n=8), 96: -32,630 (n=8), 104: -32,639 (n=5), 55: -32,754 (n=679), 41: -32,836 (n=55), 87: -32,906 (n=18), 109: -32,944 (n=4), 52: -32,951 (n=23), 4: -33,017 (n=39), 69: -33,033 (n=28), 88: -33,112 (n=12), 98: -33,151 (n=21), 68: -33,247 (n=19), 76: -33,276 (n=18), 78: -33,288 (n=16), 93: -33,297 (n=10), 0: -33,320 (n=222), 21: -33,400 (n=13), 95: -33,449 (n=5), 31: -33,468 (n=16), 13: -33,499 (n=7), 28: -33,526 (n=21), 83: -33,599 (n=114), 22: -33,631 (n=18), 43: -33,659 (n=21), 1: -33,664 (n=8), 119: -33,699 (n=3), 6: -33,709 (n=13), 24: -33,712 (n=23), 81: -33,724 (n=28), 2: -33,749 (n=3), 90: -33,822 (n=7), 20: -34,074 (n=8), 111: -34,111 (n=8), 102: -34,126 (n=5), 11: -34,164 (n=17), 17: -34,168 (n=8), 47: -34,169 (n=29), 82: -34,211 (n=50), 99: -34,286 (n=75), 15: -34,394 (n=12), 10: -34,451 (n=15), 140: -34,453 (n=4), 64: -34,455 (n=23), 134: -34,464 (n=2), 107: -34,481 (n=6), 32: -34,544 (n=11), 46: -34,592 (n=40), 37: -34,598 (n=14), 7: -34,904 (n=9), 79: -34,932 (n=19), 101: -34,988 (n=12), 3: -35,105 (n=7), 77: -35,188 (n=238), 12: -35,211 (n=14), 136: -35,212 (n=48), 34: -35,279 (n=70), 16: -35,335 (n=18), 100: -35,539 (n=54), 23: -35,646 (n=16), 91: -35,887 (n=10), 129: -35,962 (n=88), 75: -36,248 (n=13), 67: -36,486 (n=20), 128: -36,508 (n=3), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,612 (n=51), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,005 | 26 | 30 | 25 | 16967 | 11.2 | 26: -30,748 (n=598), 25: -30,799 (n=8279), 30: -31,055 (n=5512), 31: -31,712 (n=141), 29: -32,148 (n=141), 27: -32,498 (n=256), 28: -33,484 (n=1329), 32: -34,053 (n=160), 41: -34,307 (n=3), 35: -34,878 (n=186), 45: -35,319 (n=2), 33: -35,462 (n=140), 37: -35,762 (n=28), 34: -35,916 (n=70), 38: -35,984 (n=24), 39: -36,046 (n=13), 36: -36,822 (n=41), 42: -36,946 (n=4), 46: -38,521 (n=3), 40: -38,691 (n=13), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -40,312 (n=6), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,391 | 1 | 0 | 34 | 16964 | 24.74 | 1: -30,135 (n=1370), 9: -31,074 (n=102), 0: -31,114 (n=14084), 22: -31,572 (n=3), 2: -32,580 (n=180), 6: -33,043 (n=120), 4: -33,065 (n=112), 8: -33,119 (n=89), 3: -34,231 (n=197), 17: -34,501 (n=16), 19: -34,641 (n=8), 11: -34,935 (n=71), 5: -35,045 (n=182), 16: -35,178 (n=16), 7: -35,562 (n=102), 13: -35,639 (n=52), 28: -35,676 (n=3), 12: -35,786 (n=35), 14: -36,097 (n=26), 20: -36,357 (n=6), 15: -36,474 (n=33), 18: -36,728 (n=20), 10: -36,945 (n=53), 23: -36,978 (n=7), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,716 (n=11), 26: -40,268 (n=3), 29: -41,129 (n=33), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,805 | 3 | 3 | 4 | 16967 | 2.61 | 3: -30,823 (n=15307), 2: -35,709 (n=1177), 4: -36,366 (n=463), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 16967 | 62.35 | 61: -27,918 (n=2), 80: -29,579 (n=313), 130: -29,880 (n=14), 93: -30,076 (n=429), 138: -30,186 (n=4), 81: -30,256 (n=87), 120: -30,270 (n=18), 85: -30,517 (n=101), 86: -30,560 (n=902), 62: -30,676 (n=9), 91: -30,758 (n=100), 100: -30,883 (n=10643), 90: -31,000 (n=136), 129: -31,008 (n=20), 123: -31,037 (n=53), 50: -31,056 (n=133), 78: -31,089 (n=141), 92: -31,150 (n=29), 111: -31,163 (n=42), 125: -31,236 (n=94), 94: -31,336 (n=35), 55: -31,425 (n=4), 65: -31,427 (n=7), 141: -31,447 (n=3), 115: -31,483 (n=36), 119: -31,499 (n=18), 107: -31,506 (n=28), 99: -31,517 (n=43), 117: -31,523 (n=116), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,654 (n=121), 87: -31,688 (n=23), 103: -31,723 (n=31), 133: -31,740 (n=10), 67: -31,763 (n=10), 113: -31,890 (n=22), 84: -31,939 (n=85), 95: -32,102 (n=43), 70: -32,127 (n=19), 105: -32,274 (n=121), 132: -32,285 (n=12), 53: -32,306 (n=5), 102: -32,311 (n=45), 63: -32,321 (n=11), 114: -32,336 (n=31), 66: -32,337 (n=14), 109: -32,412 (n=44), 149: -32,426 (n=4), 104: -32,506 (n=617), 71: -32,523 (n=21), 57: -32,552 (n=6), 82: -32,585 (n=23), 127: -32,621 (n=35), 128: -32,676 (n=32), 110: -32,680 (n=25), 59: -32,721 (n=5), 88: -32,804 (n=73), 76: -33,081 (n=20), 69: -33,122 (n=10), 97: -33,186 (n=57), 112: -33,208 (n=217), 122: -33,237 (n=39), 98: -33,297 (n=61), 68: -33,455 (n=11), 89: -33,485 (n=172), 134: -33,531 (n=8), 101: -33,584 (n=45), 116: -33,623 (n=76), 126: -33,677 (n=28), 135: -33,813 (n=492), 108: -33,936 (n=29), 96: -34,037 (n=47), 74: -34,107 (n=34), 136: -34,218 (n=7), 124: -34,315 (n=26), 79: -34,469 (n=51), 75: -34,489 (n=59), 143: -34,578 (n=12), 137: -34,596 (n=5), 144: -34,772 (n=2), 106: -34,783 (n=48), 72: -34,820 (n=13), 121: -34,856 (n=17), 150: -35,786 (n=175), 131: -35,807 (n=15), 56: -35,940 (n=6), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 77: -36,825 (n=27), 118: -36,915 (n=15), 58: -37,611 (n=6), 73: -37,775 (n=13), 146: -37,838 (n=2), 51: -38,207 (n=4), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,331 | 6 | 6 | 8 | 16967 | 6.13 | 6: -30,736 (n=15128), 5: -34,693 (n=754), 7: -36,413 (n=416), 4: -37,488 (n=435), 3: -37,728 (n=139), 8: -37,984 (n=63), 9: -40,202 (n=24), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,590 | 13 | 20 | 11 | 16967 | 4.7 | 13: -30,437 (n=39), 16: -30,945 (n=371), 17: -30,952 (n=5688), 18: -31,344 (n=859), 19: -31,351 (n=903), 14: -31,360 (n=135), 20: -31,556 (n=8792), 15: -32,248 (n=151), 11: -32,310 (n=3), 12: -33,410 (n=18), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +10,189 | 0.0 | 0.0 | 13 | 16967 | 10.33 | 0.0: -30,975 (n=14785), 0.1: -33,107 (n=1053), 0.2: -33,801 (n=638), 0.4: -34,019 (n=98), 0.3: -34,067 (n=207), 0.5: -34,511 (n=59), 1.1: -34,978 (n=7), 0.7: -35,656 (n=18), 0.6: -36,718 (n=55), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -39,081 (n=9), 0.8: -41,164 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,180 | 7 | 7 | 8 | 16967 | 6.13 | 7: -30,684 (n=15116), 5: -36,237 (n=73), 6: -36,382 (n=922), 8: -36,589 (n=556), 10: -36,729 (n=124), 9: -37,277 (n=108), 4: -37,770 (n=59), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,059 | 10 | 8 | 11 | 16967 | 8.34 | 10: -30,726 (n=14402), 7: -32,447 (n=543), 8: -34,686 (n=1003), 9: -35,032 (n=586), 6: -35,308 (n=184), 5: -36,286 (n=27), 12: -37,855 (n=54), 4: -38,022 (n=25), 11: -38,139 (n=73), 14: -39,848 (n=32), 13: -40,785 (n=38) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,053 | 20 | 20 | 15 | 16967 | 7.69 | 20: -30,613 (n=9827), 19: -30,927 (n=4919), 18: -31,481 (n=395), 17: -34,362 (n=729), 16: -36,409 (n=157), 21: -36,554 (n=352), 15: -37,281 (n=77), 23: -37,623 (n=93), 22: -37,919 (n=188), 14: -38,352 (n=38), 26: -38,568 (n=42), 24: -39,225 (n=90), 25: -39,407 (n=22), 13: -39,593 (n=18), 12: -40,665 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,643 | 0 | 0 | 9 | 16967 | 7.17 | 0: -31,016 (n=15401), 1: -34,020 (n=815), 2: -34,339 (n=341), 3: -34,792 (n=258), 7: -35,103 (n=7), 4: -35,266 (n=94), 5: -35,653 (n=22), 6: -37,760 (n=26), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,518 | 0.55 | 0.5 | 15 | 16967 | 7.48 | 0.55: -30,327 (n=9591), 0.65: -31,773 (n=1265), 0.5: -31,774 (n=4057), 0.75: -32,222 (n=124), 0.7: -32,345 (n=286), 0.6: -33,243 (n=412), 0.8: -34,384 (n=57), 0.45: -34,649 (n=511), 0.9: -35,465 (n=11), 0.35: -36,035 (n=168), 0.4: -36,067 (n=196), 0.85: -36,511 (n=15), 0.95: -37,209 (n=3), 1.0: -38,525 (n=8), 0.3: -39,845 (n=263) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,637 | 14 | 13 | 9 | 16967 | 4.28 | 14: -30,906 (n=2876), 11: -31,218 (n=828), 13: -31,291 (n=9956), 12: -31,380 (n=2267), 15: -31,679 (n=531), 10: -33,047 (n=137), 16: -33,521 (n=297), 9: -36,733 (n=53), 8: -39,543 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,467 | 6 | 18 | 21 | 16967 | 9.47 | 6: -30,162 (n=22), 21: -30,671 (n=3075), 14: -30,829 (n=25), 22: -30,834 (n=8460), 23: -31,313 (n=754), 20: -31,347 (n=698), 16: -31,967 (n=109), 17: -32,389 (n=814), 25: -32,571 (n=1344), 18: -32,946 (n=648), 13: -33,057 (n=27), 24: -33,137 (n=449), 15: -33,429 (n=56), 19: -33,429 (n=218), 9: -34,073 (n=53), 12: -34,505 (n=12), 10: -34,879 (n=69), 11: -36,391 (n=38), 7: -36,543 (n=22), 5: -36,607 (n=69), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,417 | 2 | 2 | 4 | 16967 | 2.84 | 2: -31,073 (n=16283), 1: -36,987 (n=562), 3: -38,623 (n=44), 0: -39,490 (n=78) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,279 | 13 | 12 | 11 | 16967 | 8.26 | 13: -30,742 (n=1377), 14: -31,197 (n=14279), 11: -32,453 (n=230), 12: -32,607 (n=715), 9: -34,276 (n=30), 6: -34,388 (n=4), 10: -35,323 (n=281), 7: -35,686 (n=10), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,536 | frontier | frontier | 2 | 16967 | 0.92 | frontier: -31,009 (n=16251), v312: -38,545 (n=716) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,404 | 2 | 2 | 3 | 16967 | 1.83 | 2: -30,943 (n=15992), 1: -37,593 (n=918), 3: -38,347 (n=57) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +6,692 | 0.05 | 0.25 | 11 | 16967 | 4.91 | 0.05: -30,387 (n=2423), 0.2: -30,827 (n=2055), 0.4: -30,887 (n=378), 0.15: -30,965 (n=978), 0.0: -31,121 (n=601), 0.25: -31,534 (n=9114), 0.1: -31,800 (n=607), 0.3: -32,740 (n=306), 0.35: -33,443 (n=376), 0.45: -34,344 (n=68), 0.5: -37,079 (n=61) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3162)
- (12, 4, 6): -16,525 (n=525)
- (9, 3, 6): -16,578 (n=2174)
- (10, 3, 6): -16,840 (n=2791)
- (8, 3, 5): -16,866 (n=295)
- (8, 3, 6): -17,552 (n=828)
- (10, 4, 6): -17,975 (n=2461)
- (11, 3, 6): -18,175 (n=575)
- (11, 4, 6): -19,867 (n=578)
- (17, 3, 6): -20,013 (n=66)
- (8, 4, 6): -21,051 (n=787)
- (14, 3, 6): -21,679 (n=242)
- (13, 3, 6): -21,783 (n=324)
- (13, 4, 6): -21,868 (n=216)
- (8, 3, 4): -22,126 (n=87)

_Generated 2026-09-09 15:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 7449 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=7449); harvest_min=1–3 (n=7449); wheat_tiles=0–8 (n=7449); wheat_stock=0–40 (n=7449); min_hands=3–6 (n=7449); load_per_hand=12–26 (n=7449); geese=0–2 (n=7449); open_melons=4–14 (n=7449)
- **Evidence:** 7449 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 90 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=90); harvest_min=1–3 (n=90); wheat_tiles=0–2 (n=90); wheat_stock=0–6 (n=90); min_hands=3–6 (n=90); load_per_hand=15–23 (n=90); geese=0–2 (n=90); open_melons=7–13 (n=90)
- **Evidence:** 90 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 49 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=49); harvest_min=1–3 (n=49); wheat_tiles=0; wheat_stock=0–39 (n=49); min_hands=3–6 (n=49); load_per_hand=12–26 (n=49); geese=0–2 (n=49); open_melons=4–13 (n=49)
- **Evidence:** 49 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 35 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=35); harvest_min=1–3 (n=35); wheat_tiles=0–8 (n=35); wheat_stock=0–39 (n=35); min_hands=3–6 (n=35); load_per_hand=12–23 (n=35); geese=0–2 (n=35); open_melons=6–14 (n=35)
- **Evidence:** 35 candidates, multiple seeds. Confidence: high

### None (observed in 17 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=17); harvest_min=1–3 (n=17); wheat_tiles=0; wheat_stock=0–11 (n=17); min_hands=3–6 (n=17); load_per_hand=12–18 (n=17); geese=0–2 (n=17); open_melons=7–14 (n=17)
- **Evidence:** 17 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 15:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._