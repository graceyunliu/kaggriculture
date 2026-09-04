# Kaggriculture self-improving agent — technical spec (v1)

Status: draft, not yet built. Scope: design for a champion/challenger loop that iterates on the Kaggriculture agent, plus a recommended first vertical slice.

## 1. Goal

Turn the current manual review cycle (write a version, get a human or LLM opinion, argue about whether it's right, maybe fact-check against engine source) into a harness-gated loop: a challenger is only kept if it demonstrably beats the current best under a fair, repeatable test, and every rejection produces a durable, reusable record of why.

This does not aim for full autonomy out of the gate. The MVP below is intentionally manual-triggered — automation is a later phase, added once the measurement pipeline itself is trusted.

## 2. Architecture overview

Champion/challenger loop, closed by two feedback paths:

```
Champion (current best, e.g. main_v7.py)
   |
   v
Challenger generation --------------------------+
  - param search (auto, no LLM)                  |
  - code edits (agent-assisted, reviewed)         |
   |                                              |
   v                                              |
Tournament runner  <---  Opponent pool            |
  (N games x each opponent)                       |
   |                                              |
   v                                              |
Binary eval suite (invariant checks)              |
   |                                              |
   v                                              |
Decision gate: beats champion + no invariant fails|
   |                        |                     |
  yes (promote)            no                     |
   |                        v                     |
   |                  Diagnostic (root cause)      |
   |                        v                      |
   |                  Learnings store  ------------+
   |                  (AGENT_LEARNINGS.md)
   v
becomes new Champion
```

Two categories of step, by risk: mechanical pipeline steps (champion, challenger, tournament runner, opponent pool, eval suite, decision gate) can eventually run unattended. Judgment steps (challenger generation, diagnosis, learnings authorship) are where mistakes are expensive and where this project has already been burned once (v6.1's hallucinated animal schema, ChatGPT/GLM reviews that got real facts wrong) — these stay human- or agent-reviewed longer.

## 3. Component spec

Proposed file layout, additive to what already exists in the repo:

```
Kaggriculture/
  main_v7.py                    existing — current agent logic
  champion.py                   NEW — copy/pointer to current best
  challengers/                  NEW — candidate variants under test
  opponents/                    NEW — opponent agents for the pool
  eval_manifest.json            NEW — binary invariant checks
  tournament.py                 NEW — runs N games x M opponents, aggregates
  diagnose.py                   NEW — (phase 2) reads a losing replay, classifies root cause
  AGENT_LEARNINGS.md            NEW — durable rule/changelog log
  harness.py                    existing — replay -> SQLite
  smoke_test.py                 existing — single-game crash check; becomes a subroutine of tournament.py
  Replays/                      existing
  vendor/kaggle_environments_engine/   existing — ground-truth engine source
```

**Opponent pool.** Built-in engine bots (random, starter, pass) plus the current champion (self-play). A stretch addition, not required for the MVP: the five real bots found embedded in the "Hamburger" public notebook (Soil V25, Kaito V21, Replay Shield V15, Scenario V14, Frontier V12) are extractable with the same three-line `gzip.decompress(base64.b64decode(...))` trick used to inspect that notebook, and would be far more representative than hand-built stand-ins. Held out of MVP scope deliberately — see tradeoffs below.

**Binary eval suite.** Each check is pass/fail per game, not a blended score, so a rejection is diagnosable by which check broke:
- crash-free / reaches DONE (already exists, via smoke_test.py)
- no starvation (animal escapes tile after 2 unfed days) — logic already proven in the 720-turn mock-engine sim, needs porting to run against real-engine games
- (phase 2) hand count resets to 0 at each day boundary
- (phase 2) internal budget tracker never goes negative
- (phase 2) no market-order category (sell/hire/seed) starved of every slot in a turn where it had eligible orders

**Promotion gate.** Adapted directly from the Hamburger notebook's gate, which is more rigorous than a plain "average score improved" check — it protects against a challenger that wins on average by taking on more downside risk:

- *Direct* (self-play vs champion, 2+ seeds, symmetric seats): net wins > 0, at least one seed-pair with positive combined margin, mean margin > 0, mean money > 0.
- *Broad* (vs the rest of the opponent pool): wins >= champion's wins, mean money > champion's mean money, minimum money >= 99% of champion's minimum money, mean leftover inventory <= 102% of champion's mean leftover.
- Promote only if both direct and broad pass, and the challenger itself passes every binary invariant across all its games. Otherwise, fall back to keeping the current champion — silently, not as an error state.

When more than one challenger is eligible in the same cycle, rank with a weighted score in the same style as Hamburger's `selection_score` (net_wins and positive-pairs dominate via large multipliers, margin and a small leftover penalty break ties) rather than a single blended metric.

**Learnings store.** Append-only. Suggested entry format:

```
## <date> — <challenger name>
Symptom:     <what the tournament/eval showed>
Root cause:  <diagnosed mechanism, referencing engine source where relevant>
Rule:        <one plain-language sentence>
Outcome:     promoted vX.Y | rejected, reason: <gate that failed>
```

## 4. What we're deliberately borrowing vs. building fresh

| Element | Source |
|---|---|
| Promotion thresholds (99%/102% floors, direct+broad split) | Adapted from Hamburger notebook, verified against its actual source |
| Two-stage gate (cheap self-play screen, then broader validation only for finalists) | Same source — avoids running the full opponent pool against every candidate |
| Diagnosis -> learnings -> next-generation feedback loop | Not present in Hamburger (it's a one-shot batch, re-authored by hand each notebook version) — this is the part we're building that they aren't |
| Domain-mechanic binary invariants (starvation, hand-reset, budget) | Not present in Hamburger (its only structural check is a code-equality assertion) — ours is gameplay-safety, not code-correctness |
| Opponent pool diversity | Hamburger has 5 real named opponents; ours starts with 3 built-in stand-ins in the MVP, real-bot extraction deferred |

## 5. Recommended MVP: fastest end-to-end vertical slice

The goal of the MVP is not a good result — it's proof that every stage of the loop is wired correctly and produces a trustworthy verdict, end to end, once. Everything "smart" (search, LLM-driven generation, automated diagnosis, scheduling) is stubbed by a human for this first pass; everything mechanical (tournament execution, invariant checks, promotion math, the learnings file) is built for real, because that's the part future automation has to trust.

**Included in MVP:**

1. `champion.py` — copy of `main_v7.py`, unchanged.
2. One hand-authored challenger — fix the 18-hand hiring cap regression (`max(6, min(18, work//4))` in v7, already diagnosed as too aggressive given the engine's daily hands-reset mechanic and 10-order-per-turn ceiling). Chosen because it's small, bounded, and already root-caused from earlier review — a clean first test case, not a new investigation.
3. `tournament.py` — runs champion and the one challenger through smoke_test.py's existing engine harness, N=10 games each against {random, starter, self-play champion}, aggregates into the same shape as Hamburger's stage summaries (wins, mean/min money, mean leftover, margin).
4. Binary eval suite — crash-free/DONE (exists) + no-starvation (ported from the mock-engine sim). The other three invariants deferred.
5. Promotion gate — full direct/broad logic and thresholds, implemented for real (this is cheap to build correctly now that we have a concrete formula to copy, no reason to water it down).
6. `AGENT_LEARNINGS.md` — created, with one entry written by hand for this test cycle regardless of outcome.
7. Manual trigger, single session, git commit only if the gate promotes.

**Excluded from MVP, with reasoning:**

| Excluded | Why it's cut for now | Risk of cutting it | When to add back |
|---|---|---|---|
| Automated challenger generation (param search / LLM code-edit proposals) | The loop's output is only as trustworthy as the measurement pipeline underneath it; generating many candidates against an unproven harness wastes runs and risks false promotions | Low — MVP proves the harness with one known-good manual candidate first | Once MVP's promotion verdict is manually double-checked and trusted |
| Full invariant manifest (hand-reset, budget-negative, market-slot-starvation checks) | Crash + starvation are the two highest-severity, already-solved checks; the other three need new detection code | A promoted challenger could regress one of the undetected invariants | Phase 2, before letting any loop run unattended |
| Real extracted opponent bots (Soil/Kaito/etc.) | Zero-cost stand-ins (random/starter/self-play) are enough to prove wiring; extraction is a clean, separable decision with its own etiquette question (fine for local testing per this competition's own public norms, but worth deciding deliberately rather than bundling into plumbing work) | Lower opponent fidelity means MVP's verdict is less representative of the real ladder | Immediately after MVP — this is the cheapest high-value upgrade, since the extraction code already exists from this conversation |
| Statistically robust game count (N=20-30+) | MVP goal is proving pipeline wiring, not producing a shippable verdict; small N is faster to iterate on while debugging | A wrong promote/reject in the MVP run is possible from noise | Before trusting any real promotion decision, raise N |
| Automated diagnostic layer (agent reads a losing replay and classifies root cause) | Highest-uncertainty piece — even expert-sounding reviews (ChatGPT, GLM) got real facts wrong earlier in this project without ground-truth verification; automating this before validating the entry format risks polluting the learnings store with confidently wrong diagnoses | None for MVP — a human writes one entry to validate the format | Once the format is validated and there's a backlog of real losses to classify |
| Scheduling / unattended runs | Nothing should run and commit without supervision until the promotion gate and eval suite are proven correct | N/A — this is a hard prerequisite, not a nice-to-have | After several manually-supervised cycles confirm the gate's verdicts match manual judgment |
| Parameter-search / config-extraction infrastructure | Only worth building once we know the tournament+eval+promotion pipeline is worth iterating against repeatedly | None — MVP's one challenger is a direct hand-edit, not config-driven | Once MVP validates, before scaling to many candidates per cycle |

**MVP success criteria (definition of done):**

1. `tournament.py` runs unattended once triggered and produces a structured summary for both champion and challenger.
2. The no-starvation check can be shown to actually fire — validate by temporarily breaking something on purpose and confirming the eval suite catches it, not just trusting it silently passes.
3. The promotion gate computes direct_ok/broad_ok from the aggregated stats and prints a clear promote/reject verdict with the specific failing condition if rejected.
4. `AGENT_LEARNINGS.md` has one real entry in the defined format, independent of outcome.
5. If promoted: `champion.py` is updated and the change is committed to git referencing the learnings entry and a version tag (e.g. v7.1).

## 6. Known blind spots, carried forward regardless of phase

- `DemandTimingEngine` uses a hardcoded seed (42), so "randomized" demand jitter is actually identical every game. Self-play-only testing will overfit to this exact pattern — this is the main reason the opponent pool needs real diversity (built-in bots at minimum, real extracted bots ideally), not just self-play.
- Local tournament results are a proxy for real ladder performance, not the real thing — they don't capture the wider competitive metagame, only how the challenger does against whatever's in the pool at test time.
- Sep 23 deadline: the MVP is scoped to be buildable in a single focused session specifically because of this — every deferred item above is deferred with an explicit "add back" trigger, not left open-ended.

## 7. Phase 2+ roadmap (brief)

1. Extract real opponent bots from public notebooks into `opponents/`.
2. Complete the binary invariant manifest (hand-reset, budget, market-slot checks).
3. Raise tournament game count to a statistically defensible N.
4. Build the agent-assisted diagnostic step, validated against the MVP's one hand-written entry as ground truth.
5. Add the parameter-search track once there's a config-driven set of tunable constants worth searching over.
6. Only then: consider scheduling the parameter-search track unattended, per the earlier automation-level discussion. Code-edit challengers stay agent-assisted and human-reviewed regardless of phase.
7. Build the opponent archetype + anti-fingerprint module (Section 8) once (1) has produced a real opponent pool worth classifying against.

## 8. Opponent archetype + anti-fingerprint module

Status: designed, not built. This is a third pillar alongside the champion/challenger loop (Sections 1-7) and the from-scratch-policy stance (no replay-tape cloning, per the notebook review) — it's about reading and reacting to *opponent* behavior mid-match, which the loop above doesn't address at all.

### 8.1 What's grounded vs. speculative

This module rests on three facts already confirmed against the real engine source and real replay data, not assumption:

- **Opponent state is fully observable.** `interpreter()` broadcasts `obs.farms` (board tiles, money, farmer/hand positions, unlocked quadrants) to every player every step — confirmed by reading `kaggriculture.py` directly. Only `private` (shed contents, seeds) is hidden. Any archetype signal built from public board state needs no new instrumentation.
- **Land is not contested; the market is the real interaction channel.** Each player unlocks their own quadrants independently (no race for the same tile). Prices move off *combined* sell volume into a shared market inventory, so the payoff from opponent-modeling is anticipating what they'll sell and when — not blocking their land or animals directly.
- **The current real-ladder top of the field is non-adaptive.** Savko and Subin An were confirmed to run the same fixed script (near-identical order counts and timing across 8 replays; the ~5% score gap between them is RNG variance, not skill). A classifier that reacts to a bot that isn't reacting to us is safe to build and test against known ground truth — but see 8.4 for the one confirmed exception.

### 8.2 Archetype classifier

Deliberately a lookup/heuristic layer, not a statistical model — with ~10 labeled replays total in hand, a decision tree here is closer to "recognize a known shape" than genuine inference, and shouldn't be dressed up as more than that.

**Fingerprint features** (all read from public `obs.farms`, available turn-by-turn):
- day of first `BUY_LAND`, and which quadrant
- animal purchase count and species mix by day 5
- hand-hire ramp rate (hands/day trajectory over days 0-10)
- crop mix (which of WHEAT/STRAWBERRY/MELON/CARROT/TOMATO appear in planted tiles)
- per-product sell volume trend, once visible

**Known archetypes to seed the corpus with** (from replay analysis already on file):
- "standard-meta": land NE day 7 / SW day 10, never SE; 8 cow + 6 sheep by day 10; hands plateau at 12/day; wheat/strawberry/melon only. Matches Savko and Subin An in all 8 replays reviewed.
- "v5-style loss profile": aggressive early spend, crop-only, no animal pipeline — the profile our own v5 lost to on the ladder (design doc line 258 background).
- Additional archetypes to be added once the Hamburger-embedded bots (Soil/Kaito/Replay Shield/Scenario/Frontier) are extracted per Section 7 item 1 — the 3-archetype seed corpus above is too thin to generalize from alone.

**Counter-play catalog, keyed by matched archetype** (not a fixed rule per opponent, since it has to survive the promotion gate like anything else):
- vs. "standard-meta": shift crop mix toward CARROT/TOMATO/GOOSE/EGG, already identified as untouched by both observed top players — avoids adding to their oversupplied products and captures price the shared market isn't discounting.
- vs. any archetype with high observed volume in one product: bias sell timing earlier in the day/turn than their historical pattern, to avoid selling into a price the opponent's dump is about to crater.

### 8.3 Anti-fingerprint layer

Separate concern from 8.2 — applies regardless of what the opponent is doing, as a hedge against *us* being the one who gets fingerprinted.

- Motivation: this isn't hypothetical. One of the three public notebooks Grace reviewed ("adaptive-farming-strategy-for-kaggriculture") implements real clone detection and a front-run-a-clone's-sale layer. If a similar bot ever scrapes one of our own ladder replays the way we scraped Savko's, a fully deterministic policy is a liability.
- Mechanism: a small perturbation budget (~5%) sampled from a *safe deviation set* — sell-timing jitter, hire-ramp jitter, land-buy day offset, crop-mix substitution — not arbitrary randomness. "Safe" means it must not be able to trip any invariant in the Section 3 eval suite (e.g., jitter can delay a sell but never skip feeding).
- Cost model: this is a defensive move, not a performance play. It should be near-zero-cost in expectation and is tested the same way as any other challenger — it has to clear the existing direct/broad promotion gate (Section 3) without regressing mean money, not get a special exemption because the motivation is "safety" rather than "profit."

### 8.4 Deception — explicitly deferred, not built

Reasoned out but deliberately not designed further right now: deception (deliberately signaling a false early strategy) only pays against an opponent that actually watches and reacts to us mid-match. The two real-ladder-top bots analyzed in depth (Savko, Subin An) are confirmed fixed scripts — faking out a bot that isn't reacting has zero expected value. The one confirmed counterexample is the clone-detecting notebook bot referenced in 8.3, which *is* reactive. Revisit this only if that bot (or something like it) shows up in the real extracted opponent pool (Section 7 item 1) and actually exploits our patterns in testing. If revisited, the cheap version is staggering our own early-game signature so it doesn't cleanly match a known archetype — not building an active false-signal system.

### 8.5 Fit with the rest of the pipeline

- Both 8.2 and 8.3 ship as ordinary challengers — they are agent behavior changes, not changes to the eval/gate machinery, and must clear the same promotion gate as any other challenger (Section 3).
- The classifier corpus (8.2) is only as good as the opponent pool it's trained against; it's gated on Section 7 item 1 (real extracted bots), not worth building against the 3 built-in stand-ins alone.
- Not in MVP scope (Section 5). This is a phase-2/3 addition, sequenced after the loop itself is proven trustworthy.
