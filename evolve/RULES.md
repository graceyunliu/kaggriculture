# Constitution for candidate generators

Read before proposing. Everything here was measured on the ladder engine, both seats, paired seeds.

## Engine facts (vendor/kaggle_environments_engine_master/kaggriculture.py — the ladder engine)
- 30 days × 24 hours = 720 turns. Money at day 30 decides the game; opponents are fixed replay tapes.
- Two sellers share one market: prices move with inventory, so our sales change the opponent's revenue too.
- Shops are drawn with replacement; town center sells at a flat rate per `townCenterSellInterval`.
- Hands respawn at the shed every morning; hires cost fib(n) for the n-th hire of the day; 10 market orders/turn.
- Animals need daily FEED + CARE; missed days lose production; an unfed animal escapes after 2 days.
- STRAWBERRY/TOMATO are recurring (water daily, harvest repeatedly); WHEAT/CARROT/MELON are one-shot.
- Land: 3 extra quadrants at $1k/$2k/$4k with purchase deadlines by day 14/17/18.
- Crash guard: an exception in `agent()` returns PASS for the turn. A candidate with any agent error is discarded.

## What is closed (do not re-propose as a bare knob change)
- More crop coverage of any single crop (tomato scale-up, more strawberry/melon tiles): lost 4 times.
- Geese / EGG as a third species: lost 3 ways (revenue per service-day below cow/sheep).
- Bigger herd via demand_share 0.75–1.0: −$6k to −$17k. Bigger fleet caps alone: no-op or loss.
- More hands via min_hands 5–6 or load_per_hand 12–15: flat to −$3k.
- Wheat-tile floor 5+ and wheat 8/12 tiles: −$3k to −$15k (never gets land; sold early at $35).
- Holding wheat/fertilizer for late prices: negative. Buying fertilizer to apply: −$1k to −$4.5k.
- NEAR_RADIUS above 4 for siting: decisive loss. Radius growing with land: decisive loss.
- Suppressing crops days 0–9 to fund land/animals: −$96k to −$116k.
- Copying the opponent's land/herd/crop timing onto our dispatcher: −$68k. Allocation without execution loses.

## What worked
- C1 opening: day 0 = 5 HIRE, 2 COW, 2 SHEEP, 8 MELON seed, 7 WHEAT seed, 5 WHEAT feed; hires paid before the feed reserve on days 0–5; no spare feed buffer when poor. +$4.8k held-out vs V3.12.
- Movement-aware crop siting (recurring crops near shed, one-shot far): the biggest single win in the v10 lineage.
- Demand-coupled herd/crop sizing (V3.9): +$50k over its predecessor.
- fert_buy 1 on C1: +$5.4k held-out (first evolution-run finding, Sep 3).

## Where the gap is
- Frontier tapes bank $130–175k where we bank $85–100k. Decomposition: wheat sales (−$15k; tapes plant ~5 wheat tiles/day continuously and sell ~400 units late), melon timing (tapes sell 72 melons on day 10 at $242; we sell later at $166), fertilizer volume, strawberry price ($78 vs $93).
- Our labor per obligation is ~2× the winners' (11.3 vs 6.6 unit-turns per animal-day). Every scaling knob loses because the dispatcher cannot convert extra capacity into serviced obligations. Changes to `sweep`, `dispatch`, `animal_routing`, `crop_admission` are where the remaining value is; `economy` knob changes are mostly exhausted.

## Rules for proposals
- Propose mechanisms, not knob nudges; each proposal should change behaviour in a way visible in the per-day trace.
- Prefer execution-layer blocks. Batching, alternate-day watering of low-yield tiles, fertilize-from-carry, same-day deposit-and-sell, wheat cadence, fewer reversals, route merging.
- A block replacement must define exactly the same top-level functions, use only names already in the chassis, and be valid Python 3.9 (no match statements, no `X | Y` type unions).
- Never touch the crash guard, the engine constants, or `perceive`.
- Make proposals materially different from each other and from what is already in the archive.
