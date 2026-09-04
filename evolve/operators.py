"""Paired search operators: allocation (economy) x execution (labor) mutation.

Empirical motivation (evolve/RULES.md, "Routing oracle"): making the router free is ~0 on
average because the economy doesn't generate enough obligations to use the freed labor, and
copying the opponent's allocation onto our dispatcher loses -$68k. Allocation-only and
execution-only changes have both been measured to fail; the frontier's edge is *paired* --
more obligations generated AND an execution change that services them. These operators force
every mutation (or grid cell) to touch one econ/allocation knob AND one exec/labor knob (or
block), instead of leaving that pairing to chance under plain rate-based mutation.

    python3 evolve/operators.py grid --out evolve/queue/coupled_grid_sep04.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

import space  # noqa: E402
import blocks as blocks_mod  # noqa: E402

# ---------------------------------------------------------------------------
# ECON / EXEC classification
#
# EXEC_EXPLICIT and UNKNOWN_EXPLICIT are the small, hand-picked sets called out in
# evolve/RULES.md as execution/labor mechanics. Every other key in space.SPACE is
# allocation/economy (OPP_GROWTH included: it is OUR demand model's assumption about the
# opponent's supply growth, i.e. an allocation input): openings, herd/seed
# sizing, crop-species schedule constants (spec_*, STRAW_CUTOFF, MELON_*, HERD_LAST_DAY,
# MAX_SHEEP, OPENING_MELONS), land/sell/feed/fertilizer knobs.

EXEC_EXPLICIT = {
    "min_hands", "load_per_hand", "early_hire_days", "harvest_min",
    "MAX_HANDS", "ROUTE_LEN", "CROP_SWEEP_LEN", "CROP_SWEEP_RADIUS", "NEAR_RADIUS",
}

UNKNOWN_EXPLICIT = set()   # every SPACE key is classified; OPP_GROWTH is an ECON key

_ALL_SPACE_KEYS = set(space.SPACE)

EXEC_KEYS = sorted(EXEC_EXPLICIT & _ALL_SPACE_KEYS)
UNKNOWN_KEYS = sorted(UNKNOWN_EXPLICIT & _ALL_SPACE_KEYS)
ECON_KEYS = sorted(_ALL_SPACE_KEYS - EXEC_EXPLICIT - UNKNOWN_EXPLICIT)

# every key must land in exactly one bucket
_covered = set(ECON_KEYS) | set(EXEC_KEYS) | set(UNKNOWN_KEYS)
assert _covered == _ALL_SPACE_KEYS, f"unclassified SPACE keys: {_ALL_SPACE_KEYS - _covered}"
assert not (set(ECON_KEYS) & set(EXEC_KEYS)), "a key cannot be both ECON and EXEC"
if UNKNOWN_KEYS:
    print(f"operators: {len(UNKNOWN_KEYS)} SPACE key(s) classified as neither econ nor exec "
          f"(excluded from paired_mutate): {UNKNOWN_KEYS}", file=sys.stderr)

# execution-layer blocks worth pairing against an allocation change (per RULES.md: "sweep,
# dispatch, animal_routing, crop_admission are where the remaining value is")
EXEC_BLOCK_NAMES = ["sweep", "animal_routing", "dispatch", "crop_admission"]


# ---------------------------------------------------------------------------
# single-key mutation, replicating space.mutate's per-key logic exactly (that function only
# operates on a whole dict of chosen keys, so we factor its inner branch out here)

def _mutate_key(p, name, rng, sigma_frac):
    """Mutate params[name] in place (on a copy) per space.SPACE's clamp semantics, guaranteed to
    actually change the value (retries the Gaussian draw rather than risk a same-value no-op from
    rounding/clamping). Returns the copy."""
    q = dict(p)
    spec = space.SPACE[name]
    orig = q.get(name)
    if spec[0] == "cat":
        choices = [c for c in spec[1] if c != orig]
        if choices:
            q[name] = rng.choice(choices)
    else:
        _, lo, hi, step = spec
        width = (hi - lo) * sigma_frac
        for _ in range(30):
            v = orig + rng.gauss(0, max(width, step))
            cv = space.clamp(name, v)
            if cv != orig:
                q[name] = cv
                break
        else:
            # range too narrow to move by chance (shouldn't happen for any real SPACE entry) --
            # step to the nearest edge deterministically so the mutation is never a no-op.
            q[name] = hi if orig <= lo else lo
    return q


def _active(params, keys):
    return [k for k in keys if k in params]


# ---------------------------------------------------------------------------

def paired_mutate(params, rng=random, sigma_frac=0.2):
    """Mutate exactly one ECON key and one EXEC key; everything else unchanged. Deterministic
    given rng (an instance, not the module, for reproducibility across calls)."""
    p = dict(params)
    econ_pool = _active(p, ECON_KEYS)
    exec_pool = _active(p, EXEC_KEYS)
    if econ_pool:
        e = rng.choice(econ_pool)
        p = _mutate_key(p, e, rng, sigma_frac)
    if exec_pool:
        x = rng.choice(exec_pool)
        p = _mutate_key(p, x, rng, sigma_frac)
    return p


def _block_library(blocks_dir=None):
    """{block_name: [None, src1, src2, ...]} for every block that has at least one file under
    evolve/blocks/ whose top-level defs satisfy that block's required functions (evolve/blocks.py
    BLOCKS). None always comes first (chassis default)."""
    blocks_dir = Path(blocks_dir) if blocks_dir else (HERE / "blocks")
    lib = {name: [None] for name in blocks_mod.BLOCKS}
    for f in sorted(blocks_dir.glob("*.py")):
        if f.name == "__init__.py":
            continue
        src = f.read_text()
        try:
            defined = {n.name for n in __import__("ast").parse(src).body
                       if isinstance(n, __import__("ast").FunctionDef)}
        except SyntaxError:
            continue
        for name, funcs in blocks_mod.BLOCKS.items():
            if set(funcs) <= defined:
                lib[name].append(src)
    return lib


def block_pair_mutate(params, blocks, rng=random, library=None):
    """Mutate one ECON key AND swap one execution block for a random alternative from
    `library` (default: everything under evolve/blocks/, grouped by which block a file's
    functions belong to). None in a library entry means "chassis default" (remove override).
    Returns (params, blocks)."""
    library = library if library is not None else _block_library()
    p = dict(params)
    econ_pool = _active(p, ECON_KEYS)
    if econ_pool:
        e = rng.choice(econ_pool)
        p = _mutate_key(p, e, rng, 0.2)
    b = dict(blocks or {})
    candidates = [name for name in EXEC_BLOCK_NAMES if library.get(name)]
    if candidates:
        name = rng.choice(candidates)
        src = rng.choice(library[name])
        if src is None:
            b.pop(name, None)
        else:
            b[name] = src
    return p, (b or None)


def coupled_grid(base_params, econ_axes, exec_axes, block_options=None):
    """Full factorial across econ_axes x exec_axes x block_options.
    econ_axes / exec_axes: {param_name: [values]}. block_options: {block_name: [None, src, ...]}.
    Yields (params, blocks, tag) for every combination."""
    block_options = block_options or {}
    names = list(econ_axes) + list(exec_axes) + [f"block:{b}" for b in block_options]
    levels = [econ_axes[k] for k in econ_axes] + [exec_axes[k] for k in exec_axes] + \
             [block_options[b] for b in block_options]
    for combo in itertools.product(*levels):
        params = dict(base_params)
        blocks = {}
        tag = []
        for name, val in zip(names, combo):
            if name.startswith("block:"):
                bname = name[len("block:"):]
                if val:
                    blocks[bname] = val
                    tag.append(f"{bname}=custom")
                else:
                    tag.append(f"{bname}=default")
            else:
                params[name] = space.clamp(name, val) if name in space.SPACE else val
                tag.append(f"{name}={val}")
        yield params, (blocks or None), " ".join(tag)


# ---------------------------------------------------------------------------
# CLI: write a queue factorial file matching loop.py's consume_queue() "factorial" schema.

def _c1_grid_base():
    p = space.c1_params()
    p.update({
        "melon_floor": 200, "load_per_hand": 16, "open_melons": 10, "open_wheat": 8,
        "wheat_water_tier": 1, "wheat_sell_price": 29, "CROP_SWEEP_LEN": 5,
        "MELON_MAX_TILES": 50, "HERD_LAST_DAY": 22, "NEAR_RADIUS": 2, "OPP_GROWTH": 1.1,
    })
    return p


def _grid_block_options():
    """block_options for 'sweep' and 'dispatch', restricted to files whose names start with
    lib_ (sweep or dispatch), dispatch_, or animal_routing_ -- per the task spec -- plus the
    fixed banded crop_admission block (not offered as an axis; folded into every cell below)."""
    blocks_dir = HERE / "blocks"
    lib = {"sweep": [None], "dispatch": [None]}
    for f in sorted(blocks_dir.glob("*.py")):
        name = f.name
        if not (name.startswith("lib_") or name.startswith("dispatch_") or name.startswith("animal_routing_")):
            continue
        src = f.read_text()
        defined = {n.name for n in __import__("ast").parse(src).body
                   if isinstance(n, __import__("ast").FunctionDef)}
        for block_name in ("sweep", "dispatch"):
            if set(blocks_mod.BLOCKS[block_name]) <= defined:
                lib[block_name].append(src)
    return lib


def build_grid_queue_item():
    base = _c1_grid_base()
    econ_axes = {"demand_share": [0.5, 0.6], "open_melons": [10, 12], "wheat_per_animal": [0.0, 0.3]}
    exec_axes = {"load_per_hand": [16, 12], "MAX_HANDS": [13, 15]}
    block_options = _grid_block_options()
    banded_src = (ROOT / "evolve" / "blocks_banded_crop_admission.py").read_text()

    axes = dict(econ_axes)
    axes.update(exec_axes)
    n_combos = 1
    for v in axes.values():
        n_combos *= len(v)
    for v in block_options.values():
        n_combos *= len(v)

    # crop_admission is fixed (not an axis) -- fold the banded block into base via a
    # block_options entry of length 1 so consume_queue's itertools.product still applies it
    # to every cell without adding a combinatorial dimension.
    block_options = dict(block_options)
    block_options["crop_admission"] = [banded_src]

    item = {
        "kind": "factorial",
        "base": "c1",
        "axes": axes,
        "block_options": block_options,
        "origin": "operators:coupled_grid_sep04",
        "note": "coupled econ x exec grid (paired-operator hypothesis, Sep 4): demand_share/"
                "open_melons/wheat_per_animal (econ) x load_per_hand/MAX_HANDS (exec) x "
                "sweep/dispatch block swaps, banded crop_admission fixed. Base = E1-style "
                "params on c1_params().",
    }
    return item, n_combos, base


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("grid", help="write the coupled econ x exec queue factorial")
    g.add_argument("--out", default=str(HERE / "queue" / "coupled_grid_sep04.json"))
    g.add_argument("--allow-large", action="store_true", help="allow more than 64 candidates")

    args = ap.parse_args()
    if args.cmd == "grid":
        item, n, base = build_grid_queue_item()
        print(f"grid: {n} candidates")
        if n > 64 and not args.allow_large:
            print(f"refusing to write: {n} > 64 candidates; pass --allow-large to override", file=sys.stderr)
            sys.exit(1)
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(item, indent=1))
        print(f"wrote {out} ({n} candidates)")


if __name__ == "__main__":
    main()
