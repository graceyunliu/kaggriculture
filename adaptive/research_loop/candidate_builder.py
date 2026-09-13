"""
candidate_builder.py -- Adaptive Research Loop v0.1

Turns a selected hypothesis into (a) a candidate PLAN -- version name,
parent, exactly-one change description, predicted effect, validation
checklist -- and, for hypotheses that need no code change (e.g. H_RATING,
testable by accumulating more games on an unchanged candidate), a plan that
says so explicitly rather than manufacturing a fake code change.

This module does NOT write controller/config code itself and does NOT touch
adaptive-v0.2-ladder-candidate or O42. For hypotheses that already have a
prepared candidate package (H1 -> candidate/adaptive-v0.3-ladder-candidate,
built in an earlier session), it reads and reports on that existing package
rather than duplicating it.

Naming convention observed in this repo: candidate/adaptive-vX.Y-ladder-candidate/.
Never reuses or overwrites an existing version directory.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CANDIDATE_DIR = os.path.join(REPO_ROOT, "candidate")
O42_CANONICAL_HASH = "154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813"
O42_PATH = os.path.join(REPO_ROOT, "candidates", "O42_MAX_HANDS_LATE_EXPAND.py")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def existing_candidate_versions() -> list:
    pattern = os.path.join(CANDIDATE_DIR, "adaptive-v*-ladder-candidate")
    versions = []
    for path in glob.glob(pattern):
        m = re.search(r"adaptive-v(\d+)\.(\d+)-ladder-candidate$", path)
        if m:
            versions.append((int(m.group(1)), int(m.group(2)), os.path.basename(path)))
    versions.sort()
    return [v[2] for v in versions]


def next_version_name() -> str:
    versions = existing_candidate_versions()
    best = (0, 0)
    for v in versions:
        m = re.search(r"adaptive-v(\d+)\.(\d+)-ladder-candidate$", v)
        maj, minor = int(m.group(1)), int(m.group(2))
        if (maj, minor) > best:
            best = (maj, minor)
    return "adaptive-v{}.{}-ladder-candidate".format(best[0], best[1] + 1)


def check_o42_immutable() -> dict:
    ok = os.path.exists(O42_PATH) and sha256_file(O42_PATH) == O42_CANONICAL_HASH
    return {"o42_path": O42_PATH, "expected_hash": O42_CANONICAL_HASH, "matches": ok}


def lightweight_validation(candidate_dir_name: str) -> dict:
    path = os.path.join(CANDIDATE_DIR, candidate_dir_name)
    checks = {}
    checks["candidate_dir_exists"] = os.path.isdir(path)
    checks["readme_exists"] = os.path.exists(os.path.join(path, "README.md"))
    checks["provenance_manifest_exists"] = os.path.exists(
        os.path.join(path, "provenance_manifest.json"))
    checks["preflight_script_exists"] = os.path.exists(os.path.join(path, "preflight.py"))
    o42check = check_o42_immutable()
    checks["o42_hash_matches_certified"] = o42check["matches"]
    if checks["provenance_manifest_exists"]:
        with open(os.path.join(path, "provenance_manifest.json")) as f:
            manifest = json.load(f)
        checks["manifest_present"] = True
        checks["manifest_mentions_v0_2_parent"] = "v0.2" in json.dumps(manifest)
    else:
        checks["manifest_present"] = False
    checks["all_pass"] = all(v for k, v in checks.items() if isinstance(v, bool))
    return checks


def plan_for_hypothesis(hypothesis_id: str, hypothesis_statement: str) -> dict:
    o42_check = check_o42_immutable()

    if hypothesis_id == "H_RATING":
        return {
            "hypothesis_id": hypothesis_id,
            "requires_new_candidate": False,
            "plan": (
                "H_RATING is a claim about the SCORING MECHANISM, not about "
                "Adaptive v0.2's policy. It cannot be tested by changing "
                "code -- it is tested by accumulating more real-opponent "
                "games on an UNCHANGED candidate and checking whether "
                "Adaptive v0.2's rating trajectory continues converging "
                "upward toward an O42-like plateau shape (~15-20 games of "
                "tight oscillation) rather than staying depressed. "
                "Concretely: no new candidate directory; the existing, "
                "already-submitted adaptive-v0.2-ladder-submission-v2.zip "
                "(sub 56200714) simply continues accruing ladder games under "
                "Kaggle's normal matchmaking, and a future ladder_ingest.py "
                "pull + diagnostic_engine pass re-checks the trajectory."
            ),
            "predicted_effect": (
                "If H_RATING is correct: Adaptive v0.2's rating, given "
                "~20-30 more real games, should climb out of the ~840-980 "
                "band and settle into a plateau, similar in shape (not "
                "necessarily equal in level) to O42's ~15-game convergence "
                "pattern, WITHOUT any code change. If instead it stays "
                "depressed after a comparable number of additional games, "
                "H_RATING is weakened and a policy-level explanation "
                "(H1/H2/H3) becomes relatively more attractive."
            ),
            "what_would_support": "rating trend moves up and stabilizes with more games, no code change",
            "what_would_weaken": "rating stays depressed or continues falling despite 20-30 more games",
            "o42_immutability_check": o42_check,
        }

    if hypothesis_id == "H1":
        existing = os.path.join(CANDIDATE_DIR, "adaptive-v0.3-ladder-candidate")
        has_existing = os.path.isdir(existing)
        return {
            "hypothesis_id": hypothesis_id,
            "requires_new_candidate": not has_existing,
            "existing_candidate_path": existing if has_existing else None,
            "plan": (
                "A candidate already exists for H1: "
                "candidate/adaptive-v0.3-ladder-candidate (built in an "
                "earlier session, NOT yet submitted to the ladder). It adds "
                "MIN_N_TO_TRUST_B=10 to frozen-mode arm selection: falls "
                "back to A_FULL_O42 when a regime's B_ONE_PER_ORDER arm has "
                "fewer than 10 real observations. learner_frozen.json, the "
                "regime partition, and training-time UCB1 behavior are "
                "unchanged. This research loop did not modify that package; "
                "it only inspected its provenance_manifest.json to confirm "
                "the change is minimal and isolable (exactly one guard, "
                "flips 3 of 7 regimes from B to A)."
            ),
            "predicted_effect": (
                "If H1 is correct: v0.3's win rate/margin should improve "
                "over v0.2's specifically because the 3 flipped regimes no "
                "longer deploy an under-supported B pick. IMPORTANT "
                "confound flagged by H_RATING: v0.3's Kaggle rating will "
                "start at 600 and go through the same high-K early-game "
                "period v0.2 did, so a naive final-score comparison "
                "(v0.3's early rating vs v0.2's now-more-converged rating) "
                "would be misleading. The diagnostic layer must compare "
                "matched-game-index trajectories and raw win-rate/margin, "
                "not just the two final displayed scores."
            ),
            "what_would_support": (
                "v0.3's raw win-rate/margin over its first ~40 real games "
                "is higher than v0.2's over its first ~40 (matched game "
                "index), OR v0.3's early rating trajectory avoids the "
                "sharp game-5-style drop v0.2 had."
            ),
            "what_would_weaken": (
                "v0.3's raw win-rate/margin at matched game index is the "
                "same or worse than v0.2's -- would suggest the 3 flipped "
                "regimes were not where v0.2's issues (if any) actually lay."
            ),
            "changed_files": ["controller/adaptive_slice_v0.py (MIN_N_TO_TRUST_B guard only)"],
            "parent_candidate": "adaptive-v0.2-ladder-candidate",
            "o42_immutability_check": o42_check,
            "validation_checklist": (lightweight_validation("adaptive-v0.3-ladder-candidate")
                                      if has_existing else None),
        }

    return {
        "hypothesis_id": hypothesis_id,
        "requires_new_candidate": False,
        "plan": (
            "No scoped candidate change has been designed yet for {}. Per "
            "the speed principle, do not invest in designing one until it "
            "out-ranks the current top pick in experiment_selector.py. "
            "Statement on file: {}".format(hypothesis_id, hypothesis_statement)
        ),
        "o42_immutability_check": o42_check,
    }


if __name__ == "__main__":
    print("Next free version name:", next_version_name())
    print(json.dumps(plan_for_hypothesis(
        "H1", "selector conservatism / thin empirical support"), indent=2))
