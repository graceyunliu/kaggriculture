# Kaggriculture Daily Report — 2026-08-09

## Sync summary

New episodes downloaded today: **190** (30 mine, 160 opponent).

- mine — 30 new: `main_v11a_compact_livestock.py` 10, `main_v10.6_radius3.py` 10, `submission-v2-reopened-provisional.zip` 10
- leaderboard-Seb_(allegedly) (#2, 3206.7) — 40 new / 60 total
- leaderboard-HealthStone (#1, 3214.1) — 40 new / 50 total
- leaderboard-Elzandi_Irfan_Zikra (#3, 3163.6) — 30 new / 30 total
- leaderboard-brocade (#4, 3116.3) — 20 new / 20 total
- scout-16622198 = THUNDER THUNDER (#5, 3112.4) — 10 new / 10 total

All 190 ingested into `kaggriculture.db` (655 episode rows, 1310 profile rows total).

## My submissions

20 submissions on the ladder; 295 of my episodes have a recorded result. Margin = my final money − opponent final money.

| version | public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| submission-v2-reopened-provisional.zip | 556.0 | 5 | 5 | 0 | +7,303 | -14,157 |
| main_v11a_compact_livestock.py | 671.5 | 9 | 11 | 0 | +29,890 | -28,458 |
| main_v10.6_radius3.py | 657.4 | 10 | 10 | 0 | +32,908 | -30,382 |
| main_v10.5_siting.py | 681.5 | 7 | 9 | 0 | +37,305 | -13,466 |
| main_v9.10_hire_calibrated.py | 732.6 | 7 | 5 | 0 | +18,332 | -29,902 |
| main_v9.5_statehygiene.py | 720.8 | 5 | 2 | 0 | +9,643 | -39,980 |
| main_v9.3_fertilize.py | 755.8 | 5 | 3 | 0 | +27,964 | -11,822 |
| main_v9.2_parallel_build.py | 695.2 | 3 | 2 | 0 | +33,648 | -50,377 |
| main_v9.1_buyfeed_herd.py | 701.9 | 4 | 1 | 0 | +30,584 | -21,091 |
| turn_08_small_cow_fleet.py | 711.3 | 6 | 6 | 0 | +2,126 | -55,422 |
| main_v8.3.py | 684.2 | 11 | 12 | 1 | +30,181 | -32,018 |
| main_v8.2.py | 676.2 | 10 | 7 | 1 | +28,223 | -14,334 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |

Overall: **157 W / 133 L / 5 T** (54.1% W). All 295 result-bearing episodes mapped to a submission (0 unmapped).

Note: public score does not track local W/L — `main_v9.3_fertilize.py` holds the top public score (755.8) on 8 games; `main_v10.6_radius3.py` (657.4) is 10-10 on 20 games. Small per-version samples; don't rank versions off this table alone.

## Loss tags

- `SHED_AT_CAP` — 47 (only tag present in the DB across all 133 losses)

No other loss tag has ever been emitted; the tag vocabulary in `tags` is effectively single-valued, so this is a coverage limit as much as a finding — 86 of 133 losses carry no tag at all.

## Top opponents in the data

Ranked by games logged. Note: these are dominated by today's leaderboard scouting (Seb / HealthStone / Elzandi / THUNDER / brocade are the current top 5), so their profiles come mostly from their own games, not games against me.

Caveat on sell volumes: raw per-item sell units can be inflated by round-trip buy/sell activity inside a match (known engine artifact). FERTILIZER especially — treat absolute totals as directional only.

| opponent | games | avg final $ | wheat | carrot | tomato | strawberry | melon | quad2_day | avg hires |
|---|---|---|---|---|---|---|---|---|---|
| Seb (allegedly) | 77 | 87,086 | 24.0 | 0.1 | 0 | 41.2 | 21.1 | 4.1 | 10.1 |
| HealthStone | 58 | 85,622 | 134.0 | 1.7 | 0 | 33.1 | 15.2 | 6.0 | 9.2 |
| Elzandi Irfan Zikra | 35 | 86,934 | 144.0 | 0 | 0 | 39.0 | 15.9 | 6.0 | 9.3 |
| THUNDER THUNDER | 30 | 109,213 | 123.4 | 0 | 0 | 38.7 | 21.7 | 6.5 | 9.0 |
| brocade | 20 | 92,772 | 145.9 | 0 | 0 | 36.0 | 23.0 | 6.0 | 9.0 |

Notable sells (per game):

- **Seb (allegedly)** — FERTILIZER 314, STRAWBERRY 292, MILK 207. Only top-5 team that is *not* wheat-heavy (24 wheat plants/game vs 123-146 for the rest) and the only one taking quad2 early (day 4.1 vs 6.0-6.5). Highest hires (10.1).
- **HealthStone** — WHEAT 426, FERTILIZER 256, STRAWBERRY 230. #1 on the ladder yet lowest avg final money of the five; wheat-volume archetype.
- **Elzandi Irfan Zikra** — WHEAT 419, STRAWBERRY 302, FERTILIZER 251. Near-identical shape to brocade/THUNDER.
- **THUNDER THUNDER** — WHEAT 380, STRAWBERRY 293, FERTILIZER 244. Highest avg final money in the set (109k), and the highest WOOL (187/game) — most animal-revenue of the five.
- **brocade** — WHEAT 431, STRAWBERRY 277, FERTILIZER 235. Most wheat-concentrated (145.9 plants/game).

Pattern: 4 of the top 5 run the same wheat-volume + strawberry + ~9 hires + quad2-day-6 shape; Seb is the one structural outlier. TOMATO is 0 across all five; CARROT is ~0 for all but HealthStone (1.7).

Deviation from spec: step 7's query (`p.seat != e.my_seat`) excludes scouted episodes, where `my_seat` is NULL — it returns only opponents I've actually played (top hit had 3 games). Used `(e.my_seat IS NULL OR p.seat != e.my_seat)` instead so today's scouted teams are included. For reference, the strict-spec top 5 (my real ladder opponents, 2-3 games each): Ryan Hancock 90,141 avg / Khoa Le 69,314 / John Keith Weber 67,395 / zyvren 102,350 / vineet dairashri 87,140.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

(Objective file-vs-submission-list diff only; no claim about which should be submitted.)

## Notes

- Auth OK with the persisted token; no refresh needed.
- Sandbox had stale root-owned venvs at `/tmp/kagg_env` and `/tmp/kagg_env2` (unwritable). Provisioned a fresh 3.11 venv at a timestamped path instead. System python is 3.10, so 3.11 via `uv` was required.
- Background/nohup processes do not survive between shell calls in this sandbox (PID namespace is torn down with the parent). The first `leaderboard 5` run was killed mid-flight at team 4, which (a) left 3 truncated JSON files under `leaderboard-brocade` and (b) skipped `ingest()`, which only runs after all teams finish. Truncated files were re-downloaded (delete is not permitted in the mounted folder, so they were overwritten in place); all downloaded episodes were then ingested manually via `harness.py ingest`.
- Because `select_new()` takes the 10 most-recent *not-yet-downloaded* episodes, each re-invocation pulls a *further* 10 per team rather than being a no-op. Teams 1-4 were therefore hit twice (20 episodes each today, not 10). To avoid a third pass on teams 1-4 just to reach team 5, the last team (THUNDER THUNDER) was synced directly with `sync_replays.py scout 16622198 --max-episodes 10` — same cap, same ingest path, output lands in `Replays/Auto/scout-16622198/` rather than `leaderboard-THUNDER_THUNDER/`.
- 11 submitted versions have no file in the project root (`main_v11a_compact_livestock.py`, `main_v2.py`, `main_v2.1.py`, `main_v3.py`, `main_v5.py`, `main_v7.2.py`, `main_v7.5.py`, `main_v7.9.py`, `main_v8.py`, `main_v8.2.py`, `main_v9.5_statehygiene.py`). Verified: all 11 are present under `Archived versions/` — nothing is actually missing.
- 360 of 655 episode rows have `my_result = NULL` (scouted opponent-vs-opponent games); they contribute to opponent profiles but not to my W/L.
