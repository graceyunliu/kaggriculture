#!/usr/bin/env python3
"""Fail-closed preflight for adaptive-v0.2-ladder-candidate.

Verifies that the controller, frozen learner state, and configuration files
in THIS package still match the hashes recorded in provenance_manifest.json
(which were themselves verified byte-identical to the certified,
independently-audited v0.2 artifacts). Also verifies the O42 candidate file
at its recorded external path, since O42 must never be modified, and the
three opponent files (scenario_v14, frontier_v12, soil_v25) at their
recorded repo-relative paths, since opponent files must never be modified.

Refuses to run (non-zero exit) if any hash differs. This script does not
run the experiment itself -- it only gates it. It performs no learning,
no A/B tuning, and no reward-function logic; it is packaging/integrity
tooling only.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "provenance_manifest.json"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check(label: str, path: Path, expected: str, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"MISSING: {label} not found at {path}")
        return
    actual = sha256_of(path)
    if actual != expected:
        failures.append(f"HASH MISMATCH: {label} at {path}\n    expected {expected}\n    actual   {actual}")


def main() -> int:
    if not MANIFEST.exists():
        print(f"STOP: provenance_manifest.json not found at {MANIFEST}", file=sys.stderr)
        return 2
    manifest = json.loads(MANIFEST.read_text())
    h = manifest["hashes"]
    failures: list[str] = []

    check("controller/adaptive_slice_v0.py", HERE / "controller" / "adaptive_slice_v0.py",
          h["controller_adaptive_slice_v0"]["sha256"], failures)
    check("runner/adaptive_eval_v0_2.py", HERE / "runner" / "adaptive_eval_v0_2.py",
          h["runner_adaptive_eval_v0_2"]["sha256"], failures)
    check("state/learner_frozen.json", HERE / "state" / "learner_frozen.json",
          h["frozen_learner_state"]["sha256"], failures)
    check("config/experiment_configuration.json", HERE / "config" / "experiment_configuration.json",
          h["experiment_configuration"]["sha256"], failures)
    check("config/seed_manifest.json", HERE / "config" / "seed_manifest.json",
          h["seed_manifest"]["sha256"], failures)
    check("config/opponent_manifest.json", HERE / "config" / "opponent_manifest.json",
          h["opponent_manifest"]["sha256"], failures)
    check("config/environment.json", HERE / "config" / "environment.json",
          h["environment_record"]["sha256"], failures)

    repo_root = HERE.parent.parent
    # v0.3: prefer the repo-relative O42 path when present (see provenance_manifest.json
    # "path_on_disk_note_v0_3") so preflight works regardless of the absolute path recorded
    # at v0.2 packaging time; fall back to the absolute path for backward compatibility.
    o42_rel = h["o42_candidate"].get("path_on_disk_relative_to_repo_root")
    o42_path = (repo_root / o42_rel) if o42_rel else Path(h["o42_candidate"]["path_on_disk"])
    check("O42 candidate (external, immutable)", o42_path, h["o42_candidate"]["sha256"], failures)

    for opp_name, opp in h["opponents"].items():
        check(f"opponent file ({opp_name})", repo_root / opp["path"], opp["sha256"], failures)

    if failures:
        print("PREFLIGHT FAILED -- refusing to run. Candidate integrity cannot be confirmed.", file=sys.stderr)
        for f in failures:
            print(f" - {f}", file=sys.stderr)
        return 1

    print("PREFLIGHT OK: controller, runner, frozen learner state, config, O42, and "
          "opponent files all match the recorded certified hashes. Safe to proceed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
