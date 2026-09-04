# Codex brief — day-planner executor as chassis blocks

Copy everything below the line into Codex.

---

You are implementing a new executor for a Kaggle farming-simulation agent. Everything you need is in one project folder; do not search the web and do not re-derive game rules — they are documented and engine-verified.

## Location — read this before anything else
There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

`cd` there first; every relative path below is relative to that folder. It is a git repo (`origin` = github.com/graceyunliu/kaggriculture, branch `master`). Do **not** open, read, or write anything under these other folders — they are different lineages and will confuse you:
- `/Users/graceliu/Documents/ChatGPT/Kaggriculture` (a separate agent lineage, V3_x; not your baseline)
- `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture` (a mount/mirror of the same; ignore)
- `/Users/graceliu/Claude/Projects/Kaggriculture/Archived versions`, `.../Chatgpt Agents`, `.../Perplexity Agents`, `.../User Notebooks` (history only)
- `/Users/graceliu/Downloads` (raw replay dumps; not needed)

Absolute paths of the files you will use most:
- Spec: `/Users/graceliu/Claude/Projects/Kaggriculture/docs/SPEC-day-planner-executor.md`
- Constitution / closed list: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/RULES.md`
- Loop docs: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/README.md`
- Block system: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/blocks.py`, chassis `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/chassis.py`, param space + renderer `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/space.py`
- Baseline agent: `/Users/graceliu/Claude/Projects/Kaggriculture/candidates/E1.py`; its crop_admission block source: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/blocks_banded_crop_admission.py`; knobbed chassis source of truth: `/Users/graceliu/Claude/Projects/Kaggriculture/candidates/K.py`
- Evaluator: `/Users/graceliu/Claude/Projects/Kaggriculture/mini_engine.py`, `.../decompose.py`, `.../search.py`; engine (read-only, ladder-identical): `/Users/graceliu/Claude/Projects/Kaggriculture/vendor/kaggle_environments_engine_master/kaggriculture.py`
- Opponents: `/Users/graceliu/Claude/Projects/Kaggriculture/Opponents/` (tape_*.py, opp_*.py) and `/Users/graceliu/Claude/Projects/Kaggriculture/candidates/V3_12.py`, `.../candidates/C1.py`
- Results history: `/Users/graceliu/Claude/Projects/Kaggriculture/docs/candidates-C1-H10-sep03.md`; the loop's latest report is on git branch `results` (`git fetch origin results && git show origin/results:evolve/reports/latest.md`), not on disk.
- Your outputs go under: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/blocks/` (already exists and holds other block sources such as `animal_routing_rotation.py`, `dispatch_idledrop.py` — do not modify those; add yours with the `planner_` prefix), `.../candidates/P.py`, `.../candidates/gen_p/`, `.../evolve/queue/`, `.../docs/planner-results.md`.

Python: use the system `python3` (3.10+); nothing to install — `mini_engine.py` shims the one external import. Run all commands from `/Users/graceliu/Claude/Projects/Kaggriculture`.

## Read first, in this order
1. `docs/SPEC-day-planner-executor.md` — the design you are implementing, including the **Addendum (Sep 4)** at the end. The addendum overrides the main text where they differ.
2. `evolve/README.md` and `evolve/RULES.md` — how the autonomous search loop works and what has already been proven not to work. Do not re-test anything in RULES.md's "closed" list.
3. `evolve/blocks.py` (top 60 lines) — the block system: `evolve/chassis.py` is a frozen copy of `candidates/K.py` with marker comments around named groups of functions. A candidate replaces the *source* of one or more blocks. Block → functions:
   - `hiring`: `_hire_plan`, `_load_model`
   - `animal_routing`: `_build_route`, `_route_step`
   - `crop_admission`: `_crop_pools`, `_plant_choice`, `_task_valid`
   - `sweep`: `_build_sweep`, `_crop_step`
   - `dispatch`: `_unit_action`
   - (`economy`, `demand`, `siting` exist too; you will not change them)
4. `candidates/E1.py` — the current best own-code agent (baseline to beat). Its `crop_admission` block is the "banded siting" replacement saved in `evolve/blocks_banded_crop_admission.py`; its KNOBS/constants diff vs C1 is listed in `docs/candidates-C1-H10-sep03.md` (search "E1") and in `evolve/reports/latest.md` on the `results` git branch.
5. `mini_engine.py`, `decompose.py`, `search.py` docstrings — the evaluator. No installation needed; plain Python 3.10+. A game takes ~0.6 s; 20 games (10 seeds, both seats) ~10 s with `--jobs 4`. Results are cached by file hash.

## What to build
Implement the spec's planner (§3–§7) as **block replacements**, not as a standalone agent:
- `hiring` block: `_hire_plan` unchanged; `_load_model` replaced by the planner's `hands_needed()` (spec §6, headcount = smallest N covering all hard chores; keep the same function name and signature so `economy()` keeps working).
- `animal_routing`, `sweep`, `dispatch` blocks: replaced by the chore enumeration, day plan, and hourly executor (spec §4, §6, §7). Keep the same top-level function names and signatures as the chassis (`_build_route`, `_route_step`, `_build_sweep`, `_crop_step`, `_unit_action`); internally they may call new helper functions you define *inside the block source* (helpers must live in the same block text, since only block text is substituted).
- `crop_admission`: keep E1's banded block unchanged; your planner consumes its `plant` pool and `_plant_choice`.
- Per-day planner state: the module-level `S` dict is outside the blocks; use `S.setdefault("plan", ...)` at runtime rather than editing the `S = {...}` literal. `S["day"]` reset logic in `_agent` clears `routes/sweep/setup` each day — reset your plan when `S["plan"]["day"] != day`.

Constraints on block source (from `evolve/RULES.md`): define exactly the chassis's top-level function names for that block; use only names that exist in the chassis plus your own helpers; valid Python 3.9 (no `match`, no `X | Y` types); never touch the crash guard, engine constants, or `perceive`; deterministic tie-breaks (sort by `(cost, pos)`), no randomness; keep per-turn time under 50 ms.

## Write set / read-only set
- You may create/edit: `evolve/blocks/planner_*.py` (one file per block source), `candidates/P.py` (a rendered full agent for local testing), `candidates/gen_p/`, `evolve/queue/planner_*.json`, `docs/planner-results.md`.
- Read-only: `candidates/K.py`, `candidates/E1.py`, `candidates/C1.py`, `candidates/V3_12.py`, `evolve/chassis.py`, `mini_engine.py`, `decompose.py`, `evolve/trace.py`, `Opponents/`, `vendor/`. Another agent is concurrently working in `tools/` and `Opponents/schedules/` — do not touch those either.

## How to render and test a candidate locally
```python
import sys; sys.path.insert(0, "evolve"); sys.path.insert(0, ".")
import space, json
p = space.c1_params()
p.update({...E1's knob/constant diff...})          # from docs/candidates-C1-H10-sep03.md, section "E1"
blocks = {"crop_admission": open("evolve/blocks_banded_crop_admission.py").read(),
          "hiring": open("evolve/blocks/planner_hiring.py").read(),
          "animal_routing": open("evolve/blocks/planner_animal_routing.py").read(),
          "sweep": open("evolve/blocks/planner_sweep.py").read(),
          "dispatch": open("evolve/blocks/planner_dispatch.py").read()}
path = space.render(p, blocks)                      # writes evolve/gen/cand_<key>.py
```
Copy the rendered file to `candidates/P.py` for the commands below.

## Acceptance ladder — run in order, stop and fix at the first failure
1. Runs clean: `python3 mini_engine.py candidates/P.py candidates/V3_12.py --seeds 1 2 3 --both-seats` → `agent errors [0, 0]` and no `GUARD` lines on stderr (the crash guard turns exceptions into PASS turns; a candidate with any error is worthless).
2. Coverage metric (write `evolve/trace_chores.py` or extend your own script; do not edit `evolve/trace.py`): per day, hard chores enumerated at hour 0 vs completed; animals with `consecutive_unfed ≥ 1` at end of day; plants lost to weeds; **travel per work action** (moves ÷ non-move actions). Targets on seeds 1–5 vs `candidates/V3_12.py`: 0 escaped animals, 0 weeds from unwatered crops, ≥ 95% hard chores done, travel/action ≤ 1.2 (E1 ≈ 1.5; the frontier tapes ≈ 1.0). Print E1's numbers alongside.
3. Sanity floor: `python3 mini_engine.py candidates/P.py candidates/E1.py --seeds 1 2 3 4 5 6 7 8 9 10 --both-seats --jobs 4` → margin ≥ 0. If negative, run `python3 decompose.py candidates/P.py candidates/E1.py --seeds 1-10` and look at (a) too many shed trips (cap pickups to one per route per plan), (b) over-hiring (`hands_eod`), (c) planting without same-day water.
4. **Primary test — the coupled scale test** (execution-only changes were measured ≈ $0 in `evolve/oracle.py`; the planner must pay off by enabling more work): render P with `open_melons=12`, `wheat_per_animal=0.5`, `max_animals=20`, `demand_share=0.6` and compare to E1 with the *same* knobs. E1 loses money with these settings; P must not, and P-with-scale must beat E1-baseline on seeds 1–10 both seats.
5. Held-out: seeds 11–30 vs `candidates/E1.py`, `candidates/V3_12.py`, `Opponents/tape_shirabe_105076319.py`, `Opponents/tape_yuan800_104892947.py`, `Opponents/tape_atakan_104893687.py`. Report margin, t, W-L for each. Success = ≥ E1 everywhere and tape margins improve by ≥ $5k.

## Deliverables
1. `evolve/blocks/planner_{hiring,animal_routing,sweep,dispatch}.py` — the block sources.
2. `evolve/queue/planner_factorial.json` — a `{"kind":"factorial", ...}` entry (format in `evolve/README.md`) with `block_options` for the four planner blocks × the E1 baseline blocks, and `axes` `{"open_melons":[8,12],"wheat_per_animal":[0.0,0.5],"demand_share":[0.5,0.6]}`, so the autonomous loop scores and ablates it.
3. `docs/planner-results.md` — the numbers from steps 2–5, what failed and how it was fixed, and the per-item `decompose.py` output for P vs E1 and P vs tape_yuan800.

Do not submit anything to Kaggle and do not modify `RULES.md`; leave both to the owner. If two debugging rounds on the same regression fail to find the cause, stop, write up the trace and hypotheses in `docs/planner-results.md`, and end — do not keep guessing.
