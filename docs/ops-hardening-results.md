# Evolve loop operations hardening results

Date: 2026-09-05

## Outcome

The supervisor now detects statistically decisive held-out frontier challengers, persists a visible
human-review flag, alerts once per result, monitors consecutive proposal-generator failures, and
refreshes the replay-derived clone frontier once per two-hour segment. The H32 yardstick is also
calibrated from the previously stranded frozen P6 reference.

The established decisive convention was not ambiguous: `evolve/cascade.py` defines a held-out pass
as margin greater than zero and `t >= 2.0`. `evolve/check_frontier.py` reuses that exact bar and only
compares rows whose run recorded the currently configured frontier.

## Task 1 — frontier promotion review

`evolve/check_frontier.py` joins `candidates` to `runs`, selects the strongest `held_pass` row at
stage 3 or later for the current frontier, and writes `evolve/PROMOTION_PENDING.txt`. It sends the
existing `notify.sh text` alert only when that exact result has not already been alerted. Notification
success is tracked separately from the review flag, so a failed Hermes/ntfy delivery is retried while
the pending review remains prominent. The supervisor logs the flag at the start of every segment and
runs the check after result publication.

Synthetic verification used a temporary SQLite database and a recording notification stub:

```text
candidate evolve/gen/cand_fake.py beats current frontier candidates/H32.py by $12,345/game (t=3.25) — review for promotion
promotion alert already sent; flag remains pending
notification calls after two checks: 1
after deleting the fake row and clearing the flag:
frontier check: no decisive held-out winner against candidates/H32.py
```

## Task 2 — proposal generator health

`evolve/propose_health.sh` persists `count alerted` in
`evolve/logs/propose_failures.count`. A successful proposal invocation writes `0 0`. Failures
increment the count; at the default threshold of three, the helper sends the last error through the
same notification channel. The alert bit prevents repeated alerts on later failed segments, while a
failed notification remains eligible for retry. A missing `claude` executable is now treated as a
generator failure rather than silently skipping the generator.

Synthetic verification:

```text
failure 1 -> state 1 0
failure 2 -> state 2 0
failure 3 -> state 3 1, notification sent
failure 4 -> state 4 1, no second notification
success   -> state 0 0
```

## Task 3 — replay frontier refresh

The supervisor runs `refresh_frontier.py` after each pull and before resolving `CLONE_NOW`. The
configured segment is two hours, and the measured no-corpus scan took 0.05 seconds, so a separate
longer timer would add state and failure modes without meaningful savings. If refresh returns no data
or fails, the supervisor logs it and leaves the existing selection logic unchanged: a valid
`Opponents/frontier.txt` wins, otherwise `Opponents/tape_yuan800_104892947.py` remains the fallback.

Dry-run and live-run output were identical and safe:

```text
no scouted replays found under Replays/Auto/leaderboard-*/ — run sync_replays.py leaderboard first
dry-run elapsed: 0.05s; rc=1
live run: rc=1; Opponents/frontier.txt and Opponents/tapes.json unchanged
```

This is the one requested verification that could not produce an update cleanly within scope. The
available replay tree contains 892 files under `Replays/Auto/mine` but zero under the
`leaderboard-*` layout that `refresh_frontier.py` intentionally consumes. Existing
`Opponents/frontier.txt` still points to `Opponents/tape_milanleonard_102563171.py`. No replay was
moved or relabeled merely to manufacture a live update.

## Task 4 — measured H32 calibration

`candidates/P6_baseline.py` was already present on `origin/main`, and `cmp` confirmed it is
byte-for-byte identical to the working `candidates/P.py`. That matches the documented frozen P6
control and its prior -$9,374/game result against H10. The previously untracked
`tools/calibrate_yardstick.py` is now included.

Fresh H32 calibration, seeds 1-10 and both seats:

```text
C1         margin=    -37097  t= -9.33  W-L=0-10
P6         margin=    -27792  t= -5.99  W-L=0-10
H32_self   margin=         0  t=   inf  W-L=0-0

Reference margins: mean=-32445 stdev=4652
Suggested SMOKE_FLOOR  ≈ -37000
Suggested DEV_PROMOTE  ≈ -32000
```

The committed calibration uses `SMOKE_FLOOR=-37000`, the measured loose floor, and
`DEV_PROMOTE=-28000`, near P6's own measured margin rather than the two-reference mean. This lets a
competitive P6-class candidate survive smoke while requiring approximately P6-level performance to
reach development promotion. `FRONTIER` is now `candidates/H32.py`, and the comment records the
measurement and date rather than describing an estimate.

## Verification summary

```text
python3 -m unittest -v tests/test_ops_hardening.py
Ran 2 tests in 0.116s — OK

python3 -m py_compile evolve/check_frontier.py tools/calibrate_yardstick.py
bash -n evolve/supervisor.sh evolve/propose_health.sh evolve/notify.sh
git diff --check
python3 -c "import candidates.H32; import candidates.P6_baseline"
candidate imports: OK
```
