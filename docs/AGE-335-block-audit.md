# AGE-335 — complexity gate and retroactive audit of the 8 mutation blocks

Two things live here: the **complexity gate** (five questions a new champion feature has to answer,
stated in `evolve/RULES.md` and checked mechanically by `propose.complexity_check`), and the
**retroactive audit** of the eight blocks that already exist, run against the same five questions.

The audit is a flagging exercise. Nothing is removed, nothing is blocked; the flags say where the
evidence is missing so a human can decide whether the block is carrying its weight.

## Sources

| source | what it contributes |
|---|---|
| `evolve/RULES.md` | what is closed, what worked, the measured execution gap, the routing-oracle counterfactual |
| `evolve/classify.py` | the seven failure classes and the metrics that decide them (question 2) |
| `evolve/scenarios/`, `docs/AGE-333-scenario-suite-results.md` | the five diagnostics and which of them separate real candidates (question 3) |
| `docs/block-library.md` | the only per-block replacement experiments ever run (lib_A..lib_E, seeds 1-6, both seats) |
| `docs/planner-results.md`, `docs/planner-allocation-hiring-results.md` | whole-block rewrites (P, P7) and why they lost |
| `arch_search/ledger.db` | the `early_labor/floor` hypotheses against `_load_model` |
| `evolve/loop.py::ablate` | what the loop's automatic ablation does and does not cover |

## The one structural finding that shapes every Q5 answer

**No block has ever been ablated as a block.** `loop.ablate()` reverts each single change *relative to
the candidate's parent*, only for candidates that pass held-out, and only when the candidate carries
between 2 and 8 changes (`evolve/loop.py:196-199`). All eight blocks are inherited from the frozen
chassis rather than introduced as a candidate change, so no ablation row has ever measured what
removing one costs. Where a Q5 cell below says something concrete, it comes from a *replacement*
experiment (change the block, measure) or a *counterfactual* (make the block's job free, measure),
never from a removal.

Two of the eight are not removable even in principle — `economy` is the only writer of buy/sell
orders and `siting` is the only code that places a purchased animal — so for those, "does it survive
ablation" has to be read as "is the specific policy inside it doing work", which is a different and
so-far unasked question.

## The audit

### hiring — `_hire_plan`, `_load_model` (23 lines)

| question | answer |
|---|---|
| **Q1 capability** | Sizes the crew each morning from servicing load rather than from cash, so headcount grows with obligations instead of sitting at a constant. |
| **Q2 evidence** | `LABOR_FAILURE`, `CAPITAL_FAILURE`. The need is measured: labour per obligation is ~2x the winners' (11.3 vs 6.6 unit-turns per animal-day, RULES.md). |
| **Q3 test** | `idle_labor` targets exactly this block (`max_hands`, `idle_share`, `work_per_hand_day`) but passes 30/30 real candidates — non-discriminating today. `land_pressure` (`early_cash_trough`) and `execution_overload` (`chore_completion`) are movable from here and do discriminate. |
| **Q4 mechanism** | Yes. Load model -> target headcount -> fib-priced hires, with hires paid before the feed reserve on days 0-5 (part of the C1 opening, +$4.8k held-out). |
| **Q5 ablation** | **Never ablated.** Three independent *replacement* attempts all lost: P7's coupled load model -$3.3k -> -$17.8k -> -$21.5k per game; `arch_search` `early_labor/floor_v1` = ARCHITECTURAL_DEAD_END, `floor_v2` = FALSIFIED; `min_hands` 5-6 / `load_per_hand` 12-15 flat to -$3k (closed in RULES). All say changing it hurts; none says what removing it is worth. |
| **flag** | Q5 open. Not dead weight — the block is well-defended by failed alternatives. |

### demand — `_instances`, `_daily_demand`, `_demand_room` (36 lines)

| question | answer |
|---|---|
| **Q1 capability** | Reads unlocked shop instances to compute what the town will absorb, so herd and crop sizing track live demand instead of a constant. |
| **Q2 evidence** | `CAPACITY_FAILURE`, `MARKET_FAILURE`. Positive evidence rather than failure evidence: demand-coupled herd/crop sizing (V3.9) was **+$50k over its predecessor**, the largest documented single win in the lineage. |
| **Q3 test** | `unsupported_livestock` decides on `peak_animals` / `animal_revenue_per_animal` — this block's direct output — and separates the population 3 pass / 27 fail. `land_pressure` also. Best-tested block in the set. |
| **Q4 mechanism** | Yes. `_demand_room` caps per-species purchases at what the unlocked instances consume. |
| **Q5 ablation** | **Never ablated, and never replaced** — no candidate in `evolve/queue/` or `evolve/blocks/` has ever substituted this block. The nearest evidence is one-sided knob movement: `demand_share` 0.75-1.0 costs -$6k to -$17k, i.e. loosening the cap loses. |
| **flag** | Q5 open. Not dead weight. |

### economy — `economy` (277 lines)

| question | answer |
|---|---|
| **Q1 capability** | The whole daily market policy: opening, feed, seeds, animals, land, selling, fertilizer. |
| **Q2 evidence** | `CAPITAL_`, `MARKET_`, `TIMING_`, `LAND_`, `CAPACITY_FAILURE`. The entire frontier-gap decomposition is economy: wheat sales -$15k, melon timing, fertilizer volume, strawberry price $78 vs $93. |
| **Q3 test** | All five scenarios; three of them discriminating. `unsupported_livestock` fails 27/30 on `animal_revenue_per_animal` (economy buys and sells the herd) and `land_pressure` fails 13/30 on `early_cash_trough` (economy is what spends). |
| **Q4 mechanism** | Yes, in the most detail of any block (C1 opening +$4.8k, `fert_buy` 1 +$5.4k). |
| **Q5 ablation** | **Not removable** — nothing else emits buy/sell orders — so block-level ablation is undefined. Knob-level exploration is the most thorough in the project and RULES already records the conclusion: "`economy` knob changes are mostly exhausted". |
| **flag** | Q5 not answerable as posed. Needs restating as "which policy *inside* economy survives ablation", which no run has asked. |

### animal_routing — `_build_route`, `_route_step` (75 lines)

| question | answer |
|---|---|
| **Q1 capability** | Chains feed/care/collect stops (plus shed pickups) into one route so a hand services several animals per trip. |
| **Q2 evidence** | `EXECUTION_FAILURE` — `missed_feed`, `escapes`. The gap is measured: travel per work action 1.5-1.6 vs the frontier tapes' 0.97-1.05. |
| **Q3 test** | `execution_overload` (`missed_feed`, `escapes`, `chore_completion`), discriminating — H10/H11/H12 fail it on `missed_feed`. |
| **Q4 mechanism** | Yes. `ROUTE_LEN` stops per trip, feed/care paired on the tile, fertilizer collected on-tile. |
| **Q5 ablation** | **The one block with a measured upper bound, and it is ~zero.** The routing oracle (RULES.md, Sep 3) made travel free on C1 vs the Yuan800 tape, seeds 1-8: own money moved -$63k to +$25k per seed, **mean ~0**; halving travel is also ~0. A concrete improvement attempt, `lib_C` (herd-scaled route length, unfed-first ordering), lost -$3,398/game. |
| **flag** | **Low measured value.** Required for the agent to feed animals at all, so not removable, but every measured attempt to improve it is <= 0 and the counterfactual ceiling on it *alone* is ~0. A proposal scoped to this block by itself should have to argue against that number. |

### siting — `_pick_site`, `_setup_step` (41 lines)

| question | answer |
|---|---|
| **Q1 capability** | Chooses where a purchased animal is placed (nearest empty pasture to the shed, else nearest empty tile) and walks a carrying hand through BUILD/PLACE. |
| **Q2 evidence** | **None specific.** `EXECUTION_FAILURE` only by inference (placement -> travel -> missed feed). `classify.py` has no placement or distance metric, so no rule can ever fire *on* this block. The "movement-aware siting" win in RULES.md is *crop* siting — `_crop_pools`/`_plant_choice`, i.e. the `crop_admission` block — not this one. |
| **Q3 test** | **None specific.** No scenario thresholds a siting metric; the only reachable verdict is `execution_overload`'s `chore_completion`, several steps downstream. |
| **Q4 mechanism** | Stated but never tested: "put animals near the shed to shorten service trips." Plausible; no measurement attached. |
| **Q5 ablation** | **Nothing at all.** Never ablated, never replaced (no `evolve/blocks/` file and no queue entry touches it), and it reads **no SPACE parameter** — `NEAR_RADIUS`, the knob usually associated with siting, is read by `crop_admission`. There is no experiment of any kind on this block in the repository. |
| **flag** | **Dead-weight candidate #1 — zero evidence on four of five questions.** Also carries literal dead code: `_pick_site(v, species=None)` never reads `species` and its only call site passes one argument (`evolve/chassis.py:659,689`). |

### crop_admission — `_crop_pools`, `_plant_choice`, `_task_valid` (29 lines)

| question | answer |
|---|---|
| **Q1 capability** | Decides which tiles are eligible for which crop task and what to plant where — recurring crops near the shed, one-shot crops far. |
| **Q2 evidence** | `EXECUTION_FAILURE` (`missed_water`, population mean 375/game), `CAPACITY_FAILURE` (`plants_final`). Positive evidence: movement-aware crop siting is "the biggest single win in the v10 lineage". |
| **Q3 test** | **Weak.** Only `execution_overload`, and only via `chore_completion`. No scenario thresholds plant count, crop mix or planting cadence, which is what this block actually decides. |
| **Q4 mechanism** | Yes, and both directions are bounded: `NEAR_RADIUS` above 4 is a decisive loss, radius growing with land is a decisive loss. |
| **Q5 ablation** | **Never ablated.** One extension was measured and was an **exact no-op**: `lib_E` (WHEAT preferred over MELON in the far band once the herd reaches 12) -$8/game, t=-0.05, because the herd never reaches 12 while far-tile seed slots are still open. |
| **flag** | Q3 weak, Q5 open. Not dead weight — it holds a documented win — but the thing it decides has no independent test. |

### sweep — `_build_sweep`, `_crop_step` (107 lines)

| question | answer |
|---|---|
| **Q1 capability** | Gives each hand a bounded tiered crop sweep (urgent water, harvest, water, plant, weeds) instead of one task at a time. |
| **Q2 evidence** | `EXECUTION_FAILURE` — `missed_water`, `chore_completion_ratio`. The frontier tapes batch watering into fewer, fuller sweeps (water_hour 14.2-14.3 vs our 13.1, missed plant-days 334-407 vs 430-564). |
| **Q3 test** | `execution_overload` via `chore_completion`, discriminating — P5 and P_pre_tape fail it on exactly that metric. |
| **Q4 mechanism** | Yes: tier order plus a `CROP_SWEEP_LEN` cap and a `CROP_SWEEP_RADIUS` local extension. |
| **Q5 ablation** | **The only block with a signed, decisive result.** `lib_A` removed the `CROP_SWEEP_LEN` cap (chain every pending task by nearest neighbour): **-$19,099/game, t=-10.78**. The cap demonstrably earns its keep. Other measurements are noise: `lib_B` +$98/game (t=1.16), region-assignment sweep exactly neutral (travel 1.008, cov_hard 0.999). |
| **flag** | Best-evidenced block on Q5. Note the shape of that evidence: it defends the existing cap, it does not show the tier order or the radius extension is worth anything. |

### dispatch — `_unit_action` (60 lines)

| question | answer |
|---|---|
| **Q1 capability** | Chooses, per unit per turn, between an animal route, a crop sweep, setup work, and idling. |
| **Q2 evidence** | `EXECUTION_FAILURE`, and `LABOR_FAILURE` **only nominally** — RULES.md's measurement points the other way: "tapes carry more idle (13% vs 8%) and still win: idle is not the problem, wasted movement is". So half of this block's nominal failure-class evidence is contradicted by the measurement. |
| **Q3 test** | `idle_labor` (non-discriminating, 30/30 pass) and `execution_overload` (discriminating). |
| **Q4 mechanism** | Yes — priority order over carry state, pending setup, animal routes and sweeps. |
| **Q5 ablation** | **Never ablated.** The one measured dispatch change, `lib_D` (opportunistic deposit when one step from a shed tile), is a no-op: +$449/game, t=0.50; queued as harmless rather than as a win. |
| **flag** | Q2 half-contradicted, Q5 open. Not dead weight (something must arbitrate), but the idle-reduction rationale attached to it should stop being cited — it is measured false. |

## Summary

| block | Q1 capability | Q2 failure evidence | Q3 independent test | Q4 mechanism | Q5 ablation | flag |
|---|---|---|---|---|---|---|
| hiring | yes | LABOR / CAPITAL, gap measured | partial (only non-discriminating `idle_labor` is specific) | yes | never; 3 replacements lost | Q5 open |
| demand | yes | CAPACITY / MARKET, +$50k win | **yes** (`unsupported_livestock`, 3/27) | yes | never; never replaced | Q5 open |
| economy | yes | all five non-execution classes | yes (3 discriminating) | yes | not removable; knobs exhausted | Q5 ill-posed |
| animal_routing | yes | EXECUTION, travel 1.5 vs 1.0 | yes (`execution_overload`) | yes | **ceiling ~$0** (oracle); `lib_C` -$3.4k | **low value** |
| siting | yes | **none specific** | **none specific** | asserted, untested | **none at all** | **dead weight** |
| crop_admission | yes | EXECUTION / CAPACITY, v10 win | **weak** (nothing tests crop mix) | yes | never; `lib_E` exact no-op | Q3 weak, Q5 open |
| sweep | yes | EXECUTION, batching gap | yes (`execution_overload`) | yes | **cap defended, -$19.1k to remove** | best evidenced |
| dispatch | yes | EXECUTION; **LABOR contradicted** | partial | yes | never; `lib_D` no-op | Q2 half false |

## Dead weight flagged (nothing removed — humans decide)

1. **`siting` (the whole block).** No failure class can fire on it, no scenario tests it, no experiment
   has ever been run on it, and it reads no search-space parameter. It is the only block where four
   of the five questions have no answer at all. It cannot simply be deleted (something must place a
   purchased animal), but "nearest empty pasture to the shed" is an untested constant policy sitting
   inside a search space that has never once been allowed to vary it. *Cheapest next step:* add a
   `siting` block replacement to the queue (e.g. place near the crop centroid, or near the next
   animal's route) and score it — one dev run answers Q5 for the block that has nothing.
2. **`_pick_site`'s `species` parameter** (`evolve/chassis.py:659`). Declared, never read, and the only
   call site passes one argument. Literal dead code inside the frozen chassis; costs nothing but
   advertises a capability (species-aware placement) that does not exist.
3. **`animal_routing` as a lever, not as code.** Keep the block; drop the belief that improving it
   pays. The oracle bound (mean ~$0 with travel free) and `lib_C` (-$3.4k) both say so, and RULES
   already states the general form: execution-only changes without a paired allocation change fail.
4. **24 of the 65 SPACE parameters are inert.** They are in `space.KNOB_SPACE` but absent from the
   frozen chassis's `KNOBS`, so `space.render()` raises on any candidate that sets one (AGE-336) —
   they are pure proposal-poison: all 20 `spec_*_<CROP>` entries plus `seed_orders_cap`,
   `land_deadline_shift`, `sell_order`, `herd_species_bias`. One is already sitting in the queue:
   `evolve/queue/llm_20260906-043705_3.json` sets `seed_orders_cap` and is dead on arrival. The gate
   now flags these as `inert_param` before a game is ever run.
5. **2 more parameters are live but never read, which is worse.** `setup_capital_share` (0.25) and
   `labor_reserve_buffer` (50) are declared in the chassis's `KNOBS` dict and referenced by no code
   anywhere in `evolve/chassis.py`. Because the name *is* in `KNOBS`, AGE-336's render contract
   passes: `render()` writes a file whose `KNOBS` literal differs, the candidate gets its own key and
   its own dev run, and it behaves identically to its parent. That is precisely the silent no-op the
   render contract was built to stop, reached by the one path the contract does not check. The gate
   flags them as `unread_param`; the durable fix is either to wire them up or to drop them from
   `KNOBS` and `KNOB_SPACE`, which is a chassis change and therefore out of this ticket's scope.
6. **9 live parameters are read outside every typed block**, so no failure class attaches to them and
   the gate flags them `no_failure_evidence`: `harvest_min`, `wheat_water_tier`, `STRAW_CUTOFF`,
   `MELON_MAX_TILES`, `MELON_PRICE_CUSHION`, `FERT_RADIUS`, `OPP_GROWTH`, `SPREAD_W`, `SPREAD_CAP`.
   Not necessarily worthless — but nothing in the taxonomy or the scenario suite can currently say
   why any of them should move.
7. **`idle_labor` and `late_expansion` as evidence.** Both pass 30/30 of the real population and fail
   only for injected controls (AGE-333). They are the only scenarios specific to `hiring` and to
   late-game `economy`, so citing either as a proposal's independent test is weaker than it looks;
   the gate flags that as `test_does_not_discriminate`.

## What the gate does at proposal time

`propose.complexity_check(cand)` is a dictionary lookup over the proposal's own JSON — no game, no
LLM, no database. It runs on every LLM proposal in `propose.main()` (flags are logged and stored on
the queue item as `complexity_flags`) and standalone over any candidate file:

```
python3 evolve/propose.py --gate evolve/queue/*.json
python3 evolve/propose.py --gate            # the whole queue
```

Flags, by question:

| question | flags |
|---|---|
| structural | `unknown_block`, `unknown_param`, `inert_param`, `unread_param`, `no_op_param`, `no_change`, `malformed_blocks`, `malformed_params` |
| Q1 capability | `no_capability_statement` (records `capability_recorded` / `capability_from_note`) |
| Q2 evidence | `no_failure_evidence`, `unknown_failure_class`, `failure_class_mismatch` |
| Q3 test | `no_independent_test`, `unknown_scenario`, `scenario_mismatch`, `test_does_not_discriminate` |
| Q4 mechanism | `mechanism_not_explained` (records `mechanism_recorded`) |
| Q5 ablation | `ablation_will_be_skipped` (>8 changes); records whether the loop will ablate at all |

Nothing here blocks a candidate. `main()` logs the summary line and queues the candidate anyway; the
cascade still decides. Run against the nine queue entries that existed when this landed, the gate
found:

* one **dead on arrival**: `llm_20260906-043705_3.json` sets `seed_orders_cap`, which `render()`
  raises on — it would burn a validation game to learn that;
* one 18-change grid (`grace_opt2_exec_grid_sep07.json`) whose per-change contribution the loop's
  ablation will never measure, because `ablate()` only handles 2-8 changes;
* two `no_op_param`s — axis levels set to the value C1 already carries (`load_per_hand` in that same
  grid, `open_sheep` in `llm_20260905-203826_1.json`);
* `no_failure_evidence` and `no_independent_test` on all nine, which is expected rather than damning:
  the proposal schema had no field for either answer until this ticket added one. The number to watch
  is how fast that fraction falls now that `SCHEMA_DOC` asks for `failure_class` and `scenario`.
