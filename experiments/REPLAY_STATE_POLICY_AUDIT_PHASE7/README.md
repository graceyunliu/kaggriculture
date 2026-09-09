# Phase 7: melon-sell-threshold candidate (retest of Phase 4B with a verified baseline)

Phase 4B tested the melon-hold divergence against C1 as a baseline proxy,
which already sells melon near-unconditionally (nothing like the ~0.63%
opportunity-conditioned real-play rate Phase 4A measured) -- the same
mistake-class Phase 6 caught on land-expansion. This phase retests with a
verified baseline.

## Step 1: baseline verification (same check as Phase 6)

`verify_baseline.py` runs `candidates/V3_15.py` (current champion, per
Phase 6) via `mini_engine.run_game` against real opponent tapes and
computes its own melon opportunity-conditioned sell rate. Result: **~43-54%**
(varies by opponent sample), nowhere near Phase 4A's historical ~0.63%
figure -- the same "current chassis vs. historical mixture corpus" gap
Phase 6 found for land-expansion. Per the coordinator's instruction, this
phase does NOT treat Phase 4A's 0.63% as still-applicable; instead it uses
the CURRENT champion's own measured hold rate (~43-58% hold, i.e. sells
42-54% of opportunities) as the real reference point for testing whether
an intervention moves the needle.

## Variant

`variant_melon_aggressive.py`: byte-for-byte identical to
`baseline_V3_15.py` (a plain copy of `candidates/V3_15.py`) except
`MELON_SELL_PRICE = 150` -> `MELON_SELL_PRICE = 1` (near-unconditional
sell), using the real decision point already found and cited in earlier
phases (`shed.get("MELON", 0) > 0 and (prices.get("MELON",0) >=
MELON_SELL_PRICE or day >= 27 or shed_load > 75)`, `candidates/V3_15.py`
line 332 / `candidates/V3_12.py` line 305, identical in both).

## Scripts

- `verify_baseline.py`: melon opportunity/action rate check.
- `eval_phase7.py`: matched-seed and fresh-seed paired evaluation
  (`mini_engine.run_game`, both seats) across 3 opponent tapes.
