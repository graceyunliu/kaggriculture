# Kaggriculture Daily Report — 2026-08-21

## Sync summary

- `mine`: 20 new episodes ingested. New activity on `submission-v2-reopened-provisional.zip` (10 new) and `main_v11a_compact_livestock.py` (10 new). All other submissions (v10.6 down to v2) had 0 new — no fresh games played on those.
- `leaderboard`: 50 new episodes ingested, 10 each from 5 scouted top teams: Ryo Hasegawa, tetsuya, Arman Tuganbaev, Subramanya N, Izzoudine Mohamed KANTA.

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | $17,519 | -$19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | $17,198 | -$22,038 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | $16,029 | -$38,293 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | $12,102 | -$27,614 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | $20,056 | -$17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | $27,686 | -$16,062 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | $31,836 | -$31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | $30,931 | -$34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | $20,004 | -$53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | $25,197 | -$12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | $25,912 | -$30,258 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | $27,330 | -$22,675 |
| main_v11a_compact_livestock.py | 647.6 | 65 | 75 | 0 | $22,054 | -$34,398 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | $30,425 | -$36,078 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | $9,724 | -$83,517 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | $27,198 | -$21,401 |
| main_v5.py | 556.8 | 14 | 12 | 1 | $19,641 | -$43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | $34,316 | -$37,710 |
| main_v2.py | 564.2 | 4 | 4 | 0 | $27,302 | -$46,834 |
| submission-v2-reopened-provisional.zip | 514.4 | 59 | 71 | 0 | $15,852 | -$32,050 |

Overall today's DB (all versions combined): 372 W / 369 L / 5 T.

## Loss tags

- SHED_AT_CAP: 88 (the only tag currently logged — all identified losses across all versions tag out as shed-capacity-bound)

## Top opponents in the data

Most-represented distinct opponents in the DB today (mix of real ladder + newly scouted leaderboard teams, each still thin at n=3-4 games):

- **Solve Langseth** (n=4): avg final money $67,020. Plant mix wheat/carrot/tomato/straw/melon = 39.5/26.5/0/0/29.5. quad2_day 9.0, avg hires 6.6. Notable sells: MILK 9,920, FERTILIZER 9,804, MELON 9,784, CARROT 9,355, WHEAT 9,212 — these totals are very large relative to a 30-day game and likely reflect round-trip buy/sell activity, not raw production; treat as directional only.
- **Khoa Le** (n=4): avg final money $70,224. Plant mix 92.75/0/0/18.25/21.25 (wheat-heavy, no carrot/tomato). quad2_day 0.0 (expands quadrant 2 immediately), avg hires 10.2. Sells: WHEAT 1,380, MILK 867, FERTILIZER 630, MELON 483, WOOL 454 — plausible-scale, no round-trip flag.
- **Darshan Makwana** (n=4): avg final money $95,656 — highest of the five. Plant mix 93/2/0/1.25/30, quad2_day 11.0, avg hires 7.1. Sells: FERTILIZER 1,237, WOOL 729, MILK 576, MELON 502, WHEAT 205.
- **pengshy** (n=3): avg final money $81,135. Plant mix 42.3/2.7/0/34/28.7 (heavier strawberry). quad2_day 9.0, avg hires 8.9. Sells: WHEAT 2,328, MILK 586, FERTILIZER 578, MELON 445, WOOL 256.
- **mchicen** (n=3): avg final money $67,399. Plant mix 13.3/0/0/5.3/5 — much lower overall planting volume. quad2_day 9.0, avg hires 8.0. Sells: FERTILIZER 953, MILK 693, WOOL 333, EGG 208, STRAWBERRY 4.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py` (per project memory: this is the round-10 clone-replica rebuild, already tested and decisively rejected in self-play — exists locally as a closed experiment, not a submission candidate)

## Notes

- Auth via persisted token worked cleanly, no refresh needed.
- Only one loss tag (SHED_AT_CAP) is present in the tagging system currently — no other loss-cause tags have fired in this data slice.
- Today's 5 "top opponents" are a blend of real ladder history and freshly scouted leaderboard teams; sample sizes are small (n=3-4) so the plant-mix/money figures above are indicative, not statistically solid yet.
