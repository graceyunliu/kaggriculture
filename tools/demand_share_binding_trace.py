#!/usr/bin/env python3
"""DEMAND_SHARE Layer-1 (binding) + local Layer-2 (sensitivity) PILOT trace.

Per kaggriculture-research-sequence-sep11-v2.md: this is the PILOT step only -- verifies
instrumentation and event population on a small sample. It does NOT promote DEMAND_SHARE
past Layer 1 on its own; that requires the full standard population (4 tapes x both seats x
2x20-seed sets x full horizon) per the pre-registered sampling standard.

WHAT THIS MEASURES
-------------------
candidates/O26_CARROT_SIZING.py line 579 sizes the crop seed-buy pool for each candidate crop c
in the BUY_SEED loop inside economy():
    pool = DEMAND_SHARE * (max(0, I0-inv_c) + cushion_left + _daily_demand(...)*(29-day))
    room_units = pool - committed[c] - seed_orders.get(c,0)*sp_["units"]
    if room_units < sp_["units"] * 0.5: <skip this crop this iteration>   # GATE
    ...
    k = min(space, int(room_units // sp_["units"]), int(free // sp_["seed"]), 20)  # SIZING CAP

DEMAND_SHARE can matter in two distinct ways, both logged separately (never collapsed):
  GATE:   room_units < sp_["units"]*0.5 -> crop c is excluded from consideration this
          iteration solely because of a demand-room shortfall.
  SIZING: room_units//units is the strictly tightest of the four terms in the k=min(...) call
          for whichever crop wins selection -- i.e. DEMAND_SHARE, not space/cash/the hardcoded
          20 cap, actually determines how many seeds get bought.

METHOD (non-invasive, no reimplementation of the real decision)
-----------------------------------------------------------------
sys.settrace is used to snapshot economy()'s own local variables at the exact source lines
where pool/room_units/k are computed, DURING the real, single, unmodified call to economy()
that the game actually uses to decide -- no monkeypatching of economy() itself, no second
"shadow" call (economy() mutates module-global S, so calling it twice per turn would corrupt
the real game trajectory -- avoided entirely here).

From the captured locals we algebraically recover the same-turn, same-trajectory counterfactual:
    X = pool / DEMAND_SHARE                         (DEMAND_SHARE is 0.5 for every capture)
    room_units_alt = alt_share * X - committed[c] - seed_orders.get(c,0)*sp_["units"]
This is a LOCAL counterfactual (holds the trajectory up to this decision fixed) -- it is NOT a
full alternate-timeline rerun. A full Layer-2 measurement (rerunning entire games with
DEMAND_SHARE permanently changed) is a separate, later step; flagged here as a known pilot
limitation, not silently conflated with it.

alt_share is NOT auto-picked to make 0.5 "look wrong" -- it's read from --alt-share and must be
justified by the caller (per governance: the alternative estimator must be explicitly justified
before being used to declare 0.5 wrong; this pilot does not itself supply that justification).

Usage:
  KAGG_FIXED_SHOPS=1 python3 demand_share_binding_trace.py --opp bahaen --seeds 71,72 --alt-share 0.35
"""
import sys, os, argparse, json, collections, importlib.util

ROOT = os.environ.get("KAGG_ROOT", os.path.expanduser("~/mnt/Kaggriculture"))
sys.path.insert(0, ROOT)
import mini_engine as me  # noqa: E402

CAND_PATH = os.path.join(ROOT, "candidates/O26_CARROT_SIZING.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}

PHASES = [("early", 0, 9), ("mid", 10, 19), ("late", 20, 29)]


def phase_of(day):
    for name, lo, hi in PHASES:
        if lo <= day <= hi:
            return name
    return "late"


def load_cand():
    spec = importlib.util.spec_from_file_location(f"cand_{id(object())}", CAND_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class BindingTracer:
    """sys.settrace-based capture of economy()'s locals at the two decision lines."""

    def __init__(self, mod, alt_share, log):
        self.mod = mod
        self.alt_share = alt_share
        self.log = log
        self.economy_code = mod.economy.__code__
        # line numbers inside candidates/O26_CARROT_SIZING.py -- re-derive at load time so a
        # future source edit that shifts lines fails loudly instead of silently mis-capturing.
        src_lines, start = __import__("inspect").getsourcelines(mod.economy)
        self.gate_lineno = None
        self.sizing_lineno = None
        for i, line in enumerate(src_lines):
            if "if room_units < sp_[" in line and self.gate_lineno is None:
                self.gate_lineno = start + i
            if "k = min(space, int(room_units //" in line and self.sizing_lineno is None:
                self.sizing_lineno = start + i
        assert self.gate_lineno and self.sizing_lineno, "instrumentation target lines not found -- source has drifted, update this script"

    def _tracer(self, frame, event, arg):
        if frame.f_code is not self.economy_code:
            return None
        if event == "line":
            lineno = frame.f_lineno
            if lineno == self.gate_lineno:
                self._capture_gate(frame)
            elif lineno == self.sizing_lineno:
                self._capture_sizing(frame)
            return self._tracer
        return self._tracer

    def _capture_gate(self, frame):
        f = frame.f_locals
        day = f.get("day"); c = f.get("c"); sp_ = f.get("sp_")
        pool = f.get("pool"); room_units = f.get("room_units")
        committed = f.get("committed", {}); seed_orders = f.get("seed_orders", {})
        if day is None or c is None or sp_ is None:
            return
        DEMAND_SHARE = self.mod.DEMAND_SHARE
        X = pool / DEMAND_SHARE if DEMAND_SHARE else 0.0
        room_alt = self.alt_share * X - committed.get(c, 0) - seed_orders.get(c, 0) * sp_["units"]
        gated_baseline = room_units < sp_["units"] * 0.5
        gated_alt = room_alt < sp_["units"] * 0.5
        ph = phase_of(day)
        self.log["gate_eligible"][(c, ph)] += 1
        if gated_baseline:
            self.log["gate_excluded_baseline"][(c, ph)] += 1
        if gated_baseline != gated_alt:
            self.log["gate_flips_under_alt"][(c, ph)] += 1

    def _capture_sizing(self, frame):
        f = frame.f_locals
        day = f.get("day"); c = f.get("c"); sp_ = f.get("sp_")
        room_units = f.get("room_units"); space = f.get("space")
        free = f.get("free"); pool = None
        committed = f.get("committed", {}); seed_orders = f.get("seed_orders", {})
        if day is None or c is None or sp_ is None:
            return
        units = sp_["units"]; seed_price = sp_["seed"]
        terms = {
            "demand_room": int(room_units // units),
            "space": space,
            "cash": int(free // seed_price),
            "hardcap20": 20,
        }
        k_actual = min(terms.values())
        binder = min(terms, key=lambda k_: terms[k_])
        ph = phase_of(day)
        self.log["sizing_eligible"][(c, ph)] += 1
        if binder == "demand_room":
            self.log["sizing_bound_by_demand"][(c, ph)] += 1
        # local counterfactual sizing under alt_share, recovering X the same way as the gate capture
        DEMAND_SHARE = self.mod.DEMAND_SHARE
        pool_baseline = DEMAND_SHARE * (room_units + committed.get(c, 0) + seed_orders.get(c, 0) * units) / DEMAND_SHARE if False else None
        # room_units already = pool - committed - seed_orders*units, and pool = DEMAND_SHARE * X
        # -> X = (room_units + committed[c] + seed_orders.get(c,0)*units) / DEMAND_SHARE
        X = (room_units + committed.get(c, 0) + seed_orders.get(c, 0) * units) / DEMAND_SHARE if DEMAND_SHARE else 0.0
        room_alt = self.alt_share * X - committed.get(c, 0) - seed_orders.get(c, 0) * units
        k_alt = min(int(room_alt // units) if room_alt > 0 else 0, terms["space"], terms["cash"], 20)
        if k_alt != k_actual:
            self.log["sizing_material_diff"][(c, ph)].append(k_alt - k_actual)


def run_game(mod, opp_path, seed, cand_seat, tracer):
    engine_mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    opp_agent = me.load_agent(opp_path)

    def cand_agent(obs, configuration):
        sys.settrace(tracer._tracer)
        try:
            return mod.agent(obs, configuration)
        except Exception:
            return {}
        finally:
            sys.settrace(None)

    agents = [None, None]
    agents[cand_seat] = cand_agent
    agents[1 - cand_seat] = opp_agent
    state = me.structify(
        [{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
          "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)]
    )
    state = engine_mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = engine_mod.interpreter(state, env); step += 1
        for s in state:
            s.observation.step = step
        if state[0].status != "ACTIVE" or step >= steps:
            break


def parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-"); out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def new_log():
    return {
        "gate_eligible": collections.Counter(),
        "gate_excluded_baseline": collections.Counter(),
        "gate_flips_under_alt": collections.Counter(),
        "sizing_eligible": collections.Counter(),
        "sizing_bound_by_demand": collections.Counter(),
        "sizing_material_diff": collections.defaultdict(list),
        "n_games": 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--opp", required=True, choices=list(OPPS))
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--alt-share", type=float, required=True,
                     help="Alternative DEMAND_SHARE for the local counterfactual. Caller must justify this value; the script does not choose it.")
    ap.add_argument("--json")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    opp_path = OPPS[args.opp]
    log = new_log()

    for seed in seeds:
        for cand_seat in (0, 1):
            mod = load_cand()
            tracer = BindingTracer(mod, args.alt_share, log)
            run_game(mod, opp_path, seed, cand_seat, tracer)
            log["n_games"] += 1

    print(f"PILOT -- opp={args.opp} seeds={args.seeds} alt_share={args.alt_share} n_games={log['n_games']}")
    print("(pilot only -- does not promote DEMAND_SHARE past Layer 1; verifies instrumentation)\n")

    crops = sorted({c for c, _ in log["gate_eligible"]} | {c for c, _ in log["sizing_eligible"]})

    print("== LAYER 1a: GATE (crop excluded from consideration this iteration by demand-room shortfall) ==")
    print(f"{'crop':10s} {'phase':6s} {'eligible':>9s} {'excluded':>9s} {'excl_rate':>10s} {'flips_under_alt':>16s}")
    for c in crops:
        for ph, _, _ in PHASES:
            elig = log["gate_eligible"][(c, ph)]
            if not elig:
                continue
            exc = log["gate_excluded_baseline"][(c, ph)]
            flips = log["gate_flips_under_alt"][(c, ph)]
            print(f"{c:10s} {ph:6s} {elig:9d} {exc:9d} {exc/elig:10.2%} {flips:16d}")

    print("\n== LAYER 1b: SIZING (was demand-room the strictest of the four caps on k?) ==")
    print(f"{'crop':10s} {'phase':6s} {'eligible':>9s} {'demand_bound':>13s} {'bound_rate':>11s}")
    for c in crops:
        for ph, _, _ in PHASES:
            elig = log["sizing_eligible"][(c, ph)]
            if not elig:
                continue
            bound = log["sizing_bound_by_demand"][(c, ph)]
            print(f"{c:10s} {ph:6s} {elig:9d} {bound:13d} {bound/elig:11.2%}")

    print("\n== LOCAL LAYER 2: counterfactual k delta under alt_share (same trajectory, single-decision) ==")
    print(f"{'crop':10s} {'phase':6s} {'n_diffs':>8s} {'mean_delta_k':>13s} {'max_abs_delta':>14s}")
    for c in crops:
        for ph, _, _ in PHASES:
            diffs = log["sizing_material_diff"][(c, ph)]
            if not diffs:
                continue
            mean_d = sum(diffs) / len(diffs)
            max_abs = max(abs(d) for d in diffs)
            print(f"{c:10s} {ph:6s} {len(diffs):8d} {mean_d:13.2f} {max_abs:14d}")

    if args.json:
        out = {
            "opp": args.opp, "seeds": args.seeds, "alt_share": args.alt_share, "n_games": log["n_games"],
            "gate_eligible": {f"{c}|{p}": v for (c, p), v in log["gate_eligible"].items()},
            "gate_excluded_baseline": {f"{c}|{p}": v for (c, p), v in log["gate_excluded_baseline"].items()},
            "gate_flips_under_alt": {f"{c}|{p}": v for (c, p), v in log["gate_flips_under_alt"].items()},
            "sizing_eligible": {f"{c}|{p}": v for (c, p), v in log["sizing_eligible"].items()},
            "sizing_bound_by_demand": {f"{c}|{p}": v for (c, p), v in log["sizing_bound_by_demand"].items()},
            "sizing_material_diff": {f"{c}|{p}": v for (c, p), v in log["sizing_material_diff"].items()},
        }
        with open(args.json, "w") as fh:
            json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
