# Phase 7: melon-sell-threshold candidate (verified-baseline retest)

**Verdict: NO_ROBUST_SIGNAL.** The intervention changed melon-sell
behavior exactly as intended (42.6% -> 100.0% of opportunities), but
produced no consistent score effect across fresh seeds and opponent
cohorts. Not promoted anywhere. Diagnostic only.

## Executive summary

Phase 4A found a large, statistically massive melon-hold divergence
(rate ratio 3.13, p=7.1e-169) between the champion's seat and paired
opponents in real play. Phase 4B tested this causally but used C1 as a
baseline proxy, which already sells melon near-unconditionally --
unrepresentative of the actual ~0.63%-opportunity-conditioned real-play
hold pattern -- and came back NO_ROBUST_SIGNAL. Because that null result
rode on an unverified baseline, the coordinator asked for a retest using
the same baseline-verification discipline Phase 6 established for land
expansion.

**Step 1, baseline verification:** measured `candidates/V3_15.py`'s (the
current champion, confirmed in Phase 6) own melon-sell rate via
`mini_engine.run_game` against real opponent tapes. It sells 42.6% of
melon opportunities in a 5-seed sample (54 opportunity-days, 23 sell-days)
against one opponent, and 43-58% hold rate range across the opponent
samples checked -- **far from Phase 4A's historical 0.63% figure**, the
same "current chassis vs. historical mixture corpus" gap Phase 6 found
for land expansion. Per the coordinator's explicit guidance for this
situation, Phase 4A's historical figure was **not** used as the reference;
the current champion's own measured ~43-54% sell rate was used instead as
the real baseline behavior to test an intervention against.

**Step 2, variant:** `variant_melon_aggressive.py` — byte-for-byte
identical to a plain copy of `candidates/V3_15.py`
(`baseline_V3_15.py`), except `MELON_SELL_PRICE: 150 -> 1` (near-
unconditional sell), using the real decision point already found and
cited in earlier phases:

```python
n = shed.get("MELON", 0)
if n > 0 and (prices.get("MELON", 0) >= MELON_SELL_PRICE or day >= 27 or shed_load > 75):
    orders.append(["SELL", "MELON", int(n)])
```
(`candidates/V3_15.py:332`, identical logic in `V3_12.py:305`)

**Step 3, pre-registered predictions, checked separately:**

| # | Prediction | Result |
|---|---|---|
| 1 | Melon-sell rate conditional on opportunity increases substantially | **CONFIRMED** — 42.6% -> 100.0% (same 5 seeds) |
| 2 | Realized melon revenue changes in the expected direction | Not separately isolated; folded into the score comparison (#4) |
| 3 | Downstream cash/inventory consequence measurable | Partially observed — opportunity-day counts drop (54 -> 23) exactly as expected when melon is cleared immediately rather than held across days; not further decomposed into a cash-timing metric |
| 4 | Score effect survives fresh seeds | **FAILED** — see below |

**Step 4/5, matched-then-fresh-seed evaluation** (`mini_engine.run_game`,
both seats, paired per-seed comparison):

- Matched seeds 1-20 vs. `tape_mtn`: mean diff (variant - baseline)
  **-$1,133/game**, t = -1.51 (not significant, n=40 seat-games; negative
  direction — variant slightly *worse*).
- Fresh seeds 101-120, 3 different opponent tapes:
  - `tape_mtn`: mean diff -$754/game, t = -0.96 (negative, not significant)
  - `tape_kwa`: mean diff +$16/game, t = 0.20 (~zero)
  - `tape_furina`: mean diff +$2,354/game, t = 2.42 (positive, only
    marginally significant at n=40)

No consistent sign or robust significance across the four independent
checks (1 matched + 3 fresh/cross-opponent). This is the textbook failure
mode prediction 4 exists to catch: the manipulation clearly worked
(prediction 1), but the score consequence does not survive fresh-seed,
cross-opponent scrutiny.

**Step 5 continued, RNG/side-effect audit:** the gate itself remains
RNG_INDEPENDENT (unchanged finding from Phase 3/4A — only
`shed.MELON>0`/price/day/shed-load, all deterministic). `SELL` at
price > 1 increments market inventory deterministically
(`kaggriculture.py`'s `_commit_unit`) and does not touch the day's RNG
stream (`_spawn_weeds`/shop-unlock selection). No RNG-path contamination
identified from this single-line change.

## Conclusion

With a properly verified baseline (the current champion's own measured
melon-sell behavior, not C1's unrepresentative near-unconditional
selling), the melon-sell-threshold intervention **still** returns
NO_ROBUST_SIGNAL on score. Rather than reopening Phase 4B's conclusion,
this **strengthens** it: the earlier null result was not an artifact of
using the wrong baseline. Melon-sell timing, across two independently
chosen baselines, does not show a robust causal effect on final score
within the ranges tested here.

## What was NOT done, per the instructions

No further variants were built chasing a positive result (the marginal
`tape_furina` signal, alone and unreplicated elsewhere, does not meet the
bar for further pursuit without cherry-picking). No promotion of any kind:
`variant_melon_aggressive.py` and `baseline_V3_15.py` are experiment-only
copies under `experiments/`, not champion, submission, `evolve/cascade.py`,
or parent-selection files. No adoption recommendation.
