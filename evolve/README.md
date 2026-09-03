# evolve — autonomous candidate search for Kaggriculture

An evolution loop over the parameters of the knobbed V3.12 chassis (`candidates/K.py`), judged by the
real ladder engine, with a cascaded evaluator, a population archive, and a morning report. Phase 1 of
the program in `docs/cs329a-applied-to-kaggriculture.md`: constants-only search, no LLM, to prove the
machinery and find whatever interaction effects the hand sweeps missed.

## What it does

```
population (SQLite)  ->  pick parent(s)  ->  mutate / crossover  ->  render agent file
        ^                                                                 |
        |                                                                 v
   archive score  <-  cascade: fingerprint -> smoke -> dev -> held-out  <-+
```

* **Search space** (`space.py`): 24 `KNOBS` of K.py + 12 numeric constants (`MAX_HANDS`, `NEAR_RADIUS`,
  `STRAW_CUTOFF`, `HERD_LAST_DAY`, …), each with a range. A candidate is a dict; `render()` writes a
  normal single-file agent to `evolve/gen/cand_<key>.py`.
* **Chassis snapshot**: at run start `candidates/K.py` is copied to `evolve/base/K_<sha>.py` and every
  candidate is rendered from that snapshot, so edits to K.py by other sessions mid-run cannot corrupt
  a run. Candidate keys include the snapshot sha; scores are only comparable within a snapshot.
* **Cascade** (`cascade.py`), all paired both-seats on the master engine, cached by file sha:
  1. fingerprint — 2 games (seeds 1, 2) vs frontier; identical per-day trace to any known candidate ⇒ no-op, skipped
  2. smoke — seeds 1–3 both seats vs frontier; agent errors or margin < −$6k ⇒ dead
  3. dev — seeds 1–10 both seats vs frontier **and** vs the scenario-v14 clone; this is the selection score
  4. held-out — seeds 11–30, only if dev margin ≥ +$1.5k with t ≥ 2; **never used for selection**
* **Selection** (`loop.py`): parents by tournament from the top of the dev ranking (65%), a random
  behavioural cell — animals@day15 × land × hands (25%), or uniform (10%). Children: Gaussian/flip
  mutation (70%) or uniform crossover (30%). Duplicates are skipped by key.
* **Yardstick is fixed per run**: frontier `candidates/V3_12.py` + clone `Opponents/opp_scenario_v14.py`
  by default. Promote a held-out winner to the next run's `--frontier` by hand.
* **Report** (`report.py`): cascade counts, reference rows (V3.12, C1), held-out table, top-15 by dev,
  parameter importance (mean margin by value), behavioural cells. Written to `evolve/reports/<run>.md`.

## Throughput (measured)

Sandbox, 4 cores: 0.6–0.8 s/game, ~13–19k games/hour, ~13 s per candidate that reaches dev
(46 games), ~2 s per candidate that dies at smoke. Expect roughly 2× that on an 8-core Air:
**several hundred to ~1,000 candidates per 8-hour night**, most dying cheaply.

## Run it

```bash
# quick check (any machine with python3 >= 3.9; nothing to install)
python3 evolve/loop.py --minutes 5

# a night
evolve/run_nightly.sh 8                       # hours; JOBS defaults to cores-1
evolve/run_nightly.sh 8 candidates/C1.py      # different frontier opponent

# report for the latest run (also written automatically at the end of a run)
python3 evolve/report.py
```

Useful flags on `loop.py`: `--max-candidates N`, `--jobs N`, `--frontier`, `--clone`, `--base evolve/base/K_<sha>.py`
(continue a population on an older chassis snapshot), `--smoke-floor`, `--dev-promote`, `--mutation-rate`, `--sigma`, `--seed`.

## Put it on the MacBook Air

1. On this Mac: `bash evolve/make_bundle.sh` → `evolve/evolve_bundle.zip` (engine, chassis, opponents, loop; ~1 MB).
2. Copy the zip to the Air (AirDrop, or `scp evolve/evolve_bundle.zip air.local:~/`).
3. On the Air:
   ```bash
   mkdir -p ~/Kaggriculture && cd ~/Kaggriculture && unzip -o ~/evolve_bundle.zip
   bash evolve/setup_air.sh          # version check, 1 game, 20-game throughput, 3-minute loop
   ```
   If `python3` is older than 3.9: `brew install python@3.12` and run with `PYTHON=python3.12`.
4. Nightly job (21:00 → stops itself after 9 h → report):
   ```bash
   sed -i '' "s#/Users/graceliu/Kaggriculture#$HOME/Kaggriculture#" evolve/com.grace.kaggriculture-evolve.plist
   cp evolve/com.grace.kaggriculture-evolve.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.grace.kaggriculture-evolve.plist
   launchctl start com.grace.kaggriculture-evolve    # optional: kick one off now
   ```
   System Settings → Energy: keep "Prevent automatic sleeping when the display is off" on (the run also
   wraps itself in `caffeinate`). Stop a run early with `pkill -f evolve/loop.py` — it finishes the current
   candidate and writes the report.
5. Get results back: `evolve/reports/latest.md` is the morning read. To bring the population home,
   copy `evolve/evolve.db` and `evolve/gen/` (the files named in the report) — or just `scp air.local:~/Kaggriculture/evolve/reports/latest.md .`

## Keeping the yardstick current (ladder → Air)

The loop's secondary opponent is `Opponents/frontier.txt` (falls back to the September Yuan800 tape).
The Mac's 2:04 PM daily task runs, after the replay sync:

```bash
python3 evolve/refresh_frontier.py     # cluster newest scouted replays by opening; build tapes for new ≥10% clusters; set frontier.txt
python3 evolve/gh_push.py Opponents/tapes.json Opponents/frontier.txt Opponents/tape_<new>.py   # Contents-API push, no local git
```

`gh_push.py` needs a fine-grained GitHub token (this repo, Contents read/write) at `.github/token`
(gitignored). Without it the task prints the `git add/commit/push` line for you. The Air's nightly
`git pull` then picks the tapes up, so a ladder regime change on Monday is the Air's opponent Monday night.
The Air never touches Kaggle; the Mac never runs the loop.

## Reading the report

Only the **held-out** table counts. Dev margins are the selection score and will be seed-fit for the
top of the ranking (winner's curse). A candidate is worth promoting when its held-out margin vs the
frontier is positive with t ≥ 2 *and* its held-out margin vs the clone is not worse than C1's.
The "where the signal is" table shows which parameters the population's score actually depends on;
parameters that never appear there are inert on this chassis and can be dropped from the space.

## What this is not

Not an LLM loop, not code mutation, not a planner. Those are later phases (typed mutation blocks,
factorial bundles over lifecycle mechanisms, the oracle-bound routing experiment) and they plug into
the same evaluator and archive.
