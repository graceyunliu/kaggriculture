# Codex brief — evolve loop ops hardening: auto-promotion, generator health alerts, frontier-refresh scheduling, final yardstick calibration

Copy everything below the line into Codex.

---

You are hardening the always-on evolve loop's operations so today's two staleness bugs (a frontier candidate stuck 24+ hours out of date, an LLM generator silently dead for 9 hours) can't recur unnoticed, plus finishing one piece of unfinished data (a stranded candidate file needed for accurate calibration). This is ops/infrastructure work, not game strategy.

## Location and worktree discipline — read this first

There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

The main checkout here has a **stale, unremovable `.git/index.lock`** and dirty modified tracked files (`candidates/K.py`, `candidates/P.py` — belonging to a concurrent session's in-progress planner work, do not touch or copy them) plus several relevant **untracked** files you need (`candidates/P6_baseline.py`, `candidates/P7.py`, `candidates/P7b.py`, `tools/calibrate_yardstick.py`, and this project's various `docs/PROMPT-codex-*.md` briefs and result docs). Do not attempt to `git add`/`git commit`/`rm .git/index.lock` in the main checkout directly — it will fail or, worse, risk touching the concurrent session's uncommitted edits.

Instead: create an isolated worktree the way the `codex/loop-integration` branch did successfully (see its commits `2ec1bd9`..`bf0846b` for the pattern), e.g. `git worktree add /tmp/kag-ops-hardening -b codex/ops-hardening`. From inside that worktree, `git status` will not show the main checkout's dirty files (they're a different working directory), and you can safely `cp` in the specific untracked files you need (see Task 4) without disturbing the concurrent session at all. Commit and push from the worktree.

Do **not** open, read, or write anything under `/Users/graceliu/Documents/ChatGPT/Kaggriculture`, `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture`, `Archived versions/`, `Chatgpt Agents/`, `Perplexity Agents/`, `User Notebooks/`, or `/Users/graceliu/Downloads`. Do not modify `candidates/K.py`, `candidates/P.py`, or `evolve/blocks/planner_sweep.py` — concurrent-session territory.

## Background — read these in full first

- `evolve/yardstick.conf` — current state: `FRONTIER=candidates/H32.py`, `SMOKE_FLOOR=-40000`, `DEV_PROMOTE=-20000`, explicitly commented as **provisional** (estimated, not measured — see the file's own comment for why).
- `evolve/supervisor.sh` — the continuous loop driver; read its full source, not just the frontier-sourcing lines.
- `evolve/digest.py`, `evolve/notify.sh`, `evolve/notify.conf` — the existing alert channel ("beats C1" alerts already fire through this; you're extending it, not building a new one).
- `evolve/refresh_frontier.py` — exists, does what it says (clusters ladder replays, writes `Opponents/frontier.txt`), but nothing currently schedules it (`launchctl list | grep -i frontier` on the deployment machine returns nothing).
- `tools/calibrate_yardstick.py` — the script that measures reference candidates against the current `FRONTIER`; already run once with only `C1` available (margin -$37,097/game vs H32, t=-9.33). `candidates/P6_baseline.py` (this project's best own-code planner) was the missing reference.
- `evolve/archive.json`, `evolve/db.py`'s `candidates` table schema (dev/held margins, `stage`, `status`) — what "beats the frontier decisively" should be computed from.

## Task 1 — Auto-promotion: detect when a held-out winner should replace the current frontier

Today's bug: H32 shipped as the real best candidate, but `evolve/yardstick.conf`'s `FRONTIER` stayed on the previous candidate (H10) for over a day because nothing checked. Fix this class of bug, don't just fix today's instance:

1. Write `evolve/check_frontier.py`: queries the archive/DB for any candidate with `stage`/`status` = held-out-pass whose held-out margin against the *current* `FRONTIER` exceeds a decisive threshold (reuse the project's existing convention for "decisive" — check `docs/block-library.md` or `RULES.md` for the t-stat/margin bar already in use, don't invent a new one).
2. When found, do NOT auto-edit `yardstick.conf` silently (a frontier change also requires recalibrating `SMOKE_FLOOR`/`DEV_PROMOTE`, which is not something to automate blindly — see Task 4's caution about this exact thing). Instead, fire a clear alert through the existing `notify.sh`/Hermes channel: "candidate X beats current frontier Y by $Z/game (t=T) — review for promotion," and write a short flag file (e.g. `evolve/PROMOTION_PENDING.txt`) that `supervisor.sh` checks and logs prominently at the start of each segment until a human clears it.
3. Wire `check_frontier.py` to run once per segment inside `supervisor.sh`'s loop (after `report.py`/archive export, before the next segment starts).
4. Verify with a short synthetic test: manually insert a fake DB row with a decisive margin against the current frontier, run `check_frontier.py`, confirm it fires the alert and writes the flag file; then clear it and confirm a normal run does not.

## Task 2 — Generator health alerting

Today's bug: `propose.py` failed for ~9 hours (`RuntimeError('claude exit 1: ')` in `evolve/logs/propose.log`) with no alert — it was only caught by a human manually tailing logs. Fix:

1. In `supervisor.sh` (or wherever the propose step's exit status is already checked — note the existing log line `"propose failed (see evolve/logs/propose.log)"` already exists, so the detection point exists, just not the alerting), add a consecutive-failure counter (persisted across segments, e.g. a small state file `evolve/logs/propose_failures.count`).
2. When the counter reaches a threshold (suggest 3 consecutive segments, i.e. roughly matching today's real incident duration relative to the 30-minute `PROPOSE_INTERVAL`) fire an alert through the same `notify.sh`/Hermes channel used for "beats C1" alerts: "propose.py has failed N consecutive times, last error: <tail of propose.log>."
3. Reset the counter to 0 on any successful propose round.
4. Verify by simulating N consecutive failures (temporarily point `claude` at a nonexistent binary, or stub the failure condition) and confirming the alert fires once, not once per segment forever, and resets on a subsequent success.

## Task 3 — Schedule `refresh_frontier.py`

Nothing currently runs this script on a schedule. Per its own docstring, `run_nightly.sh` reads `Opponents/frontier.txt` as the `--clone` opponent but nothing writes fresh values to that file periodically.

1. Add a call to `python3 evolve/refresh_frontier.py` inside `supervisor.sh`'s main loop, once per segment (or on a longer interval if every-2-hours is wasteful — check the script's own runtime cost first with `--dry-run` and decide; document your choice).
2. Confirm it composes safely with the existing `CLONE_NOW` fallback logic in `supervisor.sh` (lines ~30-35) — it should only change behavior when `Opponents/frontier.txt` actually gets a new value, not break the existing fallback to `tape_yuan800_104892947.py` when no file exists yet.
3. Verify with `--dry-run` first, then a live run, confirming `Opponents/frontier.txt` and `Opponents/tapes.json` update as expected and `supervisor.sh` picks up the new clone opponent on its next segment.

## Task 4 — Finish the yardstick calibration for real

1. From your isolated worktree (see the worktree-discipline note above), copy in the untracked `candidates/P6_baseline.py` from the main checkout (verify it's genuinely the frozen P6 — diff its key behavioral markers against what `docs/planner-allocation-hiring-results.md` describes as P6's control result, -$9,374/game vs H10, if you can re-derive that; don't just trust the filename) and `tools/calibrate_yardstick.py`. Commit both to your branch.
2. Run `python3 tools/calibrate_yardstick.py` for real, with `P6_baseline.py` now present, against `FRONTIER=candidates/H32.py`.
3. Update `evolve/yardstick.conf`: replace the provisional `SMOKE_FLOOR=-40000`/`DEV_PROMOTE=-20000` estimate with values derived from the actual measured P6-vs-H32 margin (follow the same reasoning style as the existing comment: floor loose enough to let a competitive-but-losing candidate like P6 survive smoke, promote threshold near or somewhat above P6's own margin). Update the file's comment to say "measured" instead of "provisional/estimated," with the real number and date.
4. Push your branch, merge to `main` following the same process as `codex/loop-integration`.

## Deliverables

1. `evolve/check_frontier.py` + `supervisor.sh` wiring (Task 1), with the synthetic test's output shown in the results doc.
2. `supervisor.sh`'s propose-failure counter + alert wiring (Task 2), with the simulated-failure test's output shown.
3. `supervisor.sh`'s `refresh_frontier.py` scheduling (Task 3), with a `--dry-run` and live-run output shown.
4. Updated `evolve/yardstick.conf` with a real, measured calibration (Task 4), and `candidates/P6_baseline.py` finally committed to `main`.
5. `docs/ops-hardening-results.md`: what was built for each task, verification output, and — same discipline as every other brief in this project — an explicit note on anything that could not be done cleanly within scope (e.g. if the "decisive" promotion threshold convention isn't clearly defined anywhere and you had to pick one, say so and say what you picked and why).

## Rules

Two debugging rounds per task, then write up and stop. Do not touch any concurrent session's claimed files (`candidates/K.py`, `candidates/P.py`, `evolve/blocks/planner_sweep.py`). Do not merge without confirming `main` still builds/imports cleanly after your merge (a quick `python3 -c "import candidates.H32"`-style smoke check, adapted to whatever the project's existing smoke-check convention is). This is ops work: no new game-strategy logic anywhere in this task.
