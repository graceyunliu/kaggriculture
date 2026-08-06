# Kaggriculture v8 Architecture — grounded in `main_v7.11.py`

**Status:** supersedes `kaggriculture-v8-design-spec.md` (and its duplicate), the v8.1 order-slots plan, and `main_v8.py`'s Phase 1 foundation as the *starting point* (its infrastructure is still worth reusing — see §6.1 — but its fork point is stale). Written Aug 5, 2026, after reading `main_v7.11.py` end to end, the full project decision log through D71, and the 7 previously-undocumented `main_v8_candidate{A,B2,B3,D,E,E2,H}.py` files.

---

## 0. Why this doc exists

Three separate things have been called "v8" in this project and none of them is a reliable base:

1. **The original `kaggriculture-v8-design-spec.md`** proposed a centralized EV Decision Engine replacing hard-coded rules. It was written against v7.2 and is now four versions stale — the two gaps it opens with (fleet ceiling, wheat priority) were already fixed, not by an EV formula, but by reordering budget priority (v7.3/v7.5). Its centerpiece idea (score every candidate action on one shared value formula) has an actual track record on this project: it's the thing that keeps losing to "diagnose the real bug, let behavior emerge" (v7.1's three "obviously correct" fixes cancelled each other; D63 found Phase 2's target — the calendar attack dump — fires 0-1 times/match, so nothing built on top of it could ever have mattered).
2. **`main_v8.py`** ("Phase 1 foundation") is a real, working piece of infrastructure — a state-builder, opponent analyzer, and a decision log that's been fault-injection-tested and verified as a true behavioral no-op. But it forks from `main_v7.6.py`, not `main_v7.9.py`/`main_v7.11.py` — it's missing the strawberry fix and the order-priority sort that make v7.11 the current champion. Reusable, not current.
3. **The v8.1 order-slots plan** (`kaggriculture-v8.1-order-slots-plan.md`) proposed two changes: spread hiring across hours (Change A) and rank orders by cost-of-delay (Change B). Both got built and tested independently, just under different names. Change B **won** and became `main_v7.11.py`. Change A **lost decisively** as `main_v7.10.py` (-$21,731/game, t=-8.45) — the engine's Fibonacci wage curve makes hiring past ~11 hands actively unprofitable, so "spread the hire burst" was solving a problem that wasn't actually a problem. The plan is half-shipped, half-refuted; treat it as closed.

There's also a fourth, previously untracked line of work: 7 `main_v8_candidate*.py` files in the project folder, built on top of v7.9, testing FERTILIZE and crop-mix reweights. None of this was in project memory or the design doc before now. §4 catalogues them — most have no recorded verdict at all.

**v8 needs one fork point.** It should be `main_v7.11.py`, the current, properly-validated (leak-free harness, `--both-seats`) local champion — not `main_v7.6.py` (stale) and not `main_v7.9.py` (superseded by v7.11's order-priority sort, +$1,279/game on top).

---

## 1. What v7.11 actually is (architecture as-built)

Single-file agent, ~1150 lines, three module-level mutable globals (`timing_engine`, `animal_plans`, `reserved_sites` — fine for one Kaggle episode process, but re-loading the module across episodes in a test loop leaks state; the local harness now reloads a fresh module instance per game, see §7).

- **`perceive()`** — full board rescan every turn. No memory of anything: tile classification (urgent_water / water / harvest / empty / weeds / occupied-pastures / empty-pastures) and opponent imminent-harvest counts are recomputed from scratch each call.
- **`economy()`** — builds this turn's market orders. As of v7.11, every candidate order is scored by a *cost-of-delay* function (§ file header has the full band table: ENORMOUS = animal about to escape, HIGH = capacity-relief/final-turn/attack-window sells and hiring, MEDIUM-rising = seed buys nearing cutoff, MEDIUM = routine feed/animal buys, NEAR-ZERO = ordinary paced sells, ZERO = land while tiles sit idle) into one list, sorted descending, truncated to `MAX_MARKET_ORDERS=10`. This replaced a fixed-bucket concatenation that dropped whatever fell past index 10 regardless of value — the sort is the whole of v7.11's contribution over v7.9.
- **Animal pipeline** — one `animal_plans` entry can be `BOUGHT`/`CARRYING` at a time (single farmer, can't build two pastures in parallel); feasibility to buy the *next* animal is a live symptom check (`_animal_expansion_feasible`: survival, wheat-affordability, hand-capacity projection, real current crop-neglect, crop-tile-space), not a forecast or a fixed cap. Maintenance (`animal_maintenance_action`) is stateless and fleet-wide — ranks every pasture's real pending need each call, works for any caller.
- **Crop task allocation (`unit_action`)** — also fully stateless: every idle unit, every turn, independently recomputes its own nearest highest-priority task from the fresh `tasks` dict. This is the one place v7.11 has *no* memory across turns, and it's the identified root cause of the project's biggest unsolved inefficiency (§3, §5.1).
- **Dispatch (`_agent`)** — farmer: animal setup (if in progress) → animal maintenance (unconditional, full priority) → crop tasks. Hands: a live-computed fraction (`_reserved_crop_hand_count`, scales with weed ratio / crop-pressure symptoms) is walled off to crop-only work plus feed-critical animal response; the rest get full-priority animal maintenance then crop tasks.
- **Crash guard** — `agent()` wraps `_agent()`, swallows any exception, returns a PASS turn. Confirmed (D65) this can silently forfeit a whole turn's actions with zero visible signal outside a stderr print — this is exactly what a decision log needs to catch (§6.1).

---

## 2. Ground truth to build from, not re-derive

Confirmed against `vendor/kaggle_environments_engine/kaggriculture.py`, not assumed:

| Fact | Why it matters for v8 |
|---|---|
| Hiring cost is `fib(hires_today)`, hands + `hires_today` wipe to 0 every day boundary | Labor is rented daily, not owned. Marginal cost cliffs around the 11th-12th hand/day (~$233→~$1,220). **More hands is a closed question — don't reopen it.** |
| Non-ongoing crops (WHEAT, CARROT, MELON) accrue yield via the WATER handler, capped by watering-window days; ongoing crops (STRAWBERRY, TOMATO) accrue via a calendar path with `min(max_yield, ...)` | FERTILIZE can raise a non-ongoing crop's realized yield toward its cap (real lever); it **cannot** raise an ongoing crop's yield ceiling, only reach the same cap faster (already tested, loses). |
| Town demand pools per match: WHEAT 635, STRAWBERRY 534, MILK 440, CARROT 431, EGG 341, WOOL 336, TOMATO 335, MELON 140, FERTILIZER 0 | The game is supply-constrained. WHEAT and STRAWBERRY have the most unclaimed headroom; MELON and FERTILIZER are near/at saturation already. |
| Market order list is truncated to the first 10 **by submission order** — sorting the list *is* the allocation mechanism | Anything added to `economy()`'s order set must get a real priority score, not just be appended. |
| Real top-of-ladder convergent baseline (5+ independently-scouted teams, near-identical profiles): WHEAT ~66-67 planted, STRAWBERRY ~41-44, MELON ~21-26, zero CARROT/TOMATO, quad2 by ~day 7, ~9-10 hires/day, final money $121-141k | This is the reference tier v7.11 is still ~2-2.5x below. Not a strategy to copy wholesale (species/line-item mirroring has repeatedly been a trap — sheep, day-0 land — see §4) but the right scale to calibrate ambition against. |

---

## 3. The one number that matters

Seat-controlled measurement (D67, `--both-seats`) of the v7.6/v8-lineage vs the two fixed strong bots (`opp_frontier_v12`, `opp_scenario_v14`): **0/12, mean margin -$155k to -$165k.** Every later round (v7.9, v7.11) narrowed local self-play margins by low four figures — real, but a rounding error against a quarter-million-dollar gap.

Root cause, traced to actual action counts (not inferred): **731 units sold vs frontier's 1,921.** Our realized *prices* are good (MILK $215 vs $160 base, STRAWBERRY $221, WHEAT $48 vs $25) — we are not a pricing problem, we are a **volume** problem. Every plausible volume lever has now been tested and most are ruled out (§4). What's left standing is labor *throughput*, not labor *headcount*: a full-match trace shows **66-70% of all unit-turns are movement, 26-32% are work, 2-4% are pass** — in every version measured, including v7.11. This ratio is the actual ceiling on production volume, and it has not been fixed by anything tried so far.

**Corroborated by real ladder data (Aug 5 sync, 87 own episodes across 7 submissions): `SHED_AT_CAP` is the dominant loss tag, 31 of 41 losses.** At first read this looks like the opposite of an under-production problem — a full shed means too much sits unsold, not too little gets grown. But it's the same root cause seen from the other side: with 66-70% of unit-turns spent walking rather than working, harvest/water/sell labor isn't allocated evenly turn to turn — it comes in uneven bursts wherever units happen to converge. A burst of harvest can spike the shed past its force-dump trigger faster than the existing (already reasonably sophisticated) overflow-relief selling can clear it, even though *average* production stays below the opponent's steadier, larger economy. This is not a separate problem from §3's volume gap and does not argue for a different fix — if anything it strengthens the case for §5.1 (global per-turn task assignment), since smoothing labor allocation should reduce both symptoms at once. Worth adding "`SHED_AT_CAP` incidence" as a measured outcome, not just final money, when that experiment eventually runs.

---

## 4. Graveyard — tested and rejected, do not re-attempt without new evidence

| Idea | Version | Result | Why it failed |
|---|---|---|---|
| Flat animal fleet cap (any single number) | v7.3 rounds 1-4 | Round 4's cap=15 helped one opponent, hurt the other by about the same | No fixed number generalizes across opponent styles; replaced by the live symptom-check gate v7.11 still uses. |
| Enable SHEEP | v7.8 | -$11,912 mean/6 seeds, t=-3.23 | Sheep displace cows 1:1 at fixed fleet size (feasibility gate caps headcount regardless of species); cow is ~45% more $/day/slot, and our realized MILK price never drops enough to make diversification pay. |
| More hands — either raise `HAND_TARGET_MAX` or spread the daily hire burst across hours | v7.10 (spread), v7.10a/b (raise target) | v7.10: 0/8, -$21,731/game, t=-8.45. a/b not even tested — same direction as a result already known to be wrong | Fibonacci wage curve is exponential in hand count; ~11 hands/day is roughly the point where marginal cost exceeds marginal product. Order-slot contention was accidentally rationing hiring *correctly*. |
| Day-0 land purchase | v7.12 | 0/30, -$14,354/game | Extra land gets filled with whatever seed budget remains once premium crops are funded, diluting the crop mix toward WHEAT/CARROT and lowering average realized value despite more raw units planted. |
| Unconditional per-unit target locking (stop recomputing nearest task mid-walk) | v7.13 | 5/20, -$13,492/game, t=-3.42 | Kills priority-preemption — urgent work can't pull in a unit already committed to something lower-priority. |
| Priority-preemptible target locking | v7.15 | 0/20, -$19,571/game, t=-11.28 | Preemption check was global-existence, not nearest-unit: every locked unit below a newly-urgent task independently abandons its walk, but only one (farmer, then hand0...) actually claims it. Net: more idle time than the churn it targeted (pass-rate rose 3.6%→7.9%). |
| FERTILIZE STRAWBERRY/TOMATO | Candidate A (3 iterations) | v1 -$50,711, v2 -$32,137 mean/11 seeds — shrinking but still losing badly, v3 untested | Ongoing crops' yield is capped by `min(max_yield, ...)` regardless of fertilizer — it only reaches the same ceiling faster, not higher. Mechanically can't pay for the labor diversion. |
| Lower WHEAT/STRAWBERRY seed targets | Candidate B2 | -$30,757 mean/11 seeds | Not investigated further — direction alone (cutting an already-headroom crop) was enough to lose decisively. |
| Undocumented: count weeds in the animal-expansion neglect gate | Candidate H | No test recorded — abandoned mid-edit | Header comment block was never updated from its copied-v7.9 text; treat as orphaned, not evidence either way. |
| FERTILIZE WHEAT only, isolated, on `main_v8.py` | `main_v8.1.py` (Aug 5) | 0/15 seeded `--both-seats` vs `main_v8.py`, mean -$19,019/game, min -$40,570, max -$7,769, t=-7.69 | Mechanically sound per the engine math (real ~2x yield lever, §5.2 below), but the labor diversion to fetch/carry/apply FERTILIZER costs more than the yield gain is worth while §3's movement/work ratio is still the binding constraint. Worse: `fertilize_action()` was placed ahead of `assign_tasks()` in dispatch, so it diverts a unit from the just-validated joint global assignment (§5.1) on *every* turn an eligible tile + spare fertilizer exists, not just the 6-8 turns/game a FERTILIZE actually fired — fighting the mechanism that made v8 beat v7.11 in the first place. Do not re-attempt without a fundamentally different design (e.g. only fertilizing a tile a unit is already standing on/passing through en route to something else — zero-diversion, never a reason to divert — untested, not yet designed). |

---

## 5. Open threads — where v8's effort should actually go, ranked

### 5.1 Global per-turn task assignment — BUILT AND VALIDATED Aug 5, now `main_v8.py`

Both locking attempts (§4) tried to fix the movement/work ratio by giving *individual units* memory. Both failed for the same underlying reason: a per-unit local decision (lock, or preempt-if-eligible) can't see what every *other* unit is about to do this turn, so units collide, abandon good walks for nothing, or leave urgent work uncovered while a lower-priority walk finishes. The variant flagged after v7.15's rejection but not yet attempted at the time this section was first written is qualitatively different, not a tweak of the same idea: **a single global assignment pass, once per turn**, that matches idle/reassignable units to tasks the way the existing per-turn task lists already group them — nearest-unit-to-task, but computed jointly (build every candidate (unit, tile) pair within a tier, sort by ascending Manhattan distance, confirm pairs greedily) rather than each unit greedily grabbing its own nearest target in a fixed roster order.

**Built as `assign_tasks()` in `main_v8.py`, gated behind `GLOBAL_TASK_ASSIGNMENT` (flag-off is a required byte-identical no-op vs `main_v7.11.py` — verified, 3 seeds `--both-seats`, exactly 0.0 margin every seed). Result: decisive win, not a coin flip.**

- **Seeded `--both-seats` vs `main_v7.11.py`, 15 seeds (1,7,42,99,123,202,303,555,2024,8080,17,2025,3001,3002,3003): 15/15 wins, 0 losses.** Mean paired margin +$10,238/game (first batch of 8: +$10,322, t=+5.32; second batch of 7: +$10,144, t=+3.07). Every single seed positive, min +$855, max +$20,419. This is a materially larger and more consistent edge than any other change tested on this project's champion lineage, including v7.11's own +$1,279/game win over v7.9.
- **Mechanism confirmed, not just money:** move-share dropped from v7.11's 66.7-67.9% to 63.3-63.8%, work-share rose from 29.4-30.6% to 31.8%, across two independently-traced seeds (42, 7) vs the `starter` opponent. Direction matches the intended fix exactly.
- **One caveat worth watching, not disqualifying:** pass-rate also rose (2.7%→4.5%, 2.7%→4.9%) — the same *direction* of side effect that accompanied v7.13/v7.15's failures (pass-rate 3.6%→7.9%), though far smaller in magnitude here and this version won decisively where those lost decisively. Worth re-checking if a future change on top of this one also nudges pass-rate up — that combination is this specific mechanism's known failure signature.
- **Against the strong fixed bot (`opp_frontier_v12.py`, 4 seeds `--both-seats`): still loses 0/4, but the gap did NOT close and the absolute-score improvement is real and separately measurable.** v8's own average money across these games: ~$70,134/game vs v7.11's ~$62,901/game on the same seeds — **+$7,233/game (+11.5%) even against an opponent strong enough that neither version has ever beaten it.** Margin vs frontier is statistically unchanged (v8: -$142,833 mean, t=-77.01; v7.11: -$145,523 mean, t=-16.74) because frontier's own realized score also shifted slightly (shared-market interaction — our selling volume affects its realized prices too). **This is the expected, not disappointing, result:** §3's volume gap (731 vs 1,921 units) is large enough that one lever was never going to close it alone; this is genuine, validated progress on the mechanism most directly responsible for it, not the whole fix.
- Smoke tests clean: `starter` 720-turn, `pass` 720-turn, `starter` 48-turn truncated — all DONE/DONE, zero crashes, zero `GUARD` invocations.
- **Shipped as `main_v8.py`.** The prior Phase-1 state/decision-log foundation is preserved as `main_v8_phase1_foundation.py` (not lost, not folded in — see §6.1, that rebase is still a separate future step).
- **`main_v8.py` (plain, pre-§5.2/5.3) was submitted to the real ladder Aug 5, 19:51 UTC (ref 55279558) — public score 667.1, confirmed via the Kaggle API.** Not yet tested against `opp_scenario_v14.py` or larger opponent-pool sweeps. `main_v8.2.py` (§5.3's validated reweight, the current local champion) has NOT been submitted yet — that's the next actionable ladder step, not a further local build.

### 5.2 FERTILIZE on WHEAT only — CLOSED Aug 5, rejected (see §4)

**Tested clean, isolated, on `main_v8.py` as `main_v8.1.py`: 0/15 seeded `--both-seats`, mean -$19,019/game, t=-7.69 — decisive rejection.** Candidate D's engine analysis was correct (WHEAT's non-ongoing yield path genuinely doubles per-watering accrual toward its cap during the age 2-4 window, a real ~2x lever, unlike STRAWBERRY/TOMATO) but mechanically sound does not mean economically worth it: the labor cost of proactively walking to the shed, picking up FERTILIZER, and carrying it to a WHEAT tile outweighs the yield gain while §3's movement/work ratio is still the binding constraint, and placing that diversion ahead of §5.1's `assign_tasks()` in dispatch actively fights the mechanism that made v8 beat v7.11 in the first place (see §4 entry for the full mechanism trace). Not a bug — both smoke tests ran clean, DONE/DONE. Do not re-attempt without a fundamentally different, zero-diversion design. `main_v8.py` remains the champion.

### 5.3 WHEAT/STRAWBERRY reweight directly on `main_v8.py` — VALIDATED Aug 5, now `main_v8.2.py`

**Candidate B3's never-tested higher-WHEAT variant (`want["STRAWBERRY"]=min(space,8/14)`, `want["WHEAT"]=min(space,40)`), ported onto `main_v8.py`: 12/15 seeded `--both-seats` wins, mean +$4,482/game, t=+4.86, 95% CI [+$2,674,+$6,289] — entirely positive, decisive.** This is the first real win on this project's champion lineage since main_v8.py's own task-assignment result, and it resolves the open question the architecture doc flagged: Candidate B's own v7.9-base result was a statistical wash (+$5,384/11 seeds, t=1.52, not significant) and B2's lower WHEAT target (min(space,16)) lost decisively (-$30,757) — the missing data point was always whether B's WHEAT target was too LOW rather than crop reweights being a dead end, and B3 (never run) tested exactly that direction.
- **Absolute money moved, not just relative margin:** vs fixed opponents on the same seeds, `main_v8.2.py` scored $96,717 (`starter`) and $97,877 (`pass`), up from `main_v8.py`'s own $81,668/$77,159 on identical matchups — roughly +$16-20k absolute. Consistent with the theory: `min(space,40)`/`min(space,8/14)` fill tiles that were sitting idle (the 36-50/100 idle-tile gap already measured in this doc) against WHEAT's and STRAWBERRY's demand pools, the two largest in the game (635, 534 units).
- The 3 losing seeds (303, 2025, 3003: -$1,772, -$30, -$1,868) are noise-scale against wins of +$4,500 to +$9,700 — not a competing pattern.
- Smoke tests: `starter`/`pass` 720-turn and `starter` 48-turn truncated all clean (DONE/DONE, zero crashes) — full 3-part protocol (§7) confirmed.
- **Ported directly onto `main_v8.py`, isolated to exactly these two `want[]` constants (diff-verified) — nothing else touched, single-variable discipline maintained.**

### 5.4 Stress-test v7.11's own untested risk — DONE Aug 5, and the "0 truncation events" premise was WRONG

**Directly instrumented and measured: truncation fires in 100% of games tested (56/56 on `main_v8.2.py`, 3/3 spot-checked on plain `main_v7.11.py`), averaging 17.1 events/game, every single game, entirely at `hour==0` (the daily hiring decision point) from roughly day 9-12 through day 27-28.** The "0 truncation events observed" claim in v7.11's original 40-game validation set was never actually a direct measurement — this section's own framing already called it "not a known bug, but an unverified assumption," and verifying it directly overturns the premise rather than confirming it. No adversarial hire-heavy/sell-heavy pairing was even needed: self-play alone reproduces it reliably (frequency is statistically flat across `starter`/`pass`/all 5 real fixed bots in `Opponents/`/self-play mirror — 17.0-17.9 events/game regardless of opponent, since the volume is driven by this agent's own order count, not adversarial pressure).
- **Provenance confirmed, not a v8/v8.2 regression:** ran the identical instrumented check on plain `main_v7.11.py` (seeds 1/7/42 vs `starter`) and got the exact same event counts (21/21/17) as `main_v8.py`/`main_v8.2.py` on those seeds — the mechanism (`economy()`'s order-priority sort, `MAX_MARKET_ORDERS=10`, `PRIORITY_HIGH_HIRE=700`) is byte-identical across v7.11→v8→v8.2, so this has been true of every version in the current lineage since v7.11 shipped. It does NOT confound any of the already-measured champion comparisons (v8 vs v7.11, v8.2 vs v8) — it's a constant background condition present equally in both sides of every one of those A/B tests.
- **What actually gets dropped, aggregated over the 56-game `main_v8.2.py` sweep (958 total truncation events):** ~121 HIRE orders dropped per game on average — the dominant casualty by volume — vs an estimated $14,585/game face value (qty × base price, likely an underestimate of realized value in this supply-constrained economy) of dropped SELL orders on the ~40% of truncation events that touch a SELL at all. **This directly reinforces, with real numbers for the first time, the already-documented v7.10 graveyard finding that "order-slot contention was accidentally rationing hiring correctly"** (§4) — the sheer volume of HIRE requests silently dropped here confirms truncation is already doing real, substantial implicit hire-throttling on top of `HAND_TARGET_MAX`, not a rare edge case.
- **Is the dropped-SELL side actually a loss?** Likely a cost-of-delay tax, not a permanent one — the goods stay in the shed and get resubmitted as ordinary sell orders next turn (this is the same framing the whole order-priority sort already uses), so this isn't outright forfeited revenue in most cases. But it stacks with the already-flagged `SHED_AT_CAP` dominant loss-tag mechanism (§3) — a delayed sell is exactly the kind of thing that can tip a shed into force-dump territory before the "paced" sell path would have cleared it on its own.
- **Verdict: not a blocker, doesn't invalidate any prior result, but corrects the record — this risk is not rare, it is constant and now fully quantified.** Worth flagging as a well-motivated *future* candidate (e.g. a HIRE priority that declines within a day as `hire_count` rises, mirroring Fibonacci's exploding marginal cost, similar in spirit to how `_seed_priority` already rises toward a cutoff) but that would need its own isolated, single-variable test per §7's discipline — not built here, this section was the audit, not a fix.
- **Diagnostic scripts kept in the project folder:** `trace_v82_truncation_agent.py` (instrumented copy of `main_v8.2.py`, TRUNC stderr line whenever `priced_orders` exceeds `MAX_MARKET_ORDERS`, zero behavior change) and `trace_v82_truncation.py` (the seed×opponent sweep runner). Reusable for re-checking this after any future build.

---

## 6. Proposed v8 architecture

**Fork point: `main_v7.11.py` for anything not yet touching task assignment; `main_v8.py` for anything that is,** now that §5.1 is built and validated. Not `main_v7.6.py` (stale — missing the strawberry fix and order-sort), not `main_v7.9.py` (superseded by v7.11's validated +$1,279/game order-sort).

### 6.1 Layer 0 — instrumentation (rebase, don't redesign)

`main_v8.py`'s Phase 1 foundation is good work and shouldn't be redone from scratch: `build_state()`, `analyze_opponent()` (direct extraction, explicitly not a Bayesian classifier — already correctly scoped down once, keep it that way), and the `DecisionLog`/`_log_safe(kind, day, hour, build)` thunk pattern (assembly + write share one try/except, so a logging bug costs one record, never a turn — this was a real, deliberately-designed fix, not incidental). **Action: re-fork this layer onto `main_v7.11.py`** (currently it's a diff against v7.6) and re-run the existing no-op verification (`--both-seats` exactly 0.0, fault-injection test, smoke matrix) before trusting it as the new foundation. Ship decision-log on by default per D65's reasoning (replays only show what the agent *did*, not the branch that produced it — a dormant log is zero diagnostic data from the only real-opponent games this project gets).

### 6.2 Layer 1 — the one real architecture change: global task assignment

Replace `unit_action()`'s independent-per-unit-greedy loop with a single per-turn assignment pass (§5.1). This is the only item on this list that changes the agent's *shape*, not just its constants — build and test it in total isolation from everything else below.

### 6.3 Layer 2 — isolated, cheap, still-open economic variables

In priority order per §5: FERTILIZE-wheat alone (5.2) → wheat/strawberry reweight on v7.11 (5.3) → hire/sell truncation stress test (5.4). Each gets its own file, its own `--both-seats` A/B, never stacked with another untested variable — this discipline is the reason v7.1's three-fix bundle silently cancelled itself and the reason Candidate E's real result was hidden behind a gate bug for a whole test cycle.

### 6.4 What v8 should explicitly NOT touch

Everything in §4, plus: the animal feasibility gate's existing five checks (symptom-based, already validated, resist the urge to add a sixth without a specific measured failure it's fixing — Candidate H's untested weeds-in-neglect-work edit is exactly this kind of speculative addition); `HAND_TARGET_MAX=18` (dead config by the Fibonacci math, changing it does nothing since budget/order-slots never let it bind — leave it, don't "clean it up"); any EV/marginal-value scoring formula as a *replacement* for existing rule logic (the cost-of-delay order sort is a scoring model and it works, but it scores *order submission priority*, a genuinely scarce resource — it is not a general license to re-litigate land/animal/crop decisions as EV comparisons, which is the exact framing that lost in the v7.1 round and that the original v8 spec never recovered from).

---

## 7. Testing discipline (restated, this project has been burned by all of these)

- **Always `--both-seats`, never `--swap-half`.** The engine's per-day weed RNG stream is shared and sequential across both players, so seat position alone is worth several thousand dollars; `--swap-half` shuffles that bias without cancelling it (D62 — this is how v7.7 was wrongly rejected).
- **Fresh module instance per game in any local A/B loop.** `animal_plans`/`reserved_sites` are module globals; reusing one loaded module across `env.run()` calls leaks state between "independent" games and can flip a result (the v7.11 round's first test run gave a false regression this way).
- **`random` as an opponent is a crash check only, not an A/B baseline** — its RNG is unseeded and unreachable by `env.info["seed"]`, ~$2,150 spread across identical repeated runs with the agent held constant (D66).
- **Confirm any mechanism trace across ≥5 seeds before writing it down**, not one game — single-game traces gave the wrong answer twice in one session (v7.8's fleet-shrink hypothesis, true on 2/6 seeds only; a seed-42 spot check where v7.8 actually won the one game sampled while losing 5/6 overall).
- **Any opponent-pool result must record both sides' money.** The v7.5 round's own numbers (§3) looked like progress for months because only our own score was logged.
- **One variable per build.** Every rejection in §4 that had a root cause traced (v7.1, Candidate E) traced back to a bundle hiding which specific change did the damage.

---

## 8. Suggested build order

1. ~~Build and test global task assignment (§5.1) in full isolation~~ — **done, Aug 5. Validated: 15/15 seeded wins vs v7.11, +$10,238/game mean, mechanism confirmed, shipped as `main_v8.py`.** This was listed as the biggest lift/least certain item on this list and it's now the current champion candidate.
2. Rebase the decision-log/state foundation onto `main_v8.py` (not v7.11 directly, now that v8 exists), reverify no-op — unblocks instrumented diagnosis of whatever's tested next, including a fresh movement/work-ratio and `SHED_AT_CAP`-equivalent trace on top of the new base.
3. ~~Stress-test the HIRE-priority assumption inherited from v7.11 (§5.4)~~ — **done, Aug 5. Result: truncation fires in 100% of games (17.1/game), not the assumed 0 — see §5.4/§4 for the full quantified breakdown. Not a regression (identical on v7.11/v8/v8.2), not a blocker, flagged as a future optimization candidate only.**
4. ~~Test FERTILIZE-wheat alone (§5.2), on top of `main_v8.py`~~ — **done, Aug 5. Rejected: 0/15 seeded vs `main_v8.py`, -$19,019/game, t=-7.69. See §4/§5.2.**
5. ~~Test WHEAT/STRAWBERRY reweight directly on `main_v8.py` (§5.3)~~ — **done, Aug 5. Validated: 12/15 seeded wins vs main_v8.py, +$4,482/game mean, t=+4.86, 95% CI entirely positive. Shipped as `main_v8.2.py`, new champion candidate pending the 48-turn smoke re-run.**
6. ~~Submit `main_v8.py` to the real ladder~~ — **done, Aug 5, 19:51 UTC, public score 667.1.** **Submit `main_v8.2.py` next** — it supersedes plain v8 (§5.3, +$4,482/game validated) and hasn't touched the ladder yet. `main_v7.11.py` remains unsubmitted too, but is now superseded by both v8 and v8.2 either way.
7. `main_v8.py` still loses decisively to `opp_frontier_v12.py`/`opp_scenario_v14.py` — the §3 volume gap is not closed by this one change. Re-run the full opponent-pool matrix (both sides' money, per §7) once another lever from steps 3-5 stacks on top, to see how much of the remaining gap each closes.
