# Kaggriculture Agent: System Design Document

**Status:** v5 submitted (issues found); v6 reviewed & rejected; v7 built on replay-verified schema; **v7.1 built on real vendored engine source + head-to-head local testing, beats v7 5/5 seeded games**
**Last updated:** August 4, 2026 (v7.1)
**Competition:** Kaggle Kaggriculture (entry deadline Sep 23, 2026, $50k pool, ~750 teams)

---

## 1. Problem Statement

Build an autonomous agent for a two-player farming simulation. Each player manages a farm over 720 turns (24 turns/day x 30 days), starting with $3,000. The winner is whoever holds more cash at the end; unsold inventory counts for nothing. Agents compete head-to-head on a skill-rated ladder, so only win/loss matters, not margin.

The game is not a prediction problem. It is a resource-constrained scheduling problem layered under a shared-market pricing game, played against an adversary whose farm is public but whose inventory is private.

## 2. Design Principles

1. **Rules-first, ML-later.** Precedent from comparable simulation competitions (Lux AI) shows hand-crafted strategy with exact environment math dominates leaderboards for months. RL and search are late-stage refinements, not the skeleton.
2. **The engine source is ground truth.** The environment (`kaggriculture.py`) is open source. Every rule belief in the agent is copied from or verified against it, never reconstructed from memory or secondhand descriptions. All four external strategy sources reviewed during design contained at least one confidently stated false mechanic (see Decision Log).
3. **Never-die before clever.** A crash, timeout, starved plant, or overflowed shed is an unforced loss. Survival invariants outrank optimization until the agent solidly beats the median.
4. **Evaluability is architectural.** The world model is built as pure functions so unit evals are cheap; every strategy change is judged by batch self-play win rate, not single games.

## 3. Architecture

Six layers. The world model is the foundation everything queries; layers 2 through 5 transform observation into decisions; layer 6 assembles the legal action dict.

```
                [ Game observation (per turn) ]
                              |
        +---------------------+---------------------+
        |                                           |
  [2. Perception & state tracker]        [3. Economy policy]
   task lists, price/opponent             standing evaluator,
   history, harvest calendars             paced selling, capital plan
        |                                           |
  [4. Task allocation]                              |
   units claim work, routing                        |
        |                                           |
        +---------------------+---------------------+
                              |
                 [5. Robustness guards]
            survival invariants veto/override
                              |
                 [6. Action assembly]
          farmer op + hand ops + market orders
                              |
              [ 1. World model (foundation) ]
     exact price math, growth timing, yield rules,
        forward simulation, all copied from engine
```

### Layer 1: World model (foundation)

Pure, unit-tested functions replicating engine math exactly, preferably copied from `kaggriculture.py` rather than re-implemented:

- `price_after(resource, inventory, delta)` using the published per-resource curve (base, I0=10,000, anchor T, asymmetric shape functions, $1 floor)
- Growth timing: first yield day, max yield day, bonus watering windows, decay onset per crop
- Yield rules: watering bonus (+1/day one-time crops, +2 fertilized), ongoing crop doubling, animal care bonus banking
- Town demand schedule: shop unlock cadence, per-shop consumption, town center scaling (2x after day 10, 4x after day 20)

Rationale: a state-tracking bug silently corrupts every layer above it with no error message, only quietly lower earnings. Exactness here makes an entire category of loss impossible.

### Layer 2: Perception & state tracker

Reads the observation into structured views. v1 scope: own tiles bucketed into water/harvest/plant task lists. Target scope adds:

- Weed detection (v1 gap: weeds are never dug)
- Urgency tiers: a plant at `consecutive_unwatered == 1` is one miss from death and jumps the queue
- Cross-turn memory (the observation is a snapshot with no history): price and market-inventory trajectories, opponent deltas
- Opponent harvest calendar computed from their public tiles, crops, and planting days

### Layer 3: Economy policy

The money brain. Decides hiring, purchasing, land expansion, and sell timing.

- **Hiring:** hands cost fib(n) per day (1, 1, 2, 3, 5...), making action throughput nearly free. Hire aggressively; tune count to available work.
- **Three-flow inventory forecast:** projected market inventory per resource = own planned sales + town drain (known schedule) + opponent harvests (computed from public farm) with a crude sell-lag assumption (e.g. sells within a day of harvest), refined by observing realized price moves. This forecast is the input to sell timing, not today's price alone.
- **Paced selling:** premium goods (strawberry, melon, milk, wool) crash to the $1 floor on modest gluts. Sell in batches sized and timed against the forecast; front-run predicted opponent gluts.
- **Standing evaluator:** the opponent's bank is public and only win/loss scores. Ahead late: reduce variance, liquidate early, protect the lead. Behind: accept variance, hold premium goods for scarcity spikes, take longer-payback bets.
- **Capital plan:** land purchases ($1k/$2k/$4k) and animal investments staged by season phase; planting cutoffs so nothing matures after day 30; full liquidation before season end.

### Layer 4: Task allocation

Maps units (farmer + hands) to tasks each turn.

- v1: greedy nearest-task claiming with Manhattan routing. Sufficient because units can co-occupy tiles; there is no collision or pathfinding problem in this game.
- v3: global assignment via Hungarian algorithm on a units x tasks cost matrix (travel + action turns, weighted by expected gold and urgency). Fixes greedy misallocation where one unit takes a task another was closer to.

### Layer 5: Robustness guards

Hard invariants that veto or override plans:

- Watering/feeding can never be skipped for a living asset; death-imminent assets preempt all other work
- Plant-then-water pipeline: planting day counts as the first unwatered day, so fresh plants get watered same-day by design, not luck
- Shed buffer guard: late each day, project the end-of-day inventory drop; if it would exceed the 100 cap (overflow is destroyed), force sales or halt harvesting. Only matters once paced selling introduces deliberate holding.
- Action legality: never emit an action the engine would reject; wrap the loop so no exception ever escapes (a crash is an automatic loss)

### Layer 6: Action assembly

Produces `{"farmer": op, "hands": [ops], "market": [orders]}` with the market list capped at 10 orders/turn, ordered by priority since extras are silently dropped.

## 4. Evaluation Strategy

Two layers catching different failure classes:

- **Unit evals (component level):** fixed cases asserting world-model outputs match engine outputs. Catches "beliefs about the world are wrong." Runs in seconds on every change.
- **Self-play (end to end):** batches of 20 to 50 seeded games against prior versions and built-in bots ("starter", "random"). Win rate is the only success metric; everything else is a leading indicator. Single games are too noisy to trust.

Benchmark so far (3 seeds, full 720-turn games): v1 beats built-in `starter` 3 of 3, averaging ~$9,300 vs ~$3,500.

## 5. Roadmap

| Version | Scope | Status |
|---|---|---|
| v1 | Greedy scheduler, wheat + tomato economy, hire 4 hands/day, sell-everything-instantly, land expansion, planting cutoffs | Built, beats starter 3/0 |
| v2/v2.1 | World-model price math; paced selling with per-item floors; weed clearing; urgency-tiered watering | Built |
| v3 | Opponent-imminent-harvest front-running; standing evaluator (behind/ahead risk) | Built |
| v4 | Slimmed rewrite | Built |
| v5 | High-scale economy: fleet up to 18 hands, aggressive land to 4 quadrants, melon-heavy portfolio, randomized demand-timing engine (hold premium goods, dump near day-10/20 town demand jumps), same-day-water invariant on planting, zero-PASS idle micro | **Submitted; had issues** |
| v6 | ChatGPT-authored "diagnostic hybrid": adds a speculative cow/pasture state machine (BUY_ANIMAL → PICKUP → PLACE with verification stages, retries, timeouts), schema logging, budget-tracked market-order category buckets. Also silently scales the economy DOWN (hands 18→8, ≤2 hires/day, plant slots halved, earlier plant cutoff) and drops the same-day-water invariant and per-turn task reservation | Built, reviewed — **do not submit as-is** (see 5a) |
| v7 | v5 economy restored in full (18-hand fleet, task reservation, same-day-water, hour-21 plant cutoff) + v6's budget-tracked ordering + one-cow pipeline on the verified schema: buy (lifetime cap 3) → build pasture adjacent to shed → PICKUP at center → PLACE → stateless daily feed/care/milk/deposit loop; feed wheat reserved from selling; live `market.prices` used over computed prices | Built; passes mock-engine lifecycle sim (27/27 days fed, 0 starvation, milk sold) + regression probes |
| v7.1 | v7's animal pipeline (now ground-truth confirmed, not just replay-inferred) + real hire-cost accounting (Fibonacci, deducted from budget) + real cow economics ($400, not ~$1,200) + feed-priority starvation guard + market-order starvation floor without sacrificing sell throughput. Deliberately does NOT adopt v6.1's lower hand cap or dynamic planting guard, and does NOT "fix" the task-remove-on-transit behavior — all three were tried and lost head-to-head to v7 in local testing; see 5c | Built; beats v7 5/5 seeded 720-turn games (modest, consistent edge, ~$14.6-15.4k vs ~$14.5-15.0k) after an initial draft that adopted all of ChatGPT/GLM's advice literally and LOST to v7 by ~2.5x, caught via local A/B testing before submission |
| v7.2 | Generalized `animal_plans` list (multi-animal, multi-species), fixed far-site selection and blind-nearest-pasture maintenance bugs, shipped at `FLEET_TARGET={"COW":4,"SHEEP":0}` + STRAWBERRY added to crop mix | Built; 20/20 seeded wins vs v7.1 locally; **scored 691 on real ladder** (up from ~500s); 6 real loss replays analyzed (5e) — found FLEET_TARGET=4 likely too conservative, WHEAT starved out of planting, land stuck at day 11 |
| v8 (planned) | Expected-value decision engine replacing v7.2's fixed thresholds (fleet ceiling, crop priority, dump-day, land thresholds) with state-dependent scoring across land/animal/hire/seed/sell decisions; keeps v7.2's execution layer (scheduler/movement/maintenance) unchanged. Full spec in `kaggriculture-v8-design-spec.md`, phased with "Phase 0: close the 3 proven v7.2 gaps" first, broader EV-engine phases deferred until Phase 0 is validated | Design spec drafted (see 5f), not yet built |
| Later | Refined opponent sell-lag model from observed price moves; local search on discrete decisions (land timing, sell-now-vs-hold) via forward simulation; mutual-glut timing game; Hungarian assignment; ladder A/B on COW_BUY_START_DAY (3 vs later) | Backlog |

### 5a. v6 review findings (Aug 4, 2026)

Verified: v6 compiles, imports, and the crash guard works. Most of ChatGPT's changelog claims are accurate descriptions of the code. But:

1. **The entire animal action vocabulary is unverified.** `BUY_ANIMAL`, `BUILD_PASTURE`, `PICKUP`, `PLACE`, `FEED`, `CARE`, `COLLECT_FERTILIZER`, and the `"COW"` shed key are all guesses. This violates D2 (engine source is ground truth). The engine file `kaggriculture.py` is not in the repo — recovering it and verifying the schema is the prerequisite for any animal work.
2. **Money-leak loop (reproduced in simulation):** if `BUY_ANIMAL` succeeds but the cow never appears under the `"COW"` shed key, the WAIT_FOR_PURCHASE stage times out to IDLE and re-buys — 18 `BUY_ANIMAL` orders emitted across days 12–14. Needs a lifetime purchase-attempt cap.
3. **Economy scale-down disguised as reliability fixes:** hand cap 18→8 with max 2 hires/day (hands cost fib(n), throughput is nearly free — v5's scale was its strength); plant slots halved (`free_units // 2`); plant cutoff moved from hour 21 to ~hour 15 with a full fleet. Likely costs more than one cow earns.
4. **D11 (same-day-water invariant) silently dropped:** v5 pushed freshly planted tiles into the urgent-water queue; v6 removed this, so every new plant loses a day of watering bonus and starts one miss from death.
5. **Per-turn task reservation removed (reproduced):** all units now chase the same nearest task — 4 units all stepped toward one water tile in test. Duplicate-travel throughput regression vs v5.
6. Minor: dead `remaining_sell_slots` variable; per-animal per-turn stderr schema logging; module-level globals leak across episodes if the runner reuses the process; the 5-sell/2-hire/2-seed slot policy is invented, not an engine rule.

Path forward, either: (a) verify the animal schema, fix items 2–5, then re-evaluate via self-play; or (b) strip the animal machine, keep v6's genuinely good parts (budget-tracked ordering, category buckets, safer `.get()` perception) on top of v5's economy.

### 5b. Animal/engine schema — VERIFIED from ladder replays (Aug 4, 2026)

The engine source is not available, but the three full loss replays (`Replays/Losses/898953*.json` etc.) contain every observation and both players' actions. Opponents ran full animal economies, so the schema is now ground truth (replays > guesses):

**Occupied pasture tile** (there is NO separate ANIMAL tile kind — the animal lives on the PASTURE tile):

```json
{"kind": "PASTURE", "animal": "COW", "fed_today": false, "cared_today": false,
 "consecutive_unfed": 0, "fertilizer_available": false, "pending_care_bonus": 0,
 "placed_day": 1, "yield_units": 0}
```

Empty pasture is just `{"kind": "PASTURE"}`. Species observed: COW, SHEEP (GOOSE key exists in shed).

**Worker carry inventory:** `obs["private"]["inventories"]` — a list of per-unit dicts (farmer first, then hands), e.g. `[{"COW": 1}, {}, {"WHEAT": 2}, ...]`. This is the "worker-inventory schema" v6 lacked.

**Verified action formats** (as used successfully by ladder opponents):

- Unit ops, no args, act on current tile: `["BUILD_PASTURE"]`, `["FEED"]`, `["CARE"]`, `["COLLECT_FERTILIZER"]`, `["HARVEST"]`, `["DROP"]`, `["FERTILIZE"]`
- Carry ops: `["PICKUP", item, qty]` (e.g. `["PICKUP","COW",1]`, `["PICKUP","WHEAT",4]`); `["PLACE", "COW"]` for animals (no qty arg observed), `["PLACE","WOOL",4]` with qty for products
- Market: `["BUY_ANIMAL", species, qty]` — the animal appears in the shed under its species key (`"COW"`) on the SAME turn

**Additional engine facts verified in the second mining pass (used by v7):**

- Board is **10x10**; the shed is the center 2x2 — tiles (4,4), (4,5), (5,4), (5,5). PICKUP and PLACE only succeed on those four tiles (v5/v6's assumption of a shed at (0,0) was wrong).
- `obs["market"]` contains BOTH `inventory` and **`prices`** — current prices are published directly; the price formula is only needed for forecasting.
- Cow production cadence (traced across a full game): +1 `pending_care_bonus` per cared day (cap 5); every 2nd day after placement, `yield_units = 1 + pending_care_bonus` and the bonus resets. Daily-cared cow ≈ 3 milk per 2 days.
- Cow price: confounded by same-turn orders, but ≈ $1,000–1,100 (one clean-ish observation: −$1,105 incl. 2 wheat). v7 budgets $1,200 conservatively and verifies via the shed.
- Animal purchases can fail silently (several observed BUY_ANIMAL turns with no money delta) — verification loops are mandatory, guessing is not.

**Newly confirmed v6 bugs beyond 5a:**

7. **Fatal perceive bug:** occupied pastures match v6's `kind == "PASTURE"` branch first, so they never reach the `animals` list — v6 would never feed, care for, or milk any animal. The cow starves (`consecutive_unfed` climbs) and VERIFY_ACTIVE fails → possible re-buy loop even when everything worked.
8. **FEED requires carried wheat:** opponents `PICKUP WHEAT` from the shed, walk to the pasture, then `FEED`. v6 only buys wheat into the shed and never routes a carrier — its FEED would fire with empty hands.
9. **PLACE arg mismatch:** v6 emits `["PLACE","COW",1]`; every observed animal placement is `["PLACE","COW"]`.
10. v6's fertilizer-flag guesses (`fertilizer_ready`/`has_fertilizer`/`manure_ready`) are all wrong — the real key is `fertilizer_available`. Its `fed_today`/`cared_today`/`yield_units` guesses were correct (moot given bug 7).

Explicitly rejected: MAPF/collision pathfinding (no collisions exist), statistical price fitting (formula is published), end-to-end RL as skeleton (poor ROI per Lux precedent), global tree search (branching factor hopeless; information structure doesn't require it).

### 5c. Real engine source ground truth + external review verification + v7.1 build (Aug 4, 2026)

The real `kaggriculture.py` was found on GitHub (`Kaggle/kaggle-environments`, branch `master`, not on PyPI yet) and vendored into `vendor/kaggle_environments_engine/` — this supersedes replay-mining (5b) as ground truth wherever the two conflict. Two external reviews of v7 (ChatGPT reviewing against its own "Main_v6.1.py", and GLM reviewing the same pair independently) were fact-checked line-by-line against this source before acting on either, and a v7.1 was built by literally applying the *reasonable-sounding* consensus of both — which then lost head-to-head to plain v7 by ~2.5x in local testing, catching that most of that consensus was wrong for reasons neither review could see from reading code alone. Full detail below; short version: read code, but don't trust static review over an actual played-out game.

**Ground truth confirmed from the real engine (not replay-inferred, not either review's guesses):**
- Shed-access tiles are exactly `(4,4),(5,4),(4,5),(5,5)` for board_size=10 (`_shed_access_tiles`) — matches v7's `CENTER_TILES`. v6.1 hardcodes `SHED_POS=(0,0)` and would never successfully complete its cow pipeline; ChatGPT and GLM both agreed on this after it was pointed out, neither had caught it independently.
- Occupied pasture is `{"kind":"PASTURE","animal":"COW",...}` (`_new_animal`) — matches v7's perception model exactly.
- `private["inventories"][0]` = farmer, hands appended after — confirmed.
- Cow cost is a **flat $400** (`ANIMALS["COW"]["cost"]`), not the ~$1,000-1,200 both v6.1 and v7 guessed from replay mining. Real stats: `first_yield_day=8, interval=2, max_held=6` (v7's comment said cap 5, wrong).
- **Hiring cost resets to $0 every day** — `_end_of_day` wipes `hands`, `farmer` position, and `private["inventories"]` to empty for BOTH players every single day, unconditionally, confirmed both in source and empirically in a real ladder replay (hand count goes 3→0→3→0→5 at exact day boundaries in `Replays/Losses/89895315.json`). There is no such thing as a persistent fleet in this game — every version built so far (v5, v6, v7) implicitly assumed hands accumulate across days. They don't.
- Market orders are hard-capped at **10/turn** by the engine itself (`maxMarketOrdersPerTurn`, config default 10), independent of whatever an agent's own code tries to submit.
- An animal that goes 2 consecutive days unfed is lost permanently (structure remains, no refund) — `_daily_refresh_animals`.
- `DemandTimingEngine` (identical in v7 and v6.1) is seeded with a **hardcoded** `match_seed=42`, not the real episode seed — its "randomized" jitter is actually the same fixed offset every single game.

**ChatGPT's review of v7 (7 claims): 6 confirmed real, 1 refuted.** Confirmed: 18-hand labor cap, task-remove-on-transit, flat 10-slot market list (no category reservation), hire cost not deducted from budget, weak flat planting guard, aggressive Day-3 cow start. Refuted: v6.1 does NOT have deterministic Day-10/20 attack timing — the two files' `DemandTimingEngine` classes are byte-identical, both randomized-looking but actually both deterministic per the hardcoded-seed finding above.

**GLM's review of v7 (independent pass): mostly repeated ChatGPT's list, plus two new claims, both of which were wrong.** (1) "Hiring 18 hands costs $6,764/day, will bankrupt the bot" — the Fibonacci math is correct for an unbroken 18-hire batch, but the engine's 10-order/turn ceiling makes that batch impossible; the real worst case is ~$143/day, and every hire is affordability-gated so it can never overdraw regardless. (2) Accused v7's "replay-verified schema" claim of being hallucinated, since v6.1 itself was never run on the ladder — correct that v6.1 has no replay of its own (it was reviewed and rejected pre-submission), but wrong that no real replay was ever pulled: the schema came from `Replays/Losses/89895315.json` etc., which are **v5's** ladder losses (0W/6L/1T) showing the *opponents'* real animal-economy tile data. GLM later conceded this once shown the actual matching JSON.

**Building v7.1 — the literal-consensus draft lost to v7 by ~2.5x, and why.** A first draft applied every recommendation both reviews agreed on: lower hand cap to 8, v6.1's dynamic worker/backlog-aware planting guard, "fix" task-remove-on-transit to only remove on arrival, and reorder market categories so hire/seed get slots before sell. Local head-to-head testing (`kaggle_environments.make("kaggriculture", configuration={"seed": N})`, fixed seeds for reproducibility) showed this draft losing to plain v7 by roughly 2.5x, consistently across 4+ seeds. Bisecting via targeted A/B variants (isolating each change, then combinations) found the mechanism: this economy's profit is dominated by one melon stockpile-and-dump event around day 10-11 (confirmed in a seeded trace: v7 sold 84 melons in one turn for a ~$20.8k windfall that funded three land purchases in the next three turns; the throttled draft only had 12 melons to sell at the same turn). Each of the three "obviously correct" changes independently starved that dump:
- Lower hand cap → less early labor → less planted/watered/harvested before the dump window.
- Dynamic planting guard → same effect, compounding with the hand cap.
- Task-remove-on-transit "fix" → actively harmful given the daily hand/farmer wipe: since every unit *respawns clustered at the same shed tiles every morning*, removing a target only on arrival (not on first step) means many freshly-spawned units compute the same `_nearest()` target from nearly the same position and pile onto ONE tile instead of spreading out. The "bug" (remove on first step) was accidentally serving as same-turn load-balancing — each unit's removal made the next unit's `_nearest()` call land on a different tile. This mechanism only exists because of the daily-wipe finding above; it wouldn't apply in a game where units keep their positions across days.
- Market-order reordering (hire/seed before sell) independently cost the melon dump its slot on turns where hiring also fired at hour 0.

v7.1 as shipped keeps the parts that tested as free improvements (real Fibonacci hire-cost budget tracking, real $400 cow economics, a feed-priority safeguard against the 2-day starvation rule, and a starvation floor for hire/seed that bumps the lowest-priority sell order only when literally all 10 slots are full) and reverts the three that tested as harmful back to v7's originals. Result: beats v7 5/5 on seeds {1,7,42,99,123}, ~$14.6-15.4k vs ~$14.5-15.0k (modest, consistent edge, not the dramatic win the "improvements" were expected to produce) — and still crushes `starter`/`random`/v6.1 (~$28-42k vs ~$0-7k). Zero crash-guard triggers across all test games.

**Takeaway for future review rounds:** both ChatGPT and GLM produced reasonable-sounding, partially-correct critiques from reading code alone, and got the two lowest-stakes claims right (schema legitimacy, deterministic seed) while getting the two highest-stakes ones (hand cap, task-removal semantics) backwards for reasons that only became visible by actually running games. Static code review is worth doing and worth fact-checking against engine source, but it is not a substitute for local self-play before locking in a "fix" — this is the same lesson as D35 (six ladder losses were strategic, not environmental) applied one level up, to the review process itself.

### 5d. v7.2: multi-animal fleet build (Aug 4, 2026)

A diagnostic run of v7.1 against the engine's built-in `starter` bot (full 720-step episode) showed it winning decisively (~$42k vs ~$3.5k) but revealed a structural gap vs. the observed leaderboard top-2: `cow_state`'s buy gate (`not view["my_pastures"]`) makes a second cow purchase impossible, and `SHEEP` never appears in a `BUY_ANIMAL` call anywhere in the file — v7.1 sold 0 WOOL and only 18 MILK / 17 FERTILIZER in that run, vs. the ~864 MILK / 487 WOOL / 445 FERTILIZER Savko/Subin An (the same underlying script, see their replay analysis above) sell from a deliberately-built 8-cow + 6-sheep fleet by day 10. An outside critique of this diagnosis (shared by Grace) independently confirmed the same three code-level facts by reading the file, plus reasonable caveats (the $42k number isn't ladder-comparable since `starter` creates much less market pressure; the 60% animal-revenue estimate uses base prices not realized ones) and proposed a scaling plan: replace the singular `cow_state` with a generic `animal_plans` list, then test 2 cows → 4 cows → +sheep → strawberries incrementally, watching for a single-farmer bottleneck at each step rather than copying the leaderboard's 8+6 fleet size wholesale.

**Build.** `cow_state` (bare dict) became `animal_plans` (list of `{species, stage, site, stage_turn, retries}` dicts), with the same NONE→BOUGHT→CARRYING→ACTIVE/ABANDONED state machine now keyed per-plan instead of a single global. Purchases are strictly **sequential** — only one plan is ever BOUGHT/CARRYING at a time (`economy()`'s `in_progress` gate) — one farmer can't usefully carry two animals in parallel, so there's no reason to buy a second before the first is placed. `FLEET_TARGET = {"COW": n, "SHEEP": m}` is the scaling knob; ANIMAL_SPECS holds both species' real cost/day-window (COW $400, SHEEP $500, both verified in engine source, both use structure `"PASTURE"` so any built pasture accepts either species — confirmed via the engine's `PLACE` handler).

**Two real maintenance bugs found via local A/B testing, invisible with v7.1's single cow:**
1. *Far-site death.* A late-firing purchase (once budget/day conditions happened to align) could only pick a site from whatever empty tiles crops hadn't already claimed by that point in the match — often far from the shed. A single farmer visiting a far pasture every day, on top of a near one plus wheat/product shed trips, can blow the 24-turn daily action budget and miss 2 feedings running, permanently losing the animal (`_daily_refresh_animals`, no refund). Fixed by reserving `FLEET_TARGET`-total near-shed tiles for pastures from turn one (`_init_reserved_sites`) and excluding them from crop planting immediately, regardless of when the actual purchase fires.
2. *Blind-nearest-pasture selection.* `cow_maintenance_action` (now `animal_maintenance_action`) picked the physically nearest pasture every turn, with zero regard for whether that pasture had anything pending. Harmless with one animal; with two+, the farmer could return to an already-fed nearby pasture turn after turn while a farther one's feed need went unaddressed — this, not raw distance, turned out to be the dominant cause of animal loss. Fixed with need-based priority ranking (`_pasture_priority`: urgent feed > any feed > harvest > care > fertilizer > nothing, distance only as tiebreak).

**Scaling results (seeded local self-play vs. v7.1, `env.info["seed"]` set directly — the `configuration={"seed": N}` kwarg does NOT propagate to the engine's actual weed-spawn RNG, which reads `env.info.get("seed", 0)`; confirmed empirically before trusting any of these numbers):**
- 2 cows: 10/10 seeds won, 0 animals lost, 0 unfed events, ~$19-22k vs v7.1's ~$14-15k (~35-45% more money).
- 4 cows: 10/10 seeds won, 0 animals lost (72 near-miss unfed events but none reaching the 2-day loss threshold), ~$21-24k vs ~$14-16k (~55-65% more money).
- 4 cows + 2 sheep, AND 6 cows alone (tested separately to isolate species vs. raw count): **both collapsed catastrophically** — final money ~$2-5k, well below even v7.1's baseline, not a graceful degradation. Root cause (confirmed via a turn-by-turn debug trace): feed-wheat purchase cost scales linearly with fleet size (6 animals → 14 wheat/day target) while reserved-tile crop-capacity loss simultaneously shrinks what hands can plant, and together they starve the melon stockpile-and-dump this whole economy depends on (D54/D55) — days 12-29 in the collapsed run show almost every market-order slot consumed by `HIRE` with literally nothing to sell some turns.
- Shipped at `{"COW": 4, "SHEEP": 0}` — the validated safe ceiling. The SHEEP pipeline exists and works correctly in isolation (verified in the 4+2 trace: sheep purchased, placed, and produced WOOL before the overall economy collapsed from the *combined* fleet size, not a sheep-specific bug) but is left at target 0. Pushing past 4 total animals needs either a feasibility gate before each purchase or a second hand dedicated to animal duty — left for a v7.3, not attempted here.
- STRAWBERRY was added to `PLANT_PRIORITY`/`CUTOFF` only after fertilizer logistics were confirmed reliable at the 4-cow scale (15 FERTILIZER/game sold consistently) — ranked below MELON so it wouldn't compete with the dominant profit driver for hand time. Result: money improved further (~$21-28k) with no observed MELON crowding-out.

**Final shipped result (`main_v7.2.py`):** 20/20 seeded head-to-head wins vs. v7.1, zero animals lost in any run, zero crashes across `starter`/`random`/`pass` opponents and a truncated 48-turn episode (edge case: multi-day animal setup must not crash on a short game).

**Takeaway:** the outside critique's structural diagnosis (single-animal cap, no sheep pipeline) and its "controlled scaling, don't copy the leaderboard fleet size wholesale, watch for single-farmer bottleneck" methodology were both directionally correct and empirically vindicated — the bottleneck showed up exactly where predicted, at 6 total animals, well short of Savko's 14. But the *specific mechanism* only showed up under actual play: it wasn't primarily "8 cows is a lot to carry one at a time" (travel distance), it was "the maintenance loop silently ignores whichever pasture isn't nearest" (a selection bug) plus "feed-wheat cost and crop-capacity both scale against the same single farmer's daily budget" (a resource-contention ceiling) — neither of which is visible from reading the purchase-gate code alone. Same lesson as 5c, one level deeper: even a correct structural critique still needs a played-out game to find the actual failure mode.

### 5e. v7.2 real ladder losses (Aug 4, 2026)

v7.2 scored 691 on the real Kaggle ladder (up from ~500s on prior versions, D56-D61). Grace pulled 6 real loss replays (episodes 90005605, 90006925, 90010183, 90010851, 90011432, 90014106 — opponents Sonuaswar1, Szymon Kłapiński, aarav maheshwari1, AdamBelniak, protoLabs.studio, cheng-han) for analysis. Margins ranged from a near-coinflip ($36,971 vs $37,214) to a blowout ($26,345 vs $129,899); v7.2 lost all 6.

**These are a different opponent pool than the earlier Savko/Subin An snapshot (5a-era replay analysis).** Savko/Subin An were the #1/#2 leaderboard bots running an identical shared script (land NE-day7/SW-day10-never-SE, 8 cow + 6 sheep by day 10, hand cap 12/day, wheat+strawberry+melon only). None of these 6 real opponents — presumably rating-matched near v7.2's own 691 — replicate that script. Their fleets range from 1 animal (AdamBelniak, near-pure WHEAT monoculture: 239 planted, 1125 sold, still beat us by $17.5k) to 27 animals (aarav maheshwari1: 14 cow + 9 goose + 4 sheep, max 18 simultaneous pastures). This is a fresh reference set, not an extension of the Savko-era one — the ladder meta at this rating band looks meaningfully more diverse.

**The dominant, consistent pattern: v7.2 hits its FLEET_TARGET=4 ceiling in literally all 6 games (max pastures = 4, COW:4 exactly, every time), while 5 of 6 opponents run substantially larger fleets** — Sonuaswar1 (16 pastures, 9 cow+7 sheep+5 goose), Szymon Kłapiński (6), aarav maheshwari1 (18, the largest observed), protoLabs.studio (14), cheng-han (bought 26 cow + 90 sheep, though only 12 ever simultaneously active — many purchases likely went unplaced or were replacements). v7.2's own feed ratio (fraction of pasture-days where the animal was fed, capped at exactly 67.99% in all 6 games — itself a sign of fully deterministic, opponent-blind play) is often *higher* than these bigger-fleet opponents' (aarav: 39.5%, protoLabs: 43.6%, cheng-han: 65.3%), yet they still win.

**This complicates D60's "6 animals collapses the economy" finding.** Re-reading the real engine's `_daily_refresh_animals` (5c): base yield (`base = 1`) is added on schedule *regardless* of `fed_today`, as long as the animal hasn't hit its 2-consecutive-unfed-day escape threshold that turn — only the care *bonus* (`pending_care_bonus`) requires same-day fed+cared. `fertilizer_available` is also set to `True` unconditionally every refresh, independent of feeding. So a larger, imperfectly-fed fleet (feed ratio well under 100%, as every real opponent above runs) can still out-produce a smaller, near-fully-fed one, provided the anti-death guard (D59's `_pasture_priority`, already shipped) keeps it under the 2-day threshold. D60's local collapse at 6 animals wasn't actually about fed_ratio or animal death (unfed_events were elevated but no deaths were logged in that test either) — the local trace pointed to feed-wheat *purchase cost* scaling linearly with fleet size plus the reserved-tile scheme's crop-capacity loss, both draining the budget/tile supply that funds the melon dump this whole economy depends on. Real opponents evidently solve this differently — whether by not reserving as many exclusive near-shed tiles, growing more of their own feed wheat organically, hiring more (5 of 6 opponents hire 10-12.5/day late-game vs. v7.2's ~8.3-8.6, total 275-317 vs. v7.2's ~212-216), or simply running a fundamentally different portfolio (crop-light/animal-heavy, or the reverse) isn't yet known from replay data alone — worth a real experiment before concluding 4 is actually the right ceiling against ladder-realistic opponents rather than just against a fixed v7.1 clone.

**Second finding: v7.2's own play is completely deterministic through day 10, regardless of opponent.** Money at day 5 ($588) and day 10 ($388) is identical to the dollar across all 6 replays. Land unlock always lands on exactly day 11 for all three purchasable quadrants (budget-gated, not date-gated — v7.2 spends everything on the 4-cow buildout/seeds/hires through day 10 and only affords land once a melon dump refills the budget around day 11+). Two of six opponents (AdamBelniak, cheng-han) unlock their second quadrant on day 0 — an immediate land-first purchase before anything else — and both beat v7.2 comfortably. Untested whether land-first sequencing would help v7.2 specifically, but it's a concrete, cheap experiment (three numeric threshold changes, no architecture change) and both real winners in this small sample used it.

**Third finding: WHEAT is being left on the table.** `PLANT_PRIORITY = ["MELON", "STRAWBERRY", "CARROT", "WHEAT"]` ranks it last, so despite `BUY_SEED WHEAT` firing for 4-6 units in every single game, WHEAT is planted 0-2 times per game (fully starved of plant slots by the higher-priority crops) — yet 4 of 6 opponents sell 217-1125 units of WHEAT, sometimes as a primary revenue source (AdamBelniak: 1125 sold, near-monoculture, still beat us). WHEAT is also v7.2's own feed input — a real organic surplus would reduce the JIT `BUY_PRODUCT WHEAT` cost that D60's diagnosis flagged as part of the fleet-scaling budget drain, so this connects directly to the fleet-ceiling question above rather than being a separate issue.

**Not attempted yet — all three findings above are diagnosis, not fixes.** No file changes made from this replay round. Next step if Grace wants it: a v7.3 experiment that (a) re-tests a higher FLEET_TARGET now specifically diagnosing whether the wheat-purchase cost or the tile-reservation crop-crowding is the actual bottleneck (rather than assuming both matter equally), (b) tries land-first purchase sequencing, and (c) reconsiders WHEAT's PLANT_PRIORITY ranking given it's both a revenue crop other real opponents use profitably and v7.2's own feed input.

### 5f. v8 design spec review (Aug 4, 2026)

Grace shared a ChatGPT proposal for a "self-improving meta-agent" (strategy classifier → decision engine → meta-agent choosing between policies). I pushed back on two points before any design doc existed: (1) Kaggriculture is NOT imperfect-information — `perceive()` and `analyze_losses.py` both already read `obs["farms"][1-p]` directly, so opponent tiles/money/animals/land are fully visible every turn, meaning "strategy recognition" is direct state-reading, not Bayesian inference; (2) none of the 6 real loss replays (5e) show evidence that *reacting differently to the opponent* would have changed the outcome — all 6 losses trace to v7.2's own policy ceilings (FLEET_TARGET=4, WHEAT starved of plant priority, day-11 land timing), not to misjudging the opponent. I recommended fixing those three concrete gaps before investing in any classifier/meta-agent architecture.

The revised spec (`kaggriculture-v8-design-spec.md`, full text saved to the project folder) incorporates both corrections directly: drops the Bayesian classifier and meta-agent from the MVP, reframes "opponent state" as a directly-read `opponent_summary` (not inferred), and opens with an explicit "Phase 0: close proven v7.2 gaps" (fleet ceiling, wheat mismatch, land timing, static melon dump) before any broader EV-engine rewrite. Reviewed the full spec against what we actually know:

- **Good:** the opponent-sensitivity test (§7 — score the same decision against the actual opponent state vs. a neutral one, diff the two) is a genuinely useful empirical tool for deciding which decisions actually need opponent-awareness, rather than assuming. The champion/challenger process (§12: paired seeds, symmetric seats, fresh validation seeds before promotion) matches the testing discipline that's already caught bad "obviously correct" ideas twice in this project (D54, and the v8 proposal's own first draft). Phasing the fleet-ceiling/wheat/land/selling fixes as a standalone "Phase 0" before the rest is the right call — it's genuinely testable and matches what the replay evidence actually supports.
- **Missing:** the animal-expansion EV formula (§6.1) includes "risk of missed feeding" as a cost term but doesn't reflect the actual engine mechanic found in 5e — base MILK/WOOL/FERTILIZER yield ticks on schedule regardless of `fed_today` (only the *bonus* needs same-day feed+care, per `_daily_refresh_animals`). That should lower the effective cost of imperfect feeding in the formula relative to what the spec currently implies, since a real ladder fleet can apparently run well under 100% fed ratio (opponents in 5e ran 39-65%) and still out-produce a smaller, near-fully-fed one.
- **Slightly overstated:** §2.4 characterizes selling as fully calendar-driven ("static"), but `economy()`'s sell logic already has some live-price reactivity (the `price_now >= 1.05*base` dump trigger, and the frac-based floor outside attack windows) — what's actually calendar-fixed is specifically the *big* `is_attack` dump window (~day 9-10/19-20, hardcoded seed 42, independent of the real price level that day). Worth sharpening Phase 2's target to that specific mechanism rather than "selling in general."
- **Scope/deadline risk:** the full spec (Phases 1-6: unified state object, opponent analyzer, EV scoring across every decision category, forecasting, policy coordination) is a substantial rewrite against a Sep 23 deadline, and this project's own history (D54, the literal-consensus v7.1 draft) shows elaborate multi-term formulas that look right on paper have repeatedly failed local A/B testing. With only a handful of real replays available to calibrate against, an elaborate multi-coefficient EV model risks overfitting to this specific loss sample. Recommendation: treat Phase 0 as its own real release (effectively v7.3) with its own promotion gate, before committing further phases — consistent with the spec's own ordering, just flagging it as a hard stopping point to evaluate at, not just a soft first step.

No file changes to any agent version yet — spec review only, Grace hasn't asked for a build.

**Addendum — quantified the "static selling" gap directly from the 6 loss replays:** pulled every SELL order v7.2 placed alongside the live market price at that instant. In every single one of the 6 games, v7.2 sells its day-11 melon dump well below base price ($43-209 vs. $250 base, `is_attack`'s fixed ~65-85% dump ratio firing regardless of the actual price that day) — and, more strikingly, sells a further **800 units across 11 separate orders at literally the $1 price floor** across the 6 games (avg ~133 units/game, mostly MELON, in the day 23-28 window, well before the day-28 `LIQUIDATE_DAY` cutoff). This traces to `force_dump` (`shed_load > SHED_CAP-15` i.e. >85/100, `hour>=18`): once the shed is nearly full, the sell logic dumps the *entire* remaining quantity of an item with zero price floor, because production (melon harvests, mostly) is outpacing what the market can absorb at a reasonable price. This is a bigger, sharper, and now fully quantified version of what design doc 5e and the v8 spec §2.4 described more loosely as "static selling" — worth promoting to the top of any Phase 0 list, since giving away ~130 units/game at $1 each is plausibly worth more than the margin in at least one of the 6 losses (90010183 lost by only $243, and shows a 78-unit sale at $13 and a 90-unit sale at $1 in its own log).

## 6. Decision Log (traceability)

Each major decision, its driver, and its provenance, grouped by the phase it came from. Sources: S1 = simulation-competition analysis (Lux comparison), S2 = "algorithms over business sense" analysis, S3 = hierarchical MAPF/MILP architecture proposal, S4 = review of my critique of S3, S5 = code review during the v1→v2 build round. CR = code review generally; later phases are named for the round they came out of (Gemini review, ladder validation rounds, DeepSeek review).

**Founding architecture** (from S1–S4, pre-build)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D1 | Rules-first architecture, ML deferred | Lux AI precedent: heuristics + exact math dominate; RL rarely tops | S1, accepted |
| D2 | World model as pure, unit-tested functions copied from engine | State bugs silently poison all layers; open source makes exactness free | S1, accepted and strengthened |
| D3 | Add standing evaluator (risk keyed to public money differential) | Ladder scores win/loss only, not margin | S2, accepted |
| D4 | Reject 40% effort on MCTS/deep-RL opponent counter-strategy | Contradicted by S1 precedent and branching factor; bad ROI | S2, rejected |
| D5 | Correct: opponent shed is PRIVATE | S2 claimed it public. Opponent modeling must infer sell timing, not read it | S2 error, caught vs engine |
| D6 | Reject MAPF/collision layer entirely | Engine: units CAN co-occupy tiles. No deadlock exists | S3 error, caught vs engine |
| D7 | Reject statistical price-elasticity fitting | Price function is published and deterministic; copy it | S3 error, caught vs engine |
| D8 | Correct: shed persists across days | S3 claimed nightly erasure; only overflow past cap 100 is lost. Multi-day holding is legal, enabling paced selling | S3 error, caught vs engine |
| D9 | Adopt Hungarian assignment as a future upgrade | Fixes greedy misallocation; milliseconds via off-the-shelf solver | S3, accepted (later demoted, see D35) |
| D10 | Adopt shed buffer guard | Paced selling + 100 cap + destroy-on-overflow creates a new failure mode | S3, accepted |
| D11 | Adopt plant-then-water invariant | Planting day counts as first unwatered day | S3, accepted |
| D12 | Sequencing: ceiling weights (scheduling 50%) do not dictate build order | Foundation and survival come first regardless of endgame differentiators | S3 weighting, reframed |
| D13 | Price is a deterministic function of an adversarial input; forecast the inventory path, not just today's number | "Copy the formula" alone invites a static-calculator mental model | S4, accepted |
| D14 | Crude opponent harvest calendar moves INTO v2 (was a "later" layer) | Paced selling is defined over the inventory forecast; ignoring opponent flow means holding into foreseeable gluts | S4, accepted |
| D15 | Reject Minimax for the market game | Opponent production is public and computable; only sell timing is hidden, one narrow band of uncertainty, not a deep game tree | S4, pushed back |

**v1 → v2 build round** (code reviews, source S5)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D16 | Reject "fatal fall-through bug" | Unreachable via caller gating; instrumented at 0 occurrences | CR, rejected |
| D17 | Adopt defensive plant-target filter; keep the local seed decrement | The decrement is the two-PLANT-one-seed protection, not dead code | CR, accepted |
| D18 | Eval harness discipline | Promotion gate, snapshot league, failure-mode tagging | S5, accepted |
| D19 | Phase FSM keyed to the day-10/20 town demand steps | Aligns strategy phase with the actual demand schedule | S5, accepted |
| D20 | Price-threshold / town-consumption-bounded selling as the default policy | Simple, robust default before paced-selling refinements | S5, accepted |
| D21 | Defer bandit learning and JAX rewrite | Mis-sized for a solo builder at this stage | S5, deferred |
| D22 | Crop portfolio computed from engine params; melon = strongest mid-game crop | README throughput table is wrong for tomato | S5 error, caught vs engine |
| D23 | Reject "task-loss bug" | Task lists rebuild every turn; audit showed every plant watered daily | CR, rejected |
| D24 | Weed neglect quantified | v1 ends with ~50 weeds vs v2's 6–8 | S5, accepted |
| D25 | Animals promoted to exploration; land aggression made an A/B experiment | Both flagged as high-value unknowns worth testing | S5, accepted |
| D26 | Reject "slightest glut floors it" | Melon glut sensitivity quantified: 72 units sellable from equilibrium before price < $200 | S5 error, caught vs engine |

**v2 patch round** (Gemini review)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D27 | Same-night-death guard | No planting after hour 20 + freshly planted tile joins urgent-water; engine kills an unwatered new plant that night | Gemini review, accepted |
| D28 | Harvest one-time crops at yield cap OR max day (melons cap on day 10, not 12) | Wins the 10/10 promotion gate and adds a market-timing weapon | Gemini review, accepted |
| D29 | Seed purchases capped by plantable space | Prevents buying seed that can never be planted | Gemini review, accepted |

**Ladder round 1** (validation episode + replay analyzer)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D30 | Compute budget resolved: 1s/turn, 1200s/game | Guard must log swallowed exceptions loudly | Ladder validation, resolved |
| D31 | Capital crunch root cause found | Per-turn seed top-up outspent the land gate; quadrant 2 delayed to day 13 | Replay analysis |
| D32 | Mid-game income desert flagged | Days 15–20 flat | Replay analysis |
| D33 | Shed cap grazed on melon harvest days | Flags a near-miss failure mode for the buffer guard | Replay analysis |
| D34 | Land-first capital priority promoted | Land order precedes seeds from day 1+; 10/10 promotion gate, +22% | Replay analysis, accepted |

**Ladder round 2** (six real losses)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D35 | Losses are strategic, not environmental | Full runs at 21ms/turn (2% of budget); Hungarian allocator demoted — zero losses attribute to allocation | Replay analysis |
| D36 | Two-sided sell logic with smooth shed-pressure relaxation | Fixes the hold/dump death spiral: held melons filled the shed, force_dump sold 98 at the $1 floor | Replay analysis, accepted |
| D37 | Animal economy promoted to core | Cows/sheep + feed + strawberries; ongoing production is structurally immune to wave-glut front-running (the $96k build) | Replay analysis, accepted |
| D38 | Hires to 7–8/day; portfolio reactivity to the opponent's visible build | Tunes throughput and responsiveness against real opponents | Replay analysis, accepted |
| D39 | Death spiral confirmed in every v2q loss | 42–63% of melons sold at ≤$30; v3 fix pre-validated | Replay analysis |
| D40 | Correct: fertilizer IS sellable (docs wrong) | Every fed animal mints ~$46–100/day extra; verified via market inventory (+301) | Docs error, caught vs engine |
| D41 | JIT feed via market churn is near-free warehousing | Wheat chronically scarce (~$45 vs $25 base) in the animal meta, making wheat farming a picks-and-shovels play | Replay analysis, accepted |

**v3 review round** (DeepSeek)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D42 | Reject "seed race condition" vulnerability | Tested — seeds never go negative; the proposed fix would reintroduce a real bug | DeepSeek review, rejected |
| D43 | Reject fertilizer-doubling and tomato-13-harvest math | Engine hard-caps yield at max_yield; third independent recurrence of the D22 trap | DeepSeek review, rejected |
| D44 | Melon cutoff stays 16 | Extension to 18 failed the gate 1/8 (late melons sell into the liquidation dump); liquidation-ramp idea deferred and linked for joint re-test | DeepSeek review, gate failed |

**Running tallies:** 9 external sources/reviewers, every one carrying at least one confidently false claim; 3 documentation errors caught against the engine (shed persistence, tomato throughput, fertilizer sellability); 4 promotion gates passed (D28 build, D34, D36/v3a, D38/v3b) and 1 failed (D44); ladder record 0W/6L/1T with all six losses to animal builds, which is what makes v4 the animal economy.

**Engine-source verification + v7.1 build round** (real vendored `kaggriculture.py`, ChatGPT + GLM reviews of v7, local head-to-head testing)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D45 | Real engine source vendored, supersedes replay-mining as ground truth | Found on GitHub master branch, not yet on PyPI; resolves D42/old-blocker | Direct source fetch |
| D46 | Cow cost is a flat $400, not ~$1,000-1,200 | `ANIMALS["COW"]["cost"]` in engine source; both v6.1 and v7 guessed high from replay mining | Engine source, caught vs both agent files |
| D47 | Shed-access tiles are exactly (4,4),(5,4),(4,5),(5,5); v6.1's SHED_POS=(0,0) is wrong and unfixed | `_shed_access_tiles`; v6.1's animal pipeline would never complete on real ladder | Engine source, caught vs v6.1 |
| D48 | Hands, farmer position, and per-unit inventories reset to empty EVERY day, unconditionally | `_end_of_day`; confirmed empirically in a real ladder replay (hand count 3→0→3→0→5 at day boundaries). No version built so far (v5/v6/v7) modeled this | Engine source + replay cross-check |
| D49 | Market orders hard-capped at 10/turn by engine config, independent of agent code | `maxMarketOrdersPerTurn`; makes GLM's "$6,764/day to hire 18 hands" claim impossible — real worst case ~$143/day | Engine source, caught vs GLM review |
| D50 | Animal lost permanently (no refund) after 2 consecutive unfed days | `_daily_refresh_animals`; neither v6.1 nor v7 guarded against this explicitly | Engine source |
| D51 | DemandTimingEngine is fully deterministic (hardcoded seed 42), not randomized | Both v6.1 and v7 use `random.Random(42)`, not the real episode seed | Code inspection, caught vs both ChatGPT and GLM reviews |
| D52 | ChatGPT's 7 v7-regression claims: 6 confirmed, 1 refuted | v6.1 does NOT have deterministic Day-10/20 timing — byte-identical DemandTimingEngine to v7, see D51 | ChatGPT review, mostly accepted |
| D53 | GLM's two new claims (hire-cost bankruptcy, schema hallucination) both rejected | Hire cost capped by D49, not unbounded; schema came from real v5 loss replays (5b), not fabricated — GLM conceded after being shown the matching JSON | GLM review, rejected |
| D54 | Literal-consensus draft (hand cap 8, dynamic planting guard, task-remove-on-arrival fix, hire/seed-before-sell ordering) rejected after losing to v7 ~2.5x head-to-head | All four "obviously correct" fixes independently starved the day-10 melon-dump strategy this economy's profit depends on; see 5c for full mechanism, especially the daily-wipe interaction with task removal | Local seeded self-play, rejected |
| D55 | v7.1 built: keeps real hire-cost accounting, real cow economics, feed-priority starvation guard, and a non-destructive hire/seed starvation floor (bump lowest sell order only if all 10 slots full); reverts hand cap, planting guard, and task-removal timing to v7's originals | Beats v7 5/5 on seeded trials after the reverts, vs. losing 2.5x before them | Local self-play, promoted |

**v7.2 multi-animal fleet round** (see 5d for full detail)

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D56 | `cow_state` replaced with generic `animal_plans` list; purchases strictly sequential (one plan BOUGHT/CARRYING at a time) | Enables multiple animals of multiple species with a single farmer, without the harder problem of parallel carries | Outside critique + design doc scaling plan |
| D57 | `configuration={"seed": N}` does NOT propagate to the engine's real weed-spawn RNG — must set `env.info["seed"] = N` directly | Confirmed empirically: identical results across configuration seeds until `env.info["seed"]` was set explicitly; engine reads `env.info.get("seed", 0)` in `_end_of_day` | Local test harness, caught before trusting any seeded A/B numbers |
| D58 | Reserve `FLEET_TARGET`-total near-shed tiles for pastures from turn one, excluded from crop planting immediately | Late-firing purchases were claiming far-from-shed sites once nearby tiles were already planted, risking a 2-consecutive-unfed-day animal loss | Local A/B testing, animal-death root cause #1 |
| D59 | Pasture maintenance targets highest-*need* pasture, not nearest one (`_pasture_priority`) | `cow_maintenance_action`'s pure-nearest selection silently starved a second pasture whenever the nearest one had nothing pending — animal-death root cause #2, more significant than #1 | Local A/B testing (turn-by-turn debug trace) |
| D60 | FLEET_TARGET capped at `{"COW": 4, "SHEEP": 0}` for shipping; 6 total animals (tested as both 4+2 and 6+0) rejected | Both configurations collapsed the economy to ~$2-5k (worse than v7.1's baseline) via feed-wheat cost scaling + reserved-tile crop-capacity loss starving the melon dump — not a graceful degradation | Local seeded self-play, gate failed at 6 |
| D61 | STRAWBERRY added to PLANT_PRIORITY/CUTOFF, ranked below MELON | Only attempted after fertilizer logistics confirmed reliable at 4-cow scale; improved money further with no observed MELON crowding-out | Local self-play, promoted |

**Running tally addition:** the outside critique that prompted this round (structural diagnosis: single-cow cap, no sheep pipeline, controlled-scaling methodology) was directionally correct and empirically vindicated — the predicted single-farmer bottleneck materialized exactly as warned, at 6 animals. But its proposed *mechanism* (implicitly, travel distance / raw carrying capacity) wasn't the actual cause; the dominant bug was a nearest-pasture selection blindness only visible by running games, consistent with the meta-lesson from 5c one level deeper.

## 7. Open Questions

- ~~Where is `kaggriculture.py`?~~ Found on GitHub (Kaggle/kaggle-environments, master branch) and vendored — see 5c. Real engine source now supersedes replay mining wherever they'd conflict.
- ~~Is the 10-order market cap real? Per-category limits?~~ Resolved (D49): 10/turn is a real, hardcoded engine config default (`maxMarketOrdersPerTurn`), enforced independent of agent code. No per-category limits exist in the engine — any category reservation is agent-side policy only, and v7.1 found that pre-reserving categories (rather than a floor-only fallback) actively hurts (D54/D55).
- ~~Animal purchase prices and per-species yield/feed economics beyond COW~~ Resolved for both COW and SHEEP (D46, D56): COW $400/first_yield_day=8/interval=2/max_held=6, SHEEP $500/first_yield_day=6/interval=3/max_held=6, both structure="PASTURE". SHEEP's purchase pipeline is built and verified working in `main_v7.2.py` (ANIMAL_SPECS/animal_plans), just shipped at FLEET_TARGET 0 pending the v7.3 capacity work (D60).
- NEW: what would let the fleet scale past 4 animals without collapsing the economy (D60)? Two candidate approaches, neither attempted yet: (a) a feasibility gate that only allows the next animal purchase if the single farmer's projected daily feed-wheat cost + travel time stays within budget/turn limits, or (b) dedicating a second hand specifically to animal maintenance duty, freeing the farmer for setup/crops. Worth testing both before assuming either works.
- New: is COW_BUY_START_DAY=3 actually optimal now that the real $400 cost is known? Untested on the ladder — v7.1 kept it at 3 (cheap enough to plausibly be fine) but this specific parameter wasn't part of the local A/B testing that validated the rest of v7.1's changes. Worth a dedicated harness sweep (day 3 vs 6 vs 10) before the next ladder run.
- New: does the "hire/seed starvation floor bumps the lowest sell order" mechanism in v7.1 ever actually trigger in practice, and does it help when it does? Not directly observed in the 5-seed test batch — worth confirming with instrumentation before trusting it blindly.
- ~~What actually went wrong in the submitted v5 games~~ Resolved by ladder rounds 1–2 (D31–D34, D35–D41): capital-crunch timing bug, then a hold/dump death spiral confirmed in every animal-build loss. Remaining: the fix (D36/D39) is pre-validated but not yet proven on the ladder — record is still 0W/6L/1T.
- ~~Whether the v5 demand-timing engine (hold-then-dump) wins or loses vs. simple paced selling~~ Answered: it loses — it's the death-spiral mechanism itself (D39). Replaced by two-sided sell logic with smooth shed-pressure relaxation (D36). Not yet A/B'd on the ladder.
- ~~Compute budget per turn on Kaggle's runners~~ Resolved: 1s/turn, 1200s/game; real usage measured at 21ms/turn (D30, D35).
- Optimal crop portfolio by season phase awaits ROI computation on the world model
- Opponent sell-lag estimation method: fixed assumption vs. Bayesian update from observed price deltas
- Whether the shed cap ever binds hard enough to justify hand-inventory staging tactics (D33: grazed on melon harvest days, not yet a hard binding case)
- Whether wheat farming is worth building out as a standalone play now that D41 flags it as chronically scarce (~$45 vs $25 base) in the animal meta
- D44's liquidation-ramp idea for extending the melon cutoff past day 16 — deferred, needs joint re-test with the sell-logic fix
- The three v6-review requirements (schema-verification gate, no strategy changes disguised as reliability fixes, lifetime attempt caps on state machines) were previously logged as D42–D44 but are superseded by this renumbering — they're preserved narratively in 5a/5b but currently have no decision-log entry. Worth a deliberate renumbering pass if they should stay traceable in section 6.

---

## 8. V8 Phase 1 — Foundation (`main_v8.py`)

**Status:** built, verified as an exact behavioral no-op vs `main_v7.6.py`. Not submitted to the ladder (there is no reason to — it plays identically to v7.6, which is the current champion).

**Why a deliberately inert release.** The v8 design spec (`kaggriculture-v8-design-spec.md`) scopes six phases. This project's consistent experience across the v7.1, v7.2, v7.5, v7.6 and v7.7 rounds is that a change only earns trust through seeded A/B testing, and that plausible-sounding changes fail that test often enough to make it non-negotiable. A foundation that also changed behavior could not be A/B'd cleanly: any regression would be unattributable between "the refactor broke something" and "the new policy is worse." So the substrate ships first, provably inert, and each behavioral change is tested against it one at a time.

### 8.1 What Phase 1 adds

| Component | Purpose | Spec ref |
|---|---|---|
| `build_state()` | One normalized read-only state object per turn: `my` / `opponent` / `market` / `capacity`. Nothing reads it for decisions yet. Phase 2+ scorers read it instead of digging into raw `obs` at each call site — that shared basis is what makes decisions comparable. | 5.1 |
| `analyze_opponent()` | Direct extraction of the opponent's visible farm: crop tiles, mature and near-mature counts, fleet by species, land, hands, and a Herfindahl concentration score. Not a classifier — Kaggriculture is fully observable, so present-state facts are read, never inferred. | 5.2 |
| `DecisionLog` | Records each strategic decision with the state that produced it, plus an empty `alternatives` field that Phase 2+ scorers populate without a schema change. Also `snapshot()` for per-turn mechanism traces. | 11 |
| `capacity` metrics | Crop backlog, animal workload, weed ratio, crop pressure, weighted work — surfaced together in one place. v7.6 recomputes overlapping versions of these in three separate rules with three slightly different definitions of "work"; unifying them is a later phase, because changing any definition changes behavior. | 5.1 |

**Logging is on by default** (`DECISION_LOG = True`). It initially shipped dormant, on the reasoning that a logging fault in a submitted file could cost a real match. That was reconsidered: downloaded ladder replays record what the agent *did*, not the state or rule branch that produced it, so a dormant log means real matches — the only games against real opponents — generate no diagnostic data at all, which is precisely where it is most valuable.

The cost objection did not survive scrutiny either. Measured agent time is ~21ms against a 1s/turn budget (D30/D35), the log is in-memory with no I/O, and a full 720-turn game produces 1,862 records. The *real* objection was `agent()`'s crash guard: it swallows any exception and returns a PASS turn, so a bug in diagnostic-only code could silently forfeit a turn's entire action set — invisibly, and only on the ladder.

`_log_safe(kind, day, hour, build)` closes that. It takes a **thunk** rather than assembled arguments, which matters for two reasons: the risky part of a record is the `inputs` dict (nested `.get()` chains, division by base prices, arithmetic on engine values), and passing pre-built arguments would assemble it at the call site *outside* any handler. Building it inside one try/except means a logging bug costs one record and increments `DECISION_LOG_SINK.errors` — never a turn. Taking a thunk also keeps the disabled path genuinely free, since the payload never evaluates, so `disable_decision_log()` remains a real kill switch rather than merely suppressing storage.

Harnesses call `enable_decision_log()` (which also clears prior records) and read `DECISION_LOG_SINK.records` or `.to_jsonl(path)`.

**Deliberately absent:** no EV engine, no candidate scoring, no adaptive selling. Those are Phases 2–4. v7.8's sheep work is also not merged; when it lands it becomes a scored candidate inside the Phase 4 expansion model rather than a hand-merge.

### 8.2 Verification

Static: `diff main_v7.6.py main_v8.py` removes exactly two lines — the `economy()` signature and its call site, both re-added with an optional `state=None` parameter. Every other change is additive.

Empirical: `seeded_h2h.py main_v8.py main_v7.6.py --both-seats` scores **exactly 0.0 margin on every seed**, re-confirmed after logging was switched on by default.

**Fault injection.** Monkey-patching `DecisionLog.record` to raise on every call, then playing a full 720-turn match: **1,862 logging failures, final scores bit-identical to the clean run (49,023 / 51,035), status DONE/DONE.** Total logging failure is invisible to gameplay — which is the property that makes running the log live on the ladder safe. `disable_decision_log()` was verified to produce the same scores with zero records.

**Smoke tests.** `smoke_test.py` against `starter` / `random` / `pass` at 720 turns, plus a truncated 48-turn episode: all DONE/DONE, no crashes, no `GUARD swallowed exception` output. vs `starter` scored $86,573 vs $3,494 — matching v7.6's own logged smoke-test figure exactly. (Earlier verification runs had piped stderr to `/dev/null`, which would have hidden guard messages; these were re-run with stderr captured and counted.)

**Opponent-pool no-op matrix.** v8 and v7.6 played against `starter`, `random`, `pass`, `opp_frontier_v12` and `opp_scenario_v14`, each at 720 / 48 / 3 turns (the 3-turn case exercising the early-return and terminal paths). **14 of 15 cells bit-identical**, `DECISION_LOG_SINK.errors == 0` in every cell, zero guard invocations.

The one non-matching cell was `random` at 720 turns. Control: v7.6 vs `random` at a fixed seed across four repeated runs scored 76,628 / 76,896 / 75,801 / 77,955 — a ~$2,150 spread with the agent held constant, since the built-in `random` opponent draws from its own unseeded RNG that `env.info["seed"]` does not reach. v8's value sat inside that band. **`random` is therefore not usable as an A/B opponent at all** — it is a crash-stability check only. `starter` repeated at a fixed seed reproduced exactly (77,160 twice) and is the deterministic choice.

### 8.3 D62 — `--swap-half` was never a seat control, and it invalidated the v7.7 result

Verifying the no-op surfaced a measurement bug affecting every A/B result this project has recorded.

`main_v8.py` vs `main_v7.6.py` under the standard 11-seed `--swap-half` protocol returned 2/11, mean −$2,772, min −$6,544, max +$5,407. Those are, to the dollar, the numbers recorded for v7.7's rejection. Running `main_v7.6.py` against **itself** under the same protocol reproduced the identical table.

**Cause.** `_end_of_day` builds one RNG per day and calls `_spawn_weeds` for each player sequentially from the same stream, so seat 0 and seat 1 receive different weed layouts even under identical code (this was already known from the Savko/Subin An analysis — what was missed is that it biases the harness, not just individual matches). `--swap-half` alternates which seed lands in which seat, but each seed is still played in only one seat, so the seat effect is shuffled rather than cancelled, and at n=11 it does not average out. The residual is a ≈−$2,772 offset against whichever agent is passed first.

**Consequences.**

1. **v7.7 was rejected on a false negative.** Its measured "regression" is the mirror-match table. It never demonstrably changed behavior in those 11 games. The rejection should not be treated as evidence against price-aware selling.
2. **Prior margins carry an uncorrected offset.** v7.6's +$6,081 over v7.5 and v7.5's +$4,658 over v7.3 were measured with the same protocol and the same agent-ordering. Correcting for the baseline moves both in the challenger's favor, so the promotion decisions still stand — but the *magnitudes* are wrong, and the seeds reported as near-ties or narrow losses are the least reliable of the set.
3. **The fix is `--both-seats`** (added to `seeded_h2h.py`): every seed is played in both seat assignments and summed money is compared, which cancels the seat effect exactly. An agent against itself scores a clean 0.0. Cost is 2× the games. `--swap-half` is retained only to reproduce historical numbers, and now prints a warning.

### 8.4 D63 — the calendar attack dump fires at most once per match

First real finding from the decision log, and it redirects Phase 2.

Instrumenting the six branches of the selling rule and counting them over full matches:

| Seed | attack_dump | holding_phase | price_strong | paced | liquidate |
|---|---|---|---|---|---|
| 1 | 1 | 22 | 90 | 246 | 11 |
| 42 | **0** | 0 | 92 | 197 | 10 |
| 202 | 1 | 22 | 82 | 228 | 12 |
| 8080 | 1 | 22 | 90 | 225 | 11 |

The `DemandTimingEngine` attack window is a single turn (`t in (214, 454)` — hardcoded seed 42, so identical every game), and premium-crop inventory is usually not staged in the shed at that exact instant. Out of roughly 330 sell decisions per match, **zero or one** is an attack dump.

This explains v7.7 mechanically, independent of the harness bug: gating the attack dump could only ever affect 0–1 decisions per game, so it was never going to move a score. It also means the "stronger version" proposed as v7.7's successor — comparing 0%/30%/70% dump quantities by expected proceeds — is aimed at the same near-dead branch and should be expected to do just as little.

**Phase 2 should target `paced` (197–246 decisions/match) and `price_strong` (82–92/match).** Together those are ~95% of all selling. The `price_strong` branch in particular sells an item's *entire* holding whenever price ≥ 1.05 × base, with no quantity comparison and no market-impact estimate — that is where a sell-value model has room to work.

### 8.5 Decision log additions

| ID | Decision | Rationale | Evidence |
|---|---|---|---|
| D62 | `--swap-half` deprecated as a control; `--both-seats` added and required for any actionable result | Mirror-match under `--swap-half` returns a −$2,772 mean bias, reproducing v7.7's rejection numbers exactly; per-seed margins are dominated by a seat×seed interaction | v7.6-vs-itself control run, 11 seeds |
| D63 | Phase 2 adaptive selling targets the `paced` and `price_strong` branches, not the attack dump | Branch counting over 4 full matches: attack dump fires 0–1 times per game vs ~330 total sell decisions | Decision-log branch instrumentation |
| D64 | v8 Phase 1 ships behaviorally inert, verified at 0.0 seat-controlled margin | A foundation that also changed behavior would make any later regression unattributable between refactor and policy | `--both-seats` verification, all seeds exactly 0 |
| D66 | The built-in `random` opponent is a stability check only, never an A/B opponent | Its RNG is unseeded and unreachable by `env.info["seed"]` — v7.6 against it at a fixed seed varies ~$2,150 across repeated identical runs, while `starter` reproduces exactly | 4-run control, agent held constant |
| D65 | Decision log runs ON by default on the ladder, via `_log_safe()` taking a thunk so assembly and write share one try/except | Replays capture actions but not the state or branch behind them, so a dormant log yields no data from the only real-opponent games. The lone real risk was the crash guard converting a logging bug into a forfeited turn; fault injection (1,862 forced failures) produced bit-identical scores and DONE status, removing it | Fault-injection run, seed 42 |

### 8.6 D67 — v8/v7.6 loses 0/12 to the strong fixed bots, and the gap is production volume, not sell timing

The first seat-controlled measurement of the current champion against `opp_frontier_v12` and `opp_scenario_v14` (the real bots extracted from the Hamburger notebook). Six seeds each, `--both-seats`:

| Opponent | Record | Our money | Their money | Mean paired margin | t |
|---|---|---|---|---|---|
| frontier_v12 | 0/6 | $45.6–58.0k | $127.5–146.5k | **−$165,591** | −20.1 |
| scenario_v14 | 0/6 | $49.4–60.3k | $121.0–140.0k | **−$155,641** | −34.6 |

Not noise: t of −20 and −35, and every individual seed loses by more than $135k.

**This was hiding in the record.** The v7.5 round logged our own money against these two bots ($51–57k / $52–63k) but never logged *theirs*, so a version comparison that looked like clear progress (v7.5 > v7.3 on both matchups) was measured entirely between our own versions while both were being beaten roughly 2.5:1 by the fixed opponent. The v7.4 round did record the opponent side (frontier $131–143k vs v7.4's $20–29k) — so the lineage has roughly doubled our own score since then while the target has not moved. **Any future opponent-pool result must log both sides.**

**Where the gap is.** Seed 42 vs frontier ($57,764 vs $136,495), realized sell volume from the action stream plus the v8 decision log:

| Item | v8 units | frontier units |
|---|---|---|
| WHEAT | 243 | **1,027** |
| WOOL | **0** | **263** |
| STRAWBERRY | 44 | **204** |
| FERTILIZER | 85 | 202 |
| MELON | 156 | 108 |
| MILK | 164 | 102 |
| **Total** | **731** | **1,921** |

v8's realized prices are *good*: MILK $215/unit, STRAWBERRY $221/unit, MELON $190/unit, WHEAT $48/unit against a $25 base. Prices are running well above base because town demand drains market inventory — and we do not have the goods to sell into it. Frontier also hires 324 times to our 207 and issues 252 `BUY_PRODUCT` orders to our 92.

**This partially walks back D63's Phase 2 recommendation.** D63 correctly showed the attack dump is near-dead and that `paced`/`price_strong` carry the volume — but it does not follow that selling logic is where the money is. We are selling at strong prices; we are producing roughly a third of the units. Sell-timing improvements operate on a small base.

The three largest single line items are all production, not selling:

1. **WOOL: 0 vs 263 units.** `SHEEP_ENABLED = False`. This is exactly what `main_v7.8.py` changes, and it has never been A/B'd. At WOOL's $200 base this line alone is plausibly a large fraction of the gap.
2. **WHEAT: 243 vs 1,027.** Wheat is realizing ~1.9× base, and is also our own feed input, so more of it cuts the `BUY_PRODUCT` spend too.
3. **STRAWBERRY: 44 vs 204.** Already flagged in real ladder losses (an opponent made $69,878 off 294 units in a game we lost by $22,931).

**Revised sequencing suggestion:** A/B `main_v7.8.py` under `--both-seats` before starting Phase 2, since it targets the single largest line item and is already built. Phase 2 adaptive selling should be re-scoped as a multiplier on production volume rather than as the primary lever.

| ID | Decision | Rationale | Evidence |
|---|---|---|---|
| D67 | Opponent-pool results must record both sides' money; production volume, not sell timing, is the current binding constraint | 0/12 vs frontier/scenario at −$155k to −$166k paired margin, with our realized prices strong ($48/unit wheat vs $25 base) but total sell volume 731 vs 1,921 units | 24 seat-controlled games + seed-42 decision-log breakdown |

### 8.7 D68 — v7.8 (sheep) tested and rejected: sheep are strictly worse per pasture slot at our production scale

**This supersedes the sheep recommendation in D67, which was wrong.**

`main_v7.8.py` had never been A/B'd — no result existed anywhere in this document or the project notes. Tested now, `--both-seats`, 6 seeds vs `main_v7.6.py`: **1/6, mean paired margin −$11,912** (min −$24,469, max +$3,458, stdev $9,027, t = −3.23). A real regression.

**It is not a fleet-size effect.** Final fleet sizes are essentially unchanged (v7.8 / v7.6 by seed: 11/10, 7/11, 8/8, 10/9, 10/9). The first seed inspected happened to show a shrink, which would have been the wrong conclusion from one game.

**The actual mechanism — a fixed, unfavourable product substitution.** Across every seed tested:

| Seed | Δ MILK units | Δ WOOL units | Δ money |
|---|---|---|---|
| 1 | −94 | +62 | −$9,150 |
| 7 | −96 | +53 | −$12,614 |
| 99 | −88 | +61 | −$5,705 |
| 123 | −85 | +60 | −$6,714 |
| 202 | −97 | +56 | −$10,689 |

Roughly 90 milk units traded for 58 wool units, every time — a ratio of ~1.55. That is the engine's yield-interval ratio almost exactly:

```
COW:   cost 400, first_yield_day 8, interval 2, MILK base $160  ->  $80.0/day
SHEEP: cost 500, first_yield_day 6, interval 3, WOOL base $200  ->  $66.7/day
```

3/2 = 1.5 observed as 1.55. A sheep occupies the same pasture slot, consumes the same 1 WHEAT/day (feed is species-agnostic in the engine), and demands the same care labour as a cow — while costing **25% more** and producing **17% less value per day**. Swapping cows for sheep is a downgrade on identical resources.

**Sheep's one real advantage is worthless to us right now.** Sheep yield 2 days earlier (day 6 vs 8), and diversifying avoids saturating the MILK market. But v7.6 realizes MILK at **$215/unit against a $160 base** — milk price sits *above* base for the whole match, meaning we never sell enough to depress it. There is no saturation to hedge against, so we pay sheep's full cost for none of its benefit. Diversification into WOOL only starts paying once MILK volume is high enough to push realized milk price below wool's, which is a problem we do not have.

**Correcting D67.** D67 read "WOOL 0 vs 263 units" as the largest addressable line item and recommended enabling sheep. That inverted cause and effect. Frontier's 263 WOOL is not a species choice we can copy — it is a symptom of an animal economy roughly twice our size, funded by a crop economy roughly four times ours (1,027 WHEAT to our 243). Species substitution cannot close a scale gap; at our scale it makes things worse.

**What this leaves.** The production-volume diagnosis in D67 stands — 731 units to frontier's 1,921 — but the lever is **scale**, not **mix**. The open question is why our fleet plateaus around 8–11 animals and our wheat output sits near 243 units while frontier reaches 1,027, not which animal fills a pasture. `SHEEP_ENABLED` should stay `False` unless milk saturation ever actually appears in the decision log.

| ID | Decision | Rationale | Evidence |
|---|---|---|---|
| D68 | v7.8 rejected; `SHEEP_ENABLED` stays False until MILK realized price falls below base | Sheep cost 25% more, yield 17% less value/day, and occupy identical slot/feed/labour; observed as a fixed ~90 MILK for ~58 WOOL trade on every seed, matching the engine's 3:2 interval ratio. Their diversification benefit is nil while MILK realizes $215 against a $160 base | 12 seat-controlled games + 5-seed mechanism trace |

### 8.8 D69 — the top bug is order-slot contention in hiring, which no v8 phase addresses

Following D67's "scale, not mix" conclusion, the decision log was used to find what actually caps our scale. Seed 42 vs frontier_v12 ($57,764 vs $136,495).

**Ruled out first.** Seed purchases do *not* freeze — v8 buys seeds on 21 of 30 days, last purchase day 26. The seed-freeze pattern from the v7.5 ladder replays was genuinely fixed by v7.6 and is no longer a live issue. Land completes by day 11 (all 4 quadrants). Budget is not binding late: the hire loop reports $23,558 / $34,933 / $41,183 left over on days 24 / 26 / 28.

**The binding constraint is labour, and not for the reason the hiring formula thinks.** `work` climbs to 101–112, so `target = ceil(work/5)` pins to the `HAND_TARGET_MAX = 18` cap on **17 of 29 days**. v7.6 duly issues up to 18 `HIRE` orders. But actual hands held, sampled at hour 12, are only **5–9** — and *declining* late (day 28: 5).

The orders do not land:

| | v8 / v7.6 | frontier_v12 |
|---|---|---|
| Total HIRE orders | 207 | **324** |
| Hours of day used for hiring | **{1}** | **{1, 2}** |
| Mean hires/day | 6.9 | **10.8** |
| Turns at the 10-order cap | 23 | 28 |
| Hands held (day 12→28) | 8, 9, 6, 8, 5 | **12, 12, 12, 12, 11** |

v7.6 fires its entire daily hiring burst inside a single turn (`if hour == 0`), where the engine's hard `maxMarketOrdersPerTurn = 10` is shared with sells, seeds, land, animals and feed. Frontier splits hiring across **two** turns per day and consequently lands ~57% more hands. Because hands wipe to zero at every day boundary, this is re-paid daily — it is not a one-off.

So the hiring formula asks for 18, the budget can afford 18, and roughly 7 arrive. Every downstream throughput number — watering, weeding, harvesting, wheat output — is gated by that.

**Does any v8 phase address this? No.**

| Phase | Addresses the scale gap? |
|---|---|
| 2 — Adaptive selling | **No.** Aimed at a non-problem: realized prices are already above base (MILK $215/$160, WHEAT $48/$25). Its stated rationale — "large score variation from realized melon prices" — is not what these games show. |
| 3 — Unified crop/seed scoring | **Partly, but its premise is stale.** Its headline goal is eliminating purchased-but-unused seeds; seeds no longer freeze. Tile-allocation gains may remain. |
| 4 — Adaptive animal/land expansion | **Partly.** Section 6.3 models the marginal value of the *next hand* — but it assumes a hire decision executes. Here the decision is correct and does not execute. |
| 5 — Forecasting / 6 — Coordination | No. |

The spec's framing is "compare candidate actions on a shared value model." This bug is a different species: the chosen action is right and fails to land because order slots are a scarce resource the agent never allocates deliberately. Section 3 lists "market-order limit" under *real constraints to keep hard-coded*, and section 12 states the execution layer "remains stable unless replay evidence identifies a mechanical failure" — this is that mechanical failure.

It is also a reminder that the spec was written against **v7.2** and is three versions stale: its evidence items 2.1 (hard fleet ceiling) and 2.2 (wheat seed/planting mismatch) are already fixed.

**Cheapest next experiment:** spread the daily hire burst across two or three turns instead of one, so hire orders stop colliding with sell orders for the same 10 slots. Pure scheduling change, no new model, directly targets the measured bottleneck.

| ID | Decision | Rationale | Evidence |
|---|---|---|---|
| D69 | Order-slot contention, not decision quality, is the current top bug; hire spreading is the next experiment | Hiring asks for 18/day with budget to spare, but fires in one turn against a shared 10-order cap and lands ~7; frontier splits across two turns and holds 12 hands to our 5–9 | Decision-log + action-stream analysis, seed 42 |
