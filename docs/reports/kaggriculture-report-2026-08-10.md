# Kaggriculture Daily Report — 2026-08-10

## Sync summary

New replay files downloaded today: **187** (mine 30, leaderboard 157). Leaderboard sync needed 4 invocations (shell timeout kills long runs); the top-5 team set shifted between invocations, so more than 5 teams were scouted.

| source | team | new files |
|---|---|---|
| mine | graceyunliu (all submissions) | 30 |
| leaderboard | THUNDER THUNDER | 47 |
| leaderboard | Abracadabra | 36 |
| leaderboard | Ezzzzzekki | 30 |
| leaderboard | Valmorlee | 28 |
| leaderboard | Jince | 16 |

- Final leaderboard run completed cleanly with `Done. 50 new replay(s)`.
- DB grew 735 → **1152 episodes**. Only 187 of that came from today's downloads — a **backlog of ~230 previously-downloaded-but-never-ingested replays** was swept in by a manual `harness.py ingest` pass (417 ingested, 735 skipped). See Notes.
- Of my 30 new: all from `main_v10.6_radius3.py` (59 episodes total on ladder, 10 new capped) plus older submissions; every other submission returned 0 new.

## My submissions

497 episodes have `my_result`. Overall: **W 252 / L 240 / T 5** (51.2% win rate).

| version | public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v11a_compact_livestock.py | 665.5 | 12 | 18 | 0 | +32,743 | -26,710 |
| main_v10.6_radius3.py | 657.4 | 13 | 17 | 0 | +35,673 | -29,040 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| submission-v2-reopened-provisional.zip | 517.8 | 7 | 13 | 0 | +11,721 | -15,669 |

Observations (facts only, no ranking claim):

- `main_v11a_compact_livestock.py` is live on the ladder at 665.5 despite being rejected in local 10-seed testing (round 11, memory). It sits above `main_v10.6_radius3.py` (657.4) in public score.
- Highest public score is `main_v9.3_fertilize.py` (755.8), which is not the local champion.
- Public score and local-harness W/L are not aligned: v10.6 has the largest avg win margin (+35.7k) but the 2nd-lowest public score among v7+ submissions.
- Every episode resolved to a submission — 0 unmapped.

## Loss tags

Only one tag type exists in the DB.

- `SHED_AT_CAP` — 54 (of 240 losses; 940 instances DB-wide across all seats)

No other loss tags are emitted by the current `harness.py` tagger, so this breakdown is single-dimension and can't discriminate between loss modes.

## Top opponents in the data

The spec query (`p.seat != e.my_seat`) only matches episodes where `my_seat` is non-NULL; 655 of 1152 episodes are leaderboard-scouted with `my_seat` NULL, so that query returns only my head-to-head opponents (n=3–4 each). Both views below.

### A. Head-to-head opponents (spec query)

| opponent | n | avg final $ | wheat/carrot/tomato/straw/melon | quad2_day | avg hires | notable sells (per game) |
|---|---|---|---|---|---|---|
| Khoa Le | 4 | 70,224 | 92.8 / 0 / 0 / 18.3 / 21.3 | 0 | 10.16 | WHEAT 345, MILK 217, FERT 158 |
| islet | 3 | 106,912 | 82.7 / 0 / 0 / 32.7 / 20.3 | 7 | 9.77 | FERT 184, STRAWBERRY 170, MILK 136 |
| Syed Muhammad Gillani | 3 | 82,615 | 21 / 0 / 0 / 8 / 24.3 | 8.7 | 7.42 | WHEAT 1,867 ⚠, MILK 198, FERT 171 |
| Solve Langseth | 3 | 67,339 | 39 / 26.3 / 0 / 0 / 27.7 | 9 | 6.58 | MILK 2,480 ⚠, FERT 2,451 ⚠, MELON 2,433 ⚠ |
| Shuiys | 3 | 103,407 | 40.7 / 0 / 0 / 71.3 / 33.3 | 10.3 | 9.68 | FERT 562, MILK 482, STRAWBERRY 333 |

### B. Most-represented opponents overall (incl. scouted teams)

| opponent | n | avg final $ | wheat/carrot/tomato/straw/melon | quad2_day | avg hires | notable sells (per game) |
|---|---|---|---|---|---|---|
| Seb (allegedly) | 86 | 85,174 | 23.6 / 0.1 / 0 / 41.4 / 20.8 | 4.0 | 10.1 | FERT 314, STRAWBERRY 294, MILK 207 |
| THUNDER THUNDER | 77 | 99,222 | 136.2 / 0 / 0 / 36.4 / 20.2 | 6.2 | 9.1 | WHEAT 415, STRAWBERRY 276, FERT 258 |
| HealthStone | 66 | 87,275 | 133.3 / 2.3 / 0 / 33.1 / 15.4 | 6.0 | 9.2 | WHEAT 425, FERT 255, STRAWBERRY 231 |
| somewhere after | 60 | **131,730** | 66 / 0 / 0 / 44.0 / 21 | 7.0 | 10.1 | WHEAT 1,134 ⚠, STRAWBERRY 1,037 ⚠, MILK 970 ⚠ |
| J.M.Mubasshir Rahman | 48 | **135,289** | 65.0 / 0 / 0 / 44 / 21 | 7.0 | 10.1 | WHEAT 1,131 ⚠, MILK 864 ⚠, STRAWBERRY 788 ⚠ |
| CARLOS CAADA ROSTRO | 47 | **133,335** | 66 / 0 / 0 / 44 / 21 | 7.0 | 10.1 | WHEAT 1,108 ⚠, MILK 707, STRAWBERRY 634 |
| Ezzzzzekki | 41 | 84,252 | 142.6 / 0 / 0 / 36.6 / 19.2 | 6.0 | 8.8 | WHEAT 453, STRAWBERRY 282, FERT 240 |
| Valmorlee | 38 | 80,069 | 142.2 / 0 / 0 / 37.3 / 18.7 | 6.0 | 8.7 | WHEAT 441, STRAWBERRY 280, FERT 237 |

⚠ = raw sell-unit totals can be inflated by round-trip buy/sell activity inside the same match (known engine artifact). Do not read absolute sell volume as production volume without cross-checking.

Notes on the mix:

- `somewhere after` / `J.M.Mubasshir Rahman` / `CARLOS CAADA ROSTRO` have near-identical profiles (straw 44, melon 21, quad2_day 7.0, hires 10.1, FERT 445/game exactly) and all land at $131–135k — consistent with the shared-clone fingerprint already documented in `kaggriculture_opponent_strategy_identifiers.md`.
- The newly-scouted top-5 teams (THUNDER THUNDER, Ezzzzzekki, Valmorlee, Abracadabra, Jince) show a **different** profile: much heavier wheat (133–143 plant actions vs the clones' 65–66), fewer hires (8.7–9.2 vs 10.1), earlier quad2 (day 6 vs 7), and avg final money $80–99k — *below* the clone family's $131–135k despite ranking higher on the public leaderboard (3,116–3,215 vs my 657–756).
- Nobody in the data plants TOMATO. CARROT is near-zero for everyone except Solve Langseth.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

(Neutral fact: these files exist in the project root and do not appear in the submitted `fileName` set. No claim about merit.)

## Notes

- **Ingest backlog found.** After today's downloads the DB held 735 episodes against 1,152 replay files on disk. A manual `python3 harness.py ingest <files>` sweep ingested 417. `sync_replays.py`'s auto-ingest only covers replays it downloads in that same run — anything downloaded by a run that was killed mid-flight never lands in the DB. Worth checking whether prior scheduled runs left similar gaps.
- **10 corrupt replay JSONs** (truncated mid-file, from interrupted downloads) blocked ingest and were moved to `Replays/_corrupt/`. They will be re-downloaded by a future sync since they no longer occupy their `Replays/Auto/` paths. Affected: CARLOS_CAADA_ROSTRO ×2, J.M.Mubasshir_Rahman ×2, somewhere_after ×3, THUNDER_THUNDER ×1, Valmorlee ×1, mine ×1 (episode-90270324).
- **Shell timeout ceiling ~180s** in this environment. Long `sync_replays.py` runs had to be backgrounded with `setsid nohup` and polled; two runs were killed before reaching their ingest step (which caused part of the backlog above). The venv at `/tmp/kagg_env` from a prior run is owned by `nobody` and unusable — built a fresh one at `~/kenv_tmp/kagg` (Python 3.11.15).
- **Submitted-but-not-on-disk:** 11 submitted files have no local copy in the project root — `main_v11a_compact_livestock.py`, `main_v9.5_statehygiene.py`, `main_v8.py`, `main_v8.2.py`, `main_v7.9.py`, `main_v7.5.py`, `main_v7.2.py`, `main_v5.py`, `main_v3.py`, `main_v2.1.py`, `main_v2.py`. All 11 were located in `Archived versions/` (v11a also has a copy in `Chatgpt Agents/`) — none are actually missing, they just live outside the root, so step 8's root-only `ls main_v*.py` under-reports them.
- Leaderboard top-5 is volatile intra-day — the 5 teams returned changed between sync invocations (Seb/Elzandi in early attempts, THUNDER/Abracadabra/Ezzzzzekki/Valmorlee/Jince in the completed run).
- Competition standing: rank 2012 of 3686 teams, deadline 2026-09-30.
