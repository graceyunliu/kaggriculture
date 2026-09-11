#!/usr/bin/env python3
"""
Phase 2 of the idle-land-reasons trace: hook economy() itself (via sys.settrace, read-only,
no source modification) to capture the REAL post-herd `free` cash figure at the exact line
where the crop seed-buying loop is about to start (candidates/O36_MIN_HANDS2.py:568, right
after `space = ...` and before `while space > 0 and n_seed_orders < 4:`).

This directly tests the open hypothesis from kaggriculture-idle-land-reasons-sep11.md:
  "the [Phase-1] replica didn't subtract real herd/animal purchase spending, which runs first
   in economy() and shares the same cash pool -- next step is hooking economy() itself to get
   the true post-herd `free` cash before re-testing [the CARROT-always-eligible cash check]."

Re-runs the same CARROT sizing formula as Phase 1, but this time against the REAL free/space/
committed values captured directly from the live economy() frame -- not a hand-rewritten replica.
No gameplay change: this only reads locals out of the running frame via settrace.
"""
import sys, os, argparse, importlib.util
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
DEBUG_COUNTS = Counter()
HOOK_LINE = 568  # "while space > 0 and n_seed_orders < 4:" -- real post-herd free/space/committed
                 # are all fully computed in f_locals at this point, before the loop body runs.
POST_LINE = 607  # "for c, k in seed_orders.items():" -- right after the while loop terminates:
                 # tells us WHY it stopped (space==0 vs n_seed_orders==4 cap vs best is None).
EXCL_LINE = 596  # "if k <= 0:" -- fires only when the chosen best-crop `c` got throttled to k<=0
                 # despite passing space/room/cash pre-checks (line 593). Distinguishes labor
                 # throttle (MAX_HANDS via _load_model) from a genuine space/room/cash shortfall.


def load_agent_module(path, tag):
    p = Path(path)
    name = f"idle_probe2_{tag}_{p.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def make_tracer(econ_code, out, day_lo, day_hi):
    """Global sys.settrace hook: watches for calls into the real economy() frame. HOOK_LINE (568,
    the while-condition) and POST_LINE (607, a for-loop header) both re-fire on every loop
    iteration, so each traced call gets its OWN fresh per-call record dict + one-shot guards --
    otherwise later iterations' already-mutated locals silently overwrite the pre-loop snapshot."""

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
                if day is not None and day_lo <= day <= day_hi:
                    CROP_SPECS = frame.f_globals["CROP_SPECS"]
                    DEMAND_SHARE = frame.f_globals["DEMAND_SHARE"]
                    I0 = frame.f_globals["I0"]
                    obs = lv["obs"]
                    free = lv["free"]
                    space = lv["space"]
                    committed = lv["committed"]
                    seed_orders = lv["seed_orders"]
                    n_total = lv["n_total"]
                    pending_place = lv["pending_place"]

                    carrot_spec = CROP_SPECS["CARROT"]
                    inv_c = obs["market"]["inventory"].get("CARROT", I0)
                    cushion_left = max(0.0, carrot_spec.get("cushion", 0) - max(0.0, inv_c - I0))
                    daily_dem = frame.f_globals["_daily_demand"](obs, "CARROT", day, day + carrot_spec["first"])
                    pool = DEMAND_SHARE * (max(0.0, I0 - inv_c) + cushion_left + daily_dem * (29 - day))
                    committed_carrot = committed.get("CARROT", 0.0) + seed_orders.get("CARROT", 0) * carrot_spec["units"]
                    room_units = pool - committed_carrot
                    k_by_space = space
                    k_by_room = int(room_units // carrot_spec["units"]) if carrot_spec["units"] else 0
                    k_by_cash = int(free // carrot_spec["seed"]) if carrot_spec["seed"] else 0
                    k_carrot_real = max(0, min(k_by_space, k_by_room, k_by_cash, 20))

                    rec.update({
                        "day": day, "space": space, "free_real": free,
                        "k_by_space": k_by_space, "k_by_room": k_by_room, "k_by_cash": k_by_cash,
                        "k_carrot_real": k_carrot_real,
                        "n_total": n_total, "pending_place": pending_place,
                    })
                    out.append(rec)
                else:
                    return None  # outside day window, stop tracing this frame entirely
            elif lineno == EXCL_LINE and rec["hook_done"] and not rec["post_done"]:
                DEBUG_COUNTS["excl_line_hits"] += 1
                lv = frame.f_locals
                rec["excl_events"].append({
                    "crop": lv.get("c"), "k_after_throttle": lv.get("k"), "space": lv.get("space"),
                })
            elif lineno == POST_LINE and not rec["post_done"] and rec["hook_done"]:
                rec["post_done"] = True
                lv = frame.f_locals
                rec["post_space"] = lv["space"]
                rec["post_n_seed_orders"] = lv["n_seed_orders"]
                rec["post_excluded"] = sorted(lv["excluded"])
                rec["post_seed_orders"] = dict(lv["seed_orders"])
                rec["carrot_bought"] = lv["seed_orders"].get("CARROT", 0)
                rec["carrot_excluded"] = "CARROT" in lv["excluded"]
                rec["stopped_by_cap"] = (lv["n_seed_orders"] >= 4 and lv["space"] > 0)
                return None  # done with this frame, stop tracing it
            return local_tracer
        return local_tracer

    def global_tracer(frame, event, arg):
        if event == "call" and frame.f_code is econ_code:
            return make_local_tracer()
        return None

    return global_tracer

def run_game(agent_path, opp_path, seed, out, econ_code_unused):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    mod0 = load_agent_module(agent_path, "p0")
    econ_code = mod0.economy.__code__
    a1 = load_agent_module(opp_path, "p1").agent
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                            "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engmod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    tracer = make_tracer(econ_code, out, DAY_LO, DAY_HI)
    while True:
        for i in (0, 1):
            o = me._fast_copy(state[i].observation); o["step"] = step
            try:
                if i == 0:
                    sys.settrace(tracer)
                    act = mod0.agent(o, me._fast_copy(env.configuration))
                    sys.settrace(None)
                else:
                    act = a1(o, me._fast_copy(env.configuration))
            except Exception:
                sys.settrace(None)
                act = {}
            state[i].action = act
        state = engmod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent", nargs="?", default="candidates/O36_MIN_HANDS2.py")
    ap.add_argument("--seeds", default="11-18")
    ap.add_argument("--opp", default="all")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}

    mod0 = load_agent_module(args.agent, "codecheck")
    econ_code = mod0.economy.__code__
    print(f"hooked economy() code object at {econ_code.co_filename}:{econ_code.co_firstlineno}, "
          f"watching line {HOOK_LINE}")

    records = []
    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            run_game(args.agent, opp_path, seed, records, econ_code)

    n = len(records)
    print(f"\n=== REAL post-herd CARROT cash check, days {DAY_LO}-{DAY_HI}, {n} capital-hour observations ===\n")
    sp = [r for r in records if r["space"] > 0]
    print(f"observations with space>0: {len(sp)}/{n} ({100*len(sp)/max(1,n):.1f}%)")
    zero_k = [r for r in sp if r["k_carrot_real"] <= 0]
    print(f"k_carrot_real<=0 despite space>0: {len(zero_k)}/{len(sp)} ({100*len(zero_k)/max(1,len(sp)):.1f}%)")
    if zero_k:
        cash_bound = sum(1 for r in zero_k if r["k_by_cash"] <= 0 and r["k_by_room"] > 0)
        room_bound = sum(1 for r in zero_k if r["k_by_room"] <= 0)
        both = sum(1 for r in zero_k if r["k_by_cash"] <= 0 and r["k_by_room"] <= 0)
        print(f"  of those: cash-bound only: {cash_bound}   room-bound only: {room_bound}   both<=0: {both}")
        neg_free = sum(1 for r in zero_k if r["free_real"] <= 0)
        print(f"  free_real<=0 (fully cash-exhausted after herd spend): {neg_free}/{len(zero_k)}")
    nonzero = [r for r in sp if r["k_carrot_real"] > 0]
    if nonzero:
        mean_k = sum(r["k_carrot_real"] for r in nonzero) / len(nonzero)
        mean_space = sum(r["space"] for r in nonzero) / len(nonzero)
        print(f"  when k_carrot_real>0: mean k={mean_k:.1f} vs mean space available={mean_space:.1f} "
              f"(shortfall={mean_space-mean_k:.1f})")
    all_free = [r["free_real"] for r in records]
    print(f"\nDEBUG_COUNTS: {dict(DEBUG_COUNTS)}")
    print(f"\nfree_real (post-herd) across ALL observations: min={min(all_free):.0f} "
          f"mean={sum(all_free)/len(all_free):.0f} max={max(all_free):.0f}  "
          f"(<=0 in {sum(1 for f in all_free if f<=0)}/{n} = {100*sum(1 for f in all_free if f<=0)/n:.1f}%)")

    print("\n=== WHY the real while-loop actually stopped (line 607, post-loop state) ===")
    have_post = [r for r in records if "post_space" in r]
    print(f"observations with post-loop data: {len(have_post)}/{n}")
    idle_after = [r for r in have_post if r["post_space"] > 0]
    print(f"post_space>0 (land STILL idle after the real loop ran): {len(idle_after)}/{len(have_post)} "
          f"({100*len(idle_after)/max(1,len(have_post)):.1f}%)")
    if idle_after:
        cap_bound = [r for r in idle_after if r["stopped_by_cap"]]
        excl_bound = [r for r in idle_after if not r["stopped_by_cap"]]
        print(f"  stopped by n_seed_orders>=4 CAP (space left, but 4-crop-type limit hit): "
              f"{len(cap_bound)}/{len(idle_after)} ({100*len(cap_bound)/len(idle_after):.1f}%)")
        print(f"  stopped because best-crop search found nothing left eligible (demand/window exhausted): "
              f"{len(excl_bound)}/{len(idle_after)} ({100*len(excl_bound)/len(idle_after):.1f}%)")
        carrot_excluded_when_idle = sum(1 for r in idle_after if r["carrot_excluded"])
        carrot_bought_when_idle = sum(1 for r in idle_after if r["carrot_bought"] > 0)
        print(f"  of idle-after observations: CARROT ended up excluded (tried+rejected or skipped by cap): "
              f"{carrot_excluded_when_idle}/{len(idle_after)}   CARROT was actually bought (some amount): "
              f"{carrot_bought_when_idle}/{len(idle_after)}")
        mean_idle_space = sum(r["post_space"] for r in idle_after) / len(idle_after)
        print(f"  mean post-loop idle space on these observations: {mean_idle_space:.1f} tiles")

        print("\n  Labor-throttle (MAX_HANDS) events on idle-land days -- crop chosen as 'best' but k throttled to 0:")
        for r in idle_after:
            ev = r.get("excl_events", [])
            if ev:
                print(f"    day {r['day']}: {ev}")
        n_throttled_idle = sum(1 for r in idle_after if r.get("excl_events"))
        print(f"  idle-after observations with at least one labor-throttle-to-zero event: "
              f"{n_throttled_idle}/{len(idle_after)}")
        print("\n  Full diagnostic dump per idle-after observation:")
        for r in idle_after:
            print(f"    day {r['day']}: post_space={r['post_space']} post_n_seed_orders={r['post_n_seed_orders']} "
                  f"post_excluded={r['post_excluded']} post_seed_orders={r['post_seed_orders']} "
                  f"k_carrot_at_hook={r['k_carrot_real']} k_by_room={r['k_by_room']} k_by_cash={r['k_by_cash']} "
                  f"k_by_space={r['k_by_space']}")


if __name__ == "__main__":
    main()
