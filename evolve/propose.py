#!/usr/bin/env python3
"""LLM candidate generator: reads the archive, asks Claude (via the Claude Code CLI, i.e. Grace's
subscription login) for materially different candidates, validates them, and drops them in the queue.

    python3 evolve/propose.py                 # one proposal round (rate-limited; see --min-interval)
    python3 evolve/propose.py --dry-run       # print the prompt, call nothing
    python3 evolve/propose.py --blocks sweep dispatch --n 6 --force

Requires `claude` on PATH (native install: curl -fsSL https://claude.ai/install.sh | bash) and a
one-time interactive `claude` login on this machine. Uses `claude -p --output-format json`.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))
import blocks as blocks_mod  # noqa: E402
import space  # noqa: E402
from db import DB  # noqa: E402

ARCHIVE = HERE / "archive.json"
RULES = HERE / "RULES.md"
QUEUE = HERE / "queue"
STATE = HERE / "logs" / "propose_state.json"
LOG = HERE / "logs" / "propose.log"

SCHEMA_DOC = """Return ONLY a JSON array (no prose, no code fences) of candidate objects:
[
  {"note": "one line: the mechanism and why it should help",
   "base": "c1",
   "params": {"<param>": value, ...},            // optional, only params listed under SEARCH SPACE
   "blocks": {"<block>": "<full replacement Python source for that block>"}   // optional
  }, ...
]
Rules: every block replacement must define exactly the functions listed for that block and nothing else at
top level; use only names that already exist in the chassis; Python 3.9 syntax; no new imports. Prefer
candidates that change execution (sweep/dispatch/animal_routing/crop_admission). Each candidate must differ
from the others in mechanism, not just numbers."""


def log(msg):
    LOG.parent.mkdir(exist_ok=True)
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def build_prompt(block_names, n, archive, chassis_text, rejected_mechanisms=None):
    blk = blocks_mod.extract(chassis_text)
    parts = []
    parts.append("You are the candidate generator inside an AlphaEvolve-style loop for a Kaggle farming-simulation agent. "
                 "An exact simulator evaluates every candidate you propose (paired, both seats, vs the current frontier). "
                 "Your job is volume and diversity of *mechanisms*; the evaluator decides what is good.\n")
    parts.append("# CONSTITUTION\n" + RULES.read_text())
    if archive.get("frontier_gap") and archive["frontier_gap"].get("text"):
        fg = archive["frontier_gap"]
        parts.append("# EXECUTION GAP TO THE LADDER FRONTIER (process trace, seed 1)\n" + fg["text"] +
                     "\nC1 execution: " + json.dumps(fg.get("c1")) + "\nfrontier tape execution: " + json.dumps(fg.get("tape")) +
                     "\n(travel_per_task = move turns per work action; missed_feed = animal-days unfed; feed_hour/water_hour = mean hour of first service)")
    parts.append("# CURRENT ARCHIVE (machine summary)\n" + json.dumps({
        "frontier": archive.get("frontier"), "clone": archive.get("clone"),
        "counts_all_runs": archive.get("counts_all_runs"),
        "held_out_top": archive.get("held_out", [])[:8],
        "islands_top3": {k: v[:3] for k, v in archive.get("islands", {}).items()},
        "param_importance_top10": archive.get("param_importance", [])[:10],
        "recent_dead": archive.get("recent_dead", [])[:12],
    }, indent=0, default=str))
    parts.append("# CLOSED MECHANISMS (do not re-propose)\n" + json.dumps(
        rejected_mechanisms or [], indent=0, default=str))
    parts.append("# SEARCH SPACE (params you may set)\n" + json.dumps(
        {k: (v[1] if v[0] == "cat" else [v[1], v[2]]) for k, v in space.SPACE.items()}))
    parts.append("# BLOCKS YOU MAY REPLACE (current source)\n")
    for b in block_names:
        parts.append(f"## block `{b}` — {blocks_mod.BLOCK_DOC[b]}\nfunctions: {blocks_mod.BLOCKS[b]}\n```python\n{blk[b]}```\n")
    helpers = [n for n in ("_dist", "_step", "_shed_dist", "_water_needed", "_harvest_ready", "_fert_eligible", "_nearest", "_animal_pending", "S", "KNOBS")]
    parts.append("Helper names available in the chassis (do not redefine): " + ", ".join(helpers) +
                 ". `S` is the per-day state dict; `KNOBS` the knob dict; `v` is the perception dict "
                 "(keys: tiles, empty, urgent, water, wwater, harvest, fert, weeds, slack, animals, shed_tiles, positions).")
    parts.append(f"# TASK\nPropose {n} candidates. At least {max(1, n - 2)} must replace one of the blocks above; the rest may be "
                 "param-only if the archive evidence suggests a specific untested combination.\n" + SCHEMA_DOC)
    return "\n\n".join(parts)


def call_claude(prompt, model=None, timeout=900):
    exe = shutil.which("claude") or str(Path.home() / ".local" / "bin" / "claude")
    cmd = [exe, "-p", "--output-format", "json", "--max-turns", "5",
           "--allowedTools", "Bash", "--permission-mode", "bypassPermissions"]
    if model:
        cmd += ["--model", model]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, cwd=str(ROOT))
    if r.returncode != 0:
        raise RuntimeError(f"claude exit {r.returncode}: {r.stderr[:500]}")
    try:
        out = json.loads(r.stdout)
        text = out.get("result") if isinstance(out, dict) else r.stdout
    except json.JSONDecodeError:
        text = r.stdout
    return text or ""


def parse_candidates(text):
    text = text.strip()
    m = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", text, re.S)
    if m:
        text = m.group(1)
    start = text.find("[")
    end = text.rfind("]")
    if start < 0 or end < 0:
        raise ValueError("no JSON array in response")
    return json.loads(text[start:end + 1])


def validate(cand, chassis_text):
    """Render, compile, and play one game. Returns (ok, reason)."""
    import mini_engine as me  # noqa: E402 (repo root on sys.path)
    base = space.c1_params() if cand.get("base", "c1") == "c1" else space.base_params()
    params = dict(base)
    for k, v in (cand.get("params") or {}).items():
        if k in space.SPACE:
            params[k] = space.clamp(k, v)
    blocks = cand.get("blocks") or None
    if blocks:
        for b in blocks:
            if b not in blocks_mod.BLOCKS:
                return False, f"unknown block {b}"
    try:
        path = space.render(params, blocks)
        compile(path.read_text(), str(path), "exec")
    except Exception as e:  # noqa: BLE001
        return False, f"render/compile: {e!r}"[:200]
    try:
        r = me.run_game(str(path), str(ROOT / "candidates" / "V3_12.py"), seed=1, engine="master")
    except Exception as e:  # noqa: BLE001
        return False, f"game crashed: {e!r}"[:200]
    if r["errors"][0] > 0:
        return False, f"{r['errors'][0]} agent errors in a test game"
    return True, f"test game money {r['money'][0]:,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--blocks", nargs="*", default=None, help="blocks to expose this round (default: 2 random execution blocks)")
    ap.add_argument("--model", default=None)
    ap.add_argument("--min-interval", type=float, default=1800, help="seconds between rounds unless --force")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    if not args.force and not args.dry_run and time.time() - state.get("last", 0) < args.min_interval:
        print("rate-limited; use --force")
        return 0
    if not ARCHIVE.exists():
        print("no archive.json yet (run the loop once)")
        return 1
    archive = json.loads(ARCHIVE.read_text())
    snap, _ = space.freeze_base()
    chassis_text = snap.read_text()
    rng = random.Random()
    pool = ["sweep", "dispatch", "animal_routing", "crop_admission", "siting", "hiring", "demand"]
    block_names = args.blocks or rng.sample(pool[:4], 1) + rng.sample(pool, 1)
    block_names = list(dict.fromkeys(block_names))
    prompt = build_prompt(block_names, args.n, archive, chassis_text, DB().rejected_mechanisms())
    if args.dry_run:
        print(prompt)
        return 0

    log(f"round: blocks={block_names} n={args.n} prompt={len(prompt)} chars")
    try:
        text = call_claude(prompt, args.model)
        cands = parse_candidates(text)
    except Exception as e:  # noqa: BLE001
        log(f"FAILED: {e!r}"[:300])
        state["last"] = time.time()
        STATE.parent.mkdir(exist_ok=True)
        STATE.write_text(json.dumps(state))
        return 1
    QUEUE.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    kept = 0
    for i, c in enumerate(cands):
        if not isinstance(c, dict):
            continue
        ok, why = validate(c, chassis_text)
        note = (c.get("note") or "")[:200]
        if not ok:
            log(f"  reject #{i}: {why} :: {note}")
            continue
        item = {"kind": "candidate", "base": c.get("base", "c1"), "params": c.get("params") or {},
                "blocks": c.get("blocks") or {}, "origin": "llm", "island": "queue", "note": note}
        (QUEUE / f"llm_{stamp}_{i}.json").write_text(json.dumps(item))
        kept += 1
        log(f"  queued #{i}: {why} :: {note}")
    state["last"] = time.time()
    state["rounds"] = state.get("rounds", 0) + 1
    state["queued_total"] = state.get("queued_total", 0) + kept
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state))
    log(f"round done: {kept}/{len(cands)} candidates queued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
