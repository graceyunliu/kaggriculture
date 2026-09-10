# Evolution run 20260910-090435

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.18 h · candidates evaluated this run: 26 · games 1,654 (8,986/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 1 | 2 |
| dead_pattern | 8 | 16 |
| dead_smoke | 4 | 32 |
| alive | 12 | 1296 |
| held_fail | 1 | 308 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 181 · held-out evaluated: 7 · held-out PASS: 0

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
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |
| `ffbf75678458` | M2 | paired | **+59** | 0.1 | 10-10 | -27,551 | +2,170 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 22 (gap -4,389 -> final -18,581); days 20-27 drivers: sales_rev -21,759, work_turns -185, weeds_new +2, reversals +5. Hands 11 vs 11, animals 8 vs 11, plants 42 vs 47. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `89822c12eba2` | wide | crossover | +3,032 | 1.6 | 8-2 | -22,099 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→4, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ef9bb31c7a35` | c1 | mutate | +2,574 | 1.6 | 8-2 | -24,298 | alive | melon_floor 0→150, open_melons 8→10, open_wheat 7→3, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→102 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `961ab6fb4730` | M2 | mutate | +2,342 | 1.8 | 6-4 | -19,878 | alive | melon_floor 0→150, harvest_min 1→3, wheat_tiles 0→1, load_per_hand 20→21, open_melons 8→9, open_wheat 7→6, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ffbf75678458` | M2 | paired | +2,170 | 2.3 | 7-3 | -27,607 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `be39051210fb` | c1 | block_pair | +2,143 | 0.3 | 2-8 | -28,277 | alive | geese 0→1, open_melons 8→6 · blocks: sweep |
| `362ca8604fb4` | c1 | paired | +2,033 | 1.6 | 7-3 | -24,144 | alive | MAX_HANDS 14→13, SPREAD_W 1.25→1.0 |
| `926d7668ad53` | queue | mutate | +1,769 | 1.9 | 8-2 | -28,807 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→3, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4 |
| `7a0b60c391c7` | wide | mutate | +1,686 | 0.8 | 5-5 | -23,482 | alive | melon_floor 0→150, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=23
- M2: best +2,342 (`961ab6fb4730`), n=15
- c1: best +2,683 (`5fd05605827b`), n=34
- queue: best +4,836 (`7ec902ce836b`), n=55
- v312: best +1,192 (`038351a768ec`), n=27
- wide: best +3,032 (`89822c12eba2`), n=27

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +7,723 | 102 | 100 | 17 | 170 | 4.4 | 102: +1,114 (n=3), 85: +765 (n=4), 100: -1,551 (n=153), 110: -3,429 (n=3), 92: -4,998 (n=5), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +5,775 | 3 | 6 | 6 | 180 | 2.78 | 3: -604 (n=32), 6: -1,772 (n=136), 8: -1,921 (n=2), 5: -2,021 (n=7), 7: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,698 | 9 | 8 | 7 | 180 | 1.97 | 9: +212 (n=5), 11: -1,034 (n=8), 10: -1,061 (n=73), 8: -2,142 (n=89), 4: -4,132 (n=2), 5: -5,485 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +5,248 | 39 | 38 | 11 | 178 | 2.15 | 39: -108 (n=16), 32: -363 (n=3), 35: -552 (n=22), 34: -1,206 (n=53), 38: -2,282 (n=70), 41: -3,113 (n=2), 43: -3,218 (n=9), 46: -5,356 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,120 | 2 | 2 | 4 | 181 | 2.45 | 2: -1,351 (n=156), 1: -3,036 (n=19), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +4,977 | 58 | 92 | 20 | 170 | 5.72 | 58: +1,114 (n=3), 107: -415 (n=6), 124: -423 (n=5), 11: -1,573 (n=17), 92: -1,715 (n=127), 73: -1,731 (n=2), 150: -2,225 (n=6), 76: -3,783 (n=2), 102: -3,863 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +4,952 | 25 | 22 | 8 | 180 | 3.71 | 25: -638 (n=18), 13: -769 (n=16), 22: -1,582 (n=121), 18: -2,657 (n=13), 20: -2,751 (n=5), 24: -3,782 (n=3), 23: -5,591 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +4,676 | 2 | 3 | 3 | 181 | 1.54 | 2: -834 (n=15), 3: -1,397 (n=153), 4: -5,510 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +4,434 | 8 | 5 | 7 | 180 | 3.6 | 8: +469 (n=3), 4: -594 (n=2), 3: -1,468 (n=27), 5: -1,637 (n=138), 7: -2,330 (n=7), 0: -3,964 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +4,244 | 12 | 14 | 6 | 181 | 3.48 | 12: +13 (n=23), 13: -48 (n=8), 14: -1,839 (n=135), 11: -2,569 (n=3), 15: -3,228 (n=9), 16: -4,231 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,814 | frontier | frontier | 2 | 181 | 0.88 | frontier: -1,414 (n=170), v312: -5,227 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,714 | 0.45 | 0.25 | 8 | 180 | 4.02 | 0.45: -576 (n=7), 0.2: -662 (n=3), 0.15: -704 (n=2), 0.4: -1,091 (n=17), 0.25: -1,376 (n=129), 0.5: -3,672 (n=3), 0.35: -4,290 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| min_hands | +3,566 | 3 | 3 | 3 | 181 | 1.88 | 3: -1,580 (n=174), 5: -1,887 (n=4), 4: -5,146 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,479 | 0.45 | 0.55 | 7 | 180 | 3.07 | 0.45: -40 (n=13), 0.65: -520 (n=15), 0.6: -1,046 (n=4), 0.55: -1,644 (n=122), 0.5: -3,181 (n=22), 0.3: -3,518 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +3,245 | 14 | 17 | 7 | 180 | 3.63 | 14: -381 (n=2), 17: -1,323 (n=139), 18: -1,624 (n=6), 16: -1,682 (n=4), 15: -2,605 (n=11), 20: -3,626 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +3,205 | 2 | 2 | 3 | 181 | 1.85 | 2: -1,498 (n=172), 3: -4,270 (n=5), 1: -4,703 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +3,082 | 3 | 7 | 8 | 180 | 4.17 | 3: -629 (n=9), 4: -918 (n=29), 8: -1,640 (n=2), 7: -1,803 (n=133), 6: -2,337 (n=3), 10: -3,113 (n=2), 5: -3,711 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +2,784 | 17 | 19 | 6 | 181 | 2.65 | 17: +89 (n=20), 16: -1,065 (n=19), 19: -1,884 (n=110), 20: -2,012 (n=17), 14: -2,206 (n=5), 18: -2,695 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +2,605 | 19 | 17 | 8 | 180 | 2.77 | 19: -641 (n=52), 16: -679 (n=3), 18: -1,223 (n=9), 17: -1,942 (n=97), 22: -2,656 (n=7), 20: -3,144 (n=3), 14: -3,246 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +2,582 | 18 | 20 | 8 | 179 | 3.06 | 18: -293 (n=4), 19: -1,066 (n=33), 20: -1,600 (n=121), 22: -2,577 (n=3), 23: -2,636 (n=3), 21: -2,874 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=12)
- (7, 3, 4): +3,920 (n=17)
- (14, 3, 6): +3,066 (n=4)
- (7, 3, 3): +3,032 (n=9)
- (9, 3, 4): +2,683 (n=14)
- (11, 3, 5): +2,663 (n=11)
- (11, 3, 6): +2,574 (n=7)
- (9, 3, 5): +2,565 (n=4)
- (6, 3, 3): +2,293 (n=3)
- (15, 3, 6): +2,143 (n=1)
- (10, 4, 6): +2,033 (n=12)
- (12, 3, 4): +1,225 (n=2)
- (6, 3, 4): +1,192 (n=3)
- (10, 3, 5): +1,108 (n=5)
- (8, 4, 6): +744 (n=3)

_Generated 2026-09-10 09:15. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 96 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=96); harvest_min=1–2 (n=96); wheat_tiles=0–5 (n=96); wheat_stock=0–19 (n=96); min_hands=3–4 (n=96); load_per_hand=12–25 (n=96); geese=0–1 (n=96); open_melons=4–12 (n=96)
- **Evidence:** 96 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 09:15. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._