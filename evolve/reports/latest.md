# Evolution run 20260910-083454

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.20 h · candidates evaluated this run: 22 · games 1,752 (8,950/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 2 | 4 |
| dead_pattern | 2 | 4 |
| dead_smoke | 4 | 32 |
| alive | 13 | 1404 |
| held_fail | 1 | 308 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 116 · held-out evaluated: 5 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |
| `362ca8604fb4` | c1 | paired | +2,033 | 1.6 | 7-3 | -24,144 | alive | MAX_HANDS 14→13, SPREAD_W 1.25→1.0 |
| `7a0b60c391c7` | wide | mutate | +1,686 | 0.8 | 5-5 | -23,482 | alive | melon_floor 0→150, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `a1c2b0acfbad` | wide | crossover | +1,312 | 0.6 | 4-6 | -23,295 | alive | melon_floor 0→100, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_cap 22→25, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `038351a768ec` | v312 | crossover | +1,192 | 0.7 | 7-3 | -19,705 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, demand_share 0.55→0.45, setup_capital_share 0.25→0.45, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4 |
| `fab9a13dc437` | v312 | mutate | +1,150 | 1.0 | 6-4 | -27,354 | alive | load_per_hand 20→18, open_melons 8→9, early_hire_days 5→3, wheat_water_tier 0→1, MAX_HANDS 14→12, OPP_GROWTH 1.4→1.3, SPREAD_CAP 3→4 |
| `7624469900c3` | queue | archive_crossover:crossover_g000025_20260910-083212_1 | +1,124 | 1.7 | 7-3 | -18,432 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35 |
| `842eaa9dcc6d` | v312 | crossover | +1,121 | 2.1 | 6-4 | -23,619 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→35 |
| `af9e8426e80f` | queue | mutate | +1,056 | 0.6 | 5-5 | -19,537 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, demand_share 0.55→0.65, max_animals 17→14, wheat_sell_price 30→34, setup_capital_share 0.25→0.2, labor_reserve_buffer 92→93, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→83 |
| `16fe3c276c5b` | queue | archive_crossover:crossover_g000025_20260910-083212_0 | +887 | 1.7 | 5-5 | -23,501 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, FERT_RADIUS 3→4 |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=14
- M2: best -3,547 (`7c01cb19575f`), n=8
- c1: best +2,683 (`5fd05605827b`), n=23
- queue: best +4,836 (`7ec902ce836b`), n=36
- v312: best +1,192 (`038351a768ec`), n=18
- wide: best +1,686 (`7a0b60c391c7`), n=17

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| open_melons | +7,713 | 11 | 8 | 6 | 115 | 1.87 | 11: +1,098 (n=2), 10: -844 (n=43), 8: -2,318 (n=66), 4: -4,132 (n=2), 5: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +7,393 | 85 | 100 | 12 | 109 | 3.59 | 85: +784 (n=2), 100: -1,578 (n=100), 92: -4,156 (n=3), 110: -4,899 (n=2), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +6,208 | 5 | 6 | 6 | 114 | 2.19 | 5: -172 (n=2), 3: -318 (n=18), 6: -1,968 (n=91), 7: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +5,927 | 13 | 22 | 7 | 116 | 3.89 | 13: -452 (n=9), 25: -582 (n=9), 22: -1,537 (n=81), 18: -3,436 (n=8), 24: -3,782 (n=3), 20: -5,213 (n=3), 23: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +4,970 | 2 | 2 | 4 | 116 | 2.38 | 2: -1,501 (n=98), 1: -2,582 (n=12), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +4,207 | 0.45 | 0.25 | 8 | 114 | 3.16 | 0.45: +26 (n=3), 0.2: -1,031 (n=2), 0.4: -1,338 (n=14), 0.25: -1,503 (n=79), 0.5: -3,672 (n=3), 0.35: -4,181 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +4,186 | 17 | 19 | 6 | 116 | 3.29 | 17: +475 (n=10), 14: -172 (n=2), 16: -773 (n=7), 19: -1,881 (n=83), 18: -3,479 (n=7), 20: -3,711 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +4,119 | 25 | 30 | 7 | 114 | 1.76 | 25: -757 (n=28), 26: -1,747 (n=15), 28: -2,132 (n=6), 30: -2,156 (n=63), 36: -4,876 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +3,875 | 12 | 14 | 6 | 115 | 3.0 | 12: +593 (n=13), 13: -1,184 (n=3), 14: -2,022 (n=92), 11: -2,486 (n=2), 15: -3,281 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,853 | 0.45 | 0.55 | 6 | 116 | 3.14 | 0.45: -139 (n=7), 0.65: -709 (n=8), 0.55: -1,592 (n=80), 0.3: -3,235 (n=3), 0.5: -3,485 (n=16), 0.6: -3,992 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +3,755 | 2 | 3 | 3 | 116 | 1.59 | 2: -1,433 (n=7), 3: -1,507 (n=100), 4: -5,188 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_RADIUS | +3,645 | 3 | 5 | 5 | 116 | 2.02 | 3: -941 (n=18), 5: -1,556 (n=70), 2: -2,162 (n=3), 6: -2,868 (n=23), 4: -4,586 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +3,609 | 19 | 20 | 8 | 112 | 2.0 | 19: -908 (n=20), 20: -1,756 (n=84), 22: -2,296 (n=2), 21: -4,517 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +3,545 | 39 | 38 | 9 | 112 | 1.37 | 39: +328 (n=7), 35: -509 (n=14), 34: -977 (n=29), 38: -2,569 (n=53), 43: -3,218 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,528 | frontier | frontier | 2 | 116 | 0.88 | frontier: -1,576 (n=109), v312: -5,103 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +3,503 | 1.0 | 1.25 | 5 | 114 | 1.84 | 1.0: -144 (n=2), 1.25: -1,738 (n=108), 1.5: -3,646 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +3,449 | 11 | 14 | 4 | 116 | 2.38 | 11: -51 (n=2), 14: -1,555 (n=98), 12: -3,146 (n=3), 13: -3,500 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,187 | 7 | 5 | 6 | 114 | 2.19 | 7: -1,148 (n=3), 3: -1,393 (n=18), 5: -1,832 (n=91), 0: -4,334 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +3,030 | 107 | 92 | 10 | 111 | 3.28 | 107: -752 (n=3), 150: -888 (n=3), 11: -1,109 (n=8), 92: -1,896 (n=95), 76: -3,783 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +2,568 | 2 | 2 | 3 | 116 | 1.84 | 2: -1,667 (n=110), 1: -3,592 (n=2), 3: -4,235 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=7)
- (7, 3, 4): +3,920 (n=14)
- (9, 3, 4): +2,683 (n=8)
- (11, 3, 5): +2,663 (n=5)
- (9, 3, 5): +2,565 (n=2)
- (6, 3, 3): +2,293 (n=1)
- (10, 4, 6): +2,033 (n=11)
- (6, 3, 4): +1,192 (n=1)
- (11, 3, 6): +1,150 (n=5)
- (11, 4, 6): +642 (n=7)
- (8, 3, 5): +619 (n=5)
- (7, 3, 5): +619 (n=1)
- (10, 3, 4): +400 (n=5)
- (7, 3, 3): +395 (n=6)
- (12, 3, 5): -465 (n=2)

_Generated 2026-09-10 08:46. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 65 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=65); harvest_min=1–2 (n=65); wheat_tiles=0–5 (n=65); wheat_stock=0–19 (n=65); min_hands=3–4 (n=65); load_per_hand=12–23 (n=65); geese=0–1 (n=65); open_melons=4–12 (n=65)
- **Evidence:** 65 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 08:46. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._