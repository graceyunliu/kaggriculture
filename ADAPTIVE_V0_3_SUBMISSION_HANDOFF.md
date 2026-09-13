# Adaptive v0.3 Submission Handoff

Concise handoff for actually submitting Adaptive v0.3 to the Kaggle ladder. Full rationale/validation is in `ADAPTIVE_V0_3_FAST_ITERATION_REPORT.md`.

## What is ready

- Package: `candidate/adaptive-v0.3-ladder-candidate/`
- Flat single-file submission (already built): `candidate/adaptive-v0.3-ladder-candidate/main.py`
- Zipped, ready to upload: `candidate/adaptive-v0.3-ladder-candidate/adaptive-v0.3-ladder-submission.zip`
  - sha256: `5d5a2e249f0dcd59fd2d8a00edb2a61bca3c4a46f7aff2cc7225a7c802d2d212`
- `preflight.py` passes (run it again yourself before submitting if you've touched anything: `python3 candidate/adaptive-v0.3-ladder-candidate/preflight.py`).

## One remaining manual step

Submitting to Kaggle requires the interactive Kaggle CLI with your own credentials, which this session does not have. On your machine, from the repo root:

```
kaggle competitions submit -c kaggriculture \
  -f candidate/adaptive-v0.3-ladder-candidate/adaptive-v0.3-ladder-submission.zip \
  -m "Adaptive v0.3: MIN_N_TO_TRUST_B=10 guard on frozen B-selection (v0.2 baseline reference: submission 56200714)"
```

(Matches the pattern used for v0.2's own submission per `pull_ladder.py`/the v2 README; adjust the competition slug if it differs from `kaggriculture` in your setup.)

If Kaggle's sandbox rejects `main.py` at the Validation Episode stage the way v0.2's FIRST attempt (56200346) did, the fix that worked for v0.2 (flat inlining, no sibling imports) is already applied here -- `main.py` has zero imports of local sibling files, only stdlib (`base64`, `hashlib`, `json`) plus whatever O42 itself imports. If it still fails, check the Kaggle error log first; do not "fix" it by editing the embedded O42/controller/learner-state content to work around a hash gate failure -- investigate why the content changed instead (same rule as `preflight.py`'s own instructions).

## After submission, record

Per the task's ask, once submitted please capture (a follow-up session can pull this via `pull_ladder.py` / `pull_leaders.py`, the same tooling used for v0.2 and O42):

- Kaggle submission ID and timestamp
- Number of completed episodes
- Score trajectory (initialScore/updatedScore per episode, chained -- see `KAGGLE_SCORE_RECONSTRUCTION.md` for the method)
- Win/loss record and money margins if available
- Opponent submission IDs (to check overlap with both v0.2's 41-game sample and O42's 71-game sample -- zero overlap between those two was already established and is a live confound for any comparison)
- Match-level per-game results (`LADDER_ADAPTIVE_V0_2_PER_GAME.csv` is the template format used for v0.2; produce an analogous `LADDER_ADAPTIVE_V0_3_PER_GAME.csv`)

## Explicitly out of scope for this handoff

- Do not conclude v0.3 "beats" or "loses to" O42 or v0.2 from a small number of games (hard constraint from the task spec).
- Do not attempt to reverse-engineer Kaggle's exact rating formula further (already partially reconstructed and documented as sufficient in `KAGGLE_SCORE_RECONSTRUCTION.md`/`SCORE_DIAGNOSTIC_AUDIT_HANDOFF.md`).
- v0.2 remains live on the ladder (submission 56200714) and is left untouched; this is a new, separate submission, not a replacement.
