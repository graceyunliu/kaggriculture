# Evolution run 20260908-124426

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1197 · games 24,636 (12,314/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 379 | 758 |
| dead_pattern | 211 | 422 |
| dead_smoke | 142 | 1136 |
| alive | 465 | 22320 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 11773 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1366
- M2: best -16,461 (`0c25e1226b27`), n=1423
- c1: best -16,310 (`23734cef4da1`), n=2151
- queue: best -15,412 (`fe4745b56024`), n=2942
- v312: best -15,275 (`52b3d5cc236e`), n=2041
- wide: best -16,047 (`512e53fe15bc`), n=1850

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +21,602 | 120 | 50 | 143 | 11762 | 64.14 | 120: -18,328 (n=3), 141: -24,735 (n=4), 118: -25,349 (n=2), 143: -26,636 (n=2), 19: -27,075 (n=13), 8: -27,428 (n=2), 35: -27,894 (n=8), 112: -28,098 (n=12), 72: -28,170 (n=6), 5: -28,572 (n=45), 71: -28,690 (n=23), 56: -29,061 (n=12), 27: -29,195 (n=34), 26: -29,341 (n=6), 89: -29,503 (n=27), 92: -29,507 (n=285), 58: -29,584 (n=81), 49: -29,873 (n=64), 18: -29,955 (n=659), 63: -30,158 (n=175), 74: -30,377 (n=145), 61: -30,467 (n=91), 51: -30,565 (n=12), 50: -30,714 (n=5804), 48: -30,741 (n=487), 65: -30,742 (n=116), 80: -30,851 (n=12), 150: -31,076 (n=124), 42: -31,172 (n=677), 60: -31,180 (n=28), 144: -31,182 (n=2), 40: -31,192 (n=87), 66: -31,218 (n=180), 85: -31,279 (n=9), 33: -31,322 (n=21), 45: -31,322 (n=107), 9: -31,680 (n=12), 2: -31,685 (n=2), 14: -31,695 (n=15), 86: -31,717 (n=8), 57: -31,735 (n=82), 93: -31,753 (n=7), 96: -31,788 (n=6), 36: -31,790 (n=97), 73: -31,853 (n=15), 84: -32,162 (n=12), 39: -32,172 (n=50), 70: -32,183 (n=28), 62: -32,220 (n=17), 59: -32,251 (n=15), 110: -32,277 (n=4), 95: -32,333 (n=4), 25: -32,369 (n=7), 69: -32,403 (n=22), 97: -32,526 (n=22), 94: -32,527 (n=15), 103: -32,559 (n=8), 76: -32,628 (n=10), 38: -32,804 (n=17), 24: -32,807 (n=16), 88: -32,815 (n=9), 52: -32,819 (n=11), 109: -32,844 (n=3), 115: -32,856 (n=7), 21: -32,959 (n=7), 31: -33,145 (n=12), 113: -33,163 (n=8), 55: -33,239 (n=484), 41: -33,248 (n=31), 98: -33,249 (n=13), 83: -33,258 (n=91), 108: -33,264 (n=5), 104: -33,266 (n=4), 0: -33,328 (n=174), 6: -33,331 (n=10), 119: -33,340 (n=2), 4: -33,399 (n=36), 78: -33,423 (n=9), 111: -33,451 (n=7), 13: -33,499 (n=7), 23: -33,511 (n=11), 43: -33,691 (n=18), 30: -33,744 (n=14), 90: -33,822 (n=7), 22: -33,829 (n=14), 28: -33,832 (n=18), 81: -33,835 (n=24), 136: -33,990 (n=33), 68: -33,999 (n=11), 82: -34,131 (n=40), 54: -34,180 (n=17), 44: -34,233 (n=20), 10: -34,299 (n=13), 102: -34,320 (n=4), 99: -34,411 (n=68), 1: -34,413 (n=5), 134: -34,464 (n=2), 46: -34,493 (n=28), 15: -34,699 (n=8), 7: -34,718 (n=6), 79: -34,751 (n=12), 107: -34,996 (n=4), 34: -34,996 (n=54), 77: -35,139 (n=213), 91: -35,168 (n=8), 32: -35,252 (n=7), 101: -35,278 (n=11), 100: -35,306 (n=39), 20: -35,382 (n=5), 16: -35,406 (n=11), 53: -35,536 (n=21), 11: -35,563 (n=13), 87: -35,609 (n=8), 64: -35,634 (n=17), 106: -35,704 (n=5), 129: -35,876 (n=73), 47: -35,882 (n=17), 37: -36,131 (n=9), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 67: -36,875 (n=17), 145: -36,990 (n=7), 75: -37,220 (n=8), 114: -37,370 (n=3), 12: -37,385 (n=10), 29: -37,535 (n=20), 140: -38,489 (n=3), 17: -38,658 (n=4), 131: -38,847 (n=2), 124: -39,372 (n=2), 132: -39,931 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,090 | 25 | 30 | 25 | 11771 | 10.03 | 25: -30,663 (n=5644), 26: -30,679 (n=369), 30: -30,822 (n=3788), 31: -31,834 (n=103), 29: -31,906 (n=98), 27: -32,434 (n=195), 28: -33,587 (n=1026), 35: -34,714 (n=170), 32: -34,852 (n=109), 38: -35,335 (n=16), 41: -35,551 (n=2), 33: -35,688 (n=104), 37: -35,850 (n=21), 34: -36,050 (n=55), 39: -36,508 (n=9), 44: -37,771 (n=4), 40: -38,012 (n=10), 36: -38,389 (n=30), 46: -38,521 (n=3), 47: -39,384 (n=2), 50: -40,579 (n=6), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,855 | 3 | 3 | 4 | 11773 | 2.61 | 3: -30,715 (n=10617), 2: -35,907 (n=829), 4: -36,568 (n=313), 5: -43,570 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,055 | 1 | 0 | 33 | 11771 | 25.76 | 1: -30,472 (n=607), 0: -30,981 (n=10160), 9: -31,302 (n=81), 22: -31,539 (n=2), 2: -32,455 (n=112), 6: -33,187 (n=63), 4: -33,280 (n=70), 8: -33,446 (n=62), 17: -33,644 (n=10), 5: -34,099 (n=106), 11: -34,345 (n=53), 19: -34,523 (n=4), 3: -34,592 (n=149), 7: -35,520 (n=66), 13: -35,577 (n=31), 28: -36,361 (n=2), 16: -36,379 (n=8), 12: -36,402 (n=25), 18: -36,506 (n=19), 14: -36,586 (n=16), 23: -36,694 (n=6), 20: -36,836 (n=5), 15: -36,840 (n=23), 10: -37,145 (n=40), 24: -37,504 (n=4), 21: -38,756 (n=6), 39: -38,995 (n=8), 26: -40,268 (n=3), 40: -41,262 (n=6), 29: -41,718 (n=20), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,924 | 61 | 100 | 101 | 11772 | 62.29 | 61: -27,918 (n=2), 138: -28,049 (n=2), 69: -28,538 (n=7), 130: -28,802 (n=10), 92: -29,398 (n=15), 80: -29,680 (n=95), 85: -30,054 (n=83), 65: -30,099 (n=5), 94: -30,112 (n=26), 86: -30,114 (n=504), 113: -30,212 (n=15), 93: -30,222 (n=320), 91: -30,321 (n=73), 129: -30,419 (n=15), 81: -30,473 (n=64), 100: -30,632 (n=7450), 114: -30,689 (n=21), 120: -30,726 (n=13), 111: -30,738 (n=30), 62: -30,897 (n=5), 84: -31,162 (n=56), 115: -31,166 (n=22), 141: -31,181 (n=2), 78: -31,203 (n=55), 133: -31,210 (n=9), 125: -31,291 (n=83), 66: -31,331 (n=11), 123: -31,432 (n=30), 83: -31,441 (n=105), 64: -31,589 (n=8), 102: -31,693 (n=39), 107: -31,718 (n=19), 70: -31,724 (n=16), 147: -31,811 (n=6), 103: -31,813 (n=22), 132: -31,873 (n=8), 63: -31,882 (n=9), 82: -31,935 (n=21), 109: -31,962 (n=23), 57: -31,969 (n=5), 95: -32,062 (n=31), 149: -32,176 (n=3), 87: -32,233 (n=17), 99: -32,241 (n=30), 128: -32,258 (n=15), 53: -32,281 (n=4), 90: -32,338 (n=59), 67: -32,542 (n=6), 104: -32,557 (n=482), 105: -32,613 (n=68), 68: -32,715 (n=9), 122: -32,768 (n=31), 71: -32,801 (n=19), 56: -32,821 (n=2), 101: -32,878 (n=29), 136: -33,061 (n=6), 119: -33,065 (n=13), 112: -33,142 (n=192), 127: -33,194 (n=24), 88: -33,319 (n=58), 97: -33,417 (n=49), 76: -33,459 (n=17), 89: -33,676 (n=136), 96: -33,693 (n=37), 79: -33,723 (n=36), 135: -33,726 (n=417), 117: -33,775 (n=51), 98: -33,847 (n=33), 59: -33,898 (n=4), 116: -33,918 (n=50), 124: -34,000 (n=20), 143: -34,012 (n=11), 108: -34,230 (n=23), 121: -34,260 (n=10), 110: -34,334 (n=18), 74: -34,399 (n=29), 134: -34,482 (n=7), 126: -34,517 (n=21), 75: -34,730 (n=54), 144: -34,772 (n=2), 55: -34,785 (n=2), 106: -35,145 (n=37), 137: -35,375 (n=3), 150: -35,453 (n=159), 77: -35,916 (n=14), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 58: -36,674 (n=4), 131: -36,786 (n=11), 73: -36,936 (n=9), 50: -37,008 (n=34), 118: -37,259 (n=13), 51: -37,500 (n=2), 72: -37,554 (n=9), 140: -38,416 (n=3), 54: -39,448 (n=3), 60: -39,580 (n=7), 145: -39,842 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,603 | 0.0 | 0.0 | 13 | 11773 | 10.1 | 0.0: -30,825 (n=10050), 0.1: -32,983 (n=859), 0.2: -33,868 (n=519), 0.4: -34,143 (n=71), 0.3: -34,652 (n=138), 0.5: -35,146 (n=43), 1.1: -35,241 (n=6), 0.7: -36,679 (n=15), 0.9: -37,063 (n=4), 0.6: -37,533 (n=33), 1.0: -37,910 (n=22), 1.2: -39,109 (n=8), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +11,143 | 17 | 20 | 11 | 11773 | 5.12 | 17: -30,746 (n=3600), 14: -30,948 (n=102), 16: -31,037 (n=270), 13: -31,076 (n=26), 19: -31,231 (n=548), 18: -31,333 (n=551), 20: -31,507 (n=6554), 15: -32,174 (n=101), 11: -32,310 (n=3), 12: -34,429 (n=11), 10: -41,889 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,946 | 6 | 6 | 8 | 11773 | 6.11 | 6: -30,639 (n=10462), 5: -34,689 (n=520), 7: -36,253 (n=329), 4: -37,218 (n=280), 3: -37,912 (n=107), 8: -38,376 (n=52), 9: -40,973 (n=17), 10: -41,585 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,683 | 6 | 18 | 21 | 11773 | 9.1 | 6: -29,449 (n=15), 14: -29,940 (n=16), 21: -30,397 (n=1914), 22: -30,696 (n=5665), 20: -31,185 (n=590), 23: -31,387 (n=547), 25: -32,306 (n=1017), 16: -32,382 (n=69), 17: -32,439 (n=642), 18: -32,839 (n=501), 24: -33,153 (n=362), 19: -33,589 (n=161), 12: -33,771 (n=10), 15: -33,782 (n=42), 9: -33,973 (n=44), 10: -34,521 (n=63), 13: -34,539 (n=21), 5: -35,957 (n=38), 11: -36,584 (n=32), 7: -36,889 (n=20), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,568 | 20 | 20 | 15 | 11773 | 6.98 | 20: -30,386 (n=6264), 19: -30,964 (n=3864), 18: -31,674 (n=272), 17: -34,283 (n=620), 21: -36,268 (n=247), 16: -36,506 (n=109), 23: -37,121 (n=55), 15: -37,333 (n=55), 22: -37,776 (n=118), 14: -38,094 (n=28), 26: -38,783 (n=34), 25: -38,834 (n=18), 24: -38,936 (n=60), 13: -39,604 (n=16), 12: -40,953 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,213 | 7 | 7 | 8 | 11773 | 6.07 | 7: -30,538 (n=10398), 6: -36,458 (n=721), 5: -36,485 (n=60), 8: -36,663 (n=379), 10: -36,770 (n=96), 9: -37,163 (n=79), 4: -38,581 (n=32), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +10,178 | 14 | 13 | 9 | 11773 | 4.42 | 14: -30,414 (n=1625), 13: -31,254 (n=7091), 11: -31,313 (n=657), 12: -31,378 (n=1715), 15: -31,459 (n=349), 16: -33,349 (n=196), 10: -34,113 (n=91), 9: -37,525 (n=36), 8: -40,592 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,093 | 10 | 8 | 11 | 11773 | 8.21 | 10: -30,555 (n=9856), 7: -32,641 (n=355), 8: -34,840 (n=807), 9: -34,911 (n=443), 6: -35,487 (n=139), 5: -35,952 (n=15), 12: -38,078 (n=40), 4: -38,638 (n=20), 11: -38,641 (n=53), 14: -39,191 (n=25), 13: -40,648 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,987 | 0.55 | 0.5 | 15 | 11773 | 6.69 | 0.55: -30,021 (n=6033), 0.65: -31,633 (n=1083), 0.5: -31,883 (n=3223), 0.75: -32,211 (n=83), 0.7: -32,254 (n=197), 0.6: -32,744 (n=286), 0.8: -33,051 (n=38), 0.45: -34,633 (n=367), 0.9: -34,927 (n=9), 0.85: -35,798 (n=11), 0.35: -36,126 (n=130), 0.4: -36,307 (n=131), 0.95: -37,209 (n=3), 1.0: -39,813 (n=6), 0.3: -40,008 (n=173) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,762 | 0 | 0 | 9 | 11773 | 7.12 | 0: -30,897 (n=10627), 1: -34,067 (n=613), 2: -34,628 (n=239), 3: -35,032 (n=196), 4: -35,794 (n=59), 5: -36,586 (n=17), 7: -36,592 (n=4), 6: -37,392 (n=15), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,786 | 2 | 2 | 4 | 11773 | 2.84 | 2: -30,996 (n=11307), 1: -36,998 (n=377), 3: -38,658 (n=34), 0: -39,783 (n=55) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,038 | 14 | 12 | 10 | 11773 | 7.48 | 14: -30,982 (n=9979), 13: -31,546 (n=800), 12: -32,939 (n=530), 11: -32,983 (n=177), 6: -34,434 (n=3), 9: -35,199 (n=24), 10: -35,450 (n=223), 7: -35,898 (n=8), 8: -37,051 (n=26), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,846 | frontier | frontier | 2 | 11773 | 0.92 | frontier: -30,922 (n=11279), v312: -38,769 (n=494) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,674 | 2 | 2 | 3 | 11773 | 1.82 | 2: -30,858 (n=11078), 1: -37,467 (n=653), 3: -38,532 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,430 | 38 | 40 | 30 | 11773 | 7.48 | 38: -30,134 (n=2363), 34: -30,272 (n=198), 33: -30,416 (n=47), 43: -30,496 (n=3329), 49: -30,563 (n=347), 30: -30,732 (n=54), 44: -31,011 (n=294), 39: -31,068 (n=389), 45: -31,147 (n=413), 47: -31,178 (n=176), 37: -31,191 (n=404), 27: -31,389 (n=8), 28: -31,698 (n=14), 32: -31,729 (n=54), 26: -31,931 (n=35), 31: -32,070 (n=33), 46: -32,301 (n=76), 29: -32,367 (n=13), 35: -32,502 (n=184), 40: -32,707 (n=2465), 42: -33,033 (n=191), 36: -33,071 (n=171), 50: -33,090 (n=310), 41: -33,252 (n=78), 25: -34,303 (n=4), 20: -35,006 (n=30), 48: -35,059 (n=60), 24: -35,533 (n=23), 23: -36,212 (n=6), 22: -37,564 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2226)
- (10, 3, 6): -16,840 (n=1856)
- (8, 3, 5): -16,866 (n=230)
- (9, 3, 6): -16,959 (n=1422)
- (8, 3, 6): -17,804 (n=633)
- (12, 4, 6): -17,899 (n=401)
- (10, 4, 6): -17,975 (n=1633)
- (11, 3, 6): -18,175 (n=418)
- (11, 4, 6): -19,867 (n=446)
- (17, 3, 6): -20,013 (n=50)
- (8, 4, 6): -21,051 (n=564)
- (13, 4, 6): -21,868 (n=154)
- (8, 3, 4): -22,126 (n=64)
- (13, 3, 6): -22,174 (n=222)
- (10, 3, 5): -22,188 (n=51)

_Generated 2026-09-08 14:44. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 2899 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=2899); harvest_min=1–3 (n=2899); wheat_tiles=0–8 (n=2899); wheat_stock=0–40 (n=2899); min_hands=3–6 (n=2899); load_per_hand=12–26 (n=2899); geese=0–2 (n=2899); open_melons=4–14 (n=2899)
- **Evidence:** 2899 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 34 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=34); harvest_min=1–3 (n=34); wheat_tiles=0–2 (n=34); wheat_stock=0–4 (n=34); min_hands=3–6 (n=34); load_per_hand=19–21 (n=34); geese=0–2 (n=34); open_melons=7–13 (n=34)
- **Evidence:** 34 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 21 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=21); harvest_min=1–3 (n=21); wheat_tiles=0; wheat_stock=0–29 (n=21); min_hands=3–6 (n=21); load_per_hand=12–20 (n=21); geese=0–1 (n=21); open_melons=9–13 (n=21)
- **Evidence:** 21 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 13 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=13); harvest_min=1–3 (n=13); wheat_tiles=0–8 (n=13); wheat_stock=0–39 (n=13); min_hands=3–6 (n=13); load_per_hand=12–17 (n=13); geese=0–2 (n=13); open_melons=8–14 (n=13)
- **Evidence:** 13 candidates, multiple seeds. Confidence: moderate

### None (observed in 7 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=7); harvest_min=1–2 (n=7); wheat_tiles=0; wheat_stock=0–11 (n=7); min_hands=3–6 (n=7); load_per_hand=12–18 (n=7); geese=0–2 (n=7); open_melons=10–14 (n=7)
- **Evidence:** 7 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 14:44. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._