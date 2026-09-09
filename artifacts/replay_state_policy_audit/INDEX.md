# Replay State-Conditioned Policy Audit - Index

## ⚠️ PROVENANCE CORRECTION (READ FIRST)

**Throughout Phases 1, 2, 3, and 4A, every "opponent" / "opp" data point
means the opposing seat observed inside Grace's own game history
(`Replays/Auto/mine/`) - NOT an independently sampled leaderboard/ladder
reference population.**

Phases 1-3 additionally scanned 304 files from
`Replays/Auto/leaderboard-*/` and `Replays/Leader Replays/` directories and
reported file counts / directory names from that scan. Phase 4A discovered
that **none of those 304 files contain a `graceyunliu` game** - they are
games between other Kaggle competitors and contributed **zero rows** to any
mine-vs-opp comparison in any phase. The "opp" cohort in every finding, in
every phase, was always sourced entirely from the non-Grace seat within
`Replays/Auto/mine/` games - i.e. the specific set of rivals Grace has
actually played, not a separately curated or independently sampled
reference population.

**What this means for reading any earlier phase's language:**
- Phrases like "opponent field," "pooled opponent field," or "84/306
  distinct opponent identities" refer to the *variety of rivals Grace has
  played*, which is a real and fairly broad set - but it is **not a random
  or representative sample of the whole competitive ladder**. It is
  whichever opponents happened to be paired against Grace by the matchmaking
  process that produced her game history.
- Any generalization from these phases ("agents systematically do X") should
  be read as **"agents Grace has actually played systematically do X,"**
  not as a claim about the full leaderboard population.
- This does **not** invalidate the statistical findings themselves (sample
  sizes, significance tests, effect sizes in Phase 4A are unaffected by this
  correction - they were always computed over the correct, actually-used
  data). It only corrects the *population the findings generalize to*.
- No numbers, findings, or verdicts in `REPORT.md`, `REPORT_PHASE2.md`,
  `REPORT_PHASE3.md`, or `REPORT_PHASE4A.md` have been changed. Each of
  those four files now carries a short correction note near its top
  pointing back here.

## Phases

| Phase | Report | One-line summary |
|---|---|---|
| 1 | [REPORT.md](REPORT.md) | Initial replay inventory + day-boundary state-conditioned mining; found a repeatable strawberry-vs-wheat crop-mix divergence, RNG-exposed, not causal. Status: PARTIAL_EVIDENCE. |
| 2 | [REPORT_PHASE2.md](REPORT_PHASE2.md) | Intra-day decision-triggered resampling (fixing Phase 1's day-boundary blind spots); found genuine parity on fertilizer/chore, corroborating (not new) crop-mix evidence, melon hold/sell noted as an open thread. Status: PARTIAL_EVIDENCE. |
| 3 | [REPORT_PHASE3.md](REPORT_PHASE3.md) | Reconstructed true HIRE/MELON opportunity gates from engine code, converting "action happened" data into "opportunity existed, action taken or not" data; surfaced the melon-opportunity action-rate gap as the most promising lead (PLAUSIBLE_BUT_UNPROVEN, n=24 actions). Status: PARTIAL_EVIDENCE. |
| 4A | [REPORT_PHASE4A.md](REPORT_PHASE4A.md) | Statistically confirmed the melon-opportunity divergence at scale (Fisher's exact p=7.1e-169, rate ratio 3.13 [2.88,3.40], cluster-bootstrap CI [2.09,4.77] excluding 1); also the source of this provenance correction. Promoted to STRONGLY_SUPPORTED for existence/robustness only - no causal or performance claim. Status: CONFIRMED (behavioral divergence exists). |
| 4B | [REPORT_PHASE4B.md](REPORT_PHASE4B.md) | Minimal causal intervention test of the melon-opportunity divergence on isolated policy-variant copies (not the champion). Diagnostic only - see report for the pre-registered predictions and per-prediction pass/fail results. |
| 5 | [REPORT_PHASE5_EXPANSION_GATE.md](REPORT_PHASE5_EXPANSION_GATE.md) | Applied this audit's opportunity-reconstruction method to the EXPANSION (BUY_LAND) decision, following up on TDAS's (arch_search/) falsified H1 labor-timing hypothesis. Found a large, statistically robust gap in land-expansion reach rate (59.3% vs 90.0%, non-overlapping CIs) with no RNG/hidden gate involved (RNG_INDEPENDENT); the likely mechanism (cash allocated elsewhere) is PLAUSIBLE_BUT_UNPROVEN, not causally isolated this round. Status: PARTIAL_EVIDENCE. |

## Machine-readable findings

`FINDINGS.json`, `FINDINGS_PHASE2.json`, `FINDINGS_PHASE3.json`,
`FINDINGS_PHASE4A.json`, `FINDINGS_PHASE4B.json` - one array per phase, same
field shape (extended per-phase as needed; see each phase's report for the
schema notes). Their `agents_or_cohorts` fields already use the generic
labels `"mine (graceyunliu)"` / `"pooled opponent field"` and do not
themselves contain a "leaderboard" or "ladder" provenance claim, so they
were **not edited** for this correction - the correction is a population-
interpretation note, not a data-labeling fix. (`FINDINGS_PHASE4A.json` does
mention "leaderboard" directories, but only inside its own methodological
finding entry that documents this exact discovery - that mention is
accurate and was left as-is.)

## Standing constraints across all phases (unchanged)

Read-only except the isolated artifact/experiment files each phase creates.
No champion, submission, `evolve/cascade.py`, or parent-selection edits. No
strategy changes. No dev-margin-as-causal claims. No ranking agents by
replay-derived "skill." No whole-game-score-as-mechanism claims. No
promoting ASSOCIATED/HYPOTHESIZED evidence to causal status without direct
supporting evidence.
