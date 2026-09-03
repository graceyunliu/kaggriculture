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

## Measured execution gap (process traces, seed 1, Sep 3) — the numbers to move
- **travel per work action: C1 1.5–1.6 vs frontier tapes 0.97–1.05.** Same hand count (12–13). That is the whole
  labor-efficiency gap in one number: the tapes do ~250 more work actions in days 8–15 with fewer moves.
- **The tapes skip feeding on non-production days**: missed_feed 37 (Milan Leonard) / 12 (Yuan800) vs C1's 13/7 — an
  animal only escapes after 2 consecutive unfed days, and cows produce every 2 days, sheep every 3. C1 feeds everything
  daily. Deliberate alternate-day feeding of animals not due to produce frees ~10–15 unit-turns/day.
- Tapes water later in the day (water_hour 14.2–14.3 vs 13.1) but miss fewer plant-days (334–407 vs 430–564): they
  batch watering into fewer, fuller sweeps instead of scattering it.
- Tapes carry more idle (13% vs 8%) and still win: idle is not the problem, wasted movement is.
- Net-worth divergence starts at **day 10** in both tape matchups — the days-8–15 window (second land quadrant,
  herd at 10–14, 50–60 plants) is where the sweep/dispatch design decides the game.

## Routing oracle (evolve/oracle.py, Sep 3 night) — routing alone is NOT the lever
- Counterfactual executor with travel made free (every relocation = 1 turn) on C1 vs the Yuan800 tape, seeds 1–8:
  own money changes between **−$63k and +$25k per seed, mean ≈ 0**. Idle unit-turns explode (3–10× the base).
  With travel free, C1 does not have enough work to give its hands, and its economy does not scale production
  to use the freed labor (hires and seed purchases are driven by load and morning cash, not by capacity).
- Halving travel ("speed2") is also ≈ 0 on average. Conclusion: **a better router bolted onto C1's allocation
  is worth little.** The frontier's edge is *paired*: it generates more obligations (13–14 animals, ~5 wheat tiles
  planted every day, 400 wheat units sold) AND services them at 1.0 moves per action.
- So proposals must couple the two: raise the work available per hand-day (herd size, continuous wheat/one-shot
  planting cadence, harvest batching) together with the execution change that makes it serviceable. Execution-only
  or allocation-only changes have both been measured to fail.

## Rules for proposals
- Propose mechanisms, not knob nudges; each proposal should change behaviour in a way visible in the per-day trace.
- Prefer execution-layer blocks. Batching, alternate-day watering of low-yield tiles, fertilize-from-carry, same-day deposit-and-sell, wheat cadence, fewer reversals, route merging.
- A block replacement must define exactly the same top-level functions, use only names already in the chassis, and be valid Python 3.9 (no match statements, no `X | Y` type unions).
- Never touch the crash guard, the engine constants, or `perceive`.
- Make proposals materially different from each other and from what is already in the archive.
