# Evolution run 20260910-075324

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.65 h · candidates evaluated this run: 84 · games 5,958 (9,189/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 9 | 18 |
| dead_pattern | 10 | 20 |
| dead_smoke | 15 | 120 |
| alive | 48 | 5184 |
| held_fail | 2 | 616 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 84 · held-out evaluated: 4 · held-out PASS: 0

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
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |
| `362ca8604fb4` | c1 | paired | +2,033 | 1.6 | 7-3 | -24,144 | alive | MAX_HANDS 14→13, SPREAD_W 1.25→1.0 |
| `7a0b60c391c7` | wide | mutate | +1,686 | 0.8 | 5-5 | -23,482 | alive | melon_floor 0→150, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `a1c2b0acfbad` | wide | crossover | +1,312 | 0.6 | 4-6 | -23,295 | alive | melon_floor 0→100, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_cap 22→25, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `038351a768ec` | v312 | crossover | +1,192 | 0.7 | 7-3 | -19,705 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, demand_share 0.55→0.45, setup_capital_share 0.25→0.45, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4 |
| `842eaa9dcc6d` | v312 | crossover | +1,121 | 2.1 | 6-4 | -23,619 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→35 |
| `362753b71bee` | wide | paired | +722 | 1.1 | 6-4 | -21,955 | alive | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12 · blocks: hiring |
| `437ddb04ab9d` | c1 | paired | +642 | 0.5 | 5-5 | -22,313 | alive | wheat_stock 0→4, geese 0→1, open_melons 8→10, open_wheat 7→4, early_hire_days 5→8, wheat_per_animal 0.0→0.3, wheat_sell_price 30→26, wheat_hold_days 0→2, labor_reserve_buffer 92→107, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→1 · blocks: hiring |
| `772d75bd7670` | v312 | crossover | +619 | 0.6 | 4-6 | -18,337 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→2, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35 |
| `01813b5007fe` | queue | crossover | +619 | 0.4 | 4-6 | -26,416 | alive | min_hands 3→5, open_wheat 7→4, demand_share 0.55→0.65, wheat_cap 22→25, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→18, MAX_SHEEP 14→13 · blocks: hiring |
| `3d99fd8d1063` | wide | crossover | +495 | 0.5 | 6-4 | -21,802 | alive | melon_floor 0→100, open_melons 8→10, max_animals 17→18, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=11
- M2: best -3,630 (`f443671ed6df`), n=6
- c1: best +2,683 (`5fd05605827b`), n=15
- queue: best +4,836 (`7ec902ce836b`), n=28
- v312: best +1,192 (`038351a768ec`), n=11
- wide: best +1,686 (`7a0b60c391c7`), n=13

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| wheat_cap | +6,266 | 13 | 22 | 6 | 83 | 2.61 | 13: -114 (n=8), 25: -661 (n=5), 22: -1,619 (n=60), 18: -2,817 (n=7), 23: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +6,187 | 3 | 6 | 4 | 83 | 1.42 | 3: -192 (n=13), 6: -1,826 (n=67), 7: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,013 | 10 | 8 | 5 | 83 | 1.46 | 10: -603 (n=28), 8: -2,115 (n=51), 4: -4,132 (n=2), 5: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,656 | 12 | 14 | 6 | 82 | 2.56 | 12: +1,041 (n=4), 13: -1,184 (n=3), 14: -1,808 (n=73), 15: -4,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +5,200 | 100 | 100 | 8 | 79 | 1.85 | 100: -1,409 (n=75), 92: -4,461 (n=2), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +5,147 | 17 | 19 | 5 | 84 | 3.05 | 17: +1,368 (n=3), 16: +45 (n=4), 19: -1,727 (n=68), 20: -3,699 (n=6), 18: -3,779 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +4,959 | 11 | 14 | 4 | 84 | 2.48 | 11: -51 (n=2), 14: -1,467 (n=73), 12: -3,146 (n=3), 13: -5,011 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +4,496 | 25 | 30 | 5 | 84 | 2.04 | 25: -379 (n=14), 26: -1,634 (n=14), 30: -2,009 (n=51), 28: -2,105 (n=3), 36: -4,876 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,178 | 19 | 20 | 5 | 82 | 1.38 | 19: -833 (n=12), 20: -1,574 (n=65), 21: -5,012 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +3,994 | 2 | 3 | 3 | 84 | 1.54 | 2: -1,145 (n=6), 3: -1,463 (n=71), 4: -5,139 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +3,930 | 39 | 38 | 7 | 82 | 1.74 | 39: +565 (n=6), 34: -623 (n=20), 35: -727 (n=6), 38: -2,536 (n=45), 43: -3,365 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,599 | 0.4 | 0.25 | 6 | 82 | 1.88 | 0.4: -878 (n=11), 0.25: -1,467 (n=59), 0.35: -4,087 (n=10), 0.5: -4,477 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +3,536 | 1.0 | 1.25 | 4 | 83 | 1.82 | 1.0: -144 (n=2), 1.25: -1,681 (n=78), 1.5: -3,679 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,395 | 0.65 | 0.55 | 6 | 82 | 1.93 | 0.65: +194 (n=5), 0.45: +42 (n=3), 0.55: -1,602 (n=60), 0.5: -3,202 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,376 | frontier | frontier | 2 | 84 | 0.88 | frontier: -1,546 (n=79), v312: -4,921 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_RADIUS | +3,222 | 3 | 5 | 5 | 83 | 1.6 | 3: -1,363 (n=10), 5: -1,388 (n=54), 6: -2,915 (n=17), 4: -4,586 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +3,206 | 2 | 2 | 4 | 83 | 1.67 | 2: -1,447 (n=74), 1: -3,507 (n=7), 0: -4,652 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +2,667 | 5 | 5 | 6 | 82 | 2.32 | 5: -1,668 (n=68), 3: -1,722 (n=10), 7: -1,922 (n=2), 0: -4,334 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +2,663 | 2 | 2 | 3 | 84 | 1.79 | 2: -1,572 (n=78), 1: -3,592 (n=2), 3: -4,235 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +2,420 | 0.3 | 0.0 | 4 | 83 | 0.95 | 0.3: -944 (n=24), 0.0: -1,906 (n=54), 0.2: -3,364 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=5)
- (7, 3, 4): +3,920 (n=12)
- (9, 3, 4): +2,683 (n=5)
- (9, 3, 5): +2,565 (n=2)
- (6, 3, 3): +2,293 (n=1)
- (10, 4, 6): +2,033 (n=10)
- (6, 3, 4): +1,192 (n=1)
- (11, 3, 6): +1,121 (n=2)
- (11, 4, 6): +642 (n=5)
- (8, 3, 5): +619 (n=3)
- (7, 3, 5): +619 (n=1)
- (7, 3, 3): +395 (n=6)
- (12, 3, 5): -465 (n=2)
- (13, 3, 5): -468 (n=1)
- (13, 4, 6): -755 (n=2)

_Generated 2026-09-10 08:32. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 50 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–150 (n=50); harvest_min=1–2 (n=50); wheat_tiles=0–5 (n=50); wheat_stock=0–19 (n=50); min_hands=3–4 (n=50); load_per_hand=12–23 (n=50); geese=0–1 (n=50); open_melons=4–12 (n=50)
- **Evidence:** 50 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 08:32. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._