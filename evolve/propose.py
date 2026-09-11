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
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))
import blocks as blocks_mod  # noqa: E402
import classify  # noqa: E402  (failure taxonomy, for the complexity gate)
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
   "capability": "what the agent can DO now that it could not before (not what code changed)",
   "failure_class": "EXECUTION_FAILURE",         // the evolve/classify.py class this addresses
   "scenario": "execution_overload",             // the evolve/scenarios/ diagnostic that would move
   "params": {"<param>": value, ...},            // optional, only params listed under SEARCH SPACE
   "blocks": {"<block>": "<full replacement Python source for that block>"}   // optional
  }, ...
]
Rules: every block replacement must define exactly the functions listed for that block and nothing else at
top level; use only names that already exist in the chassis; Python 3.9 syntax; no new imports. Prefer
candidates that change execution (sweep/dispatch/animal_routing/crop_admission). Each candidate must differ
from the others in mechanism, not just numbers.
`capability`, `failure_class` and `scenario` answer the complexity gate (see RULES.md). They are not
blocking -- a candidate without them is still evaluated -- but a proposal that cannot name the failure
class it addresses or the diagnostic that would detect it is, on this project's record, usually a knob
nudge wearing a mechanism's clothes."""


def log(msg):
    LOG.parent.mkdir(exist_ok=True)
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


# --------------------------------------------------------------------------- complexity gate (AGE-335)
# Five questions have to have answers before a new champion feature earns its keep (RULES.md,
# "Complexity gate"). Three of them can be checked mechanically at proposal time, cheaply:
#
#   Q2 evidence   -- does the change attach to a failure class evolve/classify.py can measure?
#   Q3 test       -- is there a diagnostic in evolve/scenarios/ that would move if it works?
#   Q4 mechanism  -- is a mechanism stated, or only an outcome?
#
# Q1 (capability) is recorded, Q5 (ablation) is a post-hoc measurement the loop makes -- the gate only
# says whether the loop *will* make it. Nothing here blocks a candidate or runs a game: it is a
# dictionary lookup over the proposal's own JSON, and the evaluator still decides.

# block -> the classify.py failure classes whose evidence metrics that block can move. Derived from
# the rules in classify.py: each class is decided by named trajectory metrics, and a block is listed
# under a class when it is on the causal path to one of those metrics.
BLOCK_FAILURE_CLASSES = {
    # _hire_plan/_load_model set the crew size that LABOR_FAILURE reads (hands/work_turns/idle_turns
    # in days 8-15) and spend cash in CAPITAL_FAILURE's day-1..8 window.
    "hiring":         ("LABOR_FAILURE", "CAPITAL_FAILURE"),
    # _demand_room sizes the herd and the crop footprint: CAPACITY_FAILURE's animals_d15/plants_final,
    # and MARKET_FAILURE's shed_units_final when sizing outruns what the town absorbs.
    "demand":         ("CAPACITY_FAILURE", "MARKET_FAILURE"),
    # economy() is the only writer of buys and sells, so it is upstream of every non-execution class.
    "economy":        ("CAPITAL_FAILURE", "MARKET_FAILURE", "TIMING_FAILURE", "LAND_FAILURE",
                       "CAPACITY_FAILURE"),
    "animal_routing": ("EXECUTION_FAILURE",),          # missed_feed, escapes
    "siting":         ("EXECUTION_FAILURE",),          # placement -> travel -> missed_feed/chore ratio
    "crop_admission": ("EXECUTION_FAILURE", "CAPACITY_FAILURE"),   # missed_water, plants_final
    "sweep":          ("EXECUTION_FAILURE",),          # missed_water, chore_completion_ratio
    "dispatch":       ("EXECUTION_FAILURE", "LABOR_FAILURE"),      # idle_turns vs work_turns
}

# block -> the diagnostic scenarios whose *deciding* metric that block moves (evolve/scenarios/).
# No scenario isolates a single block -- every verdict is downstream of several -- so this is
# "a change here can move that verdict", not "that scenario tests only this".
BLOCK_SCENARIOS = {
    "hiring":         ("idle_labor", "land_pressure", "execution_overload"),
    "demand":         ("unsupported_livestock", "land_pressure"),
    "economy":        ("unsupported_livestock", "late_expansion", "land_pressure", "idle_labor",
                       "execution_overload"),
    "animal_routing": ("execution_overload",),
    "siting":         ("execution_overload",),
    "crop_admission": ("execution_overload",),
    "sweep":          ("execution_overload",),
    "dispatch":       ("idle_labor", "execution_overload"),
}

# Scenarios that have separated real candidates, not just injected controls (AGE-333 population run,
# docs/AGE-333-scenario-suite-results.md): unsupported_livestock 3/27, land_pressure 17/13,
# execution_overload 25/5. idle_labor and late_expansion pass 30/30 of the real population and fail
# only for the lab controls, so naming one of them as a proposal's independent test is weaker
# evidence -- it cannot currently distinguish this lineage's candidates from each other.
DISCRIMINATING_SCENARIOS = ("unsupported_livestock", "land_pressure", "execution_overload")

# Mirrored from evolve/scenarios/registry.py rather than imported: the scenario package pulls in the
# tracer and the engine, and the gate must stay a dictionary lookup. tests/test_complexity_gate.py
# imports the real registry and fails if this list drifts from it.
SCENARIO_NAMES = ("unsupported_livestock", "idle_labor", "late_expansion", "land_pressure",
                  "execution_overload")

# knob/constant -> the block that reads it in the frozen chassis, or None when it is read outside every
# typed block (perception, helpers, module level). A param with no block has no failure class attached
# to it, which is exactly what Q2 is asking about. Regenerated by tests/test_complexity_gate.py, which
# re-derives this table from evolve/chassis.py and fails if the two disagree.
PARAM_BLOCK = {
    "MAX_HANDS": "hiring", "load_per_hand": "hiring", "min_hands": "hiring",
    "demand_share": "demand",
    "HERD_LAST_DAY": "economy", "MAX_SHEEP": "economy", "OPENING_MELONS": "economy",
    "early_hire_days": "economy", "feed_spare_poor": "economy", "fert_buy": "economy",
    "fert_keep": "economy", "geese": "economy", "max_animals": "economy", "melon_floor": "economy",
    "open_cows": "economy", "open_melons": "economy", "open_sheep": "economy", "open_wheat": "economy",
    "opening": "economy", "wheat_cap": "economy", "wheat_hold_days": "economy",
    "wheat_per_animal": "economy", "wheat_sell_price": "economy", "wheat_stock": "economy",
    "wheat_tiles": "economy",
    "ROUTE_LEN": "animal_routing",
    "NEAR_RADIUS": "crop_admission",
    "CROP_SWEEP_LEN": "sweep", "CROP_SWEEP_RADIUS": "sweep",
    "fert_carry": "dispatch",
}

# A note that only claims an outcome ("scores better", "+$5k") is not an answer to Q4. These are the
# words that carry a mechanism: a because, a therefore, or a verb describing what changes on the board.
_MECHANISM_MARKERS = re.compile(
    r"\b(because|since|so that|so the|therefore|instead of|rather than|which lets|which frees|"
    r"lets|frees|avoids|batch|batches|batching|defer|defers|skip|skips|reorder|reorders|merge|merges|"
    r"couples?|coupling|when |while |per |before |after )", re.I)


def _flag(question, name, target, detail, severity="flag"):
    return {"question": question, "flag": name, "target": target, "detail": detail, "severity": severity}


@lru_cache(maxsize=4)
def _default_base(name="c1"):
    """The params a proposal is a diff against. Doubles as the set of SPACE names the frozen chassis
    actually realizes: a SPACE name outside it is inert, and space.render() raises on it (AGE-336),
    so a proposal that sets one is dead on arrival. `None` if the chassis cannot be read at all."""
    try:
        return space.base_params() if name == "base" else space.c1_params()
    except Exception:  # noqa: BLE001 - the gate must never be the thing that breaks a round
        return None


@lru_cache(maxsize=4)
def _unread_param_names():
    """Params the chassis declares but never reads. render() accepts them (the name is in KNOBS, so
    AGE-336's contract check passes) and writes a file whose KNOBS literal differs, so the candidate
    gets its own key and its own dev run -- while behaving identically to its parent. A silent no-op
    scored as a real candidate, which is the one thing the render contract exists to prevent."""
    try:
        text = space.K_SRC.read_text() if space.K_SRC.exists() else blocks_mod.CHASSIS.read_text()
        m = re.search(r"^KNOBS = \{.*?\n\}\n", text, re.S | re.M)
        body = text[:m.start()] + text[m.end():] if m else text
        words = set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", body))
        return frozenset(n for n in space.SPACE if n not in words)
    except Exception:  # noqa: BLE001
        return frozenset()


def _as_list(v):
    if v is None:
        return []
    return list(v) if isinstance(v, (list, tuple)) else [v]


def complexity_check(cand, base_params=None):
    """The complexity gate (RULES.md), applied to one proposed candidate.

    Returns a list of items, each {"question", "flag", "target", "detail", "severity"}; severity
    "flag" is something missing, "info" is something recorded. Never raises, never runs a game, never
    rejects: `main()` logs the flags and queues the candidate anyway, and the evaluator decides.
    """
    items = []
    if not isinstance(cand, dict):
        return [_flag(0, "not_a_candidate", None, f"expected a dict, got {type(cand).__name__}")]

    if cand.get("kind") == "factorial":
        # a grid, not a single candidate: its axes are the targets (loop.py consumes `axes` /
        # `block_options`). The gate asks the same five questions of the grid as a whole.
        blocks = cand.get("block_options") or {}
        params = {k: (v[-1] if isinstance(v, list) and v else v)
                  for k, v in (cand.get("axes") or {}).items()} if isinstance(cand.get("axes"), dict) else {}
    else:
        blocks = cand.get("blocks") or {}
        params = cand.get("params") or {}
    if not isinstance(blocks, dict):
        items.append(_flag(0, "malformed_blocks", None, f"`blocks` is {type(blocks).__name__}, not an object"))
        blocks = {}
    if not isinstance(params, dict):
        items.append(_flag(0, "malformed_params", None, f"`params` is {type(params).__name__}, not an object"))
        params = {}
    note = (cand.get("note") or "").strip()
    base = base_params if base_params is not None else _default_base(cand.get("base") or "c1")
    live = set(base) if base is not None else None

    # ---- structural: what does this proposal actually change?
    known_blocks, changed_params = [], []
    for b in blocks:
        if b in blocks_mod.BLOCKS:
            known_blocks.append(b)
        else:
            items.append(_flag(0, "unknown_block", b,
                               f"not a mutation block; have {sorted(blocks_mod.BLOCKS)}"))
    for k, v in params.items():
        if k not in space.SPACE:
            items.append(_flag(0, "unknown_param", k, "not in space.SPACE; render() would ignore it"))
        elif live is not None and k not in live:
            items.append(_flag(0, "inert_param", k,
                               "in SPACE but not realized by the frozen chassis -- space.render() "
                               "raises on it (rebuild with `python3 evolve/blocks.py build`)"))
        elif k in _unread_param_names():
            items.append(_flag(0, "unread_param", k,
                               "declared in the chassis KNOBS but never read by any code, so setting "
                               "it renders a behaviourally identical agent under a fresh key"))
        elif base is not None and base.get(k) == v:
            items.append(_flag(0, "no_op_param", k, f"already {v!r} in the base params"))
        else:
            changed_params.append(k)
    targets = known_blocks + changed_params
    if not targets:
        items.append(_flag(0, "no_change", None, "proposal changes no known block and no live param"))

    # ---- Q1: what capability does it add?
    capability = (cand.get("capability") or "").strip()
    if capability:
        items.append(_flag(1, "capability_recorded", None, capability[:200], severity="info"))
    elif len(note) < 12:
        items.append(_flag(1, "no_capability_statement", None,
                           "neither `capability` nor a usable `note`: nothing says what the agent can "
                           "do that it could not before"))
    else:
        items.append(_flag(1, "capability_from_note", None, note[:200], severity="info"))

    # ---- Q2: what evidence shows the capability is missing?
    plausible = []
    for b in known_blocks:
        plausible += list(BLOCK_FAILURE_CLASSES.get(b, ()))
    for k in changed_params:
        blk = PARAM_BLOCK.get(k)
        if blk is None:
            items.append(_flag(2, "no_failure_evidence", k,
                               "this param is not read inside any typed block, so no classify.py "
                               "failure class is attached to it"))
        else:
            plausible += list(BLOCK_FAILURE_CLASSES.get(blk, ()))
    plausible = list(dict.fromkeys(plausible))
    declared = [str(c).strip().upper() for c in _as_list(cand.get("failure_class"))]
    if not declared:
        if targets:
            items.append(_flag(2, "no_failure_evidence", None,
                               "no `failure_class` declared; the classes these targets can move are "
                               + (", ".join(plausible) or "none")))
    else:
        for c in declared:
            if c not in classify.CLASSES:
                items.append(_flag(2, "unknown_failure_class", c,
                                   f"not a classify.py class; have {', '.join(classify.CLASSES)}"))
            elif plausible and c not in plausible:
                items.append(_flag(2, "failure_class_mismatch", c,
                                   f"{c} is not on the causal path of {', '.join(targets)} "
                                   f"(those move {', '.join(plausible)})"))
            else:
                items.append(_flag(2, "failure_class", c, f"addressed via {', '.join(targets)}",
                                   severity="info"))

    # ---- Q3: can we test the capability independently?
    suggested = []
    for b in known_blocks:
        suggested += list(BLOCK_SCENARIOS.get(b, ()))
    for k in changed_params:
        suggested += list(BLOCK_SCENARIOS.get(PARAM_BLOCK.get(k), ()))
    suggested = list(dict.fromkeys(suggested))
    named = [str(s).strip() for s in _as_list(cand.get("scenario"))]
    if not named:
        if targets:
            items.append(_flag(3, "no_independent_test", None,
                               "no `scenario` named; scenarios these targets can move: "
                               + (", ".join(suggested) or "none")))
    else:
        for s in named:
            if s not in SCENARIO_NAMES:
                items.append(_flag(3, "unknown_scenario", s,
                                   f"not a diagnostic scenario; have {', '.join(SCENARIO_NAMES)}"))
            elif suggested and s not in suggested:
                items.append(_flag(3, "scenario_mismatch", s,
                                   f"{s}'s deciding metric is not downstream of {', '.join(targets)} "
                                   f"(try {', '.join(suggested)})"))
            elif s not in DISCRIMINATING_SCENARIOS:
                items.append(_flag(3, "test_does_not_discriminate", s,
                                   f"{s} passes 30/30 of the real population (AGE-333) and fails only "
                                   "for injected controls, so it cannot currently separate candidates"))
            else:
                items.append(_flag(3, "independent_test", s, "deciding metric is movable from "
                                   + ", ".join(targets), severity="info"))

    # ---- Q4: can we explain the mechanism?
    if not note:
        items.append(_flag(4, "mechanism_not_explained", None, "empty `note`"))
    else:
        items.append(_flag(4, "mechanism_recorded", None, note[:200], severity="info"))
        if not _MECHANISM_MARKERS.search(note):
            items.append(_flag(4, "mechanism_not_explained", None,
                               "the note states an outcome, not a mechanism: no causal clause "
                               f"({note[:120]!r})"))

    # ---- Q5: does it survive ablation? (a measurement, not a claim -- say whether the loop will make it)
    n = len(targets)
    if n == 1:
        items.append(_flag(5, "ablation_is_the_dev_margin", targets[0],
                           "single change: loop.ablate() skips it (needs >= 2), and its dev margin "
                           "vs the parent already is the ablation", severity="info"))
    elif n > 8:
        items.append(_flag(5, "ablation_will_be_skipped", None,
                           f"{n} changes vs the base; loop.ablate() only ablates 2-8, so no per-change "
                           "contribution will be measured"))
    elif n >= 2:
        items.append(_flag(5, "ablation_planned", None,
                           f"{n} changes: loop.ablate() will revert each one at the dev stage if this "
                           "candidate passes held-out", severity="info"))
    return items


def gate_summary(items):
    """One line for the log: the flags only, in question order."""
    flags = [i for i in items if i["severity"] == "flag"]
    if not flags:
        return "gate: clean"
    return "gate: " + "; ".join(
        f"Q{i['question']} {i['flag']}" + (f"[{i['target']}]" if i["target"] else "") for i in flags)


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
        "param_exploration_top10": archive.get("param_exploration", [])[:10],
        "recent_dead": archive.get("recent_dead", [])[:12],
        "failure_observations": archive.get("failure_observations", [])[:5],
    }, indent=0, default=str))
    parts.append("# EPISTEMIC FRAMING (read this before interpreting the archive)\n"
                 "\"param_exploration\" is OBSERVED OUTCOME VARIATION, not causal importance or parameter sensitivity.\n"
                 "A parameter with high spread may appear important because of interactions with companion parameters,\n"
                 "seed/matchup variance, a few outlier candidates, selection bias, or because it was tested in more\n"
                 "diverse contexts. The per-value sample counts (n=) tell you how much data supports each mean.\n"
                 "n<5 is fragile; n>=30 is moderate confidence. Uneven sampling (high balance value) means the\n"
                 "apparent spread may just reflect the better-sampled value having more chances to find an outlier.\n"
                 "\n"
                 "\"failure_observations\" groups recent dead candidates by failure class and lists parameter ranges\n"
                 "frequently seen in those failures. These are CORRELATIONS, not established causes. A parameter\n"
                 "appearing in a failure group may be part of the failure mechanism, or it may be confounded by the\n"
                 "companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not\n"
                 "interpret these as 'avoid this parameter range.'\n"
                 "\n"
                 "\"recent_dead\" is the last 12 dead candidates at the individual level — the most granular signal.\n"
                 "Each entry has its own status, diagnosis, and smoke_margin. Use these to understand specific failure\n"
                 "modes, not to derive global parameter penalties.\n"
                 "\n"
                 "None of these signals should be used to automatically down-weight or avoid parameter values.\n"
                 "They are observational context for the proposer, not search-policy inputs.")
    parts.append("# CLOSED MECHANISMS (do not re-propose)\n" + json.dumps(
        rejected_mechanisms or [], indent=0, default=str))
    try:
        import directions as _dir
        _rows = _dir.load()
        parts.append("# RESEARCH-DIRECTION LEDGER (evolve/directions.yaml; AGE-361). A proposal must name which DELAY it "
                     "resolves or which self-model question it corrects (docs/economic-self-model.md); do not re-propose an "
                     "ABANDON at its stated scope without a new instrument.\n" + _dir.render(_rows))
        parts.append("# EVIDENCE CONTRACT (AGE-362): minimum depth before a direction may be promoted or closed\n" + _dir.contract_text())
    except Exception as _e:  # noqa: BLE001
        parts.append(f"# RESEARCH-DIRECTION LEDGER unavailable: {_e!r}")
    try:
        import directions as _dir
        _rows = _dir.load()
        parts.append("# RESEARCH-DIRECTION LEDGER (evolve/directions.yaml; AGE-361). A proposal must name which DELAY it "
                     "resolves or which self-model question it corrects (docs/economic-self-model.md); do not re-propose an "
                     "ABANDON at its stated scope without a new instrument.\n" + _dir.render(_rows))
        parts.append("# EVIDENCE CONTRACT (AGE-362): minimum depth before a direction may be promoted or closed\n" + _dir.contract_text())
    except Exception as _e:  # noqa: BLE001
        parts.append(f"# RESEARCH-DIRECTION LEDGER unavailable: {_e!r}")
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
    cmd = [exe, "-p", "--output-format", "json", "--max-turns", "80",
           "--allowedTools", "Bash", "--permission-mode", "bypassPermissions"]
    if model:
        cmd += ["--model", model]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, cwd=str(ROOT))
    if r.returncode != 0:
        raise RuntimeError(f"claude exit {r.returncode}: stderr={r.stderr!r} stdout={r.stdout[:200]!r}")
    try:
        out = json.loads(r.stdout)
        if isinstance(out, dict) and out.get("is_error"):
            reason = out.get("terminal_reason", "?")
            msg = out.get("error", {}).get("message", out.get("result", "unknown error"))
            raise RuntimeError(f"claude API error (is_error={reason!r}): {msg[:300]}")
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


def run_gate(paths):
    """`--gate`: print the complexity gate for candidate JSON files. No LLM, no games."""
    paths = [Path(p) for p in (paths or [])] or sorted(QUEUE.glob("*.json"))
    if not paths:
        print("nothing to check (no files given and evolve/queue is empty)")
        return 1
    flagged = 0
    for path in paths:
        try:
            payload = json.loads(Path(path).read_text())
        except Exception as e:  # noqa: BLE001
            print(f"{path}: unreadable ({e!r})")
            flagged += 1
            continue
        for cand in (payload if isinstance(payload, list) else [payload]):
            items = complexity_check(cand)
            flags = [i for i in items if i["severity"] == "flag"]
            flagged += bool(flags)
            print(f"\n{path}: {gate_summary(items)}")
            for i in items:
                mark = "!" if i["severity"] == "flag" else "-"
                tgt = f" [{i['target']}]" if i["target"] else ""
                print(f"  {mark} Q{i['question']} {i['flag']}{tgt}: {i['detail']}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--blocks", nargs="*", default=None, help="blocks to expose this round (default: 2 random execution blocks)")
    ap.add_argument("--model", default=None)
    ap.add_argument("--min-interval", type=float, default=1800, help="seconds between rounds unless --force")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--gate", nargs="*", metavar="FILE",
                    help="run the complexity gate (RULES.md) over candidate JSON files and exit; "
                         "reads a queue item, a proposal object, or an array of them")
    args = ap.parse_args()

    if args.gate is not None:
        return run_gate(args.gate)

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
        gate = complexity_check(c)
        ok, why = validate(c, chassis_text)
        note = (c.get("note") or "")[:200]
        if not ok:
            log(f"  reject #{i}: {why} :: {note}")
            log(f"    {gate_summary(gate)}")
            continue
        item = {"kind": "candidate", "base": c.get("base", "c1"), "params": c.get("params") or {},
                "blocks": c.get("blocks") or {}, "origin": "llm", "island": "queue", "note": note,
                "capability": (c.get("capability") or "")[:300] or None,
                "failure_class": c.get("failure_class"), "scenario": c.get("scenario"),
                "complexity_flags": gate}
        (QUEUE / f"llm_{stamp}_{i}.json").write_text(json.dumps(item))
        kept += 1
        log(f"  queued #{i}: {why} :: {note}")
        log(f"    {gate_summary(gate)}")
    state["last"] = time.time()
    state["rounds"] = state.get("rounds", 0) + 1
    state["queued_total"] = state.get("queued_total", 0) + kept
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state))
    log(f"round done: {kept}/{len(cands)} candidates queued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
