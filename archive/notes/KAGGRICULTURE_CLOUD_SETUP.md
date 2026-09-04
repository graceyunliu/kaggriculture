# Kaggriculture — runnable environment for head-to-head tests

Everything needed to run seeded head-to-head tests between agent scripts lives
in this repo. No Kaggle account or API access is required — the engine runs
fully offline.

## 1. Get the code

```bash
git clone https://github.com/graceyunliu/kaggriculture.git
cd kaggriculture
```

(Repo is currently private under graceyunliu's GitHub — ask Grace for access
if the clone is rejected.)

## 2. Install the environment

Requires Python 3.10+.

```bash
./setup_local_env.sh
```

What this does and why it's needed: the `kaggriculture` environment lives on
the `kaggle-environments` GitHub main branch but hasn't shipped to PyPI yet
(confirmed as of 2026-08-04, latest PyPI release 1.25.9 doesn't include it).
The script installs `kaggle-environments --no-deps` + `jsonschema` + `requests`
(seconds, no GPU/torch stack needed), then vendors the actual engine file
(`vendor/kaggle_environments_engine/kaggriculture.py`, pinned to a specific
GitHub commit — see `vendor/kaggle_environments_engine/SOURCE.md`) into
site-packages so `make("kaggriculture")` resolves. It's idempotent and safe
to rerun. A working venv isn't required — a bare `python3 -m pip --user`
install works fine too if `python3 -m venv` fails in your sandbox (it can,
in some containerized environments — the script still succeeds).

Verify it worked:

```bash
python3 smoke_test.py main_v8.3.py --opponent starter
```

Expect `OK: both players finished cleanly.` in a few seconds.

## 3. Run a head-to-head test

```bash
python3 seeded_h2h.py <agent_a.py> <agent_b.py> --seeds 1 2 3 4 5 --both-seats
```

**Always use `--both-seats`, not `--swap-half`.** The engine's day-end weed
RNG is drawn sequentially per player from one stream, which biases seat 0
vs seat 1 by about -$2,772/game on the standard seed set — reproducibly,
regardless of agent skill. `--both-seats` plays every seed in both seat
assignments and sums money, which cancels that bias exactly (an agent
against itself scores 0.0 margin under it). `--swap-half` does NOT cancel
it and has produced false-rejection results before (see `seeded_h2h.py`
module docstring for the full incident writeup). `--both-seats` costs 2x
the games but is the only result worth acting on.

Output includes win/loss count, paired mean margin, stdev, stderr, t-stat,
and a rough 95% CI — use those to judge whether a result is statistically
real before treating a challenger as better or worse than the champion.

Default is `--turns 720` (a full 30-day season); each game takes well under
a second, so a 15-seed `--both-seats` run (30 games) finishes in seconds.

## 4. Key files for context

- `main_v8.3.py` — current validated local champion (sheep-as-pure-fleet-
  addition, 10/15 wins vs `main_v8.py`, +$1,894/game, not yet submitted to
  the real Kaggle ladder).
- `main_v8.py` — prior champion, live on the real ladder at 667.1.
- `main_v8.2.py` — reweight variant, beat v8 12/15 locally, submitted
  2026-08-05 (696.0 on the ladder — too fresh to trust yet).
- Everything else under `main_v8*.py` and `Archived versions/` is the
  experiment trail (both validated and rejected variants are kept
  deliberately — see `kaggriculture-v8-architecture.md` and each file's
  own comments for the verdict on why it was kept or rejected).
- `harness.py` is a *different* tool — it ingests real-ladder replay JSON
  into a SQLite DB for reporting. It is not the simulation engine; for
  head-to-head simulation use `seeded_h2h.py`.

## 5. If something doesn't match this doc

The vendored engine is pinned to a specific commit
(`vendor/kaggle_environments_engine/SOURCE.md` has the hash and re-fetch
command). If PyPI has since shipped `kaggriculture` for real, a plain
`pip install -U kaggle-environments` also works and is preferred — the
vendoring is a fallback, not the source of truth.
