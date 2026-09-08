"""The five scenarios, in the order the ticket lists them (AGE-333).

Each entry is a module exposing `scenario() -> Scenario`. Adding a sixth diagnostic means writing
one module and adding it here; nothing else in the suite needs to change.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:      # scenario modules import their siblings by bare name
    sys.path.insert(0, str(_HERE))

import unsupported_livestock as _s1   # noqa: E402
import idle_labor as _s2              # noqa: E402
import late_expansion as _s3          # noqa: E402
import land_pressure as _s4           # noqa: E402
import execution_overload as _s5      # noqa: E402

# Bump when a scenario's world or thresholds change, so verdicts stored under an older definition
# are never silently compared against new ones.
SUITE_VERSION = "v1"

SCENARIO_MODULES = (_s1, _s2, _s3, _s4, _s5)


def all_scenarios():
    return [m.scenario() for m in SCENARIO_MODULES]


def names():
    return [s.name for s in all_scenarios()]


def get(name):
    for s in all_scenarios():
        if s.name == name:
            return s
    raise KeyError(f"unknown scenario {name!r}; have {names()}")


def select(only=None):
    """Scenarios named in `only`, or all of them. Scenarios are composable: any subset can be run
    on any candidate."""
    if not only:
        return all_scenarios()
    return [get(n) for n in only]
