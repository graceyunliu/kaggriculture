# Evaluator speed and pattern-death results

Measured September 4, 2026 with system Python 3.9 on this Mac. `bench_engine.py` uses E1 vs V3_12 and
C1 vs `tape_yuan800_104892947`, seeds 1–4, with caching disabled.

## Engine speed

| Measurement | Before | After | Speed-up |
|---|---:|---:|---:|
| trace on, seconds/game | 0.7205 | 0.3225 | 2.23x |
| trace off, seconds/game | 0.7215 | 0.3220 | 2.24x |
| 1 worker | 1.33 games/s | 3.03 games/s | 2.28x |
| 2 workers | 2.54 games/s | 5.70 games/s | 2.24x |
| 4 workers | 4.23 games/s | 9.59 games/s | 2.27x |

The custom copier handles the observation's JSON-like `Struct`/dict/list/scalar tree directly. It retains a
separate copy for every agent call, so agent code cannot mutate engine state. `evaluate()` also accepts a
caller-owned `pool`, avoiding pool startup when the caller already has a persistent pool.

In the two-game profile, total time fell from 3.338s to 1.677s. `deepcopy` previously consumed 2.592s (78%);
the fast copier consumed 0.941s (56%). Engine interpretation was about 0.194s and agent entry points about
0.52s cumulative (roughly 31% after optimization). Agent `perceive()` alone was about 0.23s cumulative.

Correctness checks:

- Three sampled `Replays/Auto/mine/episode-*.json` files reproduced with `exact: true` before and after.
- Final money was identical for all 20 games: E1/V3_12 and C1/Yuan800, seeds 1–5, both seats.
- Debug mutation guards passed for both representative pairs; the guard deep-copies engine state and asserts
  equality after each agent call.

## Pattern-death calibration

The screen uses seed 1's existing fingerprint trace and adds no games. The results-branch `archive.json` was
fetched and inspected, but it contains aggregate/archive records rather than per-candidate traces, so it could
not be replayed for this calibration. Historical absolute paths in the local DBs were mapped to the matching
files in `evolve/gen/`.

| Archive | Candidates tested | Escape kills | Weed kills | Cash-trap kills | Held-pass false positives |
|---|---:|---:|---:|---:|---:|
| `evolve/evolve.db` | 8 | 1 | 1 | 0 | 0 |
| `evolve/v2test.db` | 8 | 0 | 0 | 0 | 0 |
| results `archive.json` | 0 (no traces) | — | — | — | — |

Both local kills were candidates already classified `dead_smoke`; two of the three smoke deaths in the usable
archive would therefore stop six games earlier. Applying that observed 2/3 catch rate to the reported 19 smoke
deaths per 269 candidates estimates 12.7 early kills and **76 smoke games saved per 269 candidates**. This is a
small-sample estimate; the A/B switch is `evolve/loop.py --no-pattern-death`.
