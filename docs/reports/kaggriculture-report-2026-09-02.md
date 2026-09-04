# Kaggriculture Daily Report — 2026-09-02

## Sync summary
- Mine: 241 new episodes downloaded + ingested across 8 submissions (V3_9 44 eps total/all new pulled over 3 runs; V3_7, V3_4_CENTER, V2_8D, V3_4_INTERIM, V2_2, V2_1_CLEAN, main_v11a). Note: `--max-episodes 10` caps per *run*; three back-to-back runs (needed for shell timeouts) each pulled the next-10-newest unseen, so more than 10/sub landed.
- Leaderboard (top 5 today): 10 each for Yuan800 (2950.4), Crop Dusta (2923.6), icelemon2004 (2919.9), curiosity (2907.4), Atakan Aldemir (2877.7) = 50, all ingested.
- Backlog: 636 replay files on disk were never in the DB (Aug 29 timeouts + earlier); 630 ingested now. DB episodes 2548 → 3178. 6 unrecoverable (see Notes).

## My submissions
Live public score from Kaggle; W/L/T and margins from all DB episodes mapped to each submission.

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| V3_9_SCENARIO_V14_CHALLENGER.zip | 779.0 | 22 | 22 | 0 | +24,023 | -22,913 |
| main_v9.3_fertilize.py (2 subs: 755.8 / 671.8) | 755.8 | 31 | 24 | 0 | +17,041 | -16,767 |
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
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v11a_compact_livestock.py | 634.7 | 124 | 145 | 0 | +20,549 | -30,769 |
| V3_4_CENTER_PASTURE_CHALLENGER.zip | 632.7 | 19 | 16 | 0 | +23,103 | -28,406 |
| V2_8D_CENTER_PASTURE_CHALLENGER.zip | 616.4 | 18 | 17 | 0 | +20,666 | -34,794 |
| V3_4_INTERIM_CHAMPION.zip | 615.8 | 17 | 15 | 0 | +26,090 | -23,796 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| V3_7_DUTY_AWARE_LAND_ACTIVATION_EXPERIMENTAL.zip | 603.9 | 14 | 12 | 0 | +18,751 | -12,340 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| submission-v2-reopened-provisional.zip | 489.3 | 81 | 99 | 0 | +15,431 | -32,113 |
| V2_2_CARROT_9_CHALLENGER.zip | 460.6 | 19 | 20 | 0 | +13,914 | -19,308 |
| V2_1_MINIMAL_SCENARIO_CHALLENGER_CLEAN.zip | 458.4 | 12 | 15 | 1 | +8,018 | -31,157 |
| v2_1_experimental_ladder.zip | 448.7 | 11 | 15 | 0 | +11,329 | -35,449 |
| v2_1_minimal_scenario_challenger.zip | 425.3 | 11 | 14 | 1 | +12,934 | -17,664 |

- Overall (all my episodes in DB, n=1243): 611 W / 625 L / 7 T.
- Today's newly synced mine episodes (n=241): 123 W / 118 L. V3_9 22-22, V3_4_CENTER 19-16, V2_8D 18-17, V3_4_INTERIM 17-15, V3_7 14-12, V2_2 19-20, V2_1_CLEAN 4-4, v11a 10-12.
- V3_9 (submitted today 09:08) is the highest public score of any submission so far (779.0), but its DB record is exactly .500 with symmetric margins.

## Loss tags
- SHED_AT_CAP: 220 (only tag present on my-seat losses)

## Top opponents in the data
Query as specified (real ladder opponents only, `p.seat != e.my_seat`): the ladder is flat — top 5 all tied at n=4. Scouted leaderboard teams have `my_seat IS NULL` so they're excluded from that query; listed separately below.

Ladder opponents (n=4 each):
| name | avg final $ | wheat/carrot/tomato/straw/melon plants | quad2_day | avg hires | notable sells |
|---|---|---|---|---|---|
| Darshan Makwana | 95,656 | 93 / 2 / 0 / 1.25 / 30 | 11 | 7.07 | FERTILIZER 1,237, WOOL 729, MILK 576 |
| DavidX | 82,722 | 76 / 0 / 0 / 36 / 23.25 | 11 | 7.32 | MILK 8,606, STRAWBERRY 7,582, MELON 4,922 (likely round-trip inflated) |
| Nikunj Pahwa | 72,850 | 83.75 / 0 / 0 / 15 / 18.5 | 7.25 | 9.18 | WHEAT 4,377, FERTILIZER 788, MILK 525 |
| Khoa Le | 70,224 | 92.75 / 0 / 0 / 18.25 / 21.25 | 0 | 10.16 | WHEAT 1,380, MILK 867, FERTILIZER 630 |
| Solve Langseth | 67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9 | 6.59 | MILK 9,920, FERTILIZER 9,804, MELON 9,784 (uniform ~9.8k across 5 items = round-trip artifact, not real volume) |

Scouted leaderboard teams (most games in DB):
| name | n | avg final $ | wheat/carrot/tomato/straw/melon plants | quad2_day | avg hires | notable sells (4-item top) |
|---|---|---|---|---|---|---|
| Crop Dusta | 320 | 101,037 | 120 / 25 / 4.6 / 29 / 16 | 5.0 | 9.8 | WHEAT 512k (round-trip inflated), FERTILIZER 62k, STRAWBERRY 60k, MILK 60k |
| Ryo Hasegawa | 222 | 96,041 | 146 / 18 / 3.5 / 31 / 12.5 | 5.2 | 9.65 | WHEAT 77k, STRAWBERRY 52k, FERTILIZER 51k, MILK 49k |
| Subramanya N | 193 | 93,770 | 117 / 24 / 1.2 / 33 / 15 | 6.0 | 10.1 | WHEAT 60k, FERTILIZER 46k, STRAWBERRY 39k, MILK 37k |
| カワシギ | 170 | 89,549 | 126 / 6 / 0 / 39 / 15 | 6.0 | 9.23 | FERTILIZER 317k + WHEAT 202k (round-trip inflated), STRAWBERRY 46k, MILK 39k |
| tetsuya | 123 | 87,812 | 134 / 4 / 0.8 / 37 / 12.5 | 7.0 | 10.34 | WHEAT 42k, FERTILIZER 32k, STRAWBERRY 30k, MILK 27k |

- Caveat: raw sell-unit totals can be inflated by same-match round-trip buy/sell (engine artifact); Crop Dusta WHEAT, カワシギ FERTILIZER/WHEAT and Solve Langseth's uniform ~9.8k are the obvious cases.
- Common shape across all 5 scouted teams: wheat-dominant (117-146 plants), strawberry second (29-39), ~zero tomato, land expansion by day 5-7, ~10 hires/day, ~$88-101k final.

## Local versions not yet submitted
- main_v10.6a_radius3.py
- main_v_clonereplica1.py
- (all other `main_v*.py` in project root have a matching submission fileName)

## Notes
- **`sync_replays.py` was missing from the project root** (deleted from working tree ~Aug 30 16:00 during a cleanup pass; `git status` shows ` D sync_replays.py` plus many other deletions). Restored the file content from `git show HEAD:sync_replays.py` (the committed version already has `--max-episodes`). `git checkout` itself failed because a stale `.git/index.lock` exists — left it alone; remove manually if no git process is running.
- Shell tool caps commands at ~3 min and kills background processes between calls, so sync ran as repeated idempotent foreground calls (mine x3, leaderboard x1); every run ended with a "Done." line.
- 5 replay files are truncated JSON (never ingestible): Crop_Dusta/episode-101390860, mine/episode-91406493, Yusuke_Hayashi/episode-102533949, -102524997, -102556360. 1 file raises `KeyError: 0` in harness ingest: mine/episode-98950706. Consider re-downloading or moving to `Replays/_corrupt`.
- Submitted-but-not-on-disk: main_v2.py, main_v2.1.py, main_v3.py, main_v5.py, main_v7.2.py, main_v7.5.py, main_v7.9.py, main_v8.py, main_v8.2.py, main_v9.5_statehygiene.py, main_v11a_compact_livestock.py, turn_08_small_cow_fleet.py, and all V2_*/V3_* zips (moved to `Archived versions/` or `ChatGPT--Kaggriculture/` / ~/Documents/ChatGPT per memory; not in project root).
- `harness.py` has uncommitted local modifications (` M harness.py`); used as-is.
- `main_v9.3_fertilize.py` submitted twice (755.8 on Aug 6, 671.8 on Aug 28); table merges both under one row and shows the higher score.
