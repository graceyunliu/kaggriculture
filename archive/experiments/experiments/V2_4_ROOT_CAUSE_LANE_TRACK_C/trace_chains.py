"""V2.4 Track C: production-chain bottleneck tracing.

Diagnostic-only, non-controlling instrumentation of the frozen V10.6
self-contained oracle. Never modifies the returned actions -- only
appends observations to a module-level diagnostic list that the caller
clears/reads each turn, exactly the pattern used in V2_3O Track C's
characterize.py and V2_3S Track B.

Captures, per turn, real (not simulated) online-decision-point signals:
  - tier task-pool sizes BEFORE this turn's crop dispatch (demand)
  - tier task-pool sizes AFTER this turn's crop dispatch (leftover ==
    tasks that existed and had no worker assigned to them this turn --
    a directly observed worker/capacity blocker, Evidence A)
  - animal_plans stage snapshot (purchase/setup pipeline)
  - the market list issued this turn (sale events)

State needed for crop-tile lifecycle reconstruction (kind/crop/
planted_day/yield_units/watered_today/consecutive_unwatered/animal on
pasture) is read directly from the unmodified raw observation returned
by the kaggle_environments step -- no instrumentation of main.py is
needed for that part, since obs already carries it every turn.
"""
from __future__ import annotations
import hashlib, importlib.util, json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V10_6 = ROOT / "experiments/V2_3B_V10_6_SELF_CONTAINED/candidate/main.py"
V9_3 = ROOT / "experiments/V2_3B_V9_3_SELF_CONTAINED/candidate/main.py"
OUT_JSON = ROOT / "artifacts/v2_4_root_cause/production_chain_bottlenecks.json"
SEEDS = (920, 921, 922, 923)


def instrument(src: str) -> str:
    src = src.replace("import sys\n", "import sys\n_CHAIN_DIAG=[]\n", 1)

    # Snapshot tier demand right after the crop task pool is assembled
    # and filtered against claimed animal-build sites -- this is the
    # exact pool the dispatch below will try to clear this turn.
    old = (
        '    if excluded:\n'
        '        tasks["plant"] = [t for t in tasks["plant"] if t not in excluded]\n'
    )
    new = old + (
        '    _chain_demand = {k: list(v) for k, v in tasks.items()}\n'
    )
    assert src.count(old) == 1
    src = src.replace(old, new)

    # Snapshot animal_plans pipeline state at the same point (post
    # reconcile/confirm, pre this-turn dispatch) -- purchase/setup stage
    # for every in-flight animal.
    old2 = (
        '    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans)\n'
    )
    new2 = (
        '    _chain_plans_before = [dict(p) for p in animal_plans]\n'
        + old2
    )
    assert src.count(old2) == 1
    src = src.replace(old2, new2)

    # Final snapshot: leftover tier pools after all crop dispatch, plus
    # animal_plans after this turn's dispatch/reconcile, plus the
    # returned market list -- appended right before the function return.
    old3 = '    return {"farmer": farmer_op, "hands": hand_ops, "market": market}\n'
    new3 = (
        '    _chain_leftover = {k: list(v) for k, v in tasks.items()}\n'
        '    _CHAIN_DIAG.append({\n'
        '        "day": day, "hour": hour,\n'
        '        "demand": _chain_demand, "leftover": _chain_leftover,\n'
        '        "plans_before": _chain_plans_before,\n'
        '        "plans_after": [dict(p) for p in animal_plans],\n'
        '        "market": list(market),\n'
        '        "n_hands": len(me["hands"]),\n'
        '        "farmer_pos": list(farmer_pos), "hand_pos": [list(h) for h in me["hands"]],\n'
        '        "seeds": dict(seeds), "shed": dict(shed),\n'
        '    })\n'
        + old3
    )
    assert src.count(old3) == 1
    return src.replace(old3, new3)


RUN_CODE = r'''
import hashlib, importlib, json, sys
from kaggle_environments import make

p = json.load(sys.stdin)
m = importlib.import_module("main")
actions = []
obs_log = []

def agent(obs, cfg):
    m._CHAIN_DIAG.clear()
    a = m.agent(obs, cfg)
    actions.append(a)
    for d in m._CHAIN_DIAG:
        d2 = dict(d, step=obs["step"])
        obs_log.append(d2)
    return a

def noop(obs, cfg):
    return {"farmer": ["PASS"], "hands": [], "market": []}

e = make("kaggriculture", configuration={"seed": p["seed"]}, debug=False)
e.run([agent, noop])

# Raw per-step observation snapshot for player 0 -- unmodified, direct
# from the environment, used for crop-tile / pasture-animal state
# reconstruction (no reliance on any instrumentation for this part).
raw_obs = []
for step in e.steps:
    o = step[0]["observation"]
    if "farms" not in o:
        continue
    raw_obs.append({
        "step": o.get("step"), "day": o.get("day"), "hour": o.get("hour"),
        "tiles": o["farms"][o["player"]]["tiles"],
        "farmer": o["farms"][o["player"]]["farmer"],
        "hands": o["farms"][o["player"]]["hands"],
    })

action_hash = hashlib.sha256(json.dumps(actions, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
out = {
    "seed": p["seed"],
    "cash": e.steps[-1][0]["reward"],
    "turns": len(actions),
    "action_hash": action_hash,
    "diag": obs_log,
    "raw_obs": raw_obs,
}
print(json.dumps(out, sort_keys=True))
'''

CONTROL_CODE = r'''
import hashlib, importlib, json, sys
from kaggle_environments import make
p = json.load(sys.stdin)
m = importlib.import_module("main")
actions = []
def agent(obs, cfg):
    a = m.agent(obs, cfg)
    actions.append(a)
    return a
def noop(obs, cfg):
    return {"farmer": ["PASS"], "hands": [], "market": []}
e = make("kaggriculture", configuration={"seed": p["seed"]}, debug=False)
e.run([agent, noop])
action_hash = hashlib.sha256(json.dumps(actions, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print(json.dumps({"seed": p["seed"], "cash": e.steps[-1][0]["reward"], "turns": len(actions), "action_hash": action_hash}, sort_keys=True))
'''


def run(python_exe, cwd, seed, code):
    env = dict(os.environ)
    env["PYTHONPATH"] = str(cwd)
    cp = subprocess.run([python_exe, "-c", code], input=json.dumps({"seed": seed}),
                         text=True, capture_output=True, env=env, timeout=600)
    if cp.returncode != 0:
        raise RuntimeError(cp.stdout + "\n" + cp.stderr)
    lines = [x for x in cp.stdout.splitlines() if x.startswith("{")]
    return json.loads(lines[-1])


def main():
    python_exe = sys.argv[1] if len(sys.argv) > 1 else sys.executable
    before_v106 = hashlib.sha256(V10_6.read_bytes()).hexdigest()
    before_v93 = hashlib.sha256(V9_3.read_bytes()).hexdigest()

    with tempfile.TemporaryDirectory(prefix="v24-track-c-") as d:
        p = Path(d)
        (p / "main.py").write_text(instrument(V10_6.read_text()))

        controls = [run(python_exe, V10_6.parent, s, CONTROL_CODE) for s in SEEDS]
        diag_runs = [run(python_exe, p, s, RUN_CODE) for s in SEEDS]
        diag_runs_rerun = [run(python_exe, p, s, RUN_CODE) for s in SEEDS]

    after_v106 = hashlib.sha256(V10_6.read_bytes()).hexdigest()
    after_v93 = hashlib.sha256(V9_3.read_bytes()).hexdigest()

    equivalence = {
        "exact_actions": all(a["action_hash"] == b["action_hash"] for a, b in zip(controls, diag_runs)),
        "exact_terminal_cash": all(a["cash"] == b["cash"] for a, b in zip(controls, diag_runs)),
        "deterministic_rerun": all(
            (a["action_hash"], a["cash"]) == (b["action_hash"], b["cash"])
            for a, b in zip(diag_runs, diag_runs_rerun)
        ),
        "v10_6_hash_unchanged": before_v106 == after_v106 == "f6abd7f066685bf43a797d468b0694eefa15956375850e68b8f76174d45c907e",
        "v9_3_hash_unchanged": before_v93 == after_v93 == "9d2703faf8e58c55697dc3948d06c3a1f4caac52927a38358e131d9b0344bf0b",
    }

    out_dir = ROOT / "artifacts/v2_4_root_cause"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "raw_diag_runs.json").write_text(json.dumps(diag_runs, sort_keys=True))
    (out_dir / "controls.json").write_text(json.dumps(controls, indent=2, sort_keys=True))
    (out_dir / "equivalence.json").write_text(json.dumps(equivalence, indent=2, sort_keys=True))
    print(json.dumps(equivalence, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
