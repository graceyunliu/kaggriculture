# Kaggriculture Daily Report — 2026-09-09

## Sync summary
- Auth OK (persisted token). Sandbox `/sessions` volume was 100% full → venv/cache/HOME relocated to `/tmp`; reused an existing Python 3.11 `kaggle` venv there.
- New replay files downloaded today: **383** (256 mine, 127 leaderboard).
- Leaderboard scouting (top 5 live): SpaTaro 30, Otter Vibe 30, Himanshu Kumar 30, pensukesan 23, kanno 14 (+1 truncated, see Notes).
- Mine: new episodes for O9_O8_ENDGAME (39 eps, drained), O8_PURE_ANIMAL_THROTTLE (44, drained), M2_ADAPTIVE_OPENING (511), H32-submission (495), M4_TURN_ABLATION, submission-v2-reopened-provisional (180) — `mine` completed with `Done.`; leaderboard sync hit the 165 s/command cap 3× (10/team/pass), never reached its own `Done.`.
- Ingest: `sync_replays.py` only ingests at end-of-run, so timed-out passes leave files un-ingested. Ran `harness.py ingest` manually on every Replays/Auto file missing from the DB: **1,330 ingested** (343 from today's downloads + ~987 backlog from earlier timed-out syncs). DB now 4,929 episodes (2,518 with my_result).
- Today's ingested own-games: W 91 / L 125 (M2 17-43, H32 22-36, O8 24-20, O9 20-19, M4 8-7).

## My submissions
Live public scores from Kaggle; W/L/T and margins are over all replays in the DB for that submission (not just today's). 48 submissions total.

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| O9_O8_ENDGAME.zip | 862.5 | 20 | 19 | 0 | 21,805 | -13,418 |
| O8_PURE_ANIMAL_THROTTLE.zip | 883.9 | 24 | 20 | 0 | 23,150 | -9,170 |
| O4_PRODUCTIVE_SERVICE.zip | 870.9 | 19 | 20 | 0 | 18,991 | -14,493 |
| V3_15_WEED_FEED_C1OPEN.zip | 783.0 | 20 | 24 | 0 | 18,157 | -18,540 |
| M4_TURN_ABLATION.zip | 1576.4 | 66 | 16 | 0 | 28,401 | -11,006 |
| M2_ADAPTIVE_OPENING.zip | 1665.8 | 112 | 141 | 0 | 53,540 | -6,778 |
| H32-submission.zip | 1692.1 | 116 | 163 | 0 | 10,611 | -5,086 |
| H31_M75_GUARDED_FULL_TAPE.zip | 1854.9 | 35 | 16 | 0 | 20,441 | -7,936 |
| P5_PLANNER_CONFIRMED.zip | 875.4 | 23 | 16 | 0 | 21,313 | -17,359 |
| A65AA_TAPE_HYBRID.zip | 842.2 | 9 | 10 | 1 | 16,196 | -14,196 |
| H12_H10_PLUS_GUARD.zip | 1100.9 | 38 | 29 | 0 | 19,643 | -14,776 |
| H11_TAPE_HYBRID_GUARDED.zip | 1031.9 | 34 | 33 | 0 | 23,122 | -13,526 |
| H10_TAPE_HYBRID.zip | 1209.0 | 36 | 28 | 0 | 20,087 | -18,839 |
| V3_29_CAPITAL_PACED_HERD.zip | 846.9 | 16 | 14 | 0 | 17,570 | -11,607 |
| V3_12_REAL_ENGINE.zip | 852.5 | 21 | 19 | 0 | 14,786 | -16,199 |
| V3_11_LADDER_TUNED.zip | 835.5 | 22 | 18 | 0 | 31,670 | -17,948 |
| V3_10_MELON_FIRST_OPENING.zip | 829.7 | 22 | 19 | 0 | 28,029 | -19,227 |
| V3_9_LABOR_MODEL.zip | 784.8 | 16 | 16 | 1 | 28,124 | -18,640 |
| V3_9_SCENARIO_V14_CHALLENGER.zip | 774.5 | 22 | 23 | 0 | 24,023 | -23,543 |
| V3_7_DUTY_AWARE_LAND_ACTIVATION_EXPERIMENTAL.zip | 599.9 | 15 | 13 | 0 | 21,910 | -14,408 |
| V3_4_CENTER_PASTURE_CHALLENGER.zip | 632.7 | 19 | 16 | 0 | 23,103 | -28,406 |
| V2_8D_CENTER_PASTURE_CHALLENGER.zip | 616.4 | 18 | 17 | 0 | 20,666 | -34,794 |
| V3_4_INTERIM_CHAMPION.zip | 615.8 | 17 | 15 | 0 | 26,090 | -23,796 |
| V2_2_CARROT_9_CHALLENGER.zip | 460.6 | 19 | 20 | 0 | 13,914 | -19,308 |
| V2_1_MINIMAL_SCENARIO_CHALLENGER_CLEAN.zip | 458.4 | 12 | 15 | 1 | 8,018 | -31,157 |
| v2_1_minimal_scenario_challenger.zip | 425.3 | 11 | 14 | 1 | 12,934 | -17,664 |
| v2_1_experimental_ladder.zip | 448.7 | 11 | 15 | 0 | 11,329 | -35,449 |
| main_v9.3_fertilize.py | 755.8 | 31 | 24 | 0 | 17,041 | -16,767 |
| submission-v2-reopened-provisional.zip | 489.3 | 81 | 99 | 0 | 15,431 | -32,113 |
| main_v11a_compact_livestock.py | 634.7 | 124 | 145 | 0 | 20,549 | -30,769 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | 27,330 | -22,675 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | 30,931 | -34,082 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | 17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | 12,102 | -27,614 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | 27,686 | -16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | 20,056 | -17,532 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | 16,029 | -38,293 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | 31,836 | -31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | 25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | 25,912 | -30,258 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | 30,425 | -36,078 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | 20,004 | -53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | 9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | 19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | 34,316 | -37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | 27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | 27,302 | -46,834 |


[('LOSS', 1248), ('TIE', 9), ('WIN', 1261)]

Totals (DB, all own-result episodes): **W 1,261 / L 1,248 / T 9**.

## Loss tags
- SHED_AT_CAP: 623 (all-time losses) — the only tag present; 97 of today's 125 losses carry it.

## Top opponents in the data
Counted by games logged against Grace's seat (ladder opponents; scouted-leaderboard replays have no `my_seat` and so don't appear here). Raw sell-unit totals can be inflated by same-match buy/sell round-trips (engine artifact) — WHEAT/FERTILIZER totals below are the usual suspects.

- **ALLAI** (n=7): avg final money $81,163; plant mix wheat 189.3 / carrot 6.9 / tomato 0.0 / strawberry 36.6 / melon 12.0; quad2_day 6.0 (7/7 expanded); avg hires/day 9.64; top sells: WHEAT 2,832, FERTILIZER 2,374, STRAWBERRY 2,090
- **Timass** (n=5): avg final money $44,710; plant mix wheat 186.0 / carrot 9.0 / tomato 0.0 / strawberry 32.8 / melon 12.0; quad2_day 6.0 (4/5 expanded); avg hires/day 7.57; top sells: STRAWBERRY 5,915, WOOL 4,687, MILK 4,434
- **Rotation Theory** (n=5): avg final money $80,538; plant mix wheat 187.0 / carrot 6.0 / tomato 0.0 / strawberry 38.0 / melon 12.0; quad2_day 6.0 (5/5 expanded); avg hires/day 9.70; top sells: WHEAT 1,989, FERTILIZER 1,635, STRAWBERRY 1,342
- **Revanth Tambisetty** (n=5): avg final money $52,532; plant mix wheat 169.2 / carrot 7.2 / tomato 0.0 / strawberry 26.4 / melon 18.8; quad2_day 6.0 (3/5 expanded); avg hires/day 7.05; top sells: FERTILIZER 1,841, WHEAT 1,685, STRAWBERRY 1,034
- **John Keith Weber** (n=5): avg final money $82,905; plant mix wheat 87.0 / carrot 23.6 / tomato 0.0 / strawberry 37.0 / melon 13.4; quad2_day 8.2 (5/5 expanded); avg hires/day 8.90; top sells: STRAWBERRY 2,808, WHEAT 2,704, FERTILIZER 2,570

## Local versions not yet submitted
none (no `main_v*.py` files remain in the project root; see Notes).

## Evolution loop
`evolve/refresh_frontier.py` — 90 recent scouted games, 19 opening clusters (min share 10%):

| share | n | mean $ | status | opening fingerprint | teams |
|---:|---:|---:|---|---|---|
| 13% | 12 | 96,184 | **NEW** | BUYWH13 SELWH13 BUYWH13 \| SELWH13 BUYWH5 HIR×5 | Himanshu Kumar, pensukesan |
| 13% | 12 | 100,432 | known | HIR×3 BUYSH2 BUYCO2 BUYME1 BUYWH1 BUYWH5 \| BUYSH1 HIR | get some fries, kwa |
| 7% | 6 | 87,765 | known | BUYWH30 \| SELWH25 BUYCO2 HIR×5 | Andrey Tikhomirov |
| 7% | 6 | 100,480 | known | BUYCO2 \| HIR×5 BUYSH1 | Jesse Bullard |
| 7% | 6 | 108,556 | minor | BUYWH13 \| SELWH8 BUYWH7 HIR×5 BUYCO2 BUYSH2 | Matthew Huang |
| 7% | 6 | 92,993 | known | BUYWH13 \| SELWH9 BUYWH7 BUYME12 HIR×5 BUYCO2 | Mengfei Li |
| 7% | 6 | 102,204 | known | BUYWH5 \| HIR×5 BUYWH7 BUYME12 BUYCO2 BUYSH2 | MtN |
| 7% | 6 | 114,271 | minor | HIR×5 BUYSH2 BUYWH5 BUYGO2 BUYCO1 BUYME6 \| … | Otter Vibe |
| 7% | 6 | 89,447 | known | HIR×7 BUYCO5 BUYSH1 BUYME1 \| BUYWH18 | binghua |
| 7% | 6 | 106,312 | minor | BUYWH13 BUYWH60 SELWH60 \| SELWH13 BUYWH5 HIR×5 | kanno |
| 7% | 6 | 91,807 | known | BUYWH95 SELWH90 HIR×4 BUYCO2 BUYSH2 BUYWH9 BUYME5 | ymg_aq |
| 6% | 5 | 102,451 | known | \| BUYWH1 BUYWH7 BUYME12 HIR×5 BUYCO2 BUYSH2 | OceanMix |
| 1%×7 | 1 each | 48k–108k | minor | SpaTaro variants (HIR×4 BUYME7 BUYWH7 …), 1 OceanMix | SpaTaro |

- Frontier tape: `Opponents/frontier.txt` → **`Opponents/tape_kwa_105860490.py`** (was `tape_mtn_105853290.py`; cluster mean $100,432).
- NEW tape built: `Opponents/tape_pensukesan_107199477.py` (wheat round-trip opening, Himanshu Kumar / pensukesan cluster).
- Push: **succeeded** to branch `main` (`tapes.json` updated, `frontier.txt` updated, new tape created). Note `gh_push.py`'s default branch is still `master`, which no longer exists on GitHub → first push 404'd; re-ran with `-b main`.
- Air results fetched from `results` branch: run `20260909-113455` (generated 2026-09-09T13:35), frontier opponent `candidates/H32.py`, clone `tape_jessebullard_105876759.py`, 2.00 h, 1,280 candidates, 22,894 games (11,442/h). Counts: alive 417, dead_pattern 205, dead_smoke 192, noop 466.

Reference points (verbatim):

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | -37,097 | -9.3 | 0-10 | -27,047 | — | — | —-— |

Held-out results (verbatim): "None reached held-out this run."

Islands (verbatim):
- H32: best -15,269 (`0c3989f7d742`), n=2112
- M2: best -16,102 (`8b77b3e994bc`), n=2196
- c1: best -16,310 (`23734cef4da1`), n=2963
- queue: best -15,412 (`fe4745b56024`), n=3938
- v312: best -15,275 (`52b3d5cc236e`), n=2741
- wide: best -16,047 (`512e53fe15bc`), n=2599

- `archive.json` `held_out`: empty → nothing beats C1 on the held-out yardstick. Best dev-margin candidate `0c3989f7d742` (H32 island) is -15,269 vs H32 frontier (2-8), i.e. ~+21.8k better than C1's -37,097 on dev only — dev-only, seed-fit risk, not a held-out result.

## Notes
- Sandbox `/sessions` disk 100% full (other sessions' dirs) — worked around via `/tmp`; not a project issue.
- Bash tool capped commands at ~165–178 s regardless of requested timeout; each `sync_replays.py` pass downloads ~45–50 episodes before being killed. `mine` finished with `Done.` on pass 6; `leaderboard` never did (3 passes × 50). Both idempotent; next run picks up the rest.
- `sync_replays.py` `--max-episodes 10` caps per pass, not per submission lifetime: each re-run pulls the *next* 10 unseen episodes (M2/H32 have ~500 each, so they keep yielding 10/pass).
- 3 truncated downloads (killed mid-write, invalid JSON) renamed `*.json.truncated` so the next sync re-fetches them: mine/episode-91406493, mine/episode-105488061, leaderboard-kanno/episode-107201289.
- 1 replay fails `harness.py extract` with `KeyError: 0` at line 95 (`order[0]` on a market order that is a dict, not a list): `Replays/Auto/mine/episode-98950706-replay.json`. Not ingested; harness.py left untouched.
- `main_v9.3_fertilize.py` was submitted twice (refs 55308727 score 755.8 and 55832516 score 671.8); the table row shows the first ref's score, W/L merged.
- 20 historically-submitted `.py` files no longer exist in the project root (main_v2…main_v11a, turn_08_small_cow_fleet.py) — presumably moved to `archive/`; the "not yet submitted" check is therefore vacuous.
- Top-5 "opponents" query returns ladder opponents only (n=5–7 each); scouted teams have `my_seat` NULL and are excluded by `p.seat != e.my_seat`.
- `evolve/gh_push.py` BRANCH constant = `master` (deleted); Air's supervisor should be confirmed to pull `main`. Its latest report says frontier opponent = `candidates/H32.py`, not the tape in `frontier.txt`.
