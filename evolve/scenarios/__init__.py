"""Adversarial diagnostic scenarios (AGE-333).

Five targeted economic worlds, each isolating one failure mode, run as a *diagnostic pass* that is
deliberately separate from the cascade in evolve/cascade.py: nothing here feeds ranking, selection
or promotion. A candidate that has reached dev gets a scenario report saying, per scenario, whether
it passed and which metric decided it.

    import scenarios                                   # with evolve/ on sys.path
    scenarios.all_scenarios()                          # -> [Scenario, ...] in registry order
    scenarios.get("idle_labor")                        # -> Scenario
    scenarios.run_suite("candidates/C1.py")            # -> scenario report dict

CLI:

    python3 evolve/run_scenarios.py --list
    python3 evolve/run_scenarios.py --agent candidates/C1.py
    python3 evolve/run_scenarios.py --from-db --frontier candidates/H32.py --md report.md

Each scenario lives in its own module and returns a `Scenario` (see spec.py) carrying the engine
config, the pass/fail criteria and a description, so adding or retuning one is a single-file edit.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from spec import Criterion, Scenario                                    # noqa: E402,F401
from registry import (SUITE_VERSION, SCENARIO_MODULES, all_scenarios,   # noqa: E402,F401
                      names, get, select)
from metrics import scenario_metrics, aggregate                         # noqa: E402,F401
from runner import run_scenario, run_suite, dev_candidates, resolve_frontier  # noqa: E402,F401
