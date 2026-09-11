# Evaluation plateau diagnosis — September 11, 2026

## Finding

The multi-week ladder plateau is better explained by an evaluation and search-design ceiling than by one missing game mechanic.

The overnight evidence is a severe dev-to-held-out generalization failure: 129 candidates reached the held-out stage and only one passed. Candidates selected on seeds 1–10 can show roughly +$4k to +$7k dev margins and then fall to negative or near-zero results on seeds 11–30 against the same opponent. A single dev margin threshold (`margin >= $1,500`, `t >= 2`) is therefore not a reliable promotion signal by itself.

## Important current-checkout correction

The claim that the loop evaluates only a frontier plus `opp_scenario_v14` describes an older configuration, not the current September 11 checkout.

`evolve/loop.py` now defaults to a panel of four real ladder-loss tapes (`peterparker`, `alaylm`, `bahaenes`, and `yangkuang2`). `evolve/cascade.py` evaluates that panel on both dev seeds 1–10 and held-out seeds 11–30. A held-out pass now requires all of:

- positive, significant head-to-head held-out performance against the frontier (`t >= 2`);
- no loss in mean panel margin relative to the frontier;
- no loss in the candidate's own mean money on the panel.

This is a material improvement over the frozen-tape-plus-clone design. It does not fully solve the problem: the dev promotion decision is still made from one frontier matchup on one 10-seed set, and the held-out stage is seed-held-out rather than opponent-population-held-out. The four tapes are also a fixed historical sample, not the current ladder distribution.

## Search-space ceiling

The main evolutionary line still searches numeric and categorical controls on a largely frozen heuristic dispatcher (`candidates/K.py` / `candidates/K_SELFMODEL.py`). This is effective for factual corrections and local policy calibration, but it cannot establish that the architecture class can match bots using materially different planning, look-ahead, opponent modeling, or state-adaptive openings.

The earlier planner failures should be treated as failures of those implementations and gates, not as proof that planning is permanently closed. `docs/planner-results.md` already shows that executor improvements became real while the remaining deficit moved upstream into allocation, hiring, and market timing. That is evidence for revisiting structural planning hypotheses with narrower invariants, not for resuming undirected knob search.

## Required changes before further knob search

1. Replace one-shot dev promotion with repeated disjoint seed blocks. A candidate should reach held-out only after its direction is consistent across multiple preregistered blocks, with aggregate uncertainty reported. Do not promote from one favorable 10-seed estimate.
2. Separate selection, confirmation, and population tests. Keep the four-tape panel, but reserve at least one materially different opponent panel that is never used for ranking or proposal feedback. Include weak, aggressive, alternate-opening, and reactive opponents where available.
3. Treat current ladder episodes as the external validity test. Use `pull_ladder.py` when egress is available to report non-mirror win rate, opponent fingerprints, rating trajectory, and uncertainty versus game count. This distinguishes rating convergence/episode-volume effects from true matchup weakness.
4. Pause broad knob mutation until the revised evaluation can reject seed-fit and opponent-fit cheaply. Use the saved compute for narrow structural experiments, including a planner revisit with explicit reliability and allocation invariants.

## Interpretation rule

Local margin against the frontier is a matchup statistic, not a ladder-performance estimate. A candidate is promising only when its improvement is directionally stable across disjoint seeds, preserves performance across a diverse opponent panel, and is consistent with real ladder episodes. Until those three conditions agree, report it as exploratory rather than as a promotion candidate.
