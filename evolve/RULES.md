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
- CROP_SWEEP_LEN/RADIUS or ROUTE_LEN nudges on the V3_13/15 dispatcher (Sep 8): every direction tried (sweep chain 6→8, sweep radius 4→6, both combined, route length 3→5, 3→2) lost vs C1, one decisively (route_len=5: −$28.7k/game). These constants are already near their local optimum; re-tuning them without a structural change is wasted effort.
- Fertilizer reserve/buy/pickup on the V3_13/15 dispatcher (Sep 8): porting chassis.py's `fert_keep`/`fert_buy`/opportunistic-shed-pickup mechanism (previously credited with +$5.4k on an older C1 run) regressed on this lineage in all 3 tested configurations — full port −$2,239/game vs itself, reserve+pickup alone −$1,833 (the fetch trip costs more in movement than the doubled yield is worth), shop-buy alone ≈ wash (−$50, not practically meaningful). The old finding doesn't transfer as-is; don't re-port it without isolating why the interaction changed.
- Animal opening split away from 2 COW/2 SHEEP on the C1-ported opening (Sep 8): 3/1, 1/3, 2/3, 3/2 all tested, none beat the 2/2 baseline; 2/3 was catastrophic (−$23.3k/game, likely an affordability/load-model interaction from the extra unit). 2/2 stays the answer here.
- Melon count on the same opening: 10 instead of C1's 8 was worse across every matchup tested (C1, V3_12, clone). 8 stays the answer.

## What worked
- C1 opening: day 0 = 5 HIRE, 2 COW, 2 SHEEP, 8 MELON seed, 7 WHEAT seed, 5 WHEAT feed; hires paid before the feed reserve on days 0–5; no spare feed buffer when poor. +$4.8k held-out vs V3.12.
- Movement-aware crop siting (recurring crops near shed, one-shot far): the biggest single win in the v10 lineage.
- Demand-coupled herd/crop sizing (V3.9): +$50k over its predecessor.
- fert_buy 1 on C1: +$5.4k held-out (first evolution-run finding, Sep 3).
- **V3_13_WEED_AND_FEED (Sep 8), on top of V3_12** — two execution-layer fixes, both directly targeting the labor-per-obligation gap below: (1) moved the "weeds" sweep tier ahead of harvest/water — a weeded tile is a 100% capacity loss until dug, worse than an unwatered crop, and the old order checked it dead last; (2) alternate-day feed/care via `consecutive_unfed == 0` — base animal production isn't gated by feeding at all (only the care bonus is, and it still accrues on a skipped day), so feeding every animal every day was pure wasted movement; skip is safe against the 2-consecutive-day escape rule. Held-out (20 seeds) vs the real clone opponent: **+$13,467/game, t=8.49, 20-0**. Consistently better or equal against every other opponent spot-checked (frontier, soil, andrey); ~even against tape_antigone (both lose there already). Confirms the RULES.md execution-gap diagnosis was directionally right and gives a first concrete win from it — see `candidates/V3_13_WEED_AND_FEED.py` header for full numbers.
- **V3_15 (Sep 8)** — V3_13's fixes + C1's frontier opening (5 HIRE/2 COW/2 SHEEP/8 MELON/7 WHEAT/5 feed, all at hour 0 day 0) + C1's labor-first early-hire ordering (days ≤5: hire before feed). Closes the V3_13-vs-C1 gap from a decisive −$8.8k/game loss to a genuine statistical tie (30-seed combined dev+held-out: +$512/game, 15-15 wins) while still beating V3_12 (+$7.4k dev) and the real clone decisively (+$18.4k held-out, t=9.41, 19-1). Best own-code candidate as of Sep 8; see `candidates/V3_15.py`.
- **O4 (Sep 9, separate task)** — a from-scratch reactive policy (no copied turn schedule) built on top of O2, adding: (1) shared-resource reservation within a turn for fertilizer/wheat pickups, not just animals — O2 let concurrent workers race for the same fertilizer and lose 19 pickups to no effect in one instrumented game; (2) care scheduling that accounts for an animal's stored care bonus, first-yield day, production interval, and feed history — care given on a production day pays off on the *next* harvest, not that day's (an off-by-one here was caught and fixed in lifecycle tests before shipping); (3) intra-day cash release/reinvestment — sell what route-completing workers deposit during the day rather than only at fixed hours, and allow bounded extra capital decisions after an observed cash bump. Frozen seeds 5001–5050, both seats, 100 games/matchup: **+$15,299/game vs C1 (50-0, paired t≈2.95 for the O2→O4 delta of +$3,734/game)**, but −$28,900/game vs H32 (1-49) and −$14,167/game vs a real Mengfei replay (9-41) — same pattern seen throughout this file: a real win against a reactive/own-code baseline does not transfer to beating a replay-wrapped tape. Zero agent errors across 600 games; 87 isolated lifecycle fixtures confirmed the husbandry logic preserves the daily-care control's yield. Not yet cross-tested against V3_13/V3_15/M2/M4 — worth doing before assuming it's the new best own-code candidate, since O4's reference point (C1) is not the current best (V3_15 ties C1). Submission zip at `submissions/O4_PRODUCTIVE_SERVICE.zip`; detail in `docs/O4-original-candidate-sep09.md`.

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

## Lessons from O4 (Sep 9) — apply to every future proposal, not just the reactive-policy family
- **Fix resource conflicts before adding more work.** If two workers can claim the same fertilizer/wheat/site in one turn, more hands or more crops just means more collisions, not more output. Check for un-reserved shared resources (anything pulled from a shared shed/pool without decrementing it for the rest of that turn's dispatch) before proposing capacity increases.
- **Useful work matters more than raw activity.** More care/feed/watering isn't automatically more production — check the actual payoff timing (e.g. a care bonus earned today may only pay off on a *later* scheduled production day, not today's). Verify off-by-one timing assumptions against the engine source, not against intuition.
- **Small, familiar seed sets mislead.** A margin measured on a handful of dev seeds can vanish or reverse on a larger frozen, paired, held-out set (this file's own M5/M6 and V3_16/19 results are the same lesson from the other direction). Keep selection data separate from confirmation data, pair both seats, and freeze the exact seed range and candidate SHA before trusting a result.
- **Audit the actual entrypoint and engine effects, not just error counts.** A wrapper (e.g. a tape-hybrid fallback path) can bypass code you think you changed. Zero Python errors does not mean zero wasted/ineffective actions — a legal-looking action that doesn't actually change engine state (like a fertilizer pickup that loses a race) won't raise an exception; it just does nothing. Instrument for state-change, not just crash-freedom.
- **Economic plausibility isn't sufficient evidence.** "This should help the economy" isn't a substitute for a measured, paired-seed result — several plausible-sounding ideas (competitive herd sizing, anticipatory fertilizer buying) have been built, tested, and rejected in this project (see "What is closed" above); a new plausible-sounding idea needs the same bar, not a lower one.
- **A win over a reactive/own-code baseline is not a ladder win.** Beating C1, V3_12, or V3_15 decisively is real progress but does not mean beating a replay-wrapped tape (H32/M2/M4) or the real ladder field — those categories have been shown repeatedly to require a different kind of edge (see the M2-adaptive-opening doc). Always state which baseline a result is against.
