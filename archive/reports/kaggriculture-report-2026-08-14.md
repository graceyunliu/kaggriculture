# Kaggriculture Daily Report — 2026-08-14

## Sync summary

- Mine: 20 new episodes ingested (all 18 older submissions returned 0 new; new games came from the two currently-active submissions).
  - `submission-v2-reopened-provisional.zip` — 10 new
  - `main_v11a_compact_livestock.py` — 10 new
- Leaderboard scout (top 5, cap 10 each): 50 new episodes.
  - カワシギ (team 16677252, LB 3261.9) — 10
  - researchstudio.site (16676904, 3115.1) — 10
  - Ueddy (16623451, 3114.7) — 10
  - Utkarsh #2 (16696304, 3090.4) — 10
  - somewhere after (16658931, 3088.7) — 10
- Today's new mine episodes: **7W / 13L**, avg win margin +$19,803, avg loss margin −$48,474.

## My submissions

All-time, per submission version, from the DB (606 scored episodes, 691 episode ids mapped from 20 submissions; 0 unmapped).

| version | public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | −19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | −22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | −27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | −38,293 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | −17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | −16,062 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | −31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | −34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | −53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | −12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | −30,258 |
| main_v11a_compact_livestock.py | 673.7 | 31 | 39 | 0 | +25,931 | −35,298 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | −22,675 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | −36,078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | −21,401 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | −83,517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | −46,834 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | −43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | −37,710 |
| submission-v2-reopened-provisional.zip | 508.7 | 24 | 36 | 0 | +17,155 | −30,608 |

Overall: **303 W / 298 L / 5 T**.

- Note: `main_v11a_compact_livestock.py` is live on the ladder (673.7, 31-39) despite the offline round-11 rejection recorded in memory; its offline test was against v10.5/opp_v14, not the live field.
- `main_v10.6_radius3.py` (offline champion) sits at 657.4 — lower public score than v9.3/v9.10 despite the offline edge; ladder score and head-to-head margin continue to diverge.

## Loss tags

- `SHED_AT_CAP` — 76 (only tag present across all logged losses)

## Top opponents in the data

Ranked by games logged vs. me. Caveat: sell-unit totals can be inflated by same-match round-trip buy/sell activity (engine artifact) — Solve Langseth's ~9-10k unit totals are almost certainly this, not real production.

| opponent | games | avg final $ | wheat | carrot | tomato | straw | melon | quad2_day | avg hires |
|---|---|---|---|---|---|---|---|---|---|
| Solve Langseth | 4 | 67,020 | 39.5 | 26.5 | 0 | 0 | 29.5 | 9.0 | 6.6 |
| Khoa Le | 4 | 70,224 | 92.8 | 0 | 0 | 18.2 | 21.2 | 0 | 10.2 |
| Darshan Makwana | 4 | 95,656 | 93.0 | 2.0 | 0 | 1.2 | 30.0 | 11.0 | 7.1 |
| islet | 3 | 106,912 | 82.7 | 0 | 0 | 32.7 | 20.3 | 7.0 | 9.8 |
| Yermak Petro | 3 | 15,681 | 68.0 | 58.7 | 0 | 2.7 | 17.7 | 11.0 | 8.0 |

Notable sell totals:

- Solve Langseth — MILK 9,920 / FERTILIZER 9,804 / MELON 9,784. Extreme; round-trip artifact, disregard absolute level.
- Khoa Le — WHEAT 1,380 / MILK 867 / FERTILIZER 630. Wheat-dominant, no quad2 expansion (quad2_day 0), highest hire rate of the group (10.2).
- Darshan Makwana — FERTILIZER 1,237 / WOOL 729 / MILK 576. Wheat+melon planting, near-zero berry/tomato.
- islet — FERTILIZER 551 / STRAWBERRY 510 / MILK 409. Highest avg money (106.9k) and the only one with real strawberry volume; heaviest wheat+straw mix, 9.8 hires.
- Yermak Petro — CARROT 359 / WHEAT 342 / MELON 210. Carrot-heavy, lowest money by far (15.7k).

Pattern: the three highest-money opponents (islet, Darshan, Khoa) all run wheat-dominant (83-93 plant actions) with 7-10 avg hires. Tomato is 0 across all five.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

## Notes

- Submitted historically but no longer on disk in the project root: `main_v11a_compact_livestock.py`, `main_v9.5_statehygiene.py`, `main_v2.py`, `main_v2.1.py`, `main_v3.py`, `main_v5.py`, `main_v7.2.py`, `main_v7.5.py`, `main_v7.9.py`, `main_v8.py`, `main_v8.2.py`. Several of these live under `Archived versions/`; the step-8 check only globs the root.
- Env: the sandbox's pre-existing `/tmp/kagg_env` and `/tmp/kagg_env2` venvs are unusable this session (permission-denied on their interpreters, left over from a prior run and not removable). Built a fresh 3.11 venv at `~/kagg_env` instead; `sync_replays.py` shells out to a bare `kaggle`, so `PATH` must include `~/kagg_env/bin` or the leaderboard command fails with `FileNotFoundError: 'kaggle'`.
- Auth via the persisted `.kaggle/access_token` succeeded, no re-issue needed.
- Both sync commands completed with a `Done.` line on the first (leaderboard: second) attempt; no timeouts, no retries needed.
- Loss-tag data remains single-tag (`SHED_AT_CAP`, 76) — the tagger appears to emit only this one tag, so the breakdown carries no discriminating signal.
