# P8v2 → P8v5 — Crop-Selection (R4) Diagnosis

Status label convention (same as DIAGNOSIS.md / DIAGNOSIS_V2.md / DIAGNOSIS_V3.md /
REPORT.md / RNG_PATH_DEPENDENCE_AUDIT):
**DIRECTLY_OBSERVED** = read straight off code or an engine run with no inference.
**SUPPORTED** = inferred from multiple directly-observed data points.
**PLAUSIBLE** = a reasonable read that wasn't independently confirmed.
**UNRESOLVED** = open question, flagged rather than guessed at.

## 0. Scope and method — DIRECTLY_OBSERVED

Task brief: DIAGNOSIS_V3.md ruled out sell-timing (R5) and cash-buffer sizing as the
residual `P8v2_reactive_allocation.py` vs `P6_baseline.py`/`C1.py` gap
(-$12,634/-$16,365 per game) and pointed at R4 crop-mix selection — P8v2 sells 5-7x
more low-value WHEAT while moving 25-40% as much high-value STRAWBERRY/MILK, at
realized prices *equal to or better* than P6/C1's. This round diagnoses R4 itself:
why does the identical greedy value/cycle ranking pick WHEAT so much more often for
P8v2 than for P6/C1?

`experiments/P8_DIAGNOSIS/instrument_v4_cropmix.py` (new file) monkeypatches each
policy's freshly-loaded, in-memory `economy(obs, v)` function with a read-only
logging shim: the shim calls the real, unmodified `economy()` to get the real orders
(nothing about the decision is altered), then independently recomputes — for
logging only, using each policy's own `CROP_SPECS`/`I0`/`DEMAND_SHARE` constants and,
for P6, its own `_daily_demand` helper — the `room_units`/`val`/`eligible` score the
real greedy loop assigned to WHEAT/STRAWBERRY/MELON that call, plus the actual live
tile count per crop (`v["crops"]`) at every hour-0 snapshot. This is the same
monkeypatch pattern `eval_protocol.py` already uses on `mod._commit_unit`; neither
`P8v2_reactive_allocation.py` nor `P6_baseline.py` is modified on disk. Ran P8v2 and
P6 vs `Opponents/opp_scenario_v14.py`, seeds 1-10, both seats (n=20 games/policy).
Raw per-game logs: `experiments/P8_DIAGNOSIS/raw_v4/*.json`. Aggregate:
`experiments/P8_DIAGNOSIS/summary_v4.json`. 0 agent errors across all 40 games.

**Methodology correction made mid-run, DIRECTLY_OBSERVED**: R4 has no `hour==0` gate
in P8v2 (unlike R5's sell logic) — the first pass of the instrument only logged at
hour 0 and undercounted purchases by ~15x (26 WHEAT-seed units logged vs the ~780
actually bought per 6-game sample). Fixed by logging every `economy()` call that
actually places a `BUY_SEED` order, not just the hour-0 call.

## 1. Headline finding — DIRECTLY_OBSERVED: real tile-occupancy inversion, not a
   ranking-formula preference for WHEAT

Cumulative `BUY_SEED` unit counts are biased by rebuy frequency (WHEAT's 5-day
cycle needs re-seeding ~4x more often per tile than STRAWBERRY's 18-day one, since
STRAWBERRY is an "ongoing" crop that keeps yielding on the same planting). The
unbiased metric is **live tile count per crop, sampled at every hour-0 snapshot**
(`summary_v4.json`, n=20 games/policy, seeds 1-10, both seats):

| metric | P8v2 | P6 |
|---|---|---|
| mean live WHEAT tiles | **18.67** | 5.14 |
| mean live STRAWBERRY tiles | **6.45** | 24.88 |
| max live WHEAT tiles (any snapshot) | 54 | 43 |
| max live STRAWBERRY tiles (any snapshot) | 21 | 69 |
| % of logged calls where STRAWBERRY is `eligible` (room_units/min_val pass) | 41.1% ineligible | 42.0% ineligible |
| mean greedy `val` for STRAWBERRY when eligible | **46.96** | 39.88 |
| mean greedy `val` for WHEAT when STRAWBERRY also eligible | 41.05 | 35.39 |

This confirms the tile-allocation split is real and dramatic (P8v2 runs ~2.9x more
WHEAT tiles than STRAWBERRY tiles; P6 runs ~4.8x more STRAWBERRY tiles than WHEAT
tiles — a near-total inversion), **not** an artifact of counting rebuy events. But
it directly **disconfirms** the most obvious hypothesis (that P8v2's greedy formula
scores WHEAT higher): STRAWBERRY's `eligible`-day rate is statistically identical
between the two policies (41.1% vs 42.0% ineligible), and STRAWBERRY's mean `val`
when eligible is *higher* than WHEAT's for **both** policies (46.96 > 41.05 for
P8v2; 39.88 > 35.39 for P6) — the `if val > best[0]` greedy pick should favor
STRAWBERRY over WHEAT about as often in both files. Something other than the
ranking formula itself is driving the skew.

**Candidate mechanism identified, DIRECTLY_OBSERVED**: `P6_baseline.py` line 317-318
gates its entire hiring/land/herd/crop-mix block behind a once-per-day check:
```python
capital_hour = 0 if day == 0 else 1
if hour != capital_hour and not (...): 
    <skip the whole R1-R4-equivalent block>
```
P8v2's R1-R4 have **no such gate** — `economy()`'s crop-mix section runs on every
hour of every day. Call-count data confirms this directly: P8v2 logged 3,455
economy-with-activity calls across 20 games (172.75/game, ~6x/day) vs P6's 934
(46.7/game, ~1.6x/day). WHEAT's cheap seed cost (`$10` vs STRAWBERRY's `$100`) means
`k = min(space, room_units // units, free // seed, 20)` is rarely cash-limited for
WHEAT (so it hits the `20`-unit cap whenever it wins a greedy iteration) while
STRAWBERRY's `k` is very often limited by `free // 100`, buying only a few tiles per
win even when it does win the greedy race.

## 2. Retune tried — TESTED, made the outcome WORSE, and the mechanism hypothesis
   is DISCONFIRMED by the retune's own trace

`candidates/P8v5_reactive_allocation.py` (new file, branched from P8v2 only — NOT
from P8v3/P8v4) makes one targeted change: gate R4 to run once per day, matching
P6's `capital_hour` pattern exactly:
```python
capital_hour = 0 if day == 0 else 1
if space > 0 and not labor_saturated and day >= 1 and hour == capital_hour:
```
(R1/R2/R3/R5 left untouched, to isolate the R4-frequency effect specifically.)

**Paired-eval results** (`eval_protocol.py compare_paired()`, seeds 1-20, both seats,
n=40 games/pair):

| comparison | mean delta | stdev | t | wins/losses/ties |
|---|---|---|---|---|
| P8v5 vs P8v2 (direct) | **-$9,492/game** | $18,035 | -3.33 | 12W/28L/0T |
| P8v5 vs P6 | **-$23,825/game** | $24,020 | -6.27 | 5W/35L/0T |
| P8v5 vs C1 | **-$25,871/game** | $24,561 | -6.66 | 7W/33L/0T |

This is a decisive regression relative to P8v2's own baseline (-$12,634/-$16,365 vs
P6/C1) on both real targets, and a decisive, large-sample loss directly against
P8v2 (t=-3.33, n=40) — worse than DIAGNOSIS_V2's/V3's herd/cash-buffer retunes were
against P8v2 directly (those were t=-0.77 to -2.58, not this decisive).

**Re-instrumenting P8v5 with the same `instrument_v4_cropmix.py` harness
(seeds 1-10, both seats, n=20) shows the once-per-day gate did NOT meaningfully fix
the tile-occupancy skew it was built to fix**:

| metric | P8v2 | P8v5 | P6 |
|---|---|---|---|
| mean live WHEAT tiles | 18.67 | **15.44** | 5.14 |
| mean live STRAWBERRY tiles | 6.45 | **6.25** | 24.88 |
| mean final $ delta vs opp | -29,736 | **-36,166** | +17,668 |

WHEAT tiles dropped only modestly (18.67 -> 15.44), STRAWBERRY tiles barely moved
at all (6.45 -> 6.25, essentially unchanged), and the $ outcome against the fixed
opponent got *worse*, not better (-29,736 -> -36,166). **The call-frequency
hypothesis from §1 is therefore DISCONFIRMED by its own retune's data**: cutting R4
to once/day mostly just cut total planting throughput (fewer opportunities to
re-fill tiles that harvests free up mid-day) without rebalancing which crop wins
when it does fire, and losing that throughput cost more than the (nearly
nonexistent) mix improvement was worth.

## 3. What the data leaves as the live lead — UNRESOLVED, not further tested this
   session (budget)

Given §2's result, the tile-count skew is still real (§1) but its cause is not the
call-frequency mechanism this round tested. The one remaining concrete,
DIRECTLY_OBSERVED asymmetry not yet isolated is the **per-iteration order-size cap
interacting with cash affordability**: `k = min(space, room_units // units,
free // seed, 20)` lets WHEAT (seed cost $10) hit the flat `20`-unit cap almost
every time it wins a greedy iteration, while STRAWBERRY (seed cost $100) is
constrained by `free // 100` far more often — meaning even on the many days
STRAWBERRY's `val` legitimately beats WHEAT's (§1's 46.96 vs 41.05 mean), the order
STRAWBERRY places may still be small relative to WHEAT's maxed-out order the next
time WHEAT wins. **This is PLAUSIBLE, grounded in the same instrument_v4 data
(cheap-seed high-cap crop vs expensive-seed cash-limited crop), but was not
independently isolated with its own controlled retune in this session** — doing so
honestly would require a fifth build-test-measure cycle, which the evidence below
argues against committing to blind.

## 4. Verdict — gap NOT closed, this line of investigation should stop here

**R4 ranking formula**: not the leak. STRAWBERRY's greedy `val` beats WHEAT's on
average whenever both are eligible, in both P8v2 and P6 (§1) — the formula itself,
copied verbatim from P6, is not mis-ranking crops.

**R4 call frequency (hourly vs once/day)**: tested directly and **disconfirmed** —
gating to once/day barely moved the WHEAT/STRAWBERRY tile split and made the $
outcome decisively worse (§2), the most decisive single-retune regression across
all four diagnosis rounds (t=-3.33 vs P8v2 directly, t=-6.27/-6.66 vs P6/C1).

**Four independent diagnosis rounds now** (DIAGNOSIS.md's `LOAD_PER_HAND` fix aside,
which is the one retune that worked) **have each identified a real, concrete,
directly-observed structural gap between P8v2 and P6/C1, and each time retuning
that specific gap has made the $ outcome worse, not better**: land/herd (DIAGNOSIS_V2,
worse in both directions tried), sell-timing/cash-buffer (DIAGNOSIS_V3, no-op to
marginal regression), and now crop-selection call-frequency (this report, decisive
regression). The pattern across all three post-LOAD_PER_HAND rounds is consistent:
**every individual allocation rule in P8v2, examined in isolation, looks locally
"wrong" relative to P6/C1's hand-tuned equivalent — but P6/C1's rules are not
independent constants, they are a jointly co-tuned system** (P6's `capital_hour`
gate, `wheat_target=0`-so-inert wheat floor, `HERD_RATIO_CAP`-equivalent, and
`melon_floor`/`wheat_sell_price` were all evidently tuned together against each
other and against a fixed opening), and porting any single piece of that system
into P8v2's differently-structured reactive policy does not reproduce the
system's emergent behavior — it just perturbs a different equilibrium.

**Recommendation: stop iterating on P8 via further single-constant or
single-mechanism retunes.** Four rounds (this one included) have now each found a
real gap and each time made the outcome worse by fixing it in isolation — that is
no longer noise, it is a structural signal that P8v2's remaining -$12.6k/-$16.4k
gap to P6/C1 is not decomposable into independently-retunable pieces the way
`LOAD_PER_HAND` was. Closing it further would need either (a) a full joint
re-tune/search over R1-R5's constants together (an ES/grid search, not a hand
picked single change — out of scope for a diagnosis session), or (b) accepting
`candidates/P8v2_reactive_allocation.py` as the terminal state of this reactive-
policy line and moving effort to a different lever entirely. This report does not
recommend which of those two paths to take next — only that continuing to test
one-constant-at-a-time hypotheses against this specific gap has now failed
identically four times running and should not be a fifth default next step without
new information.

## Files

- `candidates/P8v5_reactive_allocation.py` — P8v2 + R4 gated to `hour ==
  capital_hour` (once/day, matching P6's pattern). Tested, decisive regression —
  see §2-4. Does not touch R1/R2/R3/R5.
- `experiments/P8_DIAGNOSIS/instrument_v4_cropmix.py` — instrumentation harness
  (monkeypatches each policy's in-memory `economy()` with a read-only logging shim;
  reused unmodified against P8v5 for the §2 re-check).
- `experiments/P8_DIAGNOSIS/raw_v4/*.json`, `experiments/P8_DIAGNOSIS/summary_v4.json`
  — the 40-game P8v2/P6 crop-decision trace data behind §1.
- `experiments/P8_DIAGNOSIS/raw_v4b/*.json` — the 20-game P8v5 re-check trace behind §2.
- `experiments/P8_DIAGNOSIS/p8v5_vs_P8v2.json`, `p8v5_vs_P6.json`, `p8v5_vs_C1.json`
  — full `compare_paired()` reports (n=40, seeds 1-20, both seats) behind §2.
- This report: `artifacts/reactive_allocation_p8/DIAGNOSIS_V4.md`.
- Prior reports: `artifacts/reactive_allocation_p8/DIAGNOSIS_V3.md`,
  `DIAGNOSIS_V2.md`, `DIAGNOSIS.md`, `REPORT.md`.
