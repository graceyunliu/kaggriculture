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
- **O4 (Sep 9, separate task) — CONFIRMED NEW BEST OWN-CODE CANDIDATE, cross-tested Sep 9.** A from-scratch reactive policy (no copied turn schedule) built on top of O2, adding: (1) shared-resource reservation within a turn for fertilizer/wheat pickups, not just animals — O2 let concurrent workers race for the same fertilizer and lose 19 pickups to no effect in one instrumented game; (2) care scheduling that accounts for an animal's stored care bonus, first-yield day, production interval, and feed history — care given on a production day pays off on the *next* harvest, not that day's (an off-by-one here was caught and fixed in lifecycle tests before shipping); (3) intra-day cash release/reinvestment — sell what route-completing workers deposit during the day rather than only at fixed hours, and allow bounded extra capital decisions after an observed cash bump. Original report (frozen seeds 5001–5050, both seats, 100 games/matchup): +$15,299/game vs C1 (50-0), −$28,900/game vs H32 (1-49), −$14,167/game vs a real Mengfei replay (9-41).
  Independently cross-tested against V3_15 (this file's prior best) on this repo's cascade harness: **O4 beats V3_15 decisively too** — dev (10 seeds) +$13,938/game (t=5.55, 9-1), held-out (20 seeds) **+$15,065/game (t=14.42, 20-0)**; re-confirms the C1 win on this repo's own C1.py (held-out +$13,164/game, t=14.41, 20-0); and vs the real clone (opp_scenario_v14), held-out **+$32,084/game (t=10.24, 20-0)** — roughly double V3_15's own +$18.4k edge over the same opponent. All t-values here are far past the usual ≥2 promotion bar; this is not a marginal result.
  Still loses badly to the tape-hybrid line (H32/M2/M4), same pattern as every other own-code candidate in this file — a real win against a reactive/own-code baseline does not transfer to beating a replay-wrapped tape. Zero agent errors across every test. Submission zip at `submissions/O4_PRODUCTIVE_SERVICE.zip`; candidate at `candidates/O4_PRODUCTIVE_SERVICE.py`; detail in `docs/O4-original-candidate-sep09.md`. **This supersedes V3_15 as the frontier for future own-code proposals — diff against O4, not V3_15 or C1, going forward.**

- **O4's ~$3.1k "bundle" gain (O2→O3, minus shared-stock) is NOT one mechanism and NOT simply additive — it is dominated by one solo effect plus a real two-way interaction (Sep 9 factorial ablation, `evolve/factorial_ablation.py` + `factorial_heldout_check.py`, paired same-seed DEV_SEEDS 1-10 and HELD_SEEDS 11-30, all three sub-mechanisms behaviorally verified before trusting any margin — see below).**
  The bundle decomposes into three sub-mechanisms, each built as a minimal patch against O2: **B = lifecycle-aware care/feed timing** (skip a feed/care visit when the production calendar and stored bonus say it isn't due yet), **C = intraday capital-event timing** (sell every hour instead of only at hour 0/day 28+, and allow off-schedule BUY/HIRE after an observed same-day cash jump), **D = mid-route product release** (drop carried product at a nearby shed mid-route instead of waiting to finish the route).
  Solo effects vs O2 (dev/held-out): **B alone +$2,457/game (t=2.38, 8-2) / +$2,457 (t=2.19, 12-8) — real and the only mechanism that stands on its own.** C alone +$124 (t=0.76, 3-2) / +$183 (t=0.92, 7-5) — negligible alone. D alone **−$2,043 (t=-1.21, 4-6) / −$1,291 (t=-1.25, 9-11) — a wash-to-mild-loss alone**, releasing product mid-route without also selling it faster just moves inventory around.
  Naive sum of solo effects: 2,457 + 124 − 2,043 ≈ **$538/game**. Actual measured bundle (BCD vs O2): **+$3,101 (t=3.50, 8-2) dev, +$3,392 (t=4.42, 17-3) held-out** — the combined bundle materially outperforms what the standalone effects alone would predict. (Don't over-read the ratio between these two numbers as a stable quantity — one input to it, D's solo effect, is itself a weak/noisy negative, so "naive sum vs actual" is a useful descriptive signal that an interaction exists, not a mechanistic multiplier to reuse elsewhere.) The gap is a genuine, directly-confirmed C×D interaction: **CD vs D alone = +$2,864 to +$3,304/game (t=2.97-3.23, both seed sets, 9-1 / 15-5)** and **CD vs C alone = +$1,048 to +$2,160 (t=0.80-1.87, weaker but same direction on held-out)**. Mechanism hypothesis: mid-route release creates intraday-sellable inventory; intraday selling is what converts that availability into usable capital — neither half realizes the full benefit alone. B (lifecycle) sits mostly outside this interaction — its marginal add on top of C+D (BCD vs CD) is +$3,018/game (t=1.77, dev only, not independently re-confirmed held-out), consistent with its solo effect, i.e. lifecycle looks close to additive on top of the C×D pair.
  Verification method note: the first attempt at verifying C used an instrumentation proxy that only counted off-hour BUY/HIRE actions and saw zero difference from O2 on 9 of 10 seeds — an apparent silent no-op, essentially a miniature repeat of the earlier proposal/render-pipeline bug (`kaggriculture-evolve-pipeline-bugs-sep07`). The proxy was missing the mechanism's actual dominant effect (SELL orders firing every hour instead of only hour 0); once SELL was added to the tally, O2_capital showed 9-13 off-schedule sells/game on every seed tested versus 0 for O2 baseline. **Lesson for future verification: confirm the instrumentation covers every order type the patch touches, not just the ones assumed most likely to move — a "no difference found" result can be a broken probe, not a broken mechanism.**

  **Frozen mechanism structure (do not split C and D apart in future proposals — treat as a coupled pair):**
  ```
  O4 bundle decomposition
  B — lifecycle-aware care/feed
      Status: independently beneficial
      Evidence: dev + held-out (+$2,457/game both, t=2.38 / t=2.19)
  C — intraday capital timing
      Status: insufficient/weak alone (+$124 to +$183, not significant)
  D — mid-route product release
      Status: insufficient/negative alone (-$1,291 to -$2,043, not significant)
  C × D
      Status: strongly supported positive interaction (+$1,048 to +$3,304 over either solo, t up to 3.23)
      Mechanism hypothesis: release creates intraday sellable inventory;
      intraday selling converts that availability into usable capital.
  B + (C × D)
      Status: explains the bundle substantially better than an additive three-mechanism model.
  ```
  Practical takeaway for future proposals: don't credit "the bundle" as a black box, and don't assume future timing-mechanism combinations are additive — test the pair directly. Lifecycle-aware feed/care timing is independently valuable and portable on its own. A component that looks harmful or neutral in isolation (C or D alone) can still be essential to a validated interaction — don't reject C or D individually from a future proposal without checking what it's paired with.

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
