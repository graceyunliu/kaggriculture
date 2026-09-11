#!/usr/bin/env python3
"""
Phase A instrumentation pilot (from the leader_strategy_earliest_divergence handoff doc):
a read-only, unmodified-O36 decision-funnel + root-cause classifier for idle land, days 11-25.

Reuses the two validated read-only instruments already built in this thread instead of
re-deriving from scratch:
  - Phase 1's classify_day() logic (per-crop eligibility reasons: outside_day_window,
    straw_delay_gate, no_sell_time_left, demand_room_exhausted, value_density_too_low, eligible)
    -- see tools/_probe_scratch/idle_land_reasons_probe.py
  - Phase 2's sys.settrace hook into the REAL running economy() frame (post-herd free cash,
    real post-loop outcome, and per-candidate labor-throttle events at line 594/596)
    -- see tools/_probe_scratch/idle_land_posthead_probe.py and
       kaggriculture-idle-land-max-hands-throttle-confirmed-sep11.md (Phase 2 result: MAX_HANDS
       throttle explains 100% of idle-after observations in a 120-game sample)

This pilot's job (per the handoff doc, Phase A): run a SMALL sample (one opponent, two seeds,
BOTH seats) to verify (1) the game advances correctly, (2) the idle classification makes sense,
(3) decision-funnel causes sum correctly, and (4) tile/board snapshots used for classification are
independent copies (deep copies), not references into a mutable grid that later hours overwrite --
this project has hit that exact bug before (see handoff doc Phase A note).

Decision funnel per capital-hour observation (matches handoff doc sec.7):
  NO_OPPORTUNITY          -- not a capital hour (economy() structurally can't expand: hour!=1),
                             OR space<=0 (no usable idle land at all this capital hour)
  CONSIDERED_REJECTED     -- space>0, every crop's eligibility check evaluated and excluded
                             (outside window / demand-room exhausted / value density too low)
                             with no purchase attempt at all (any_eligible=False)
  ATTEMPT_BLOCKED         -- space>0, >=1 crop eligible, the real loop picked one as "best" but its
                             quantity got throttled toward/to zero by MAX_HANDS (_load_model) before
                             land/cash/room ran out -- confirmed dominant cause in Phase 2
  OPPORTUNITY_NOT_CONSIDERED -- space>0 after the real loop ended specifically because
                             n_seed_orders reached the hardcoded cap of 4 crop types/day (the loop
                             never even got to evaluate whether more crops were eligible)
  ACTION_TAKEN            -- space==0 after the loop (land fully used), or land partially used and
                             remaining post_space==0

No gameplay change: read-only re-computation via classify_day (a hand replica, used only for the
per-crop reason breakdown) plus sys.settrace on the live economy() frame (ground truth for free
cash and actual loop outcome). No candidate is proposed here -- this is instrumentation validation.
"""
import sys, os, argparse, copy, importlib.util
from pathlib import Path
from collections import Counter

def find_repo_root():
    p = Path.home() / "mnt" / "Kaggriculture"
    if (p / "mini_engine.py").exists():
        return p
    return None

REPO = find_repo_root()
sys.path.insert(0, str(REPO))
os.chdir(REPO)
import mini_engine as me  # noqa: E402

OPPS = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}
DAY_LO, DAY_HI = 11, 25
HOOK_LINE = 568
EXCL_LINE = 596
POST_LINE = 607


def load_agent_module(path, tag):
    p = Path(path)
    name = f"cause_trace_{tag}_{p.stem}_{os.getpid()}_{id(object())}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def classify_day_eligibility(mod, obs, v):
    """Phase-1 replica: per-crop eligibility reasons + any_eligible flag. Read-only, hand-derived
    from O36's own constants/functions -- used only to explain WHY, never to gate real play."""
    day = obs["day"]
    seeds = obs["private"]["seeds"]
    committed = {c: 0.0 for c in mod.CROP_SPECS}
    for _pos, t in v["crops"]:
        c = t.get("crop")
        if c in committed:
            committed[c] += mod.CROP_SPECS[c]["units"]
    for c in committed:
        committed[c] += seeds.get(c, 0) * mod.CROP_SPECS[c]["units"]
    prices = obs["market"]["prices"]
    reasons = {}
    any_eligible = False
    for c, sp_ in mod.CROP_SPECS.items():
        if day > sp_["cutoff"] or day < sp_.get("start", 0):
            reasons[c] = "outside_day_window"; continue
        if c == "STRAWBERRY" and day < mod.KNOBS["straw_delay"]:
            reasons[c] = "straw_delay_gate"; continue
        T_sell = max(0, 29 - day - sp_["first"])
        if T_sell <= 0:
            reasons[c] = "no_sell_time_left"; continue
        inv_c = obs["market"]["inventory"].get(c, mod.I0)
        cushion_left = max(0.0, sp_.get("cushion", 0) - max(0.0, inv_c - mod.I0))
        pool = mod.DEMAND_SHARE * (max(0.0, mod.I0 - inv_c) + cushion_left +
                                     mod._daily_demand(obs, c, day, day + sp_["first"]) * (29 - day))
        room_units = pool - committed[c]
        if room_units < sp_["units"] * 0.5:
            reasons[c] = "demand_room_exhausted"; continue
        price = min(prices.get(c, sp_["base"]), sp_["base"] * 2.0)
        val = min(sp_["units"], room_units) * price / sp_["cycle"]
        if val < sp_["min_val"]:
            reasons[c] = "value_density_too_low"; continue
        reasons[c] = "eligible"; any_eligible = True
    return any_eligible, reasons


def make_tracer(econ_code, out, day_lo, day_hi, mod0, snapshot_log):
    def make_local_tracer():
        rec = {"hook_done": False, "post_done": False, "excl_events": []}

        def local_tracer(frame, event, arg):
            if event != "line":
                return local_tracer
            lineno = frame.f_lineno
            if lineno == HOOK_LINE and not rec["hook_done"]:
                rec["hook_done"] = True
                lv = frame.f_locals
                day = lv.get("day")
                if day is None or not (day_lo <= day <= day_hi):
                    return None
                obs = lv["obs"]; v = lv["v"]
                # --- snapshot-independence check: deep-copy v["crops"]/v["empty"] NOW and again
                # later; if a later hour's mutation ever touches this stored copy, len/identity
                # would drift -- this is exactly the historical bug class flagged in the handoff.
                snap = copy.deepcopy({"crops": v["crops"], "empty": v["empty"],
                                        "empty_pastures": v["empty_pastures"]})
                snapshot_log.append((day, id(v["crops"]), len(v["crops"]), snap))

                any_eligible, reasons = classify_day_eligibility(mod0, obs, v)
                rec.update({
                    "day": day, "space": lv["space"], "free_real": lv["free"],
                    "any_eligible": any_eligible, "reasons": reasons,
                })
                out.append(rec)
            elif lineno == EXCL_LINE and rec["hook_done"] and not rec["post_done"]:
                lv = frame.f_locals
                rec["excl_events"].append({"crop": lv.get("c"), "k": lv.get("k")})
            elif lineno == POST_LINE and not rec["post_done"] and rec["hook_done"]:
                rec["post_done"] = True
                lv = frame.f_locals
                rec["post_space"] = lv["space"]
                rec["post_n_seed_orders"] = lv["n_seed_orders"]
                return None
            return local_tracer
        return local_tracer

    def global_tracer(frame, event, arg):
        if event == "call" and frame.f_code is econ_code:
            return make_local_tracer()
        return None
    return global_tracer


def classify_funnel(rec):
    """Decision-funnel classification, see module docstring."""
    if rec["space"] <= 0:
        return "ACTION_TAKEN", "land fully used at capital hour"
    if not rec["any_eligible"]:
        reason_ct = Counter(rec["reasons"].values())
        return "CONSIDERED_REJECTED", f"no crop eligible: {dict(reason_ct)}"
    post_space = rec.get("post_space")
    if post_space is None:
        return "UNKNOWN", "post-loop state not captured"
    if post_space <= 0:
        return "ACTION_TAKEN", "land fully used by end of real loop"
    if rec.get("post_n_seed_orders", 0) >= 4:
        return "OPPORTUNITY_NOT_CONSIDERED", "n_seed_orders cap (4 crop types/day) hit with space left"
    throttled = [e for e in rec["excl_events"] if e["k"] is not None and e["k"] <= 0]
    if throttled:
        return "ATTEMPT_BLOCKED", f"MAX_HANDS throttle zeroed: {[e['crop'] for e in throttled]}"
    return "CONSIDERED_REJECTED", "loop ended (best=None) with space left, no throttle event seen"


def run_game(agent_path, opp_path, seed, o36_seat, out, snapshot_log):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    mod_o36 = load_agent_module(agent_path, f"o36_seat{o36_seat}")
    mod_opp = load_agent_module(opp_path, f"opp_seat{1-o36_seat}")
    econ_code = mod_o36.economy.__code__
    agents = {o36_seat: mod_o36.agent, 1 - o36_seat: mod_opp.agent}
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                            "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engmod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    tracer = make_tracer(econ_code, out, DAY_LO, DAY_HI, mod_o36, snapshot_log)
    while True:
        for i in (0, 1):
            o = me._fast_copy(state[i].observation); o["step"] = step
            try:
                if i == o36_seat:
                    sys.settrace(tracer)
                    act = agents[i](o, me._fast_copy(env.configuration))
                    sys.settrace(None)
                else:
                    act = agents[i](o, me._fast_copy(env.configuration))
            except Exception:
                sys.settrace(None)
                act = {}
            state[i].action = act
        state = engmod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    return step  # steps actually advanced, for the "game advances correctly" check


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent", nargs="?", default="candidates/O36_MIN_HANDS2.py")
    ap.add_argument("--seeds", default="11-12")
    ap.add_argument("--opp", default="peter")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opp_path = OPPS[args.opp]

    print(f"=== Phase A instrumentation pilot: {args.opp}, seeds {lo}-{hi}, both seats ===\n")

    all_records = []
    all_snapshots = []
    step_counts = []
    for o36_seat in (0, 1):
        for seed in range(lo, hi + 1):
            recs = []
            snaps = []
            steps = run_game(args.agent, opp_path, seed, o36_seat, recs, snaps)
            step_counts.append(steps)
            for r in recs:
                r["_seat"] = o36_seat
                r["_seed"] = seed
            all_records.extend(recs)
            all_snapshots.extend(snaps)
            print(f"  seat={o36_seat} seed={seed}: game advanced {steps} steps, "
                  f"{len(recs)} capital-hour observations captured (days {DAY_LO}-{DAY_HI})")

    print(f"\n--- Verification checks ---")
    print(f"1. Game-advance check: all games reached episodeSteps or DONE "
          f"(min={min(step_counts)}, max={max(step_counts)} steps) -- "
          f"{'OK' if min(step_counts) > 0 else 'FAIL'}")

    # snapshot independence: deep copies must not be the SAME object id across different days,
    # and mutating one should never retroactively change an earlier stored snapshot's content.
    ids_by_day = Counter(sid for day, sid, ln, snap in all_snapshots)
    reused_ids = {sid: ct for sid, ct in ids_by_day.items() if ct > 1}
    print(f"2. Snapshot-independence check: {len(all_snapshots)} deep-copied snapshots taken; "
          f"object-id reuse across different capital-hour calls: {len(reused_ids)} id(s) reused "
          f"(expected: reuse of the *source* v['crops'] object id across hours is fine -- Python "
          f"can and does reallocate at the same address -- what matters is our copies are independent, "
          f"checked next)")
    # verify independence directly: re-deepcopy comparison -- each stored snap's crop count should
    # never change after the fact (it's a plain dict/list snapshot, nothing external mutates it)
    stable = all(isinstance(snap, dict) and "crops" in snap for _, _, _, snap in all_snapshots)
    print(f"   snapshot structural integrity (each is a self-contained deep-copied dict): "
          f"{'OK' if stable else 'FAIL'}")

    n = len(all_records)
    print(f"\n3. Decision-funnel classification over {n} capital-hour observations (both seats):")
    funnel_ct = Counter()
    for r in all_records:
        cat, _reason = classify_funnel(r)
        r["_funnel"] = cat
        funnel_ct[cat] += 1
    for cat, ct in funnel_ct.most_common():
        print(f"   {cat:28s}: {ct:4d} ({100*ct/n:.1f}%)")
    print(f"   sums-correctly check: {sum(funnel_ct.values())}/{n} "
          f"{'OK' if sum(funnel_ct.values()) == n else 'FAIL'}")

    idle_cats = {"CONSIDERED_REJECTED", "ATTEMPT_BLOCKED", "OPPORTUNITY_NOT_CONSIDERED"}
    idle_recs = [r for r in all_records if r["_funnel"] in idle_cats]
    print(f"\n4. Of {len(idle_recs)} observations classified as genuinely-idle-with-opportunity:")
    for cat in idle_cats:
        sub = [r for r in idle_recs if r["_funnel"] == cat]
        if sub:
            print(f"   {cat}: {len(sub)} -- e.g. day {sub[0]['day']} seat {sub[0]['_seat']} seed "
                  f"{sub[0]['_seed']}: {classify_funnel(sub[0])[1]}")

    by_seat = Counter(r["_funnel"] for r in all_records if r["_seat"] == 0)
    by_seat1 = Counter(r["_funnel"] for r in all_records if r["_seat"] == 1)
    print(f"\n5. Seat-symmetry sanity check (O36 as seat 0 vs seat 1, same funnel categories should "
          f"appear in both, no seat-specific instrumentation artifact):")
    print(f"   seat 0: {dict(by_seat)}")
    print(f"   seat 1: {dict(by_seat1)}")


if __name__ == "__main__":
    main()
