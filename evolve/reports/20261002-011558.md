# Evolution run 20261002-011558

Frontier opponent: `O162_THREE_SHOPS65.py` · clone: `tape_thirdfarmclub_111923787.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_3b070353e431.py` (sha `3b070353e431`)
Elapsed 0.00 h · candidates evaluated this run: 0 · games 0 (0/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 0 | 0 |
| dead_smoke | 0 | 0 |
| alive | 0 | 0 |
| held_fail | 0 | 0 |
| held_exploit | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 13739 · held-out evaluated: 8353 · held-out PASS: 894

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | — | — | not evaluated (no-op) | — | — | — | —-— |
| chassis + C1 params (seed row) | — | — | not evaluated (no-op) | — | — | — | —-— |
| C1.py (file) vs O162_THREE_SHOPS65.py | -21,351 | -16.3 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O162_THREE_SHOPS65.py | -29,650 | -11.4 | 0-10 | — | — | — | — |
| O162_THREE_SHOPS65.py own panel (dev / held) | — | — | — | +33,967 / +26,780 | — | — | — |

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

- best: best +15,151 (`51435ac9641b`), n=3780
- o15: best +14,660 (`a75ac7f5628a`), n=3570
- queue: best +14,471 (`5716cad50618`), n=3048
- wide: best +14,856 (`69f83ba942be`), n=3341

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +16,954 | 53 | 100 | 98 | 13735 | 45.66 | 53: +12,736 (n=3), 82: +9,377 (n=264), 63: +8,694 (n=3), 112: +8,282 (n=76), 68: +8,143 (n=29), 86: +8,046 (n=13), 146: +7,051 (n=9), 59: +6,232 (n=2), 122: +5,989 (n=12), 81: +5,983 (n=6), 80: +5,860 (n=19), 116: +5,571 (n=84), 65: +5,532 (n=2), 60: +5,522 (n=6), 120: +5,189 (n=40), 135: +5,120 (n=12), 71: +5,120 (n=2), 103: +5,064 (n=73), 119: +4,827 (n=22), 147: +4,819 (n=31), 75: +4,756 (n=9), 127: +4,740 (n=216), 138: +4,577 (n=27), 96: +4,514 (n=317), 73: +4,383 (n=4), 100: +4,302 (n=2399), 101: +4,287 (n=31), 92: +4,278 (n=15), 106: +4,274 (n=22), 123: +4,241 (n=88), 143: +4,186 (n=14), 128: +4,111 (n=40), 137: +4,105 (n=6818), 99: +4,103 (n=23), 74: +4,082 (n=46), 131: +4,019 (n=18), 129: +3,872 (n=43), 50: +3,813 (n=51), 93: +3,612 (n=11), 139: +3,599 (n=32), 126: +3,543 (n=21), 55: +3,500 (n=4), 140: +3,397 (n=12), 150: +3,361 (n=345), 87: +3,357 (n=17), 54: +3,231 (n=17), 114: +3,183 (n=19), 72: +3,171 (n=4), 109: +3,051 (n=18), 144: +3,027 (n=107), 104: +3,021 (n=9), 149: +3,015 (n=5), 124: +3,007 (n=181), 70: +2,986 (n=3), 130: +2,946 (n=57), 141: +2,840 (n=11), 94: +2,838 (n=30), 132: +2,740 (n=19), 118: +2,665 (n=20), 108: +2,563 (n=216), 76: +2,498 (n=15), 136: +2,326 (n=25), 121: +2,305 (n=32), 148: +2,161 (n=137), 107: +2,076 (n=545), 125: +1,981 (n=18), 64: +1,981 (n=40), 117: +1,929 (n=245), 67: +1,908 (n=28), 88: +1,896 (n=23), 90: +1,813 (n=7), 113: +1,745 (n=93), 58: +1,596 (n=31), 97: +1,543 (n=46), 83: +1,507 (n=22), 89: +1,442 (n=6), 142: +1,265 (n=13), 115: +1,234 (n=13), 95: +980 (n=7), 134: +849 (n=18), 84: +675 (n=61), 102: +667 (n=10), 85: +634 (n=10), 111: +353 (n=42), 145: +323 (n=20), 105: +192 (n=10), 110: +190 (n=59), 52: +189 (n=4), 66: +97 (n=3), 133: -91 (n=77), 98: -164 (n=10), 51: -268 (n=5), 77: -596 (n=10), 62: -4,217 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +16,380 | 37 | 92 | 48 | 7360 | 9.62 | 37: +8,974 (n=9), 79: +8,811 (n=3), 76: +8,235 (n=2), 125: +8,148 (n=2), 41: +6,829 (n=2), 73: +4,597 (n=1780), 92: +3,893 (n=5210), 150: +3,742 (n=64), 145: +3,524 (n=269), 58: +2,738 (n=7), 0: +2,231 (n=2), 68: +1,318 (n=3), 43: +31 (n=3), 66: -3,604 (n=2), 99: -7,406 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +12,929 | 15 | 14 | 9 | 13739 | 4.01 | 15: +4,633 (n=2471), 16: +4,165 (n=7649), 14: +3,592 (n=2059), 13: +2,465 (n=1127), 12: +2,098 (n=314), 11: +1,597 (n=68), 10: -1,220 (n=33), 9: -5,010 (n=11), 8: -8,296 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,433 | 2 | 3 | 4 | 13739 | 2.64 | 2: +4,185 (n=12515), 3: +2,359 (n=1062), 4: -4,803 (n=159), 5: -8,248 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +11,287 | 14 | 22 | 21 | 13739 | 8.61 | 14: +6,954 (n=74), 17: +5,179 (n=74), 7: +4,944 (n=5), 20: +4,898 (n=2521), 9: +4,822 (n=11), 21: +4,556 (n=6288), 5: +3,985 (n=29), 10: +3,950 (n=16), 8: +3,848 (n=4), 18: +3,671 (n=176), 12: +3,608 (n=89), 24: +3,190 (n=152), 16: +3,052 (n=59), 23: +2,910 (n=173), 15: +2,753 (n=49), 25: +2,544 (n=2231), 19: +2,452 (n=105), 22: +2,274 (n=1556), 11: +1,717 (n=84), 13: +1,716 (n=38), 6: -4,333 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,810 | 16 | 17 | 11 | 13739 | 7.59 | 16: +5,935 (n=1101), 17: +4,080 (n=10724), 15: +3,557 (n=683), 18: +3,465 (n=232), 19: +2,290 (n=228), 20: +1,660 (n=227), 14: +884 (n=312), 13: +394 (n=57), 11: -3,059 (n=26), 12: -3,356 (n=117), 10: -4,875 (n=32) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +10,596 | 15 | 0 | 32 | 13734 | 23.71 | 15: +8,100 (n=2), 4: +7,892 (n=14), 5: +7,574 (n=75), 23: +7,477 (n=3), 3: +6,583 (n=50), 17: +5,992 (n=7), 9: +5,900 (n=17), 18: +5,884 (n=3), 10: +5,833 (n=19), 1: +5,782 (n=618), 20: +5,133 (n=3), 11: +4,955 (n=10), 6: +4,954 (n=12), 2: +4,897 (n=211), 7: +3,968 (n=21), 0: +3,802 (n=12570), 8: +3,708 (n=15), 16: +3,194 (n=7), 40: +3,179 (n=6), 14: +2,337 (n=5), 21: +1,925 (n=2), 13: +1,672 (n=30), 25: +1,654 (n=2), 12: +235 (n=26), 32: -445 (n=2), 35: -486 (n=2), 22: -2,496 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +10,325 | 13 | 14 | 11 | 13739 | 8.98 | 13: +6,346 (n=718), 14: +3,906 (n=12466), 12: +2,308 (n=233), 7: +1,480 (n=10), 11: +1,291 (n=140), 10: +1,260 (n=68), 9: +998 (n=66), 8: -143 (n=20), 6: -1,210 (n=10), 5: -3,607 (n=4), 4: -3,979 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +7,621 | 18 | 14 | 14 | 7393 | 10.38 | 18: +7,953 (n=9), 20: +7,621 (n=2), 22: +6,771 (n=6), 9: +6,675 (n=4), 19: +5,805 (n=6), 15: +5,444 (n=515), 11: +4,399 (n=16), 13: +4,369 (n=407), 12: +4,239 (n=380), 16: +4,062 (n=10), 14: +3,909 (n=6008), 17: +3,506 (n=8), 10: +3,447 (n=4), 8: +332 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +7,551 | 2 | 2 | 4 | 13739 | 2.71 | 2: +4,294 (n=12739), 3: +1,032 (n=363), 1: -960 (n=476), 0: -3,257 (n=161) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,246 | frontier | frontier | 2 | 13739 | 0.8 | frontier: +4,657 (n=12374), v312: -2,589 (n=1365) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +7,193 | 9 | 10 | 11 | 13739 | 5.73 | 9: +5,716 (n=2108), 6: +4,817 (n=125), 11: +3,965 (n=8409), 4: +3,666 (n=1050), 7: +3,479 (n=151), 8: +3,203 (n=303), 12: +2,640 (n=97), 5: +1,959 (n=73), 10: +1,812 (n=1354), 13: -1,200 (n=27), 14: -1,477 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,175 | 0.0 | 0.0 | 13 | 13739 | 10.72 | 0.0: +4,088 (n=12385), 0.3: +3,453 (n=198), 0.2: +3,272 (n=353), 0.1: +2,991 (n=456), 0.4: +1,503 (n=162), 0.8: +1,329 (n=9), 0.5: +956 (n=58), 0.6: -65 (n=59), 0.7: -371 (n=38), 1.2: -839 (n=8), 1.0: -1,221 (n=3), 0.9: -1,737 (n=8), 1.1: -3,087 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +6,944 | 0.55 | 0.55 | 15 | 13739 | 7.4 | 0.55: +4,765 (n=2948), 0.6: +4,304 (n=7690), 0.65: +3,796 (n=806), 0.5: +3,708 (n=371), 0.7: +2,855 (n=196), 0.45: +2,780 (n=222), 0.75: +2,450 (n=240), 0.8: +2,301 (n=373), 0.85: +1,751 (n=136), 0.4: +1,172 (n=223), 1.0: +964 (n=49), 0.9: +396 (n=102), 0.95: -777 (n=21), 0.35: -1,762 (n=250), 0.3: -2,179 (n=112) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,872 | 17 | 20 | 15 | 13739 | 7.02 | 17: +5,387 (n=244), 21: +4,852 (n=334), 18: +4,510 (n=739), 19: +4,393 (n=7347), 16: +3,997 (n=145), 20: +3,554 (n=3715), 23: +3,358 (n=125), 14: +2,565 (n=67), 15: +1,723 (n=154), 22: +1,565 (n=530), 24: +912 (n=101), 25: +677 (n=52), 12: +639 (n=71), 13: +633 (n=36), 26: -1,485 (n=79) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +6,412 | 1.1 | 1.4 | 9 | 13739 | 3.78 | 1.1: +7,523 (n=900), 1.3: +4,334 (n=924), 1.8: +4,016 (n=7304), 1.5: +3,722 (n=857), 1.6: +3,617 (n=219), 1.7: +3,335 (n=1894), 1.2: +3,149 (n=551), 1.4: +2,431 (n=562), 1.0: +1,111 (n=528) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +6,357 | 0.45 | 0.25 | 11 | 7393 | 9.86 | 0.45: +7,680 (n=2), 0.05: +7,446 (n=5), 0.15: +6,561 (n=10), 0.4: +5,724 (n=10), 0.3: +5,640 (n=9), 0.1: +5,378 (n=16), 0.25: +4,050 (n=7300), 0.35: +3,931 (n=21), 0.5: +3,863 (n=9), 0.2: +3,208 (n=9), 0.0: +1,323 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +6,311 | 2 | 2 | 3 | 13739 | 1.73 | 2: +4,246 (n=12482), 1: +1,221 (n=1124), 3: -2,065 (n=133) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MORNING_LAST_HOUR | +6,087 | 9 | 8 | 9 | 13739 | 3.13 | 9: +6,861 (n=1387), 11: +4,234 (n=38), 5: +4,181 (n=6309), 8: +3,725 (n=1249), 4: +3,644 (n=1279), 6: +3,633 (n=426), 7: +2,691 (n=2399), 10: +1,826 (n=207), 12: +774 (n=445) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_UNITS | +5,883 | 8.5 | 7.5 | 17 | 7392 | 14.26 | 8.5: +6,623 (n=15), 6.0: +6,010 (n=15), 9.0: +5,772 (n=15), 9.5: +5,761 (n=6), 10.5: +5,450 (n=4), 11.0: +4,828 (n=2), 10.0: +4,696 (n=2), 5.0: +4,219 (n=5), 7.5: +4,095 (n=7051), 6.5: +4,078 (n=26), 8.0: +4,043 (n=109), 5.5: +3,273 (n=10), 4.5: +2,957 (n=2), 12.0: +2,216 (n=3), 7.0: +1,456 (n=121), 4.0: +740 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +15,151 (n=186)
- (9, 3, 4): +14,873 (n=358)
- (11, 3, 6): +14,856 (n=642)
- (11, 3, 5): +14,836 (n=1541)
- (10, 3, 6): +14,801 (n=148)
- (10, 3, 5): +14,696 (n=566)
- (10, 3, 4): +14,607 (n=508)
- (11, 3, 4): +14,581 (n=858)
- (12, 3, 5): +13,973 (n=4664)
- (13, 3, 5): +13,609 (n=201)
- (12, 3, 6): +13,558 (n=1647)
- (9, 3, 3): +13,310 (n=34)
- (9, 2, 3): +13,292 (n=22)
- (9, 3, 6): +13,258 (n=43)
- (8, 3, 4): +12,621 (n=142)

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

_Generated 2026-10-02 01:16. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 11829 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0–8 (n=11829); wheat_stock=0–40 (n=11829); min_hands=3–6 (n=11829); load_per_hand=12–26 (n=11829); open_melons=4–14 (n=11829); open_cows=1–3 (n=11829); open_sheep=0–3 (n=11829); early_hire_days=0–8 (n=11829)
- **Evidence:** 11829 candidates, multiple seeds. Confidence: high

### MARKET_FAILURE (observed in 2 recent candidates)

- **Observed outcome:** sales=111,822; missed_water=367; idle_share=0.10
- **Associated parameter ranges (correlation, not cause):** wheat_tiles=0; wheat_stock=0; min_hands=3; load_per_hand=19–20 (n=2); open_melons=9–11 (n=2); open_cows=2; open_sheep=2; early_hire_days=3–8 (n=2)
- **Evidence:** 2 candidates, multiple seeds. Confidence: low

## Action timing patterns (AGE-359: observational — correlations, not causes)

**13739 candidates** with action_table data, **1856997 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +3,953 (n=187274) |         +3,937 (n=96173) |         +3,937 (n=109912) | 393359 |
| BUY_ANIMAL |         +3,802 (n=97628) |         +3,897 (n=22440) |              — (n=0) | 120068 |
| BUY_SEED |         +4,054 (n=140113) |         +3,822 (n=49982) |         +3,721 (n=21479) | 211574 |
| BUY_LAND |         +4,091 (n=51514) |         +3,022 (n=6840) |              — (n=0) | 58354 |
| BUY_PRODUCT |         +3,938 (n=205845) |         +3,937 (n=96173) |         +3,954 (n=94949) | 396967 |
| HIRE |         +4,041 (n=100993) |         +3,899 (n=52101) |         +4,054 (n=23976) | 177070 |
| WATER_MISSED |         +4,010 (n=152766) |         +3,937 (n=96173) |         +3,933 (n=108478) | 357417 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +3,829 (n=88051) |         +3,498 (n=24752) |         +3,725 (n=29385) | 142188 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +3,993 |      +3,934 |      +3,684 |      +4,241 |      +3,969 |      +3,932 |
| BUY_ANIMAL |      +3,365 |           — |           — |      +2,742 |      +4,657 |      +3,788 |
| BUY_SEED |      +3,550 |      +4,038 |      +2,873 |      -1,180 |      +4,588 |      +3,987 |
| BUY_LAND |      -4,447 |        -628 |      +4,037 |      -1,966 |      +4,735 |      +3,953 |
| BUY_PRODUCT |      +3,942 |           — |           — |           — |           — |           — |
| HIRE |      +4,001 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +3,937 |      +3,372 |      +3,937 |      +3,978 |
| FEED_MISSED |           — |      +3,941 |      +2,760 |           — |           — |      +3,743 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | early | +4,091 | 51514 | 0.85 |
| 2 | BUY_SEED | early | +4,054 | 140113 | 0.84 |
| 3 | HIRE | late | +4,054 | 23976 | 0.81 |
| 4 | HIRE | early | +4,041 | 100993 | 0.83 |
| 5 | WATER_MISSED | early | +4,010 | 152766 | 0.83 |
| 6 | BUY_PRODUCT | late | +3,954 | 94949 | 0.82 |
| 7 | SELL | early | +3,953 | 187274 | 0.82 |
| 8 | BUY_PRODUCT | early | +3,938 | 205845 | 0.81 |
| 9 | SELL | mid | +3,937 | 96173 | 0.81 |
| 10 | SELL | late | +3,937 | 109912 | 0.81 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_ANIMAL** in ('mid', 'high', 'low', 'high'): -6,196 (n=7)
- **HIRE** in ('mid', 'mid', 'low', 'mid'): -6,018 (n=3)
- **BUY_LAND** in ('low', 'low', 'low', 'mid'): -5,556 (n=3)
- **HIRE** in ('low', 'mid', 'low', 'high'): +5,504 (n=5778)
- **BUY_ANIMAL** in ('mid', 'low', 'mid', 'mid'): +5,470 (n=292)
- **FEED_MISSED** in ('mid', 'low', 'mid', 'mid'): +5,470 (n=292)
- **SELL** in ('mid', 'low', 'mid', 'mid'): +5,450 (n=293)
- **BUY_PRODUCT** in ('mid', 'low', 'mid', 'mid'): +5,450 (n=293)
- **WATER_MISSED** in ('mid', 'low', 'mid', 'mid'): +5,450 (n=293)
- **BUY_LAND** in ('mid', 'mid', 'mid', 'high'): +5,369 (n=9369)
- **WATER_MISSED** in ('low', 'mid', 'low', 'high'): +5,359 (n=6036)
- **BUY_PRODUCT** in ('low', 'mid', 'low', 'high'): +5,227 (n=6191)
- **SELL** in ('low', 'mid', 'low', 'high'): +5,226 (n=6195)
- **WATER_MISSED** in ('low', 'mid', 'mid', 'mid'): +5,146 (n=1054)
- **SELL** in ('mid', 'high', 'low', 'high'): -4,990 (n=10)

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

_Generated 2026-10-02 01:16. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._