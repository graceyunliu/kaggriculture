# Evolution run 20260905-194022

Frontier opponent: `H32.py` · clone: `tape_mengfeili_105887030.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.06 h · candidates evaluated this run: 1243 · games 30,522 (14,828/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 219 | 438 |
| dead_pattern | 238 | 476 |
| dead_smoke | 203 | 1624 |
| alive | 583 | 27984 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 4112 · held-out evaluated: 0 · held-out PASS: 0

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
| `667332b39bf5` | queue | archive_crossover:crossover_g000850_20260905-205857_1 | -15,738 | -3.0 | 3-7 | -27,827 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `512e53fe15bc` | wide | paired | -16,047 | -3.7 | 1-9 | -15,964 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→37, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `7eb169e63774` | queue | archive_crossover:crossover_g000800_20260905-205431_1 | -16,091 | -3.4 | 2-8 | -16,982 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `a71aba279a14` | queue | archive_crossover:crossover_g000125_20260905-195057_1 | -16,104 | -3.6 | 1-9 | -16,325 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `d04cc6dfa57a` | queue | archive_crossover:crossover_g000375_20260905-201121_1 | -16,336 | -3.6 | 1-9 | -16,325 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `c073385d7bff` | queue | archive_crossover:crossover_g000550_20260905-202915_0 | -16,387 | -3.3 | 2-8 | -16,561 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→25, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `d7eb9d3d47a8` | queue | archive_crossover:crossover_g000525_20260905-184049_1 | -16,488 | -3.4 | 2-8 | -27,523 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `0a8e7066b5c4` | c1 | mutate | -16,565 | -3.3 | 2-8 | -17,301 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→25, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `5cf96dc0b3c7` | queue | archive_crossover:crossover_g000325_20260905-200746_0 | -16,628 | -3.4 | 2-8 | -29,647 | alive | melon_floor 150→100, harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `c23a3c07bd27` | queue | crossover | -16,661 | -3.3 | 2-8 | -28,384 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `21f16d71a4a8` | queue | archive_crossover:crossover_g000400_20260905-201323_0 | -16,807 | -3.4 | 2-8 | -32,238 | alive | melon_floor 150→100, harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `43c50ead663e` | queue | archive_crossover:crossover_g000450_20260905-201900_1 | -16,840 | -4.2 | 1-9 | -20,080 | alive | melon_floor 150→100, harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→25, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `0a4075f306d0` | queue | crossover | -16,846 | -3.6 | 2-8 | -17,751 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→44, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `b223d8a81851` | queue | migrate | -16,860 | -3.3 | 2-8 | -30,307 | alive | melon_floor 150→100, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→25, wheat_sell_price 30→25, labor_reserve_buffer 50→58, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `23955eb36d5b` | queue | archive_crossover:crossover_g000600_20260905-203302_0 | -16,867 | -3.5 | 2-8 | -14,991 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |

## Islands (best dev margin, population size)

- H32: best -18,936 (`236b0dcc607b`), n=159
- M2: best -18,310 (`c671a5538a68`), n=178
- c1: best -16,565 (`0a8e7066b5c4`), n=934
- queue: best -15,738 (`667332b39bf5`), n=1208
- v312: best -17,031 (`f665e5aabacb`), n=932
- wide: best -16,047 (`512e53fe15bc`), n=701

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| ROUTE_LEN | 14,211 | 3 | 3 | 3: -31,722 (3651), 2: -36,195 (350), 4: -37,302 (108), 5: -45,933 (3) |
| MELON_PRICE_CUSHION | 13,396 | 65 | 100 | 65: -28,144 (2), 69: -29,694 (3), 94: -29,794 (6), 66: -30,176 (7), 93: -30,244 (65), 70: -30,657 (6), 114: -30,668 (10), 86: -30,883 (59), 100: -31,136 (2388), 63: -31,210 (3), 74: -31,415 (10), 129: -31,459 (9), 85: -31,467 (18), 76: -31,633 (9), 125: -31,720 (19), 132: -31,783 (3), 111: -31,930 (15), 105: -31,951 (22), 147: -31,970 (4), 87: -32,023 (6), 83: -32,049 (49), 133: -32,254 (4), 59: -32,381 (2), 130: -32,409 (4), 78: -32,419 (9), 108: -33,085 (11), 122: -33,087 (17), 99: -33,091 (7), 149: -33,138 (2), 67: -33,385 (2), 89: -33,413 (86), 71: -33,426 (12), 136: -33,457 (3), 95: -33,488 (17), 112: -33,618 (144), 64: -33,629 (4), 102: -33,633 (17), 135: -33,806 (295), 126: -33,885 (11), 82: -33,889 (4), 113: -33,930 (3), 120: -34,068 (4), 96: -34,083 (21), 92: -34,097 (5), 143: -34,106 (6), 88: -34,112 (35), 68: -34,145 (4), 97: -34,173 (27), 104: -34,210 (212), 142: -34,291 (4), 103: -34,358 (9), 148: -34,572 (2), 128: -34,671 (5), 107: -34,777 (5), 91: -34,842 (21), 84: -34,852 (10), 109: -34,924 (10), 150: -34,993 (97), 110: -35,261 (9), 106: -35,329 (16), 115: -35,375 (5), 75: -35,376 (44), 116: -35,437 (20), 117: -35,504 (26), 124: -35,538 (15), 123: -35,551 (5), 127: -35,579 (6), 52: -35,646 (2), 79: -35,834 (7), 118: -35,874 (5), 134: -36,723 (3), 80: -36,725 (4), 101: -36,753 (8), 50: -36,754 (11), 98: -37,068 (10), 77: -37,164 (8), 119: -37,430 (5), 90: -37,579 (8), 73: -37,893 (4), 72: -38,136 (5), 60: -38,171 (4), 131: -38,355 (8), 145: -38,434 (6), 81: -39,307 (2), 54: -39,448 (3), 121: -40,188 (4), 140: -40,282 (2), 139: -40,609 (5), 58: -41,540 (2) |
| wheat_cap | 13,358 | 14 | 18 | 14: -27,540 (7), 21: -30,917 (550), 20: -31,075 (315), 22: -31,733 (1622), 17: -32,382 (350), 23: -32,607 (155), 12: -32,981 (6), 16: -33,124 (33), 9: -33,581 (30), 25: -33,590 (465), 18: -33,611 (256), 24: -33,840 (125), 10: -34,578 (54), 19: -34,611 (51), 15: -34,769 (18), 13: -35,733 (10), 11: -36,937 (29), 7: -37,248 (17), 5: -38,364 (15), 6: -38,904 (2), 8: -40,898 (2) |
| labor_reserve_buffer | 12,933 | 35 | 50 | 35: -28,345 (3), 27: -28,409 (13), 104: -28,663 (2), 58: -28,769 (18), 85: -28,921 (4), 49: -29,284 (7), 61: -29,778 (58), 18: -29,796 (126), 65: -30,512 (39), 60: -30,604 (11), 48: -30,670 (242), 90: -30,728 (2), 25: -30,748 (3), 144: -31,182 (2), 59: -31,243 (7), 33: -31,263 (14), 50: -31,304 (1846), 93: -31,438 (4), 57: -31,528 (57), 63: -31,567 (6), 26: -31,811 (2), 38: -31,933 (6), 56: -32,051 (4), 40: -32,289 (58), 83: -32,402 (61), 62: -32,443 (9), 19: -32,490 (2), 44: -32,524 (9), 73: -32,529 (7), 76: -32,534 (4), 24: -32,612 (4), 111: -32,641 (3), 42: -32,676 (320), 28: -32,945 (12), 39: -33,184 (37), 4: -33,260 (34), 36: -33,275 (11), 7: -33,340 (2), 119: -33,340 (2), 43: -33,399 (8), 52: -33,558 (3), 115: -33,572 (2), 78: -33,572 (3), 88: -33,585 (6), 0: -33,601 (88), 80: -33,788 (5), 94: -33,791 (9), 34: -33,853 (17), 6: -33,901 (5), 84: -33,930 (7), 55: -33,993 (284), 51: -33,998 (3), 13: -34,125 (3), 103: -34,175 (3), 69: -34,177 (9), 14: -34,333 (4), 70: -34,534 (10), 41: -34,617 (7), 82: -34,695 (13), 29: -34,697 (6), 99: -34,708 (58), 74: -34,756 (6), 45: -34,785 (35), 110: -34,863 (2), 77: -34,951 (173), 30: -34,984 (3), 53: -35,165 (5), 46: -35,179 (14), 129: -35,199 (57), 100: -35,385 (26), 68: -35,536 (3), 81: -35,572 (17), 32: -35,665 (3), 31: -35,716 (4), 47: -35,800 (9), 91: -35,937 (3), 21: -35,947 (2), 106: -36,115 (2), 101: -36,200 (7), 66: -36,233 (11), 3: -36,240 (2), 23: -36,354 (5), 22: -36,407 (4), 16: -36,603 (10), 10: -36,732 (7), 107: -36,913 (2), 145: -36,990 (7), 11: -36,993 (11), 15: -37,056 (3), 114: -37,370 (3), 97: -37,411 (5), 64: -37,446 (7), 102: -37,461 (2), 1: -37,771 (3), 12: -37,835 (6), 37: -38,174 (2), 87: -38,817 (3), 150: -39,400 (12), 67: -40,756 (5), 136: -41,277 (2) |
| load_per_hand | 12,751 | 19 | 20 | 19: -31,263 (2218), 20: -31,967 (1055), 18: -33,195 (96), 17: -34,238 (428), 21: -35,954 (117), 16: -37,159 (47), 23: -37,166 (27), 24: -37,252 (10), 15: -37,301 (25), 22: -37,548 (31), 14: -37,912 (14), 25: -39,428 (10), 26: -39,755 (17), 13: -41,358 (11), 12: -44,013 (6) |
| CROP_SWEEP_LEN | 11,070 | 6 | 6 | 6: -31,533 (3460), 5: -35,217 (216), 7: -35,679 (230), 4: -36,890 (111), 3: -37,591 (54), 8: -38,645 (29), 9: -40,210 (9), 10: -42,603 (3) |
| wheat_tiles | 10,969 | 0 | 0 | 0: -31,902 (3621), 1: -34,260 (279), 7: -34,992 (2), 2: -35,516 (92), 3: -35,607 (89), 4: -35,718 (12), 5: -36,728 (9), 6: -37,473 (6), 8: -42,871 (2) |
| max_animals | 10,749 | 17 | 20 | 17: -31,875 (735), 20: -32,180 (2893), 16: -32,639 (103), 18: -32,714 (176), 14: -33,099 (16), 19: -33,399 (139), 13: -35,947 (12), 15: -36,281 (27), 12: -38,342 (7), 10: -42,624 (3) |
| wheat_stock | 10,597 | 9 | 0 | 9: -31,535 (48), 6: -31,891 (19), 0: -31,916 (3609), 4: -32,738 (21), 19: -32,920 (2), 8: -33,483 (23), 5: -34,171 (34), 1: -34,492 (123), 3: -34,788 (88), 10: -35,567 (14), 2: -35,984 (27), 7: -36,013 (26), 28: -36,361 (2), 23: -36,391 (4), 13: -36,506 (12), 17: -36,558 (2), 15: -37,072 (8), 14: -37,212 (6), 11: -37,317 (10), 12: -37,832 (8), 29: -38,302 (4), 20: -38,590 (4), 18: -38,877 (5), 39: -39,247 (2), 40: -41,450 (5), 33: -42,132 (3) |
| MELON_MAX_TILES | 10,576 | 38 | 40 | 38: -29,097 (201), 33: -29,658 (18), 43: -30,701 (1202), 49: -31,167 (86), 31: -31,598 (15), 46: -32,215 (19), 35: -32,629 (100), 30: -32,715 (8), 40: -33,021 (1668), 47: -33,119 (63), 36: -33,131 (105), 45: -33,143 (121), 37: -33,176 (30), 41: -33,177 (30), 28: -33,424 (5), 44: -33,548 (66), 48: -33,924 (19), 42: -34,234 (102), 50: -34,535 (108), 32: -34,635 (13), 34: -34,680 (27), 39: -35,096 (55), 20: -35,860 (11), 24: -35,886 (19), 29: -36,140 (7), 23: -36,659 (3), 27: -37,083 (3), 22: -39,119 (2), 26: -39,673 (6) |
| MAX_HANDS | 9,969 | 12 | 13 | 12: -31,777 (925), 11: -31,911 (375), 13: -32,250 (2510), 14: -32,422 (150), 15: -33,794 (56), 10: -35,628 (41), 16: -37,981 (41), 9: -39,898 (7), 8: -41,746 (7) |
| wheat_sell_price | 9,961 | 26 | 30 | 26: -31,359 (163), 30: -31,423 (1322), 25: -31,475 (1605), 27: -33,041 (80), 29: -33,661 (42), 31: -33,843 (48), 44: -34,154 (3), 35: -34,292 (134), 28: -34,537 (532), 38: -35,468 (11), 40: -35,635 (5), 34: -35,776 (24), 37: -36,190 (14), 33: -36,660 (53), 32: -36,747 (45), 39: -37,577 (7), 36: -38,695 (16), 46: -39,707 (2), 43: -41,320 (3) |
| demand_share | 9,150 | 0.55 | 0.5 | 0.55: -30,633 (921), 0.65: -31,644 (760), 0.75: -31,706 (22), 0.5: -32,427 (1886), 0.6: -33,018 (138), 0.8: -33,153 (10), 0.7: -34,412 (47), 0.9: -34,743 (4), 0.45: -35,409 (131), 0.4: -36,228 (46), 0.85: -36,613 (6), 0.35: -36,636 (76), 0.95: -37,587 (2), 1.0: -39,628 (4), 0.3: -39,782 (59) |
| open_melons | 9,110 | 10 | 8 | 10: -31,247 (3016), 9: -34,375 (260), 7: -34,472 (115), 8: -34,934 (566), 6: -35,075 (73), 5: -36,005 (3), 11: -38,079 (27), 14: -38,892 (14), 12: -38,973 (18), 4: -39,292 (13), 13: -40,357 (7) |
| wheat_per_animal | 8,826 | 0.0 | 0.0 | 0.0: -31,712 (3083), 0.1: -33,071 (556), 0.2: -34,026 (329), 1.1: -34,046 (2), 0.5: -36,135 (8), 0.3: -36,284 (51), 0.4: -36,725 (36), 0.7: -36,825 (11), 0.6: -37,078 (8), 1.0: -37,269 (18), 0.9: -39,381 (2), 1.2: -39,773 (6), 0.8: -40,539 (2) |
| open_wheat | 8,618 | 7 | 7 | 7: -31,492 (3493), 6: -36,163 (373), 5: -36,538 (31), 10: -36,875 (51), 8: -36,887 (118), 9: -38,543 (26), 4: -39,469 (15), 3: -40,110 (5) |
| setup_capital_share | 8,228 | 0.05 | 0.25 | 0.05: -29,434 (156), 0.1: -31,621 (70), 0.25: -32,054 (3204), 0.15: -32,399 (108), 0.2: -32,953 (184), 0.4: -33,758 (60), 0.0: -33,934 (73), 0.45: -34,242 (19), 0.3: -34,579 (102), 0.35: -35,348 (94), 0.5: -37,661 (42) |
| open_sheep | 7,812 | 2 | 2 | 2: -31,974 (3899), 1: -36,937 (164), 3: -38,995 (25), 0: -39,785 (24) |
| opening | 7,240 | frontier | frontier | frontier: -31,855 (3882), v312: -39,094 (230) |
| open_cows | 7,154 | 2 | 2 | 2: -31,843 (3800), 1: -37,230 (293), 3: -38,997 (19) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,738 (n=511)
- (10, 3, 6): -16,840 (n=560)
- (11, 3, 6): -18,175 (n=171)
- (8, 3, 6): -18,403 (n=348)
- (8, 3, 5): -18,554 (n=140)
- (12, 4, 6): -19,210 (n=216)
- (9, 3, 6): -19,729 (n=356)
- (11, 4, 6): -19,867 (n=258)
- (17, 3, 6): -20,338 (n=38)
- (10, 4, 6): -20,442 (n=478)
- (8, 4, 6): -21,523 (n=239)
- (13, 4, 6): -21,868 (n=41)
- (10, 3, 5): -22,188 (n=17)
- (13, 3, 6): -22,519 (n=114)
- (14, 3, 6): -23,164 (n=47)

_Generated 2026-09-05 21:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._