# Evolution run 20260905-084336

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105739218.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.01 h · candidates evaluated this run: 1371 · games 30,808 (15,363/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 103 | 206 |
| dead_pattern | 357 | 714 |
| dead_smoke | 346 | 2768 |
| alive | 565 | 27120 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 1118 · held-out evaluated: 0 · held-out PASS: 0

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
| `8c1ad3488ef5` | queue | archive_crossover:crossover_g000650_20260905-093236_0 | -18,175 | -3.5 | 2-8 | -18,665 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→1, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→48, MAX_HANDS 13→11, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `f7948c8a5256` | queue | mutate | -19,867 | -4.8 | 1-9 | -24,035 | alive | melon_floor 150→0, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, fert_carry 3→2, demand_share 0.5→0.65, wheat_cap 18→17, wheat_sell_price 30→26, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5 |
| `d5c7f1c7464c` | v312 | migrate | -20,119 | -5.5 | 1-9 | -18,203 | alive | load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→1, demand_share 0.5→0.65, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→11, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, OPENING_MELONS 10→8, SPREAD_W 1.0→1.5 |
| `db7241c2664f` | queue | mutate | -20,121 | -4.3 | 1-9 | -25,275 | alive | harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_buy 0→1, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `d661997d96d0` | queue | mutate | -20,685 | -3.7 | 2-8 | -19,557 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→3, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→48, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `deabddbe036d` | queue | archive_crossover:crossover_g000925_20260905-095424_1 | -21,003 | -4.6 | 1-9 | -19,694 | alive | melon_floor 150→200, harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→1, demand_share 0.5→0.65, wheat_cap 18→20, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `ec2c3e0deb7c` | queue | archive_crossover:crossover_g001175_20260905-101823_1 | -21,164 | -5.3 | 1-9 | -18,988 | alive | load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→2, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `f33c14c80c3c` | queue | archive_crossover:crossover_g000175_20260905-085520_1 | -21,203 | -5.8 | 1-9 | -28,308 | alive | load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→2, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→22, wheat_sell_price 30→25, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→6, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, SPREAD_CAP 5→4 |
| `170a01ee902c` | queue | archive_crossover:crossover_g001125_20260905-081159_1 | -21,356 | -5.1 | 2-8 | -18,923 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, demand_share 0.5→0.65, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `27e9289c5a03` | c1 | migrate | -21,464 | -5.3 | 1-9 | -19,916 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→1, demand_share 0.5→0.65, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, OPENING_MELONS 10→9, SPREAD_W 1.0→1.5 |
| `e3919ba5726a` | queue | archive_crossover:crossover_g000325_20260905-090643_1 | -21,501 | -4.8 | 1-9 | -18,221 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→2, fert_carry 3→2, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `6b9b72ef5e9c` | queue | archive_crossover:crossover_g000625_20260905-093105_1 | -21,595 | -4.4 | 1-9 | -20,166 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→3, demand_share 0.5→0.65, wheat_cap 18→22, labor_reserve_buffer 50→48, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `f69ed515c1c6` | queue | archive_crossover:crossover_g000750_20260905-073920_1 | -21,646 | -4.6 | 0-10 | -23,057 | alive | load_per_hand 20→17, open_melons 8→10, demand_share 0.5→0.55, wheat_per_animal 0.0→0.1, wheat_cap 18→22, wheat_sell_price 30→25, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→6, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_CAP 5→4 |
| `89de98415ea0` | v312 | crossover | -21,695 | -5.0 | 1-9 | -33,866 | alive | melon_floor 150→0, harvest_min 2→1, load_per_hand 20→17, geese 0→1, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 4→6, MELON_MAX_TILES 40→36, MELON_PRICE_CUSHION 100→112, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, SPREAD_CAP 5→4 |
| `df62a383f60d` | v312 | crossover | -21,737 | -4.4 | 1-9 | -21,515 | alive | load_per_hand 20→17, open_melons 8→10, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→22, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→6, STRAW_CUTOFF 17→16, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, SPREAD_CAP 5→4 |

## Islands (best dev margin, population size)

- c1: best -21,464 (`27e9289c5a03`), n=268
- queue: best -18,175 (`8c1ad3488ef5`), n=380
- v312: best -20,119 (`d5c7f1c7464c`), n=302
- wide: best -24,044 (`44ffe249de02`), n=168

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| labor_reserve_buffer | 15,710 | 33 | 50 | 33: -27,319 (7), 39: -28,099 (3), 18: -29,484 (4), 48: -29,489 (34), 34: -29,897 (2), 58: -30,359 (6), 28: -30,872 (7), 0: -30,922 (17), 93: -31,438 (4), 6: -31,439 (3), 62: -31,802 (3), 45: -31,834 (3), 36: -31,854 (6), 94: -31,884 (5), 70: -32,348 (3), 44: -32,361 (5), 69: -32,452 (7), 42: -32,514 (172), 38: -32,949 (2), 84: -32,988 (2), 50: -33,053 (394), 4: -33,084 (29), 100: -33,935 (11), 67: -34,015 (2), 13: -34,125 (3), 73: -34,175 (3), 99: -34,244 (36), 77: -34,397 (108), 24: -34,399 (2), 27: -34,688 (2), 40: -34,858 (7), 29: -34,858 (2), 110: -34,863 (2), 83: -34,918 (12), 43: -34,954 (3), 60: -34,989 (3), 46: -35,029 (8), 64: -35,125 (3), 82: -35,262 (6), 81: -35,646 (15), 97: -35,647 (3), 129: -35,814 (16), 21: -35,947 (2), 16: -36,453 (5), 49: -36,602 (2), 55: -36,864 (75), 47: -37,471 (7), 145: -37,752 (3), 11: -37,769 (7), 101: -37,913 (6), 32: -37,968 (2), 12: -38,212 (2), 65: -38,221 (5), 87: -38,817 (3), 150: -40,675 (6), 66: -43,029 (2) |
| MELON_PRICE_CUSHION | 14,178 | 74 | 100 | 74: -26,022 (3), 99: -29,098 (2), 76: -29,918 (2), 66: -29,961 (6), 105: -30,665 (4), 111: -30,794 (7), 71: -32,119 (7), 130: -32,409 (4), 100: -32,666 (569), 97: -32,996 (10), 112: -33,213 (49), 102: -33,259 (11), 129: -33,467 (5), 89: -33,803 (59), 88: -33,971 (24), 95: -34,572 (11), 150: -34,752 (10), 104: -34,808 (131), 75: -34,826 (21), 91: -35,128 (9), 116: -35,198 (2), 103: -35,306 (2), 115: -35,488 (3), 78: -35,528 (2), 109: -35,844 (4), 135: -35,963 (60), 125: -35,984 (4), 128: -35,986 (2), 83: -36,341 (5), 124: -36,374 (9), 96: -36,733 (8), 90: -36,910 (4), 98: -36,947 (5), 110: -37,011 (5), 106: -37,579 (4), 108: -37,596 (4), 50: -37,876 (2), 72: -38,136 (5), 73: -38,377 (3), 77: -38,504 (3), 87: -39,175 (2), 54: -39,448 (3), 134: -40,200 (2) |
| wheat_stock | 13,739 | 6 | 0 | 6: -29,931 (3), 9: -30,298 (28), 1: -33,495 (54), 0: -33,548 (963), 10: -34,165 (7), 8: -34,259 (2), 7: -34,867 (9), 5: -35,228 (11), 23: -35,381 (3), 3: -35,651 (10), 13: -36,362 (4), 11: -36,519 (2), 2: -37,387 (7), 20: -38,043 (3), 15: -38,369 (4), 40: -43,670 (3) |
| MELON_MAX_TILES | 12,345 | 49 | 40 | 49: -30,411 (6), 43: -30,564 (140), 38: -31,657 (6), 41: -32,656 (12), 46: -32,763 (3), 47: -33,232 (33), 40: -33,831 (720), 24: -34,142 (11), 35: -34,147 (28), 32: -34,148 (4), 36: -34,297 (22), 30: -34,335 (3), 39: -34,918 (21), 34: -34,955 (11), 50: -35,108 (28), 37: -35,799 (4), 33: -35,846 (3), 45: -35,863 (32), 44: -36,226 (13), 48: -37,667 (4), 42: -38,921 (8), 20: -42,755 (2) |
| load_per_hand | 12,045 | 19 | 20 | 19: -31,874 (425), 17: -33,473 (181), 18: -33,519 (32), 20: -34,706 (346), 21: -34,771 (58), 24: -36,304 (2), 23: -36,958 (15), 15: -37,211 (11), 16: -37,458 (12), 22: -37,488 (15), 25: -37,987 (4), 14: -38,736 (4), 26: -40,255 (6), 13: -40,334 (3), 12: -43,919 (4) |
| wheat_sell_price | 11,631 | 26 | 30 | 26: -29,871 (25), 25: -32,655 (365), 30: -33,167 (347), 27: -33,273 (12), 38: -33,351 (5), 29: -33,739 (11), 35: -34,181 (98), 31: -34,201 (21), 37: -34,576 (6), 39: -35,424 (3), 28: -35,600 (170), 32: -36,262 (13), 33: -36,497 (28), 34: -38,652 (5), 36: -41,502 (6) |
| MAX_HANDS | 10,404 | 12 | 13 | 12: -31,668 (216), 11: -33,736 (57), 13: -33,861 (773), 14: -35,450 (21), 10: -35,959 (14), 15: -36,202 (16), 8: -38,636 (2), 16: -39,030 (15), 9: -42,072 (4) |
| open_melons | 9,714 | 10 | 8 | 10: -32,321 (535), 9: -33,479 (115), 8: -34,827 (394), 6: -35,259 (19), 7: -35,743 (31), 14: -37,141 (3), 11: -39,017 (8), 4: -40,112 (5), 12: -40,830 (5), 13: -42,035 (3) |
| demand_share | 8,370 | 0.55 | 0.5 | 0.55: -32,181 (207), 0.65: -32,244 (121), 0.5: -33,655 (635), 0.6: -33,984 (35), 0.75: -35,421 (4), 0.7: -36,233 (10), 0.45: -36,304 (42), 0.4: -37,035 (8), 0.35: -37,897 (43), 0.3: -40,552 (10) |
| early_hire_days | 8,119 | 4 | 5 | 4: -32,278 (272), 7: -32,746 (57), 5: -33,511 (557), 2: -34,726 (22), 3: -34,804 (54), 6: -34,851 (50), 8: -36,356 (86), 0: -37,963 (15), 1: -40,397 (5) |
| STRAW_CUTOFF | 7,809 | 16 | 17 | 16: -32,187 (142), 17: -33,563 (795), 18: -33,905 (103), 14: -34,111 (10), 19: -34,850 (20), 20: -37,240 (27), 15: -37,909 (14), 12: -39,996 (6) |
| wheat_per_animal | 7,556 | 0.1 | 0.0 | 0.1: -32,548 (224), 0.0: -33,554 (634), 0.2: -33,901 (198), 0.6: -34,359 (3), 0.7: -36,636 (6), 0.5: -36,859 (2), 1.0: -37,087 (13), 0.3: -37,148 (19), 0.4: -38,661 (13), 1.2: -40,105 (3) |
| CROP_SWEEP_LEN | 6,717 | 6 | 6 | 6: -33,052 (879), 7: -34,806 (129), 5: -35,035 (39), 3: -37,056 (27), 4: -37,633 (28), 8: -39,248 (10), 9: -39,769 (5) |
| opening | 6,670 | frontier | frontier | frontier: -33,252 (1055), v312: -39,922 (63) |
| max_animals | 6,514 | 18 | 20 | 18: -33,019 (57), 13: -33,221 (3), 20: -33,546 (833), 17: -33,777 (168), 19: -34,110 (23), 16: -34,297 (16), 14: -34,446 (3), 15: -35,931 (10), 12: -39,533 (4) |
| setup_capital_share | 6,336 | 0.25 | 0.25 | 0.25: -33,133 (927), 0.35: -35,046 (41), 0.2: -35,186 (33), 0.1: -35,472 (12), 0.15: -35,669 (18), 0.0: -35,849 (22), 0.45: -36,265 (4), 0.4: -36,311 (20), 0.3: -36,399 (21), 0.5: -39,469 (19) |
| wheat_tiles | 6,325 | 0 | 0 | 0: -33,352 (955), 1: -33,689 (84), 2: -36,113 (34), 6: -36,181 (4), 3: -37,286 (32), 5: -37,371 (4), 4: -39,677 (4) |
| open_sheep | 6,102 | 2 | 2 | 2: -33,340 (1035), 1: -36,713 (63), 3: -38,434 (13), 0: -39,442 (7) |
| open_wheat | 6,091 | 7 | 7 | 7: -33,181 (935), 6: -34,887 (104), 8: -36,642 (35), 10: -36,758 (17), 5: -36,970 (9), 9: -38,959 (11), 4: -39,272 (7) |
| open_cows | 5,967 | 2 | 2 | 2: -33,080 (974), 1: -37,271 (139), 3: -39,047 (5) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (11, 3, 6): -18,175 (n=34)
- (11, 4, 6): -19,867 (n=47)
- (8, 3, 6): -20,121 (n=96)
- (10, 3, 6): -20,685 (n=129)
- (10, 4, 6): -21,203 (n=129)
- (12, 4, 6): -21,695 (n=94)
- (8, 3, 5): -22,477 (n=45)
- (13, 3, 6): -22,724 (n=38)
- (9, 3, 6): -22,897 (n=115)
- (14, 3, 6): -23,164 (n=12)
- (8, 3, 4): -23,525 (n=19)
- (8, 4, 6): -23,823 (n=60)
- (8, 4, 5): -23,880 (n=9)
- (9, 4, 6): -24,181 (n=123)
- (11, 3, 5): -25,148 (n=3)

_Generated 2026-09-05 10:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._