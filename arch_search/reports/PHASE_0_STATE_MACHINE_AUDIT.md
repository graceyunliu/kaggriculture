# Phase 0 State-Machine Audit + Phase 1 Findings (TDAS)

Date: 2026-09-07. Scope: `arch_search/` Phase 0 (state taxonomy validation) and Phase 1
(divergence, hand-built candidates, causal-prediction testing), per
`docs/SPEC-trajectory-directed-architecture-search.md`.

**Substrate honesty note (read first):** every DayState in this audit comes from
`evolve/trace.py`'s existing per-day METRICS (via `arch_search/trajectory.py`, which adds no
new instrumentation). That substrate does NOT expose land-parcel counts, per-species crop/
animal composition, or explicit spatial layout. `production_composition` here is therefore
always the aggregate stock `animals + plants` (a count of live tiles, not cumulative
production), never a per-species breakdown. Every finding below is stated in terms of what
this substrate actually contains — no field was invented to make a state "fit."

## Reference panel (arch_search/references.py)

Built from real inspection of `Opponents/tapes.json` (17 entries) and `Opponents/*.py`:

| name | file | why picked |
|---|---|---|
| shared_clone | tape_atakan_104893687.py | representative of an 8/17-tape shared fingerprint family (5xHIR, BUYCO2, BUYSH2, wheat round-trip, BUYME12); median money in that family ($107,245) |
| budget_fork | tape_jessebullard_105876759.py | clearest minority template: cow-heavy, 1 sheep, no wheat round-trip/melon buy |
| divergent_strawhats | tape_strawhats_105080848.py | highest-money tape in the file ($175,524); wheat trade BEFORE hiring (reverse of clone order) |
| divergent_kronki | tape_kronki_99169921.py | no SELWH round-trip at all; interleaved hire/buy order; $135,975 |
| divergent_kwa | tape_kwa_105860490.py | hires before any animal purchase (reverse of clone); buys CARROT (unique); $133,821 |

`candidates/V3_12.py` is the champion under test (confirmed via `evolve/space.py`'s K.py
docstring "knob-parameterized V3.12 chassis" and repo memory: "frontier = V3_12 per
Grace"). It is NOT part of the panel. All 5 panel members were run seat 0 vs. V3_12 (a
fixed neutral opponent, seed 1); V3_12 itself was run seat 0 vs. `Opponents/opp_scenario_v14.py`
(a genuinely independent opponent), so neither trajectory is self-referential.

## A. Taxonomy validity, per state

Method: ran `extract_state_sequence()` (arch_search/state_machine.py) on all 5 panel
trajectories + V3_12, read the resulting graphs by hand, then computed
`find_convergent_transitions()` (min_fraction=0.6). Full per-reference sequences are
reproducible via `python3 -m arch_search... ` (see references.py/state_machine.py
docstrings for the exact calls used).

| state | verdict | evidence |
|---|---|---|
| BOOTSTRAP | **supported** | production_units == 0 on day 0 for all 6 trajectories by construction; not a tuned threshold. |
| PRODUCTION_ACTIVATION | **supported, but recurs (not a one-time gate)** | fires 5/5 on the panel at day 1 (confidence 5/5, entry_day_spread 0). All 6 trajectories jump from 0 to ~20-24 units within days 1-3. However, because "production_units" is a live-tile *stock*, not cumulative output, this condition re-fires every time the stock grows again later in the game (visible in every sequence dump: PRODUCTION_ACTIVATION intervals recur at days 7-9, 12-13, 15-25 for various references). This is a real property of the data, not a bug: the taxonomy's implicit assumption that each state is entered once needs revision — see section B. |
| DENSIFICATION | **supported as a plateau signal, but weak on champion** | 5/5 panel confidence, all entering at day 3 (entry_day_spread 0). Champion enters 3 days later (day 6) — see section D. Champion's version of the "plateau" is also less clean (see D). |
| LABOR_SCALE | **supported** | 5/5 panel confidence; single-day hands_delta>=3 fires in every panel member (entry_day_spread only 2 days, days 5-7). Champion's LABOR_SCALE burst is at day 12 — the single largest divergence found (section D). |
| EXPANSION_READY | **ambiguous / weakest state in the taxonomy** | 4/5 panel confidence (kronki and, on inspection, its own day-8/day-13 waves don't show a clean pre-jump "ready" day the way shared_clone/budget_fork/strawhats/kwa do), relative_order_agreement 0.75 (not 1.0). Cash-floor and idle-share conditions (THRESHOLDS `expansion_ready_min_cash`/`expansion_ready_max_idle_share`) did not cleanly separate a distinct "ready" day from ordinary DENSIFICATION days in several trajectories — this state is currently defined mostly by lookahead (the day before an EXPANSION jump), which is circular for prediction purposes. **This state needs revision or removal before further automation** — it is currently doing less work than the taxonomy assumed. |
| EXPANSION | **supported for 4/5, absent as a clean single spike for kronki** | 4/5 panel confidence; the `expansion_min_jump=15` threshold (picked as the min-across-panel second-wave delta) correctly separates the wave from the day3-8 plateau noise for 4 of 5 references. kronki's growth is smoother/more continuous rather than wave-shaped, so its EXPANSION intervals fire multiple times at smaller jumps that don't individually cross 15 as cleanly — a real, reported case of the taxonomy not fitting one panel member. |
| THROUGHPUT_SCALE | **supported, and the clearest real divergence for the champion** | 5/5 panel confidence, but entry_day_spread is 9 (days 10-19) — this is genuinely the least day-stable of the "5/5" states, meaning "reaches revenue-scale" varies more in timing than the other convergent states even though every panel member does reach it. Champion crosses the 25,000/5-day-window threshold only once (day 23) versus the panel's sustained multi-day windows starting day 10-19 -- champion's revenue rate is structurally weaker here, not just later. |
| ENDGAME_CONVERSION | **supported but the champion's version is more extreme** | 5/5 panel confidence. Every trajectory's production_units stock drops sharply in the last ~5 days (harvest liquidation) but champion's drop is much steeper (71->19, a 73% decline) than the panel's (typically 30-45% declines) — worth flagging as a *possible* additional real difference (champion may over-liquidate at the end), though this was not tested causally in Phase 1 (out of scope this round). |

## B. State overlap

**Yes — trajectories are frequently in multiple states at once, and the representation was
designed for that from the start** (`extract_state_sequence(..., allow_overlap=True)` is
the default). Concretely: LABOR_SCALE (a single burst day) very often coincides with an
active DENSIFICATION or EXPANSION_READY interval in the same day, and PRODUCTION_ACTIVATION
recurs inside what would otherwise be called an ongoing THROUGHPUT_SCALE window (see e.g.
`shared_clone`'s dump: THROUGHPUT_SCALE 10-14 overlaps PRODUCTION_ACTIVATION 12-13 and
EXPANSION 12-12). The representation is a **list of possibly-overlapping
`(state, entry_day, exit_day)` intervals**, not a single label per day; `allow_overlap=False`
is offered for callers that need a flattened, priority-ordered single-state view, but that
mode was NOT used for the findings in this report, since it would have hidden real
concurrent behavior (per the spec's explicit instruction not to force exclusivity without
evidence).

## C. Convergent transitions (confidence counts)

From `find_convergent_transitions()` on the 5-reference panel:

| transition | confidence | entry_day_spread | relative_order_agreement |
|---|---|---|---|
| BOOTSTRAP | 5/5 | 0 | 1.0 |
| PRODUCTION_ACTIVATION | 5/5 | 0 | 1.0 |
| DENSIFICATION | 5/5 | 0 | 1.0 |
| LABOR_SCALE | 5/5 | 2 | 1.0 |
| EXPANSION_READY | 4/5 | 4 | 0.75 |
| EXPANSION | 4/5 | 4 | 0.75 |
| THROUGHPUT_SCALE | 5/5 | 9 | 0.8 |
| ENDGAME_CONVERSION | 5/5 | 3 | 0.6 |

`implementation_detail` was empty at `min_fraction=0.6` — i.e. every state in the taxonomy
clears the bar on this panel, though several (EXPANSION_READY, EXPANSION,
ENDGAME_CONVERSION's order agreement at only 0.6) are marginal, not clean invariants. This
is reported honestly rather than treated as "the taxonomy fully validated" — see the
adversarial test in `arch_search/tests/test_convergence.py` confirming the same code
correctly REJECTS convergence on a panel deliberately constructed to disagree.

## D. Champion divergence

`find_first_divergence()` (state-level-first, per spec 2.5) on V3_12's sequence against the
panel's convergent-transition set returns, in trajectory order:

```
kind: state_trigger_change
day: 6
state: DENSIFICATION
candidate_entry_day: 6
panel_entry_day_range: [3, 3]
```

**Causal framing (claimed only to the extent evidence supports it):** V3_12's first
structural divergence from every panel reference is that its production-stock growth
continues through day 4-5 before plateauing (DENSIFICATION at day 6), where every panel
member plateaus by day 3. The SECOND, larger divergence (not "first" by trajectory order,
but the largest gap found) is LABOR_SCALE: V3_12's first hiring burst (hands_delta>=3) is
day 12, vs. the panel's day 5-7 — a 5-7 day lag. Because LABOR_SCALE's panel median day (6)
is later than DENSIFICATION's (3) in `find_first_divergence`'s panel-order-based check,
DENSIFICATION is reported as occurring earlier in trajectory order, but **this ordering
does not establish which is causally upstream of the other** — that is exactly why Phase 1
built a testable hypothesis (H1) around the labor lag rather than asserting it. Testing H1
directly (see below) is what actually probes causal order, not the priority heuristic alone.

## E. Relationship to prior findings

- Memory's "labor scaling" / "V3.4 wastes...labor per obligation is half V3.4's" line of
  investigation, and the day-planner-executor work, both independently arrived at labor
  timing/allocation as a suspect area. This audit's finding (champion's hiring burst lags
  the panel by 5-7 days) is **consistent with that prior suspicion**, but is a distinct,
  freshly-measured finding, not a restatement of it — the panel/method here (condition-
  triggered state sequences across 5 independently-selected tapes) did not exist before.
- Memory's `kaggriculture-m2-exploit-vs-m3-general-sep05.md` explicitly warns that an edge
  derived from ONE opponent's fingerprint (M2) failed to generalize (M3). This audit's
  reference panel was deliberately built from 5 *different* tapes spanning the shared-clone
  fingerprint, the budget fork, and 3 independently-strong divergent tapes, specifically to
  avoid repeating that mistake — see `find_convergent_transitions`'s adversarial test.
- **Contradiction worth reporting plainly:** the "three-quadrant land timing" and
  "densification" narratives in `docs/cs329a-applied-to-kaggriculture.md` are framed around
  *land* utilization. This substrate (evolve/trace.py) does not expose land-parcel counts at
  all, so this audit's DENSIFICATION/EXPANSION states are proxies built from the
  animal+plant stock, NOT literal land utilization. The audit's finding (day-6 vs day-3
  plateau) may or may not be the same phenomenon prior land-timing work found — this cannot
  be confirmed or denied with the current tracer, and should not be conflated with it. A
  genuinely land-aware version of this taxonomy would need `mini_engine.py`'s richer
  `run_game(trace=True)` output (which does carry a `land` field), not `evolve/trace.py`'s.

---

# Phase 1 addendum: divergence, hand-built candidates, causal-prediction testing

## Hypothesis H1 (arch_search/hypothesis.py, arch_search/ledger.db)

> **Causal claim:** V3_12's demand-coupled hiring target (`_load_model`) lags the reference
> panel's own hiring bursts by ~6-7 days; this labor lag is upstream of (causes) V3_12's
> later DENSIFICATION/EXPANSION/THROUGHPUT_SCALE, not merely correlated with them.
>
> **Prediction, in order:**
> 1. LABOR_SCALE (hands_delta>=3) fires by day 9 (vs. V3_12's own day 12)
> 2. DENSIFICATION fires by day 4 (vs. V3_12's own day 6)
> 3. EXPANSION fires earlier than V3_12's own day 13
> 4. final money improves vs. V3_12 (same seed/opponent)

## Hand-built candidates (arch_search/candidates/early_labor/)

Two candidates test this hypothesis with different implementations of "pull hiring
forward" — a `.py` copy of `candidates/V3_12.py` with ONLY `_load_model`'s output floored
by a new function, `_early_labor_floor(day)`. Neither candidate copies any opponent's exact
actions (the clone-replica dead end recorded in memory); the floor is an internal knob
override, not a fingerprint port.

- **floor_v1** (gradual ramp, target floor 4->9 over days 0-6)
- **floor_v2** (aggressive front-load, target floor ~8-9 in days 0-2, tapering by day 5)

Both were smoke-tested via `mini_engine.py` (3 seeds, both seats) vs. `Opponents/opp_scenario_v14.py`
— no agent errors either candidate:

| candidate | mean money (agent) | vs. V3_12 baseline mean ($84,855) |
|---|---|---|
| V3_12 (baseline) | $84,855 | — |
| floor_v1 | $94,089 | **+$9,234** |
| floor_v2 | $86,817 | +$1,962 |

**This is exactly the situation the spec's causal-prediction check exists for.** Both
candidates scored ABOVE baseline. A score-only view would read this as "the labor-lag
hypothesis worked, and worked best for the gentler version." `test_causal_prediction()`
tells a different, more careful story:

| candidate | novelty gate | step 1 (LABOR_SCALE<=9) | step 2 (DENSIFICATION<=4) | step 3 (EXPANSION<13) | step 4 (money up) | classification |
|---|---|---|---|---|---|---|
| floor_v1 | **FAILED** (day-10 distances all below threshold; state sequence unchanged) | day 13 — **False** | day 6 — **False** | day 14 — **False** | True | **PREDICTION_CHAIN_FAILED** |
| floor_v2 | **PASSED** (investment_sequence distance 0.52; state sequence diverged) | day 8 — **True** | day 4 — **True** | day 15 — **False** | True | **FALSIFIED** |

**Reading this honestly:**
- **floor_v1**, the candidate that scored *best*, never actually achieved an earlier hiring
  burst against this particular opponent (`_load_model`'s own organic demand already exceeded
  the gentle floor most of the time) — its trajectory barely differs from V3_12's at all by
  day 10 (it fails the novelty gate outright). Its score gain is very likely NOT explained by
  H1's mechanism; the code change was close to a no-op against this opponent, and whatever
  produced the +$9,234 is unexplained by this hypothesis. This is the exact failure mode the
  spec warns about (a correlated score gain almost got mistaken for confirmation) — caught
  here specifically because `test_causal_prediction()` was checked before believing the
  score.
- **floor_v2** DID achieve the mechanism's first two steps for real (LABOR_SCALE day 8,
  DENSIFICATION day 4 — both clearly pulled forward, and it passes the novelty gate). But
  EXPANSION fired LATER (day 15), not earlier, than V3_12's own day 13 — the predicted chain
  breaks at step 3. Per the classification rule, this is FALSIFIED, not "partially working":
  pulling labor and densification forward did not propagate into an earlier expansion, so H1's
  specific causal claim (labor lag -> densification lag -> expansion lag -> throughput
  gap) is not supported past its second link, even though floor_v2 also beat baseline on
  final score.

**Conclusion for H1:** REJECTED as a full causal chain on this evidence. The labor-timing
divergence found in Phase 0 is real (both floor_v1 and floor_v2 exist as valid tests of it),
but pulling hiring forward alone does not reproduce the panel's earlier EXPANSION timing —
something else (plausibly land/site availability, which this tracer cannot see, or a
downstream capital-allocation decision independent of headcount) is also gating EXPANSION.
Both findings are recorded in `arch_search/ledger.db` (`early_labor/floor_v1` ->
ARCHITECTURAL_DEAD_END, `early_labor/floor_v2` -> FALSIFIED) and neither candidate is
promoted anywhere; per spec, falsified/dead-end entries are kept, not deleted.

## Limitations (explicit)

- The taxonomy's thresholds were derived from a 5-tape + 1-champion panel, all facing either
  V3_12 or opp_scenario_v14 as the opponent — a single opposing-pressure condition. Whether
  the same thresholds hold against a materially different opponent is untested.
- EXPANSION_READY is the weakest state in the taxonomy (section A) and should be revised or
  cut before any further automation.
- The raw-field fallback (`divergence.raw_field_divergence`, 1.5 MAD / >=2-day persistence)
  was implemented and unit-tested but not exercised on real trajectories in this round,
  because the state-level check found a real divergence first in every case tried — its
  per-field tolerance is still an unvalidated starting guess (spec's own open question).
- `production_composition` is a stock, not cumulative output — this caused
  PRODUCTION_ACTIVATION to recur rather than gate once, which the taxonomy did not originally
  anticipate (documented in section A rather than patched over).
- Land utilization (central to the spec's own EXPANSION_READY definition) is not observable
  from `evolve/trace.py` at all; this audit's EXPANSION_READY/EXPANSION conditions are proxies
  built from production-stock deltas and cash/idle-share, not literal land saturation. A
  land-aware revision would need to switch part of the substrate to `mini_engine.py`'s
  `run_game(trace=True)` output (which has a `land` field) instead of/alongside
  `evolve/trace.py`.
- Only 2 hand-built candidates were tested (spec allows 2-3); no `classify.py`/`hypothesize.py`
  automation was built, per the spec's stop condition (automation should wait for at least
  one fully CONFIRMED hypothesis, which this round did not produce).
