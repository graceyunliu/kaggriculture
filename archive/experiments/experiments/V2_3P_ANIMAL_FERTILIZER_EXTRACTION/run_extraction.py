#!/usr/bin/env python3
"""V2_3P: run instrumented V9.3 games across seeds 920-923 vs a real
opponent, then diff the shadow reconstructions (shadow_animal.py,
shadow_fertilizer.py) against the oracle call log turn-by-turn.

Does NOT modify main_v9.3_fertilize.py, main_v10.6_radius3.py, or anything
under "Archived versions/". Writes only under artifacts/v2_3p/ and
experiments/V2_3P_ANIMAL_FERTILIZER_EXTRACTION/.
"""
import copy
import importlib.util
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

from kaggle_environments import make  # noqa: E402
import instrument_v93  # noqa: E402
import shadow_animal  # noqa: E402
import shadow_fertilizer  # noqa: E402

V93_PATH = os.path.join(ROOT, "main_v9.3_fertilize.py")
OPP_PATH = os.path.join(ROOT, "Opponents", "opp_scenario_v14.py")
SEEDS = [920, 921, 922, 923]


def load_plain_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_") + "_plain", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


def run_game(seed, seat0_agent, seat1_agent, episode_steps=720):
    env = make("kaggriculture", configuration={"episodeSteps": episode_steps}, debug=False)
    env.info = {"seed": seed}
    t0 = time.time()
    env.run([seat0_agent, seat1_agent])
    elapsed = time.time() - t0
    final = env.steps[-1]
    money0 = final[0]["observation"]["farms"][0]["money"]
    money1 = final[0]["observation"]["farms"][1]["money"]
    return {"seed": seed, "elapsed_s": round(elapsed, 2),
            "final_money_seat0": money0, "final_money_seat1": money1,
            "n_steps": len(env.steps)}


def diff_animal_setup(log, m):
    mismatches = []
    n = 0
    for rec in log.get("animal_setup_action", []):
        n += 1
        (pos, view, shed, farmer_carry, plan, day, hour) = rec["args"][:7]
        reserved_sites = rec["args"][7] if len(rec["args"]) > 7 else ()
        exclude_sites = rec["kwargs"].get("exclude_sites", set())
        plan_copy = copy.deepcopy(plan)
        shadow_result = shadow_animal.animal_setup_action(
            pos, view, shed, farmer_carry, plan_copy, day, hour, reserved_sites, exclude_sites,
            dist_fn=m._dist, step_toward_fn=m._step_toward,
            nearest_center_fn=m._nearest_center, center_tiles=m.CENTER_TILES)
        if shadow_result != rec["result"]:
            mismatches.append({"t": rec["t"], "oracle": rec["result"], "shadow": shadow_result,
                                 "plan_species": plan.get("species"), "plan_stage": plan.get("stage")})
    return n, mismatches


def diff_animal_maintenance(log, m):
    mismatches = []
    n = 0
    for rec in log.get("animal_maintenance_action", []):
        n += 1
        (pos, view, shed, carry, day, hour) = rec["args"][:6]
        exclude = rec["args"][6] if len(rec["args"]) > 6 else set()
        critical_only = rec["kwargs"].get("critical_only", False)
        shadow_result = shadow_animal.animal_maintenance_action(
            pos, view, shed, carry, day, hour, exclude, critical_only,
            dist_fn=m._dist, step_toward_fn=m._step_toward, nearest_center_fn=m._nearest_center,
            animal_products=m.ANIMAL_PRODUCTS, product_deposit_at=m.PRODUCT_DEPOSIT_AT,
            feed_carry_target=m.FEED_CARRY_TARGET, center_tiles=m.CENTER_TILES,
            liquidate_day=m.LIQUIDATE_DAY)
        if list(shadow_result) != list(rec["result"]):
            mismatches.append({"t": rec["t"], "oracle": rec["result"], "shadow": shadow_result})
    return n, mismatches


def diff_fertilizer(log, m):
    """Track B partial equivalence check: for every turn, verify (a) every
    executed FERTILIZE op stood on a tile in that turn's view["fert_targets"]
    (generated set), (b) every executed PICKUP FERTILIZER 2 restock op
    happened at a center tile with >=2 FERTILIZER in shed and a non-empty
    fert_targets set, and (c) no FERTILIZE/restock op occurred when
    fert_targets was empty. This validates the admission/eligibility
    boundary; it does not replay the exact pool-competition order across
    multiple units competing for the same tile in one turn (documented as
    a known incompleteness in the report, not silently passed)."""
    econ_by_t = {rec["t"]: rec for rec in log.get("economy", [])}
    checks = {"fertilize_ops": 0, "fertilize_ok": 0, "restock_ops": 0, "restock_ok": 0,
              "bad_examples": []}
    for act in log.get("agent_actions", []):
        t = act["t"]
        econ = econ_by_t.get(t)
        if econ is None:
            continue
        obs = econ["args"][0]
        view = econ["args"][3]
        fert_targets = set(tuple(p) for p in view.get("fert_targets", []))
        player = obs.get("player")
        me = obs["farms"][player]
        farmer_pos = tuple(me["farmer"])
        hand_positions = [tuple(h) for h in me["hands"]]
        shed = obs["private"]["shed"]
        action = act["action"]
        units = [("farmer", farmer_pos, action.get("farmer"))]
        for i, hp in enumerate(hand_positions):
            hop = action.get("hands", [None] * len(hand_positions))
            units.append((f"hand{i}", hp, hop[i] if i < len(hop) else None))
        for name, pos, op in units:
            if not op:
                continue
            if op[0] == "FERTILIZE":
                checks["fertilize_ops"] += 1
                ok = pos in fert_targets
                if ok:
                    checks["fertilize_ok"] += 1
                else:
                    checks["bad_examples"].append({"t": t, "unit": name, "pos": pos,
                                                      "reason": "FERTILIZE off a generated fert_target"})
            elif op[0] == "PICKUP" and len(op) > 1 and op[1] == "FERTILIZER":
                checks["restock_ops"] += 1
                ok = (pos in m.CENTER_TILES and shed.get("FERTILIZER", 0) >= 2
                      and len(fert_targets) > 0)
                if ok:
                    checks["restock_ok"] += 1
                else:
                    checks["bad_examples"].append({"t": t, "unit": name, "pos": pos,
                                                      "reason": "FERTILIZER restock outside documented preconditions"})
    return checks


def diff_expansion_gates(log, m):
    results = {}
    for fn_name, shadow_fn, extra_kwargs in [
        ("_animal_expansion_feasible", shadow_animal.animal_expansion_feasible, {}),
        ("_sheep_expansion_feasible", shadow_animal.sheep_expansion_feasible, {"i0": getattr(m, "I0", 10000)}),
    ]:
        n = 0
        mismatches = []
        for rec in log.get(fn_name, []):
            n += 1
            (obs, view, budget, shed, n_animals, n_hands, quads) = rec["args"][:7]
            day = rec["args"][7] if len(rec["args"]) > 7 else rec["kwargs"].get("day", 99)
            reserved_sites_then = rec.get("extra", {}).get("reserved_sites", m.reserved_sites)
            kwargs = dict(
                live_price_fn=m.live_price, reserved_sites=reserved_sites_then,
                experiment_max_fleet=m.EXPERIMENT_MAX_FLEET, feed_carry_target=m.FEED_CARRY_TARGET,
                expansion_wheat_budget_frac=m.EXPANSION_WHEAT_BUDGET_FRAC,
                animal_work_weight=m.ANIMAL_WORK_WEIGHT, hand_target_max=m.HAND_TARGET_MAX,
                crop_neglect_tasks_per_hand=m.CROP_NEGLECT_TASKS_PER_HAND,
                expansion_min_crop_tiles_per_quad=m.EXPANSION_MIN_CROP_TILES_PER_QUAD,
            )
            if fn_name == "_sheep_expansion_feasible":
                kwargs["sheep_hand_headroom"] = m.SHEEP_HAND_HEADROOM
                kwargs["i0"] = getattr(m, "I0", 10000)
            shadow_result = shadow_fn(obs, view, budget, shed, n_animals, n_hands, quads, day, **kwargs)
            if bool(shadow_result) != bool(rec["result"]):
                mismatches.append({"t": rec["t"], "oracle": rec["result"], "shadow": shadow_result})
        results[fn_name] = {"n": n, "mismatches": mismatches}
    return results


def main():
    combined = {"seeds": SEEDS, "games": [], "track_a_setup": {"n": 0, "mismatches": []},
                "track_a_maintenance": {"n": 0, "mismatches": []},
                "track_a_gates": {"_animal_expansion_feasible": {"n": 0, "mismatches": []},
                                    "_sheep_expansion_feasible": {"n": 0, "mismatches": []}},
                "track_b_fertilizer": {"fertilize_ops": 0, "fertilize_ok": 0,
                                          "restock_ops": 0, "restock_ok": 0, "bad_examples": []},
                "determinism_check": []}

    opp_agent_fixed = load_plain_agent(OPP_PATH)

    for seed in SEEDS:
        log = {}
        v93_instrumented, m = instrument_v93.load_instrumented_agent(V93_PATH, log)
        opp_agent = load_plain_agent(OPP_PATH)
        result = run_game(seed, v93_instrumented, opp_agent)
        combined["games"].append(result)
        print(f"seed {seed}: money0={result['final_money_seat0']:.0f} "
              f"money1={result['final_money_seat1']:.0f} elapsed={result['elapsed_s']}s "
              f"steps={result['n_steps']}")

        n1, mm1 = diff_animal_setup(log, m)
        n2, mm2 = diff_animal_maintenance(log, m)
        gates = diff_expansion_gates(log, m)
        fert_checks = diff_fertilizer(log, m)
        for k in ("fertilize_ops", "fertilize_ok", "restock_ops", "restock_ok"):
            combined["track_b_fertilizer"][k] += fert_checks[k]
        combined["track_b_fertilizer"]["bad_examples"].extend(
            [{"seed": seed, **rec} for rec in fert_checks["bad_examples"]])

        combined["track_a_setup"]["n"] += n1
        combined["track_a_setup"]["mismatches"].extend(
            [{"seed": seed, **rec} for rec in mm1])
        combined["track_a_maintenance"]["n"] += n2
        combined["track_a_maintenance"]["mismatches"].extend(
            [{"seed": seed, **rec} for rec in mm2])
        for fn_name in ("_animal_expansion_feasible", "_sheep_expansion_feasible"):
            combined["track_a_gates"][fn_name]["n"] += gates[fn_name]["n"]
            combined["track_a_gates"][fn_name]["mismatches"].extend(
                [{"seed": seed, **rec} for rec in gates[fn_name]["mismatches"]])

        print(f"  setup calls={n1} mismatches={len(mm1)} | "
              f"maintenance calls={n2} mismatches={len(mm2)} | "
              f"expansion_gate calls={gates['_animal_expansion_feasible']['n']} "
              f"mismatches={len(gates['_animal_expansion_feasible']['mismatches'])} | "
              f"sheep_gate calls={gates['_sheep_expansion_feasible']['n']} "
              f"mismatches={len(gates['_sheep_expansion_feasible']['mismatches'])}")
        print(f"  fert: fertilize_ops={fert_checks['fertilize_ops']} ok={fert_checks['fertilize_ok']} "
              f"restock_ops={fert_checks['restock_ops']} ok={fert_checks['restock_ok']}")

    # Determinism check: rerun seed 920 (plain, uninstrumented agents) twice,
    # confirm identical terminal money both times, and confirm the
    # instrumented run above matched a plain rerun (instrumentation changed
    # nothing).
    plain_v93_a = load_plain_agent(V93_PATH)
    plain_opp_a = load_plain_agent(OPP_PATH)
    r1 = run_game(920, plain_v93_a, plain_opp_a)
    plain_v93_b = load_plain_agent(V93_PATH)
    plain_opp_b = load_plain_agent(OPP_PATH)
    r2 = run_game(920, plain_v93_b, plain_opp_b)
    instrumented_920 = combined["games"][0]
    combined["determinism_check"] = {
        "plain_rerun_1": r1, "plain_rerun_2": r2,
        "instrumented_run": instrumented_920,
        "plain_reruns_match": (r1["final_money_seat0"] == r2["final_money_seat0"]
                                 and r1["final_money_seat1"] == r2["final_money_seat1"]),
        "instrumentation_preserves_actions": (
            r1["final_money_seat0"] == instrumented_920["final_money_seat0"]
            and r1["final_money_seat1"] == instrumented_920["final_money_seat1"]),
    }
    print("determinism:", combined["determinism_check"]["plain_reruns_match"],
          "| instrumentation-neutral:", combined["determinism_check"]["instrumentation_preserves_actions"])

    out_path = os.path.join(ROOT, "artifacts", "v2_3p", "extraction_run_raw.json")
    with open(out_path, "w") as f:
        json.dump(combined, f, indent=2, default=str)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
