# Evolution run 20260907-030609

Frontier opponent: `H32.py` · clone: `tape_mengfeili_105887030.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.09 h · candidates evaluated this run: 1451 · games 30,676 (14,658/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 348 | 696 |
| dead_pattern | 314 | 628 |
| dead_smoke | 213 | 1704 |
| alive | 576 | 27648 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 7032 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=618
- M2: best -16,932 (`8aea624a62b9`), n=624
- c1: best -16,310 (`23734cef4da1`), n=1389
- queue: best -15,412 (`fe4745b56024`), n=1912
- v312: best -15,275 (`52b3d5cc236e`), n=1372
- wide: best -16,047 (`512e53fe15bc`), n=1117

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| wheat_stock | 14,210 | 0 | 0 | 0: -31,095 (6214), 9: -31,150 (62), 6: -31,765 (35), 1: -32,294 (212), 19: -32,857 (3), 17: -33,304 (5), 4: -33,615 (40), 8: -33,632 (39), 2: -33,966 (47), 5: -34,004 (57), 11: -34,605 (28), 3: -34,982 (112), 16: -35,043 (5), 13: -35,835 (16), 7: -36,034 (41), 15: -36,187 (15), 28: -36,361 (2), 10: -36,546 (25), 14: -36,808 (11), 20: -36,836 (5), 23: -37,081 (5), 12: -37,268 (14), 21: -38,105 (3), 18: -38,193 (10), 39: -41,294 (4), 40: -41,450 (5), 29: -41,585 (10), 33: -42,526 (4), 26: -45,305 (2) |
| load_per_hand | 12,751 | 20 | 20 | 20: -30,302 (2992), 19: -31,122 (2906), 18: -32,396 (149), 17: -34,302 (517), 21: -36,156 (165), 16: -36,663 (67), 23: -36,984 (38), 15: -37,186 (35), 22: -37,597 (58), 24: -38,093 (28), 14: -38,200 (19), 25: -38,533 (15), 26: -39,358 (22), 13: -40,253 (12), 12: -43,054 (9) |
| wheat_per_animal | 12,537 | 0.0 | 0.0 | 0.0: -30,875 (5728), 1.1: -32,362 (3), 0.1: -33,131 (679), 0.2: -34,033 (410), 0.5: -34,998 (24), 0.4: -35,350 (49), 0.3: -35,668 (78), 0.7: -37,204 (14), 1.0: -37,474 (20), 0.6: -37,790 (14), 0.9: -39,381 (2), 1.2: -39,783 (7), 0.8: -43,412 (4) |
| CROP_SWEEP_LEN | 12,499 | 6 | 6 | 6: -30,750 (6135), 5: -34,907 (329), 7: -35,886 (265), 4: -37,181 (172), 3: -37,748 (74), 8: -38,457 (38), 9: -41,192 (15), 10: -43,248 (4) |
| max_animals | 12,476 | 17 | 20 | 17: -30,699 (1739), 14: -31,032 (61), 16: -31,427 (181), 18: -31,550 (321), 20: -31,644 (4378), 19: -31,834 (279), 13: -34,262 (16), 15: -34,458 (43), 12: -37,278 (8), 10: -43,175 (5) |
| ROUTE_LEN | 11,980 | 3 | 3 | 3: -30,880 (6331), 2: -36,251 (513), 4: -36,902 (180), 5: -42,860 (8) |
| labor_reserve_buffer | 11,893 | 112 | 50 | 112: -26,296 (7), 71: -26,416 (11), 72: -26,442 (3), 5: -27,134 (14), 92: -27,642 (67), 26: -27,805 (3), 86: -28,304 (3), 35: -28,345 (3), 27: -28,672 (30), 9: -28,701 (6), 58: -28,702 (41), 49: -29,052 (30), 63: -29,256 (57), 96: -29,425 (4), 90: -29,751 (4), 18: -29,804 (342), 65: -29,861 (70), 61: -30,314 (72), 89: -30,327 (12), 33: -30,650 (16), 50: -30,706 (3433), 48: -30,747 (358), 56: -30,766 (5), 85: -30,825 (7), 115: -31,023 (5), 59: -31,138 (9), 144: -31,182 (2), 60: -31,205 (20), 36: -31,250 (36), 136: -31,282 (19), 73: -31,318 (9), 24: -31,352 (11), 93: -31,438 (4), 40: -31,469 (71), 42: -31,499 (444), 45: -31,575 (76), 80: -31,689 (8), 76: -31,767 (9), 51: -31,838 (9), 74: -31,856 (36), 25: -31,865 (4), 57: -31,907 (74), 44: -31,944 (12), 52: -32,111 (8), 66: -32,191 (39), 69: -32,258 (13), 14: -32,290 (5), 84: -32,305 (10), 39: -32,417 (47), 70: -32,434 (16), 150: -32,481 (25), 38: -32,519 (12), 28: -32,609 (14), 30: -32,622 (5), 104: -32,627 (3), 88: -32,733 (7), 78: -32,765 (5), 62: -32,845 (13), 43: -32,937 (14), 83: -32,957 (76), 4: -33,260 (34), 31: -33,290 (9), 119: -33,340 (2), 111: -33,417 (5), 0: -33,496 (118), 55: -33,573 (361), 6: -33,635 (9), 19: -33,712 (4), 94: -33,747 (11), 103: -33,915 (6), 34: -34,255 (29), 1: -34,413 (5), 21: -34,457 (4), 134: -34,464 (2), 91: -34,507 (4), 13: -34,564 (5), 54: -34,669 (10), 81: -34,736 (20), 99: -34,811 (60), 23: -34,865 (9), 79: -34,866 (6), 22: -35,000 (12), 7: -35,029 (4), 77: -35,080 (189), 29: -35,102 (8), 41: -35,128 (17), 47: -35,128 (12), 82: -35,190 (19), 32: -35,252 (7), 100: -35,307 (29), 53: -35,432 (14), 46: -35,483 (20), 129: -35,513 (65), 10: -35,579 (10), 87: -35,642 (6), 107: -35,804 (3), 68: -36,013 (7), 97: -36,084 (9), 106: -36,115 (2), 110: -36,353 (3), 3: -36,531 (5), 16: -36,603 (10), 109: -36,655 (2), 37: -36,792 (6), 101: -36,918 (8), 145: -36,990 (7), 11: -36,993 (11), 15: -37,056 (3), 98: -37,150 (4), 114: -37,370 (3), 64: -37,573 (11), 12: -37,835 (6), 67: -37,954 (14), 140: -38,186 (2), 102: -38,189 (3) |
| MELON_PRICE_CUSHION | 11,846 | 69 | 100 | 69: -29,694 (3), 130: -29,707 (9), 86: -29,752 (219), 85: -29,764 (63), 63: -30,037 (6), 65: -30,099 (5), 93: -30,159 (165), 92: -30,468 (9), 62: -30,527 (2), 100: -30,575 (4260), 125: -30,631 (66), 70: -30,641 (11), 67: -30,734 (4), 66: -30,750 (10), 115: -30,831 (16), 78: -30,838 (21), 94: -30,880 (9), 120: -30,949 (9), 81: -31,001 (26), 111: -31,177 (24), 141: -31,181 (2), 114: -31,463 (17), 132: -31,496 (4), 129: -31,539 (11), 64: -31,589 (8), 105: -31,779 (45), 82: -31,871 (12), 83: -31,904 (71), 147: -31,970 (4), 113: -31,983 (10), 133: -32,096 (5), 91: -32,097 (33), 149: -32,176 (3), 71: -32,246 (14), 68: -32,262 (5), 90: -32,299 (19), 76: -32,386 (10), 102: -32,413 (28), 99: -32,526 (18), 95: -32,538 (23), 122: -32,663 (27), 57: -32,707 (4), 109: -32,815 (14), 136: -32,828 (4), 123: -32,877 (13), 127: -32,929 (17), 97: -32,958 (39), 104: -33,007 (316), 74: -33,052 (18), 101: -33,160 (20), 103: -33,189 (17), 89: -33,299 (107), 112: -33,397 (168), 107: -33,446 (10), 88: -33,447 (44), 87: -33,480 (10), 79: -33,550 (15), 53: -33,612 (2), 135: -33,629 (357), 119: -33,644 (12), 116: -33,736 (32), 143: -33,776 (10), 96: -33,853 (28), 59: -33,898 (4), 121: -33,956 (8), 84: -33,986 (14), 108: -34,027 (16), 128: -34,043 (8), 98: -34,188 (18), 124: -34,377 (19), 110: -34,675 (14), 106: -34,764 (26), 117: -34,924 (32), 80: -34,941 (7), 137: -35,004 (2), 150: -35,058 (128), 75: -35,327 (45), 126: -35,580 (14), 134: -36,023 (6), 52: -36,201 (4), 77: -36,265 (11), 142: -36,268 (7), 148: -36,528 (3), 118: -37,023 (9), 51: -37,500 (2), 73: -37,519 (5), 72: -37,674 (7), 50: -37,691 (17), 131: -37,838 (9), 139: -38,005 (6), 140: -38,416 (3), 54: -39,448 (3), 60: -39,567 (5), 145: -40,643 (10), 58: -41,540 (2) |
| wheat_cap | 11,706 | 14 | 18 | 14: -28,132 (10), 21: -30,393 (1046), 22: -30,772 (3077), 20: -30,851 (428), 23: -31,147 (298), 17: -32,203 (497), 25: -32,609 (715), 12: -32,981 (6), 18: -33,111 (357), 16: -33,448 (49), 24: -33,681 (242), 9: -33,722 (39), 15: -34,244 (31), 19: -34,287 (96), 10: -34,594 (57), 5: -35,357 (21), 13: -35,733 (10), 11: -36,937 (29), 7: -37,056 (19), 6: -38,904 (2), 8: -39,838 (3) |
| wheat_sell_price | 10,682 | 25 | 30 | 25: -30,639 (3178), 30: -30,863 (2248), 26: -31,113 (221), 27: -32,772 (132), 29: -33,425 (66), 31: -33,508 (64), 28: -33,910 (723), 44: -34,154 (3), 35: -34,511 (151), 38: -35,249 (13), 50: -35,422 (3), 32: -35,590 (69), 34: -35,843 (33), 33: -36,210 (68), 39: -36,586 (8), 37: -36,820 (16), 40: -38,396 (8), 36: -38,982 (20), 46: -39,707 (2), 43: -41,320 (3) |
| MELON_MAX_TILES | 10,574 | 38 | 40 | 38: -29,513 (938), 34: -29,858 (105), 43: -30,292 (2128), 33: -30,517 (35), 37: -30,551 (167), 28: -30,859 (10), 49: -30,865 (173), 44: -31,329 (140), 46: -31,550 (48), 31: -31,670 (20), 45: -32,056 (216), 39: -32,183 (131), 25: -32,322 (3), 32: -32,403 (34), 30: -32,441 (14), 35: -32,595 (132), 40: -32,811 (2053), 47: -32,966 (90), 36: -33,092 (127), 42: -33,271 (139), 50: -33,320 (189), 41: -33,541 (46), 29: -33,925 (10), 48: -34,933 (32), 20: -35,056 (16), 24: -36,058 (20), 23: -36,659 (3), 27: -37,083 (3), 22: -39,119 (2), 26: -40,087 (8) |
| demand_share | 10,487 | 0.55 | 0.5 | 0.55: -29,678 (2774), 0.65: -31,572 (915), 0.75: -32,111 (42), 0.5: -32,135 (2450), 0.6: -32,434 (199), 0.7: -32,555 (108), 0.8: -34,111 (20), 0.9: -34,710 (7), 0.45: -34,918 (212), 0.4: -36,196 (92), 0.85: -36,289 (8), 0.35: -36,363 (93), 0.95: -37,587 (2), 1.0: -39,830 (5), 0.3: -40,165 (105) |
| MAX_HANDS | 10,288 | 14 | 13 | 14: -30,351 (562), 12: -31,355 (1278), 13: -31,424 (4342), 11: -31,577 (501), 15: -31,892 (163), 16: -34,103 (100), 10: -34,634 (62), 9: -37,780 (14), 8: -40,639 (10) |
| open_wheat | 9,920 | 7 | 7 | 7: -30,663 (6124), 5: -36,276 (40), 6: -36,369 (521), 10: -36,786 (71), 8: -36,859 (203), 9: -37,928 (48), 4: -39,171 (19), 3: -40,584 (6) |
| open_melons | 9,718 | 10 | 8 | 10: -30,534 (5606), 7: -33,134 (196), 9: -34,716 (330), 8: -34,986 (681), 6: -35,219 (98), 5: -36,987 (8), 12: -38,360 (28), 4: -38,404 (15), 11: -38,541 (35), 14: -39,129 (20), 13: -40,252 (15) |
| wheat_tiles | 9,607 | 0 | 0 | 0: -31,051 (6298), 1: -34,269 (395), 3: -35,062 (132), 2: -35,219 (150), 4: -35,785 (31), 5: -36,410 (14), 7: -36,854 (3), 6: -37,473 (6), 8: -40,658 (3) |
| open_sheep | 8,831 | 2 | 2 | 2: -31,158 (6721), 1: -36,977 (244), 3: -38,976 (28), 0: -39,989 (39) |
| setup_capital_share | 7,948 | 0.05 | 0.25 | 0.05: -29,824 (736), 0.2: -30,757 (417), 0.15: -31,038 (242), 0.25: -31,515 (4758), 0.1: -31,617 (226), 0.0: -31,879 (207), 0.4: -32,672 (83), 0.3: -33,185 (142), 0.35: -33,933 (147), 0.45: -34,178 (29), 0.5: -37,772 (45) |
| opening | 7,754 | frontier | frontier | frontier: -31,073 (6699), v312: -38,826 (333) |
| open_cows | 7,646 | 2 | 2 | 2: -31,041 (6594), 1: -37,375 (414), 3: -38,687 (24) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=1228)
- (10, 3, 6): -16,840 (n=1041)
- (8, 3, 5): -17,352 (n=173)
- (9, 3, 6): -17,681 (n=736)
- (12, 4, 6): -17,899 (n=296)
- (10, 4, 6): -17,975 (n=909)
- (11, 3, 6): -18,175 (n=255)
- (8, 3, 6): -18,250 (n=460)
- (11, 4, 6): -19,867 (n=327)
- (17, 3, 6): -20,338 (n=44)
- (8, 4, 6): -21,051 (n=366)
- (13, 4, 6): -21,868 (n=75)
- (10, 3, 5): -22,188 (n=26)
- (13, 3, 6): -22,519 (n=155)
- (9, 3, 5): -23,138 (n=84)

_Generated 2026-09-07 05:11. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._