# Evolution run 20260915-132851

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_majkel1337_109144271.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 0.03 h · candidates evaluated this run: 1 · games 610 (17,543/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 1 | 2 |
| dead_smoke | 0 | 0 |
| alive | 1 | 608 |
| held_fail | 0 | 0 |
| held_exploit | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 1416 · held-out evaluated: 908 · held-out PASS: 894

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | +6,918 | 6.2 | 28-2 | -5,975 | +9,000 | 6.3 | 18-2 |
| chassis + C1 params (seed row) | +6,918 | 6.2 | 28-2 | -5,975 | +9,000 | 6.3 | 18-2 |
| C1.py (file) vs O15_SALE_PRIORITY.py | -21,945 | -16.8 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O15_SALE_PRIORITY.py | -25,061 | -10.2 | 0-10 | — | — | — | — |
| O15_SALE_PRIORITY.py own panel (dev / held) | — | — | — | -18,329 / -22,947 | — | — | — |

Measurement mode: `KAGG_FIXED_SHOPS=1` (shop unlocks policy-independent; panel margins comparable at ±$3k/opponent).

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `753a5a1fa946` | wide | block_pair | **+16,010** | 14.5 | 20-0 | -11,867 | +14,255 | open_melons 10→9, early_hire_days 3→8, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 · blocks: crop_admission |  | cand falls behind C1 from day 24 (gap -3,414 -> final -4,730); days 22-29 drivers: sales_rev -4,397, missed_water +14, water_hour +1.82, idle_turns +8. Hands 4 vs 5, animals 11 vs 11, plants 2 vs 5. |
| `77232db80dbf` | queue | mutate | **+15,594** | 9.2 | 19-1 | -11,953 | +12,763 | open_melons 10→9, early_hire_days 3→8, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→32, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand falls behind C1 from day 24 (gap -2,303 -> final -2,788); days 22-29 drivers: sales_rev -3,333, water_hour +1.31, idle_turns +2. Hands 5 vs 5, animals 11 vs 11, plants 4 vs 5. |
| `cf560462215d` | best | mutate | **+15,551** | 12.0 | 20-0 | -12,547 | +13,236 | load_per_hand 20→19, open_melons 10→11, early_hire_days 3→8, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 | load_per_hand +1,539, open_melons -133, max_animals ? | cand falls behind C1 from day 29 (gap -2,339 -> final -2,339); days 27-29 drivers: sales_rev -2,191, water_hour +2.27, work_turns -19, idle_turns +3. Hands 5 vs 5, animals 11 vs 11, plants 2 vs 5. |
| `e871e09038ac` | o15 | ablate:ROUTE_LEN | **+15,421** | 11.8 | 20-0 | -11,275 | +11,817 | open_melons 10→9, early_hire_days 3→8, demand_share 0.55→0.5, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→3, NEAR_RADIUS 2→5, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→4, SPREAD_CAP 3→5, MELON_MORNING 1→0 |  | cand vs C1: net worth never diverged by >$1,500 (final +1,341). |
| `7d9b2ebc2744` | best | paired | **+15,383** | 11.9 | 20-0 | -13,242 | +12,077 | wheat_tiles 0→1, wheat_stock 0→5, min_hands 3→4, load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 | min_hands -59, wheat_hold_days +176 | cand falls behind C1 from day 25 (gap -5,452 -> final -4,741); days 23-29 drivers: sales_rev -3,965, missed_water +14, idle_turns +70, water_hour +0.06. Hands 5 vs 5, animals 11 vs 11, plants 2 vs 5. |
| `d681ae3c4473` | wide | paired | **+15,377** | 10.5 | 19-1 | -12,296 | +13,310 | load_per_hand 20→21, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→14, wheat_sell_price 30→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→120, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, OPENING_MELONS 14→12, FERT_RADIUS 3→1, SPREAD_CAP 3→7, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand vs C1: net worth never diverged by >$1,500 (final -860). |
| `66af76e4dec9` | queue | crossover | **+15,360** | 12.3 | 20-0 | -12,273 | +12,781 | load_per_hand 20→19, early_hire_days 3→8, wheat_cap 22→20, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand falls behind C1 from day 24 (gap -1,786 -> final -3,011); days 22-29 drivers: sales_rev -6,414, weeds_new +2, water_hour +1.85, work_turns -24. Hands 4 vs 5, animals 11 vs 11, plants 0 vs 5. |
| `950f0e30eba0` | queue | migrate | **+15,346** | 11.3 | 19-1 | -12,794 | +13,185 | load_per_hand 20→21, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→14, wheat_sell_price 30→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→120, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→7, HIRE_MAX_MARGINAL 144→377, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand vs C1: net worth never diverged by >$1,500 (final -860). |
| `fb6f7ec05cd2` | o15 | crossover | **+15,327** | 12.3 | 20-0 | -11,795 | +12,660 | wheat_tiles 0→1, wheat_stock 0→3, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, demand_share 0.55→0.5, max_animals 17→16, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→7, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand pulls ahead of C1 from day 28 (gap +2,134 -> final +1,278); days 26-29 drivers: idle_turns -40, sales_rev +1,382, feed_hour -1.07, weeds_new -1. Hands 6 vs 5, animals 10 vs 11, plants 8 vs 5. |
| `995eb0a74a68` | queue | migrate | **+15,291** | 10.9 | 20-0 | -11,396 | +12,988 | min_hands 3→4, open_melons 10→9, early_hire_days 3→8, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→6, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 | min_hands -476, wheat_water_tier +655, SPREAD_CAP ? | cand vs C1: net worth never diverged by >$1,500 (final +106). |
| `a7860f3574fb` | best | ablate:load_per_hand | **+15,268** | 12.7 | 20-0 | -11,937 | +11,697 | open_melons 10→11, early_hire_days 3→8, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand falls behind C1 from day 25 (gap -1,576 -> final -2,629); days 23-29 drivers: sales_rev -3,853, missed_water +16, water_hour +0.9, travel_per_task +0.16. Hands 6 vs 5, animals 11 vs 11, plants 8  |
| `86b5465bf1d4` | wide | ablate:wheat_stock | **+15,242** | 10.9 | 20-0 | -11,668 | +13,638 | wheat_stock 0→1, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→21, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_W 1.25→1.5, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand pulls ahead of C1 from day 28 (gap +1,900 -> final +1,675); days 26-29 drivers: feed_hour -3.03, sales_rev +1,036, weeds_new -1, missed_feed -2. Hands 4 vs 5, animals 9 vs 11, plants 3 vs 5. |
| `544b6e598abf` | wide | block_pair | **+15,238** | 10.5 | 20-0 | -11,041 | +11,871 | open_melons 10→9, open_wheat 7→9, early_hire_days 3→8, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_W 1.25→1.5, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 · blocks: crop_admission |  | cand pulls ahead of C1 from day 22 (gap +2,564 -> final +1,587); days 20-27 drivers: feed_hour -2.14, work_turns +21, travel_per_task -0.05. Hands 10 vs 11, animals 11 vs 11, plants 37 vs 42. |
| `b59a939bdf4e` | wide | mutate | **+15,160** | 12.9 | 20-0 | -11,089 | +14,713 | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand falls behind C1 from day 25 (gap -1,601 -> final -1,957); days 23-29 drivers: sales_rev -4,331, weeds_new +2, missed_water +4, water_hour +1.27. Hands 5 vs 5, animals 11 vs 11, plants 4 vs 5. |
| `f2151cac53a6` | o15 | crossover | **+15,099** | 10.8 | 19-1 | -11,239 | +12,440 | load_per_hand 20→21, open_melons 10→9, early_hire_days 3→8, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→11, FERT_RADIUS 3→2, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |  | cand vs C1: net worth never diverged by >$1,500 (final -957). |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `51435ac9641b` | best | mutate | +15,151 | 12.3 | 28-2 | -7,126 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `14fb3191638a` | best | crossover | +14,868 | 12.7 | 29-1 | -7,015 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `9c02b45cd0fe` | best | crossover | +14,752 | 12.0 | 29-1 | -7,621 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→112, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `b59a939bdf4e` | wide | mutate | +14,713 | 11.9 | 28-2 | -5,853 | held_pass | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `a75ac7f5628a` | o15 | crossover | +14,660 | 10.8 | 29-1 | -7,428 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→11, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→5, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→10, MELON_MORNING_MIN_YIELD 6→5 |
| `4dc9d21748ef` | best | crossover | +14,625 | 12.5 | 29-1 | -7,671 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→112, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `deb55b1eec45` | o15 | crossover | +14,581 | 12.2 | 29-1 | -6,986 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→23, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→2, MELON_PRICE_CUSHION 100→80, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `208c590bda29` | wide | migrate | +14,570 | 12.3 | 29-1 | -7,538 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, wheat_cap 22→11, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.5, OPENING_MELONS 14→11, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→7, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `d8cab6910941` | best | mutate | +14,569 | 11.7 | 28-2 | -7,500 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→112, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `d53096d20341` | wide | crossover | +14,554 | 11.5 | 28-2 | -7,479 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_CAP 3→5, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `dc4fde844a9b` | best | crossover | +14,507 | 12.1 | 28-2 | -8,004 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.5, OPENING_MELONS 14→11, FERT_RADIUS 3→2, SPREAD_CAP 3→6, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `5716cad50618` | queue | archive_crossover:crossover_g000025_20260914-161809_1 | +14,471 | 10.8 | 29-1 | -6,951 | held_pass | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→11, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→7, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `0c4c57de0130` | best | mutate | +14,438 | 11.8 | 28-2 | -7,483 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→120, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→12, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_W 1.25→1.0, SPREAD_CAP 3→4, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `f2847e53c866` | best | migrate | +14,403 | 11.8 | 28-2 | -5,753 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `378d4ddae49e` | best | mutate | +14,359 | 11.9 | 29-1 | -6,154 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +15,151 (`51435ac9641b`), n=496
- o15: best +14,660 (`a75ac7f5628a`), n=301
- queue: best +14,471 (`5716cad50618`), n=279
- wide: best +14,713 (`b59a939bdf4e`), n=340

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| ROUTE_LEN | +17,554 | 2 | 3 | 4 | 1416 | 1.77 | 2: +9,306 (n=981), 3: +5,292 (n=412), 4: +591 (n=20), 5: -8,248 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +15,762 | 16 | 14 | 8 | 1416 | 1.83 | 16: +9,357 (n=501), 15: +8,653 (n=436), 13: +7,565 (n=41), 12: +7,140 (n=23), 14: +5,796 (n=405), 11: +4,653 (n=6), 10: -616 (n=2), 8: -6,404 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +13,649 | 80 | 100 | 61 | 1398 | 23.36 | 80: +12,758 (n=3), 53: +12,736 (n=3), 73: +12,491 (n=2), 50: +11,920 (n=3), 119: +11,101 (n=7), 60: +10,957 (n=3), 86: +10,542 (n=8), 117: +10,236 (n=5), 127: +10,230 (n=13), 146: +10,158 (n=2), 54: +10,157 (n=2), 133: +10,154 (n=2), 63: +9,835 (n=2), 82: +9,771 (n=188), 101: +9,491 (n=15), 112: +9,447 (n=20), 103: +9,395 (n=3), 96: +8,485 (n=3), 120: +8,159 (n=20), 68: +8,143 (n=29), 99: +8,109 (n=10), 100: +8,000 (n=792), 94: +7,681 (n=5), 111: +7,630 (n=11), 106: +7,433 (n=8), 148: +6,535 (n=2), 107: +6,400 (n=117), 114: +6,129 (n=2), 131: +6,008 (n=4), 116: +5,946 (n=66), 84: +5,799 (n=4), 128: +5,640 (n=11), 92: +4,657 (n=3), 93: +4,132 (n=5), 143: +3,933 (n=3), 136: +3,537 (n=3), 87: +3,081 (n=2), 90: +2,614 (n=2), 150: +2,409 (n=3), 85: +1,681 (n=2), 134: +1,663 (n=6), 77: +1,272 (n=2), 118: -891 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,201 | 3 | 0 | 24 | 1408 | 10.17 | 3: +9,705 (n=11), 13: +9,459 (n=4), 5: +9,034 (n=48), 4: +8,779 (n=7), 9: +8,563 (n=8), 2: +8,548 (n=5), 0: +8,336 (n=983), 17: +7,175 (n=5), 7: +7,048 (n=7), 1: +6,942 (n=303), 10: +6,648 (n=14), 6: +5,817 (n=2), 8: +5,801 (n=4), 12: +4,114 (n=3), 11: +3,818 (n=2), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,937 | 16 | 17 | 11 | 1415 | 5.4 | 16: +9,877 (n=275), 15: +9,627 (n=114), 14: +7,963 (n=19), 17: +7,674 (n=906), 19: +6,601 (n=10), 13: +5,522 (n=3), 18: +3,994 (n=58), 20: +2,930 (n=22), 10: +50 (n=2), 12: -1,060 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,867 | 7 | 10 | 11 | 1416 | 7.36 | 7: +10,175 (n=16), 11: +8,835 (n=45), 6: +8,358 (n=63), 10: +8,116 (n=69), 9: +8,109 (n=1076), 8: +7,215 (n=95), 12: +6,812 (n=13), 5: +6,249 (n=8), 4: +4,075 (n=24), 13: +3,083 (n=2), 14: -692 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +9,950 | 17 | 22 | 18 | 1413 | 5.85 | 17: +10,266 (n=9), 23: +10,001 (n=7), 24: +9,831 (n=3), 14: +9,813 (n=38), 20: +9,634 (n=390), 11: +8,275 (n=14), 21: +7,527 (n=645), 13: +7,078 (n=3), 25: +7,000 (n=52), 22: +6,975 (n=168), 16: +6,678 (n=2), 5: +6,304 (n=6), 19: +6,298 (n=5), 18: +5,768 (n=61), 15: +315 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,297 | 21 | 20 | 15 | 1415 | 6.95 | 21: +10,113 (n=40), 19: +9,596 (n=311), 20: +7,904 (n=804), 16: +7,835 (n=23), 17: +7,341 (n=84), 18: +7,305 (n=50), 14: +6,219 (n=10), 22: +6,216 (n=17), 23: +4,591 (n=10), 24: +4,275 (n=5), 13: +3,027 (n=3), 15: +2,450 (n=49), 12: +2,307 (n=7), 26: +816 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +9,260 | frontier | frontier | 2 | 1416 | 0.79 | frontier: +8,952 (n=1267), v312: -308 (n=149) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,188 | 0.0 | 0.0 | 9 | 1415 | 6.5 | 0.0: +8,147 (n=1326), 0.3: +6,266 (n=14), 0.2: +6,177 (n=39), 0.1: +5,647 (n=16), 0.4: +4,505 (n=7), 0.5: +4,380 (n=7), 0.6: +4,309 (n=4), 0.7: -1,041 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +8,990 | 0.55 | 0.55 | 14 | 1416 | 9.87 | 0.55: +8,439 (n=1099), 0.45: +7,910 (n=25), 0.6: +7,674 (n=31), 0.4: +7,626 (n=10), 0.5: +7,421 (n=117), 0.75: +6,821 (n=10), 0.85: +6,621 (n=3), 0.65: +6,610 (n=24), 0.35: +6,190 (n=9), 0.7: +4,081 (n=41), 0.3: +3,869 (n=21), 0.8: +3,825 (n=21), 0.9: +3,786 (n=3), 1.0: -551 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,898 | 2 | 2 | 4 | 1416 | 2.74 | 2: +8,183 (n=1325), 1: +5,939 (n=65), 0: +4,393 (n=17), 3: -715 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +8,760 | 9 | 8 | 9 | 1416 | 3.58 | 9: +9,351 (n=721), 10: +8,935 (n=32), 5: +8,778 (n=6), 11: +7,060 (n=19), 8: +6,915 (n=526), 7: +6,481 (n=13), 4: +5,038 (n=23), 12: +3,400 (n=71), 6: +591 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +8,511 | 37 | 30 | 21 | 1412 | 6.16 | 37: +10,903 (n=2), 33: +10,746 (n=3), 31: +9,321 (n=8), 29: +9,047 (n=595), 38: +8,824 (n=4), 25: +8,510 (n=337), 28: +8,363 (n=13), 26: +8,029 (n=102), 32: +7,785 (n=7), 27: +7,468 (n=13), 34: +7,024 (n=15), 36: +6,988 (n=6), 42: +6,603 (n=18), 30: +5,363 (n=267), 35: +4,935 (n=13), 43: +3,122 (n=6), 40: +2,392 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +7,884 | 1.1 | 1.4 | 9 | 1416 | 2.04 | 1.1: +9,788 (n=467), 1.5: +8,601 (n=151), 1.2: +7,774 (n=104), 1.3: +6,942 (n=479), 1.4: +6,571 (n=140), 1.8: +6,218 (n=10), 1.0: +6,031 (n=35), 1.6: +5,768 (n=11), 1.7: +1,904 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,583 | 13 | 14 | 10 | 1413 | 3.86 | 13: +9,488 (n=363), 14: +7,717 (n=981), 12: +6,965 (n=17), 11: +6,378 (n=6), 8: +6,166 (n=3), 9: +3,489 (n=21), 10: +1,905 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +7,169 | 8 | 14 | 8 | 1415 | 3.25 | 8: +11,498 (n=4), 10: +10,090 (n=5), 11: +9,736 (n=152), 13: +9,399 (n=357), 12: +8,354 (n=32), 14: +7,069 (n=860), 9: +4,329 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +6,710 | 16 | 19 | 8 | 1415 | 4.7 | 16: +9,380 (n=58), 19: +8,018 (n=1152), 17: +7,731 (n=20), 20: +7,413 (n=160), 18: +7,265 (n=20), 14: +5,891 (n=2), 15: +2,670 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HIRE_MAX_MARGINAL | +5,643 | 233 | 144 | 6 | 1416 | 3.28 | 233: +9,107 (n=247), 1000000000: +8,188 (n=31), 144: +7,905 (n=1010), 89: +7,135 (n=63), 377: +6,670 (n=42), 55: +3,464 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +5,243 | 8 | 6 | 8 | 1416 | 3.58 | 8: +8,799 (n=811), 5: +7,813 (n=27), 7: +7,499 (n=68), 10: +7,320 (n=53), 6: +6,934 (n=345), 9: +6,710 (n=56), 3: +5,512 (n=43), 4: +3,557 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +15,151 (n=56)
- (9, 3, 4): +14,868 (n=132)
- (11, 3, 5): +14,752 (n=311)
- (11, 3, 4): +14,581 (n=179)
- (10, 3, 4): +14,305 (n=165)
- (11, 3, 6): +14,264 (n=133)
- (10, 3, 5): +14,155 (n=171)
- (13, 3, 5): +13,609 (n=8)
- (12, 3, 6): +13,558 (n=20)
- (10, 3, 6): +13,508 (n=43)
- (9, 3, 3): +13,310 (n=12)
- (9, 2, 3): +13,292 (n=18)
- (9, 3, 6): +13,258 (n=5)
- (8, 3, 4): +12,621 (n=8)
- (12, 3, 4): +12,339 (n=2)

## Remaining-horizon ROI (AGE-360)

`candidates/O17_ORCH_CAPITAL.py` | mode `cutoff+marginal` | 64 cells (4 tapes x 16 seeds) | fixed_shops=True | generated 2026-09-11T02:29:18

ROI = base final money - counterfactual final money, net of acquisition, operating and opportunity cost. **Read the intervention column before the number.** `class blocked` prices the whole subsystem and, for a class the policy replenishes continuously (labour, feed), is near-total ablation -- it does NOT estimate the value of the last unit. `-K unit/day` is the marginal experiment. The two can have opposite signs, and on this chassis HIRE does.

| investment | intervention | from day | n | ROI | t | 95% CI | cells + | payback |
|---|---|---:|---:|---:|---:|---|---:|---|
| BUY_ANIMAL | class blocked | 2 | 12 | +6,734 | 2.94 | [+2,243, +11,226] | 83% | 83% by day 15 |
| BUY_ANIMAL | class blocked | 4 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 5 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 6 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 7 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 8 | 24 | +3,350 | 1.01 | [-3,132, +9,831] | 29% | 29% by day 17 |
| BUY_ANIMAL | class blocked | 9 | 24 | -208 | -0.15 | [-2,983, +2,566] | 25% | 25% by day 23 |
| BUY_ANIMAL | class blocked | 10 | 12 | -1,008 | -2.03 | [-1,980, -36] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 2 | 12 | +3,019 | 1.93 | [-50, +6,088] | 75% | 75% by day 29 |
| BUY_ANIMAL:COW | class blocked | 6 | 12 | -1,042 | -1.00 | [-3,086, +1,003] | 50% | 50% by day 29 |
| BUY_ANIMAL:COW | class blocked | 10 | 12 | -917 | -1.82 | [-1,902, +69] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 2 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 6 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 10 | 12 | +2,218 | 2.24 | [+277, +4,159] | 33% | 33% by day 28 |
| BUY_LAND | class blocked | 14 | 12 | -302 | -1.00 | [-893, +290] | 0% | 0% never |
| BUY_LAND | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_PRODUCT | class blocked | 2 | 12 | +35,501 | 5.90 | [+23,717, +47,285] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 6 | 12 | +38,533 | 5.34 | [+24,396, +52,670] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 10 | 32 | +38,821 | 5.92 | [+25,960, +51,681] | 97% | 97% by day 13 |
| BUY_PRODUCT | class blocked | 14 | 32 | +22,151 | 4.29 | [+12,032, +32,269] | 78% | 78% by day 19 |
| BUY_PRODUCT | class blocked | 18 | 32 | +13,697 | 3.84 | [+6,709, +20,685] | 62% | 62% by day 22 |
| BUY_PRODUCT | class blocked | 22 | 32 | +10,598 | 4.44 | [+5,916, +15,279] | 81% | 81% by day 25 |
| BUY_PRODUCT | class blocked | 26 | 32 | +4,647 | 5.85 | [+3,090, +6,205] | 94% | 94% by day 29 |
| BUY_PRODUCT:FERTILIZER | class blocked | 16 | 32 | +105 | 0.40 | [-409, +620] | 38% | 38% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 18 | 32 | +332 | 1.20 | [-209, +873] | 53% | 53% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 20 | 32 | +274 | 1.06 | [-231, +779] | 47% | 47% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 22 | 32 | +201 | 1.42 | [-76, +479] | 44% | 44% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 24 | 32 | +156 | 1.20 | [-99, +411] | 25% | 25% by day 26 |
| BUY_PRODUCT:WHEAT | class blocked | 16 | 32 | +17,487 | 4.10 | [+9,124, +25,850] | 66% | 66% by day 20 |
| BUY_PRODUCT:WHEAT | class blocked | 18 | 32 | +13,145 | 3.91 | [+6,548, +19,742] | 59% | 59% by day 22 |
| BUY_PRODUCT:WHEAT | class blocked | 20 | 32 | +10,597 | 3.75 | [+5,059, +16,135] | 59% | 59% by day 24 |
| BUY_PRODUCT:WHEAT | class blocked | 22 | 32 | +9,922 | 4.13 | [+5,212, +14,632] | 72% | 72% by day 25 |
| BUY_PRODUCT:WHEAT | class blocked | 24 | 32 | +6,874 | 4.74 | [+4,033, +9,715] | 91% | 91% by day 27 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 8 | 32 | +1,300 | 1.88 | [-57, +2,658] | 53% | 53% by day 26 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 12 | 32 | +246 | 0.71 | [-430, +923] | 44% | 44% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 16 | 32 | +262 | 1.49 | [-82, +606] | 53% | 53% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 20 | 32 | +335 | 2.09 | [+20, +649] | 53% | 53% by day 28 |
| BUY_SEED | class blocked | 2 | 12 | +32,017 | 6.75 | [+22,721, +41,312] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 6 | 12 | +27,234 | 5.80 | [+18,025, +36,443] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 10 | 32 | +17,307 | 7.33 | [+12,677, +21,936] | 94% | 94% by day 22 |
| BUY_SEED | class blocked | 14 | 32 | +6,720 | 7.51 | [+4,966, +8,474] | 97% | 97% by day 24 |
| BUY_SEED | class blocked | 18 | 32 | +3,991 | 6.01 | [+2,689, +5,293] | 94% | 94% by day 26 |
| BUY_SEED | class blocked | 22 | 32 | +2,252 | 6.07 | [+1,525, +2,979] | 91% | 91% by day 29 |
| BUY_SEED | class blocked | 26 | 32 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED | -1 unit/day | 8 | 32 | +870 | 1.63 | [-179, +1,920] | 84% | 84% by day 26 |
| BUY_SEED | -1 unit/day | 12 | 32 | +825 | 3.29 | [+334, +1,316] | 91% | 91% by day 27 |
| BUY_SEED | -1 unit/day | 16 | 32 | +710 | 3.68 | [+331, +1,088] | 91% | 91% by day 28 |
| BUY_SEED | -1 unit/day | 20 | 32 | +444 | 4.11 | [+232, +656] | 84% | 84% by day 28 |
| BUY_SEED | -1 unit/day | 24 | 32 | +216 | 2.92 | [+71, +360] | 75% | 75% by day 29 |
| BUY_SEED:MELON | class blocked | 2 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 6 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 10 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 14 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 2 | 12 | +19,487 | 4.50 | [+10,992, +27,982] | 100% | 100% by day 21 |
| BUY_SEED:STRAWBERRY | class blocked | 6 | 12 | +12,168 | 2.35 | [+2,002, +22,334] | 67% | 67% by day 23 |
| BUY_SEED:STRAWBERRY | class blocked | 10 | 12 | +2,506 | 0.54 | [-6,564, +11,575] | 33% | 33% by day 25 |
| BUY_SEED:STRAWBERRY | class blocked | 14 | 12 | +1,510 | 2.08 | [+87, +2,933] | 58% | 58% by day 28 |
| BUY_SEED:STRAWBERRY | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| HIRE | class blocked | 2 | 12 | +60,467 | 8.28 | [+46,154, +74,780] | 100% | 100% by day 12 |
| HIRE | class blocked | 6 | 12 | +67,166 | 9.32 | [+53,044, +81,289] | 100% | 100% by day 11 |
| HIRE | class blocked | 10 | 12 | +65,554 | 9.34 | [+51,794, +79,315] | 100% | 100% by day 11 |
| HIRE | class blocked | 14 | 32 | +58,984 | 8.97 | [+46,102, +71,867] | 100% | 100% by day 15 |
| HIRE | class blocked | 18 | 32 | +44,291 | 9.10 | [+34,746, +53,835] | 100% | 100% by day 19 |
| HIRE | class blocked | 22 | 32 | +27,209 | 7.39 | [+19,990, +34,427] | 100% | 100% by day 23 |
| HIRE | class blocked | 26 | 32 | +12,805 | 9.78 | [+10,238, +15,371] | 100% | 100% by day 27 |
| HIRE | -1 unit/day | 8 | 32 | -1,907 | -2.64 | [-3,325, -489] | 28% | 28% by day 29 |
| HIRE | -1 unit/day | 12 | 64 | -2,108 | -6.31 | [-2,763, -1,453] | 12% | 12% by day 29 |
| HIRE | -1 unit/day | 16 | 32 | -832 | -3.82 | [-1,258, -405] | 19% | 19% by day 29 |
| HIRE | -1 unit/day | 20 | 64 | -1,178 | -10.36 | [-1,401, -955] | 8% | 8% by day 29 |
| HIRE | -1 unit/day | 24 | 32 | -361 | -3.34 | [-573, -150] | 9% | 9% by day 29 |
| HIRE | -2 unit/day | 12 | 32 | +153 | 0.24 | [-1,080, +1,385] | 59% | 59% by day 23 |
| HIRE | -2 unit/day | 20 | 32 | -531 | -1.77 | [-1,119, +58] | 22% | 22% by day 29 |

__Observational. Exact per-cell counterfactual against deterministic tapes; uncertainty is across tapes/seeds only. Downstream policy behaviour is held fixed, so a zero crossing is NOT an optimal cutoff day. Not wired to mutation weighting.__

A wide CI here is the measurement telling you the panel is too thin for that class, not that the class is worthless -- lumpy investments (animals, land) need more cells than the 12-cell margin panel provides. See `docs/AGE-360-horizon-roi.md`.

_Generated 2026-09-15 13:30. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 260 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–5 (n=260); wheat_stock=0–26 (n=260); min_hands=3–5 (n=260); load_per_hand=12–26 (n=260); open_melons=4–14 (n=260); open_cows=1–3 (n=260); open_sheep=0–3 (n=260); early_hire_days=0–8 (n=260)
- **Evidence:** 260 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1416 candidates** with action_table data, **193747 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +8,022 (n=19116) |         +7,978 (n=9912) |         +7,978 (n=11328) | 40356 |
| BUY_ANIMAL |         +7,623 (n=9435) |         +7,742 (n=2198) |              — (n=0) | 11633 |
| BUY_SEED |         +8,198 (n=15741) |         +7,992 (n=5250) |         +7,725 (n=2105) | 23096 |
| BUY_LAND |         +8,143 (n=5324) |         +7,880 (n=1043) |              — (n=0) | 6367 |
| BUY_PRODUCT |         +7,978 (n=21219) |         +7,978 (n=9912) |         +8,012 (n=9704) | 40835 |
| HIRE |         +8,006 (n=10701) |         +8,045 (n=5164) |         +8,343 (n=3537) | 19402 |
| WATER_MISSED |         +8,139 (n=16731) |         +7,978 (n=9912) |         +7,986 (n=11207) | 37850 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +7,736 (n=8562) |         +6,790 (n=2534) |         +7,377 (n=3112) | 14208 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +8,103 |      +7,987 |      +7,655 |      +8,521 |      +7,849 |      +7,956 |
| BUY_ANIMAL |      +7,107 |           — |           — |         -35 |      +8,952 |      +7,560 |
| BUY_SEED |      +7,931 |      +8,456 |      +4,434 |      +2,068 |      +9,183 |      +8,061 |
| BUY_LAND |           — |      +2,693 |      +8,028 |      +1,630 |      +8,489 |      +8,170 |
| BUY_PRODUCT |      +7,986 |           — |           — |           — |           — |           — |
| HIRE |      +8,078 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +7,978 |      +8,472 |      +7,978 |      +8,042 |
| FEED_MISSED |           — |      +7,993 |      +5,455 |           — |           — |      +7,453 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | HIRE | late | +8,343 | 3537 | 1.82 |
| 2 | BUY_SEED | early | +8,198 | 15741 | 1.79 |
| 3 | BUY_LAND | early | +8,143 | 5324 | 1.74 |
| 4 | WATER_MISSED | early | +8,139 | 16731 | 1.79 |
| 5 | HIRE | mid | +8,045 | 5164 | 1.7 |
| 6 | SELL | early | +8,022 | 19116 | 1.73 |
| 7 | BUY_PRODUCT | late | +8,012 | 9704 | 1.71 |
| 8 | HIRE | early | +8,006 | 10701 | 1.7 |
| 9 | BUY_SEED | mid | +7,992 | 5250 | 1.68 |
| 10 | WATER_MISSED | late | +7,986 | 11207 | 1.7 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_SEED** in ('low', 'low', 'low', 'mid'): +11,076 (n=160)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +9,719 (n=290)
- **SELL** in ('low', 'low', 'low', 'mid'): +9,704 (n=294)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +9,704 (n=294)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +9,704 (n=275)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +9,696 (n=292)
- **FEED_MISSED** in ('mid', 'low', 'mid', 'high'): +9,646 (n=159)
- **BUY_LAND** in ('mid', 'low', 'mid', 'high'): +9,600 (n=164)
- **BUY_ANIMAL** in ('mid', 'low', 'mid', 'high'): +9,554 (n=165)
- **WATER_MISSED** in ('mid', 'low', 'mid', 'high'): +9,531 (n=165)
- **SELL** in ('mid', 'low', 'mid', 'high'): +9,503 (n=167)
- **BUY_SEED** in ('mid', 'low', 'mid', 'high'): +9,503 (n=167)
- **BUY_PRODUCT** in ('mid', 'low', 'mid', 'high'): +9,503 (n=167)
- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +9,163 (n=1956)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +9,151 (n=896)

## Remaining-horizon ROI (AGE-360)

`candidates/O17_ORCH_CAPITAL.py` | mode `cutoff+marginal` | 64 cells (4 tapes x 16 seeds) | fixed_shops=True | generated 2026-09-11T02:29:18

ROI = base final money - counterfactual final money, net of acquisition, operating and opportunity cost. **Read the intervention column before the number.** `class blocked` prices the whole subsystem and, for a class the policy replenishes continuously (labour, feed), is near-total ablation -- it does NOT estimate the value of the last unit. `-K unit/day` is the marginal experiment. The two can have opposite signs, and on this chassis HIRE does.

| investment | intervention | from day | n | ROI | t | 95% CI | cells + | payback |
|---|---|---:|---:|---:|---:|---|---:|---|
| BUY_ANIMAL | class blocked | 2 | 12 | +6,734 | 2.94 | [+2,243, +11,226] | 83% | 83% by day 15 |
| BUY_ANIMAL | class blocked | 4 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 5 | 24 | +13,376 | 2.99 | [+4,621, +22,132] | 67% | 67% by day 15 |
| BUY_ANIMAL | class blocked | 6 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 7 | 24 | +4,372 | 1.36 | [-1,914, +10,658] | 33% | 33% by day 18 |
| BUY_ANIMAL | class blocked | 8 | 24 | +3,350 | 1.01 | [-3,132, +9,831] | 29% | 29% by day 17 |
| BUY_ANIMAL | class blocked | 9 | 24 | -208 | -0.15 | [-2,983, +2,566] | 25% | 25% by day 23 |
| BUY_ANIMAL | class blocked | 10 | 12 | -1,008 | -2.03 | [-1,980, -36] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 2 | 12 | +3,019 | 1.93 | [-50, +6,088] | 75% | 75% by day 29 |
| BUY_ANIMAL:COW | class blocked | 6 | 12 | -1,042 | -1.00 | [-3,086, +1,003] | 50% | 50% by day 29 |
| BUY_ANIMAL:COW | class blocked | 10 | 12 | -917 | -1.82 | [-1,902, +69] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 14 | 12 | +6 | 0.03 | [-402, +414] | 17% | 17% by day 29 |
| BUY_ANIMAL:COW | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_ANIMAL:COW | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 2 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 6 | 12 | +8,781 | 1.99 | [+115, +17,448] | 33% | 33% by day 25 |
| BUY_LAND | class blocked | 10 | 12 | +2,218 | 2.24 | [+277, +4,159] | 33% | 33% by day 28 |
| BUY_LAND | class blocked | 14 | 12 | -302 | -1.00 | [-893, +290] | 0% | 0% never |
| BUY_LAND | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_LAND | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_PRODUCT | class blocked | 2 | 12 | +35,501 | 5.90 | [+23,717, +47,285] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 6 | 12 | +38,533 | 5.34 | [+24,396, +52,670] | 100% | 100% by day 9 |
| BUY_PRODUCT | class blocked | 10 | 32 | +38,821 | 5.92 | [+25,960, +51,681] | 97% | 97% by day 13 |
| BUY_PRODUCT | class blocked | 14 | 32 | +22,151 | 4.29 | [+12,032, +32,269] | 78% | 78% by day 19 |
| BUY_PRODUCT | class blocked | 18 | 32 | +13,697 | 3.84 | [+6,709, +20,685] | 62% | 62% by day 22 |
| BUY_PRODUCT | class blocked | 22 | 32 | +10,598 | 4.44 | [+5,916, +15,279] | 81% | 81% by day 25 |
| BUY_PRODUCT | class blocked | 26 | 32 | +4,647 | 5.85 | [+3,090, +6,205] | 94% | 94% by day 29 |
| BUY_PRODUCT:FERTILIZER | class blocked | 16 | 32 | +105 | 0.40 | [-409, +620] | 38% | 38% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 18 | 32 | +332 | 1.20 | [-209, +873] | 53% | 53% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 20 | 32 | +274 | 1.06 | [-231, +779] | 47% | 47% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 22 | 32 | +201 | 1.42 | [-76, +479] | 44% | 44% by day 28 |
| BUY_PRODUCT:FERTILIZER | class blocked | 24 | 32 | +156 | 1.20 | [-99, +411] | 25% | 25% by day 26 |
| BUY_PRODUCT:WHEAT | class blocked | 16 | 32 | +17,487 | 4.10 | [+9,124, +25,850] | 66% | 66% by day 20 |
| BUY_PRODUCT:WHEAT | class blocked | 18 | 32 | +13,145 | 3.91 | [+6,548, +19,742] | 59% | 59% by day 22 |
| BUY_PRODUCT:WHEAT | class blocked | 20 | 32 | +10,597 | 3.75 | [+5,059, +16,135] | 59% | 59% by day 24 |
| BUY_PRODUCT:WHEAT | class blocked | 22 | 32 | +9,922 | 4.13 | [+5,212, +14,632] | 72% | 72% by day 25 |
| BUY_PRODUCT:WHEAT | class blocked | 24 | 32 | +6,874 | 4.74 | [+4,033, +9,715] | 91% | 91% by day 27 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 8 | 32 | +1,300 | 1.88 | [-57, +2,658] | 53% | 53% by day 26 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 12 | 32 | +246 | 0.71 | [-430, +923] | 44% | 44% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 16 | 32 | +262 | 1.49 | [-82, +606] | 53% | 53% by day 28 |
| BUY_PRODUCT:WHEAT | -1 unit/day | 20 | 32 | +335 | 2.09 | [+20, +649] | 53% | 53% by day 28 |
| BUY_SEED | class blocked | 2 | 12 | +32,017 | 6.75 | [+22,721, +41,312] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 6 | 12 | +27,234 | 5.80 | [+18,025, +36,443] | 100% | 100% by day 21 |
| BUY_SEED | class blocked | 10 | 32 | +17,307 | 7.33 | [+12,677, +21,936] | 94% | 94% by day 22 |
| BUY_SEED | class blocked | 14 | 32 | +6,720 | 7.51 | [+4,966, +8,474] | 97% | 97% by day 24 |
| BUY_SEED | class blocked | 18 | 32 | +3,991 | 6.01 | [+2,689, +5,293] | 94% | 94% by day 26 |
| BUY_SEED | class blocked | 22 | 32 | +2,252 | 6.07 | [+1,525, +2,979] | 91% | 91% by day 29 |
| BUY_SEED | class blocked | 26 | 32 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED | -1 unit/day | 8 | 32 | +870 | 1.63 | [-179, +1,920] | 84% | 84% by day 26 |
| BUY_SEED | -1 unit/day | 12 | 32 | +825 | 3.29 | [+334, +1,316] | 91% | 91% by day 27 |
| BUY_SEED | -1 unit/day | 16 | 32 | +710 | 3.68 | [+331, +1,088] | 91% | 91% by day 28 |
| BUY_SEED | -1 unit/day | 20 | 32 | +444 | 4.11 | [+232, +656] | 84% | 84% by day 28 |
| BUY_SEED | -1 unit/day | 24 | 32 | +216 | 2.92 | [+71, +360] | 75% | 75% by day 29 |
| BUY_SEED:MELON | class blocked | 2 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 6 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 10 | 12 | +884 | 3.11 | [+327, +1,441] | 83% | 83% by day 25 |
| BUY_SEED:MELON | class blocked | 14 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:MELON | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 2 | 12 | +19,487 | 4.50 | [+10,992, +27,982] | 100% | 100% by day 21 |
| BUY_SEED:STRAWBERRY | class blocked | 6 | 12 | +12,168 | 2.35 | [+2,002, +22,334] | 67% | 67% by day 23 |
| BUY_SEED:STRAWBERRY | class blocked | 10 | 12 | +2,506 | 0.54 | [-6,564, +11,575] | 33% | 33% by day 25 |
| BUY_SEED:STRAWBERRY | class blocked | 14 | 12 | +1,510 | 2.08 | [+87, +2,933] | 58% | 58% by day 28 |
| BUY_SEED:STRAWBERRY | class blocked | 18 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 22 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| BUY_SEED:STRAWBERRY | class blocked | 26 | 12 | +0 | 0.00 | [+0, +0] | 0% | 0% never |
| HIRE | class blocked | 2 | 12 | +60,467 | 8.28 | [+46,154, +74,780] | 100% | 100% by day 12 |
| HIRE | class blocked | 6 | 12 | +67,166 | 9.32 | [+53,044, +81,289] | 100% | 100% by day 11 |
| HIRE | class blocked | 10 | 12 | +65,554 | 9.34 | [+51,794, +79,315] | 100% | 100% by day 11 |
| HIRE | class blocked | 14 | 32 | +58,984 | 8.97 | [+46,102, +71,867] | 100% | 100% by day 15 |
| HIRE | class blocked | 18 | 32 | +44,291 | 9.10 | [+34,746, +53,835] | 100% | 100% by day 19 |
| HIRE | class blocked | 22 | 32 | +27,209 | 7.39 | [+19,990, +34,427] | 100% | 100% by day 23 |
| HIRE | class blocked | 26 | 32 | +12,805 | 9.78 | [+10,238, +15,371] | 100% | 100% by day 27 |
| HIRE | -1 unit/day | 8 | 32 | -1,907 | -2.64 | [-3,325, -489] | 28% | 28% by day 29 |
| HIRE | -1 unit/day | 12 | 64 | -2,108 | -6.31 | [-2,763, -1,453] | 12% | 12% by day 29 |
| HIRE | -1 unit/day | 16 | 32 | -832 | -3.82 | [-1,258, -405] | 19% | 19% by day 29 |
| HIRE | -1 unit/day | 20 | 64 | -1,178 | -10.36 | [-1,401, -955] | 8% | 8% by day 29 |
| HIRE | -1 unit/day | 24 | 32 | -361 | -3.34 | [-573, -150] | 9% | 9% by day 29 |
| HIRE | -2 unit/day | 12 | 32 | +153 | 0.24 | [-1,080, +1,385] | 59% | 59% by day 23 |
| HIRE | -2 unit/day | 20 | 32 | -531 | -1.77 | [-1,119, +58] | 22% | 22% by day 29 |

__Observational. Exact per-cell counterfactual against deterministic tapes; uncertainty is across tapes/seeds only. Downstream policy behaviour is held fixed, so a zero crossing is NOT an optimal cutoff day. Not wired to mutation weighting.__

A wide CI here is the measurement telling you the panel is too thin for that class, not that the class is worthless -- lumpy investments (animals, land) need more cells than the 12-cell margin panel provides. See `docs/AGE-360-horizon-roi.md`.

_Generated 2026-09-15 13:31. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._