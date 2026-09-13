HYPOTHESIS: Adaptive v0.2's frozen (ladder-eval) selector deviates from O42 (picks variant B_ONE_PER_ORDER) in several regimes where B's empirical mean is estimated from only 1-6 real training games, and its "frozen_greedy" selection is plain greedy on those noisy means (UCB1's explore bonus is negligible once game counts are fixed at eval time) -- so some live deviations from O42 rest on statistically thin evidence rather than a reliably-better B.
CHANGE: Added a single guard, MIN_N_TO_TRUST_B=10, to the certified v0.2 controller's `Learner.choose()`: in frozen mode, if the greedy pick is B_ONE_PER_ORDER but that regime's B sample count is below 10, fall back to A_FULL_O42 (O42's own unmodified behavior) instead. Training-time UCB1 behavior, the learner's own (n, mean) statistics, the regime partition, reward window, and O42 are all unchanged.
STATUS: READY_FOR_LADDER

# Adaptive v0.3 Fast Iteration Report

## 1. v0.2 evidence used

- `artifacts/ladder_adaptive_v0.2_diagnostic_2026-09-13/derived/LADDER_ADAPTIVE_V0_2_RAW_EVIDENCE.md` and `LADDER_ADAPTIVE_V0_2_DIAGNOSTICS.json`: established v0.2's live ladder identity (Kaggle sub 56200714 vs O42's 56175177), that raw per-game money-margin/win-rate for v0.2 (mean margin +$3,367, 20W/21L, n=41) is NOT dramatically worse than O42's (+$1,929, 36W/35L, n=71), and that Kaggle's displayed score gap (895.9 vs 1174.0) is explained by a sequential, path-dependent rating system with zero opponent overlap between the two submissions' samples -- i.e. the ladder score gap does not by itself establish that v0.2's underlying decisions are worse.
- `KAGGLE_SCORE_RECONSTRUCTION.md` / `SCORE_DIAGNOSTIC_AUDIT_HANDOFF.md`: confirmed no production ladder decision trace (regime/arm/learner-state at decision time) is recoverable from Kaggle's replay format, so v0.3's hypothesis had to be tested against the certified offline frozen learner state, not live-ladder traces.
- `candidate/adaptive-v0.2-ladder-candidate/state/learner_frozen.json` (certified v0.2 frozen state, sha256 `d8864c049b78da94329a9cb10184acec31582bff7c2afb062400af2c42173c64`, pulled unmodified from `/tmp/ladder_submit/candidate/adaptive-v0.2-ladder-candidate/` where the certified/hardened v0.2 package was packaged, commit-tagged `58dd51b` per its zip filename): read directly. Of 7 regimes, 4 have an arm with n<=6: `early|high|tight` (A n=1), `early|low|tight` (A n=4), `late|high|roomy` (A n=1, B n=4), `late|high|tight` (A n=1, B n=2), `mid|high|roomy` (A n=3), `mid|low|roomy` (A n=1, B n=4). Held-out selection counts (from `provenance_manifest.json`, carried from the certified audit) show B was picked 261/309 times vs A 48/309 -- a strong, possibly evidence-outrunning preference for B.
- `adaptive/README.md`-adjacent project memory (`kaggriculture-buy-animal-commit-panel-audit-sep13.md`, `kaggriculture-animal-formation-canonical-panel-audit-sep13.md`): established, independently and adversarially, that O42's own day-8 animal-purchase divergence is a genuine successful-commit-volume effect, not a measurement artifact -- relevant context confirming O42's animal-purchase behavior (the exact boundary the adaptive controller sits on) is a real, trustworthy signal, not noise from an instrumentation bug, so a controller change at that boundary is meaningful.

## 2. Selected hypothesis

Stated above (HYPOTHESIS line). In short: some of v0.2's live B-selections are supported by too little data to trust, and B is picked far more often than A overall (261 vs 48 held-out), so any noise in a handful of B estimates has outsized influence on deployed behavior.

## 3. Why this hypothesis was selected

It was the most directly testable against data already in hand (the frozen learner state), required no new offline study, and maps cleanly onto one of the pre-approved small interventions ("require minimum sample size before trusting B" / "restrict B selection when evidence is weak"). Alternative hypotheses considered and set aside for this iteration: (a) reward-horizon misalignment (24-turn window vs eventual ladder outcome) -- plausible but would require redefining the reward function, a larger change than "smallest reasonable"; (b) missing state-partition distinctions -- no specific missing distinction was evidenced by existing data, so inventing one would violate the "only if evidence clearly shows a specific missing distinction" constraint; (c) early-game B exposure causing downstream damage -- the `early|*` regimes here are actually the BEST-supported (n=45, n=13) and are unchanged by this fix, so this did not look like the highest-value target once the per-regime n's were inspected directly.

## 4. Exact code change

File: `candidate/adaptive-v0.3-ladder-candidate/controller/adaptive_slice_v0.py` (copied from the certified v0.2 controller, sha256 `9ff99b50656c1ed19b4410d773a83946082bb6f88d605020615dcb3c8e735687`; v0.3 result sha256 `1e7393a52664558ff5bc132121f30f39fceb7a41401ad40097e0f72874afbe4f`).

Added constant:
```python
MIN_N_TO_TRUST_B = 10
```

Changed `Learner.choose()`, added 4 lines after the existing greedy/UCB1 selection:
```python
        v = max(VARIANTS, key=lambda x: (scores[x], -VARIANTS.index(x)))
        if frozen and v == "B_ONE_PER_ORDER" and st["B_ONE_PER_ORDER"]["n"] < MIN_N_TO_TRUST_B:
            return VARIANTS[0], {"algorithm": "frozen_greedy_min_n_guard", "scores": scores,
                                  "reason": "insufficient_B_support", "b_n": st["B_ONE_PER_ORDER"]["n"],
                                  "min_n_to_trust_b": MIN_N_TO_TRUST_B, "would_have_selected": v}
        return v, {"algorithm": "frozen_greedy" if frozen else "UCB1", "scores": scores}
```
The guard only fires when `frozen=True` (i.e. ladder/eval-time decisions), never during training (`learning=True, frozen=False`), and it never calls `learner.update()` or otherwise touches `learner_frozen.json`.

Effect on the 7 certified v0.2 regimes (recomputed directly, see `provenance_manifest.json` -> `v0_3_change`):

| Regime | v0.2 pick | v0.3 pick | B's n |
|---|---|---|---|
| early\|high\|tight | B | B (unchanged) | 45 |
| early\|low\|tight | B | B (unchanged) | 13 |
| late\|high\|roomy | B | **A** (flipped) | 4 |
| late\|high\|tight | B | **A** (flipped) | 2 |
| mid\|high\|roomy | B | B (unchanged) | 53 |
| mid\|high\|tight | A | A (unchanged) | 6 (A already won) |
| mid\|low\|roomy | B | **A** (flipped) | 4 |

3 of 7 regimes flip to O42's own behavior; the 3 best-supported B regimes (n=13, 45, 53) are untouched.

## 5. What was intentionally NOT changed

- `state/learner_frozen.json` -- byte-identical to v0.2 (sha256 `d8864c049b78da94329a9cb10184acec31582bff7c2afb062400af2c42173c64`). No retraining.
- `runner/adaptive_eval_v0_2.py`, all `config/*.json` -- byte-identical to v0.2 (hashes verified, recorded in `provenance_manifest.json`).
- Regime partition function (`regime()`), `state_vector()`, `apply_variant()`, reward window (24 turns), UCB1 training-time formula -- all unchanged.
- O42 (`candidates/O42_MAX_HANDS_LATE_EXPAND.py`) -- unmodified, hash reconfirmed below.
- The MIN_N_TO_TRUST_B threshold (10) was chosen as a round number clearly separating the observed "thin" cluster (n=1-6) from the "well-supported" cluster (n=13-53) in this specific frozen state; it was not fit/tuned against any held-out or ladder outcome.

## 6. Lightweight validation results

- `python3 -m ast.parse` / manual syntax check: OK.
- Unit tests (`tests/test_min_n_guard.py`, 6 tests, run with plain `python3 tests/test_min_n_guard.py`, no pytest dependency): 6/6 passed, including a regression-pin test against the real certified v0.2 frozen state (confirms exactly the 3 regimes above flip, no more, no fewer) and a determinism/no-mutation test confirming `choose()` never calls `update()`.
- `preflight.py`: PREFLIGHT OK (all hashes -- controller (new v0.3 hash), runner, learner state, all configs, O42, all 3 opponent files -- verified against `provenance_manifest.json`).
- O42 hash independently reconfirmed via `shasum -a 256 candidates/O42_MAX_HANDS_LATE_EXPAND.py`: unchanged.
- Smoke test: loaded the real O42 agent via `load_agent()`, constructed `WrappedAgent` in `adaptive_frozen` mode with the real frozen state loaded, confirmed no crash, confirmed `regime()`/`apply_variant()` behave sanely, confirmed no learner mutation across repeated `choose()` calls. Full `kaggle_environments`-driven game episode was not run in this pass (kaggle_environments availability in the working shell was not confirmed) -- this matches the depth of pre-submission checking already documented for v0.2's own package.
- Built the flat single-file Kaggle submission (`main.py`, `build_submission.py`) using the same embed/rename/hash-gate method documented for v0.2's submission-v2 fix; imported it directly and confirmed `agent` is callable, the embedded `_o42_agent` (renamed O42 entrypoint) is callable, `MIN_N_TO_TRUST_B == 10` is present in the built file, and all 7 regimes load with the correct (n, mean) values.
- `git diff`/`git status` reviewed: only files under `candidate/` and these two report files are staged for this commit; no other repo changes are part of it.

## 7. Candidate hashes

- Controller (v0.3): `1e7393a52664558ff5bc132121f30f39fceb7a41401ad40097e0f72874afbe4f`
- Controller (v0.2, unchanged reference): `9ff99b50656c1ed19b4410d773a83946082bb6f88d605020615dcb3c8e735687`
- Runner (unchanged from v0.2): `f434cffccd641e545bba7bc97da6658740b4d5537f789eaf57e1f051f1df0113`
- Frozen learner state (unchanged from v0.2): `d8864c049b78da94329a9cb10184acec31582bff7c2afb062400af2c42173c64`
- `config/experiment_configuration.json` (unchanged): `ab1922217cc06fc160d8f513f576e321321c52561da137cb8ed6c6434c17adc3`
- `config/seed_manifest.json` (unchanged): `837be728116269b38f4e445cac83e4bd422ed9c2a4031d77833a3be326b5fabc`
- `config/opponent_manifest.json` (unchanged): `6b18166995b117c1b607f1576a0e09ed7bc26da567ff7f477fab8d083802cb2d`
- Built submission `main.py`: `ac2f63786894d1dfb132019b0cdc701a8910523150627262164f196363e764eb`
- Submission zip `adaptive-v0.3-ladder-submission.zip`: `5d5a2e249f0dcd59fd2d8a00edb2a61bca3c4a46f7aff2cc7225a7c802d2d212`

## 8. O42 hash

`154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813` -- confirmed unchanged (reconfirmed directly against `candidates/O42_MAX_HANDS_LATE_EXPAND.py` on disk during this iteration; not touched at any point).

## 9. Git commit SHA

See the commit that introduces this report and the `candidate/adaptive-v0.3-ladder-candidate/` and `candidate/adaptive-v0.2-ladder-candidate/` directories in this repository (this report is committed in the same commit; check `git log -1` for the SHA at HEAD after this commit).

## 10. Submission readiness

The flat single-file `main.py` and `adaptive-v0.3-ladder-submission.zip` are built and hash-gated, ready to submit. See `ADAPTIVE_V0_3_SUBMISSION_HANDOFF.md` for the one remaining manual step (interactive Kaggle CLI submission).

## 11. What ladder result would support/weaken the hypothesis

- **Supports**: v0.3's ladder score/trajectory is at or above v0.2's on a comparable number of games, OR v0.3's raw money-margin distribution over its early games (particularly ones landing in `late|high|roomy`, `late|high|tight`, `mid|low|roomy`) shows fewer large negative outliers than v0.2's did in the same regimes. Neither is independently confirmable from Kaggle's replay format (no regime/arm trace is exposed, per the score-diagnostic evidence above) -- so this would be an indirect, descriptive comparison at best, not a controlled one.
- **Weakens**: v0.3 performs distinguishably worse than v0.2 on a comparable sample, which would suggest the flipped-to-A regimes were in fact valuable B deviations despite thin support (i.e. the guard is overly conservative for this particular game), or that the true driver of v0.2's ladder standing lies elsewhere (opponent population, reward horizon, etc.) and this change is a no-op or mild negative.
- A single noisy game must not be used to judge either direction (hard constraint); at minimum a sample on the order of v0.2's own 41 real-opponent games would be needed before any comparative read, and even then opponent-population differences (already documented as unresolved for v0.2 vs O42) would still confound a v0.3-vs-v0.2 read unless opponent overlap is checked directly.

## 12. Known uncertainty

- This is a controller-only change validated by unit tests and a static/import-level smoke test, not a full offline re-run of the 320-game-style study; whether the 3 flipped regimes are net-helpful, net-neutral, or net-harmful in live play is exactly what ladder submission is meant to find out, and is not claimed here.
- MIN_N_TO_TRUST_B=10 is a reasonable, evidence-motivated round-number threshold given the sharp n=1-6 vs n=13-53 split observed in this specific frozen state, not a value derived from a formal statistical power calculation or tuned against any outcome.
- The flat `main.py` build was smoke-tested by direct import, not by a live `kaggle_environments` game run in this session (tooling availability unconfirmed) -- this is the same level of pre-submission verification already accepted for v0.2's own submitted package, not a new gap introduced here.
- No production ladder decision trace exists for v0.2 (confirmed by the score-diagnostic evidence), so this change cannot be validated against v0.2's actual live-play regime distribution -- only against the certified offline frozen state, which is what v0.2's own ladder submission was built from.
