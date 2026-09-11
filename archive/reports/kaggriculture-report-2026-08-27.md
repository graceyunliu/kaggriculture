# Kaggriculture Daily Report — 2026-08-27

## Sync summary

- Mine: 16 new episodes — submission-v2-reopened-provisional.zip (6), main_v11a_compact_livestock.py (10).
- Leaderboard (top 5 scouted teams, 10 new episodes each, 50 total): Crop Dusta (16714457), Ryo Hasegawa (16644287), Subramanya N (16705390), William Diment (16764431), Blu3s (16730065).

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | $17,519 | -$19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | $17,198 | -$22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | $12,102 | -$27,614 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | $27,687 | -$16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | $20,056 | -$17,532 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | $16,029 | -$38,293 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | $31,836 | -$31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | $30,931 | -$34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | $20,004 | -$53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | $25,197 | -$12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | $25,913 | -$30,258 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | $27,330 | -$22,675 |
| main_v11a_compact_livestock.py | 640.4 | 93 | 117 | 0 | $22,035 | -$32,221 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | $30,425 | -$36,078 |
| main_v3.py | 550.6 | 8 | 6 | 1 | $34,316 | -$37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | $27,198 | -$21,401 |
| main_v5.py | 556.8 | 14 | 12 | 1 | $19,641 | -$43,033 |
| main_v2.py | 564.2 | 4 | 4 | 0 | $27,302 | -$46,835 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | $9,724 | -$83,517 |
| submission-v2-reopened-provisional.zip | 497.6 | 74 | 91 | 0 | $15,928 | -$32,408 |

Note: `main_v11a_compact_livestock.py` (rejected in offline testing, per memory) has the largest sample (210 games) since it's the current live submission — matches the round-11 finding that it loses to v10.6 in controlled tests. `submission-v2-reopened-provisional.zip` is also currently live and shows the weakest live win rate (74/165, 44.8%) of any tracked version.

## Loss tags

- SHED_AT_CAP — 102 (only tag currently instrumented; every logged loss with a tag hit shed capacity).

Overall today's cumulative DB: 415 W / 431 L / 5 T across all tracked versions (all-time, not just today's new episodes).

## Top opponents in the data

Ranked by games logged against a seat of mine (leaderboard-scouted episodes are self-contained, i.e. don't include Grace's seat, so they don't surface here — see Notes).

| opponent | n | avg final money | wheat/carrot/tomato/strawberry/melon plant-mix | quad2_day | avg hires |
|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0.0 / 0.0 / 29.5 | 9.0 | 6.6 |
| Khoa Le | 4 | $70,224 | 92.75 / 0.0 / 0.0 / 18.25 / 21.25 | 0.0 | 10.2 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0.0 / 1.25 / 30.0 | 11.0 | 7.1 |
| pengshy | 3 | $81,135 | 42.3 / 2.7 / 0.0 / 34.0 / 28.7 | 9.0 | 8.9 |
| mchicen | 3 | $67,399 | 13.3 / 0.0 / 0.0 / 5.3 / 5.0 | 9.0 | 8.0 |

Sell totals for these 5 came back empty/near-zero (sells_json parsed to 0 units for the top-listed item in each case) — sample sizes are too small (3-4 games each) to read into it; flagging rather than reporting noise as signal. Round-trip buy/sell caveat applies if larger samples are pulled later.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py` (the round-10 clone-replica rebuild — per memory, already tested offline and decisively rejected, so absence from the ladder is expected/correct, not an oversight)

## Notes

- Auth via persisted token succeeded, no issues.
- Leaderboard-scouted episodes (the 50 just synced) have `my_seat = NULL` in the DB — they're pure opponent-vs-opponent/other-team matchups, not games involving Grace. This means the "top opponents" table above draws only from historical games where Grace had a seat; the 5 newly-scouted teams (Crop Dusta, Ryo Hasegawa, Subramanya N, William Diment, Blu3s) aren't represented in that head-to-head profile table today. Their replays are in the DB for separate strategy-mining if needed, just not surfaced via this join.
- Only one loss tag (`SHED_AT_CAP`) is currently instrumented in `harness.py` — consistent with memory's shed-capacity findings (10-animal service ceiling).
