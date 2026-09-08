"""Control agents for validating that a scenario's criteria actually fire (AGE-333).

These are lab fixtures, not candidates. Each one wraps an existing agent and rewrites its action
dict to inject exactly one pathology -- hire past the work available, hold animal products, defer
land to the last week, never expand, never hire. They exist so the suite can be checked in both
directions: a scenario that no agent in the population fails is only evidence of a healthy
population if the FAIL path is known to work.

    from controls import write_control
    bad = write_control("candidates/C1.py", "overhire", out_dir)   # -> path to a runnable agent

Nothing in the evolution loop reads this module, and no control agent is ever a candidate.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

ANIMAL_PRODUCTS = ("MILK", "WOOL", "EGG")
LATE_DAY = 23           # matches metrics.LATE_GAME_START
EXTRA_HIRES_PER_TURN = 2
MAX_KEPT_HANDS = 2      # for the "starve_labor" control


def _market(act):
    m = act.get("market")
    return list(m) if isinstance(m, list) else []


def _day(obs):
    return obs["day"] if isinstance(obs, dict) else getattr(obs, "day", 0)


def _op(order):
    return order[0] if isinstance(order, (list, tuple)) and order else None


def overhire(obs, act, farm):
    """Hire as hard as the market-order budget allows, every turn, regardless of work available."""
    act["market"] = _market(act) + [["HIRE"]] * EXTRA_HIRES_PER_TURN
    return act


def hold_animal_products(obs, act, farm):
    """Never sell MILK/WOOL/EGG: the herd still eats, but nothing it makes is ever monetised."""
    act["market"] = [o for o in _market(act)
                     if not (_op(o) == "SELL" and len(o) > 1 and o[1] in ANIMAL_PRODUCTS)]
    return act


def no_livestock(obs, act, farm):
    """Positive control: never buy an animal, so the herd never exists to be unsupported."""
    act["market"] = [o for o in _market(act) if _op(o) != "BUY_ANIMAL"]
    return act


def defer_expansion(obs, act, farm):
    """Buy no land until day 23, then buy it -- capital committed with no time left to work it."""
    day = _day(obs)
    orders = [o for o in _market(act) if _op(o) != "BUY_LAND"]
    if day >= LATE_DAY:
        orders.append(["BUY_LAND"])
    act["market"] = orders
    return act


def hoard(obs, act, farm):
    """Never expand capacity: no land, no hires. Cash accumulates while demand goes unmet."""
    act["market"] = [o for o in _market(act) if _op(o) not in ("BUY_LAND", "HIRE")]
    return act


def starve_labor(obs, act, farm):
    """Keep the footprint the base agent builds but stop hiring past a token crew.

    Positive control for execution_overload: this chassis reads its own crew size when it sizes
    the next day's planting, so starving it of hands makes it plant less rather than break -- which
    is the scenario's second pass condition ("limits production footprint to what it can service").
    """
    hands = len(farm.get("hands") or []) if isinstance(farm, dict) else 0
    if hands >= MAX_KEPT_HANDS:
        act["market"] = [o for o in _market(act) if _op(o) != "HIRE"]
    return act


def neglect_feeding(obs, act, farm):
    """Negative control for execution_overload: keep the herd, drop every FEED and CARE action.

    The end state of a farm that outgrew its crew -- obligations enumerated at day start and never
    serviced -- injected directly, so the escape/missed-feed criteria can be checked without
    needing an agent that happens to over-expand.
    """
    drop = {"FEED", "CARE"}
    if _op(act.get("farmer")) in drop:
        act["farmer"] = ["PASS"]
    act["hands"] = [(["PASS"] if _op(h) in drop else h) for h in (act.get("hands") or [])]
    return act


MODES = {
    "overhire": overhire,
    "hold_animal_products": hold_animal_products,
    "no_livestock": no_livestock,
    "defer_expansion": defer_expansion,
    "hoard": hoard,
    "starve_labor": starve_labor,
    "neglect_feeding": neglect_feeding,
}


def apply(mode, obs, act, farm):
    act = dict(act) if isinstance(act, dict) else {"farmer": ["PASS"], "hands": [], "market": []}
    return MODES[mode](obs, act, farm)


_TEMPLATE = '''# AGE-333 scenario control agent -- lab fixture, never a candidate.
# base: {base}
# pathology: {mode}
import importlib.util as _ilu
import sys as _sys

_sys.path[:0] = [r"{scen_dir}", r"{evolve_dir}", r"{root}"]
import controls as _controls  # noqa: E402

_spec = _ilu.spec_from_file_location("ctl_base_{tag}", r"{base}")
_base = _ilu.module_from_spec(_spec)
_sys.modules[_spec.name] = _base
_spec.loader.exec_module(_base)


def agent(obs, configuration=None):
    act = _base.agent(obs, configuration)
    player = obs["player"] if isinstance(obs, dict) else obs.player
    farms = obs["farms"] if isinstance(obs, dict) else obs.farms
    return _controls.apply("{mode}", obs, act, farms[player])
'''


def write_control(base_agent, mode, out_dir):
    """Write (and return the path to) a runnable agent that plays `base_agent` with `mode` injected."""
    if mode not in MODES:
        raise KeyError(f"unknown control mode {mode!r}; have {sorted(MODES)}")
    base = Path(base_agent).resolve()
    tag = hashlib.sha256(f"{base}|{mode}".encode()).hexdigest()[:8]
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"ctl_{mode}_{base.stem}_{tag}.py"
    path.write_text(_TEMPLATE.format(base=base, mode=mode, tag=tag, scen_dir=HERE,
                                     evolve_dir=ROOT / "evolve", root=ROOT))
    return path
