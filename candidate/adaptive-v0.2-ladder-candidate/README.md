# adaptive-v0.2-ladder-candidate

A frozen, packaged copy of the independently audited (verdict A — CLEARED)
Adaptive Eval v0.2 mechanism. This package changes nothing about the
learner, reward function, regime definitions, or O42 — it only packages
the certified artifacts with provenance and a fail-closed preflight check.

## What is in this package

| File | Role | SHA256 |
|---|---|---|
| `controller/adaptive_slice_v0.py` | Certified controller (regime function, Learner, WrappedAgent) | `9ff99b50656c1ed19b4410d773a83946082bb6f88d605020615dcb3c8e735687` |
| `runner/adaptive_eval_v0_2.py` | Certified train/held-out evaluation runner, with built-in O42/controller hash gates | `f434cffccd641e545bba7bc97da6658740b4d5537f789eaf57e1f051f1df0113` |
| `state/learner_frozen.json` | Certified v0.2 frozen learner state (7 regimes, empirical (n, mean) per arm) | `d8864c049b78da94329a9cb10184acec31582bff7c2afb062400af2c42173c64` |
| `config/experiment_configuration.json` | Certified experiment config | `ab1922217cc06fc160d8f513f576e321321c52561da137cb8ed6c6434c17adc3` |
| `config/seed_manifest.json` | Certified train/eval seed split | `837be728116269b38f4e445cac83e4bd422ed9c2a4031d77833a3be326b5fabc` |
| `config/opponent_manifest.json` | Certified opponent roles + hashes | `6b18166995b117c1b607f1576a0e09ed7bc26da567ff7f477fab8d083802cb2d` |
| `config/environment.json` | Certified run environment record | `7465a2e2592c138c3b90aa8336cc17ce11c936804d89ed0a9bb77b109586cb40` |
| `provenance_manifest.json` | This package's own provenance record | (see file) |
| `preflight.py` | Fail-closed hash gate; run before anything else | (see file) |

Every hash above was independently recomputed during hardening (2026-09-13)
and matches, byte-for-byte, the corresponding certified v0.2 artifact
(`ADAPTIVE_EVAL_V0_2_FINAL_AUDIT.md`). No content was altered.

## Not included (by design)

- **O42** (`candidates/O42_MAX_HANDS_LATE_EXPAND.py`, sha256
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`) is
  **not copied** into this package. It lives outside this repository, in a
  separate connected project folder
  (`/Users/graceliu/Claude/Projects/Kaggriculture/candidates/`), and is
  referenced by absolute path + hash only. It is never modified by this
  hardening effort. Running the candidate requires that exact file at that
  path (or an equivalent path you configure), and `preflight.py` will
  refuse to run if its hash does not match.
- Opponent files (`opp_scenario_v14.py`, `opp_frontier_v12.py`,
  `opp_soil_v25.py`) are likewise referenced by hash in
  `provenance_manifest.json` rather than copied, since they are shared
  research assets used elsewhere in the repo.
- No new experiment, tuning, or learning code is included. This package
  cannot retrain, re-tune A/B, or modify O42.

## Reproduction procedure

1. Run `python3 preflight.py` from this directory. It must print
   `PREFLIGHT OK` before you do anything else. If it fails, STOP — do not
   proceed, and do not "fix" it by editing O42, the controller, or the
   frozen state to match; investigate why the file changed instead.
2. Minimal sufficient check performed during hardening (2026-09-13): every
   file in this package was diffed byte-for-byte against its certified
   source in the main repo (`adaptive/provenance/adaptive-eval-v0.2/...`,
   `adaptive/logs/adaptive-eval-v0.2-run1/learner_frozen.json`) and found
   identical (`diff` reported no differences on all of controller, runner,
   and frozen learner state). This is sufficient to establish that the
   candidate package is an unmodified copy of the certified mechanism; it
   does not itself re-run the experiment.
3. To reproduce the full certified evaluation (optional, not required to
   trust this package): use a Python 3.12.13 environment with
   `kaggle_environments==1.32.3` (see `config/environment.json`) and invoke
   `runner/adaptive_eval_v0_2.py` with the certified seed/opponent
   manifests, pointing `--o42` at the external O42 file above. The runner's
   own built-in `CERTIFIED_O42` / `CERTIFIED_CONTROLLER` constants will
   raise `SystemExit` if either input's hash has drifted, both before and
   after execution.

## Known limitations (inherited from the certified audit; not introduced here)

- The certified performance result did **not** establish adaptive
  superiority: Adaptive − Fixed A = +$423.84 (95% CI [−$6,088, +$6,936]);
  Adaptive − Fixed B = −$1,392.97 (95% CI [−$6,058, +$3,273]). Both CIs
  straddle zero widely. **This candidate inherits the certified
  mechanism-generalization result, not a superiority claim, and none is
  made here.**
- Several individual regimes have thin training support (single digits);
  the *direction* of learned preference generalized held-out, but
  per-regime statistical reliability was not established.
- The main repository (outside this candidate folder) lacked git history
  prior to this hardening pass; see `ADAPTIVE_CANDIDATE_HARDENING_REPORT.md`
  at the repo root for the git-provenance step taken during hardening.
- O42 lives in a separate project folder outside this repository — a real
  packaging dependency, documented rather than hidden.
