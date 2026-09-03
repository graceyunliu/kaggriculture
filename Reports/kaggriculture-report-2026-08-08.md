# Kaggriculture Daily Report — 2026-08-08

## Sync summary

- Mine: 32 new episodes downloaded (across main_v11a, main_v10.6_radius3, main_v10.5_siting, main_v9.10_hire_calibrated, main_v8.3 — all capped at 10/submission).
- Leaderboard: 50 new episodes downloaded, 10 each from 5 scouted teams: Seb (allegedly), HealthStone, tao wu11, Mohamed abdelrazik, kevin park.
- Both sync commands completed in a single pass (no timeouts, no retries needed).
- Total episodes in DB: 485 (265 with a `my_result`, i.e. involve graceyunliu; 220 are leaderboard-vs-leaderboard scouting games with no my_result).

## My submissions

Lifetime W/L/T and margins per submitted version (all history in DB, not just today):

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 5 | 3 | 0 | +27,964 | -11,822 |
| main_v9.10_hire_calibrated.py | 732.6 | 7 | 5 | 0 | +18,332 | -29,902 |
| main_v9.5_statehygiene.py | 720.8 | 5 | 2 | 0 | +9,643 | -39,981 |
| main_v9.2_parallel_build.py | 695.2 | 3 | 2 | 0 | +33,648 | -50,377 |
| main_v9.1_buyfeed_herd.py | 701.9 | 4 | 1 | 0 | +30,584 | -21,091 |
| turn_08_small_cow_fleet.py | 711.3 | 6 | 6 | 0 | +2,126 | -55,422 |
| main_v8.3.py | 684.2 | 11 | 12 | 1 | +30,181 | -32,018 |
| main_v10.5_siting.py | 681.5 | 7 | 9 | 0 | +37,305 | -13,466 |
| main_v10.6_radius3.py | 679.2 | 5 | 5 | 0 | +33,875 | -15,481 |
| main_v11a_compact_livestock.py | 676.4 | 5 | 5 | 0 | +20,998 | -14,341 |
| main_v8.2.py | 676.2 | 10 | 7 | 1 | +28,223 | -14,334 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,913 | -30,258 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,835 |

Today's 32 new mine-episodes only: **14 W / 17 L / 1 T**, split main_v10.5 (1W-5L), main_v10.6_radius3 (5W-5L), main_v11a (5W-5L), main_v8.3 (2W-1L-1T), main_v9.10 (1W-1L).

## Loss tags

Lifetime (117 losses total): `SHED_AT_CAP` — 40 occurrences (only tag present in the DB; no other loss-tag categories logged).

Today's 17 losses: `SHED_AT_CAP` — 9 occurrences.

## Top opponents in the data

Opponent pool is highly diverse (316 distinct names across 485 episodes) — no single name dominates. Top 5 by game count, all n=2-3:

**Ryan Hancock** (n=3) — avg final money $90,141. Plant mix: wheat 54.7, strawberry 7.0, melon 25.3, carrot/tomato 0. quad2_day 9.7, avg hires 8.0/day. Sells: WHEAT 1,017, MILK 593, FERTILIZER 570 (round-trip caveat applies to fertilizer/wheat volumes).

**Khoa Le** (n=3) — avg final money $69,314. Plant mix: wheat 94.7, strawberry 11.3, melon 19.3. quad2_day 0.0 (expands to quadrant 2 immediately/day-0). avg hires 10.4/day — highest of the five. Sells: WHEAT 850, MILK 692, FERTILIZER 579, WOOL 454.

**zyvren** (n=2) — avg final money $102,350, highest of the five. Plant mix: wheat 81.0, strawberry 23.5 (heaviest berry lean), melon 8.0. quad2_day 7.0, avg hires 10.1/day.

**vineet dairashri** (n=2) — avg final money $87,140. Most diversified crop mix: wheat 58.5, carrot 21.5, strawberry 35.5, melon 26.5. quad2_day 7.0, avg hires 9.6/day.

**maniginam** (n=2) — avg final money $72,664, lowest hires (3.9/day) and almost no planting (carrot 7.0 only). Sells: WHEAT 9,562 — extreme outlier, almost certainly round-trip buy/sell inflation rather than real production, given near-zero planting logged.

## Local versions not yet submitted

19 local `main_v*.py` files with no matching submission on the ladder:

main_v10.6a_radius3.py, main_v10.6b_radius6.py, main_v10.6c_radius2.py, main_v10.6d_radius1.py, main_v11b_berry_factory.py, main_v11c_marginal_roi.py, main_v11d_opponent_responsive.py, main_v12.1_freq_dist_ranking.py, main_v12.2_local_tour.py, main_v12.3_ev_land.py, main_v12.4_unified_ev.py, main_v12.5_predictive_throttle.py, main_v12.6_ev_land_plus_throttle.py, main_v12.7_local_economy.py, main_v13.1_wheat_cash_crop.py, main_v13.2_deprioritize_glass_cannons.py, main_v13.3_wheat_egg_combo.py, main_v13.4_goose_realistic_ev.py, main_v13.5_glut_aware_dynamic.py, main_v_clonereplica1.py.

## Notes

- Auth succeeded cleanly on first attempt (persisted token still valid).
- Both sync commands (`mine` and `leaderboard 5`) completed fully in one invocation each — no timeout/retry cycles needed today.
- 11 previously-submitted `fileName`s have no matching local file on disk: main_v2.1.py, main_v2.py, main_v3.py, main_v5.py, main_v7.2.py, main_v7.5.py, main_v7.9.py, main_v8.2.py, main_v8.py, main_v9.5_statehygiene.py, turn_08_small_cow_fleet.py — these are historical/early versions or externally-supplied variants, consistent with memory noting main_v9.5 lives under "Archived versions/" rather than the project root.
- Only one loss-tag category (`SHED_AT_CAP`) exists in the tags table at all — this isn't a "dominant" tag among several, it's the sole tag ever logged.
- Sell-unit totals should not be read as raw production volume; the engine allows round-trip buy/sell within a match that inflates totals (most visible in maniginam's 9,562 WHEAT sold against near-zero logged planting).
