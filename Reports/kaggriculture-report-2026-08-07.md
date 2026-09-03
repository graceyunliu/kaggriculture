# Kaggriculture Daily Report — 2026-08-07

## Sync summary

- Mine: 63 new episodes ingested across 17 submissions (main_v2.py through main_v10.5_siting.py), each capped at 10 most recent.
- Leaderboard: 50 new episodes ingested across top-5 scouted teams: Wufang Hong, Seb (allegedly), ╰┈➤ˎˊ˗ www.sleepyai.org, venks, THUNDER THUNDER (10 each).
- Both sync commands completed cleanly on first attempt (no timeouts/retries needed).

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 5 | 3 | 0 | 27964 | -11822 |
| main_v9.10_hire_calibrated.py | 741.3 | 6 | 4 | 0 | 21384 | -17999 |
| main_v10.5_siting.py | 729.7 | 6 | 4 | 0 | 43511 | -16136 |
| main_v9.5_statehygiene.py | 720.8 | 5 | 2 | 0 | 9643 | -39980 |
| turn_08_small_cow_fleet.py | 711.3 | 6 | 6 | 0 | 2126 | -55422 |
| main_v9.1_buyfeed_herd.py | 701.9 | 4 | 1 | 0 | 30584 | -21091 |
| main_v9.2_parallel_build.py | 695.2 | 3 | 2 | 0 | 33648 | -50377 |
| main_v8.3.py | 684.2 | 9 | 11 | 0 | 31687 | -33055 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | 20004 | -53481 |
| main_v8.2.py | 676.2 | 10 | 7 | 1 | 28223 | -14334 |
| main_v8.py | 673.8 | 10 | 10 | 0 | 25912 | -30258 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | 30425 | -36078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | 27198 | -21401 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | 9724 | -83517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | 27302 | -46834 |
| main_v5.py | 556.8 | 14 | 12 | 1 | 19641 | -43033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | 34316 | -37710 |

Overall (all versions, all games in DB): 129 W / 100 L / 4 T.

## Loss tags

- SHED_AT_CAP: 31 losses (only tag currently logged — every tagged loss hit shed capacity).

## Top opponents in the data

### Ryan Hancock (3 games)

- Avg final money: 90141
- Plant mix (avg): wheat=54.7, carrot=0.0, tomato=0.0, strawberry=7.0, melon=25.3
- quad2_day avg: 9.666666666666666
- avg_hires avg: 7.98
- Notable sell totals: WHEAT=1017, MILK=593, FERTILIZER=570 (raw sell-unit totals can be inflated by round-trip buy/sell within a match — treat as directional, not literal production)

### Khoa Le (3 games)

- Avg final money: 69314
- Plant mix (avg): wheat=94.7, carrot=0.0, tomato=0.0, strawberry=11.3, melon=19.3
- quad2_day avg: 0.0
- avg_hires avg: 10.39
- Notable sell totals: WHEAT=850, MILK=692, FERTILIZER=579 (raw sell-unit totals can be inflated by round-trip buy/sell within a match — treat as directional, not literal production)

### zyvren (2 games)

- Avg final money: 102350
- Plant mix (avg): wheat=81.0, carrot=0.0, tomato=0.0, strawberry=23.5, melon=8.0
- quad2_day avg: 7.0
- avg_hires avg: 10.08
- Notable sell totals: WHEAT=783, WOOL=289, MILK=279 (raw sell-unit totals can be inflated by round-trip buy/sell within a match — treat as directional, not literal production)

### vineet dairashri (2 games)

- Avg final money: 87140
- Plant mix (avg): wheat=58.5, carrot=21.5, tomato=0.0, strawberry=35.5, melon=26.5
- quad2_day avg: 7.0
- avg_hires avg: 9.60
- Notable sell totals: WHEAT=697, FERTILIZER=423, MILK=313 (raw sell-unit totals can be inflated by round-trip buy/sell within a match — treat as directional, not literal production)

### maniginam (2 games)

- Avg final money: 72664
- Plant mix (avg): wheat=0.0, carrot=7.0, tomato=0.0, strawberry=0.0, melon=0.0
- quad2_day avg: 9.0
- avg_hires avg: 3.92
- Notable sell totals: WHEAT=9562, MILK=481, WOOL=302 (raw sell-unit totals can be inflated by round-trip buy/sell within a match — treat as directional, not literal production)

## Local versions not yet submitted

- main_v10.10_modest_coverage.py
- main_v10.11_melon_near.py
- main_v10.12_realloc.py
- main_v10.13_fert_reserve.py
- main_v10.14_no_se.py
- main_v10.15_bigger_fleet.py
- main_v10.16_concentrated_crops.py
- main_v10.17_concentrated_full.py
- main_v10.18_compact_hire4.py
- main_v10.19_no_carrot.py
- main_v10.1_carrot_boost.py
- main_v10.20_decoupled_animals.py
- main_v10.20b_decoupled_fleet14.py
- main_v10.21_goose.py
- main_v10.22_goose_floor.py
- main_v10.2_shop_aware_selling.py
- main_v10.3_fleet12.py
- main_v10.4_tomato_scale.py
- main_v10.6_radius3.py
- main_v10.6a_radius3.py
- main_v10.6b_radius6.py
- main_v10.6c_radius2.py
- main_v10.6d_radius1.py
- main_v10.7_three_tier.py
- main_v10.8_quad_scaled.py
- main_v10.9_distance_hire.py
- main_v10.py

Note: `main_v10.6_radius3.py` — the current standing champion per project memory — is in this list (never submitted to the live ladder).

## Notes

- Auth via persisted `.kaggle/access_token` worked without issue.
- All 427 real-ladder episodes mapped cleanly to a submission version (0 unmapped).
- Submissions with files no longer present in the project root (main_v2.py, v2.1, v3, v5, v7.2, v7.5, v7.9, v8.py, v8.2, v9.5_statehygiene.py, turn_08_small_cow_fleet.py) all still exist under `Archived versions/` — nothing is actually lost.
- Top-5 opponents by game count in the DB (Ryan Hancock, Khoa Le, zyvren, vineet dairashri, maniginam) only have 2-3 games each — small sample, treat profile averages as noisy.
- maniginam shows plant_wheat=0 but WHEAT sell total=9562 — likely round-trip buy/sell rather than real production; flagged per the known engine artifact.
