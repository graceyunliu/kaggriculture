# Kaggriculture Daily Report — 2026-08-23

## Sync summary

- Mine: 20 new episodes — 10 for `submission-v2-reopened-provisional.zip`, 10 for `main_v11a_compact_livestock.py`. All 18 older submissions: 0 new (capped at 10 most recent, already have them).
- Leaderboard (top 5 scout): 50 new episodes — 10 each from Ryo Hasegawa (score 3134.2), Subramanya N (3037.2), Crop Dusta (2956.8), Arman Tuganbaev (2952.4), MiMi (2947.6).
- DB now holds 2034 episodes total; 779 are my own games with a result.

## My submissions

| version | public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| submission-v2-reopened-provisional.zip | 507.3 | 65 | 78 | 0 | +$15,373 | -$32,796 |
| main_v11a_compact_livestock.py | 641.9 | 73 | 87 | 0 | +$22,481 | -$34,523 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +$27,330 | -$22,675 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +$30,931 | -$34,082 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +$17,198 | -$22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +$12,102 | -$27,614 |
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +$17,519 | -$19,057 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +$27,686 | -$16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +$20,056 | -$17,532 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +$16,029 | -$38,293 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +$31,836 | -$31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +$25,197 | -$12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +$25,912 | -$30,258 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +$30,425 | -$36,078 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +$20,004 | -$53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +$9,724 | -$83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +$19,641 | -$43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +$34,316 | -$37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +$27,198 | -$21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +$27,302 | -$46,835 |

Overall: 386 W / 388 L / 5 T.

## Loss tags

- SHED_AT_CAP: 91 (only tag present on losses)

## Top opponents in the data

Counts include today's leaderboard-scouted episodes (both seats counted where I'm not a player — see Notes). Sell totals carry the round-trip buy/sell caveat: same-item buy-then-sell within a match inflates raw units, so extreme volumes (esp. カワシギ's FERTILIZER/WHEAT) shouldn't be read as net production.

- **カワシギ** (n=140): avg money $90,907; plants W125/C6/T0/S39/M15; quad2_day 6.0; hires 9.2. Sells: FERTILIZER 260,626; WHEAT 166,212; STRAWBERRY 37,716 (volumes extreme — round-trip artifact likely).
- **THUNDER THUNDER** (n=91): avg money $96,575; plants W137/C0/T0/S36/M20; quad2_day 6.2; hires 9.1. Sells: WHEAT 37,702; STRAWBERRY 24,899; MILK 20,379.
- **Seb (allegedly)** (n=87): avg money $85,277; plants W25/C0/T0/S41/M21; quad2_day 4.1; hires 10.1. Sells: FERTILIZER 27,383; STRAWBERRY 25,432; MILK 18,037.
- **Thomas Tschinkel** (n=73): avg money $86,903; plants W123/C9/T0/S39/M15; quad2_day 6.0; hires 9.2. Sells: WHEAT 52,667; FERTILIZER 32,574; STRAWBERRY 18,590.
- **somewhere after** (n=72): avg money $125,396 (highest); plants W76/C1/T0/S43/M21; quad2_day 6.8; hires 10.0. Sells: WHEAT 80,274; STRAWBERRY 65,285; MILK 61,432.

Common shape across all five: zero TOMATO, heavy STRAWBERRY (36-43), ~9-10 hires/day, quad2 by day 4-7.

## Local versions not yet submitted

- main_v10.6a_radius3.py
- main_v_clonereplica1.py

## Notes

- The step-7 query as literally specified (`p.seat != e.my_seat`) excludes leaderboard-scouted episodes (my_seat is NULL there, NULL comparison drops the row) and returned only n=3-4 opponents. Used `(e.my_seat IS NULL OR p.seat != e.my_seat)` instead so scouted teams count; noted as a deliberate deviation.
- 11 historically-submitted files no longer exist locally in the project root (archived?): main_v2.py, main_v2.1.py, main_v3.py, main_v5.py, main_v7.2.py, main_v7.5.py, main_v7.9.py, main_v8.py, main_v8.2.py, main_v8.3.py, main_v9.5_statehygiene.py.
- Newest submission is `submission-v2-reopened-provisional.zip` (Aug 9, public score 507.3) — a .zip, and the current lowest-scoring active entry (65W/78L in synced data).
- Sandbox quirk: a stale root-owned venv at /tmp/kagg_env blocked reuse; built a fresh venv at ~/kagg_env instead. No impact on results.
- Mine-replay files land in Replays/Auto/mine; today's 50 leaderboard replays were downloaded and ingested (per sync output) but are not under a Replays/Auto/leaderboard/*.json path — didn't chase the exact directory since ingestion succeeded.
