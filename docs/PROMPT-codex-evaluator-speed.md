# Codex brief — evaluator speed-up + cheap early-death screen

Copy everything below the line into Codex.

---

You are speeding up the local evaluation pipeline for a Kaggle farming-simulation agent search. Two tasks, in order. Correctness is defined by exact reproduction of recorded games; do not trade correctness for speed.

## Location — read this first
There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

`cd` there; all relative paths below are relative to it. Do **not** open or modify anything under `/Users/graceliu/Documents/ChatGPT/Kaggriculture`, `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture`, `Archived versions/`, `Chatgpt Agents/`, `Perplexity Agents/`, `User Notebooks/`, or `/Users/graceliu/Downloads`. Another agent is concurrently working in `evolve/blocks/`, `candidates/P.py`, `candidates/gen_p/`, `evolve/queue/`; a third in `tools/` and `Opponents/schedules/`. Do not touch those paths.

Absolute paths you will use:
- Game runner: `/Users/graceliu/Claude/Projects/Kaggriculture/mini_engine.py` (read its docstring first)
- Determinism test: `/Users/graceliu/Claude/Projects/Kaggriculture/replay_verify.py`
- Cascade: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/cascade.py`; loop: `.../evolve/loop.py`; per-day metrics: `.../evolve/trace.py`; DB: `.../evolve/db.py`; docs: `.../evolve/README.md`
- Engine (read-only, identical to the ladder): `/Users/graceliu/Claude/Projects/Kaggriculture/vendor/kaggle_environments_engine_master/kaggriculture.py`
- Agents for benchmarking: `/Users/graceliu/Claude/Projects/Kaggriculture/candidates/E1.py`, `.../candidates/C1.py`, `.../candidates/V3_12.py`, `.../candidates/K.py` (the knobbed chassis source; agents are ~900 lines, `perceive()` at ~line 153, `_agent()` at ~line 889)
- Recorded ladder replays for the determinism test: `/Users/graceliu/Claude/Projects/Kaggriculture/Replays/Auto/mine/episode-*.json` (each ~25 MB; use 3–4 of them, not all)
- Opponent tapes: `/Users/graceliu/Claude/Projects/Kaggriculture/Opponents/tape_*.py`

Python: system `python3` (3.10+), nothing to install. `mini_engine.py` shims the one external import (`kaggle_environments.utils.resolve_episode_seed`).

## Write set
You may edit: `mini_engine.py`, `evolve/cascade.py`, `evolve/trace.py`, `evolve/loop.py`, `evolve/db.py`, `evolve/README.md`, and create `docs/evaluator-speed-results.md` and `bench_engine.py`. Read-only: everything else, especially `candidates/*.py`, `evolve/chassis.py`, `evolve/space.py`, `evolve/blocks.py`, `vendor/`.

## Invariants (check after every change)
1. **Exact reproduction**: `python3 replay_verify.py <3-4 replay files>` must print `"exact": true` for every file, before and after. This proves the shim + engine still match the ladder bit-for-bit.
2. **Identical results**: for the pairs (E1 vs V3_12), (C1 vs tape_yuan800_104892947) on seeds 1–5 both seats, final money for every game must be identical before and after (capture a JSON of `run_game(...)["money"]` per (a, b, seed) first; compare after). Results are cached by file hash in `.mini_engine_cache/` — pass `--no-cache` or call `run_game` directly so you are measuring real runs.
3. Agents are untrusted code: they may mutate the observation you pass them. Any optimization that stops copying must guarantee the engine's state is never mutated by an agent (check by asserting equality of a deep copy of `state` before/after the agent call in a debug mode, across the two pairs above).

## Task 1 — make `mini_engine.run_game` faster (target ≥ 2× games/hour; report what you get)
Measure first: write `bench_engine.py` that runs E1 vs V3_12 and C1 vs tape_yuan800 for seeds 1–4 with `cProfile` and prints the top 25 cumulative entries, plus wall time per game with `trace=True` and `trace=False`. Current baseline on a 4-core sandbox: 0.6–0.9 s/game single-process; ~2.5 games/s with 4 workers.

Likely hotspots, in expected order — verify with the profile, don't assume:
- `copy.deepcopy(state[i].observation)` and `copy.deepcopy(env.configuration)` once per agent per step (1,440 deep copies per game of a structure containing two 10×10 tile grids). Options: pass a *shallow-protected* view (copy only the parts the agent could mutate — `farms`, `private`, `market`, `town` — with `json.loads(json.dumps(...))` being no better; test a custom fast copier that handles only dict/list/str/int/float/bool/None, since the observation contains nothing else); or copy once per step and hand the same copy to the engine-side only if invariant 3 holds.
- `_snapshot()` in trace mode scans 100 tiles per player per day (cheap) but `traces[i]["shed"].append(dict(...))` and `animal_mix` accumulate — check they're not quadratic.
- The engine's own `interpreter` cost is fixed and off-limits; but the shim's `structify` on the initial state and `Struct.__getattr__` (dict lookups via attribute access) show up if called in hot loops — measure.
- Agent-side `perceive()` rescans the board per hour and is the agents' dominant cost; you may not edit agents, but note in the results how much of the per-game time is agent vs. harness so the owner can decide.
- Parallelism: `evaluate()` uses a fresh `multiprocessing.Pool` per call; `evolve/cascade.py` already keeps a persistent pool (`get_pool`). Make `mini_engine.evaluate` accept an existing pool or reuse a module-level one; measure scaling at 1/2/4 workers with `bench_engine.py --workers`.

Deliver: the speed-up, the before/after profile summary, and the invariant checks, in `docs/evaluator-speed-results.md`.

## Task 2 — a 1-game "pattern death" screen in the cascade
Context: in the last loop run, 90 of 269 candidates were no-ops and 19 died at smoke; each smoke costs 6 games and each dev stage 46. Many doomed candidates are recognizable from a single game's per-day trace. Add stage 0.5 to `evolve/cascade.py`, between fingerprint and smoke, that reuses the fingerprint game's trace (already computed — do not run extra games) and kills a candidate if, by day 12, any of:
- an animal escaped (animals count drops without a sale of that species — use the trace's `animals` series and `animal_mix`; a drop of ≥1 between consecutive days),
- ≥ 3 weeds created from unwatered plants by day 12 (needs a per-day weed count — extend `mini_engine._snapshot` to record `weeds` (tiles with kind WEED) and `plants`, as new trace keys; keep all existing keys unchanged),
- cash < $50 at hour 0 on 3 or more of days 1–8 while owning ≥ 3 animals (the cash-trap signature),
- `errors[0] > 0` (already handled at fingerprint — keep).

Make the thresholds config entries in `cascade.py`'s cfg dict (`pattern_death_day`, `pattern_death_weeds`, `pattern_death_cash_days`) and record the reason in the DB `note` with status `dead_pattern` (add it to the status enum wherever statuses are listed: `db.py`, `report.py`, `digest.py` if present). Then:
- **Calibrate before enabling**: run the screen in dry-run mode over the existing archive — `evolve/evolve.db` and `evolve/v2test.db` locally (small), and, if the `results` git branch's `archive.json` has per-candidate traces, over that — and report false positives: candidates the screen would have killed that later reached `held_pass`. Target: **zero** held-pass candidates killed; if any would be, loosen the offending threshold and re-report. `git fetch origin results && git show origin/results:evolve/archive.json > /tmp/archive.json` to get the archive.
- Add a `--no-pattern-death` flag to `loop.py` for A/B runs.

Deliver: the screen, the calibration table (kills by reason; false-positive count = 0), and the estimated games saved per 269 candidates, appended to `docs/evaluator-speed-results.md`.

## Rules
- Work in small commits on a branch `codex/evaluator-speed`; do not push to `results`.
- Never edit `vendor/`, `candidates/`, `evolve/chassis.py`, `evolve/space.py`, `evolve/blocks.py`, `evolve/RULES.md`.
- If a change breaks invariant 1 or 2 and the cause is not obvious after two attempts, revert it, note it in the results doc, and move on.
