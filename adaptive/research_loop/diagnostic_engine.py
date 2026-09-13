"""
diagnostic_engine.py -- Adaptive Research Loop v0.1

Answers, from stored evidence (ladder_ingest summaries + experiment_ledger +
hypothesis_store), the questions a human meta-learner was doing by hand:

    What changed?          (candidate vs its parent)
    What happened?         (ladder result vs prediction)
    Was the prediction supported?
    Which hypotheses gained/lost support?
    What should we test next?  (delegated to experiment_selector.py)

This module GENERATES hypotheses from evidence (spec requirement 4) rather
than requiring a human to name them. derive_hypotheses_from_v0_2_evidence()
is the concrete implementation of that for the one dataset we currently have
(the v0.2-vs-O42 ladder diagnostic). Each hypothesis records `source`: the
specific observation in the evidence that produced it, so this is auditable,
not asserted.
"""
from __future__ import annotations

from typing import Optional

import hypothesis_store as hs
import experiment_ledger as el
import ladder_ingest


def derive_hypotheses_from_v0_2_evidence() -> list:
    ev = ladder_ingest.load_v0_2_ladder_summary()
    a = ev["candidates"]["adaptive_v0.2"]
    o = ev["candidates"]["o42"]

    hyps = []

    hyps.append({
        "hypothesis_id": "H_RATING",
        "statement": (
            "The 895.9-vs-1174.0 public-score gap is substantially explained "
            "by rating path-dependence and incomplete convergence, not by "
            "Adaptive v0.2 playing worse than O42: raw per-game win rate "
            "(48.8% vs 50.7%) and mean money margin (+3,367 vs +1,929, "
            "nominally favoring Adaptive v0.2) are close to parity, while "
            "the rating mechanism (starts at 600, large per-game step early, "
            "decaying toward single digits by ~40-70 games) means a "
            "submission with fewer games (41 vs 71) and one early loss "
            "while its step size was still large (game 5: peak ~988 -> "
            "~877) can sit well below a submission that happened to string "
            "together early wins before its step size shrank."
        ),
        "supporting_evidence": [
            {"experiment": "adaptive_v0.2_ladder_56200714",
             "note": "win rate {}/{} ({:.1%}) vs O42 {}/{} ({:.1%}) -- not a "
                     "large gap; mean margin +{:.0f} vs +{:.0f}, favoring "
                     "Adaptive v0.2 nominally.".format(
                         a['wins'], a['games_real_opponent'],
                         a['wins']/a['games_real_opponent'],
                         o['wins'], o['games_real_opponent'],
                         o['wins']/o['games_real_opponent'],
                         a['mean_margin'], o['mean_margin'])},
            {"experiment": "adaptive_v0.2_ladder_56200714",
             "note": "chained initialScore/updatedScore directly shows a "
                     "sequential rating starting at 600 with a large, "
                     "decaying per-game step -- KAGGLE_SCORE_RECONSTRUCTION.md."},
        ],
        "contradicting_evidence": [
            {"experiment": "n/a",
             "note": "Not a controlled test: Adaptive v0.2 and O42 share "
                     "zero opponents, so we cannot rule out that Adaptive's "
                     "opponent pool was simply weaker (favorable variance "
                     "on margin) rather than the rating mechanism being the "
                     "full story. This hypothesis is about the SCORE GAP, "
                     "not a claim that Adaptive v0.2 has no real weaknesses."},
        ],
        "experiments": ["adaptive_v0.2_ladder_56200714"],
        "status": "ACTIVE",
        "confidence": "WEAK",
        "last_tested": "2026-09-13",
        "next_test_priority": "high",
        "source": ("derived/KAGGLE_SCORE_RECONSTRUCTION.md section "
                    "'Score trajectory summary' + derived/"
                    "LADDER_ADAPTIVE_V0_2_RAW_EVIDENCE.md section 3"),
    })

    hyps.append({
        "hypothesis_id": "H1",
        "statement": (
            "In several regimes the frozen learner's arm-B (B_ONE_PER_ORDER) "
            "empirical mean rests on very few real games (n=1-6), and frozen "
            "selection is effectively greedy on that noisy mean (no live "
            "explore bonus at eval time). This can make the deployed policy "
            "confidently choose B in states where the evidence does not "
            "actually support deviating from O42's behavior (A)."
        ),
        "supporting_evidence": [
            {"experiment": "offline_certified_v0.2_study",
             "note": ev["learner_state_support"]},
        ],
        "contradicting_evidence": [
            {"experiment": "adaptive_v0.2_ladder_56200714",
             "note": "Adaptive v0.2's raw ladder win rate/margin are close "
                     "to O42's, not dramatically worse -- if thin-support B "
                     "picks were routinely harmful, a larger raw-margin gap "
                     "would be a more expected signature than the rating-gap "
                     "pattern actually observed (see H_RATING)."},
        ],
        "experiments": ["adaptive-v0.3-ladder-candidate (built, not yet submitted)"],
        "status": "ACTIVE",
        "confidence": "WEAK",
        "last_tested": None,
        "next_test_priority": "medium",
        "source": ("candidate/adaptive-v0.3-ladder-candidate/provenance_manifest.json "
                    "'v0_3_change' block + adaptive_v0.2_learner_frozen.json"),
    })

    hyps.append({
        "hypothesis_id": "H2",
        "statement": (
            "The controller's training-time reward window (24 turns) may "
            "not track final-game outcome well, so the frozen policy could "
            "be optimized for a proxy that diverges from what actually wins "
            "games -- a generic short-horizon-reward risk that has not been "
            "directly tested against ladder outcomes because ladder replay "
            "data lacks controller decision traces."
        ),
        "supporting_evidence": [],
        "contradicting_evidence": [],
        "experiments": [],
        "status": "NEW",
        "confidence": "NO_EVIDENCE",
        "last_tested": None,
        "next_test_priority": "low",
        "source": ("inference from controller design docs (24-turn reward window); "
                    "not yet checked against any ladder or offline data -- flagged "
                    "as untested rather than assumed true or false"),
    })

    hyps.append({
        "hypothesis_id": "H3",
        "statement": (
            "The controller's regime partition (early/mid/late x high/low x "
            "roomy/tight, 7 observed cells) may be too coarse, merging game "
            "states that actually call for different arm choices and "
            "diluting each cell's empirical mean toward noise."
        ),
        "supporting_evidence": [
            {"experiment": "offline_certified_v0.2_study",
             "note": "Only 7 regimes observed with n ranging 1-53; several "
                     "near-boundary cells (e.g. mid|high|tight, B n=6 but A "
                     "wins) are exactly where a coarse partition would blur "
                     "a real effect."},
        ],
        "contradicting_evidence": [],
        "experiments": [],
        "status": "NEW",
        "confidence": "NO_EVIDENCE",
        "last_tested": None,
        "next_test_priority": "low",
        "source": "adaptive_v0.2_learner_frozen.json regime list",
    })

    hyps.append({
        "hypothesis_id": "H5",
        "statement": (
            "The live ladder's opponent population differs from the 4 named "
            "offline opponents (scenario_v14, o42_selfplay, frontier_v12, "
            "soil_v25) the certified v0.2 study trained/evaluated against, "
            "so offline-validated mechanism generalization may not transfer "
            "as-is to ladder play."
        ),
        "supporting_evidence": [
            {"experiment": "adaptive_v0.2_ladder_56200714",
             "note": "Zero opponent-ID overlap between Adaptive v0.2's and "
                     "O42's ladder games, and neither set overlaps the "
                     "offline study's 4 named opponents/8 fixed seeds."},
        ],
        "contradicting_evidence": [
            {"experiment": "adaptive_v0.2_ladder_56200714",
             "note": "Adaptive v0.2's raw ladder margin/win-rate are close "
                     "to O42's despite the distribution difference, which is "
                     "some (weak) evidence the offline mechanism DID transfer "
                     "reasonably -- undercutting a strong version of H5."},
        ],
        "experiments": ["adaptive_v0.2_ladder_56200714"],
        "status": "ACTIVE",
        "confidence": "WEAK",
        "last_tested": "2026-09-13",
        "next_test_priority": "low",
        "source": ("derived/LADDER_ADAPTIVE_V0_2_RAW_EVIDENCE.md section 4 "
                    "(opponent overlap) + provenance_manifest.json opponent list"),
    })

    return hyps


def seed_hypothesis_store() -> None:
    for h in derive_hypotheses_from_v0_2_evidence():
        hs.upsert(h)


def what_changed(candidate_id: str) -> str:
    row = el.get(candidate_id)
    if row is None:
        return "No ledger entry for {}.".format(candidate_id)
    parent = row.get("parent_candidate")
    return ("{} vs parent {}: {} (files: {}); tests hypothesis {}: {}".format(
        candidate_id, parent, row.get('change_description'),
        row.get('changed_files'), row.get('hypothesis_id'), row.get('hypothesis')))


def was_prediction_supported(candidate_id: str):
    row = el.get(candidate_id)
    if row is None or row.get("ladder_result") is None:
        return None
    return row.get("hypothesis_update")


def summarize_current_state() -> dict:
    rows = el.effective_rows()
    hyps = hs.all_hypotheses()
    return {
        "n_experiments_in_ledger": len(rows),
        "candidate_ids": [r["candidate_id"] for r in rows],
        "hypotheses": [
            {"id": h["hypothesis_id"], "status": h["status"],
             "confidence": h["confidence"], "statement": h["statement"]}
            for h in hyps
        ],
    }


if __name__ == "__main__":
    seed_hypothesis_store()
    import json
    print(json.dumps(summarize_current_state(), indent=2))
