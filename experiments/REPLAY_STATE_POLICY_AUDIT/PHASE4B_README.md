# Phase 4B: Minimal Causal Intervention Test - reproduction

Follow-on to the Phase 1-4A READMEs in this directory. This phase tests one
isolated policy variant against a baseline copy - it does not touch
`candidates/`, `submissions/`, `evolve/`, or any live champion file.

## Files

- `phase4b_variants/variant0_baseline.py` - unmodified copy of
  `candidates/C1.py`.
- `phase4b_variants/variant1_melon_floor0.py` - single-line diff:
  `KNOBS["melon_floor"]` changed from `150` to `0`.
- `phase4b_variants/variant2_melon_floor50.py` - single-line diff:
  `KNOBS["melon_floor"]` changed from `150` to `50`.
- `phase4b_analyze.py` - runs `mini_engine.run_game` for baseline vs a
  variant, both seat orders, over a given seed list; computes
  opportunity/sold-day counts, melon units/revenue, and a seat-controlled
  (both-seats-summed) money margin with a paired t-statistic.

## Harness reused

`mini_engine.py` (already in this repo, no new harness written) - a
dependency-free reimplementation of the `kaggle_environments` framework
loop around the vendored engine, with built-in `--both-seats` seat-bias
control (same convention as `seeded_h2h.py`'s `--both-seats` flag) and
result caching keyed by agent file content hash. `kaggle_environments`
itself is not installed on this machine (confirmed:
`pip`/`.venv`/`.pylibs` all lack it) - `mini_engine.py` exists specifically
to make evaluation possible without it; use it, not `seeded_h2h.py`, on
this machine.

## Reproducing this phase's exact numbers

```bash
cd ~/mnt/Kaggriculture

# Variant 1, matched seeds 1-20 (both seats = 40 games), ~12s:
python3 experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_analyze.py \
    /tmp/p4b_v1_matched.json v1 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 matched

# Variant 1, fresh seeds 501-510 (both seats = 20 games), ~6s:
python3 experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_analyze.py \
    /tmp/p4b_v1_fresh.json v1 501,502,503,504,505,506,507,508,509,510 fresh

# Variant 2, matched seeds 1-20:
python3 experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_analyze.py \
    /tmp/p4b_v2_matched.json v2 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 matched
```

Each run prints a JSON summary (opportunity/sold-day counts, revenue,
units, seat-controlled margin, stderr, t-statistic) and writes the full
per-game rows plus a weed-sequence audit to the given output path.
Results are deterministic given `mini_engine.py`'s seeded engine and its
`.mini_engine_cache/` (re-running is near-instant once cached).

## RNG / side-effect audit

Run as an ad-hoc script (not a saved file this phase - reproduce with the
snippet below); compares, seed-by-seed, the weed-spawn sequence
(`trace[seat]["weeds"]`, one count per in-game day) between:
1. the intervened farm's own sequence (variant vs baseline opponent) and
   what the same seat draws in a baseline-vs-baseline self-play game
   (checks for a same-player downstream RNG-pathway effect from the
   intervention), and
2. the unmodified opponent's sequence when paired against the variant vs.
   against baseline-self-play (checks for a cross-player RNG-coupling
   effect).

```python
import sys; sys.path.insert(0, ".")
from mini_engine import run_game
BASE = "experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_variants/variant0_baseline.py"
V1 = "experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_variants/variant1_melon_floor0.py"
for seed in range(1, 21):
    r_bb = run_game(BASE, BASE, seed=seed, engine="master", trace=True)
    r_vb = run_game(V1, BASE, seed=seed, engine="master", trace=True)
    seat0_diverges = r_bb["trace"][0]["weeds"] != r_vb["trace"][0]["weeds"]
    seat1_diverges = r_bb["trace"][1]["weeds"] != r_vb["trace"][1]["weeds"]
    print(seed, "seat0(intervened)_diverges=", seat0_diverges, "seat1(opponent)_diverges=", seat1_diverges)
```

Result archived at `artifacts/replay_state_policy_audit/p4b_rng_audit.json`
(from the matched-seed run) - see `REPORT_PHASE4B.md` "RNG / side-effect
audit" for the interpretation.

## Inputs required

`candidates/C1.py` (read-only, copied not modified), `mini_engine.py`,
`vendor/kaggle_environments_engine_master/` (the engine `mini_engine.py`
defaults to, `--engine master`). No network, no `kaggle_environments`
package, no `scipy`/`numpy` required.

## Known limitations (see REPORT_PHASE4B.md "Limitations" for full list)

- C1's melon-hold behavior does not resemble Grace's actual play (near-
  always-sell vs Phase 4A's ~96%-hold) - this phase tests the knob's
  effect on a policy that barely exhibits the behavior Phase 4A measured.
- `mini_engine`'s daily trace is coarser than Phase 3's hourly opportunity
  gate; sell-rate numbers here are approximate proxies.
- Small sample (20 matched + 10 fresh seeds per variant), chosen to fit
  this session's time budget - sufficient to detect a large effect, not
  necessarily a small one.

## Hard constraints confirmed

`candidates/C1.py` was read but never written to. No file under
`candidates/`, `submissions/`, or `evolve/` was modified. Nothing from this
phase was added to `evolve/cascade.py`, mutation weighting, or parent
selection. All new files are under `experiments/REPLAY_STATE_POLICY_AUDIT/`
and `artifacts/replay_state_policy_audit/`.
