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


def _read_base():
    text = K_SRC.read_text()
    m = re.search(r"^KNOBS = \{.*?\}\n", text, re.S | re.M)
    assert m, "KNOBS block not found in K.py"
    knobs = eval(m.group(0)[len("KNOBS = "):])  # noqa: S307 - our own file
    consts = {}
    for name in CONST_SPACE:
        cm = re.search(rf"^{name}\s*=\s*([^#\n]+)", text, re.M)
        assert cm, f"constant {name} not found in K.py"
        consts[name] = eval(cm.group(1).strip())  # noqa: S307
    return text, knobs, consts


def base_params():
    """K.py's own defaults (== V3.12 behaviour with opening=v312)."""
    _, knobs, consts = _read_base()
    p = {k: knobs[k] for k in KNOB_SPACE}
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


def mutate(params, rate=0.2, sigma_frac=0.2, rng=random):
    """Gaussian/flip mutation. Each param mutated with prob `rate`; at least one."""
    p = dict(params)
    names = list(SPACE)
    chosen = [n for n in names if rng.random() < rate] or [rng.choice(names)]
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
    child = {n: (a[n] if rng.random() < 0.5 else b[n]) for n in SPACE}
    return mutate(child, rate=0.05, rng=rng)


def params_key(params, blocks=None):
    """Identity of a candidate = parameters + block overrides + the chassis snapshot they render into."""
    payload = json.dumps({k: params[k] for k in sorted(SPACE)}, sort_keys=True) + "|" + BASE_SHA + "|" + _blocks.blocks_key(blocks)
    return hashlib.sha256(payload.encode()).hexdigest()[:12]


def render(params, blocks=None, out_dir=GEN_DIR):
    """Write a concrete agent file for these params (+ optional block overrides); returns its path."""
    text, knobs, consts = _read_base()
    if blocks:
        text = _blocks.substitute(text, blocks)
    knobs = dict(knobs)
    for k in KNOB_SPACE:
        knobs[k] = params[k]
    m = re.search(r"^KNOBS = \{.*?\}\n", text, re.S | re.M)
    text = text[:m.start()] + "KNOBS = " + json.dumps(knobs) + "\n" + text[m.end():]
    for name in CONST_SPACE:
        text = re.sub(rf"^{name}\s*=\s*[^#\n]+", f"{name} = {params[name]!r}", text, count=1, flags=re.M)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"cand_{params_key(params, blocks)}.py"
    if not path.exists():
        path.write_text(text)
    return path


def diff(params, ref):
    return {k: (ref[k], params[k]) for k in SPACE if params[k] != ref[k]}
