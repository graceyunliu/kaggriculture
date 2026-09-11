# Spend diff: what H_GATE144 actually does (Sep 11)

`tools/spend_diff.py`, base `O16_ORCH_ON_O15` -> `H_GATE144_O16_ORCH_ON_O15`, vs
`tape_peterparker_106816877`, seeds 21-30, `KAGG_FIXED_SHOPS=1`. Accounting is exact: the engine's
`_commit_unit`, `_do_hire` and `_do_buy_land` are wrapped, so every unit is recorded at its realized price
and no hire is billed that the engine silently skipped for want of cash.

## The one-line answer

The gain is **entirely a cost saving**, not a reallocation and not a price win. The identity closes with
nothing left over:

| | delta |
|---|---:|
| wages | **-1,836** |
| revenue | -504 |
| market purchases | +188 |
| **final money** | **+1,144** |

`-(-1836) - 504 - 188 = +1,144`. Every dollar of the improvement is wage that is no longer paid, less the
production the removed hands would have generated.

**The marginal hire returns about 27 cents on the dollar.** It costs $1,836 and produces $504 of revenue.
That is the number behind AGE-360's marginal counterfactual, now measured directly rather than inferred.

## Layer 2: the freed cash is not redeployed. It is banked.

This is the finding worth carrying forward, and it answers "what does the agent spend its marginal dollar
on?" with: nothing.

| class | delta units | delta cost |
|---|---:|---:|
| BUY_ANIMAL:COW | 0.0 | +0 |
| BUY_ANIMAL:SHEEP | 0.0 | +0 |
| BUY_LAND | 0.0 | +0 |
| BUY_SEED:MELON | 0.0 | +0 |
| BUY_SEED:STRAWBERRY | +0.1 | +10 |
| BUY_SEED:CARROT | +0.3 | +6 |
| BUY_SEED:WHEAT | **-1.1** | -11 |
| BUY_PRODUCT:WHEAT | +2.6 | +133 |
| BUY_PRODUCT:FERTILIZER | +1.2 | +50 |

Total purchase response to $1,836 of freed cash: **+$188**, about 10%, and most of that is feed the smaller
crew still consumes rather than an investment. Animals, land and melon do not move at all.

**The chassis has no capital allocator.** Its purchase decisions are driven by fixed targets and schedules,
not by available cash, so freeing capital does not cause it to buy anything. That has a direct consequence
for the planned marginal capital substitution matrix: **categories in this chassis do not substitute.**
Removing a dollar from class A does not move it to class B; it moves it to the bank. So a substitution
matrix run against this policy will mostly measure "no substitution", and the interesting version of that
experiment requires a policy that *can* reallocate.

It also means every marginal ROI number in AGE-360 is cleaner than feared. The counterfactual's "opportunity
cost" term is near zero here, because the policy does not in fact deploy freed cash elsewhere.

## Layer 3: the opponent's gain is a pure price effect, and it is confirmed

The tape sells **identical units of every product** -- CARROT, FERTILIZER, MELON, MILK, STRAWBERRY, WHEAT,
WOOL, all delta 0.0 -- and its wages and purchases are unchanged. Yet its revenue rises +287 and its final
money +285.

The mechanism is visible in the inventory column. We sell less (STRAWBERRY -8.2 units, WHEAT -3.9, MILK
-1.5), so the shared pool holds less (inv STRAWBERRY -4.1, WHEAT -6.5, MILK -1.5), so prices are higher for
everyone, so the tape's unchanged sales fetch more money.

**This is the exact mirror of the capital checkpoint.** That candidate bought MORE inputs, raising the input
prices the fixed-quantity tape paid, so the tape lost. This one sells FEWER outputs, raising the output
prices the tape receives, so the tape gains. Both are price externalities on a shared pool; one is an
attack, the other a gift. Neither is farming better.

Note what is NOT true: our own gain is not a price gain. Our revenue *fell* by 504 despite higher unit
prices, because we sold fewer units. We profit purely by not paying the wage.

## What this implies

1. **H_GATE144 is a real own-economy improvement** and the mechanism is now fully accounted for. It should
   transfer to an adapting field, because the part that helps us (not paying an overpriced wage) does not
   depend on the opponent at all.
2. **The opponent's share is unavoidable given the mechanism.** Producing less necessarily lifts the pool
   price. The only way to widen the margin is to cut the wage WITHOUT cutting output -- i.e. keep the
   production the removed hands were doing and get it from the hands that remain. The removed hire produced
   $504; if better dispatch recovered even half of that at no wage cost, the margin gain grows without
   giving the tape anything extra.
3. **The tighter caps give the tape progressively more.** At M=55 the tape gained +2,846 on the panel, which
   by this mechanism means a much larger output reduction. That, not our own capacity loss, is what
   collapses the margin -- our own money kept rising all the way to a cap of 10.
4. **Do not build the substitution matrix against this chassis** expecting substitution. Build it only after
   there is a policy with a capital allocator, or use it deliberately to demonstrate the absence.

## Caveat

One tape, 10 seeds. The layer-1 identity and the zero-redeployment result should be stable (they are
mechanical), but the size of the opponent's price gift will vary with how much the opponent sells into the
same products. Worth repeating across the four-tape panel before quoting the +285 as typical.
