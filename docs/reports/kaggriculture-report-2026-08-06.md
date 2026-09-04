# Kaggriculture Daily Report — 2026-08-06

## Sync summary

- **Mine**: 33 new episodes ingested. turn_08_small_cow_fleet.py +10, main_v8.3.py +10, main_v8.2.py +10, main_v8.py +3 (capped at 10/submission; older versions had 0 new).
- **Leaderboard** (top 5 scouted): 50 new episodes, 10 each — Mohit Rao (16665841), Yaroslav (16621590), UwU (16658384), Kaileh57 (16671767), roma (16655323).
- Both syncs completed in a single pass, no timeouts/retries needed.

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| turn_08_small_cow_fleet.py | 723.9 | 5 | 5 | 0 | $2,531 | -$47,434 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | $20,004 | -$53,481 |
| main_v8.2.py | 676.2 | 6 | 5 | 1 | $25,602 | -$7,881 |
| main_v8.3.py | 675.7 | 4 | 6 | 0 | $33,291 | -$49,202 |
| main_v8.py | 673.8 | 10 | 10 | 0 | $25,913 | -$30,258 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | $27,198 | -$21,401 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | $30,425 | -$36,078 |
| main_v2.py | 564.2 | 4 | 4 | 0 | $27,302 | -$46,835 |
| main_v5.py | 556.8 | 14 | 12 | 1 | $19,641 | -$43,033 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | $9,724 | -$83,517 |
| main_v3.py | 550.6 | 8 | 6 | 1 | $34,316 | -$37,710 |

Overall across all mapped episodes: 90 W / 76 L / 4 T.

## Loss tags

- SHED_AT_CAP: 31 (only tag present in DB — no other loss-tag categories logged).

## Top opponents in the data

| opponent | n games | avg final money | wheat/carrot/tomato/strawberry/melon | quad2_day | avg hires/day |
|---|---|---|---|---|---|
| Ryan Hancock | 3 | $90,141 | 54.7 / 0 / 0 / 7.0 / 25.3 | 9.7 | 7.98 |
| Tians12 | 2 | $76,130 | 85.5 / 7.5 / 0 / 43.0 / 40.5 | 11.0 | 8.80 |
| TheSven | 2 | $63,272 | 0 / 9.0 / 26.5 / 12.5 / 14.5 | 8.0 | 9.32 |
| StupidXie | 2 | $61,007 | 33.5 / 0 / 0 / 0 / 33.0 | 4.5 | 3.33 |
| Solve Langseth | 2 | $69,155 | 38.5 / 24.5 / 0 / 0 / 29.5 | 9.0 | 6.65 |

Notable sells:
- Ryan Hancock: WHEAT 1017, MILK 593, FERTILIZER 570 — wheat-heavy economy, highest avg money of the five.
- Tians12: WHEAT 1044, MELON 329, STRAWBERRY 283 — only one in this group running a real strawberry line.
- Solve Langseth: MILK 4960, FERTILIZER 4902, MELON 4882, CARROT 4677, WHEAT 4609 — these totals are implausible for 2 games and almost certainly inflated by round-trip buy/sell activity (known engine artifact); don't read as real trade volume.

## Per-opponent per-day sell volumes by good

Summed across all logged games per opponent (n games noted per section). Units are `SELL` order quantities, keyed by in-game day (0-29). Zero cells omitted from view but present in the underlying `sell_events` table.

**Caveat**: day-29 (final-day) totals can include end-of-game liquidation / round-trip buy-sell artifacts and shouldn't be read as steady-state production — see Solve Langseth below for an extreme example.


### Ryan Hancock (n=3 games)

| day | FERTILIZER | MELON | MILK | STRAWBERRY | WHEAT | WOOL |
|---|---|---|---|---|---|---|
| 0 |  |  |  |  | 54 |  |
| 1 | 6 |  |  |  | 2 |  |
| 2 | 12 |  |  |  | 14 |  |
| 3 | 10 |  |  |  | 19 |  |
| 4 | 5 |  |  |  | 9 |  |
| 5 | 16 |  |  |  | 52 |  |
| 6 | 12 |  |  |  | 15 | 9 |
| 7 | 11 |  |  |  | 20 | 1 |
| 8 | 7 |  | 17 |  | 3 |  |
| 9 | 10 |  | 29 |  | 45 |  |
| 10 | 11 |  |  |  | 8 | 13 |
| 11 | 20 | 118 | 24 |  |  | 1 |
| 12 | 19 | 24 | 3 |  |  |  |
| 13 | 22 |  | 21 |  | 23 | 11 |
| 14 | 22 |  |  |  | 6 | 11 |
| 15 | 28 |  | 42 |  | 23 |  |
| 16 | 30 | 12 | 3 |  | 9 | 18 |
| 17 | 21 |  | 48 |  | 2 | 8 |
| 18 | 25 |  | 24 |  | 6 | 5 |
| 19 | 24 |  | 45 |  | 6 | 12 |
| 20 | 25 | 58 | 27 |  | 19 | 11 |
| 21 | 31 | 92 | 54 |  | 2 | 8 |
| 22 | 22 | 24 | 15 | 3 | 3 | 8 |
| 23 | 29 | 36 | 50 | 6 | 5 | 12 |
| 24 | 31 | 18 | 22 | 4 | 20 | 7 |
| 25 | 24 | 6 | 42 | 4 | 5 | 12 |
| 26 | 30 |  | 29 | 7 | 3 | 8 |
| 27 | 27 |  | 42 | 5 | 18 | 12 |
| 28 | 30 | 2 | 32 | 9 | 247 | 13 |
| 29 | 10 |  | 24 | 10 | 379 | 4 |

### Tians12 (n=2 games)

| day | CARROT | FERTILIZER | MELON | MILK | STRAWBERRY | WHEAT | WOOL |
|---|---|---|---|---|---|---|---|
| 11 |  |  | 130 |  | 24 |  |  |
| 12 |  |  |  |  |  | 29 |  |
| 13 |  |  |  |  | 24 | 33 |  |
| 14 |  |  |  |  |  | 25 |  |
| 15 |  |  |  |  | 37 | 100 |  |
| 16 |  |  |  |  |  | 24 |  |
| 17 |  | 5 |  |  | 46 | 32 |  |
| 18 |  | 12 |  |  |  | 24 | 18 |
| 19 |  | 12 |  |  |  | 65 |  |
| 20 |  | 12 |  | 48 |  | 49 |  |
| 21 |  | 12 | 39 |  |  | 33 | 12 |
| 22 |  | 7 | 85 | 21 |  | 18 | 6 |
| 23 |  | 10 | 5 |  | 9 | 57 |  |
| 24 |  | 5 | 43 | 20 | 4 | 19 | 4 |
| 25 |  | 12 |  |  | 20 | 32 | 3 |
| 26 |  | 5 |  | 19 | 18 | 98 |  |
| 27 |  | 2 | 15 |  | 33 | 86 | 10 |
| 28 |  | 15 | 12 | 20 | 47 | 179 | 3 |
| 29 | 3 |  |  |  | 21 | 141 |  |

### TheSven (n=2 games)

| day | CARROT | FERTILIZER | MELON | MILK | STRAWBERRY | TOMATO | WOOL |
|---|---|---|---|---|---|---|---|
| 1 |  | 4 |  |  |  |  |  |
| 2 |  | 3 |  |  |  |  |  |
| 3 |  | 4 |  |  |  |  |  |
| 4 | 18 | 6 |  |  |  |  |  |
| 5 |  | 6 |  |  |  |  |  |
| 6 | 7 | 9 |  |  |  |  | 6 |
| 7 | 6 | 1 |  |  |  |  |  |
| 8 | 11 | 5 |  | 9 |  |  |  |
| 9 |  | 1 |  | 19 |  |  |  |
| 10 |  | 5 | 8 | 9 |  |  | 4 |
| 11 |  |  | 42 | 6 |  |  |  |
| 12 |  |  | 16 | 6 | 4 |  |  |
| 13 |  | 1 | 4 | 23 | 1 |  | 4 |
| 14 |  | 1 |  | 3 | 2 |  |  |
| 15 |  | 9 | 2 | 19 | 5 |  |  |
| 16 |  | 3 | 23 | 3 | 1 |  | 8 |
| 17 |  | 15 | 8 | 21 | 2 |  | 11 |
| 18 |  | 15 | 6 | 2 | 1 |  |  |
| 19 |  | 13 | 12 | 26 |  |  | 7 |
| 20 |  | 15 | 6 | 13 | 1 | 5 | 14 |
| 21 |  | 16 |  | 44 |  | 3 |  |
| 22 |  | 14 |  | 6 | 8 | 12 | 3 |
| 23 |  | 16 |  | 44 |  | 19 | 13 |
| 24 |  | 13 |  | 8 | 7 | 11 |  |
| 25 |  | 13 |  | 25 | 3 | 14 | 1 |
| 26 |  | 15 |  | 9 | 8 | 3 | 14 |
| 27 |  | 22 |  | 43 | 4 | 4 |  |
| 28 |  | 12 |  | 23 | 6 | 1 | 7 |
| 29 |  | 17 |  | 20 | 4 |  | 13 |

### StupidXie (n=2 games)

| day | FERTILIZER | MELON | WHEAT | WOOL |
|---|---|---|---|---|
| 2 | 8 |  |  |  |
| 3 | 8 |  |  |  |
| 4 | 8 |  | 2 |  |
| 5 | 8 |  | 4 |  |
| 6 | 8 |  | 12 |  |
| 7 | 8 |  | 16 | 48 |
| 8 | 8 |  | 25 |  |
| 9 | 11 |  | 27 |  |
| 10 | 9 |  | 26 | 24 |
| 11 | 10 |  | 37 | 8 |
| 12 | 11 |  | 40 |  |
| 13 | 11 | 47 | 29 | 26 |
| 14 | 11 | 9 | 40 | 8 |
| 15 | 12 |  | 39 |  |
| 16 | 11 | 9 | 29 | 29 |
| 17 | 11 | 20 | 41 | 15 |
| 18 | 12 | 4 | 39 | 2 |
| 19 | 11 | 6 | 27 | 34 |
| 20 | 11 |  | 40 | 9 |
| 21 | 13 |  | 38 |  |
| 22 | 13 | 4 | 26 | 34 |
| 23 | 13 | 6 | 41 | 10 |
| 24 | 13 | 17 | 38 |  |
| 25 | 12 | 46 | 28 | 36 |
| 26 | 11 | 16 | 42 | 17 |
| 27 | 13 |  | 42 |  |
| 28 | 13 | 6 | 35 | 36 |
| 29 | 13 | 15 | 58 | 12 |

### Solve Langseth (n=2 games)

| day | CARROT | FERTILIZER | MELON | MILK | WHEAT |
|---|---|---|---|---|---|
| 2 |  | 10 |  |  |  |
| 3 |  | 12 |  |  |  |
| 4 |  | 12 |  |  |  |
| 5 |  | 12 |  |  |  |
| 6 |  | 12 |  |  |  |
| 7 | 12 | 12 |  |  |  |
| 8 | 12 | 12 |  |  |  |
| 9 | 8 | 10 |  | 60 |  |
| 10 |  | 12 |  | 12 | 6 |
| 11 |  | 10 |  | 30 |  |
| 12 | 8 | 12 |  | 2 |  |
| 13 | 4 | 10 |  | 30 |  |
| 14 | 8 | 12 |  | 2 |  |
| 15 |  | 10 |  | 30 |  |
| 16 |  | 12 |  | 2 |  |
| 17 | 2 | 10 | 6 | 30 |  |
| 18 | 2 | 12 | 6 | 2 |  |
| 19 | 5 | 10 | 42 | 30 |  |
| 20 |  | 12 | 12 | 2 |  |
| 21 |  | 10 | 54 | 30 |  |
| 22 |  | 12 | 18 | 2 |  |
| 23 |  | 10 | 36 | 30 |  |
| 24 |  | 12 | 6 | 2 |  |
| 25 | 4 | 10 | 18 | 30 |  |
| 26 | 4 | 12 | 36 | 2 |  |
| 27 | 2 | 10 | 12 | 30 |  |
| 28 | 6 | 12 | 36 | 2 | 3 |
| 29 | 4600 | 4600 | 4600 | 4600 | 4600 |

Solve Langseth's day-29 row (4,600 units across every good simultaneously) is the round-trip artifact called out above in raw form — treat as noise, not a real end-game liquidation.

## Local versions not yet submitted

main_v8.1.py, main_v8.4.py, main_v8.5.py, main_v8.6.py, main_v8.7.py, main_v8.8.py, main_v8.9.py, main_v8.10.py, main_v8.11.py, main_v8.11_berry.py, main_v8.11_wheat.py, main_v8.12.py, main_v8.13.py

(Per project memory, v8.8/v8.9/v8.10/v8.11/v8.11_berry/v8.11_wheat/v8.12/v8.13 were all locally rejected in offline testing — listed here as an objective on-disk/submitted-set diff only, not a recommendation.)

## Notes

- Auth succeeded on first try, no token issues.
- All 11 submitted fileNames resolve to an on-disk file (older ones live under `Archived versions/`).
- turn_08_small_cow_fleet.py currently holds Grace's highest live public score (723.9) despite a thin avg win margin ($2,531) and a 5-5 split in logged episodes — worth watching, small sample.
- profiles table stores identical rows for both seats when name is 'graceyunliu' (self-play safeguard already excluded via `p.name != 'graceyunliu'` filter, per spec).
- **Schema addition**: `harness.py` now writes a `sell_events` table (episode_id, seat, day, item, qty — one row per raw SELL order) alongside the existing aggregate `profiles.sells_json`. Populated automatically on future `ingest()` calls; backfilled once for all 290 pre-existing episodes via new `python3 harness.py backfill-sells <files>` command (290/290 filled, 0 skipped-as-already-filled, 153 skipped as not-yet-in-`episodes` table — duplicate/orphaned replay files, harmless). 7 replay files on disk are truncated/corrupt JSON (likely incomplete downloads) and can't be parsed; none of them belong to episodes currently in the DB.
