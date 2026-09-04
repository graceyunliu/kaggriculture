# Kaggriculture Daily Report — 2026-08-11

## Sync summary

Mine: 30 new episodes.
- submission-v2-reopened-provisional.zip: +10 (50 total)
- main_v11a_compact_livestock.py: +10 (89 total)
- main_v10.6_radius3.py: +10 (59 total)
- all other submissions: 0 new (already at cap or no new episodes)

Leaderboard (top 5 scouted): 50 new episodes.
- Kaito Fukami (score 3212.1): +10
- THUNDER THUNDER (score 3157.9): +10
- Victor @ Tufa Labs (score 3147.1): +10
- Erfan Eshratifar (score 3146.3): +10
- Dmitry Larko (score 3130.1): +10

Total new: 80 episodes.

## My submissions

Cumulative W/L/T across all DB history per version (not just today's new episodes).

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +$30,931 | -$34,082 |
| main_v10.6_radius3.py | 657.4 | 17 | 23 | 0 | +$33,580 | -$26,101 |
| main_v11a_compact_livestock.py | 663.6 | 16 | 24 | 0 | +$31,013 | -$25,451 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +$17,198 | -$22,038 |
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +$17,519 | -$19,057 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +$12,102 | -$27,614 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +$27,687 | -$16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +$20,056 | -$17,532 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +$31,836 | -$31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +$25,197 | -$12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +$25,913 | -$30,258 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +$16,029 | -$38,293 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +$30,425 | -$36,078 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +$20,004 | -$53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +$9,724 | -$83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +$19,641 | -$43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +$34,316 | -$37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +$27,198 | -$21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +$27,302 | -$46,835 |
| submission-v2-reopened-provisional.zip | 529.5 | 11 | 19 | 0 | +$14,958 | -$28,988 |

Overall totals: 264 W / 258 L / 5 T across 527 scored episodes in DB.

## Loss tags

- SHED_AT_CAP: 63 losses tagged (only tag currently populated in DB).

## Top opponents in the data

Ranked by episode count in DB (mix of ladder + today's leaderboard scouts).

**Khoa Le** (4 eps) — avg final money $70,224. Plant mix: wheat 92.8, carrot 0, tomato 0, strawberry 18.2, melon 21.2. quad2_day 0.0 (never expanded past quad1). avg_hires 10.16/day. Top sells: WHEAT 1,380, MILK 867, FERTILIZER 630, MELON 483, WOOL 454.

**islet** (3 eps) — avg final money $106,912 (highest of the five). Plant mix: wheat 82.7, strawberry 32.7, melon 20.3, no carrot/tomato. quad2_day 7.0. avg_hires 9.77/day. Top sells: FERTILIZER 551, STRAWBERRY 510, MILK 409, WOOL 330, WHEAT 303.

**Syed Muhammad Gillani** (3 eps) — avg final money $82,615. Plant mix: wheat 21.0, strawberry 8.0, melon 24.3, no carrot/tomato. quad2_day 8.7. avg_hires 7.42/day. Top sells: WHEAT 5,602 (very high relative to plant count — likely round-trip buy/sell inflation, treat with caution), MILK 594, FERTILIZER 513.

**Solve Langseth** (3 eps) — avg final money $67,339 (lowest of the five). Plant mix: wheat 39.0, carrot 26.3, melon 27.7, no tomato/strawberry. quad2_day 9.0. avg_hires 6.58/day (lowest). Sell totals for MILK/FERTILIZER/MELON/CARROT/WHEAT all ~7,000-7,440 — extremely even and extremely high, almost certainly round-trip buy/sell artifact rather than real production volume.

**Shuiys** (3 eps) — avg final money $103,407. Plant mix: wheat 40.7, strawberry 71.3 (highest strawberry commitment of the five), melon 33.3, no carrot/tomato. quad2_day 10.3. avg_hires 9.68/day. Top sells: FERTILIZER 1,685, MILK 1,447, STRAWBERRY 998, WOOL 996.

## Local versions not yet submitted

- main_v10.6a_radius3.py
- main_v_clonereplica1.py

## Notes

- Auth succeeded on first check; no token issues.
- Both sync commands (`mine`, `leaderboard 5`) completed in a single invocation each — no retries needed.
- `sells_json` totals above can include round-trip buy/sell inventory churn within a match (known engine artifact); Solve Langseth's and Syed Muhammad Gillani's wheat/multi-item totals look inflated for this reason — don't read them as literal production volume.
- Loss-tag table only has one populated tag (SHED_AT_CAP) across the whole DB history — either other loss modes aren't being tagged by the harness, or this is genuinely the dominant/only detected loss pattern.
