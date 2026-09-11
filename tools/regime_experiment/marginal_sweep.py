import sys, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import mini_engine as me

REACH_PATH = str(Path(__file__).resolve().parent / "O26_REACH.py")
OPPONENTS = {
    "tape_feeltheagi": str(ROOT / "Opponents/tape_feeltheagi_107564195.py"),
}

_pending_overrides = {}
_captured = []
_orig_load_agent = me.load_agent

def _load_agent_capture(path):
    fn = _orig_load_agent(path)
    mod = sys.modules.get(fn.__module__)
    if mod is not None and getattr(mod, "__file__", "") == REACH_PATH:
        for k, v in _pending_overrides.items():
            mod.KNOBS[k] = v
        mod.BINDING_LOG.clear()
        _captured.append(mod)
    return fn

me.load_agent = _load_agent_capture


def _play_one(overrides, seed, opp_path, seat=0):
    global _pending_overrides
    _pending_overrides = dict(overrides)
    _captured.clear()
    a, b = (REACH_PATH, opp_path) if seat == 0 else (opp_path, REACH_PATH)
    res = me.run_game(a, b, seed=seed, engine="master", trace=True)
    reach_mod = _captured[-1]
    tr = res["trace"][seat]
    opp_seat = 1 - seat
    own_money = res["money"][seat]
    opp_money = res["money"][opp_seat]

    mix = tr["animal_mix"]
    peak = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    for m in mix:
        for sp in peak:
            peak[sp] = max(peak[sp], m.get(sp, 0))
    final = mix[-1] if mix else {}

    bought_units = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    bought_cost = {"COW": 0.0, "SHEEP": 0.0, "GOOSE": 0.0}
    for daybuy in tr["buys"]:
        for item, (q, cost) in daybuy.items():
            if item in bought_units:
                bought_units[item] += q
                bought_cost[item] += cost

    revenue = {"MILK": 0.0, "WOOL": 0.0, "EGG": 0.0}
    units_sold = {"MILK": 0, "WOOL": 0, "EGG": 0}
    for daysale in tr["sales"]:
        for item, (q, rev) in daysale.items():
            if item in revenue:
                revenue[item] += rev
                units_sold[item] += q

    wheat_bought_units = 0
    wheat_bought_cost = 0.0
    for daybuy in tr["buys"]:
        q, cost = daybuy.get("WHEAT", (0, 0.0))
        wheat_bought_units += q
        wheat_bought_cost += cost

    escapes = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    prev = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    for day_idx, m in enumerate(mix):
        bought_today = tr["buys"][day_idx - 1] if 1 <= day_idx <= len(tr["buys"]) else {}
        for sp in escapes:
            cur = m.get(sp, 0)
            b_q = bought_today.get(sp, (0, 0))[0] if isinstance(bought_today.get(sp), tuple) else 0
            gain = prev[sp] + b_q - cur
            if gain > 0:
                escapes[sp] += gain
            prev[sp] = cur

    bindings = {}
    for b_ in reach_mod.BINDING_LOG:
        key = (b_["species"], b_["reason"])
        bindings[key] = bindings.get(key, 0) + 1

    return {
        "seed": seed, "own_money": own_money, "opp_money": opp_money,
        "margin": own_money - opp_money,
        "peak": peak, "final": dict(final),
        "bought_units": bought_units, "bought_cost": bought_cost,
        "revenue": revenue, "units_sold": units_sold,
        "wheat_units": wheat_bought_units, "wheat_cost": wheat_bought_cost,
        "escapes": escapes, "bindings": bindings,
    }


def sweep(label_overrides, seeds, opp_key="tape_feeltheagi", seat_both=True):
    opp_path = OPPONENTS[opp_key]
    rows = []
    for label, overrides in label_overrides:
        per_seed = []
        for seed in seeds:
            per_seed.append(_play_one(overrides, seed, opp_path, seat=0))
            if seat_both:
                r = _play_one(overrides, seed, opp_path, seat=1)
                r["margin"] = -r["margin"]
                r["own_money"], r["opp_money"] = r["opp_money"], r["own_money"]
                per_seed.append(r)
        margins = [r["margin"] for r in per_seed]
        own_moneys = [r["own_money"] for r in per_seed]
        mean_margin = statistics.mean(margins)
        se = statistics.pstdev(margins) / (len(margins) ** 0.5) if len(margins) > 1 else 0.0
        t = mean_margin / se if se > 0 else float("nan")
        agg_bought_units = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
        agg_bought_cost = {"COW": 0.0, "SHEEP": 0.0, "GOOSE": 0.0}
        agg_revenue = {"MILK": 0.0, "WOOL": 0.0, "EGG": 0.0}
        agg_escapes = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
        agg_bindings = {}
        peak_max = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
        wheat_units = 0
        wheat_cost = 0.0
        for r in per_seed:
            for sp in agg_bought_units:
                agg_bought_units[sp] += r["bought_units"][sp]
                agg_bought_cost[sp] += r["bought_cost"][sp]
                agg_escapes[sp] += r["escapes"][sp]
                peak_max[sp] = max(peak_max[sp], r["peak"][sp])
            for it in agg_revenue:
                agg_revenue[it] += r["revenue"][it]
            for k, v in r["bindings"].items():
                agg_bindings[k] = agg_bindings.get(k, 0) + v
            wheat_units += r["wheat_units"]
            wheat_cost += r["wheat_cost"]
        n = len(per_seed)
        row = {
            "label": label, "overrides": overrides, "n": n,
            "mean_margin": mean_margin, "t": t, "mean_own_money": statistics.mean(own_moneys),
            "peak_max": peak_max,
            "bought_units_per_game": {k: v / n for k, v in agg_bought_units.items()},
            "bought_cost_per_game": {k: v / n for k, v in agg_bought_cost.items()},
            "revenue_per_game": {k: v / n for k, v in agg_revenue.items()},
            "escapes_per_game": {k: v / n for k, v in agg_escapes.items()},
            "wheat_units_per_game": wheat_units / n, "wheat_cost_per_game": wheat_cost / n,
            "bindings": agg_bindings,
        }
        rows.append(row)
        print(f"[{label}] n={n} mean_margin={mean_margin:+.0f} t={t:.2f} own_money={row['mean_own_money']:.0f}")
        print(f"   peak: {peak_max}  bought/game: {row['bought_units_per_game']}  wheat/game: {row['wheat_units_per_game']:.1f}u ${row['wheat_cost_per_game']:.0f}")
        print(f"   revenue/game: {row['revenue_per_game']}  escapes/game: {row['escapes_per_game']}")
        print(f"   binding: {agg_bindings}")
    print("\n--- marginal (adjacent) deltas ---")
    for i in range(1, len(rows)):
        a, b = rows[i - 1], rows[i]
        d_margin = b["mean_margin"] - a["mean_margin"]
        d_bought = {sp: b["bought_units_per_game"][sp] - a["bought_units_per_game"][sp] for sp in a["bought_units_per_game"]}
        d_cost = {sp: b["bought_cost_per_game"][sp] - a["bought_cost_per_game"][sp] for sp in a["bought_cost_per_game"]}
        d_rev = {it: b["revenue_per_game"][it] - a["revenue_per_game"][it] for it in a["revenue_per_game"]}
        print(f"  {a['label']} -> {b['label']}: d_margin={d_margin:+.0f}  d_bought={d_bought}  d_cost={d_cost}  d_revenue={d_rev}")
    return rows
