# Nightly archive regression harness

`evolve/regress.py` re-renders the strongest archived evolution candidates on the current chassis and scores them on the current vendored engine. It does not change an agent or submit to the ladder.

Before scoring, it replays the three newest local ladder episodes. `exact=True` means the local engine and `mini_engine` shim reproduced the recorded money exactly. A failed check is shown prominently but does not prevent the remaining diagnostics from running. The report records full SHA-256 hashes for the engine and chassis.

The harness fetches the `results` branch and uses its archive database or JSON when it has more candidate rows than the local database. If fetching fails, the report identifies the local fallback. The selected rows are the top held-out passes by margin plus any pinned keys; E1, C1, and V3.12 are always included as fixed references. Archive rows are rendered into `evolve/gen_regress/` without modifying the archive or agents.

## Run and read it

The normal nightly-sized run is:

```sh
cd /Users/graceliu/Claude/Projects/Kaggriculture
python3 evolve/regress.py
```

The acceptance-sized check is:

```sh
python3 evolve/regress.py --top 2 --seeds 11-14
python3 evolve/regress.py --top 2 --seeds 11-14 --accept
python3 evolve/regress.py --top 2 --seeds 11-14
```

To verify seed-set isolation, accept `11-14` and then run `--seeds 15-18`. Those cells say `new`; they are not regressions. Use `--pin key1,key2`, `--jobs N`, and `--tol 2000` to adjust selection, concurrency, and the materiality threshold.

Reports are written to timestamped `evolve/reports/regress-YYYYmmdd-HHMM.md` files and `evolve/reports/regress-latest.md`. Each score cell shows margin per game, its change from an exact matching baseline, paired-seed significance, W-L, and state:

- `new`: no baseline exists for that candidate, opponent, seed set, engine, and chassis.
- `rebased`: the same candidate/opponent/seeds exist, but the engine or chassis SHA changed.
- `regression` or `improvement`: the absolute change exceeds both the tolerance and two paired standard errors.
- `unchanged`: no material significant movement.

The process exits 1 only when it finds a regression. `--accept` merges the current cells into `evolve/regress_baseline.json`; it does not discard baselines for other seed sets or builds.

## Nightly scheduling

The supplied `evolve/com.grace.kaggriculture-regress.plist` runs at 02:30 each night. Review its paths, then the owner can install it (the harness does not load it):

```sh
cp evolve/com.grace.kaggriculture-regress.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.grace.kaggriculture-regress.plist
```

To remove it later:

```sh
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.grace.kaggriculture-regress.plist
```
