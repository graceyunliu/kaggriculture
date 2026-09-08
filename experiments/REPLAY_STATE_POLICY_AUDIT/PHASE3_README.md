# Phase 3: Counterfactual Opportunity Reconstruction - reproduction

Follow-on to `README.md` (Phase 1) and `PHASE2_README.md` (Phase 2) in this
directory. Reuses the replay format and RNG-code knowledge from Phase 1-2.
Same ~175-file replay ballpark as Phase 2 (not scaled up, per instruction).

## What's new this phase

Phase 2 could only see "an action happened." Phase 3 reconstructs, from
engine code, whether an *opportunity* existed at each hourly step for HIRE
and MELON specifically, so abstention (opportunity existed, policy declined)
is now visible - not just action.

Eligibility rules recovered (see `REPORT_PHASE3.md` for full citations):
- **HIRE**: opportunity exists iff `money >= farmHandCostMult *
  fib(hires_today)` (`kaggriculture.py:_hire_cost`/`_do_hire`,
  lines 674-683). No capacity/board gate exists.
- **MELON**: opportunity exists iff `shed.MELON > 0`
  (`kaggriculture.py:_commit_unit`, SELL branch, lines 626-635). Price is
  deterministic, not an eligibility gate.

Both gates are fully deterministic (no RNG draw) - every reconstructed row
is tagged `RNG_INDEPENDENT`, and every row got a definite opportunity tag
(`OBSERVED_ACTION` or `OBSERVED_ABSTENTION`); no
`OPPORTUNITY_UNRECONSTRUCTABLE` rows were produced this run.

## Scripts

1. `mine_phase3.py` - like `mine_phase2.py`, scans every hourly step of
   each replay, but instead of just logging whether HIRE/MELON actions
   occurred, it first computes the eligibility gate above from that step's
   `farm["money"]`, `farm["hires_today"]`, `configuration.farmHandCostMult`
   (for HIRE) or `private.shed.MELON` (for MELON), and only emits a row
   when the gate confirms an opportunity existed - tagged
   `OBSERVED_ACTION` if the corresponding market order appears in that
   step's action, else `OBSERVED_ABSTENTION`.

   ```bash
   cd ~/mnt/Kaggriculture
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py \
       <output.jsonl> <files_per_dir> <start_dir_idx> <end_dir_idx> <w|a>
   ```

   Run in the same 3 chunks used for Phase 2 (5 directories each, ~11s per
   chunk on the target machine):

   ```bash
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py /tmp/phase3_output.jsonl 15 0 5 w
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py /tmp/phase3_output.jsonl 15 5 10 a
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py /tmp/phase3_output.jsonl 15 10 15 a
   ```

   As in Phases 1-2, write output to `/tmp` (not `$HOME`/`/sessions`, which
   was still full at Phase 3 time).

2. `aggregate_phase3.py` - reads the JSONL from `mine_phase3.py`, computes
   per-cohort opportunity-conditioned action rates (both globally and
   per state bucket), and applies the same >=8-observations-per-side +
   >=40%-modal-frequency divergence filter used in Phases 1-2. Every
   finding is tagged `rng_classification` (`RNG_INDEPENDENT` for both
   `hire_opportunity` and `melon_opportunity` this phase, per the
   deterministic-gate reasoning above) and `opportunity_state`.

   ```bash
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/aggregate_phase3.py \
       <input.jsonl from mine_phase3.py> > findings_raw.json 2> stats.txt
   ```

## Reproducing this phase's exact numbers

```bash
cd ~/mnt/Kaggriculture
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py /tmp/phase3_output.jsonl 15 0 5 w
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py /tmp/phase3_output.jsonl 15 5 10 a
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase3.py /tmp/phase3_output.jsonl 15 10 15 a
python3 experiments/REPLAY_STATE_POLICY_AUDIT/aggregate_phase3.py /tmp/phase3_output.jsonl \
    > /tmp/phase3_findings_raw.json 2> /tmp/phase3_stats.txt
cat /tmp/phase3_stats.txt          # opportunity/action/abstention breakdown per decision type
cat /tmp/phase3_findings_raw.json  # per-bucket divergences
```

Deterministic given unchanged `Replays/` contents (`random.Random(42)`
shuffle, identical file selection to Phase 2). The full raw event stream is
archived at `artifacts/replay_state_policy_audit/phase3_mined_events.jsonl`
for re-aggregation without re-scanning replays.

## Inputs required

Same as Phases 1-2: `Replays/Auto/mine/` and `Replays/Auto/leaderboard-*/`
(gitignored, local-machine only). No DB, no network required. Reads
`vendor/kaggle_environments_engine/kaggriculture.py` only as a reference for
the hard-coded eligibility-rule constants reproduced in `mine_phase3.py`
(`_fib`, `hire_cost`) - it is not imported or executed, only cited.

## Known limitations (see REPORT_PHASE3.md "Limitations" for full list)

- HIRE eligibility is checked only for the first hire opportunity per step;
  escalating multi-hire-per-step cost is not modeled.
- MELON action-rate gap is a global, not state-bucketed, finding - too few
  action events (24 total) for per-bucket support in this sample size.
- Population intentionally held at the Phase 1-2 ballpark (~175-265 files),
  not scaled up this phase.
- Fertilizer and chore were NOT re-examined this phase (closed per Phase 2).
