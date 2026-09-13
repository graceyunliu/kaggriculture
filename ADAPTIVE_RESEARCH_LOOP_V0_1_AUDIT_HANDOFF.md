# Audit Handoff -- Adaptive Research Loop v0.1 (2026-09-13)

**Bottom line: infrastructure built and exercised end-to-end (read-only,
no submission). It independently derives H_RATING as the top-priority next
experiment from the existing v0.2-vs-O42 ladder evidence, with H1 (an
already-built, unsubmitted candidate) as a close second. O42's hash was
re-verified unchanged. No candidate was submitted; no certified package was
modified.**

## Directly Observed

- `adaptive/` contained conflict-panel/seed-starvation analysis tooling but
  no research-loop, hypothesis-registry, or experiment-ledger
  functionality prior to this work -- confirmed by listing
  `adaptive/*.py` before writing anything.
- `artifacts/ladder_adaptive_v0.2_diagnostic_2026-09-13/derived/` contains
  four prior-audit documents (`LADDER_ADAPTIVE_V0_2_RAW_EVIDENCE.md`,
  `LADDER_ADAPTIVE_V0_2_AUDIT_HANDOFF.md`, `KAGGLE_SCORE_RECONSTRUCTION.md`,
  `SCORE_DIAGNOSTIC_AUDIT_HANDOFF.md`) -- all read in full and used as the
  sole evidence source for `derive_hypotheses_from_v0_2_evidence()`.
- `candidate/adaptive-v0.3-ladder-candidate/` already existed (built in an
  earlier session), implementing `MIN_N_TO_TRUST_B=10` -- read (README.md,
  provenance_manifest.json), not modified, not submitted.
- `candidates/O42_MAX_HANDS_LATE_EXPAND.py` sha256 =
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813` --
  matches the certified value. Re-checked via
  `candidate_builder.check_o42_immutable()` as part of
  `research_loop.py`'s own run, and independently via `sha256sum` from the
  shell.
- `python3 adaptive/research_loop/research_loop.py`, run from a fresh
  process, produced (deterministically, no randomness in the code):
  hypotheses H_RATING/H1/H2/H3/H5 with the statuses/confidences in the main
  report's table, and selected H_RATING as top experiment (score 9/10,
  tied with H1, won on priority tiebreak).
- `adaptive/research_loop/experiment_ledger.jsonl` contains exactly one row
  after this work: the retrospective v0.2 entry, written once (verified
  idempotent -- re-running `research_loop.py` does not duplicate it, since
  `run_readonly()` checks `el.get(...)` before appending).
- `adaptive/research_loop/hypotheses.json` contains exactly the 5
  hypotheses listed in the report, each with a `source` field citing the
  specific evidence file/observation it was derived from.

## Reconstructed

- The "H_RATING and H1 both score 9/10, H_RATING wins on tiebreak" ranking
  is a direct, mechanical output of `experiment_selector.py`'s stated
  5-factor formula -- reproducible by re-running the script; the choice of
  which five factors to score and their point values is a design decision
  made in this work, documented in the module's own docstring, not derived
  from data.
- The claim that H_RATING is "a prerequisite for correctly interpreting any
  future candidate's result" (main report section 4) is this work's own
  reasoning about the relationship between the two top hypotheses, not a
  quantity read off a file.

## Unavailable / Not Attempted

- This work did NOT run `preflight.py` inside
  `candidate/adaptive-v0.3-ladder-candidate/` (that requires that
  package's Python environment and O42 path configuration, out of scope
  for infrastructure-only work) -- `candidate_builder.lightweight_validation()`
  checks for the script's *existence*, not its live pass/fail, consistent
  with spec step 16 ("don't demand a full independent audit for every tiny
  iteration").
- This work did NOT independently re-derive the controller/learner hashes
  cited in the ledger's v0.2 entry from the certified source files in
  `adaptive/provenance/adaptive-eval-v0.2/` -- they are carried over
  verbatim from the prior audit's `LADDER_ADAPTIVE_V0_2_RAW_EVIDENCE.md`,
  which itself flagged the same re-derivation as not independently
  re-executed. This is an existing open item, not a new gap introduced
  here.
- No new ladder data was pulled. `ladder_ingest.py` reads only the
  evidence already collected on 2026-09-13; it does not call Kaggle's API.
  If Grace wants to test H_RATING per section 5 of the main report, a
  *human* (or `pull_ladder.py`, unchanged, run by a human) needs to pull a
  fresh episode count for submission 56200714 at a later date -- this loop
  does not do that on its own.
- Whether Kaggle's exact rating update formula (precise K-decay function,
  margin-of-victory weighting, TrueSkill-vs-Elo family) is what the prior
  audit already flagged as unresolved -- this work did not attempt to
  resolve it further; H_RATING's claim is about path-dependence/
  convergence shape, which does not require the exact formula.

## Not Yet Established (open questions this work does not answer)

1. Whether Adaptive v0.2's rating actually does converge upward with more
   games (the concrete falsifiable prediction in main report section 5) --
   requires a future ladder pull, not attempted here.
2. Whether `adaptive-v0.3-ladder-candidate` (H1) should be submitted before
   or after that additional v0.2 evidence comes in -- this work's selector
   ranks H_RATING marginally ahead but does not forbid submitting v0.3; that
   remains a human call, consistent with spec step 15.
3. H2 (reward-horizon misalignment) and H3 (regime-partition coarseness)
   have zero supporting or contradicting evidence yet (status NEW,
   confidence NO_EVIDENCE) -- correctly reflected as such, not inflated.

## Files

- `adaptive/research_loop/{experiment_ledger,hypothesis_store,ladder_ingest,diagnostic_engine,experiment_selector,candidate_builder,research_loop}.py`
- `adaptive/research_loop/experiment_ledger.jsonl`
- `adaptive/research_loop/hypotheses.json`
- `adaptive/research_loop/README.md`
- `ADAPTIVE_RESEARCH_LOOP_V0_1_REPORT.md` (repo root, this handoff's companion)
- `ADAPTIVE_RESEARCH_LOOP_V0_1_AUDIT_HANDOFF.md` (repo root, this file)
