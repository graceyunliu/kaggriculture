# Codex brief — nightly regression harness for the evolve archive

Copy everything below the line into Codex.

---

You are adding a regression harness to a Kaggle farming-simulation project. It re-scores the best archived candidates on the *current* chassis and engine so that a chassis rebuild, an engine update, or a bad merge cannot silently invalidate the archive. Pure tooling: no game-strategy decisions, no changes to any agent.

## Location — read this before anything else
There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

`cd` there first; all relative paths below are relative to it. Do **not** read or write anything under `/Users/graceliu/Documents/ChatGPT/Kaggriculture`, `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture`, `.../Archived versions`, `.../Chatgpt Agents`, `.../Perplexity Agents`, `.../User Notebooks`, or `/Users/graceliu/Downloads`.

Files you will use (absolute paths):
- Evaluator: `/Users/graceliu/Claude/Projects/Kaggriculture/mini_engine.py` — `evaluate(a, b, seeds, engine="master", both_seats=True, jobs=N)` returns `mean_margin_per_game`, `t`, `wins`, `losses`, `mean_a`, `mean_b`; results are cached by file sha under `.mini_engine_cache/`. Read its docstring.
- Replay/engine check: `/Users/graceliu/Claude/Projects/Kaggriculture/replay_verify.py` — replays a recorded ladder episode through the local engine; `exact=True` means engine and shim match the ladder.
- Candidate rendering: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/space.py` (`base_params()`, `c1_params()`, `render(params, blocks)`), block substitution `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/blocks.py`, chassis `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/chassis.py`.
- Archive: local `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/archive.json` and `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/evolve.db` (SQLite, table `candidates` with `params`, `blocks`, `held_margin`, `held_clone_margin`, `status`, `island`, `key`). **The authoritative archive is on git branch `results`** — fetch with `git fetch origin results` and read `git show origin/results:evolve/archive.json` (and `origin/results:evolve/evolve.db` if present). The local DB may be a small test DB; prefer `results` when it has more rows.
- Loop docs: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/README.md`, report format `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/report.py`.
- Reference agents: `/Users/graceliu/Claude/Projects/Kaggriculture/candidates/E1.py`, `.../candidates/C1.py`, `.../candidates/V3_12.py`.
- Opponents: every `/Users/graceliu/Claude/Projects/Kaggriculture/Opponents/tape_*.py` (replay-tape opponents from the ladder) and `.../Opponents/opp_*.py` (public-notebook policies).
- Ladder replays: `/Users/graceliu/Claude/Projects/Kaggriculture/Replays/Auto/mine/episode-*-replay.json` (each ~25 MB; do not load them all — pick the 3 newest by mtime). `/Users/graceliu/Claude/Projects/Kaggriculture/pull_ladder.py` fetches new ones (needs network; optional).
- Engine: `/Users/graceliu/Claude/Projects/Kaggriculture/vendor/kaggle_environments_engine_master/kaggriculture.py` (read-only).

Python: system `python3` (3.10+), nothing to install. Run everything from `/Users/graceliu/Claude/Projects/Kaggriculture`.

## Write set / read-only
- Create/edit only: `/Users/graceliu/Claude/Projects/Kaggriculture/evolve/regress.py`, `.../evolve/regress_baseline.json`, `.../evolve/reports/regress-*.md`, `.../docs/regression-harness.md`, and (optional) a launchd plist `.../evolve/com.grace.kaggriculture-regress.plist` modelled on the existing `com.grace.kaggriculture-digest.plist` but **not loaded** — the owner loads it.
- Read-only: everything else. Never edit `mini_engine.py`, `candidates/*`, `evolve/chassis.py`, `evolve/space.py`, `evolve/loop.py`, `evolve/RULES.md`. Other agents are concurrently writing `evolve/blocks/planner_*`, `candidates/P*.py`, `tools/`, `Opponents/schedules/` — do not touch those.

## What `evolve/regress.py` does
1. **Engine check.** Run `replay_verify.verify()` on the 3 newest replays in `Replays/Auto/mine/`. If any is not `exact`, print a red banner and still continue (record it in the report). Also record the sha256 of `vendor/kaggle_environments_engine_master/kaggriculture.py` and of `evolve/chassis.py`.
2. **Select candidates.** From the archive (prefer `results` branch), take the top N (default 5, `--top N`) by `held_margin` among `status == "held_pass"`, plus every candidate whose key is listed in `--pin` (comma-separated; default empty). Always include the references `candidates/E1.py`, `candidates/C1.py`, `candidates/V3_12.py` as fixed rows.
3. **Re-render on the current chassis.** For archive candidates, rebuild the agent file from `params` + `blocks` via `space.render` (block sources: the archive stores block *names* for some rows and full source for others — if only a name is stored, look for the source in `evolve/blocks/` and `evolve/blocks_banded_crop_admission.py`; if it cannot be found, mark the row `unrenderable` and continue). Save renders under `evolve/gen_regress/`.
4. **Score.** For each candidate row, run `mini_engine.evaluate` both seats on a fixed seed set (`--seeds`, default `11-30`) against: `candidates/E1.py`, `candidates/V3_12.py`, and every `Opponents/tape_*.py`. Use `--jobs` (default cores−1). Record margin/game, t, W-L per opponent.
5. **Compare to baseline.** `evolve/regress_baseline.json` holds the last accepted results keyed by `(candidate key, opponent, seed set, engine sha, chassis sha)`. For each cell: if the engine/chassis sha changed, mark `rebased`; else flag a **regression** if margin moved by more than `--tol` (default $2,000) *and* |Δ| > 2 × the paired standard error the evaluator reports (compute SE from per-seed margins in `evaluate()`'s `per_seed`). Flag an **improvement** symmetrically. `--accept` writes the new results as the baseline.
6. **Report.** Write `evolve/reports/regress-<YYYYmmdd-HHMM>.md` and overwrite `evolve/reports/regress-latest.md`: engine check result and shas; a table candidate × opponent with margin (Δ vs baseline in parentheses), W-L; a "REGRESSIONS" section listing every flagged cell with both numbers; an "unrenderable" list. Exit code 0 if no regressions, 1 otherwise (so a launchd/cron job can notify).

Determinism: never use randomness; the evaluator is deterministic and cached, so re-running is cheap. Budget: top-5 + 3 references = 8 candidates × ~8 opponents × 40 games ≈ 2,600 games ≈ 20 minutes at 4 jobs — print progress per candidate.

## Acceptance
1. `python3 evolve/regress.py --top 2 --seeds 11-14` completes, prints the engine check as `exact=True` for the 3 replays, and writes a report.
2. Running it twice in a row (second time with `--accept` after the first) produces zero regressions on the second run (cache makes it fast).
3. Deliberately test the detector: run once with `--seeds 11-14`, accept, then run with `--seeds 15-18` — different seeds must be reported as a different seed set (a new baseline key), **not** as regressions.
4. `docs/regression-harness.md`: what it checks, how to read the report, the exact commands, and how the owner would schedule it nightly (plist provided but not loaded).

Do not run it against the ladder or submit anything; do not modify `RULES.md`. If `git fetch origin results` fails (no network), fall back to the local `evolve/archive.json` and say so in the report.
