# Kaggriculture Daily Report — 2026-08-19

## Sync summary
- Mine: 20 new episodes ingested (skipped 0 already-known), spanning submission-v2-reopened-provisional.zip and main_v11a_compact_livestock.py (10 each, capped); all other submissions already fully synced (0 new).
- Leaderboard: 50 new episodes ingested across 5 scouted teams (10 each, capped): tetsuya, Ryo Hasegawa, カワシギ, Arman Tuganbaev, ReCurSiON.
- Both syncs completed in a single pass, no timeouts/retries needed.

## My submissions
(W/L/T and margins are cumulative across all episodes in the DB for that version, not just today's new ones.)

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v11a_compact_livestock.py | 656.7 | 56 | 64 | 0 | +20,649 | -35,049 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| submission-v2-reopened-provisional.zip | 504.0 | 48 | 62 | 0 | +15,833 | -29,253 |

Overall DB totals: **W352 / L349 / T5**.

## Loss tags
- SHED_AT_CAP: 85 (the only tag currently logged — every tagged loss in the DB hits this cause)

## Top opponents in the data
1. **Solve Langseth** (n=4): avg final money $67,020. Plant mix — wheat 39.5, carrot 26.5, tomato 0, strawberry 0, melon 29.5. quad2_day 9.0, avg hires/day 6.59. Top sells: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 / CARROT 9,355 units — these totals look extreme relative to game scale and are almost certainly inflated by round-trip buy/sell activity, not net production.
2. **Khoa Le** (n=4): avg final money $70,224. Plant mix — wheat 92.75 (wheat-heavy), strawberry 18.25, melon 21.25, no carrot/tomato. quad2_day 0 (very early quad2 expansion). Avg hires/day 10.16 (highest of the five). Top sells: WHEAT 1,380 / MILK 867 / FERTILIZER 630 / MELON 483.
3. **Darshan Makwana** (n=4): avg final money $95,656 — highest of the five. Plant mix — wheat 93.0, melon 30.0, minimal carrot/strawberry. quad2_day 11.0 (latest expansion), avg hires/day 7.07. Top sells: FERTILIZER 1,237 / WOOL 729 / MILK 576 / MELON 502.
4. **pengshy** (n=3): avg final money $81,135. Plant mix — wheat 42.3, strawberry 34.0, melon 28.7. quad2_day 9.0, avg hires/day 8.94. Top sells: WHEAT 2,328 / MILK 586 / FERTILIZER 578 / MELON 445.
5. **mchicen** (n=3): avg final money $67,399 — lowest of the five. Plant mix is sparse overall (wheat 13.3, strawberry 5.3, melon 5.0). quad2_day 9.0, avg hires/day 8.0. Top sells: FERTILIZER 953 / MILK 693 / WOOL 333 / EGG 208.

Note: raw sell-unit totals (especially Solve Langseth's) can be inflated by round-trip buy/sell activity within a match — treat as directional, not literal production volume.

## Local versions not yet submitted
- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

## Notes
- Auth via persisted token worked without issue; no token refresh needed.
- Both sync commands completed in one shot — no retry loop was required.
- Loss-tag coverage is thin (only SHED_AT_CAP appears at all, 85 instances) — most losses in the DB carry no tag, so this breakdown covers a minority of the 349 total losses.
- The two unsubmitted local files (v10.6a, clonereplica1) both relate to work noted in memory as rejected/inconclusive experiments (per project history) — listed here as a neutral fact only, not a recommendation to submit.
