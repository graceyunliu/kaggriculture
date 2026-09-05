# Codex brief — retest region-assignment sweep fix alone on P6 (P7b)

Copy everything below the line into Codex.

---

You are re-testing one specific, already-partially-validated fix in isolation, after it was previously bundled with an unrelated failed change and discarded along with it. This is a small, low-risk task — do not expand its scope.

## Location — read this first
There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

`cd` there; all relative paths below are relative to it. Do **not** open or modify anything under `/Users/graceliu/Documents/ChatGPT/Kaggriculture`, `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture`, `Archived versions/`, `Chatgpt Agents/`, `Perplexity Agents/`, `User Notebooks/`, or `/Users/graceliu/Downloads`. Other sessions may be concurrently working in `candidates/K.py`, `candidates/M3_GENERAL_SIZING.py`/`P7.py` and their branches, `tools/`, and `Opponents/schedules/` — do not touch those paths. `candidates/H32.py`/`M2.py` are frozen references; do not edit them.

Work on branch `codex/region-assignment-retest`, forked from the commit that has `candidates/P.py` = P6 and `candidates/P6_baseline.py` (the frozen P6 copy from the P7 attempt — read `docs/planner-results.md`'s "P7 — coupled allocation + hiring" section first for full context on why this fix was pulled out).

## Background

In the P7 pass, the region-assignment sweep fix was implemented and bench-tested **in isolation, before** being combined with an unrelated (and ultimately rejected) hiring-model change:

> "The sweep experiment was isolated first. Crop-pool positions are serpentine-sorted and divided into contiguous runs for units not already assigned animal/setup work; `_build_sweep` prefers the unit's run for its first tile and falls back to the global pool. On H32_s1 days 13–27 it was exactly neutral versus P6: travel 1.008, cov_all 0.963, cov_hard 0.999, with two failed actions and new-weeds delta −1."

That isolated version was never run through full games — it was folded into P7 (which failed for unrelated hiring-model reasons) and removed along with it when P7 was rejected. This task is: reconstruct that isolated version on top of clean P6, and take it all the way through full-game validation on its own, since it was never actually disqualified — it just never got a fair test.

## Task

1. Reconstruct the region-assignment fix as described above, applied to a fresh copy of P6 (`candidates/P.py`) only — do not include any part of P7's hiring/admission changes. Name the candidate `candidates/P7b.py` (or via `tools/render_p.py` if that's the established pattern for this codebase — check how P6 itself was produced).
2. Bench-confirm it reproduces the previously-reported neutral numbers: H32_s1 days 13–27 travel ≈1.008, cov_all ≈0.963, cov_hard ≈0.999; E1_s1 full ledger cov_hard ≈1.002, cov_all ≈1.000. If these don't match closely, the reconstruction is wrong — fix before proceeding to full games.
3. Since the bench result is only neutral (not a clear win), the real question this task answers is whether it's neutral-to-positive or neutral-to-negative in full games — a coverage/travel tie on the bench doesn't guarantee a full-game tie, since the bench measures execution on the tape's own state, not on states P7b reaches on its own. Run the full acceptance ladder:
   - P7b vs P6 head-to-head, seeds 1–10, both seats (fast first check).
   - P7b vs P6 head-to-head, held-out seeds 11–30, both seats — this is the primary signal. Report margin, t, W-L plainly regardless of direction.
   - P7b vs E1, seeds 1–10 and 11–30, both seats — must not regress P6's existing E1 margins (~+$2,551/game on 1-10 per the P7 report; ~+$1,963/game on 11-30 per the P6 report) by more than noise.
   - P7b vs V3_12 and H10, seeds 11–30, both seats — must not regress P6's existing margins.
4. Do not attempt any additional fixes, tuning, or the hiring-model work here even if you see an obvious opportunity — that's explicitly out of scope for this task and belongs in a separate coupled-allocation-hiring retry (already planned separately, with capital cost and recurring labor cost modeled as two distinct terms, not attempted here).

## Deliverables

1. `candidates/P7b.py`.
2. Append to `docs/planner-results.md` (new short section, "P7b — region assignment, isolated retest"): the bench reproduction numbers, the full acceptance-ladder table, and a plain verdict: promote to replace P6 as the working baseline, keep as documented-neutral-not-promoted, or (if it turns out negative in full games despite the neutral bench) reject with the causal explanation for why the bench didn't predict it — following the same rigor standard as `docs/M3-v3_12-regression-diagnosis.md` if the result is a surprise.
3. If it's a clear win (`t >= 2` vs P6 head-to-head with no regression elsewhere), rename it to become the new `candidates/P.py` (P7, next generation number after the rejected P7) and note the promotion in the doc; otherwise leave `candidates/P.py` as P6.

## Rules
This is a small, bounded task: one debugging round if the bench reproduction doesn't match, then proceed regardless (report the discrepancy rather than chasing it further). Do not touch `RULES.md`, `evolve/chassis.py`, `evolve/space.py`, `candidates/H32.py`, `candidates/M2.py`, or any tape/guard machinery. Do not start on the hiring/admission model — that's a separate, already-scoped follow-up.
