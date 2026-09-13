STATUS: READY_FOR_RAPID_ADAPTIVE_ITERATION

FIRST INDEPENDENTLY SELECTED HYPOTHESIS: H_RATING -- the 895.9-vs-1174.0
public-score gap between Adaptive v0.2 and O42 is substantially explained by
Kaggle's sequential, path-dependent rating mechanism (fewer games played,
plus one early loss while the per-game rating step was still large), not by
Adaptive v0.2 playing worse than O42 -- because raw per-game win rate
(48.8% vs 50.7%) and mean money margin (+$3,367 vs +$1,929, nominally
favoring Adaptive v0.2) are close to parity. This is derived from evidence
already in the repo (`artifacts/ladder_adaptive_v0.2_diagnostic_2026-09-13/`),
not asserted by a human.

# Adaptive Research Loop v0.1

## 1. What this is

A lightweight, deterministic (no ML, no opaque optimizer) infrastructure
layer at `adaptive/research_loop/` implementing the loop:

    candidate -> ladder submission -> ladder result -> diagnosis ->
    hypotheses -> evidence update -> next-experiment selection ->
    ONE controlled candidate change -> next candidate -> repeat

It exists because the architectural gap in the project was: the gameplay
learner adapts to game states, but a human was the meta-learner deciding
what to try next after each ladder result. This loop makes the research
*process* -- not the gameplay policy -- adaptive.

It optimizes for validated learning per unit time (Speed Principle): it
does not demand statistical certainty before proposing the next step, and
it explicitly refuses to manufacture matched comparisons the data does not
support (no shared opponents/seeds exist between Adaptive v0.2's and O42's
ladder games -- this is stated, not papered over).

## 2. What was inspected before building anything (spec step 1)

- `adaptive/` top level: existing conflict-panel/seed-starvation analysis
  scripts (`analyze_conflict_panel.py`, `analyze_seed_starvation.py`,
  `capital_conflict.py`, `parity_check.py`, `run_conflict_panel.py`,
  `summarize_conflicts.py`). None of these implement a research loop, a
  hypothesis registry, or an experiment ledger -- no functionality
  duplicated.
- `artifacts/ladder_adaptive_v0.2_diagnostic_2026-09-13/{raw,derived}/`: the
  full prior ladder-diagnostic audit (raw Kaggle pulls, per-game CSVs,
  `LADDER_ADAPTIVE_V0_2_RAW_EVIDENCE.md`, `LADDER_ADAPTIVE_V0_2_AUDIT_HANDOFF.md`,
  `KAGGLE_SCORE_RECONSTRUCTION.md`, `SCORE_DIAGNOSTIC_AUDIT_HANDOFF.md`) --
  read in full; this is the evidence base the research loop's first
  hypotheses are derived from (spec step 19).
- `candidate/adaptive-v0.2-ladder-candidate/` (certified, submitted) and
  `candidate/adaptive-v0.3-ladder-candidate/` (already built in an earlier
  session, NOT yet submitted to the ladder, implementing a
  `MIN_N_TO_TRUST_B=10` guard -- see `ADAPTIVE_V0_3_FAST_ITERATION_REPORT.md`
  at repo root): inspected, not modified. v0.3's own provenance manifest was
  read to confirm its change is minimal (one guard) and isolable (flips 3 of
  7 regimes from B to A).
- `candidates/O42_MAX_HANDS_LATE_EXPAND.py`: hash re-verified against the
  certified value before and after this work (see section 5).

Neither the certified v0.2 candidate, the pre-existing v0.3 candidate, nor
O42 was modified while building this infrastructure.

## 3. What was built

`adaptive/research_loop/` (see its own `README.md` for a per-file table):

- `experiment_ledger.py` + `experiment_ledger.jsonl` -- append-only
  candidate/experiment provenance record. A later ladder result is written
  as a new `row_kind=result_update` line, never an in-place edit;
  `effective_rows()` folds a candidate's rows together at read time.
- `hypothesis_store.py` + `hypotheses.json` -- persistent hypothesis
  registry. Confidence is qualitative (`NO_EVIDENCE`/`WEAK`/`MODERATE`/
  `STRONG`), each level's meaning fixed in code (see the module docstring),
  not a per-hypothesis judgment call -- avoiding fake numerical confidence.
- `ladder_ingest.py` -- reads the existing diagnostic evidence (does not
  re-pull Kaggle or recompute statistics `pull_ladder.py`/the prior audit
  already produced) into the shape the rest of the loop consumes, with a
  hash manifest of the source files it read.
- `diagnostic_engine.py` -- `derive_hypotheses_from_v0_2_evidence()`
  generates hypotheses from the evidence (see section 4); also answers
  what-changed / what-happened / was-the-prediction-supported for any
  ledger entry.
- `experiment_selector.py` -- simple 5-factor heuristic (information value,
  cost, isolability, untested-ness, avoids-local-optimum; each 0-2, summed
  to a score out of 10) ranking which hypothesis to test next. Not a
  Bayesian optimizer; explicitly not tuned to reproduce a target answer.
- `candidate_builder.py` -- turns a selected hypothesis into a candidate
  PLAN (proposed next version name via the repo's existing
  `adaptive-vX.Y-ladder-candidate` convention, parent, one change,
  prediction, what would support/weaken it) and a lightweight validation
  checklist (spec step 16: candidate/parent exist, one hypothesis recorded,
  changed files known, hashes recorded, O42 hash matches, preflight script
  present -- not a full independent audit). Writes no controller code.
- `research_loop.py` -- orchestrates phases 1-6 read-only, prints the
  proposal, and stops at the human SUBMIT gate (spec step 15). Running it
  is idempotent: re-running seeds/re-writes `hypotheses.json` to the same
  derived content and will not duplicate the v0.2 ledger entry.

## 4. Hypotheses independently derived from existing v0.2 evidence (spec step 19)

Running `python3 adaptive/research_loop/research_loop.py` from a fresh
invocation, with no human-supplied hypothesis, produces (abbreviated; full
text and evidence citations in `hypotheses.json`):

| ID | Statement (short) | Status | Confidence | Selector score |
|---|---|---|---|---|
| **H_RATING** | Score gap is a rating path-dependence/convergence artifact, not a performance gap (raw margin/win-rate near parity) | ACTIVE | WEAK | **9/10 (selected)** |
| H1 | Frozen selector is greedy on thin-support B arms in some regimes (already has an unsubmitted v0.3 candidate testing it) | ACTIVE | WEAK | 9/10 |
| H2 | 24-turn reward window may not track final-game outcome | NEW | NO_EVIDENCE | 8/10 |
| H5 | Ladder opponent distribution differs from the 4-opponent offline study distribution | ACTIVE | WEAK | 8/10 |
| H3 | 7-cell regime partition may be too coarse, diluting real effects into noise | NEW | NO_EVIDENCE | 7/10 |

H_RATING and H1 tie on raw score; H_RATING wins the priority tiebreak
because it is the more novel, higher-information finding (it resolves *why*
Grace's original question -- "the score seems substantially below O42" --
looks the way it does) and, critically, it is a **prerequisite for
correctly interpreting any future candidate's ladder result**: if H_RATING
is not accounted for, a v0.3 (or later) submission's early, less-converged
rating could be misread as a real regression relative to v0.2's
now-more-converged rating, when it might just be the same convergence
artifact recurring. `candidate_builder.py`'s H1 plan explicitly flags this
confound.

H1 is not dismissed -- it already has a built, unsubmitted candidate
(`adaptive-v0.3-ladder-candidate`) from a prior session, and remains a live,
reasonable thing to submit. The two are not mutually exclusive: H_RATING is
about how to *read* a score change; H1 is about whether to *make* one.

## 5. Proposed next experiment, concretely (spec step 19's "arrives at a
   defensible next hypothesis ... without a human saying 'be more
   conservative'")

Per `candidate_builder.plan_for_hypothesis("H_RATING", ...)`:

- **No new code, no new candidate directory.** H_RATING is a claim about
  the scoring mechanism, not the policy, so it cannot be tested by a code
  change.
- **Action:** continue accumulating real-opponent games on the
  already-submitted, unchanged Adaptive v0.2 (sub 56200714), then re-run
  `ladder_ingest.py` + `diagnostic_engine.py` on a fresh pull.
- **What would support H_RATING:** the rating trajectory climbs out of the
  ~840-980 band and settles into a tighter plateau over the next ~20-30
  real games, the way O42's did by ~game 15 -- without any code change.
- **What would weaken H_RATING:** the rating stays depressed or keeps
  falling despite a comparable number of additional games -- at that point
  H1 (or H2/H3) becomes the relatively more attractive next test, and
  `adaptive-v0.3-ladder-candidate` (already built) is a ready, minimal,
  isolable candidate change to submit for it.
- This prediction is recorded (this document + `hypotheses.json`) **before**
  any further ladder result is observed, so a later evaluation cannot be
  post-hoc-storied.

No candidate change is submitted by this work. This is intentional (spec
step 18: do not modify Adaptive v0.2 as the first task; spec step 15: human
remains the submission gate for anything that would go to the live ladder).

## 6. Three layers of learning, kept separate

1. **Gameplay learner** (existing, untouched): `adaptive_slice_v0.py`'s
   frozen A/B controller, game state -> arm choice.
2. **Research learner** (new, this project): `hypothesis_store.py` +
   `diagnostic_engine.py` -- experiment evidence -> which explanations are
   promising.
3. **Candidate lineage** (new, this project): `experiment_ledger.py` --
   parent -> change -> result, so a future invocation does not silently
   forget that H1 already has a v0.3 candidate built, or rediscover H_RATING
   from scratch.

## 7. Failure memory / avoiding local-optimum traps

The experiment selector's `avoids_local_optimum` factor penalizes
re-selecting whichever hypothesis produced the most recent *accepted*
change (spec step 13) -- there is no accepted change yet (v0.2 is the only
ledger entry with a completed ladder result, and it predates this loop), so
this factor is currently neutral (full credit to all hypotheses) but will
engage from the next iteration onward. `hypotheses.json` is the durable
record that prevents a future invocation from independently "rediscovering"
H1 and treating a MIN_N_TO_TRUST_B-style fix as a fresh idea rather than an
already-scoped, already-built, not-yet-submitted candidate.

## 8. Validation performed on this infrastructure itself

- `research_loop.py` was run end-to-end (`python3 adaptive/research_loop/research_loop.py`)
  and produces the proposal in section 5 deterministically.
- `candidate_builder.check_o42_immutable()` re-verified
  `candidates/O42_MAX_HANDS_LATE_EXPAND.py` sha256 =
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813` --
  MATCHES the certified value, both before and after this work.
- `candidate/adaptive-v0.2-ladder-candidate/` and
  `candidate/adaptive-v0.3-ladder-candidate/` file listings and
  `provenance_manifest.json` contents were read but not written to by any
  file this project added.
- No `git add`/commit in this project touches any file under
  `candidate/adaptive-v0.2-ladder-candidate/`, `candidates/`, or the
  `artifacts/ladder_adaptive_v0.2_diagnostic_2026-09-13/` evidence tree.

See `ADAPTIVE_RESEARCH_LOOP_V0_1_AUDIT_HANDOFF.md` for the directly-observed
/ reconstructed / unavailable breakdown of this work, in the format the
project's other audits use.
