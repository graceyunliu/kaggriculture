# Kaggriculture Agent: System Design Document

**Status:** v5 submitted (issues found); v6 diagnostic hybrid built and reviewed, NOT submission-ready
**Last updated:** August 4, 2026 (post-v6 review)
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
| Later | Refined opponent sell-lag model from observed price moves; local search on discrete decisions (land timing, sell-now-vs-hold) via forward simulation; mutual-glut timing game; Hungarian assignment; real animal economy once schema verified | Backlog |

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

**Newly confirmed v6 bugs beyond 5a:**

7. **Fatal perceive bug:** occupied pastures match v6's `kind == "PASTURE"` branch first, so they never reach the `animals` list — v6 would never feed, care for, or milk any animal. The cow starves (`consecutive_unfed` climbs) and VERIFY_ACTIVE fails → possible re-buy loop even when everything worked.
8. **FEED requires carried wheat:** opponents `PICKUP WHEAT` from the shed, walk to the pasture, then `FEED`. v6 only buys wheat into the shed and never routes a carrier — its FEED would fire with empty hands.
9. **PLACE arg mismatch:** v6 emits `["PLACE","COW",1]`; every observed animal placement is `["PLACE","COW"]`.
10. v6's fertilizer-flag guesses (`fertilizer_ready`/`has_fertilizer`/`manure_ready`) are all wrong — the real key is `fertilizer_available`. Its `fed_today`/`cared_today`/`yield_units` guesses were correct (moot given bug 7).

Explicitly rejected: MAPF/collision pathfinding (no collisions exist), statistical price fitting (formula is published), end-to-end RL as skeleton (poor ROI per Lux precedent), global tree search (branching factor hopeless; information structure doesn't require it).

## 6. Decision Log (traceability)

Each major decision, its driver, and its provenance. Sources: S1 = simulation-competition analysis (Lux comparison), S2 = "algorithms over business sense" analysis, S3 = hierarchical MAPF/MILP architecture proposal, S4 = review of my critique of S3.

| # | Decision | Rationale | Source / trigger |
|---|---|---|---|
| D1 | Rules-first architecture, ML deferred | Lux AI precedent: heuristics + exact math dominate; RL rarely tops | S1, accepted |
| D2 | World model as pure, unit-tested functions copied from engine | State bugs silently poison all layers; open source makes exactness free | S1, accepted and strengthened |
| D3 | Add standing evaluator (risk keyed to public money differential) | Ladder scores win/loss only, not margin | S2, accepted |
| D4 | Reject 40% effort on MCTS/deep-RL opponent counter-strategy | Contradicted by S1 precedent and branching factor | S2, rejected |
| D5 | Correct: opponent shed is PRIVATE | S2 claimed it public; engine README says otherwise. Opponent modeling must infer sell timing, not read it | S2 error, caught vs engine |
| D6 | Reject MAPF/collision layer entirely | Engine: units CAN co-occupy tiles. No deadlock exists | S3 error, caught vs engine |
| D7 | Reject statistical price-elasticity fitting | Price function is published and deterministic; copy it | S3 error, caught vs engine |
| D8 | Correct: shed persists across days | S3 claimed nightly erasure; only overflow past cap 100 is lost. Multi-day holding is legal, enabling paced selling | S3 error, caught vs engine |
| D9 | Adopt Hungarian assignment as v3 upgrade | Fixes greedy misallocation; milliseconds via off-the-shelf solver | S3, accepted |
| D10 | Adopt shed buffer guard | Paced selling + 100 cap + destroy-on-overflow creates a new failure mode | S3, accepted |
| D11 | Adopt plant-then-water invariant | Planting day counts as first unwatered day | S3, accepted |
| D12 | Sequencing: ceiling weights (scheduling 50%) do not dictate build order | Foundation and survival come first regardless of endgame differentiators | S3 weighting, reframed |
| D13 | Price is a deterministic function of an adversarial input; forecast the inventory path, not just today's number | "Copy the formula" alone invites a static-calculator mental model | S4, accepted |
| D14 | Crude opponent harvest calendar moves INTO v2 (was a "later" layer) | Paced selling is defined over the inventory forecast; ignoring opponent flow means holding into foreseeable gluts | S4, accepted |
| D15 | Reject Minimax/tree search for the market game | Opponent production is public and computable; only sell timing is hidden, one narrow band of uncertainty, not a deep game tree | S4, pushed back |
| D16–D41 | *(gap — not recorded here)* | Code and harness reference D18, D30–D34 (harness/replay archive), D40 (fertilizer liquidation), D41 (JIT feed buying); these decisions were made during v2–v5 iteration but never logged in this doc | Process failure, noted Aug 4 |
| D42 | No animal economy code ships until action names and tile/shed schema are read from `kaggriculture.py` | v6's cow machine is built entirely on guessed vocabulary; a wrong guess is at best wasted turns, at worst a repeated-purchase money leak (see 5a.2) | v6 review |
| D43 | Reliability fixes must not change strategy parameters | v6 bundled fleet/planting scale-downs into a "safeguards" changelog; strategy changes need their own self-play A/B, not a free ride | v6 review |
| D44 | Any multi-turn state machine needs a lifetime attempt cap, not just per-stage retries | Per-stage retry + timeout can still cycle forever through IDLE→retry at the top level | v6 review, triggered by 5a.2 |

## 7. Open Questions

- ~~Where is `kaggriculture.py`?~~ Engine source does not exist locally; **replay mining now serves as ground truth** (see 5b — animal schema, action vocabulary, and worker inventories all recovered from loss replays). Still unverified: market order slot rules (is the 10-order cap real? per-category limits?), exact watering/decay thresholds, animal purchase prices, and per-species yield/feed economics — all extractable from replays with more mining.
- What actually went wrong in the submitted v5 games — loss replays exist in `Replays/Losses/` but haven't been systematically ingested through the harness
- Whether the v5 demand-timing engine (hold-then-dump around day 10/20) wins or loses vs. simple paced selling — never A/B'd
- Optimal crop portfolio by season phase awaits ROI computation on the world model
- Opponent sell-lag estimation method: fixed assumption vs. Bayesian update from observed price deltas
- Whether the shed cap ever binds hard enough to justify hand-inventory staging tactics
- Compute budget per turn on Kaggle's runners (bounds any per-turn simulation depth)
