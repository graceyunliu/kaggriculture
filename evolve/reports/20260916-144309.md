# Evolution run 20260916-144309

Frontier opponent: `O162_THREE_SHOPS65.py` · clone: `tape_majkel1337_109144271.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.00 h · candidates evaluated this run: 169 · games 30,134 (15,046/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 17 | 34 |
| dead_pattern | 26 | 52 |
| dead_smoke | 18 | 144 |
| alive | 66 | 11088 |
| held_fail | 42 | 18816 |
| held_exploit | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 2403 · held-out evaluated: 1036 · held-out PASS: 894

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | — | — | not evaluated (no-op) | — | — | — | —-— |
| chassis + C1 params (seed row) | — | — | not evaluated (no-op) | — | — | — | —-— |
| C1.py (file) vs O162_THREE_SHOPS65.py | -21,351 | -16.3 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O162_THREE_SHOPS65.py | -29,650 | -11.4 | 0-10 | — | — | — | — |
| O162_THREE_SHOPS65.py own panel (dev / held) | — | — | — | +26,086 / +22,278 | — | — | — |

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
| `3afa6ad48d27` | best | crossover | +14,961 | 12.8 | 28-2 | -8,431 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→25, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `f64884c5deec` | best | crossover | +14,873 | 12.2 | 28-2 | -6,970 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, MAX_SHEEP 14→13, OPENING_MELONS 14→13, FERT_RADIUS 3→4, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `14fb3191638a` | best | crossover | +14,868 | 12.7 | 29-1 | -7,015 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `69f83ba942be` | wide | mutate | +14,856 | 11.9 | 28-2 | -6,725 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `39986dde3425` | best | migrate | +14,836 | 11.8 | 29-1 | -7,673 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→112, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `b9ddb338852d` | best | mutate | +14,801 | 12.5 | 29-1 | -6,867 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `9c02b45cd0fe` | best | crossover | +14,752 | 12.0 | 29-1 | -7,621 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→112, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `b59a939bdf4e` | wide | mutate | +14,713 | 11.9 | 28-2 | -5,853 | held_pass | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `6023b246b80f` | wide | block_pair | +14,696 | 12.2 | 29-1 | -6,962 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `b5c2b622e5f7` | best | crossover | +14,667 | 12.9 | 29-1 | -7,896 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.3, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→4, MELON_MORNING_MIN_YIELD 6→5 |
| `a75ac7f5628a` | o15 | crossover | +14,660 | 10.8 | 29-1 | -7,428 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, wheat_cap 22→21, wheat_sell_price 30→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→13, OPENING_MELONS 14→11, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→5, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→10, MELON_MORNING_MIN_YIELD 6→5 |
| `b9d933e3edca` | best | crossover | +14,634 | 11.9 | 28-2 | -7,252 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→15, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→107, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, SPREAD_W 1.25→1.0, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9 |
| `4dc9d21748ef` | best | crossover | +14,625 | 12.5 | 29-1 | -7,671 | alive | open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, max_animals 17→16, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→29, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→112, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→5, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_W 1.25→1.0, HIRE_MAX_MARGINAL 144→233, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |
| `a465c8d32ea0` | best | block_pair | +14,607 | 12.3 | 29-1 | -7,219 | alive | load_per_hand 20→19, open_melons 10→9, early_hire_days 3→8, feed_spare_poor 0→1, fert_buy 4→2, max_animals 17→16, wheat_cap 22→20, wheat_sell_price 30→29, MAX_HANDS 14→16, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→82, HERD_LAST_DAY 17→20, NEAR_RADIUS 2→4, OPP_GROWTH 1.4→1.1, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→5, MELON_MORNING 1→0, MELON_MORNING_LAST_HOUR 8→9, MELON_MORNING_MIN_YIELD 6→5 |

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

_direction ledger unavailable: AssertionError("min_hands_knob_interactions: ABANDON record missing ['hypothesis', 'negative_evidence', 'scope']")_

## Islands (best dev margin, population size)

- best: best +15,151 (`51435ac9641b`), n=816
- o15: best +14,660 (`a75ac7f5628a`), n=516
- queue: best +14,471 (`5716cad50618`), n=475
- wide: best +14,856 (`69f83ba942be`), n=596

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +18,336 | 81 | 100 | 81 | 2386 | 28.29 | 81: +13,020 (n=2), 53: +12,736 (n=3), 73: +12,491 (n=2), 60: +11,063 (n=4), 86: +10,542 (n=8), 112: +10,184 (n=54), 54: +10,157 (n=2), 146: +10,055 (n=3), 119: +9,950 (n=8), 63: +9,835 (n=2), 82: +9,824 (n=248), 103: +9,744 (n=6), 127: +9,392 (n=21), 99: +8,609 (n=11), 96: +8,485 (n=3), 68: +8,143 (n=29), 94: +7,681 (n=5), 106: +7,054 (n=10), 80: +6,985 (n=15), 120: +6,673 (n=28), 50: +6,592 (n=12), 100: +6,419 (n=1092), 116: +5,946 (n=66), 84: +5,799 (n=4), 87: +5,657 (n=4), 93: +5,643 (n=6), 128: +5,640 (n=11), 105: +5,364 (n=3), 74: +5,356 (n=2), 101: +4,803 (n=22), 88: +4,625 (n=3), 114: +4,008 (n=4), 143: +3,933 (n=3), 131: +3,889 (n=5), 136: +3,537 (n=3), 125: +3,294 (n=8), 97: +2,566 (n=4), 107: +2,464 (n=365), 55: +2,362 (n=2), 58: +2,254 (n=17), 92: +2,237 (n=4), 117: +2,225 (n=76), 121: +2,030 (n=10), 148: +1,692 (n=11), 111: +1,635 (n=29), 66: +1,516 (n=2), 150: +1,303 (n=7), 85: +1,274 (n=3), 77: +1,272 (n=2), 108: +850 (n=6), 134: +712 (n=7), 113: +688 (n=54), 51: +442 (n=3), 90: +440 (n=3), 76: +408 (n=5), 133: +375 (n=8), 118: +237 (n=12), 89: -147 (n=2), 83: -215 (n=9), 142: -265 (n=3), 102: -665 (n=2), 110: -940 (n=24), 137: -1,973 (n=2), 95: -5,316 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +17,182 | 16 | 17 | 11 | 2403 | 4.67 | 16: +9,274 (n=403), 17: +6,284 (n=1238), 15: +6,022 (n=306), 18: +3,506 (n=67), 19: +2,293 (n=60), 20: +2,083 (n=35), 14: +784 (n=186), 13: +49 (n=17), 12: -3,948 (n=76), 10: -5,329 (n=11), 11: -7,908 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +14,308 | 2 | 3 | 4 | 2403 | 2.16 | 2: +6,060 (n=1898), 3: +4,412 (n=475), 4: -462 (n=27), 5: -8,248 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +13,350 | 15 | 14 | 9 | 2403 | 2.03 | 15: +6,945 (n=660), 16: +6,697 (n=809), 14: +4,123 (n=657), 13: +3,626 (n=162), 12: +2,797 (n=92), 11: +2,396 (n=15), 10: -1,581 (n=4), 9: -5,607 (n=2), 8: -6,404 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +13,018 | 13 | 14 | 11 | 2400 | 5.08 | 13: +8,959 (n=430), 14: +5,206 (n=1825), 8: +4,214 (n=5), 12: +3,813 (n=34), 9: +1,501 (n=31), 11: +511 (n=42), 10: +424 (n=30), 4: -4,059 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,264 | 3 | 0 | 28 | 2395 | 15.06 | 3: +9,768 (n=13), 4: +8,779 (n=7), 5: +8,749 (n=56), 9: +7,591 (n=9), 17: +7,175 (n=5), 1: +7,062 (n=316), 2: +6,922 (n=9), 7: +6,799 (n=8), 10: +6,380 (n=16), 20: +6,190 (n=2), 6: +5,817 (n=2), 8: +5,801 (n=4), 0: +5,284 (n=1923), 12: +4,275 (n=5), 11: +3,818 (n=2), 13: +3,802 (n=10), 25: +1,654 (n=2), 40: +930 (n=2), 14: +563 (n=2), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +11,432 | 12 | 14 | 4 | 594 | 2.31 | 12: +10,878 (n=17), 15: +7,379 (n=81), 14: +4,534 (n=492), 8: -554 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,404 | 19 | 20 | 15 | 2403 | 7.73 | 19: +9,194 (n=418), 17: +7,261 (n=88), 14: +6,635 (n=11), 21: +6,589 (n=86), 16: +6,467 (n=31), 18: +5,652 (n=68), 20: +5,242 (n=1399), 23: +3,442 (n=22), 24: +2,315 (n=11), 22: +2,252 (n=173), 15: +854 (n=64), 25: +389 (n=7), 13: -885 (n=6), 12: -1,101 (n=11), 26: -1,210 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +9,967 | 11 | 14 | 9 | 2403 | 4.67 | 11: +9,646 (n=183), 13: +9,190 (n=531), 10: +6,851 (n=12), 8: +6,726 (n=7), 9: +4,329 (n=5), 14: +4,172 (n=1515), 12: +4,081 (n=94), 7: +1,204 (n=52), 6: -321 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +8,913 | 9 | 10 | 11 | 2403 | 5.5 | 9: +7,490 (n=1419), 6: +6,125 (n=85), 7: +6,063 (n=27), 11: +5,576 (n=75), 8: +5,520 (n=139), 5: +5,250 (n=10), 12: +4,642 (n=22), 4: +3,936 (n=26), 10: +1,378 (n=589), 13: +1,000 (n=4), 14: -1,422 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +8,780 | 8 | 3 | 9 | 2403 | 2.05 | 8: +9,546 (n=815), 6: +7,323 (n=30), 7: +6,858 (n=22), 5: +6,441 (n=673), 2: +3,948 (n=102), 4: +2,075 (n=49), 1: +1,451 (n=8), 0: +1,424 (n=31), 3: +766 (n=673) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +8,498 | 1.1 | 1.4 | 9 | 2403 | 1.55 | 1.1: +9,505 (n=640), 1.5: +7,490 (n=186), 1.3: +5,223 (n=680), 1.6: +4,557 (n=17), 1.2: +4,539 (n=185), 1.0: +2,594 (n=195), 1.4: +2,507 (n=374), 1.7: +2,250 (n=37), 1.8: +1,007 (n=89) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +8,490 | frontier | frontier | 2 | 2403 | 0.79 | frontier: +6,534 (n=2151), v312: -1,956 (n=252) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +8,474 | 9 | 8 | 9 | 2403 | 2.89 | 9: +8,330 (n=1039), 11: +7,125 (n=22), 5: +4,997 (n=14), 8: +4,272 (n=819), 10: +3,966 (n=98), 4: +3,818 (n=95), 7: +1,473 (n=145), 12: +1,419 (n=154), 6: -144 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,347 | 14 | 22 | 18 | 2400 | 3.36 | 14: +9,904 (n=41), 20: +9,536 (n=541), 17: +8,828 (n=14), 11: +7,817 (n=21), 21: +7,356 (n=698), 13: +5,940 (n=4), 18: +5,592 (n=68), 5: +4,810 (n=8), 19: +3,327 (n=14), 24: +2,743 (n=30), 22: +2,148 (n=511), 25: +2,017 (n=376), 23: +2,007 (n=49), 16: +1,630 (n=14), 15: +1,557 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +8,000 | 29 | 30 | 21 | 2402 | 6.04 | 29: +8,110 (n=846), 25: +7,958 (n=412), 37: +6,842 (n=4), 42: +6,603 (n=18), 27: +6,144 (n=22), 26: +5,965 (n=143), 31: +5,298 (n=15), 39: +4,307 (n=3), 34: +4,012 (n=34), 36: +3,541 (n=9), 43: +3,122 (n=6), 35: +2,447 (n=22), 30: +2,396 (n=717), 33: +2,305 (n=14), 40: +2,142 (n=5), 38: +1,757 (n=11), 28: +1,564 (n=81), 32: +1,028 (n=35), 44: +353 (n=3), 41: +110 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HIRE_MAX_MARGINAL | +7,799 | 233 | 144 | 6 | 2403 | 3.38 | 233: +8,434 (n=356), 1000000000: +5,502 (n=69), 144: +5,365 (n=1756), 89: +5,282 (n=90), 377: +3,223 (n=77), 55: +635 (n=55) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +7,663 | 0.15 | 0.25 | 4 | 592 | 0.98 | 0.15: +12,680 (n=5), 0.25: +5,017 (n=587) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,584 | 0.0 | 0.0 | 11 | 2401 | 6.88 | 0.0: +6,129 (n=2101), 0.3: +5,232 (n=29), 0.2: +4,272 (n=66), 0.1: +2,197 (n=109), 0.5: +1,665 (n=12), 0.4: +1,571 (n=39), 0.8: -35 (n=2), 0.6: -1,401 (n=23), 0.7: -1,455 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +7,493 | 8 | 6 | 8 | 2403 | 2.11 | 8: +8,772 (n=933), 10: +8,030 (n=71), 9: +4,245 (n=110), 6: +3,889 (n=714), 7: +3,789 (n=248), 3: +2,040 (n=172), 5: +1,918 (n=116), 4: +1,280 (n=39) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +15,151 (n=74)
- (9, 3, 4): +14,873 (n=171)
- (11, 3, 6): +14,856 (n=233)
- (11, 3, 5): +14,836 (n=625)
- (10, 3, 6): +14,801 (n=52)
- (10, 3, 5): +14,696 (n=215)
- (10, 3, 4): +14,607 (n=217)
- (11, 3, 4): +14,581 (n=345)
- (12, 3, 5): +13,973 (n=110)
- (13, 3, 5): +13,609 (n=22)
- (12, 3, 6): +13,558 (n=50)
- (9, 3, 3): +13,310 (n=15)
- (9, 2, 3): +13,292 (n=19)
- (9, 3, 6): +13,258 (n=12)
- (8, 3, 4): +12,621 (n=15)

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

_Generated 2026-09-16 16:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 784 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–8 (n=784); wheat_stock=0–26 (n=784); min_hands=3–6 (n=784); load_per_hand=12–26 (n=784); open_melons=4–14 (n=784); open_cows=1–3 (n=784); open_sheep=0–3 (n=784); early_hire_days=0–8 (n=784)
- **Evidence:** 784 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**2403 candidates** with action_table data, **326592 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,686 (n=32408) |         +5,643 (n=16821) |         +5,643 (n=19224) | 68453 |
| BUY_ANIMAL |         +5,347 (n=15976) |         +5,649 (n=3540) |              — (n=0) | 19516 |
| BUY_SEED |         +5,991 (n=26038) |         +5,541 (n=9011) |         +5,203 (n=3714) | 38763 |
| BUY_LAND |         +5,842 (n=8995) |         +5,071 (n=1899) |              — (n=0) | 10894 |
| BUY_PRODUCT |         +5,646 (n=35992) |         +5,643 (n=16821) |         +5,672 (n=16440) | 69253 |
| HIRE |         +5,807 (n=17746) |         +5,644 (n=8908) |         +6,265 (n=5760) | 32414 |
| WATER_MISSED |         +5,892 (n=27860) |         +5,643 (n=16821) |         +5,648 (n=19031) | 63712 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +5,486 (n=14510) |         +5,066 (n=3930) |         +5,310 (n=5147) | 23587 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,758 |      +5,645 |      +5,351 |      +6,641 |      +5,607 |      +5,576 |
| BUY_ANIMAL |      +4,843 |           — |           — |      +2,070 |      +6,534 |      +5,345 |
| BUY_SEED |      +5,936 |      +6,229 |      +2,218 |        +194 |      +6,615 |      +5,730 |
| BUY_LAND |           — |      +2,515 |      +5,739 |      -2,201 |      +6,944 |      +5,683 |
| BUY_PRODUCT |      +5,652 |           — |           — |           — |           — |           — |
| HIRE |      +5,844 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,643 |      +7,074 |      +5,643 |      +5,722 |
| FEED_MISSED |           — |      +5,681 |      +3,442 |           — |           — |      +5,361 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | HIRE | late | +6,265 | 5760 | 1.09 |
| 2 | BUY_SEED | early | +5,991 | 26038 | 1.04 |
| 3 | WATER_MISSED | early | +5,892 | 27860 | 1.02 |
| 4 | BUY_LAND | early | +5,842 | 8995 | 0.99 |
| 5 | HIRE | early | +5,807 | 17746 | 0.99 |
| 6 | SELL | early | +5,686 | 32408 | 0.98 |
| 7 | BUY_PRODUCT | late | +5,672 | 16440 | 0.97 |
| 8 | BUY_ANIMAL | mid | +5,649 | 3540 | 0.95 |
| 9 | WATER_MISSED | late | +5,648 | 19031 | 0.97 |
| 10 | BUY_PRODUCT | early | +5,646 | 35992 | 0.96 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_SEED** in ('low', 'low', 'low', 'mid'): +10,774 (n=253)
- **BUY_SEED** in ('low', 'mid', 'low', 'mid'): +8,498 (n=6)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +8,186 (n=472)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +8,125 (n=479)
- **SELL** in ('low', 'low', 'low', 'mid'): +8,100 (n=482)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +8,100 (n=482)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +8,082 (n=455)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +7,539 (n=1377)
- **BUY_SEED** in ('low', 'mid', 'high', 'high'): +7,036 (n=1472)
- **WATER_MISSED** in ('low', 'mid', 'mid', 'mid'): +7,006 (n=212)
- **BUY_ANIMAL** in ('mid', 'high', 'high', 'high'): +6,947 (n=2874)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +6,867 (n=2215)
- **HIRE** in ('low', 'mid', 'low', 'high'): +6,783 (n=525)
- **SELL** in ('low', 'low', 'mid', 'mid'): +6,764 (n=1874)
- **FEED_MISSED** in ('low', 'low', 'low', 'high'): +6,603 (n=3336)

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

_Generated 2026-09-16 16:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._