# Kaggriculture Daily Report — 2026-08-15

## Sync summary
- Mine: 20 new episodes — 10 for `submission-v2-reopened-provisional.zip`, 10 for `main_v11a_compact_livestock.py`. All other submissions already fully synced (0 new, capped at 10).
- Leaderboard: 50 new episodes across 5 scouted top teams (10 each): カワシギ (16677252), Thomas Tschinkel (16719123), Utkarsh #2 (16696304), Kostiantyn Isaienkov (16712189), Ueddy (16623451).
- Total new: 70 episodes, all ingested cleanly on first attempt (no timeouts/retries needed).

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v11a_compact_livestock.py | 682.5 | 38 | 42 | 0 | +24,117 | -33,597 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v10.6_radius3.py (champion) | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| submission-v2-reopened-provisional.zip | 504.0 | 29 | 41 | 0 | +17,049 | -31,708 |

Overall across all DB episodes with a decided result: 315 W / 306 L / 5 T.

Note: `main_v11a_compact_livestock.py` is on the ladder (score 682.5) but per repo memory was one of 4 round-11 candidates REJECTED in local seeded testing (0/40 wins vs v10.5/opp_scenario_v14) — the live W/L above reflects broader ladder matchmaking, not the local test harness result.

## Loss tags
- SHED_AT_CAP: 76 (only tag present in current data — every logged loss with a tag hit shed capacity)

## Top opponents in the data

| name | n games | avg final money | wheat/carrot/tomato/strawberry/melon (avg plantings) | quad2_day | avg hires |
|---|---|---|---|---|---|---|
| islet | 3 | $106,912 | 82.7 / 0 / 0 / 32.7 / 20.3 | 7.0 | 9.8 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0 / 1.2 / 30.0 | 11.0 | 7.1 |
| pengshy | 3 | $81,135 | 42.3 / 2.7 / 0 / 34.0 / 28.7 | 9.0 | 8.9 |
| Khoa Le | 4 | $70,224 | 92.8 / 0 / 0 / 18.2 / 21.2 | 0.0 | 10.2 |
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9.0 | 6.6 |

Notable sell totals (units, summed):
- islet: FERTILIZER 551, STRAWBERRY 510, MILK 409 — believable production-scale volumes.
- Darshan Makwana: FERTILIZER 1,237, WOOL 729, MILK 576 — plausible.
- Solve Langseth: MILK 9,920, FERTILIZER 9,804, MELON 9,784, CARROT 9,355, WHEAT 9,212 — all five items in the ~9,200-9,900 range strongly suggests round-trip buy/sell inflation, not real production; treat as non-representative of actual output.

Common pattern across the top 5: none plant TOMATO at all, and only Solve Langseth and Darshan Makwana touch CARROT meaningfully — WHEAT and MELON dominate the mix, consistent with prior memory findings on demand-side economics (MELON has thin demand but gets planted anyway; STRAWBERRY shows up in 3/5 profiles as a secondary earner).

## Local versions not yet submitted
- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

(Both exist on disk under the project root but have no matching `fileName` in the live submissions list.)

## Notes
- Auth, sync, and both API calls (submissions/episodes) all succeeded without retries.
- `sells_json` in the profiles table is a nested dict (`{"ITEM": {"units": N, "orders": N, "first_day": D, "last_day": D}}`), not a flat unit count — parsed accordingly for this report.
- Only one loss tag (SHED_AT_CAP) currently populated in the tags table; no other tag types have fired in logged losses to date.
