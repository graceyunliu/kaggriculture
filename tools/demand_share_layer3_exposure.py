#!/usr/bin/env python3
"""DEMAND_SHARE Layer-3 (economic exposure) instrument -- MELON early/mid, STRAWBERRY mid, CARROT late.

Per kaggriculture-demand-share-layer1-2-results-sep11.md: these four crop x phase cells passed Layer 1
(representative binding) and Layer 2 (materially different decisions under alt_share=0.35). This does NOT
prove 0.35 is better, or that the changed decisions matter economically -- that is exactly what this
instrument measures. Per Grace's design rule: run OBSERVATIONALLY against the real O26 trajectory. Do NOT
simulate DEMAND_SHARE=0.35 as an altered policy end-to-end -- that would be a candidate-shaped move this
stage explicitly defers.

SCOPE DECISIONS (stated up front, not buried):
- Class A (immediate decision exposure): full fidelity, captured live via the same sys.settrace hook as
  the Layer-1/2 instrument (tools/demand_share_binding_trace.py), at the real sizing-cap line.
- Class E (opportunity cost) proxy: captured at the SAME instant -- remaining free cash and tile space
  after the decision, and the set of OTHER crops excluded from consideration this same iteration (what
  else that cash/land could plausibly have gone to). This is a same-turn proxy, not a full multi-day
  opportunity-cost trace.
- Class B/C/D (physical feasibility / realized production / market exposure): reported at GAME level, not
  per-decision. For the same crop in the same game, we independently track (a) units of that crop actually
  PLANTED by day (from v["crops"], read-only census -- same style as the straw-planted census in
  tools/dormant_knob_engagement.py) and (b) units of that crop actually SOLD by phase, with realized price
  (same SELL-event recording pattern as tools/demand_share_trace.py). This gives an aggregate
  planted->sold realization rate and average realized price for the affected crop/phase in the SAME real
  trajectory the Layer-1/2 decisions came from -- it is NOT a per-decision unit-level lineage trace (that
  would require tagging individual seed-buy orders and following each planted tile to its specific harvest
  event, which is a materially larger build). This scope limit is intentional, matches the "cheap" framing
  for CARROT, and is stated here so nobody mistakes game-level context for decision-level causal proof.

Cross-thread note: this instrument hooks the REAL running economy() call via sys.settrace, so the `free`
(cash) value captured at each decision is already POST-herd-purchase-spend (herd/animal buys run earlier in
the same economy() call, before the crop loop). Per kaggriculture-idle-land-reasons-sep11.md, that thread's
open question was exactly whether a naive CARROT-only replica was wrong because it didn't subtract real herd
spend -- this instrument's `free` capture may bear on that; reported separately, not conflated with it.

Usage:
  KAGG_FIXED_SHOPS=1 python3 demand_share_layer3_exposure.py --opp bahaen --seeds 11-30,71-90 --alt-share 0.35 --json out.json
"""
import sys, os, argparse, json, collections, importlib.util, inspect

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
TARGETS = {("MELON", "early"), ("MELON", "mid"), ("STRAWBERRY", "mid"), ("CARROT", "late")}


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


class ExposureTracer:
    def __init__(self, mod, alt_share, exposures):
        self.mod = mod
        self.alt_share = alt_share
        self.exposures = exposures  # list of dicts, class A + E
        self.economy_code = mod.economy.__code__
        src_lines, start = inspect.getsourcelines(mod.economy)
        self.sizing_lineno = None
        for i, line in enumerate(src_lines):
            if "k = min(space, int(room_units //" in line and self.sizing_lineno is None:
                self.sizing_lineno = start + i
        assert self.sizing_lineno, "instrumentation target line not found -- source has drifted"

    def _tracer(self, frame, event, arg):
        if frame.f_code is not self.economy_code:
            return None
        if event == "line" and frame.f_lineno == self.sizing_lineno:
            self._capture(frame)
        return self._tracer

    def _capture(self, frame):
        f = frame.f_locals
        day = f.get("day"); c = f.get("c"); sp_ = f.get("sp_")
        room_units = f.get("room_units"); space = f.get("space"); free = f.get("free")
        committed = f.get("committed", {}); seed_orders = f.get("seed_orders", {})
        excluded = f.get("excluded", set())
        if day is None or c is None or sp_ is None:
            return
        ph = phase_of(day)
        if (c, ph) not in TARGETS:
            return
        units = sp_["units"]; seed_price = sp_["seed"]
        terms = {"demand_room": int(room_units // units), "space": space,
                 "cash": int(free // seed_price), "hardcap20": 20}
        k_actual = min(terms.values())
        DEMAND_SHARE = self.mod.DEMAND_SHARE
        X = (room_units + committed.get(c, 0) + seed_orders.get(c, 0) * units) / DEMAND_SHARE if DEMAND_SHARE else 0.0
        room_alt = self.alt_share * X - committed.get(c, 0) - seed_orders.get(c, 0) * units
        k_alt = min(int(room_alt // units) if room_alt > 0 else 0, terms["space"], terms["cash"], 20)
        if k_alt == k_actual and terms["demand_room"] != min(terms["space"], terms["cash"], 20):
            # not demand-bound and not counterfactually different -- not an exposed decision, skip
            return
        self.exposures.append({
            "day": day, "crop": c, "phase": ph,
            # class A: immediate decision exposure
            "k_actual": k_actual, "k_alt": k_alt, "delta_qty": k_alt - k_actual,
            "seed_price": seed_price,
            "cash_committed_baseline": k_actual * seed_price,
            "cash_delta": (k_alt - k_actual) * seed_price,
            "purchase_occurs": k_actual > 0,
            # class E: same-turn opportunity-cost proxy
            "space_before_this_buy": space, "space_remaining_after": space - k_actual,
            "free_cash_before_this_buy": free, "free_cash_remaining_after": free - k_actual * seed_price,
            "other_crops_excluded_this_turn": sorted(x for x in excluded if x != c),
        })


def run_game(mod, opp_path, seed, cand_seat, tracer, planted_census, sold_census):
    engine_mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    opp_agent = me.load_agent(opp_path)

    orig_commit = engine_mod._commit_unit

    def rec(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok and op == "SELL" and item in ("MELON", "STRAWBERRY", "CARROT"):
            sold_census.append((item, id(farm), price))
        return ok
    engine_mod._commit_unit = rec

    orig_perceive = mod.perceive

    def patched_perceive(obs):
        v = orig_perceive(obs)
        day = obs["day"]
        for pos, t in v["crops"]:
            crop = t.get("crop")
            if crop in ("MELON", "STRAWBERRY", "CARROT") and t.get("planted_day", day) == day:
                planted_census.append((crop, phase_of(day), day))
        return v
    mod.perceive = patched_perceive

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
    day_at_sell = {"day": 0}
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            day_at_sell["day"] = obs.get("day", day_at_sell["day"])
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
    engine_mod._commit_unit = orig_commit


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--opp", required=True, choices=list(OPPS))
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--alt-share", type=float, required=True)
    ap.add_argument("--json")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    opp_path = OPPS[args.opp]
    exposures = []
    planted_census_all = []  # (crop, phase, day) across all games
    sold_census_all = []     # (crop, farm_id_per_game, price) across all games -- farm id not comparable across games, used only as a per-game marker

    n_games = 0
    for seed in seeds:
        for cand_seat in (0, 1):
            mod = load_cand()
            tracer = ExposureTracer(mod, args.alt_share, exposures)
            planted_census = []
            sold_census = []
            run_game(mod, opp_path, seed, cand_seat, tracer, planted_census, sold_census)
            planted_census_all.extend(planted_census)
            sold_census_all.extend(sold_census)
            n_games += 1

    # aggregate class A/E by crop x phase
    by_cell = collections.defaultdict(list)
    for e in exposures:
        by_cell[(e["crop"], e["phase"])].append(e)

    print(f"LAYER-3 EXPOSURE (observational, real O26 trajectory) -- opp={args.opp} seeds={args.seeds} alt_share={args.alt_share} n_games={n_games}\n")

    for (c, ph) in sorted(TARGETS):
        recs = by_cell.get((c, ph), [])
        planted = [d for cc, p, d in planted_census_all if cc == c and p == ph]
        sold = [pr for cc, fid, pr in sold_census_all if cc == c]
        print(f"== {c} {ph} ==")
        print(f"  exposed decisions: {len(recs)}")
        if recs:
            cash_deltas = [r["cash_delta"] for r in recs]
            qty_deltas = [r["delta_qty"] for r in recs]
            occurs = sum(1 for r in recs if r["purchase_occurs"])
            print(f"  purchase occurs at baseline: {occurs}/{len(recs)} ({occurs/len(recs):.1%})")
            print(f"  mean cash_delta (alt vs baseline): {sum(cash_deltas)/len(cash_deltas):.1f}  (sum: {sum(cash_deltas):.0f})")
            print(f"  mean qty_delta: {sum(qty_deltas)/len(qty_deltas):.2f}")
            other_excl = collections.Counter()
            for r in recs:
                other_excl.update(r["other_crops_excluded_this_turn"])
            print(f"  other crops excluded same-turn (opportunity-cost proxy): {dict(other_excl)}")
            free_after = [r["free_cash_remaining_after"] for r in recs]
            space_after = [r["space_remaining_after"] for r in recs]
            print(f"  mean free cash remaining after this buy: {sum(free_after)/len(free_after):.1f}")
            print(f"  mean tile space remaining after this buy: {sum(space_after)/len(space_after):.2f}")
        print(f"  planted (this crop/phase, census): {len(planted)}")
        print(f"  sold (this crop, whole game, all phases -- game-level, not phase-isolated): {len(sold)}", end="")
        if sold:
            print(f", mean realized price: {sum(sold)/len(sold):.2f}")
        else:
            print()
        print()

    if args.json:
        out = {
            "opp": args.opp, "seeds": args.seeds, "alt_share": args.alt_share, "n_games": n_games,
            "exposures": exposures,
            "planted_census": planted_census_all,
            "sold_census": sold_census_all,
        }
        with open(args.json, "w") as fh:
            json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
