# Phase 2: Intra-Day Decision-Triggered State Audit - reproduction

Follow-on to `README.md` (Phase 1) in this same directory. Reuses the
replay format and RNG-code knowledge from Phase 1; does not re-scan
`Replays/` beyond the same ~175-265-file ballpark Phase 1 used (Grace's
instruction: fix sampling resolution, not sample size, this phase).

## Scripts

1. `mine_phase2.py` - like Phase 1's `mine.py`, but scans **every hourly
   step** of each replay (not just hour==0) and, per player-slot per step,
   detects five decision-triggered events from the actual `action` payload
   and `private.shed` inventory: HIRE, PLANT (crop chosen), FERTILIZE
   (apply vs hold, given fertilizer stock), MELON (sell vs hold, given
   melon stock), CHORE (idle vs assigned majority of hands). See
   `REPORT_PHASE2.md` "Method" section for exact trigger/decision logic per
   type.

   ```bash
   cd ~/mnt/Kaggriculture
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py \
       <output.jsonl> <files_per_dir> <start_dir_idx> <end_dir_idx> <w|a>
   ```

   The `start_dir_idx`/`end_dir_idx`/mode arguments let you split the run
   across multiple device_bash calls to stay under a ~45s timeout - each
   run appends (`a`) or starts fresh (`w`). Example (as run for this
   audit, 3 calls covering the 15 `REPLAY_DIRS` in 5-directory chunks):

   ```bash
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py /tmp/phase2_output.jsonl 15 0 5 w
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py /tmp/phase2_output.jsonl 15 5 10 a
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py /tmp/phase2_output.jsonl 15 10 15 a
   ```

   Each chunk (5 dirs x up to 15 files/dir, all hourly steps) ran in
   ~9 seconds on the target machine - well under the timeout, because only
   action-payload/shed-inventory checks are done per step (no full
   100-tile board scan), unlike Phase 1's `mine.py` which does scan the
   full board once per (daily) sample point.

   As in Phase 1, write output somewhere with free disk space - `$HOME`
   (`/sessions` mount) was still full at Phase 2 time; `/tmp` was used
   again.

2. `aggregate_phase2.py` - reads the JSONL from `mine_phase2.py`, pools
   events by `decision_type`, bins by the Level-A state signature
   `(day, cash_bucket, land_tier, labor_bucket)`, and applies the same
   >=8-observations-per-side + >=40%-modal-frequency-per-side divergence
   filter Phase 1 used. Assigns `rng_classification` using the new 4-value
   taxonomy (`RNG_INDEPENDENT / RNG_EXPOSED / RNG_COUPLED / UNKNOWN`) per
   the `rng_class()` function - see `REPORT_PHASE2.md` "RNG classification"
   section for the exact rule.

   ```bash
   python3 experiments/REPLAY_STATE_POLICY_AUDIT/aggregate_phase2.py \
       <input.jsonl from mine_phase2.py> > findings_raw.json 2> stats.txt
   ```

## Reproducing this phase's exact numbers

```bash
cd ~/mnt/Kaggriculture
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py /tmp/phase2_output.jsonl 15 0 5 w
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py /tmp/phase2_output.jsonl 15 5 10 a
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py /tmp/phase2_output.jsonl 15 10 15 a
python3 experiments/REPLAY_STATE_POLICY_AUDIT/aggregate_phase2.py /tmp/phase2_output.jsonl \
    > /tmp/phase2_findings_raw.json 2> /tmp/phase2_stats.txt
cat /tmp/phase2_stats.txt        # event counts per decision type + findings-by-class summary
cat /tmp/phase2_findings_raw.json
```

Deterministic given unchanged `Replays/` contents (`random.Random(42)`
shuffle, same as Phase 1). The full raw event stream (175 files' worth) is
also archived at
`artifacts/replay_state_policy_audit/phase2_mined_events.jsonl` for
re-aggregation without re-scanning replays.

## Inputs required

Same as Phase 1: `Replays/Auto/mine/` and `Replays/Auto/leaderboard-*/`
(gitignored, local-machine only). No DB, no network required.

## Known limitations (see REPORT_PHASE2.md "Limitations" for full list)

- HIRE and MELON are logged only at actual-action/stock-present moments,
  not against a reconstructed opportunity/eligibility baseline - true
  decision-vs-abstain tests need a hire-price and market price-window model
  not built this phase.
- FERTILIZER/MELON stock > 0 is a coarse eligibility proxy, not verified
  per-tile/per-lot eligibility.
- CHORE checks only whether a hand's action list was empty that hour, not
  chore quality or type.
- Population held at 175 files / ~15 directories, intentionally not scaled
  up this phase.
