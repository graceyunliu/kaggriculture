# Phase 4A: Statistical Confirmation of the Melon-Opportunity Divergence - reproduction

Follow-on to the Phase 1-3 READMEs in this directory. This phase is
melon-opportunity-only, statistical-analysis-only: no new decision types,
no code/policy changes. Replay volume was scaled specifically for melon
opportunities, per Grace's explicit one-time exception to the
no-scale-up rule.

## What's new this phase

- `mine_phase4a.py` - melon-only variant of `mine_phase3.py`'s opportunity
  reconstruction (same `shed.MELON > 0` gate, same `OBSERVED_ACTION`/
  `OBSERVED_ABSTENTION` tagging), but able to pull from either the
  opponent-leaderboard directories (`pool=opp`) or `Replays/Auto/mine/`
  (`pool=mine`) in arbitrary file-range chunks, for large sequential scans.
- `analyze_phase4a.py` - pure-Python statistical analysis (no `scipy`
  available on this machine): Wilson score CIs, an exact two-sided Fisher's
  exact test via log-space hypergeometric summation, rate-ratio and
  odds-ratio effect sizes with delta-method CIs, a cluster bootstrap
  resampling whole replays (not individual events) to account for
  within-replay/within-opponent non-independence, and a per-opponent-
  identity breakdown for identities with >=30 observations.

## Important discovery this phase (read before rerunning)

Scanning `pool=opp` (`Replays/Auto/leaderboard-*/`, `Replays/Leader
Replays/`, 304 files) found **zero** files containing `graceyunliu` in
`info.TeamNames` - these directories contain no games Grace played, so they
contribute nothing to any mine-vs-opp comparison. **The scale-up that
matters is entirely within `Replays/Auto/mine/`** (2,133 files available),
where each replay's other seat is some specific opponent. `mine_phase4a.py`
supports scanning `pool=opp` for completeness/verification, but you do not
need to rerun it - the finding is already recorded in
`REPORT_PHASE4A.md`'s "Negative / methodological finding" section.

## Reproducing this phase's exact numbers

```bash
cd ~/mnt/Kaggriculture

# (Optional, ~45s total across 3 chunks) verify the opponent-directory
# pool contributes zero rows - already confirmed, safe to skip:
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase4a.py /tmp/phase4a_opp.jsonl opp 100 0 w
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase4a.py /tmp/phase4a_opp.jsonl opp 100 100 a
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase4a.py /tmp/phase4a_opp.jsonl opp 104 200 a

# Required: scan 358 files from Replays/Auto/mine/ (seeded shuffle,
# random.Random(42), so this reproduces the same 358-file sample every
# time given unchanged Replays/ contents). ~15s per 120-file chunk.
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase4a.py /tmp/phase4a_mine.jsonl mine 120 0 w
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase4a.py /tmp/phase4a_mine.jsonl mine 120 120 a
python3 experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase4a.py /tmp/phase4a_mine.jsonl mine 120 240 a

# Statistical analysis (runs in well under a second - all the runtime is
# in the mining step above, not the analysis):
python3 experiments/REPLAY_STATE_POLICY_AUDIT/analyze_phase4a.py \
    /tmp/phase4a_mine.jsonl /tmp/phase4a_stats.json
cat /tmp/phase4a_stats.json   # full numeric result, including per-opponent breakdown
```

To scan more than 358 files (further scale-up, if ever re-authorized),
increase the range arguments, e.g.
`python3 mine_phase4a.py /tmp/phase4a_mine.jsonl mine 120 360 a` for the
next 120 files, appending to the same output file, then rerun
`analyze_phase4a.py` on the larger file.

Both scripts write to `/tmp` rather than `$HOME` (`/sessions` mount was
still full at Phase 4A time, as in every prior phase). The archived event
data used for this report's exact numbers is at
`artifacts/replay_state_policy_audit/phase4a_mined_events.jsonl`
(358 files' worth) and the computed statistics at
`artifacts/replay_state_policy_audit/phase4a_stats_full.json`.

## Inputs required

`Replays/Auto/mine/` (gitignored, local-machine only). No DB, no network,
no `scipy`/`numpy` required (pure Python 3 standard library:
`math`, `random`, `json`, `collections`).

## Method notes / how to sanity-check the statistics

- `fisher_exact_two_sided` computes the exact hypergeometric tail
  probability in log-space via `math.lgamma`, summing over all tables at
  least as extreme as observed (standard definition of the two-sided exact
  test) - no `scipy.stats.fisher_exact` dependency.
- `rate_ratio_ci` and `odds_ratio_ci` use standard log-scale delta-method /
  Wald CIs (Haldane-Anscombe 0.5 correction applied to the odds ratio only
  if any cell is zero - not needed in this run's data, all four cells were
  nonzero).
- The cluster bootstrap resamples **whole replay records** (each with its
  own mine-action/mine-abstain/opp-action/opp-abstain counts) with
  replacement, 2000 times, recomputing the pooled rate ratio each time -
  this is the standard "cluster bootstrap" approach for data where the
  natural independent unit (one replay/seed/opponent-pairing) is coarser
  than the raw event count.

## Known limitations (see REPORT_PHASE4A.md "Limitations" for full list)

- "Opportunity" is still the coarse `shed.MELON > 0` gate; price
  favorability at the moment of opportunity is not modeled.
- Per-opponent breakdown restricted to identities with >=30 observations.
- No performance/outcome/causal analysis - out of scope for 4A.
