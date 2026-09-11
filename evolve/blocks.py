"""Typed mutation blocks.

The chassis (evolve/chassis.py) is a frozen copy of candidates/K.py with marker comments around
groups of functions. A candidate may replace the source of any block. Everything outside the
blocks (engine constants, perception, the crash guard) is fixed.

    python3 evolve/blocks.py build            # (re)build evolve/chassis.py from K_LIVE (K_SELFMODEL.py since Sep 11)
    python3 evolve/blocks.py list             # show blocks and line counts
"""
from __future__ import annotations

import ast
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
K_LIVE = ROOT / "candidates" / "O26_CARROT_SIZING.py"   # Frozen behavioral source of truth for the exact O26 chassis.
CHASSIS = ROOT / "evolve" / "chassis.py"

# block name -> top-level function names (must be contiguous in the file, in this order)
BLOCKS = {
    "hiring":         ["_hire_plan", "_load_model"],
    "demand":         ["_instances", "_daily_demand", "_demand_room"],
    "economy":        ["economy"],
    "animal_routing": ["_build_route", "_route_step"],
    "siting":         ["_pick_site", "_setup_step"],
    "crop_admission": ["_crop_pools", "_plant_choice", "_task_valid"],
    # O26 places _orchestrate between _steal_task and _crop_step; keep the range contiguous
    # rather than relocating the function or creating a behavior-changing split.
    "sweep":          ["_build_sweep", "_steal_task", "_orchestrate", "_crop_step"],
    "dispatch":       ["_unit_action"],
}

BLOCK_DOC = {
    "hiring":         "how many hands to hire each day: labour load model and hire budget",
    "demand":         "town demand model from unlocked shop instances; herd sizing room per species",
    "economy":        "the whole daily market policy: opening, feed, seeds, animals, land, selling, fertilizer",
    "animal_routing": "per-hand routes for animal feed/care/collect trips and pickups from the shed",
    "siting":         "where new animals are placed and how a hand sets one up",
    "crop_admission": "which tiles are eligible for which crop task; what crop to plant where",
    "sweep":          "per-hand crop sweeps: tier order (urgent water, harvest, water, plant, weeds) and step choice",
    "dispatch":       "top-level per-unit action choice: animal route vs crop sweep vs idle",
}

START = "# ===== EVOLVE-BLOCK: {name} ====="
END = "# ===== END-BLOCK: {name} ====="


def _func_ranges(src):
    tree = ast.parse(src)
    out = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            start = node.lineno
            if node.decorator_list:
                start = min(d.lineno for d in node.decorator_list)
            out[node.name] = (start, node.end_lineno)
    return out


_MARKER_RE = re.compile(r"^# ===== (?:EVOLVE-BLOCK|END-BLOCK): \w+ =====\n", re.M)


def build(src_path=K_LIVE, out_path=CHASSIS):
    src = Path(src_path).read_text()
    # The O-lineage candidates descend from a rendered chassis and still carry the marker comments;
    # strip them so the rebuild does not double them up.
    src = _MARKER_RE.sub("", src)
    lines = src.splitlines(keepends=True)
    ranges = _func_ranges(src)
    inserts = []  # (line_index, text)
    for name, funcs in BLOCKS.items():
        missing = [f for f in funcs if f not in ranges]
        if missing:
            raise SystemExit(f"block {name}: functions not found in {src_path}: {missing}")
        first = ranges[funcs[0]][0]
        last = ranges[funcs[-1]][1]
        # sanity: nothing but these functions (and blank lines / comments) between first and last
        inner = {f for f, (a, b) in ranges.items() if first <= a and b <= last}
        if inner != set(funcs):
            raise SystemExit(f"block {name}: range {first}-{last} contains other functions {inner - set(funcs)}")
        inserts.append((first - 1, START.format(name=name) + "\n"))
        inserts.append((last, END.format(name=name) + "\n"))
    for idx, text in sorted(inserts, key=lambda t: -t[0]):
        lines.insert(idx, text)
    text = "".join(lines)
    header = (f"# evolve/chassis.py -- frozen copy of {Path(src_path).name} with typed mutation blocks.\n"
              f"# source sha256 {hashlib.sha256(src.encode()).hexdigest()[:12]}. Rebuild: python3 evolve/blocks.py build\n")
    Path(out_path).write_text(header + text)
    return out_path


def extract(chassis_text):
    """name -> block source (without the marker lines)."""
    out = {}
    for name in BLOCKS:
        m = re.search(re.escape(START.format(name=name)) + r"\n(.*?)" + re.escape(END.format(name=name)), chassis_text, re.S)
        if m:
            out[name] = m.group(1)
    return out


def substitute(chassis_text, blocks):
    """Return chassis text with the given blocks replaced. Each replacement must define the same functions."""
    text = chassis_text
    for name, new_src in blocks.items():
        if name not in BLOCKS:
            raise ValueError(f"unknown block {name}")
        if not new_src.endswith("\n"):
            new_src += "\n"
        defined = {n.name for n in ast.parse(new_src).body if isinstance(n, ast.FunctionDef)}
        if set(BLOCKS[name]) - defined:
            raise ValueError(f"block {name} must define {BLOCKS[name]}, got {sorted(defined)}")
        pat = re.escape(START.format(name=name)) + r"\n.*?" + re.escape(END.format(name=name))
        repl = START.format(name=name) + "\n" + new_src + END.format(name=name)
        text, n = re.subn(pat, lambda _m: repl, text, count=1, flags=re.S)
        if n != 1:
            raise ValueError(f"block {name} markers not found")
    return text


def blocks_key(blocks):
    if not blocks:
        return ""
    return hashlib.sha256("".join(f"{k}\n{blocks[k]}" for k in sorted(blocks)).encode()).hexdigest()[:12]


def from_candidate(path, name, root=ROOT):
    """Source of block `name` (its functions, contiguous, in BLOCKS order) lifted from a plain candidate file,
    so a hand-written O-family candidate that changed only one block can seed an island or a queue item."""
    src = Path(root, path).read_text()
    src = _MARKER_RE.sub("", src)
    ranges = _func_ranges(src)
    funcs = BLOCKS[name]
    missing = [f for f in funcs if f not in ranges]
    if missing:
        raise ValueError(f"block {name}: functions not found in {path}: {missing}")
    first = ranges[funcs[0]][0]; last = ranges[funcs[-1]][1]
    inner = {f for f, (a, b) in ranges.items() if first <= a and b <= last}
    if inner != set(funcs):
        raise ValueError(f"block {name}: range in {path} contains other functions {inner - set(funcs)}")
    lines = src.splitlines(keepends=True)
    return "".join(lines[first - 1:last])


def resolve_source(value, root=ROOT):
    """Resolve inline source, a repository-relative queue reference {"path": ...}, or
    {"candidate": <file>, "block": <name>} (lift the block's functions out of a plain candidate file)."""
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, dict) and set(value) == {"candidate", "block"}:
        return from_candidate(value["candidate"], value["block"], root)
    if isinstance(value, dict) and set(value) == {"path"}:
        root = Path(root).resolve()
        path = (root / value["path"]).resolve()
        if root not in path.parents:
            raise ValueError(f"block path escapes repository: {value['path']}")
        return path.read_text()
    raise ValueError(f"invalid block source reference: {value!r}")


def resolve_sources(blocks, root=ROOT):
    if not blocks:
        return None
    return {name: resolve_source(value, root) for name, value in blocks.items()}


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "build":
        print(build())
    text = CHASSIS.read_text() if CHASSIS.exists() else ""
    for name, src in extract(text).items():
        print(f"{name:15s} {len(src.splitlines()):4d} lines  {BLOCK_DOC[name]}")
