from pathlib import Path
import sys

root = Path(__file__).resolve().parent
sys.path.insert(0, str(root / "evolve"))
sys.path.insert(0, str(root))
import mini_engine as me
import space

frontier = root / "candidates" / "O26_CARROT_SIZING.py"
space.freeze_base(root / "evolve" / "chassis.py")
params = space.base_params()
rendered = space.render(params, out_dir=root / "evolve" / "gen")
seeds = [1, 2, 31, 32, 41, 42]
all_ok = True
print("frontier", frontier)
print("rendered", rendered)
print("base_param_count", len(params))
print("seeds", seeds)
for seed in seeds:
    direct = me.run_game(frontier, frontier, seed, trace=True)
    rendered_first = me.run_game(rendered, frontier, seed, trace=True)
    rendered_second = me.run_game(frontier, rendered, seed, trace=True)
    # Compare the rendered agent's corresponding farm against the O26 farm in each seat.
    money_ok = (rendered_first["money"][0] == direct["money"][0] and
                rendered_first["money"][1] == direct["money"][1] and
                rendered_second["money"][0] == direct["money"][0] and
                rendered_second["money"][1] == direct["money"][1])
    errors = rendered_first["errors"] + rendered_second["errors"]
    traces_ok = (rendered_first["trace"] == direct["trace"] and
                 rendered_second["trace"] == direct["trace"])
    paired_first = rendered_first["money"][0] - rendered_first["money"][1]
    paired_second = rendered_second["money"][1] - rendered_second["money"][0]
    ok = money_ok and errors == [0, 0, 0, 0] and traces_ok and paired_first == -paired_second
    all_ok = all_ok and ok
    print({"seed": seed, "ok": ok, "direct_money": direct["money"],
           "rendered_first_money": rendered_first["money"],
           "rendered_second_money": rendered_second["money"],
           "paired_margins": [paired_first, paired_second],
           "errors": errors, "traces_identical": traces_ok})
if not all_ok:
    raise SystemExit("O26 equivalence failed")
print("O26_EQUIVALENCE_PASS")
