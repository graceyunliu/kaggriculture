# Evolution run 20260916-205402

Frontier opponent: `O162_THREE_SHOPS65.py` · clone: `tape_majkel1337_109144271.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 2.02 h · candidates evaluated this run: 171 · games 29,854 (14,811/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 31 | 62 |
| dead_pattern | 28 | 56 |
| dead_smoke | 14 | 112 |
| alive | 51 | 8568 |
| held_fail | 47 | 21056 |
| held_exploit | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 2698 · held-out evaluated: 1171 · held-out PASS: 894

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

- best: best +15,151 (`51435ac9641b`), n=891
- o15: best +14,660 (`a75ac7f5628a`), n=583
- queue: best +14,471 (`5716cad50618`), n=557
- wide: best +14,856 (`69f83ba942be`), n=667

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +18,336 | 81 | 100 | 81 | 2685 | 30.28 | 81: +13,020 (n=2), 53: +12,736 (n=3), 73: +12,491 (n=2), 60: +11,063 (n=4), 112: +10,184 (n=54), 54: +10,157 (n=2), 146: +10,055 (n=3), 119: +9,950 (n=8), 86: +9,877 (n=9), 63: +9,835 (n=2), 82: +9,824 (n=248), 103: +9,744 (n=6), 127: +9,392 (n=21), 96: +8,485 (n=3), 68: +8,143 (n=29), 99: +7,566 (n=12), 106: +7,054 (n=10), 80: +6,985 (n=15), 50: +6,592 (n=12), 120: +6,580 (n=29), 100: +5,980 (n=1235), 116: +5,946 (n=66), 87: +5,657 (n=4), 93: +5,643 (n=6), 128: +5,640 (n=11), 105: +5,364 (n=3), 94: +5,230 (n=6), 67: +4,910 (n=8), 101: +4,795 (n=23), 74: +4,395 (n=3), 143: +3,933 (n=3), 88: +3,866 (n=10), 136: +3,537 (n=3), 84: +3,214 (n=6), 131: +2,642 (n=6), 125: +2,558 (n=10), 92: +2,402 (n=5), 55: +2,362 (n=2), 117: +2,347 (n=110), 76: +2,313 (n=8), 121: +2,280 (n=12), 107: +2,225 (n=405), 102: +2,036 (n=4), 58: +1,874 (n=22), 66: +1,516 (n=2), 114: +1,401 (n=7), 111: +1,352 (n=30), 98: +1,349 (n=2), 150: +1,303 (n=7), 148: +1,256 (n=14), 113: +1,205 (n=67), 142: +926 (n=4), 85: +875 (n=4), 108: +850 (n=6), 97: +744 (n=8), 134: +712 (n=7), 90: +670 (n=5), 133: +335 (n=9), 118: +237 (n=12), 89: -147 (n=2), 83: -215 (n=9), 51: -268 (n=5), 110: -966 (n=28), 77: -1,162 (n=4), 137: -1,973 (n=2), 130: -2,241 (n=2), 145: -2,590 (n=2), 95: -5,316 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +15,725 | 16 | 17 | 11 | 2698 | 4.79 | 16: +9,002 (n=418), 17: +5,827 (n=1421), 15: +5,321 (n=352), 18: +3,448 (n=70), 20: +2,068 (n=39), 19: +2,028 (n=87), 14: +750 (n=197), 13: -547 (n=18), 12: -3,999 (n=79), 10: -5,329 (n=11), 11: -6,723 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +13,793 | 2 | 3 | 4 | 2698 | 2.23 | 2: +5,545 (n=2179), 3: +4,277 (n=489), 4: -462 (n=27), 5: -8,248 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +13,170 | 15 | 14 | 9 | 2698 | 1.8 | 15: +6,765 (n=681), 16: +6,549 (n=839), 14: +3,856 (n=761), 13: +2,983 (n=266), 12: +2,545 (n=122), 11: +1,551 (n=19), 10: -1,380 (n=6), 9: -5,607 (n=2), 8: -6,404 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +12,787 | 13 | 14 | 11 | 2695 | 5.18 | 13: +8,808 (n=440), 14: +4,825 (n=2083), 8: +4,214 (n=5), 12: +2,705 (n=49), 9: +1,380 (n=34), 10: +573 (n=31), 11: +419 (n=49), 4: -3,979 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +12,279 | 12 | 14 | 4 | 698 | 2.39 | 12: +10,878 (n=17), 15: +7,293 (n=85), 14: +4,212 (n=591), 8: -1,401 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,264 | 3 | 0 | 28 | 2690 | 15.37 | 3: +9,768 (n=13), 4: +8,779 (n=7), 5: +8,537 (n=59), 9: +7,591 (n=9), 17: +7,175 (n=5), 1: +7,062 (n=316), 2: +6,922 (n=9), 10: +6,380 (n=16), 20: +6,190 (n=2), 6: +5,817 (n=2), 7: +5,764 (n=10), 0: +4,863 (n=2202), 8: +4,679 (n=5), 12: +4,275 (n=5), 11: +3,818 (n=2), 13: +2,524 (n=20), 25: +1,654 (n=2), 40: +930 (n=2), 14: +563 (n=2), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,693 | 19 | 20 | 15 | 2698 | 8.02 | 19: +9,067 (n=425), 17: +7,201 (n=89), 14: +6,635 (n=11), 16: +6,121 (n=32), 21: +5,725 (n=106), 18: +5,504 (n=72), 20: +4,838 (n=1622), 23: +2,758 (n=26), 24: +2,315 (n=11), 22: +2,007 (n=203), 15: +854 (n=64), 25: +256 (n=8), 13: -885 (n=6), 12: -1,101 (n=11), 26: -1,625 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +9,194 | 11 | 14 | 9 | 2698 | 4.79 | 11: +9,646 (n=183), 13: +8,872 (n=558), 10: +6,851 (n=12), 8: +6,311 (n=8), 9: +4,329 (n=5), 12: +3,989 (n=116), 14: +3,864 (n=1736), 7: +1,269 (n=74), 6: +452 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +8,319 | 8 | 3 | 9 | 2698 | 2.07 | 8: +9,423 (n=828), 6: +7,146 (n=31), 5: +6,414 (n=676), 7: +6,330 (n=24), 2: +3,512 (n=112), 0: +2,151 (n=44), 4: +1,955 (n=54), 1: +1,835 (n=10), 3: +1,104 (n=919) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +8,263 | frontier | frontier | 2 | 2698 | 0.8 | frontier: +6,076 (n=2425), v312: -2,187 (n=273) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +8,131 | 9 | 10 | 11 | 2698 | 5.2 | 9: +7,121 (n=1520), 6: +5,845 (n=90), 7: +5,406 (n=34), 8: +5,371 (n=145), 5: +5,250 (n=10), 11: +4,423 (n=122), 4: +4,329 (n=32), 12: +4,208 (n=25), 10: +1,402 (n=708), 13: +1,000 (n=4), 14: -1,009 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +8,088 | 9 | 8 | 9 | 2698 | 2.6 | 9: +8,038 (n=1079), 11: +7,125 (n=22), 8: +4,149 (n=858), 5: +3,585 (n=22), 10: +3,548 (n=112), 4: +3,429 (n=153), 7: +1,982 (n=247), 12: +1,390 (n=186), 6: -50 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +8,016 | 0.15 | 0.25 | 5 | 695 | 0.99 | 0.15: +12,680 (n=5), 0.25: +4,664 (n=690) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,862 | 20 | 22 | 18 | 2695 | 3.02 | 20: +9,419 (n=549), 14: +9,229 (n=46), 17: +8,404 (n=15), 11: +7,234 (n=22), 21: +7,216 (n=723), 13: +5,940 (n=4), 18: +5,550 (n=69), 5: +4,810 (n=8), 19: +3,229 (n=15), 24: +2,829 (n=32), 25: +2,084 (n=548), 23: +2,033 (n=50), 22: +1,975 (n=589), 16: +1,630 (n=14), 15: +1,557 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,749 | 25 | 30 | 22 | 2696 | 5.63 | 25: +7,859 (n=420), 29: +7,800 (n=880), 42: +6,603 (n=18), 26: +5,311 (n=163), 37: +5,218 (n=6), 27: +4,694 (n=28), 31: +4,604 (n=20), 39: +4,307 (n=3), 34: +3,896 (n=35), 43: +3,122 (n=6), 36: +2,882 (n=13), 35: +2,433 (n=24), 30: +2,426 (n=894), 40: +2,142 (n=5), 28: +1,678 (n=97), 33: +1,590 (n=17), 32: +1,422 (n=50), 38: +1,180 (n=12), 44: +353 (n=3), 41: +110 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +7,738 | 1.1 | 1.4 | 9 | 2698 | 1.43 | 1.1: +9,174 (n=669), 1.5: +7,235 (n=193), 1.3: +4,993 (n=727), 1.6: +4,645 (n=18), 1.2: +4,322 (n=194), 1.7: +3,034 (n=100), 1.4: +2,455 (n=416), 1.0: +2,149 (n=252), 1.8: +1,436 (n=129) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HIRE_MAX_MARGINAL | +7,543 | 233 | 144 | 6 | 2698 | 3.43 | 233: +8,146 (n=372), 89: +5,045 (n=98), 144: +4,980 (n=1992), 1000000000: +4,641 (n=87), 377: +2,787 (n=91), 55: +603 (n=58) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,339 | 0.0 | 0.0 | 11 | 2696 | 6.79 | 0.0: +5,705 (n=2333), 0.3: +4,181 (n=35), 0.2: +4,065 (n=92), 0.1: +2,255 (n=134), 0.4: +1,612 (n=41), 0.5: +1,518 (n=13), 0.8: -35 (n=2), 0.7: -1,455 (n=20), 0.6: -1,634 (n=26) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +7,328 | 8 | 6 | 8 | 2698 | 1.78 | 8: +8,730 (n=939), 10: +7,560 (n=81), 6: +3,669 (n=831), 9: +3,667 (n=145), 7: +3,249 (n=326), 3: +1,950 (n=182), 5: +1,874 (n=129), 4: +1,403 (n=65) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +15,151 (n=82)
- (9, 3, 4): +14,873 (n=187)
- (11, 3, 6): +14,856 (n=256)
- (11, 3, 5): +14,836 (n=702)
- (10, 3, 6): +14,801 (n=54)
- (10, 3, 5): +14,696 (n=225)
- (10, 3, 4): +14,607 (n=249)
- (11, 3, 4): +14,581 (n=385)
- (12, 3, 5): +13,973 (n=128)
- (13, 3, 5): +13,609 (n=26)
- (12, 3, 6): +13,558 (n=60)
- (9, 3, 3): +13,310 (n=16)
- (9, 2, 3): +13,292 (n=19)
- (9, 3, 6): +13,258 (n=13)
- (8, 3, 4): +12,621 (n=16)

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

_Generated 2026-09-16 22:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 1033 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–8 (n=1033); wheat_stock=0–26 (n=1033); min_hands=3–6 (n=1033); load_per_hand=12–26 (n=1033); open_melons=4–14 (n=1033); open_cows=1–3 (n=1033); open_sheep=0–3 (n=1033); early_hire_days=0–8 (n=1033)
- **Evidence:** 1033 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**2698 candidates** with action_table data, **366315 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,279 (n=36403) |         +5,240 (n=18886) |         +5,240 (n=21584) | 76873 |
| BUY_ANIMAL |         +4,954 (n=17994) |         +5,290 (n=3896) |              — (n=0) | 21890 |
| BUY_SEED |         +5,577 (n=29117) |         +5,139 (n=10116) |         +4,815 (n=4171) | 43404 |
| BUY_LAND |         +5,438 (n=10087) |         +4,656 (n=2140) |              — (n=0) | 12227 |
| BUY_PRODUCT |         +5,243 (n=40411) |         +5,240 (n=18886) |         +5,266 (n=18482) | 77779 |
| HIRE |         +5,401 (n=19879) |         +5,223 (n=9992) |         +5,841 (n=6396) | 36267 |
| WATER_MISSED |         +5,475 (n=31221) |         +5,240 (n=18886) |         +5,241 (n=21379) | 71486 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +5,087 (n=16333) |         +4,732 (n=4304) |         +4,940 (n=5752) | 26389 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,347 |      +5,241 |      +4,979 |      +6,211 |      +5,211 |      +5,173 |
| BUY_ANIMAL |      +4,482 |           — |           — |      +1,960 |      +6,076 |      +4,961 |
| BUY_SEED |      +5,534 |      +5,855 |      +2,244 |        -349 |      +6,117 |      +5,324 |
| BUY_LAND |      -5,213 |      +1,825 |      +5,342 |      -2,368 |      +6,585 |      +5,265 |
| BUY_PRODUCT |      +5,248 |           — |           — |           — |           — |           — |
| HIRE |      +5,429 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,240 |      +6,676 |      +5,240 |      +5,312 |
| FEED_MISSED |           — |      +5,273 |      +3,127 |           — |           — |      +4,983 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | HIRE | late | +5,841 | 6396 | 1.02 |
| 2 | BUY_SEED | early | +5,577 | 29117 | 0.97 |
| 3 | WATER_MISSED | early | +5,475 | 31221 | 0.96 |
| 4 | BUY_LAND | early | +5,438 | 10087 | 0.94 |
| 5 | HIRE | early | +5,401 | 19879 | 0.93 |
| 6 | BUY_ANIMAL | mid | +5,290 | 3896 | 0.9 |
| 7 | SELL | early | +5,279 | 36403 | 0.92 |
| 8 | BUY_PRODUCT | late | +5,266 | 18482 | 0.91 |
| 9 | BUY_PRODUCT | early | +5,243 | 40411 | 0.91 |
| 10 | WATER_MISSED | late | +5,241 | 21379 | 0.91 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_SEED** in ('low', 'low', 'low', 'mid'): +10,320 (n=263)
- **BUY_SEED** in ('low', 'mid', 'low', 'mid'): +8,498 (n=6)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +7,648 (n=501)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +7,601 (n=481)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +7,584 (n=509)
- **SELL** in ('low', 'low', 'low', 'mid'): +7,564 (n=512)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +7,564 (n=512)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +7,209 (n=1509)
- **WATER_MISSED** in ('low', 'mid', 'mid', 'mid'): +6,769 (n=225)
- **BUY_ANIMAL** in ('mid', 'high', 'high', 'high'): +6,637 (n=3069)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +6,497 (n=2421)
- **SELL** in ('mid', 'high', 'low', 'high'): -6,482 (n=5)
- **BUY_ANIMAL** in ('mid', 'high', 'low', 'high'): -6,482 (n=5)
- **BUY_SEED** in ('mid', 'high', 'low', 'high'): -6,482 (n=5)
- **BUY_PRODUCT** in ('mid', 'high', 'low', 'high'): -6,482 (n=5)

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

_Generated 2026-09-16 22:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._