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

## Complexity gate (AGE-335) — five questions before a new feature earns its keep
Every block replacement or knob change adds complexity to a chassis that is already 41k of Python.
Answer these five before proposing; the answers go in the candidate JSON and are checked (not
enforced) by `propose.complexity_check`. A missing answer is a flag on the proposal, not a veto —
the evaluator still tests it.

1. **What capability does it add?** Not what code changes: what can the agent *do* on the board that
   it could not do before. Field: `"capability"`.
2. **What evidence shows that capability is missing?** Name the `evolve/classify.py` failure class
   whose metrics the change moves — one of EXECUTION, CAPITAL, LABOR, MARKET, TIMING, CAPACITY,
   LAND_FAILURE — and, ideally, the number behind it ("missed_feed 37 on the tape vs our 13").
   Field: `"failure_class"`.
3. **Can we test the capability independently?** Name the `evolve/scenarios/` diagnostic whose
   verdict should move: `unsupported_livestock`, `idle_labor`, `late_expansion`, `land_pressure`,
   `execution_overload`. Field: `"scenario"`. Note that `idle_labor` and `late_expansion` currently
   pass 30/30 of the real population, so naming one of them is weak evidence.
4. **Can we explain the mechanism?** "Score improved" is not an answer. State the causal chain: what
   the hands do differently, and which per-day trace number that shows up in. Field: `"note"`.
5. **Does it survive ablation?** Not answerable at proposal time — `loop.ablate()` measures it after
   held-out, and only for candidates carrying 2–8 changes. Know before proposing whether your
   candidate will even get an ablation row.

Expected evidence format (all three new fields optional; a proposal without them is still evaluated):

```json
{"note": "batch non-urgent watering into one late sweep, so hands stop crossing the board per tile",
 "capability": "the agent can defer a tile's water to a later fuller sweep instead of servicing it in passing",
 "failure_class": "EXECUTION_FAILURE", "scenario": "execution_overload",
 "blocks": {"sweep": "..."}}
```

Check any candidate file, or the whole queue, without running a game:

    python3 evolve/propose.py --gate evolve/queue/llm_20260906-043705_3.json
    python3 evolve/propose.py --gate

### Retroactive audit of the 8 existing blocks
Full evidence and sources: `docs/AGE-335-block-audit.md`. Two facts from it that change how you
should read the archive: **no block has ever been ablated as a block** (the loop only reverts single
changes relative to a parent, and every block is inherited from the chassis), and the frontier gap is
*not* in animal routing.

| block | failure evidence | independent test | ablation evidence | flag |
|---|---|---|---|---|
| hiring | LABOR/CAPITAL; labour per obligation 2× the winners' | only `idle_labor`, which no real candidate fails | none; 3 replacements lost (P7, arch_search floor_v1/v2) | Q5 open |
| demand | CAPACITY/MARKET; demand-coupled sizing was +$50k | `unsupported_livestock`, splits 3/27 | none; never even replaced | Q5 open |
| economy | all five non-execution classes; the whole gap decomposition | 3 discriminating scenarios | not removable; knobs exhausted | Q5 ill-posed |
| animal_routing | EXECUTION; travel 1.5–1.6 vs 0.97–1.05 | `execution_overload` | **ceiling ≈ $0** (routing oracle); `lib_C` −$3.4k | **low value as a lever** |
| siting | **none specific** — no metric, no class | **none** — no scenario touches it | **none** — never replaced, reads no knob | **dead weight** |
| crop_admission | EXECUTION/CAPACITY; movement-aware siting was the v10 win | weak — nothing tests crop mix | none; `lib_E` exact no-op (−$8) | Q3 weak |
| sweep | EXECUTION; tapes batch water, we scatter it | `execution_overload` | **cap defended: removing it −$19.1k, t=−10.78** | best evidenced |
| dispatch | EXECUTION; LABOR half **contradicted** (our idle 8% < tapes' 13%) | `idle_labor` + `execution_overload` | none; `lib_D` no-op (+$449, t=0.50) | Q2 half false |

Two dead-weight findings that affect proposals directly: 24 of the 65 SPACE params are **inert** (in
`KNOB_SPACE`, absent from the chassis `KNOBS` — `render()` raises, so setting one wastes a round),
and `setup_capital_share` / `labor_reserve_buffer` are **live but read by nothing**, so varying them
renders a behaviourally identical agent under a fresh key. The gate flags both before any game runs.
