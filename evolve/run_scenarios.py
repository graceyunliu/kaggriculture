#!/usr/bin/env python3
"""CLI entry point for the AGE-333 adversarial diagnostic scenarios.

The suite itself lives in evolve/scenarios/ (one module per scenario plus the runner); this is the
top-level command, alongside evolve/report.py and evolve/failure_report.py.

    python3 evolve/run_scenarios.py --list
    python3 evolve/run_scenarios.py --agent candidates/C1.py candidates/V3_12.py
    python3 evolve/run_scenarios.py --from-db --frontier candidates/H32.py --md evolve/reports/scenarios.md

It is a diagnostic, not a gate: nothing it produces is read by evolve/cascade.py or by parent
selection.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

from scenarios.runner import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
