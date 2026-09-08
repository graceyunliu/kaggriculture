# Replay State-Conditioned Policy Audit - reproduction instructions

This directory holds the exact scripts used to produce
`artifacts/replay_state_policy_audit/REPORT.md`,
`artifacts/replay_state_policy_audit/FINDINGS.json`, and
`artifacts/replay_state_policy_audit/sample_mined_records.jsonl`.

Read-only w.r.t. the rest of the repo: these scripts only read files under
`Replays/` and write to paths you pass on the command line. They do not
modify champions, submissions, `evolve/cascade.py`, parent selection, or any
existing repo file.

## Scripts

1. `mine.py` - walks a fixed list of replay directories (see `REPLAY_DIRS`
   at the top of the file), samples up to N files per directory
   (seeded shuffle, `random.Random(42)`, so re-runs with the same N are
   deterministic), parses each replay JSON, and for every hour==0 (i.e.
   once per in-game day) snapshot in each game, emits a per-player record
   with: canonical Level-A state signature (`day_bucket, cash_bucket,
   land_tier, labor_bucket`), cohort label (`mine` / `opp` / `unk`,
   determined by whether `info.TeamNames` contains a name in
   `{graceyunliu, grace, Grace}`), dominant planted crop, wheat fraction of
   planted tiles, `hires_today`, `money`, `day`, `seed`, and source path.
   Output is one JSON object per input file (containing that game's full
   list of sampled records), written as JSON Lines.

   ```
   python3 mine.py <output.jsonl> <files_per_directory>
   # example used for this audit:
   python3 mine.py /tmp/mining_output.jsonl 30
   ```

   Notes:
   - Run this from the repo root (`cd ~/mnt/Kaggriculture && python3
     experiments/REPLAY_STATE_POLICY_AUDIT/mine.py ...`) since `ROOT` is
     computed as `~/mnt/Kaggriculture`.
   - Write the output file somewhere with free disk space. On this
     machine, `$HOME` (the `/sessions` mount) was found to be 100% full at
     audit time - use `/tmp` (a different, larger mount) instead, as done
     here.
   - `sample_every_hours=24` in `process_file()` controls sampling density;
     lower it (e.g. to 1) for full-resolution mining at the cost of ~24x
     more records and runtime. Given the ~45s-per-shell-call constraint
     this session operated under, large full-resolution runs should be
     split into multiple invocations over disjoint file lists, or run with
     output redirected to a log and checked in a follow-up call.

2. `aggregate.py` - reads the JSONL from `mine.py`, bins observations by
   the Level-A state signature, and for every state bucket with >= 8
   "mine" and >= 8 "opp" observations, checks whether the modal
   (most-common) dominant-crop action differs between cohorts with each
   side's mode carrying >= 40% within-bucket frequency. Emits the
   surviving divergences as JSON to stdout, plus summary stats (global
   wheat_frac and hires_today averages per cohort) to stderr.

   ```
   python3 aggregate.py <input.jsonl produced by mine.py> > findings_raw.json 2> stats.txt
   ```

## Reproducing this audit's exact numbers

```bash
cd ~/mnt/Kaggriculture
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine.py /tmp/mining_output.jsonl 30
python3 experiments/REPLAY_STATE_POLICY_AUDIT/aggregate.py /tmp/mining_output.jsonl \
    > /tmp/findings_raw.json 2> /tmp/findings_stats.txt
cat /tmp/findings_stats.txt   # global wheat_frac / hires_today numbers + divergence count
cat /tmp/findings_raw.json    # the 6 divergence buckets reported in REPORT.md
```

Because `mine.py` samples deterministically (`random.Random(42)`), running
with the same `files_per_directory` argument (30) against the same
`Replays/` contents will reproduce the same 265-file sample and the same
divergence buckets. Results will differ if replay directories have gained
or lost files since this audit (Sep 8 2026), or if `files_per_directory`
is changed.

## Inputs required

- The repo's `Replays/Auto/mine/` and `Replays/Auto/leaderboard-*/`
  directories (gitignored, local-machine only - not present in a fresh
  clone; must be synced via whatever process populates `Replays/`, e.g.
  `sync_replays.py`, before these scripts can run).
- No DB access, no network access, no other repo files are required.

## Known limitations of this pass (see REPORT.md "Limitations" for full list)

- Sampled 265 of 2478 available replay files, one snapshot/day (not
  hourly).
- Level B (operational) state - weed/idle-labor/harvestable counts - was not
  mined; only Level A state was used for divergence mining.
- `hires_today` sampling is confounded by an end-of-day reset in the engine
  (see `vendor/kaggle_environments_engine/kaggriculture.py`,
  `_end_of_day`), so no hiring-decision divergence could be tested with the
  hour==0-only sampling used here.
- No Phase 6 counterfactual/replay-intervention testing was performed - the
  repo has no infrastructure to resume simulation from a saved mid-game
  state with a single action substituted.

## Extending this audit

To mine Level B state (per the REPORT's "Recommended next experiments" #1),
add fields to the per-record dict in `mine.py`'s `process_file()`:
count of `None` tiles not `"LOCKED"` (empty), count of idle hands (hands
with an empty action queue), and shed contents for harvestable inventory -
all already present in each `farm` dict, no new data source needed.
