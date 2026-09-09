# Evolution run 20260909-092928

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1243 · games 23,258 (11,611/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 432 | 864 |
| dead_pattern | 209 | 418 |
| dead_smoke | 173 | 1384 |
| alive | 429 | 20592 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 16132 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2039
- M2: best -16,102 (`8b77b3e994bc`), n=2129
- c1: best -16,310 (`23734cef4da1`), n=2907
- queue: best -15,412 (`fe4745b56024`), n=3848
- v312: best -15,275 (`52b3d5cc236e`), n=2678
- wide: best -16,047 (`512e53fe15bc`), n=2531

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,168 | 120 | 50 | 146 | 16122 | 65.97 | 120: -22,600 (n=9), 118: -25,349 (n=2), 19: -27,891 (n=15), 141: -28,023 (n=6), 5: -28,740 (n=53), 143: -28,964 (n=3), 8: -29,345 (n=5), 112: -29,479 (n=14), 27: -29,531 (n=36), 106: -29,608 (n=28), 89: -30,005 (n=30), 18: -30,042 (n=1023), 92: -30,098 (n=424), 58: -30,201 (n=132), 63: -30,345 (n=267), 80: -30,353 (n=16), 26: -30,432 (n=8), 74: -30,487 (n=308), 49: -30,589 (n=88), 97: -30,621 (n=36), 48: -30,662 (n=544), 71: -30,666 (n=30), 108: -30,721 (n=8), 56: -30,810 (n=16), 35: -30,835 (n=16), 50: -30,844 (n=7939), 65: -30,883 (n=147), 150: -30,955 (n=226), 61: -30,965 (n=110), 70: -31,241 (n=55), 42: -31,360 (n=842), 66: -31,412 (n=303), 60: -31,435 (n=30), 86: -31,454 (n=10), 40: -31,477 (n=102), 94: -31,527 (n=22), 33: -31,535 (n=24), 51: -31,555 (n=21), 14: -31,618 (n=25), 25: -31,648 (n=9), 85: -31,653 (n=12), 30: -31,698 (n=43), 144: -31,709 (n=7), 72: -31,710 (n=11), 9: -31,785 (n=18), 45: -31,801 (n=121), 62: -31,937 (n=20), 57: -31,948 (n=84), 36: -32,050 (n=123), 53: -32,060 (n=60), 113: -32,147 (n=14), 73: -32,194 (n=19), 110: -32,277 (n=4), 39: -32,343 (n=58), 38: -32,416 (n=20), 103: -32,462 (n=9), 84: -32,465 (n=16), 115: -32,512 (n=8), 54: -32,622 (n=26), 96: -32,630 (n=8), 59: -32,632 (n=24), 104: -32,639 (n=5), 44: -32,750 (n=27), 109: -32,844 (n=3), 55: -32,856 (n=645), 41: -32,882 (n=52), 98: -32,926 (n=20), 69: -32,939 (n=26), 4: -33,088 (n=38), 88: -33,112 (n=12), 76: -33,214 (n=16), 68: -33,247 (n=19), 31: -33,271 (n=15), 93: -33,297 (n=10), 0: -33,332 (n=218), 95: -33,449 (n=5), 52: -33,470 (n=21), 13: -33,499 (n=7), 6: -33,522 (n=11), 83: -33,566 (n=111), 43: -33,575 (n=20), 21: -33,604 (n=12), 1: -33,664 (n=8), 119: -33,699 (n=3), 87: -33,711 (n=14), 24: -33,712 (n=23), 28: -33,719 (n=20), 81: -33,724 (n=28), 2: -33,749 (n=3), 90: -33,822 (n=7), 22: -33,894 (n=17), 47: -33,980 (n=26), 32: -33,992 (n=9), 78: -34,032 (n=14), 15: -34,044 (n=11), 20: -34,074 (n=8), 111: -34,111 (n=8), 102: -34,126 (n=5), 17: -34,168 (n=8), 82: -34,211 (n=50), 64: -34,259 (n=22), 11: -34,302 (n=16), 99: -34,384 (n=74), 10: -34,451 (n=15), 140: -34,453 (n=4), 134: -34,464 (n=2), 107: -34,481 (n=6), 37: -34,598 (n=14), 46: -34,598 (n=37), 7: -34,968 (n=8), 101: -34,988 (n=12), 136: -34,994 (n=46), 79: -35,034 (n=16), 77: -35,213 (n=236), 34: -35,314 (n=67), 16: -35,335 (n=18), 100: -35,405 (n=52), 23: -35,508 (n=15), 12: -35,769 (n=12), 91: -35,887 (n=10), 129: -35,956 (n=87), 128: -36,508 (n=3), 3: -36,563 (n=6), 105: -36,563 (n=3), 75: -36,596 (n=11), 117: -36,604 (n=2), 145: -36,990 (n=7), 67: -37,049 (n=18), 114: -37,341 (n=4), 127: -38,268 (n=2), 29: -38,627 (n=44), 131: -38,847 (n=2), 132: -39,931 (n=2), 124: -39,994 (n=3), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,075 | 26 | 30 | 25 | 16131 | 10.69 | 26: -30,678 (n=567), 25: -30,788 (n=7856), 30: -30,997 (n=5241), 31: -31,604 (n=136), 29: -32,181 (n=135), 27: -32,380 (n=243), 28: -33,527 (n=1274), 32: -34,107 (n=150), 41: -34,307 (n=3), 35: -34,811 (n=182), 33: -35,497 (n=134), 37: -35,806 (n=27), 38: -35,963 (n=23), 39: -36,046 (n=13), 34: -36,295 (n=65), 42: -36,946 (n=4), 36: -36,973 (n=40), 46: -38,521 (n=3), 40: -39,180 (n=12), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,371 | 1 | 0 | 34 | 16129 | 24.88 | 1: -30,155 (n=1228), 0: -31,084 (n=13467), 9: -31,118 (n=100), 22: -31,539 (n=2), 2: -32,389 (n=167), 4: -33,007 (n=106), 6: -33,107 (n=114), 8: -33,120 (n=88), 17: -34,084 (n=15), 19: -34,158 (n=6), 3: -34,292 (n=187), 11: -34,812 (n=68), 5: -35,019 (n=173), 16: -35,482 (n=15), 7: -35,563 (n=95), 12: -35,786 (n=35), 13: -35,879 (n=48), 14: -35,925 (n=24), 20: -36,357 (n=6), 28: -36,361 (n=2), 15: -36,538 (n=31), 18: -36,728 (n=20), 23: -36,978 (n=7), 24: -37,048 (n=7), 10: -37,150 (n=51), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,996 (n=10), 26: -40,268 (n=3), 29: -41,186 (n=31), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,830 | 3 | 3 | 4 | 16132 | 2.61 | 3: -30,798 (n=14560), 2: -35,741 (n=1118), 4: -36,456 (n=434), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 16132 | 62.57 | 61: -27,918 (n=2), 138: -27,990 (n=3), 80: -29,618 (n=274), 120: -29,850 (n=16), 130: -29,880 (n=14), 93: -30,056 (n=410), 81: -30,252 (n=85), 85: -30,328 (n=99), 86: -30,484 (n=833), 62: -30,511 (n=7), 92: -30,693 (n=27), 91: -30,710 (n=97), 100: -30,842 (n=10154), 129: -31,008 (n=20), 90: -31,056 (n=122), 123: -31,121 (n=51), 125: -31,171 (n=93), 113: -31,180 (n=20), 111: -31,233 (n=39), 94: -31,336 (n=35), 115: -31,402 (n=35), 55: -31,425 (n=4), 65: -31,427 (n=7), 114: -31,435 (n=29), 141: -31,447 (n=3), 99: -31,456 (n=40), 107: -31,458 (n=26), 78: -31,483 (n=120), 117: -31,542 (n=111), 50: -31,586 (n=98), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,635 (n=116), 67: -31,660 (n=9), 87: -31,702 (n=22), 103: -31,723 (n=31), 133: -31,740 (n=10), 84: -31,781 (n=80), 95: -32,032 (n=40), 105: -32,113 (n=117), 70: -32,127 (n=19), 149: -32,176 (n=3), 109: -32,188 (n=41), 119: -32,280 (n=17), 132: -32,285 (n=12), 53: -32,306 (n=5), 63: -32,321 (n=11), 102: -32,323 (n=44), 66: -32,337 (n=14), 104: -32,499 (n=596), 71: -32,523 (n=21), 57: -32,552 (n=6), 82: -32,585 (n=23), 127: -32,621 (n=35), 110: -32,680 (n=25), 88: -32,823 (n=69), 128: -33,006 (n=29), 76: -33,119 (n=19), 97: -33,119 (n=55), 69: -33,122 (n=10), 112: -33,236 (n=214), 122: -33,237 (n=39), 101: -33,246 (n=41), 98: -33,306 (n=57), 89: -33,446 (n=164), 68: -33,455 (n=11), 134: -33,531 (n=8), 135: -33,745 (n=481), 126: -33,783 (n=27), 96: -33,897 (n=43), 59: -33,898 (n=4), 116: -33,935 (n=74), 124: -34,105 (n=25), 74: -34,107 (n=34), 121: -34,131 (n=14), 136: -34,218 (n=7), 75: -34,489 (n=59), 79: -34,493 (n=49), 108: -34,512 (n=27), 143: -34,578 (n=12), 137: -34,596 (n=5), 144: -34,772 (n=2), 72: -34,832 (n=12), 56: -35,056 (n=5), 106: -35,227 (n=45), 150: -35,802 (n=172), 139: -36,068 (n=8), 131: -36,082 (n=14), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 77: -36,730 (n=25), 118: -36,915 (n=15), 58: -37,611 (n=6), 146: -37,838 (n=2), 73: -38,056 (n=12), 51: -38,207 (n=4), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,391 | 13 | 20 | 11 | 16132 | 4.74 | 13: -30,636 (n=38), 17: -30,909 (n=5373), 16: -30,960 (n=360), 14: -31,107 (n=124), 19: -31,295 (n=847), 18: -31,413 (n=800), 20: -31,545 (n=8423), 15: -32,205 (n=139), 11: -32,310 (n=3), 12: -33,439 (n=17), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,350 | 6 | 6 | 8 | 16132 | 6.14 | 6: -30,717 (n=14390), 5: -34,660 (n=708), 7: -36,441 (n=400), 4: -37,466 (n=409), 3: -37,777 (n=135), 8: -38,147 (n=61), 9: -40,190 (n=22), 10: -41,067 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,336 | 20 | 20 | 15 | 16132 | 7.61 | 20: -30,576 (n=9262), 19: -30,924 (n=4746), 18: -31,513 (n=378), 17: -34,338 (n=711), 16: -36,320 (n=146), 21: -36,632 (n=335), 15: -37,120 (n=70), 23: -37,591 (n=84), 22: -37,915 (n=178), 14: -38,242 (n=36), 26: -38,582 (n=41), 24: -39,219 (n=88), 25: -39,340 (n=21), 13: -39,593 (n=18), 12: -40,913 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +10,220 | 0.0 | 0.0 | 13 | 16132 | 10.29 | 0.0: -30,944 (n=14016), 0.1: -33,107 (n=1027), 0.2: -33,787 (n=618), 0.4: -34,064 (n=95), 0.3: -34,066 (n=197), 0.5: -34,608 (n=57), 1.1: -34,978 (n=7), 0.7: -35,656 (n=18), 0.6: -36,921 (n=50), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -39,081 (n=9), 0.8: -41,164 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,207 | 7 | 7 | 8 | 16132 | 6.12 | 7: -30,657 (n=14365), 5: -36,321 (n=71), 6: -36,412 (n=891), 8: -36,635 (n=522), 10: -36,667 (n=122), 9: -37,157 (n=102), 4: -37,936 (n=50), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,115 | 10 | 8 | 11 | 16132 | 8.34 | 10: -30,693 (n=13693), 7: -32,558 (n=499), 8: -34,689 (n=965), 9: -35,060 (n=558), 6: -35,312 (n=179), 5: -36,429 (n=25), 12: -37,763 (n=53), 4: -38,022 (n=25), 11: -38,382 (n=69), 14: -39,816 (n=30), 13: -40,807 (n=36) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,670 | 0 | 0 | 9 | 16132 | 7.17 | 0: -30,988 (n=14642), 1: -34,054 (n=779), 2: -34,453 (n=322), 3: -34,866 (n=242), 7: -35,103 (n=7), 4: -35,283 (n=90), 5: -35,653 (n=22), 6: -37,663 (n=25), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,589 | 0.55 | 0.5 | 15 | 16132 | 7.41 | 0.55: -30,280 (n=9048), 0.65: -31,772 (n=1234), 0.5: -31,779 (n=3906), 0.75: -32,119 (n=115), 0.7: -32,228 (n=269), 0.6: -33,279 (n=386), 0.8: -34,522 (n=53), 0.45: -34,619 (n=494), 0.9: -35,286 (n=10), 0.4: -36,074 (n=179), 0.35: -36,130 (n=161), 0.85: -36,511 (n=15), 0.95: -37,209 (n=3), 1.0: -38,525 (n=8), 0.3: -39,870 (n=251) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,525 | 14 | 13 | 9 | 16132 | 4.31 | 14: -30,815 (n=2663), 11: -31,239 (n=799), 13: -31,274 (n=9517), 12: -31,392 (n=2168), 15: -31,669 (n=508), 10: -33,163 (n=130), 16: -33,612 (n=278), 9: -36,901 (n=48), 8: -39,340 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,329 | 2 | 2 | 4 | 16132 | 2.84 | 2: -31,058 (n=15496), 1: -37,010 (n=519), 3: -38,375 (n=41), 0: -39,387 (n=76) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,267 | 13 | 12 | 11 | 16132 | 8.27 | 13: -30,753 (n=1288), 14: -31,163 (n=13591), 11: -32,443 (n=222), 12: -32,745 (n=678), 6: -34,388 (n=4), 9: -34,437 (n=29), 10: -35,301 (n=271), 7: -35,686 (n=10), 8: -36,793 (n=34), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,192 | 6 | 18 | 21 | 16132 | 9.44 | 6: -30,437 (n=21), 21: -30,630 (n=2900), 22: -30,799 (n=8017), 14: -30,829 (n=25), 20: -31,330 (n=681), 23: -31,354 (n=725), 16: -31,886 (n=101), 17: -32,468 (n=784), 25: -32,545 (n=1290), 18: -32,937 (n=619), 24: -33,140 (n=433), 12: -33,342 (n=11), 19: -33,491 (n=202), 15: -33,512 (n=53), 13: -33,638 (n=26), 9: -34,033 (n=51), 10: -34,716 (n=67), 11: -36,049 (n=34), 5: -36,499 (n=65), 7: -36,543 (n=22), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,596 | frontier | frontier | 2 | 16132 | 0.92 | frontier: -30,989 (n=15455), v312: -38,584 (n=677) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,530 | 2 | 2 | 3 | 16132 | 1.83 | 2: -30,921 (n=15202), 1: -37,570 (n=877), 3: -38,451 (n=53) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,291 | 34 | 40 | 31 | 16131 | 7.5 | 34: -30,299 (n=299), 38: -30,497 (n=3640), 33: -30,541 (n=62), 49: -30,596 (n=445), 27: -30,617 (n=11), 43: -30,645 (n=4573), 44: -30,783 (n=445), 47: -30,900 (n=292), 30: -31,175 (n=68), 45: -31,238 (n=662), 37: -31,326 (n=603), 39: -31,483 (n=582), 28: -31,950 (n=19), 32: -31,964 (n=62), 26: -32,051 (n=56), 46: -32,557 (n=108), 40: -32,755 (n=2793), 29: -32,779 (n=17), 31: -32,822 (n=44), 50: -32,848 (n=411), 42: -32,977 (n=228), 35: -32,986 (n=232), 41: -33,008 (n=121), 25: -33,175 (n=7), 36: -33,195 (n=195), 48: -34,546 (n=74), 20: -34,865 (n=45), 24: -36,089 (n=25), 23: -36,212 (n=6), 22: -37,589 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3007)
- (9, 3, 6): -16,578 (n=2064)
- (10, 3, 6): -16,840 (n=2657)
- (8, 3, 5): -16,866 (n=280)
- (12, 4, 6): -17,058 (n=498)
- (8, 3, 6): -17,552 (n=795)
- (10, 4, 6): -17,975 (n=2335)
- (11, 3, 6): -18,175 (n=542)
- (11, 4, 6): -19,867 (n=551)
- (17, 3, 6): -20,013 (n=65)
- (8, 4, 6): -21,051 (n=750)
- (13, 3, 6): -21,783 (n=305)
- (13, 4, 6): -21,868 (n=207)
- (14, 3, 6): -21,872 (n=227)
- (8, 3, 4): -22,126 (n=83)

_Generated 2026-09-09 11:29. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 6716 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=6716); harvest_min=1–3 (n=6716); wheat_tiles=0–8 (n=6716); wheat_stock=0–40 (n=6716); min_hands=3–6 (n=6716); load_per_hand=12–26 (n=6716); geese=0–2 (n=6716); open_melons=4–14 (n=6716)
- **Evidence:** 6716 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 81 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=81); harvest_min=1–3 (n=81); wheat_tiles=0–2 (n=81); wheat_stock=0–4 (n=81); min_hands=3–6 (n=81); load_per_hand=15–22 (n=81); geese=0–2 (n=81); open_melons=7–13 (n=81)
- **Evidence:** 81 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 41 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=41); harvest_min=1–3 (n=41); wheat_tiles=0; wheat_stock=0–39 (n=41); min_hands=3–6 (n=41); load_per_hand=12–26 (n=41); geese=0–1 (n=41); open_melons=4–13 (n=41)
- **Evidence:** 41 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 30 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=30); harvest_min=1–3 (n=30); wheat_tiles=0–8 (n=30); wheat_stock=0–39 (n=30); min_hands=3–6 (n=30); load_per_hand=12–23 (n=30); geese=0–2 (n=30); open_melons=8–14 (n=30)
- **Evidence:** 30 candidates, multiple seeds. Confidence: high

### None (observed in 16 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=16); harvest_min=1–3 (n=16); wheat_tiles=0; wheat_stock=0–11 (n=16); min_hands=3–6 (n=16); load_per_hand=12–18 (n=16); geese=0–2 (n=16); open_melons=7–14 (n=16)
- **Evidence:** 16 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 11:29. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._