# Codex brief — diagnose and (if legitimate) fix M3's regression vs V3_12

Copy everything below the line into Codex.

---

You are diagnosing why a general, opponent-blind sizing rule loses money against one specific opponent, and fixing it only if the fix is a general improvement — not a rule that special-cases that opponent.

## Location — read this first
There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

`cd` there; all relative paths below are relative to it. Do **not** open or modify anything under `/Users/graceliu/Documents/ChatGPT/Kaggriculture`, `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture`, `Archived versions/`, `Chatgpt Agents/`, `Perplexity Agents/`, `User Notebooks/`, or `/Users/graceliu/Downloads`. Other sessions are concurrently working in `evolve/blocks/`, `candidates/P.py`, `candidates/gen_p/`, `evolve/queue/`, `tools/`, `Opponents/schedules/`, and `candidates/K.py` — do not touch those paths.

Work on branch `codex/m3-v3_12-regression`, based off `codex/general-opening-sizing` (commit `5596410`). Commit as you go.

## Background — read these in full first
- `candidates/M3_GENERAL_SIZING.py` — the candidate under investigation.
- `docs/M3-general-sizing-results.md` — the result this task follows up on. Read the "Never touched during development" table: M3 is +$36,390/game vs V3_12 (t=11.89, 20-0 — still a decisive win), but **−$9,137/game worse than H32's fixed sell-25 rule** against V3_12 specifically, while being roughly flat (±$800) against E1/C1/H10. M3 still wins every game against every opponent; the question is only why the general rule leaves money on the table against this one, and whether that's fixable with more general reasoning or is a real, acceptable tradeoff of not fingerprinting opponents.
- `candidates/H32.py` — the baseline M3 is compared against (fixed sell-25 opening).
- `candidates/V3_12.py` — the opponent in question.

## What NOT to do
Do not add any check, threshold, or branch that reads V3_12's identity, its specific purchase amounts, or anything that would only fire against V3_12 or tapes resembling it. If the diagnosis turns out to require "detect this specific opponent's opening and react differently," the correct conclusion is to report that and leave M3 as documented — not to build the special case. The bar from the original brief still applies: any change must be justified by market/state reasoning that would apply to *any* opponent exhibiting the same live state, not by knowing who's on the other side.

## Task

1. **Instrument, don't guess.** Using the pattern in `tools/sell_shift.py::shed_trace` (monkeypatch `mini_engine.load_agent`), record M3's and H32's full per-step trajectories (cash, wheat inventory/price, hires, feed events, unfed-animal events) for several seeds of M3 vs V3_12, both seats. Diff them against the corresponding H32 vs V3_12 trajectories for the same seeds.
2. **Localize the mechanism.** Identify concretely what M3's different turn-1 sell quantity (computed by its price-impact/feed-reserve formula, typically 23-24 vs H32's fixed 25) causes downstream against V3_12 specifically — e.g., does V3_12's own opening interact with the market in a way that makes M3's slightly-smaller sell leave it short of cash for a specific purchase a few turns later? Does V3_12 buy/sell wheat itself in a way that changes the price curve M3's formula assumed? Report the causal chain with concrete numbers (turn, cash delta, missed/delayed action), not just the aggregate margin.
3. **Classify the cause** as one of:
   - (a) A bug or overly conservative constant in M3's formula (e.g. reserving more feed buffer than actually needed, or misestimating price impact) that is wrong in general, not just against V3_12 — fixable and the fix should also be checked against the other three never-touched opponents (E1, C1, H10) to confirm it isn't a V3_12-specific tune in disguise.
   - (b) A genuine tradeoff: M3's rule is financing-optimal in the state it sees, and V3_12 simply happens to punish slightly-smaller turn-1 sells more than the other opponents do, with no general formula change that helps here without hurting elsewhere. If so, document it and stop — this is an acceptable, honest cost of not fingerprinting opponents, and should not be "fixed" by fingerprinting them.
4. If (a): implement the fix in `candidates/M3_GENERAL_SIZING.py` (or a new `M3b_*.py` if you want to preserve the original for comparison), freeze it, then re-run `mini_engine.evaluate()` on seeds 11–30 both seats against all four never-touched opponents (V3_12, E1, C1, H10) plus the five original fitting-set tapes (yuan800, atakan, strawhats, kiro, antigone), reporting both groups exactly as in `M3-general-sizing-results.md`, clearly labeled. The fix must not regress E1/C1/H10 by more than noise (~$1k) to be worth keeping.
5. Verify with `replay_verify.py` that determinism is unchanged (same guard/tape machinery).

## Deliverables

1. `docs/M3-v3_12-regression-diagnosis.md`: the trajectory diff findings, the causal explanation with concrete numbers, and the classification (a) or (b) with justification.
2. If (a) and a fix is implemented: the updated candidate file, and an updated results table (all 9 opponents, both groups labeled, before/after the fix) appended to the same doc or a new `M3b-results.md`.
3. If (b): stop after the diagnosis doc. Do not force a fix that doesn't exist.

## Rules
Two debugging/iteration rounds on any regression found while implementing a fix, then write up and stop either way. Same fit/test discipline as before: freeze any new constant from documented mechanics or from the never-touched-opponent set's aggregate behavior, not from tuning against V3_12 until the number looks right.
