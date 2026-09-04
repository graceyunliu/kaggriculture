# Kaggriculture Daily Report — 2026-08-13

## Sync summary

- Mine: 29 new episodes ingested, across submissions `submission-v2-reopened-provisional.zip` (10), `main_v11a_compact_livestock.py` (10), `main_v10.6_radius3.py` (9). All other submitted versions already had 10+ cached (0 new, capped).
- Leaderboard: 50 new episodes ingested, 10 each from 5 scouted teams: カワシギ (16677252), jasonstillchasin (16671088), JALKARNA GAUTAM (16659081), researchstudio.site (16676904), Mohamed abdelrazik (16624979).
- Total new: 79 episodes.

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| submission-v2-reopened-provisional.zip | 521.7 | 21 | 29 | 0 | +16,514 | -28,785 |
| main_v11a_compact_livestock.py | 679.2 | 27 | 33 | 0 | +27,044 | -30,715 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |

Totals across all DB episodes with a result: 296 W / 285 L / 5 T.

## Loss tags

- SHED_AT_CAP: 72 (only tag currently populated in the DB)

## Top opponents in the data

| opponent | n games | avg final money | wheat/carrot/tomato/straw/melon plant avg | quad2_day avg | avg hires/day |
|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9.0 | 6.59 |
| Khoa Le | 4 | $70,224 | 92.75 / 0 / 0 / 18.25 / 21.25 | 0.0 | 10.16 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0 / 1.25 / 30.0 | 11.0 | 7.07 |
| islet | 3 | $106,912 | 82.7 / 0 / 0 / 32.7 / 20.3 | 7.0 | 9.77 |
| Syed Muhammad Gillani | 21 | $86,041 | 117.2 / 0 / 0 / 34.0 / 21.0 | 6.6 | 8.55 |

Notable sell totals (total units, summed across games):
- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 / CARROT 9,355 / WHEAT 9,212 — these are all clustered near the market's I0=10,000 starting inventory, strongly suggesting round-trip buy/sell activity rather than 9-10k units of real net sales per item; treat as an engine artifact, not a real sell volume.
- Khoa Le: WHEAT 1,380 / MILK 867 / FERTILIZER 630 (plausible, not near the I0 ceiling).
- Syed Muhammad Gillani (largest sample, n=21): WHEAT 14,879 / STRAWBERRY 5,634 / MILK 5,122 — wheat-heavy volume seller, consistent with its plant mix (wheat 117 avg, zero carrot/tomato).
- Darshan Makwana / islet: FERTILIZER-led sell mix, both post highest avg money ($95.6k / $106.9k) of the five — worth a closer look if fertilizer-as-cash-crop hasn't been re-tested recently.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py` (per memory: the clone-replica rebuild, decisively rejected in testing — never submitted to ladder, consistent with that result)

## Notes

- Auth succeeded on first attempt using the persisted token; no re-auth needed.
- `main_v9.5_statehygiene.py` and `turn_08_small_cow_fleet.py` are both submitted-and-scored but not in the project root — found archived at `Archived versions/main_v9.5_statehygiene.py` and still present as `turn_08_small_cow_fleet.py` (this one *is* in root, disregard — false alarm on first pass).
- `submission-v2-reopened-provisional.zip` (lowest public score, 521.7, and worst win rate 21W/29L) has no matching local `.py`/`.zip` file found in the project folder — likely an older/archived experiment; flagging since its live score is a clear outlier low vs everything else on the ladder.
- Loss-tag table is thin (only `SHED_AT_CAP` populated) — either the harness only tags that one failure mode currently, or other tag types aren't being written; worth checking `harness.py`'s tagging logic if richer loss diagnostics are wanted going forward.
