#!/usr/bin/env python3
"""
research_loop.py -- Adaptive Research Loop v0.1, orchestrator.

Implements the 8-phase speed-budgeted iteration (spec requirement 17):

  Phase 1  read evidence             -> ladder_ingest
  Phase 2  generate/update hypotheses -> diagnostic_engine.derive_hypotheses_from_v0_2_evidence
  Phase 3  select ONE experiment     -> experiment_selector.select_next_experiment
  Phase 4  make smallest change      -> candidate_builder.plan_for_hypothesis (PLAN only)
  Phase 5  lightweight validation    -> candidate_builder.lightweight_validation
  Phase 6  prepare ladder submission -> printed here; requires human SUBMIT (loop STOPS here)
  Phase 7  ingest result             -> (run again after a human submits + pulls new evidence)
  Phase 8  update hypotheses         -> hypothesis_store.record_evidence + diagnostic_engine

Run with no arguments to execute phases 1-6 read-only and print the
resulting proposal (what a fresh invocation independently arrives at).
This script never submits anything to Kaggle and never modifies O42,
adaptive-v0.2-ladder-candidate, or adaptive-v0.3-ladder-candidate.
"""
from __future__ import annotations

import json
import sys

import diagnostic_engine
import experiment_selector
import candidate_builder
import experiment_ledger as el
import hypothesis_store as hs
import ladder_ingest


V0_2_LEDGER_ENTRY = {
    "candidate_id": "adaptive-v0.2-ladder-submission-v2",
    "parent_candidate": "adaptive-v0.2-ladder-candidate",
    "commit": None,
    "submission_id": "56200714",
    "submission_timestamp": "2026-09-13T06:16:28.61Z",
    "hypothesis_id": "certified_v0_2_mechanism_generalization",
    "hypothesis": (
        "Adaptive v0.2's frozen A/B controller (choosing between "
        "A_FULL_O42 and B_ONE_PER_ORDER per regime) generalizes offline "
        "mechanism gains to live-ladder play."
    ),
    "rationale": "Offline certified study showed nominal (not statistically established) gains.",
    "predicted_effect": "Positive or neutral live performance vs O42; not decisively established offline (CIs straddled zero).",
    "change_description": "N/A -- this ledger entry is retrospective, recording the already-submitted v0.2 for lineage; the research loop did not create it.",
    "changed_files": [],
    "controller_hash": "9ff99b50656c1ed19b4410d773a83946082bb6f88d605020615dcb3c8e735687",
    "learner_hash": "d8864c049b78da94329a9cb10184acec31582bff7c2afb062400af2c42173c64",
    "o42_hash": "154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813",
    "preflight_status": "documented as fail-closed hash-gated; not independently re-executed by this loop",
    "ladder_result": "complete",
    "score": 895.9,
    "wins": 20,
    "losses": 21,
    "draws": 0,
    "games": 41,
    "opponents": "41 distinct real opponents (by submission ID), zero overlap with O42's opponent set",
    "observations": (
        "Raw win rate/margin close to O42's (48.8% vs 50.7%; mean margin "
        "+3,367 vs +1,929, nominally favoring v0.2). Public score gap "
        "(895.9 vs 1174.0) traced to sequential rating path-dependence, "
        "not raw performance -- see KAGGLE_SCORE_RECONSTRUCTION.md."
    ),
    "diagnosis": (
        "Score gap is PARTIALLY EXPLAINED by rating mechanism "
        "(path-dependence + fewer games + one early loss during high-K "
        "period). Not explained: whether the raw near-parity in "
        "margin/win-rate hides a real (if modest) policy weakness that a "
        "larger sample or matched pairing would reveal."
    ),
    "hypothesis_update": (
        "Generated H_RATING, H1, H2, H3, H5 (see hypotheses.json) from this "
        "single evidence set. H_RATING and H1 are ACTIVE with WEAK "
        "confidence; H2/H3 are NEW/untested; H5 is ACTIVE/WEAK and partially "
        "undercut by the near-parity raw margin."
    ),
    "decision": "Do not resubmit v0.2 unchanged; do not conclude v0.2 'lost' to O42 on performance grounds from this evidence alone.",
}


def run_readonly() -> dict:
    evidence = ladder_ingest.load_v0_2_ladder_summary()

    if el.get(V0_2_LEDGER_ENTRY["candidate_id"]) is None:
        el.append_entry(V0_2_LEDGER_ENTRY)

    diagnostic_engine.seed_hypothesis_store()

    selection = experiment_selector.select_next_experiment()

    hyp = selection["hypothesis"]
    plan = candidate_builder.plan_for_hypothesis(hyp["hypothesis_id"], hyp["statement"])

    proposal = {
        "phase1_evidence_summary": {
            "adaptive_v0.2_score": evidence["candidates"]["adaptive_v0.2"]["public_score"],
            "o42_score": evidence["candidates"]["o42"]["public_score"],
            "score_mechanism": evidence["score_mechanism"],
        },
        "phase2_hypotheses": [
            {"id": h["hypothesis_id"], "status": h["status"], "confidence": h["confidence"]}
            for h in hs.all_hypotheses()
        ],
        "phase3_selected_experiment": selection["selected"],
        "phase3_reasoning": selection["reasoning"],
        "phase3_full_ranking": selection["full_ranking"],
        "phase4_5_plan_and_validation": plan,
        "phase6_submission_gate": (
            "NOT SUBMITTED. This loop stops here per spec requirement 15 "
            "(human is the submission gate). A human must review the plan "
            "above and explicitly authorize SUBMIT before any candidate "
            "is sent to the live ladder."
        ),
    }
    return proposal


def main():
    proposal = run_readonly()
    print(json.dumps(proposal, indent=2, default=str))


if __name__ == "__main__":
    sys.exit(main())
