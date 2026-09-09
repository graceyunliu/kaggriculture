# O2 → O4 mechanism audit: what the bundle actually is (Sep 9)

O4 was confirmed (separately, cross-tested on this repo's own harness) to decisively beat C1, V3_15, and the real clone opponent — see RULES.md's "What worked" entry. This doc is the follow-up investigation: not "is O4 better," but "why, and which parts of it are reusable." It walks through the full decomposition, in the order it was actually established, so a future reader can see the evidence chain rather than just the conclusion.

## Method, once, up front

Every claim below was tested the same way: a minimal, behavior-preserving patch built against a single fixed baseline (mostly O2), a paired same-seed margin test via `evolve/cascade.py`'s `_eval` (DEV_SEEDS 1–10, HELD_SEEDS 11–30, both seats), and — because a favorable margin can hide a silent no-op or a broken verification proxy — a direct behavioral check that the patch's code path actually fires before the margin is trusted. Two proxies turned out to be wrong during this investigation (see "What almost went wrong" below); both were caught by requiring the behavioral check, not by the margin looking suspicious.

## The three pillars

**Pillar 1 — Worker coordination.** Prevent two of our own units from independently committing to the same scarce thing in one turn.
- *Site-claim* (`S["claimed_sites"]`/`S["pending_sites"]` in O2 itself, governing where an animal or crop gets placed): removing it costs **−$2,956/game dev (t=−2.30), −$3,310/game held-out (t=−2.11)**. Behaviorally confirmed: baseline O2 shows zero same-turn duplicate site targets across 9 `_pick_site` calls (seed 1 vs C1); the stripped version shows 1 duplicate out of 12.
- *Shared-stock accounting* (O2→O3, extends the same PICKUP-tracking guard from animals only to all shed items): **+$999/game dev (t=3.14, 9-1)**.

**Pillar 2 — Operational waste elimination.** Mechanism B, lifecycle-aware care/feed: skip a feed/care visit when the animal's production calendar and stored bonus say it isn't due yet, instead of visiting every animal every day regardless of need.
- **+$2,457/game, both dev (t=2.38) and held-out (t=2.19)** vs O2.
- Behaviorally confirmed via `evolve/trace.py`'s `skipped_feed_not_due` metric jumping 1→13.
- Reads as **waste avoidance, not reallocation**: a single-seed trace shows unit-turns drop 6,688→5,938 and chores drop ~19%, with production preserved (escapes 1→0, networth flat-to-up) — but `idle_share` barely moves (0.109→0.121), so the freed-up worker time isn't visibly being redirected into more harvesting/watering. The mechanism removes wasted work; it doesn't obviously convert the savings into extra output. (Single-seed, illustrative — the aggregate margin above stands regardless of which channel explains it.)

**Pillar 3 — Temporal economic conversion.** Mechanisms C (intraday capital timing: sell every hour instead of only hour 0/day 28+) and D (mid-route product release: drop carried product at a nearby shed mid-route instead of waiting to finish the route).
- Neither is worth much alone: C alone +$124 to +$183/game (not significant), D alone −$1,291 to −$2,043/game (not significant, a mild wash-to-loss).
- Together: **CD vs D alone = +$2,864 to +$3,304/game (t=2.97–3.23)**; CD vs C alone = +$1,048 to +$2,160/game (t=0.80–1.87). This is a genuine interaction, not two features that both happen to be good.
- The causal handoff is directly demonstrated at the action level (`evolve/cd_causal_chain.py`): in D-alone, `sell_after_drop` is `None` on every single day — released product just sits until the next scheduled sell. In CD combined, a SELL reliably follows the DROP one hour later, every day a drop occurs. **What is NOT demonstrated**: that the earlier sale → earlier cash → earlier reinvestment → higher final wealth. The cash-bump instrumentation built to test this fired at hour 1 in every variant including plain O2, i.e. it was picking up routine daily cash flow, not anything attributable to the mechanism. This half of the causal story remains a plausible, unverified extension — noted explicitly rather than assumed.

## The interaction structure (the actual scientific payoff)

Five pairwise/triple relationships were tested. Four are additive; one is a real interaction:

| Contrast | Result | Verdict |
|---|---|---|
| B × CD | dev −$1,772 (t=−0.87), held −$200 (t=−0.11) | additive (≈0) |
| Coordination × CD | dev −$1,716 (t=−1.16), held −$981 (t=−0.50) | additive (≈0) |
| Coordination × B | **pooled n=30: +$3,760/game, t=2.01** | **real interaction** |

Coordination's own effect is +$3,192/game inside plain O2 (t=2.85, n=30) but +$6,952/game inside the B context (t=6.94, n=30) — B roughly doubles what the coordination fix is worth. Plausible reading: B frees up more worker-turns for animal-placement attempts per unit time (fewer of them spent on unneeded feed/care), which increases how often two units would otherwise converge on the same site in a turn — so the fix has more to prevent. Not independently confirmed; stated as the working hypothesis, not fact.

The first two reads of Coordination×B (dev alone, held alone) were each suggestive (t=1.89, t=1.55) but below this project's own t≥2 bar. Rather than average those two summary statistics into a fabricated pooled number, the resolving step was a single direct `cascade._eval` call over the full 30-seed pooled set with true per-seed pairing — that's what produced the t=2.01 result above. This is the difference between a defensible pooled test and a reconstructed one; only the former was reported as a finding.

**Net architecture: mostly modular, one confirmed exception.** Treat Coordination and B as a linked pair in future proposals (the same rule already in place for C and D) — don't credit or blame either in isolation.

## Portability panel: does this generalize, or is it C1-specific?

Ran O2/B/CD/BCD/O4 each against the same fixed opponent (C1, V3_15, the real clone, and a real ladder-loss tape opponent), same seeds, and took the paired delta of each candidate's own money against O2's own money vs that opponent — a different question from "does the candidate beat that opponent," which was already established separately.

| Environment | B−O2 | CD−O2 | BCD−O2 | O4−O2 |
|---|---:|---:|---:|---:|
| Clone | +15,142 (t=3.21) | +9,450 (t=2.40) | +7,879 (t=1.63) | +12,420 (t=3.04) |
| TapePeter | +10,901 (t=2.35) | +6,399 (t=1.47) | +10,172 (t=2.50) | +4,465 (t=1.09) |
| C1 | +2,214 (t=0.94) | −4,565 (t=−1.08) | +2,513 (t=0.47) | −5,012 (t=−1.40) |
| V3_15 | +5,596 (t=1.06) | +5,572 (t=1.19) | +3,606 (t=0.64) | +3,531 (t=0.65) |

Against Clone and TapePeter — genuinely different economic architectures from C1 — every variant is positive, decisively for B and O4 vs Clone. Against C1 specifically, CD and O4's edge mildly reverses (not statistically decisive at n=20, but consistently signed). This doesn't contradict O4's decisive head-to-head win over C1 (+$13,164/game held-out, t=14.41) — it means the *specific O2→O4 upgrade* isn't what's buying that particular win; C1's play style may just not create the mid-day product flow the timing pair exploits. **Takeaway: B and Coordination look like portable architecture; the CD (timing) edge should be checked against a new opponent's play style before assuming it transfers.**

A dev-seed-only read of this same panel had shown an apparent sharp O4-vs-TapePeter reversal (−$10,546); the held-out re-run flatly contradicted it (+$4,465) — another instance of the standing small-sample-noise lesson.

## What almost went wrong (worth keeping as a lesson, not just a footnote)

Two separate verification proxies looked like they'd found a silent no-op, and both turned out to be broken instruments rather than dead mechanisms:
1. **Capital-timing (C) verification**: an early instrumentation pass counted only off-hour BUY/HIRE actions and found zero difference from O2 on 9 of 10 seeds. The mechanism's actual dominant effect — SELL firing every hour instead of only hour 0 — wasn't in the tally. Once added, O2_capital showed 9–13 off-schedule sells/game on every seed versus 0 for baseline.
2. **Cash→reinvestment chain**: the "cash bump" proxy (cash ≥ day's opening + $500) fired at hour 1 in nearly every day for every variant, including plain O2 — it was measuring routine daily cash flow, not anything mechanism-specific. This was recognized and the claim was left unverified rather than forced.

The general lesson: a "no difference found" verification result should be treated as ambiguous between "the mechanism is inert" and "the probe is blind to the mechanism's actual effect" until the specific order/action types the patch touches are confirmed to be covered by the instrument.

## What this means for O5 search

- Coordination and B are a linked pair — propose changes to one with the other in mind; don't isolate-test them in the future without checking whether the coupling still holds under the new change.
- C and D are already an established linked pair from the earlier decomposition (RULES.md); this reinforces the general pattern that "make information available" and "make it usable" mechanisms tend to interact rather than add.
- The reusable search framework this audit supports: for any candidate resource (worker time, animal production, inventory, cash, information), ask where it queues, where it's wasted, and whether the subsystem that would consume it is actually listening — that's the shape of all three pillars found so far.
- The C×D and Coordination×B edges both came from testing a *specific, named* interaction, not from broad search — the productive move going forward is likely "pick a plausible pairing and factorial-test it directly," not "generate many independent single-mechanism proposals and hope."
