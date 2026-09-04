"""Search space for the evolution loop.

A candidate is a flat dict of parameters. Two kinds:
  * KNOBS entries of candidates/K.py (the knobbed V3.12 chassis that C1 is built on)
  * top-level numeric constants of K.py (NAME = value lines)

render() writes a concrete agent file with those values substituted, so every
candidate is a normal single-file agent that mini_engine can run and cache by sha.
"""
from __future__ import annotations

import hashlib
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
K_LIVE = ROOT / "evolve" / "chassis.py"      # frozen chassis with typed mutation blocks (see blocks.py)
BASE_DIR = ROOT / "evolve" / "base"          # per-run snapshots of it, one per sha
GEN_DIR = ROOT / "evolve" / "gen"
K_SRC = K_LIVE                               # the snapshot in use; set by freeze_base()
BASE_SHA = ""
FRONTIER_SHA = ""                            # identity of the yardstick a candidate was scored against; set by set_frontier()

sys.path.insert(0, str(ROOT / "evolve"))
import blocks as _blocks  # noqa: E402


def freeze_base(src=K_LIVE):
    """Snapshot the chassis so a run renders every candidate from the same code even if
    candidates/K.py is edited mid-run. Returns (snapshot_path, sha)."""
    global K_SRC, BASE_SHA
    src = Path(src)
    sha = hashlib.sha256(src.read_bytes()).hexdigest()[:12]
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    snap = BASE_DIR / f"K_{sha}.py"
    if not snap.exists():
        snap.write_text(src.read_text())
    K_SRC, BASE_SHA = snap, sha
    return snap, sha


def set_frontier(frontier_path):
    """Bind the yardstick a run scores candidates against into the candidate key, so dev/held margins
    from one frontier (e.g. V3_12) can never collide with or masquerade as margins from another (e.g. H10)."""
    global FRONTIER_SHA
    FRONTIER_SHA = hashlib.sha256(Path(frontier_path).read_bytes()).hexdigest()[:12]
    return FRONTIER_SHA

# name -> (kind, low, high, step) ; kind in {"int", "float", "cat"}; for cat: (kind, choices)
KNOB_SPACE = {
    "melon_floor":      ("cat", [0, 100, 150, 200]),
    "harvest_min":      ("int", 1, 3, 1),
    "opening":          ("cat", ["v312", "frontier"]),
    "wheat_tiles":      ("int", 0, 8, 1),
    "wheat_stock":      ("int", 0, 40, 5),
    "min_hands":        ("int", 3, 6, 1),
    "load_per_hand":    ("int", 12, 26, 1),
    "geese":            ("int", 0, 2, 1),
    "open_melons":      ("int", 4, 14, 1),
    "open_wheat":       ("int", 3, 10, 1),
    "open_cows":        ("int", 1, 3, 1),
    "open_sheep":       ("int", 0, 3, 1),
    "early_hire_days":  ("int", 0, 8, 1),
    "feed_spare_poor":  ("int", 0, 3, 1),
    "fert_keep":        ("int", 0, 3, 1),
    "fert_buy":         ("int", 0, 3, 1),
    "fert_carry":       ("int", 1, 5, 1),
    "demand_share":     ("float", 0.3, 1.0, 0.05),
    "max_animals":      ("int", 10, 20, 1),
    "wheat_per_animal": ("float", 0.0, 1.2, 0.1),
    "wheat_cap":        ("int", 5, 25, 1),
    "wheat_water_tier": ("cat", [0, 1]),
    "wheat_sell_price": ("int", 25, 50, 1),
    "wheat_hold_days":  ("int", 0, 3, 1),

    "spec_units_STRAWBERRY":  ("cat", [None, 2.7, 3.6, 5.4, 6.3]),
    "spec_cycle_STRAWBERRY":  ("cat", [None, 11, 14, 22, 25]),
    "spec_cutoff_STRAWBERRY": ("cat", [None, 13, 15, 19, 21]),
    "spec_minval_STRAWBERRY": ("cat", [None, 6, 12, 18, 24, 30]),

    "spec_units_MELON":  ("cat", [None, 3.6, 4.8, 7.2, 8.4]),
    "spec_cycle_MELON":  ("cat", [None, 7, 9, 15, 17]),
    "spec_cutoff_MELON": ("cat", [None, 12, 14, 18, 20]),
    "spec_minval_MELON": ("cat", [None, 6, 12, 18, 24, 30]),

    "spec_units_WHEAT":  ("cat", [None, 3.0, 4.0, 6.0, 7.0]),
    "spec_cycle_WHEAT":  ("cat", [None, 3, 4, 6, 7]),
    "spec_cutoff_WHEAT": ("cat", [None, 20, 22, 26, 28]),
    "spec_minval_WHEAT": ("cat", [None, 6, 12, 18, 24, 30]),

    "spec_units_CARROT":  ("cat", [None, 2.4, 3.2, 4.8, 5.6]),
    "spec_cycle_CARROT":  ("cat", [None, 2, 3, 5, 6]),
    "spec_cutoff_CARROT": ("cat", [None, 21, 23, 27, 29]),
    "spec_minval_CARROT": ("cat", [None, 6, 12, 18, 24, 30]),

    "spec_units_TOMATO":  ("cat", [None, 3.0, 4.0, 6.0, 7.0]),
    "spec_cycle_TOMATO":  ("cat", [None, 8, 10, 14, 16]),
    "spec_cutoff_TOMATO": ("cat", [None, 16, 18, 22, 24]),
    "spec_minval_TOMATO": ("cat", [None, 6, 12, 18, 24, 30]),

    "seed_orders_cap":    ("int", 2, 6, 1),
    "land_deadline_shift": ("int", -4, 4, 1),
    "sell_order":         ("cat", ["default", "perishables_first", "fert_first"]),
    "herd_species_bias":  ("float", -2.0, 2.0, 0.5),
}

CONST_SPACE = {
    "MAX_HANDS":            ("int", 8, 16, 1),
    "ROUTE_LEN":            ("int", 2, 5, 1),
    "CROP_SWEEP_LEN":       ("int", 3, 10, 1),
    "CROP_SWEEP_RADIUS":    ("int", 2, 6, 1),
    "STRAW_CUTOFF":         ("int", 12, 20, 1),
    "MELON_MAX_TILES":      ("int", 20, 50, 2),
    "MELON_PRICE_CUSHION":  ("int", 50, 150, 10),
    "HERD_LAST_DAY":        ("int", 14, 22, 1),
    "NEAR_RADIUS":          ("int", 2, 5, 1),
    "OPP_GROWTH":           ("float", 1.0, 1.8, 0.1),
    "MAX_SHEEP":            ("int", 4, 14, 1),
    "OPENING_MELONS":       ("int", 6, 14, 1),
}

SPACE = {**KNOB_SPACE, **CONST_SPACE}


_warned = set()  # names we've already printed a one-time "missing from chassis" warning for


def _warn_once(name, kind):
    if name not in _warned:
        _warned.add(name)
        print(f"space: {kind} {name!r} is in SPACE but not in the frozen chassis yet "
              f"(rebuild with `python3 evolve/blocks.py build` to activate it) — skipping", file=sys.stderr)


def _read_base():
    text = K_SRC.read_text()
    m = re.search(r"^KNOBS = \{.*?\}\n", text, re.S | re.M)
    assert m, "KNOBS block not found in K.py"
    knobs = eval(m.group(0)[len("KNOBS = "):])  # noqa: S307 - our own file
    consts = {}
    for name in CONST_SPACE:
        cm = re.search(rf"^{name}\s*=\s*([^#\n]+)", text, re.M)
        if not cm:
            _warn_once(name, "constant")
            continue
        consts[name] = eval(cm.group(1).strip())  # noqa: S307
    return text, knobs, consts


def _live_knob_space():
    """KNOB_SPACE entries actually present in the current chassis (tolerant of an un-rebuilt chassis)."""
    _, knobs, _ = _read_base()
    live = [k for k in KNOB_SPACE if k in knobs]
    for k in KNOB_SPACE:
        if k not in knobs:
            _warn_once(k, "knob")
    return live


def base_params():
    """K.py's own defaults (== V3.12 behaviour with opening=v312). Only includes SPACE
    keys actually present in the frozen chassis, so an un-rebuilt chassis still works."""
    _, knobs, consts = _read_base()
    live = _live_knob_space()
    p = {k: knobs[k] for k in live}
    p.update(consts)
    return p


def c1_params():
    """C1 = K.py with the frontier-opening knobs (docs/candidates-C1-H10-sep03.md)."""
    p = base_params()
    p.update({"opening": "frontier", "early_hire_days": 5, "feed_spare_poor": 0, "open_melons": 8})
    return p


def clamp(name, v):
    spec = SPACE[name]
    if spec[0] == "cat":
        return v if v in spec[1] else random.choice(spec[1])
    _, lo, hi, step = spec
    v = max(lo, min(hi, v))
    if spec[0] == "int":
        return int(round(v))
    return round(round(v / step) * step, 4)


def _active_names(params):
    """SPACE names actually present in `params` — tolerant of a chassis that hasn't been
    rebuilt yet to carry every KNOB_SPACE/CONST_SPACE entry."""
    return [n for n in SPACE if n in params]


def mutate(params, rate=0.2, sigma_frac=0.2, rng=random):
    """Gaussian/flip mutation. Each param mutated with prob `rate`; at least one."""
    p = dict(params)
    names = _active_names(params)
    chosen = [n for n in names if rng.random() < rate] or ([rng.choice(names)] if names else [])
    for n in chosen:
        spec = SPACE[n]
        if spec[0] == "cat":
            choices = [c for c in spec[1] if c != p[n]]
            p[n] = rng.choice(choices)
        else:
            _, lo, hi, step = spec
            width = (hi - lo) * sigma_frac
            v = p[n] + rng.gauss(0, max(width, step))
            p[n] = clamp(n, v)
    return p


def crossover(a, b, rng=random):
    """Uniform crossover, then a light mutation so children are never exact copies."""
    names = [n for n in SPACE if n in a and n in b]
    child = {n: (a[n] if rng.random() < 0.5 else b[n]) for n in names}
    return mutate(child, rate=0.05, rng=rng)


def params_key(params, blocks=None):
    """Identity of a candidate = parameters + block overrides + the chassis snapshot they render into.
    Only keys actually present in `params` are hashed, so candidates from before a new knob was
    added keep their old key."""
    keys = _active_names(params)
    payload = json.dumps({k: params[k] for k in sorted(keys)}, sort_keys=True) + "|" + BASE_SHA + "|" + FRONTIER_SHA + "|" + _blocks.blocks_key(blocks)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]


def render(params, blocks=None, out_dir=GEN_DIR):
    """Write a concrete agent file for these params (+ optional block overrides); returns its path."""
    text, knobs, consts = _read_base()
    if blocks:
        text = _blocks.substitute(text, blocks)
    knobs = dict(knobs)
    for k in KNOB_SPACE:
        if k in knobs and k in params:
            knobs[k] = params[k]
    m = re.search(r"^KNOBS = \{.*?\}\n", text, re.S | re.M)
    text = text[:m.start()] + "KNOBS = " + repr(knobs) + "\n" + text[m.end():]
    for name in CONST_SPACE:
        if name not in params:
            continue
        text, n = re.subn(rf"^{name}\s*=\s*[^#\n]+", f"{name} = {params[name]!r}", text, count=1, flags=re.M)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"cand_{params_key(params, blocks)}.py"
    if not path.exists():
        path.write_text(text)
    return path


def diff(params, ref):
    return {k: (ref[k], params[k]) for k in SPACE if k in params and k in ref and params[k] != ref[k]}
