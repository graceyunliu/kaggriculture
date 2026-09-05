# Codex brief — replace M2's opponent-fingerprint sell table with a general price-impact rule

Copy everything below the line into Codex.

---

You are replacing a specific, narrowly-fit piece of logic in a Kaggle farming-simulation agent with a general one, and proving the replacement is actually general (not just re-fit to the same opponents).

## Location — read this first
There are several folders named "Kaggriculture" on this machine. **The only one you work in is:**

```
/Users/graceliu/Claude/Projects/Kaggriculture
```

`cd` there; all relative paths below are relative to it. Do **not** open or modify anything under `/Users/graceliu/Documents/ChatGPT/Kaggriculture`, `/Users/graceliu/Claude/Projects/Kaggriculture/ChatGPT--Kaggriculture`, `Archived versions/`, `Chatgpt Agents/`, `Perplexity Agents/`, `User Notebooks/`, or `/Users/graceliu/Downloads`. Other sessions are concurrently working in `evolve/blocks/`, `candidates/P.py`, `candidates/gen_p/`, `evolve/queue/`, `tools/`, and `Opponents/schedules/` — do not touch those paths. Do not modify `candidates/K.py` (a chassis rebuild attempt already tried porting a similar idea there — `docs/opening-grid-kchassis-sep04.md` — and it did not transfer; this task is deliberately scoped to a standalone candidate file instead, not the K chassis).

Work on branch `codex/general-opening-sizing`. Commit as you go with descriptive messages.

## Background — read `candidates/M2.py` and `docs/M2-adaptive-opening-sep04.md` in full first

`M2.py` (built on `H32.py`) plays a fixed recorded opening tape (`_TAPE`) for the first `SWITCH_DAY` days, with a runtime divergence guard (`_diverged()`) that falls back to the general heuristic agent (`_agent()`) if live state stops matching the recorded tape. At turn 1 only, it currently does this:

```python
M2_SELL = {"big": 18, "mid": 24, "other": 25}

def _m2_class(obs):
    inv = obs["market"]["inventory"]["WHEAT"]
    mine = int(_TAPE[0]["market"][0][2])
    n = 10000 - int(inv) - mine - 1
    if n >= 48: return "big"
    if n >= 38: return "mid"
    return "other"
```

The three thresholds (48, 38) and three sell sizes (18, 24, 25) were found by grid search against five known opponent tapes (yuan800, atakan, strawhats, kiro, antigone) — picking whichever quantity happened to break each tape's fixed turn-0 feed-buy amount (53, 43). This is a lookup table fit to break specific known scripts, not a general market-reasoning rule, and it does nothing (`"other"` = H32 default) against any opponent outside that fitted cluster. That is the problem to fix.

## What "general" means here — the acceptance bar

Replace `_m2_class` / `M2_SELL` with a function of **live market state only** (current wheat inventory, price, your own cash/holdings, day/hour) that reasons about price impact and expected value — e.g., estimate the marginal revenue of selling m units into the current depleted-inventory market versus holding, using the same demand-curve logic already in `economy()` / `_demand_room()` elsewhere in H32.py. It must not:
- read or infer the opponent's identity, submission ID, or team name (there is none in `obs` — keep it that way)
- contain any constant that was chosen because it breaks a specific known tape's specific known purchase amount (no `if n >= 48` where 48 exists only because a known opponent buys 53)
- be validated only against the five tapes it might incidentally still be tested on

Concretely: derive the sell quantity from a formula (e.g. maximize expected `revenue(m) = price_after_selling(m) * m` against the visible inventory curve, subject to your own cash/feed needs), not from a table of opponent-specific magic numbers.

## Validation — this is the part that matters most

1. **Fit/test split.** Do NOT tune any constant in the new rule by running it against `Opponents/tape_yuan800*.py`, `tape_atakan*.py`, `tape_strawhats*.py`, `tape_kiro*.py`, or `tape_antigone*.py` and observing the result, then adjusting. If the rule needs calibration constants (e.g. an elasticity estimate), derive them from the *shape of the market/demand model itself* (documented game mechanics, `mini_engine.py`), not from replaying known opponents until the number looks good.
2. **Held-out evaluation only, after the rule is frozen:** run `mini_engine.evaluate()` (see its docstring) with the finished, un-tuned-against-tapes candidate against: the five tapes above (report the numbers honestly, including if they're now smaller than M2's), plus `V3_12`, `E1`, `C1`, and `H10` (opponents *not* used to build the rule), seeds 11–30, both seats, master engine.
3. Report margin/t/W-L for every opponent in both categories, plainly labeled "opponents used to build M2 (do not use these to tune)" vs "never touched during development." Do not cherry-pick.
4. If the general rule's margin against the five known tapes is much smaller than M2's (this is expected and fine — M2's number came from exploiting them specifically), say so plainly. The point of this task is a policy that's honest about what it captures, not one that matches M2's headline number.
5. Confirm with `replay_verify.py` that the candidate reproduces deterministically (same guard/tape machinery as H32/M2, unchanged).

## Deliverables

1. `candidates/M3_GENERAL_SIZING.py` (or similar name) — H32 chassis, new sizing function replacing `_m2_class`/`M2_SELL`, guard and tape machinery otherwise untouched.
2. `docs/M3-general-sizing-results.md` — the mechanism (one paragraph, in plain terms: what market signal it uses and why the formula is expected to generalize), the fit/test-split methodology actually followed, and the held-out results table from step 2–3 above, both opponent categories clearly separated.
3. If no formula beats H32's default (25) by a meaningful, honest margin on the never-touched opponents, say so and stop — do not force a positive result by quietly evaluating against the fitting set instead.

## Rules
Two debugging/iteration rounds on any regression, then write up and stop. Do not touch `RULES.md`, `evolve/chassis.py`, `evolve/space.py`, or any path listed as claimed above.
