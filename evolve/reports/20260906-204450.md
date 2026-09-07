# Evolution run 20260906-204450

Frontier opponent: `H32.py` · clone: `tape_mengfeili_105887030.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1228 · games 30,766 (15,347/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 211 | 422 |
| dead_pattern | 232 | 464 |
| dead_smoke | 195 | 1560 |
| alive | 590 | 28320 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 5285 · held-out evaluated: 0 · held-out PASS: 0

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
| `fe4745b56024` | queue | archive_crossover:crossover_g000675_20260905-224724_0 | -15,412 | -3.3 | 2-8 | -17,273 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `a3436012d4f9` | queue | archive_crossover:crossover_g000725_20260906-214654_0 | -15,590 | -3.3 | 2-8 | -16,712 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `667332b39bf5` | queue | archive_crossover:crossover_g000850_20260905-205857_1 | -15,738 | -3.0 | 3-7 | -27,827 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `97e03be128cb` | queue | archive_crossover:crossover_g000400_20260906-211828_1 | -15,791 | -3.5 | 2-8 | -16,760 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `2286322870c4` | v312 | mutate | -15,854 | -3.0 | 3-7 | -14,497 | alive | harvest_min 2→3, open_melons 8→10, early_hire_days 5→8, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→42, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5 |
| `5b63d512ad81` | queue | archive_crossover:crossover_g000775_20260906-215507_0 | -15,896 | -3.3 | 2-8 | -15,996 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `081b43704bb8` | queue | archive_crossover:crossover_g000125_20260905-215729_0 | -15,916 | -3.1 | 2-8 | -28,354 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→7, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `165447af42cc` | queue | mutate | -15,936 | -3.5 | 2-8 | -16,892 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→0, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3 |
| `512e53fe15bc` | wide | paired | -16,047 | -3.7 | 1-9 | -15,964 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→37, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `7eb169e63774` | queue | archive_crossover:crossover_g000800_20260905-205431_1 | -16,091 | -3.4 | 2-8 | -16,982 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `a71aba279a14` | queue | archive_crossover:crossover_g000125_20260905-195057_1 | -16,104 | -3.6 | 1-9 | -16,325 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `23734cef4da1` | c1 | paired | -16,310 | -4.1 | 1-9 | -14,549 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `d04cc6dfa57a` | queue | archive_crossover:crossover_g000375_20260905-201121_1 | -16,336 | -3.6 | 1-9 | -16,325 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `136c45d49c20` | queue | archive_crossover:crossover_g000800_20260906-215709_0 | -16,353 | -3.3 | 2-8 | -16,640 | alive | melon_floor 150→0, harvest_min 2→3, open_melons 8→10, early_hire_days 5→3, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→42, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25, SPREAD_CAP 5→3 |

## Islands (best dev margin, population size)

- H32: best -15,269 (`0c3989f7d742`), n=346
- M2: best -17,604 (`97ba0a0f33e3`), n=373
- c1: best -16,310 (`23734cef4da1`), n=1115
- queue: best -15,412 (`fe4745b56024`), n=1489
- v312: best -15,854 (`2286322870c4`), n=1110
- wide: best -16,047 (`512e53fe15bc`), n=852

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| labor_reserve_buffer | 18,968 | 86 | 50 | 86: -20,673 (2), 72: -22,870 (2), 5: -25,861 (4), 71: -26,043 (4), 49: -27,654 (12), 9: -27,732 (4), 89: -28,054 (2), 35: -28,345 (3), 92: -28,473 (15), 58: -28,634 (27), 27: -28,856 (26), 85: -28,921 (4), 18: -29,643 (228), 61: -30,075 (62), 136: -30,346 (9), 48: -30,394 (285), 65: -30,534 (53), 63: -30,614 (11), 90: -30,728 (2), 56: -30,766 (5), 60: -30,849 (15), 50: -30,979 (2509), 33: -31,139 (15), 144: -31,182 (2), 59: -31,243 (7), 24: -31,352 (11), 93: -31,438 (4), 52: -31,464 (4), 115: -31,553 (4), 26: -31,811 (2), 25: -31,865 (4), 57: -31,957 (66), 40: -32,033 (65), 45: -32,034 (53), 103: -32,034 (4), 42: -32,141 (366), 19: -32,198 (3), 51: -32,244 (6), 62: -32,249 (10), 38: -32,292 (9), 74: -32,370 (16), 80: -32,481 (7), 73: -32,529 (7), 70: -32,573 (12), 28: -32,609 (14), 83: -32,615 (68), 104: -32,627 (3), 44: -32,692 (10), 39: -32,786 (43), 6: -33,118 (7), 76: -33,125 (5), 36: -33,216 (13), 4: -33,260 (34), 119: -33,340 (2), 84: -33,403 (8), 7: -33,417 (3), 111: -33,417 (5), 78: -33,572 (3), 0: -33,577 (104), 88: -33,585 (6), 55: -33,732 (317), 94: -33,747 (11), 43: -33,801 (11), 34: -33,963 (24), 13: -34,071 (4), 54: -34,086 (3), 69: -34,177 (9), 14: -34,333 (4), 21: -34,457 (4), 91: -34,507 (4), 99: -34,708 (58), 41: -34,775 (11), 53: -34,924 (7), 82: -34,939 (16), 30: -34,984 (3), 47: -35,008 (10), 77: -35,045 (181), 81: -35,147 (18), 29: -35,175 (7), 46: -35,312 (16), 100: -35,349 (27), 129: -35,370 (59), 22: -35,414 (11), 68: -35,536 (3), 97: -35,635 (8), 87: -35,642 (6), 31: -35,716 (4), 107: -35,804 (3), 32: -36,008 (6), 106: -36,115 (2), 3: -36,144 (4), 101: -36,200 (7), 66: -36,266 (16), 110: -36,353 (3), 79: -36,492 (2), 23: -36,562 (7), 16: -36,603 (10), 109: -36,655 (2), 145: -36,990 (7), 11: -36,993 (11), 10: -37,028 (9), 15: -37,056 (3), 64: -37,278 (10), 114: -37,370 (3), 67: -37,771 (8), 1: -37,771 (3), 12: -37,835 (6), 102: -38,189 (3), 150: -38,743 (13), 37: -39,641 (3) |
| ROUTE_LEN | 14,057 | 3 | 3 | 3: -31,272 (4728), 2: -36,201 (417), 4: -36,946 (136), 5: -45,329 (4) |
| MELON_PRICE_CUSHION | 13,396 | 65 | 100 | 65: -28,144 (2), 130: -29,299 (7), 69: -29,694 (3), 64: -29,716 (6), 66: -30,176 (7), 93: -30,199 (111), 86: -30,200 (129), 94: -30,484 (7), 85: -30,502 (33), 114: -30,634 (14), 70: -30,641 (11), 100: -30,817 (3123), 105: -31,178 (37), 63: -31,210 (3), 129: -31,340 (10), 125: -31,387 (43), 76: -31,633 (9), 132: -31,783 (3), 81: -31,794 (7), 111: -31,815 (16), 147: -31,970 (4), 133: -32,096 (5), 57: -32,136 (2), 149: -32,176 (3), 83: -32,231 (55), 68: -32,262 (5), 115: -32,306 (9), 74: -32,355 (13), 113: -32,399 (5), 127: -32,420 (12), 122: -32,724 (24), 102: -32,753 (22), 87: -32,812 (8), 136: -32,828 (4), 95: -32,847 (19), 107: -32,870 (8), 71: -33,052 (13), 120: -33,221 (5), 90: -33,285 (12), 67: -33,385 (2), 104: -33,396 (262), 89: -33,397 (97), 99: -33,452 (13), 97: -33,479 (33), 59: -33,500 (3), 112: -33,520 (162), 135: -33,665 (318), 80: -33,670 (5), 91: -33,697 (24), 108: -33,835 (12), 78: -33,842 (12), 88: -33,860 (38), 82: -33,990 (5), 96: -33,998 (23), 119: -34,026 (9), 92: -34,097 (5), 143: -34,119 (9), 124: -34,422 (18), 150: -34,651 (111), 109: -34,698 (11), 103: -34,708 (10), 126: -34,779 (13), 116: -34,903 (25), 52: -34,987 (3), 79: -35,008 (8), 128: -35,152 (7), 84: -35,174 (11), 123: -35,222 (7), 75: -35,376 (44), 101: -35,414 (11), 117: -35,504 (26), 106: -35,572 (19), 110: -36,136 (12), 118: -36,177 (6), 142: -36,268 (7), 148: -36,528 (3), 77: -37,164 (8), 98: -37,247 (12), 51: -37,500 (2), 73: -37,893 (4), 139: -38,005 (6), 145: -38,013 (7), 72: -38,136 (5), 60: -38,171 (4), 134: -38,214 (5), 50: -38,250 (14), 131: -38,355 (8), 54: -39,448 (3), 121: -40,188 (4), 140: -40,282 (2), 58: -41,540 (2) |
| load_per_hand | 13,010 | 20 | 20 | 20: -30,859 (1802), 19: -31,182 (2522), 18: -33,042 (117), 17: -34,263 (471), 21: -36,127 (133), 16: -36,815 (57), 23: -36,978 (31), 22: -37,352 (44), 15: -37,419 (28), 24: -37,638 (14), 14: -38,041 (15), 26: -39,342 (20), 25: -39,439 (12), 13: -41,358 (11), 12: -43,869 (8) |
| max_animals | 12,664 | 14 | 20 | 14: -30,465 (33), 17: -31,337 (1065), 16: -31,704 (145), 20: -31,850 (3552), 18: -31,963 (251), 19: -32,840 (176), 13: -34,262 (16), 15: -35,274 (34), 12: -37,278 (8), 10: -43,129 (4) |
| CROP_SWEEP_LEN | 11,490 | 6 | 6 | 6: -31,112 (4541), 5: -35,064 (264), 7: -35,791 (243), 4: -37,045 (132), 3: -37,839 (60), 8: -38,644 (32), 9: -39,738 (10), 10: -42,603 (3) |
| wheat_tiles | 11,425 | 0 | 0 | 0: -31,446 (4702), 1: -34,278 (319), 7: -34,992 (2), 3: -35,301 (108), 2: -35,311 (113), 4: -35,460 (20), 5: -36,304 (13), 6: -37,473 (6), 8: -42,871 (2) |
| wheat_per_animal | 11,301 | 0.0 | 0.0 | 0.0: -31,253 (4148), 0.1: -33,103 (607), 0.2: -33,882 (359), 1.1: -34,046 (2), 0.5: -34,559 (13), 0.4: -36,240 (39), 0.3: -36,258 (65), 0.7: -37,260 (13), 0.6: -37,358 (9), 1.0: -37,388 (19), 0.9: -39,381 (2), 1.2: -39,773 (6), 0.8: -42,554 (3) |
| wheat_stock | 11,173 | 9 | 0 | 9: -31,353 (53), 0: -31,469 (4668), 6: -32,097 (23), 17: -32,662 (3), 19: -32,920 (2), 1: -33,418 (152), 4: -33,636 (31), 8: -33,770 (27), 5: -34,020 (41), 2: -34,777 (36), 3: -35,053 (101), 11: -35,314 (16), 21: -35,375 (2), 10: -36,222 (16), 7: -36,281 (32), 13: -36,282 (13), 28: -36,361 (2), 23: -36,391 (4), 15: -36,461 (11), 14: -36,829 (10), 12: -38,241 (10), 18: -38,529 (8), 20: -38,590 (4), 39: -38,737 (3), 29: -39,509 (5), 40: -41,450 (5), 33: -42,526 (4) |
| wheat_cap | 11,046 | 14 | 18 | 14: -28,792 (9), 21: -30,560 (746), 20: -30,998 (363), 22: -31,165 (2164), 23: -32,049 (204), 17: -32,132 (425), 12: -32,981 (6), 25: -33,035 (583), 16: -33,242 (38), 18: -33,523 (297), 24: -33,594 (185), 9: -33,715 (34), 15: -34,314 (26), 19: -34,436 (72), 10: -34,506 (56), 13: -35,733 (10), 11: -36,937 (29), 7: -37,177 (18), 5: -38,364 (15), 6: -38,904 (2), 8: -39,838 (3) |
| MAX_HANDS | 10,963 | 14 | 13 | 14: -31,145 (260), 12: -31,546 (1081), 13: -31,748 (3279), 11: -31,901 (438), 15: -32,658 (104), 10: -35,222 (52), 16: -36,365 (55), 9: -39,720 (8), 8: -42,108 (8) |
| MELON_MAX_TILES | 10,911 | 38 | 40 | 38: -29,176 (443), 43: -30,488 (1605), 33: -30,594 (25), 37: -30,862 (88), 49: -30,985 (122), 46: -31,464 (29), 32: -31,781 (20), 34: -31,791 (49), 31: -31,945 (18), 44: -32,144 (81), 35: -32,354 (116), 45: -32,708 (156), 40: -32,850 (1862), 36: -33,055 (115), 47: -33,308 (75), 41: -33,521 (38), 50: -33,537 (150), 30: -33,789 (10), 39: -33,976 (73), 28: -34,003 (6), 42: -34,011 (120), 48: -34,852 (24), 20: -35,462 (15), 29: -35,552 (8), 24: -36,058 (20), 23: -36,659 (3), 27: -37,083 (3), 22: -39,119 (2), 26: -40,087 (8) |
| wheat_sell_price | 10,373 | 25 | 30 | 25: -30,948 (2236), 30: -31,231 (1707), 26: -31,400 (177), 27: -32,440 (99), 29: -33,677 (52), 31: -33,806 (51), 28: -34,094 (618), 44: -34,154 (3), 35: -34,437 (138), 38: -35,517 (12), 40: -35,635 (5), 34: -35,903 (29), 32: -36,180 (54), 37: -36,190 (14), 33: -36,664 (56), 39: -37,577 (7), 36: -39,255 (18), 46: -39,707 (2), 43: -41,320 (3) |
| demand_share | 9,835 | 0.55 | 0.5 | 0.55: -29,995 (1646), 0.65: -31,650 (835), 0.75: -32,175 (28), 0.5: -32,256 (2136), 0.6: -32,731 (158), 0.8: -33,840 (17), 0.7: -34,171 (69), 0.9: -34,743 (4), 0.45: -35,112 (165), 0.4: -36,175 (59), 0.85: -36,289 (8), 0.35: -36,481 (80), 0.95: -37,587 (2), 0.3: -39,766 (73), 1.0: -39,830 (5) |
| open_melons | 9,764 | 10 | 8 | 10: -30,846 (4061), 7: -33,900 (142), 9: -34,481 (290), 8: -34,941 (608), 6: -35,263 (83), 5: -35,428 (5), 11: -38,368 (30), 12: -38,568 (22), 4: -38,631 (14), 14: -38,941 (18), 13: -40,610 (12) |
| open_wheat | 9,084 | 7 | 7 | 7: -31,026 (4539), 6: -36,166 (438), 5: -36,428 (37), 10: -36,998 (63), 8: -37,033 (151), 9: -38,392 (36), 4: -39,743 (16), 3: -40,110 (5) |
| open_sheep | 8,172 | 2 | 2 | 2: -31,527 (5022), 1: -36,815 (206), 3: -38,946 (26), 0: -39,700 (31) |
| setup_capital_share | 8,086 | 0.05 | 0.25 | 0.05: -29,715 (397), 0.1: -31,400 (138), 0.25: -31,744 (3857), 0.2: -32,138 (247), 0.15: -32,158 (147), 0.0: -32,604 (121), 0.4: -32,900 (75), 0.3: -33,771 (119), 0.45: -33,857 (25), 0.35: -34,669 (116), 0.5: -37,802 (43) |
| open_cows | 7,555 | 2 | 2 | 2: -31,413 (4928), 1: -37,308 (336), 3: -38,968 (21) |
| opening | 7,551 | frontier | frontier | frontier: -31,426 (5011), v312: -38,978 (274) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=795)
- (10, 3, 6): -16,840 (n=759)
- (8, 3, 5): -17,352 (n=154)
- (11, 3, 6): -18,175 (n=213)
- (9, 3, 6): -18,255 (n=500)
- (12, 4, 6): -18,258 (n=246)
- (8, 3, 6): -18,403 (n=398)
- (11, 4, 6): -19,867 (n=285)
- (17, 3, 6): -20,338 (n=42)
- (10, 4, 6): -20,442 (n=649)
- (8, 4, 6): -21,051 (n=286)
- (13, 4, 6): -21,868 (n=54)
- (10, 3, 5): -22,188 (n=20)
- (13, 3, 6): -22,519 (n=129)
- (9, 3, 5): -23,138 (n=61)

_Generated 2026-09-06 22:45. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._