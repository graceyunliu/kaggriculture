# Evolution run 20260909-052039

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1279 · games 23,288 (11,632/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 452 | 904 |
| dead_pattern | 232 | 464 |
| dead_smoke | 166 | 1328 |
| alive | 429 | 20592 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 15271 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1909
- M2: best -16,461 (`0c25e1226b27`), n=1984
- c1: best -16,310 (`23734cef4da1`), n=2740
- queue: best -15,412 (`fe4745b56024`), n=3687
- v312: best -15,275 (`52b3d5cc236e`), n=2555
- wide: best -16,047 (`512e53fe15bc`), n=2396

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,913 | 120 | 50 | 145 | 15261 | 65.57 | 120: -21,855 (n=7), 118: -25,349 (n=2), 143: -26,636 (n=2), 19: -27,891 (n=15), 141: -28,023 (n=6), 5: -28,817 (n=52), 8: -29,432 (n=4), 112: -29,479 (n=14), 27: -29,531 (n=36), 35: -29,650 (n=12), 108: -29,670 (n=7), 58: -29,961 (n=125), 92: -30,005 (n=393), 89: -30,005 (n=30), 18: -30,072 (n=947), 80: -30,353 (n=16), 63: -30,414 (n=248), 26: -30,432 (n=8), 74: -30,555 (n=276), 49: -30,557 (n=83), 48: -30,644 (n=539), 106: -30,655 (n=20), 71: -30,666 (n=30), 56: -30,810 (n=16), 50: -30,815 (n=7525), 65: -30,829 (n=142), 61: -30,837 (n=107), 150: -30,876 (n=204), 86: -31,018 (n=9), 42: -31,328 (n=817), 66: -31,355 (n=277), 51: -31,357 (n=19), 40: -31,414 (n=101), 60: -31,435 (n=30), 70: -31,444 (n=49), 97: -31,460 (n=31), 85: -31,513 (n=11), 33: -31,521 (n=22), 45: -31,616 (n=116), 25: -31,648 (n=9), 9: -31,659 (n=17), 2: -31,685 (n=2), 72: -31,710 (n=11), 57: -31,948 (n=84), 14: -32,008 (n=24), 113: -32,112 (n=13), 36: -32,124 (n=119), 73: -32,194 (n=19), 110: -32,277 (n=4), 39: -32,284 (n=56), 103: -32,462 (n=9), 115: -32,512 (n=8), 54: -32,587 (n=25), 62: -32,601 (n=18), 84: -32,610 (n=15), 59: -32,612 (n=22), 96: -32,630 (n=8), 104: -32,639 (n=5), 94: -32,712 (n=20), 109: -32,844 (n=3), 41: -32,856 (n=45), 55: -32,879 (n=613), 30: -32,904 (n=35), 98: -32,926 (n=20), 69: -32,939 (n=26), 53: -32,988 (n=49), 93: -32,999 (n=9), 4: -33,088 (n=38), 52: -33,102 (n=19), 38: -33,155 (n=19), 144: -33,156 (n=5), 21: -33,189 (n=10), 31: -33,271 (n=15), 76: -33,355 (n=15), 0: -33,415 (n=211), 95: -33,449 (n=5), 83: -33,468 (n=109), 13: -33,499 (n=7), 6: -33,522 (n=11), 81: -33,568 (n=27), 43: -33,575 (n=20), 1: -33,664 (n=8), 44: -33,686 (n=22), 119: -33,699 (n=3), 28: -33,719 (n=20), 68: -33,803 (n=17), 24: -33,812 (n=21), 90: -33,822 (n=7), 88: -33,874 (n=11), 22: -33,894 (n=17), 32: -33,992 (n=9), 20: -34,103 (n=7), 111: -34,111 (n=8), 102: -34,126 (n=5), 17: -34,168 (n=8), 10: -34,204 (n=14), 82: -34,251 (n=45), 78: -34,276 (n=13), 99: -34,308 (n=73), 140: -34,453 (n=4), 134: -34,464 (n=2), 87: -34,473 (n=13), 15: -34,489 (n=10), 37: -34,598 (n=14), 7: -34,621 (n=7), 16: -34,787 (n=16), 46: -34,818 (n=35), 136: -34,831 (n=44), 64: -34,931 (n=21), 107: -34,965 (n=5), 11: -35,024 (n=15), 79: -35,034 (n=16), 47: -35,037 (n=24), 77: -35,214 (n=233), 101: -35,278 (n=11), 34: -35,348 (n=64), 23: -35,508 (n=15), 100: -35,517 (n=50), 129: -35,705 (n=83), 91: -35,887 (n=10), 128: -36,508 (n=3), 3: -36,531 (n=5), 105: -36,563 (n=3), 75: -36,596 (n=11), 117: -36,604 (n=2), 12: -36,634 (n=11), 145: -36,990 (n=7), 67: -37,049 (n=18), 114: -37,341 (n=4), 127: -38,268 (n=2), 29: -38,500 (n=39), 131: -38,847 (n=2), 132: -39,931 (n=2), 124: -39,994 (n=3), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,104 | 26 | 30 | 25 | 15270 | 10.66 | 26: -30,649 (n=521), 25: -30,793 (n=7420), 30: -30,986 (n=4960), 31: -31,431 (n=130), 29: -32,238 (n=125), 27: -32,415 (n=237), 28: -33,519 (n=1224), 32: -34,010 (n=146), 41: -34,307 (n=3), 35: -34,788 (n=178), 33: -35,504 (n=125), 39: -35,574 (n=12), 37: -35,771 (n=26), 38: -35,924 (n=22), 34: -36,081 (n=62), 42: -36,946 (n=4), 36: -37,171 (n=37), 46: -38,521 (n=3), 40: -39,180 (n=12), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,226 | 1 | 0 | 34 | 15268 | 25.04 | 1: -30,300 (n=1085), 0: -31,069 (n=12823), 9: -31,162 (n=99), 22: -31,539 (n=2), 2: -32,290 (n=155), 4: -33,055 (n=99), 6: -33,107 (n=104), 8: -33,195 (n=85), 17: -34,084 (n=15), 19: -34,158 (n=6), 3: -34,273 (n=178), 11: -34,807 (n=67), 5: -34,864 (n=161), 7: -35,474 (n=91), 16: -35,592 (n=13), 12: -35,849 (n=34), 13: -35,879 (n=48), 14: -36,218 (n=23), 20: -36,357 (n=6), 28: -36,361 (n=2), 15: -36,536 (n=28), 18: -36,728 (n=20), 23: -36,978 (n=7), 24: -37,048 (n=7), 10: -37,326 (n=48), 39: -37,445 (n=11), 21: -37,766 (n=7), 40: -39,508 (n=8), 26: -40,268 (n=3), 29: -41,366 (n=29), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,834 | 3 | 3 | 4 | 15271 | 2.61 | 3: -30,794 (n=13780), 2: -35,799 (n=1063), 4: -36,461 (n=408), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 15271 | 62.78 | 61: -27,918 (n=2), 138: -27,990 (n=3), 130: -29,311 (n=13), 120: -29,850 (n=16), 80: -29,890 (n=238), 93: -30,050 (n=388), 65: -30,157 (n=6), 85: -30,207 (n=96), 81: -30,227 (n=83), 91: -30,466 (n=91), 62: -30,511 (n=7), 86: -30,585 (n=759), 113: -30,716 (n=19), 114: -30,785 (n=25), 100: -30,801 (n=9643), 123: -30,951 (n=48), 64: -30,996 (n=12), 129: -31,008 (n=20), 125: -31,090 (n=92), 115: -31,141 (n=34), 111: -31,233 (n=39), 94: -31,268 (n=34), 78: -31,269 (n=108), 63: -31,414 (n=10), 55: -31,425 (n=4), 141: -31,447 (n=3), 107: -31,458 (n=26), 90: -31,467 (n=104), 92: -31,528 (n=25), 117: -31,534 (n=104), 147: -31,607 (n=7), 67: -31,660 (n=9), 83: -31,680 (n=113), 99: -31,706 (n=37), 133: -31,740 (n=10), 103: -31,858 (n=29), 84: -31,923 (n=75), 57: -31,969 (n=5), 87: -31,970 (n=20), 132: -31,971 (n=11), 95: -32,077 (n=39), 109: -32,090 (n=37), 70: -32,127 (n=19), 102: -32,153 (n=43), 149: -32,176 (n=3), 105: -32,254 (n=112), 53: -32,306 (n=5), 66: -32,339 (n=13), 71: -32,523 (n=21), 82: -32,550 (n=22), 119: -32,612 (n=15), 104: -32,627 (n=573), 110: -32,680 (n=25), 128: -32,857 (n=28), 50: -32,957 (n=71), 127: -32,982 (n=33), 88: -33,015 (n=66), 98: -33,106 (n=47), 122: -33,107 (n=37), 76: -33,119 (n=19), 97: -33,119 (n=55), 69: -33,122 (n=10), 112: -33,200 (n=208), 68: -33,455 (n=11), 101: -33,488 (n=39), 134: -33,531 (n=8), 89: -33,601 (n=161), 135: -33,740 (n=461), 116: -33,888 (n=67), 96: -33,890 (n=42), 59: -33,898 (n=4), 126: -33,966 (n=25), 124: -34,105 (n=25), 74: -34,126 (n=33), 121: -34,194 (n=13), 136: -34,218 (n=7), 79: -34,475 (n=47), 75: -34,489 (n=59), 108: -34,512 (n=27), 143: -34,578 (n=12), 137: -34,596 (n=5), 144: -34,772 (n=2), 72: -34,832 (n=12), 106: -34,924 (n=43), 56: -35,056 (n=5), 150: -35,756 (n=171), 139: -36,068 (n=8), 131: -36,082 (n=14), 52: -36,201 (n=4), 142: -36,242 (n=8), 77: -36,388 (n=23), 148: -36,528 (n=3), 118: -36,824 (n=14), 51: -37,500 (n=2), 58: -37,611 (n=6), 146: -37,838 (n=2), 73: -38,056 (n=12), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,501 | 0.0 | 0.0 | 13 | 15271 | 10.28 | 0.0: -30,943 (n=13256), 0.1: -33,057 (n=987), 0.2: -33,787 (n=594), 0.4: -34,115 (n=91), 0.3: -34,249 (n=177), 1.1: -34,978 (n=7), 0.5: -34,993 (n=53), 0.7: -36,163 (n=16), 0.6: -37,000 (n=46), 0.9: -37,347 (n=5), 1.0: -37,756 (n=24), 1.2: -39,081 (n=9), 0.8: -42,444 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,535 | 13 | 20 | 11 | 15271 | 4.82 | 13: -30,492 (n=37), 17: -30,912 (n=5016), 16: -30,946 (n=342), 14: -31,251 (n=121), 19: -31,296 (n=780), 18: -31,443 (n=744), 20: -31,536 (n=8077), 15: -32,202 (n=128), 11: -32,310 (n=3), 12: -34,282 (n=15), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,352 | 20 | 20 | 15 | 15271 | 7.52 | 20: -30,561 (n=8678), 19: -30,936 (n=4559), 18: -31,528 (n=354), 17: -34,322 (n=698), 16: -36,447 (n=141), 21: -36,602 (n=318), 15: -37,330 (n=68), 23: -37,439 (n=78), 22: -37,900 (n=166), 14: -38,304 (n=35), 26: -38,538 (n=39), 24: -38,928 (n=80), 25: -39,340 (n=21), 13: -39,593 (n=18), 12: -40,913 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,348 | 6 | 6 | 8 | 15271 | 6.14 | 6: -30,719 (n=13622), 5: -34,649 (n=665), 7: -36,476 (n=387), 4: -37,419 (n=382), 3: -37,749 (n=129), 8: -38,213 (n=59), 9: -40,522 (n=20), 10: -41,067 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,161 | 10 | 8 | 11 | 15271 | 8.31 | 10: -30,683 (n=12918), 7: -32,473 (n=469), 8: -34,689 (n=940), 9: -35,020 (n=542), 6: -35,414 (n=175), 5: -36,429 (n=25), 12: -37,559 (n=49), 4: -38,039 (n=24), 11: -38,404 (n=66), 14: -39,816 (n=30), 13: -40,844 (n=33) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,096 | 7 | 7 | 8 | 15271 | 6.11 | 7: -30,654 (n=13580), 6: -36,397 (n=852), 5: -36,419 (n=70), 8: -36,560 (n=495), 10: -36,685 (n=120), 9: -37,198 (n=99), 4: -37,830 (n=47), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,674 | 0 | 0 | 9 | 15271 | 7.16 | 0: -30,984 (n=13843), 1: -34,060 (n=746), 2: -34,416 (n=309), 3: -34,888 (n=233), 7: -35,103 (n=7), 4: -35,469 (n=83), 5: -35,653 (n=22), 6: -37,663 (n=25), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,627 | 0.55 | 0.5 | 15 | 15271 | 7.29 | 0.55: -30,254 (n=8437), 0.65: -31,738 (n=1207), 0.5: -31,803 (n=3775), 0.75: -31,887 (n=108), 0.7: -32,278 (n=259), 0.6: -33,227 (n=367), 0.8: -34,400 (n=52), 0.45: -34,603 (n=468), 0.9: -35,286 (n=10), 0.35: -35,993 (n=152), 0.4: -36,205 (n=172), 0.85: -37,161 (n=14), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,881 (n=240) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,924 | 14 | 13 | 9 | 15271 | 4.33 | 14: -30,780 (n=2445), 11: -31,226 (n=781), 13: -31,285 (n=9050), 12: -31,395 (n=2078), 15: -31,659 (n=472), 10: -33,311 (n=122), 16: -33,534 (n=257), 9: -36,852 (n=46), 8: -39,704 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,647 | 6 | 18 | 21 | 15271 | 9.36 | 6: -29,983 (n=18), 21: -30,599 (n=2714), 14: -30,652 (n=24), 22: -30,816 (n=7535), 20: -31,292 (n=664), 23: -31,349 (n=690), 16: -32,164 (n=94), 17: -32,440 (n=753), 25: -32,505 (n=1237), 18: -32,862 (n=602), 24: -33,105 (n=421), 15: -33,259 (n=51), 12: -33,342 (n=11), 19: -33,466 (n=196), 13: -33,925 (n=25), 9: -33,993 (n=50), 10: -34,716 (n=67), 11: -36,049 (n=34), 5: -36,170 (n=58), 7: -36,543 (n=22), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,354 | 2 | 2 | 4 | 15271 | 2.84 | 2: -31,059 (n=14662), 1: -36,957 (n=495), 3: -38,375 (n=41), 0: -39,413 (n=73) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,235 | 13 | 12 | 11 | 15270 | 7.44 | 13: -30,785 (n=1185), 14: -31,154 (n=12884), 11: -32,549 (n=213), 12: -32,780 (n=651), 6: -34,388 (n=4), 9: -34,839 (n=28), 10: -35,279 (n=258), 7: -35,686 (n=10), 8: -36,793 (n=34), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,611 | frontier | frontier | 2 | 15271 | 0.92 | frontier: -30,991 (n=14633), v312: -38,603 (n=638) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,532 | 2 | 2 | 3 | 15271 | 1.83 | 2: -30,920 (n=14381), 1: -37,554 (n=837), 3: -38,451 (n=53) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,378 | 34 | 40 | 30 | 15271 | 7.51 | 34: -30,209 (n=274), 38: -30,408 (n=3379), 27: -30,617 (n=11), 49: -30,635 (n=435), 43: -30,649 (n=4330), 33: -30,707 (n=57), 44: -30,946 (n=411), 47: -30,993 (n=269), 30: -31,212 (n=67), 37: -31,224 (n=561), 45: -31,285 (n=617), 39: -31,464 (n=541), 32: -31,859 (n=60), 26: -32,047 (n=52), 28: -32,341 (n=16), 46: -32,613 (n=102), 40: -32,758 (n=2736), 29: -32,779 (n=17), 35: -32,813 (n=226), 31: -32,839 (n=42), 41: -33,003 (n=111), 42: -33,023 (n=220), 50: -33,031 (n=392), 36: -33,129 (n=189), 25: -33,175 (n=7), 48: -34,674 (n=71), 20: -34,713 (n=43), 24: -35,776 (n=24), 23: -36,212 (n=6), 22: -37,587 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2849)
- (9, 3, 6): -16,578 (n=1931)
- (10, 3, 6): -16,840 (n=2492)
- (8, 3, 5): -16,866 (n=267)
- (12, 4, 6): -17,058 (n=486)
- (8, 3, 6): -17,552 (n=767)
- (10, 4, 6): -17,975 (n=2197)
- (11, 3, 6): -18,175 (n=516)
- (11, 4, 6): -19,867 (n=529)
- (17, 3, 6): -20,013 (n=64)
- (8, 4, 6): -21,051 (n=713)
- (13, 3, 6): -21,783 (n=291)
- (13, 4, 6): -21,868 (n=203)
- (8, 3, 4): -22,126 (n=80)
- (10, 3, 5): -22,188 (n=63)

_Generated 2026-09-09 07:20. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 5988 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=5988); harvest_min=1–3 (n=5988); wheat_tiles=0–8 (n=5988); wheat_stock=0–40 (n=5988); min_hands=3–6 (n=5988); load_per_hand=12–26 (n=5988); geese=0–2 (n=5988); open_melons=4–14 (n=5988)
- **Evidence:** 5988 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 73 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=73); harvest_min=1–3 (n=73); wheat_tiles=0–2 (n=73); wheat_stock=0–4 (n=73); min_hands=3–6 (n=73); load_per_hand=15–22 (n=73); geese=0–2 (n=73); open_melons=7–13 (n=73)
- **Evidence:** 73 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 39 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=39); harvest_min=1–3 (n=39); wheat_tiles=0; wheat_stock=0–39 (n=39); min_hands=3–6 (n=39); load_per_hand=12–26 (n=39); geese=0–1 (n=39); open_melons=4–13 (n=39)
- **Evidence:** 39 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 26 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=26); harvest_min=1–3 (n=26); wheat_tiles=0–8 (n=26); wheat_stock=0–39 (n=26); min_hands=3–6 (n=26); load_per_hand=12–23 (n=26); geese=0–2 (n=26); open_melons=8–14 (n=26)
- **Evidence:** 26 candidates, multiple seeds. Confidence: high

### None (observed in 12 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=12); harvest_min=1–3 (n=12); wheat_tiles=0; wheat_stock=0–11 (n=12); min_hands=3–6 (n=12); load_per_hand=12–18 (n=12); geese=0–2 (n=12); open_melons=7–14 (n=12)
- **Evidence:** 12 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-09 07:20. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._