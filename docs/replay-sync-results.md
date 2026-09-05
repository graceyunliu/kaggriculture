# Leaderboard replay sync: scheduling and disk retention (Sep 5)

## Background

`evolve/refresh_frontier.py` was already wired into `supervisor.sh` (ops-hardening pass,
commit `a6de34f`) to run once per segment, but nothing fetched fresh leaderboard replays
for it to cluster — `Replays/Auto/leaderboard-*/` was empty. This closes that gap.

## What was verified manually on the Air before writing any code

- Kaggle CLI: the classic `pip3 install kaggle` (system Python 3.9.6) installs the old
  username/key (`kaggle.json`) auth flow, not the `access_token` flow `sync_replays.py`'s
  docstring describes. The newer kagglesdk-based CLI (v2.2.4) needs Python 3.11+.
  Installed via `brew install python@3.11` then
  `/opt/homebrew/bin/python3.11 -m pip install kaggle` — this does **not** touch the
  Air's system Python 3.9.6, which the evolve loop itself continues to run on unchanged.
  The old, PATH-shadowing 3.9 `kaggle` install was uninstalled (`pip3 uninstall kaggle`)
  so plain `kaggle` on PATH now unambiguously resolves to `/opt/homebrew/bin/kaggle`.
  Auth verified working: `kaggle competitions list -s kaggriculture` returns real data.
- `python3 sync_replays.py leaderboard 2 --max-episodes 2` — pulled 4 real episodes
  (2 teams), ~30-31MB each (`Replays/Auto/leaderboard-keiz/` = 61MB,
  `Replays/Auto/leaderboard-Jesse_Bullard/` = 62MB, 2 episodes each), ingested cleanly
  into `kaggriculture.db`.
- `python3 evolve/refresh_frontier.py --dry-run` on that real data found 2 new opening
  clusters (50%/50% share) and proposed `tape_jessebullard_105739218.py` /
  `tape_keiz_105739216.py` correctly — confirms the full chain works end to end.

## What this change adds

1. **`evolve/supervisor.sh`**: a daily-gated block (state file
   `evolve/logs/replay_sync_last_run`, 86400s minimum interval — mirrors the existing
   `propose.py` rate-limiting pattern) placed before the existing `refresh_frontier.py`
   call, so a fresh sync is available to the same segment's clustering pass:
   - Guards with `command -v kaggle` first; if missing, logs a message and skips
     rather than failing the segment — so this is harmless on any machine without the
     Kaggle CLI set up (only the Air has it as of this change).
   - Runs `sync_replays.py leaderboard 5 --max-episodes 10` (bounded per-call growth:
     worst case ~5 teams x 10 episodes x 30MB = 1.5GB on a cold start; steady-state
     growth is much smaller since dedup skips already-downloaded episodes).
   - Runs the new `evolve/prune_replays.py --max-age-days 10` immediately after.
   - Logs `du -sh Replays/Auto/leaderboard-*` once/day so growth is visible in
     `supervisor.log` without SSHing in to check.
   - All three steps use `|| say "... (continuing)"` — never blocks or crashes the
     main evolution loop on a transient Kaggle API failure.

2. **`evolve/prune_replays.py`** (new): deletes replay JSON files under
   `Replays/Auto/leaderboard-*/` older than `--max-age-days` (default 10). Only touches
   `leaderboard-*/`, never `Replays/Auto/mine/` (the project's own submission history —
   separate retention concern, out of scope here). Safe by construction:
   `sync_replays.py`'s dedup (`already_downloaded()`) scans the filesystem for episode
   ids, not a database, so a pruned episode could at worst be re-downloaded later if it
   resurfaces in a "new" window — harmless extra bandwidth, never incorrect data.
   `--dry-run` reports without deleting; removes now-empty team directories after a
   real prune.

## Why 10 days

An opening fingerprint (turn-1/turn-2 market orders) is fixed early and
`refresh_frontier.py` clusters on it every segment (at most a few hours old at most).
There is no ongoing value in keeping raw replay JSON once it has been clustered at
least once — 10 days gives ample margin for that to have happened (segments run every
2h) while keeping steady-state disk usage bounded to roughly one day's worth of fresh
pulls plus up to 10 days of accumulation before the oldest files roll off. If disk
pressure is ever observed in practice, lowering to 3-5 days is a one-line change
(`--max-age-days` argument, or the hardcoded `10` in `supervisor.sh`'s call).

## Verification performed

1. `bash -n evolve/supervisor.sh` — syntax OK.
2. `python3 -c "import ast; ast.parse(...)"` on `prune_replays.py` — parses OK.
3. Functional test of `prune_replays.py`: created one synthetic old file (mtime forced
   to Jan 2024) and one fresh file under a test team directory. `--dry-run` correctly
   identified only the old file; a real run deleted only the old file, kept the fresh
   one, and left the (non-empty) directory in place.
4. Isolated test of the daily-gate logic (extracted the exact gate snippet used in
   `supervisor.sh`): first call fires and stamps `evolve/logs/replay_sync_last_run`;
   an immediate second call is correctly skipped with a clear log line, not silently
   and not with an error.
5. Not re-run end-to-end against a live `supervisor.sh` segment in this pass (that
   requires the Kaggle-CLI-authenticated Air itself, already manually verified
   piece-by-piece above); the Air's own `git pull --ff-only` at the top of its loop
   will pick up this commit automatically on its next segment.

## Not done / explicitly out of scope

- `Replays/Auto/mine/` retention (own-submission history) — untouched, separate concern.
- Any change to `sync_replays.py` or `refresh_frontier.py` themselves — both already
  verified working correctly; this change is purely scheduling + retention around them.
- No credentials of any kind were added to this repo. The Air's local
  `~/.kaggle/access_token` setup is machine-local and out of scope for version control.
