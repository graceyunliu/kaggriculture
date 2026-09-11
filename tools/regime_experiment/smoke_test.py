import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import mini_engine as me

REACH_PATH = str(Path(__file__).resolve().parent / "O26_REACH.py")
OPP = str(ROOT / "Opponents/tape_feeltheagi_107564195.py")

_pending_overrides = {}
_captured = []
_orig_load_agent = me.load_agent

def _load_agent_capture(path):
    fn = _orig_load_agent(path)
    mod = sys.modules.get(fn.__module__)
    if mod is not None and getattr(mod, "__file__", "") == REACH_PATH:
        for k, v in _pending_overrides.items():
            mod.KNOBS[k] = v
        _captured.append(mod)
    return fn

me.load_agent = _load_agent_capture


def run_config(label, overrides, seeds, seat=0):
    global _pending_overrides
    _pending_overrides = dict(overrides)
    peak = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    end = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
    geese_bought_any = False
    bindings = {}
    per_seed = []
    for seed in seeds:
        _captured.clear()
        a, b = (REACH_PATH, OPP) if seat == 0 else (OPP, REACH_PATH)
        res = me.run_game(a, b, seed=seed, engine="master", trace=True)
        if not _captured:
            raise RuntimeError("REACH module not captured for seed %s" % seed)
        reach_mod = _captured[-1]
        mix_series = res["trace"][seat]["animal_mix"]
        seed_peak = {"COW": 0, "SHEEP": 0, "GOOSE": 0}
        for day_mix in mix_series:
            for sp in peak:
                seed_peak[sp] = max(seed_peak[sp], day_mix.get(sp, 0))
                peak[sp] = max(peak[sp], day_mix.get(sp, 0))
        end_mix = mix_series[-1] if mix_series else {}
        for sp in end:
            end[sp] = max(end[sp], end_mix.get(sp, 0))
        for b_ in getattr(reach_mod, "BINDING_LOG", []):
            key = (b_["species"], b_["reason"])
            bindings[key] = bindings.get(key, 0) + 1
        if end_mix.get("GOOSE", 0) > 0 or seed_peak["GOOSE"] > 0:
            geese_bought_any = True
        per_seed.append((seed, seed_peak, dict(end_mix)))
    print(f"--- {label} (overrides={overrides}) ---")
    print("  peak animal_mix (max over all seeds/days):", peak)
    print("  final-day animal_mix (max over seeds):", end)
    print("  goose ever purchased:", geese_bought_any)
    print("  binding-reason counts:", bindings)
    for seed, sp, em in per_seed:
        print(f"    seed {seed}: peak={sp} final={em}")
    return peak, end, geese_bought_any, bindings


if __name__ == "__main__":
    seeds = list(range(101, 106))  # fresh held-out-style seed set, small for a smoke test
    run_config("baseline (all defaults)", {}, seeds)
    run_config("max_sheep relaxed (30)", {"max_sheep": 30, "max_animals": 40}, seeds)
    run_config("land_reserve relaxed (0) + max_animals raised", {"land_reserve": 0, "max_animals": 40, "max_sheep": 30}, seeds)
    run_config("geese permissive", {"geese": 4, "geese_day_limit": 20, "max_animals": 40}, seeds)
