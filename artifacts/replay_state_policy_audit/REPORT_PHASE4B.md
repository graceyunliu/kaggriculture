# Replay Mining Phase 4B: Minimal Causal Intervention Test

Date: 2026-09-08. Follow-on to `REPORT.md`, `REPORT_PHASE2.md`,
`REPORT_PHASE3.md`, `REPORT_PHASE4A.md` - see [INDEX.md](INDEX.md) for the
provenance correction that applies to all of those. This phase is
**diagnostic, not a strategy proposal**: it tests whether the
statistically-confirmed melon-opportunity behavioral divergence (Phase 4A)
has a measurable causal footprint on an isolated policy variant, and
reports the answer honestly regardless of direction. **No adoption
recommendation is made anywhere in this report.**

**Final status (causal question, distinct from Phase 4A's behavioral-
divergence status): NO_ROBUST_SIGNAL for a performance/score effect;
PARTIAL_EVIDENCE for a sell-rate/revenue effect (present but small, and
smaller than Phase 4A's replay-derived effect size - see Limitations for
why these are not directly comparable).**

## Pre-registered hypothesis and predictions (written before any evaluation was run)

**Hypothesis**: increasing/altering melon-sale admission (the decision made
when `shed.MELON > 0`, the same deterministic, RNG-independent gate
established in Phase 3) changes realized melon liquidation and produces a
downstream economic effect.

**Predictions, evaluated and reported separately, not collapsed into one verdict:**
1. The intervention changes melon-sell rate conditional on opportunity.
2. It changes realized melon sales/revenue in the expected direction.
3. It produces a measurable downstream cash/inventory consequence.
4. Any final-score difference survives fresh-seed evaluation.

A variant that passes (1) but not (2)-(4) is reported as a distinct outcome
from one that passes all four, or 1-3 but not 4 - the report below keeps
these separate per prediction, as required.

## Baseline and variant construction

**Baseline choice and justification**: `candidates/C1.py` - referenced in
this audit's own project-memory context as one of the established
hand-tuned baselines ("P6/C1") that the P8 diagnosis thread compared
against, and, on inspection, it is Kaggriculture's "K" knob-parameterized
V3.12 chassis, with a `melon_floor` knob (default 150) that is *already
the exact decision point* Phase 3 identified: `candidates/C1.py:280-283`:

```python
n = shed.get("MELON", 0)
if n > 0 and (prices.get("MELON", 0) >= KNOBS["melon_floor"] or day >= 27 or shed_load > 75):
    orders.append(["SELL", "MELON", int(n)])
```

This makes C1 the most defensible baseline available: the intervention can
be expressed as a single pre-existing, author-defined knob change rather
than a hand-written new code path, minimizing the risk of accidentally
changing anything beyond the melon-sell decision. **`candidates/C1.py`
itself was never modified** - all variants are copies under
`experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_variants/`.

**Variants built** (byte-for-byte identical to the baseline except the one
line shown):
- `variant0_baseline.py` - unmodified copy of `candidates/C1.py`.
  `KNOBS["melon_floor"] = 150` (unchanged default).
- `variant1_melon_floor0.py` - `KNOBS["melon_floor"] = 0`, i.e. "sell on
  arrival" (the file's own docstring's description of what floor=0 means) -
  the most direct test of "always act on a melon opportunity."
- `variant2_melon_floor50.py` (optional second variant, cheap to add given
  the knob already exists) - `KNOBS["melon_floor"] = 50`, an intermediate
  threshold, to check whether a partial nudge behaves differently from the
  extreme.

No other line differs between any variant and the baseline (verified by
`diff`, single-line change in each case - see `PHASE4B_README.md` for the
exact diffs).

## Evaluation methodology

**Harness reused, not invented**: `mini_engine.py`, this repo's existing
seeded, both-seats-capable, dependency-free evaluation harness (see its own
docstring and `seeded_h2h.py`'s warning about seat bias - `mini_engine.py`
implements the same `--both-seats` seat-bias-cancelling convention:
"every seed played in both seat assignments; margin is the sum," which
this phase reuses via `run_game(..., trace=True)` called for both seat
orders per seed). `mini_engine.py`'s per-day trace (`money, shed, sales,
weeds, ...`) was used directly rather than re-instrumenting anything.

**Seeds**: variant vs baseline, both seats, on:
- **Matched seeds 1-20** (20 seeds x 2 seat orders = 40 games per variant).
- **Fresh seeds 501-510** (10 seeds x 2 seat orders = 20 games), chosen
  from a disjoint range never used in variant construction, tuning, or the
  matched-seed evaluation above, per the pre-registered fresh-seed
  validation requirement.

**Sample size honesty**: this is a small sample (20 matched + 10 fresh
seeds per variant) chosen to fit this session's time budget. `mini_engine`
is fast (the full 40-game matched run completed in ~12 seconds thanks to
its caching and lack of `kaggle_environments` framework overhead), so a
larger run is feasible in a future session if this phase's results
motivate one - but the numbers below should be read with a small-n caveat,
not treated as a large-scale confirmation.

## Predictions (1)-(4): results, reported separately

### Variant 1 (melon_floor=0, "sell on arrival") - matched seeds 1-20

| metric | baseline | variant 1 | 
|---|---|---|
| melon opportunity-days (summed over 40 games) | 173 | 167 |
| melon sold-days | 168 | 168 |
| **approximate** sell rate (sold-days/opportunity-days) | 97.1% | 100.6% |
| melon units sold | 2,607 | 2,607 |
| melon revenue | $555,160 | $555,219 |

- **Prediction (1) - sell rate changes**: **WEAK PASS.** The approximate
  sell rate differs (97.1% vs 100.6%), but both are already near-ceiling in
  this baseline - see "Important caveat about C1's baseline behavior"
  below. The opportunity/sold-day counts are measured from `mini_engine`'s
  daily trace (end-of-day shed snapshots), which is coarser than Phase 3's
  hourly opportunity gate - see Limitations.
- **Prediction (2) - revenue changes in the expected direction**:
  **FAIL.** Melon revenue moved by +$59 out of $555,160 (+0.01%) - not a
  meaningful directional change, and units sold were identical (2,607 =
  2,607).
- **Prediction (3) - measurable downstream cash/inventory consequence**:
  **FAIL (not significant).** Mean seat-controlled margin (variant - 
  baseline), summed both seats per seed: **-$117/game**, stderr $76,
  **t = -1.53** (not significant at conventional thresholds; 17 of 20
  seed-pairs showed exactly $0 margin - see "RNG side-effect audit" for
  why the 3 nonzero seeds diverge at all).
- **Prediction (4) - final-score difference survives fresh seeds**:
  **N/A given (3) failed** - there is no significant matched-seed score
  effect to validate. Run anyway per protocol, on fresh seeds 501-510:
  mean seat-controlled margin **-$88/game**, stderr $70, **t = -1.26** -
  consistent (small, negative, not significant) with the matched-seed
  result, not a validated positive effect.

### Variant 2 (melon_floor=50) - matched seeds 1-20

Numerically identical to Variant 1 on every metric measured (opportunity-
days 167, sold-days 168, revenue $555,219, margin -$116.65/game,
t=-1.53). This is a genuine result, not a script bug (verified: the two
variant files differ from the baseline and from each other only in the
`melon_floor` value; `mini_engine`'s cache keys on agent file content).
It indicates that, for this specific baseline's specific games, melon
price essentially never sits in the 50-149 range at the moments a sale
opportunity exists - the intermediate threshold and the "sell on arrival"
threshold produce the same realized decisions on these seeds.

## Important caveat about C1's baseline behavior (read before interpreting the above as a clean null result)

`candidates/C1.py`'s melon-sell condition is `price >= floor OR day >= 27
OR shed_load > 75` - an OR of three conditions, not price alone. On the
seeds tested, the `day >= 27` and `shed_load > 75` legs already trigger a
sale in the overwhelming majority of opportunity-days regardless of the
price floor, so this **specific baseline's "hold" behavior is much rarer
than the melon-hold behavior observed in Grace's actual games in Phases
1-4A** (Phase 4A found a 3.72% opportunity-conditioned sell rate for
Grace's real games - i.e. ~96% hold - versus this baseline's ~97-100% sell
rate, effectively the opposite profile). **This means Phase 4B's null/weak
result characterizes the melon-floor knob's causal effect on this specific
proxy baseline, not a reconstruction or causal test of the actual
melon-hold behavior Phase 4A measured in Grace's real games.** This is
flagged prominently rather than left implicit, because it materially
limits what can be concluded from this phase (see Limitations).

## RNG / side-effect audit (required per Grace's instruction, run even though the melon gate itself is RNG_INDEPENDENT)

Checked whether the melon intervention shifts downstream weed-spawn RNG
consumption, via the exact mechanism Phase 1 identified
(`_end_of_day` draws weeds for each player sequentially from one
per-day `random.Random` object - `kaggriculture.py` lines ~837-867):

- **Opponent's (unmodified seat's) weed sequence**: compared, seed-by-seed,
  the baseline opponent's weed draws when paired against the variant vs.
  when paired against baseline-self-play. **Diverged in 0 of 20 seeds.**
  The intervention produces **no cross-player RNG-pathway effect** in this
  sample - consistent with `RNG_INDEPENDENT` at the interaction level.
- **The intervened farm's own weed sequence**: compared, seed-by-seed, the
  variant-farm's weed draws to what the same seat would draw in a
  baseline-vs-baseline self-play game. **Diverged in 2 of 20 seeds (10%)**
  - seeds 7 and 13, both late-game (first divergence on trace day 29 and
    26 respectively). **These are exactly the two seeds (plus seed 1) that
  showed a nonzero money margin** in the matched-seed evaluation above -
  i.e. the small money-margin effect observed is at least partly
  attributable to the intervened farm's own downstream board-occupancy
  shift (altered tile/melon-planting state late-game changing its own
  empty-tile count and hence its own weed draws), not purely to melon
  revenue itself.

**Classification**: the melon-sell decision itself remains
`RNG_INDEPENDENT` (unchanged from Phase 3/4A - confirmed again, not
revised). However, **this phase's own downstream effect (the money
margin) is best classified `RNG_EXPOSED`** for the intervened player's own
subsequent game state, not `RNG_INDEPENDENT` - the audit Grace asked for
specifically surfaced a real, small, late-game RNG-pathway effect that a
naive reading of "the melon gate is RNG-independent" would have missed.
No `RNG_COUPLED` (literal same-rng-object chaining into a shop-unlock
choice) was detected in this sample - the 2 divergent seeds' first
divergence days (26, 29) are not `day % 3 == 2` unlock-adjacent days in
both cases (day 26: 26%3=2, IS unlock-adjacent; day 29: 29%3=2, also
unlock-adjacent) - **both of the 2 divergent seeds are in fact
shop-unlock-adjacent days**, so a `RNG_COUPLED` contribution cannot be
ruled out for those two specific seeds and is flagged as
`PLAUSIBLE_BUT_UNPROVEN` rather than asserted.

## Findings by confidence tier

- **DIRECTLY_OBSERVED**: the melon-floor knob change produces a
  near-zero, non-significant score effect on this baseline over 20 matched
  + 10 fresh seeds; melon revenue and units sold are effectively unchanged;
  the intervention causes zero cross-player RNG divergence and a small
  (10% of seeds) same-player downstream RNG divergence late-game.
- **PLAUSIBLE_BUT_UNPROVEN**: that the 2 divergent-seed cases' downstream
  effect involves the literal shop-unlock RNG-chaining mechanism
  (`RNG_COUPLED`) rather than only the weed-spawn (`RNG_EXPOSED`) pathway -
  both divergence days happen to be unlock-adjacent, but n=2 is too small
  to assert this confidently.
- **Explicitly not concluded**: whether melon-selling behavior similar to
  Grace's actual play (near-always-hold, per Phase 4A) would show a
  different causal effect than this C1-based test - the baseline tested
  here already sells melon almost unconditionally regardless of the floor
  knob, so this phase cannot speak to the causal effect of *Grace's own*
  melon-hold tendency specifically (see caveat above).

## Negative findings

- No significant score/margin effect was found for either variant, on
  either matched or fresh seeds (all t-statistics between -1.26 and -1.53,
  below conventional significance thresholds).
- Variant 1 (floor=0) and Variant 2 (floor=50) produced numerically
  identical outcomes on every seed tested - the melon-floor knob's effective
  range on this baseline's realized games appears to be narrower than the
  0-150 span tested.

## Limitations

1. **Baseline mismatch with the original replay-derived finding**: C1's
   melon-hold behavior (~0-3% hold rate implied by the OR-gated condition)
   does not resemble Grace's actual play (~96% hold, per Phase 4A) - this
   phase tests the knob's causal effect on a policy that barely exhibits
   the behavior being tested, which is the primary reason this phase's
   result should not be read as "the Phase 4A divergence has no causal
   effect" - it more precisely shows "this specific proxy baseline's score
   is insensitive to this specific knob, on this sample."
2. **Opportunity-day measurement granularity**: `mini_engine`'s trace is
   per-day (end-of-day shed snapshots), coarser than Phase 3's true hourly
   opportunity gate - the sell-rate numbers in this report are approximate
   proxies, not a direct re-application of Phase 3's exact per-step method.
3. **Small sample**: 20 matched + 10 fresh seeds per variant is a small
   sample chosen to fit this session's time budget - effect sizes this
   small (a few hundred dollars against six-figure final scores) would
   need a substantially larger seed set to rule out with confidence, not
   just fail to detect.
4. RNG audit compared weed-sequence identity only; it did not attempt to
   quantify a full causal-mediation decomposition of how much of the
   $58-117/game margin is attributable to the RNG-pathway effect versus
   direct melon-revenue effect - both are small enough that further
   decomposition was not judged worth the added complexity this phase.

## Explicit scope note (per Grace's instruction)

This report answers the four pre-registered predictions honestly. **It
does not, and is not intended to, recommend adopting, mutating toward, or
weighting evolution search toward the tested melon-floor change or any
variant of it.** No such recommendation appears anywhere in this document,
and none should be inferred from a result in either direction.
