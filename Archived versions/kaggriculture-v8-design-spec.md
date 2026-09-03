# V8 Design Specification
## Expected-Value Decision Agent for Kaggriculture

**Status:** Revised draft  
**Basis:** v7.2 ladder-loss analysis, engine visibility rules, and the engineering review of the original v8 proposal.

**Objective:** Replace arbitrary strategic ceilings and disconnected deterministic rules with a centralized, state-dependent expected-value decision engine, while preserving the proven v7.2 execution layer.

---

## 1. Executive Summary

V8 should not begin as a four-layer meta-agent or a Bayesian opponent-strategy classifier.

Kaggriculture exposes most of the opponent's current farm state directly every turn, including:

- Money
- Farm tiles
- Crop composition
- Pastures and visible animals
- Land unlocks
- Workers
- Shared market inventory and prices

Because the current opponent state is directly observable, V8 does not need probabilities to answer questions such as:

- How many cows does the opponent have?
- How many mature melons are visible?
- How much land has the opponent unlocked?
- Which products are already flooding the market?

The central problem is not hidden opponent intent. The central problem is that v7.2 imposes hard strategic limits on itself and makes several disconnected decisions that conflict with one another.

V8 therefore centers on one component:

> **An Expected-Value Decision Engine that compares feasible economic actions using the current game state.**

Opponent state remains important, but only as one input to decisions whose payoffs are genuinely coupled through the shared market.

---

## 2. Evidence from v7.2 Replays

The six ladder losses revealed several repeated limitations in v7.2.

### 2.1 Hard fleet ceiling

v7.2 uses a fixed target:

```python
FLEET_TARGET = {"COW": 4, "SHEEP": 0}
```

Once four cows are active, the bot cannot buy another animal regardless of:

- Current milk price
- Remaining days
- Available money
- Farmer workload
- Opponent product mix
- Available pasture space
- Expected marginal animal profit

This is an artificial strategic ceiling, not a physical engine constraint.

### 2.2 Wheat seed and planting mismatch

The economy module purchases wheat seeds, but the planting priority ranks wheat last:

```text
MELON
STRAWBERRY
CARROT
WHEAT
```

As a result, wheat seeds may be purchased and then planted zero to two times.

The purchase decision and planting decision are made by separate rules with no shared value model.

### 2.3 Delayed land expansion

v7.2 usually completes land expansion around the first major melon payout.

This timing is largely produced by fixed money and day thresholds rather than an explicit comparison of:

- Land value
- Cow value
- Seed value
- Hiring value
- Cash reserve value

Earlier land is not automatically better, but the current timing is often accidental rather than chosen.

### 2.4 Static melon selling

v7.2 tends to sell similar melon quantities at similar scheduled times even when the realized melon price differs dramatically.

Loss replays showed major dumps at prices ranging from strong to nearly worthless.

The physical production plan was similar across matches, but final score varied sharply because the sell policy did not respond enough to:

- Current price
- Recent price movement
- Market inventory
- Opponent mature melon supply
- Shed pressure
- Cash needs

### 2.5 Fixed crop allocation

Crop choice is governed by a universal priority order rather than current marginal value.

This can prevent:

- Wheat planting when wheat is unusually valuable
- Reduced melon planting when melon prices are collapsing
- Additional strawberries when recurring-crop value is strong
- Crop selection that reflects animal feed demand

### 2.6 Deterministic opening

v7.2 behaves nearly identically through Day 10 across very different opponents.

This is not automatically bad; a strong opening can be deterministic. However, it confirms that the current policy does not use observable state to adjust investment timing or production mix during the opening.

---

## 3. Design Principle

Adaptive logic does not automatically remove hard-coded limitations.

An adaptive rule can still operate inside a narrow box.

Example:

```python
if milk_price > 180 and cows < 4:
    buy_cow()
```

This reacts to price, but it still:

- Cannot buy a fifth cow
- Does not compare cows with land
- Ignores farmer maintenance capacity
- Ignores remaining days
- Ignores sheep
- Ignores expected future milk supply

V8 must distinguish between:

### Real constraints

Keep these hard-coded:

- Available money
- Market-order limit
- Valid action schemas
- Tile availability
- Shed capacity
- Remaining turns
- Animal survival requirements
- Worker and farmer action capacity

### Arbitrary strategic ceilings

Replace these with state-dependent decisions:

- Exactly four cows
- Fixed crop priority
- Fixed dump day
- Fixed land-buy thresholds
- Buying seeds without expected planting capacity
- Universal investment ordering

The goal is not to remove all rules.

The goal is:

> **Keep physical and safety constraints; replace arbitrary strategic limits with comparable expected-value estimates.**

---

## 4. Revised Architecture

```text
                  Observation Layer
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
      My State      Opponent State   Market State
          │              │              │
          └──────────────┴──────────────┘
                         │
                         ▼
          Expected-Value Decision Engine
                         │
                         ▼
              Existing v7.2 Execution Layer
        (scheduler, movement, farming, maintenance)
```

Optional future components:

```text
Opponent Supply Forecast
```

for predicting future market pressure, and:

```text
Multi-Turn Policy Coordinator
```

for managing plans that require sustained commitment.

These are deferred until evidence shows they are necessary.

---

## 5. Component Responsibilities

### 5.1 Observation Layer

Build one normalized state object every turn.

```python
state = {
    "day": ...,
    "hour": ...,
    "days_remaining": ...,
    "my": {...},
    "opponent": {...},
    "market": {...},
    "capacity": {...},
}
```

#### My-state features

- Money
- Unlocked land
- Empty tiles
- Crop counts by type and maturity
- Seed inventory
- Shed inventory
- Active animals by species
- Animal needs
- Farmer inventory
- Worker count
- Estimated work backlog
- Farmer animal workload
- Reserved pasture capacity

#### Opponent-state features

Read directly from visible observations:

- Money
- Unlocked land
- Crop counts by type
- Mature and nearly mature crops
- Pasture count
- Visible animal count by species
- Worker count
- Recent visible expansion
- Current production footprint

No strategy label is required for the initial version.

#### Market-state features

- Current prices
- Current inventories
- Recent price velocity
- Recent inventory velocity
- Town demand schedule
- Shed capacity pressure
- Expected local supply from visible crops

---

### 5.2 Opponent State Analyzer

The original strategy-recognition component is simplified into a factual analyzer.

Its job is to answer:

- How many visible melons are mature soon?
- How many animals are producing milk or wool?
- Is the opponent rapidly expanding land?
- Which products are likely to enter the market?
- How concentrated is the opponent's production?

Example output:

```python
opponent_summary = {
    "mature_melons": 28,
    "melons_ready_within_2_days": 17,
    "active_cows": 9,
    "active_sheep": 3,
    "wheat_tiles": 22,
    "land_quadrants": 4,
}
```

This is direct state extraction, not Bayesian classification.

---

### 5.3 Expected-Value Decision Engine

The decision engine answers:

> Given the current state, which feasible economic actions have the highest expected value?

Candidate actions include:

- Buy land
- Buy cow
- Buy sheep
- Hire one or more hands
- Buy each seed type
- Plant each crop type
- Sell each product and quantity
- Hold inventory
- Reserve cash
- Stop expansion

Each candidate must be scored on the same basis.

Generic structure:

```text
Expected Future Revenue
− Direct Cost
− Feed Cost
− Labor Cost
− Farmer Logistics Cost
− Tile Opportunity Cost
− Market Impact Risk
− Time-Remaining Penalty
− Failure Risk
= Expected Utility
```

The engine selects the best feasible set subject to real constraints.

---

## 6. Decision Models

### 6.1 Animal expansion

Replace:

```python
if active_cows < 4:
    buy_cow()
```

with:

```text
Expected remaining animal-product revenue
+ Expected fertilizer value
− Animal purchase cost
− Expected feed cost
− Pasture tile opportunity cost
− Setup travel cost
− Daily maintenance burden
− Risk of missed feeding
= Next-animal value
```

Compare that value against:

- New land
- Additional labor
- Crop seeds
- Holding cash
- Another species

The result may be:

- Stop at three animals
- Expand to six
- Add sheep instead of cows
- Delay animal purchase
- Buy no animals late in the season

### 6.2 Land purchase

Estimate:

```text
Expected production from additional tiles
− Land cost
− Seed cost
− Labor required
− Delay before land becomes productive
− Value of the investment displaced
= Land value
```

Land timing should be selected, not accidentally produced by budget thresholds.

### 6.3 Hiring

Estimate the marginal value of the next hand:

```text
Expected extra completed work
× value per completed task
− Fibonacci hire cost
= Next-hand value
```

Travel-adjusted workload should include:

- Watering
- Harvesting
- Planting
- Weeds
- Expected animal support if hands can assist

### 6.4 Seed purchasing and crop planting

Seed purchasing and planting must use the same crop-value model.

Do not buy seeds unless the bot expects to have:

- Plantable tiles
- Sufficient labor
- Enough remaining season
- Positive expected crop value

Crop score:

```text
Expected yield
× Expected future price
− Seed cost
− Watering and harvest labor
− Tile opportunity cost
− Market-crowding risk
+ Strategic value
= Crop value per tile
```

This removes the wheat-seed/planting conflict.

### 6.5 Selling

Selling is the first decision that should become explicitly adaptive.

For each product and candidate quantity:

```text
Immediate cash value
− Marginal price impact
− Expected value of waiting
+ Shed-overflow relief
+ Liquidity value
− Risk of opponent supply arriving first
= Sell-now value
```

Inputs include:

- Current price
- Current inventory
- Price and inventory velocity
- Opponent mature crops
- Days remaining
- Shed pressure
- Planned purchases
- Town demand timing

A fixed Day-11 melon dump should no longer be the primary trigger.

---

## 7. When Opponent State Should Matter

Use this counterfactual test:

> Would the best decision change if the opponent's state were different?

If yes, the decision is opponent-dependent.

If no, keep it locally optimized.

### Mostly opponent-independent

- Emergency watering
- Animal survival feeding
- Harvesting ready products
- Weed removal
- Movement
- Action validity
- Basic care when capacity is available

### Moderately opponent-dependent

- Crop allocation
- Animal expansion
- Land timing
- Hiring
- Fertilizer allocation

Opponent state affects expected product prices and opportunity costs, but it is not the only input.

### Strongly opponent-dependent

- Sell timing
- Sell quantity
- Holding inventory
- Entering a crowded product market
- Responding to visible mature opponent crops
- Product diversification

### Opponent-sensitivity test

For each decision function, evaluate it twice:

```python
actual_score = score_action(my_state, actual_opponent, market)
neutral_score = score_action(my_state, neutral_opponent, market)

opponent_sensitivity = actual_score - neutral_score
```

This test helps detect:

- Missing opponent effects
- Excessive opponent reactivity
- Decisions that should remain independent

---

## 8. Bayesian Reasoning: Narrow, Optional Use

Bayesian reasoning is not removed entirely.

It is simply moved out of the critical path for facts that are directly observable.

### Do not use Bayesian inference for:

- Current cow count
- Current crop mix
- Current money
- Current land
- Current visible maturity
- Current market inventory

These can be read directly.

### Bayesian or probabilistic reasoning may help with:

- Whether the opponent will sell mature crops immediately
- Whether the opponent will hold inventory
- Whether the opponent is likely to pivot products
- Expected timing and quantity of future supply
- Confidence in price forecasts

The initial v8 should not require a full opponent-strategy classifier.

A future forecast component may maintain probabilities only where genuine uncertainty exists.

---

## 9. Meta Agent / Multi-Turn Policy Coordinator

A meta-agent is not part of the initial v8 MVP.

A one-step decision engine may naturally produce:

- A melon-heavy economy when melons score highest
- An animal-heavy economy when animals score highest
- A wheat-heavy economy when wheat scores highest

No separate mode selector is required if individual decisions remain coherent.

### Limitation of one-step scoring

Some strategies require multi-turn commitment.

Examples:

- A melon rush needs land, labor, seeds, watering capacity, and later holding behavior.
- An animal expansion requires pasture space, feed infrastructure, and farmer logistics.
- Switching repeatedly between plans may produce neither strategy effectively.

### Add a policy coordinator only if testing shows:

- The decision engine oscillates between investments
- It abandons high-value plans before payoff
- It fails to reserve required capacity
- Short-term scores repeatedly undermine long-term returns

A future coordinator may choose a temporary posture such as:

```text
For the next four days:
- prioritize animal infrastructure,
- preserve feed reserve,
- limit new melon acreage.
```

This is different from a permanent strategy archetype.

---

## 10. Randomization

Do not make intentionally irrational moves.

Randomize only among near-equivalent actions.

Example:

```text
Cow value: 8.9
Land value: 8.8
```

Possible policy:

```text
Cow: 70%
Land: 30%
```

Controlled exploration is allowed when:

- Scores are close
- Model confidence is low
- No survival constraint is at risk
- The result can improve calibration

Randomization must not override:

- Animal survival
- Crop survival
- Valid-action constraints
- Endgame liquidation
- Hard budget limits

---

## 11. Decision Logging

Every significant strategic decision should be logged.

Example:

```text
Day: 12
Decision: Buy Cow

State:
- Money: 1500
- Active cows: 4
- Farmer animal workload: 11 actions/day
- Milk price: 182
- Opponent cows: 8
- Days remaining: 18

Prediction:
- Expected milk revenue: 2300
- Expected fertilizer value: 420
- Feed cost: 340
- Setup and maintenance cost: 510
- Tile opportunity cost: 260
- Expected utility: 1610

Alternatives:
- Buy land: 1450
- Hire hands: 620
- Buy strawberry seeds: 710

Outcome:
- Actual utility: 1380
- Prediction error: -230
```

This enables calibration of:

- Yield estimates
- Price forecasts
- Feed costs
- Labor costs
- Tile opportunity costs
- Farmer capacity
- Opponent market effects

---

## 12. Self-Improvement Loop

The self-improvement system should improve the decision model rather than frequently rewriting the execution engine.

Primary optimization targets:

- Expected-value formulas
- Forecast coefficients
- Opportunity-cost estimates
- Farmer-capacity estimates
- Crop yield estimates
- Sell-quantity models
- Exploration rate
- Multi-turn commitment thresholds

The v7.2 scheduler and execution mechanics remain stable unless replay evidence identifies a mechanical failure.

### Champion/challenger process

1. Generate a challenger decision model.
2. Test on paired seeds and symmetric seats.
3. Run safety and validity invariants.
4. Compare paired score margins and downside.
5. Review failure replays.
6. Promote only with fresh validation seeds.
7. Record observations, hypotheses, and confidence.

---

## 13. Implementation Phases

### Phase 0: Close proven v7.2 gaps

Before a broad architecture rewrite, test the replay-supported changes independently:

- Replace the fixed fleet ceiling with a configurable or marginal-value gate
- Fix wheat seed purchasing versus planting mismatch
- Test land timing variants
- Replace fixed melon dumping with price-aware selling

These tests provide baseline models for v8.

### Phase 1: Unified state and decision logging

Build:

- Normalized state object
- Opponent State Analyzer
- Decision-event logging
- Metrics for farmer workload, crop capacity, and market pressure

Keep current v7.2 choices initially.

### Phase 2: Adaptive selling

Replace the fixed melon dump with sell-value scoring.

This is the highest-priority adaptive component because loss replays show large score variation from realized melon prices.

### Phase 3: Unified crop and seed scoring

Use one crop-value model for:

- Buying seeds
- Assigning tiles
- Selecting planting priority

Eliminate purchased-but-unused seed behavior.

### Phase 4: Adaptive animal and land expansion

Compare:

- Next cow
- Next sheep
- Next land quadrant
- Additional hands
- Cash reserve

Remove the fixed four-cow ceiling once capacity constraints are modeled.

### Phase 5: Forecasting

Add probabilistic forecasts only where needed:

- Opponent sell timing
- Future market supply
- Future product price
- Pivot likelihood

### Phase 6: Multi-turn policy coordination

Add only if one-step scoring exhibits harmful oscillation or failure to commit.

---

## 14. Non-Goals for Initial V8

Initial v8 does not aim to:

- Solve the full game tree
- Predict every opponent action
- Use end-to-end reinforcement learning
- Require a Bayesian strategy classifier
- Implement a meta-agent from day one
- Replace the v7.2 scheduler
- Add arbitrary irrational actions
- Implement fake-outs
- Copy a top player's fixed strategy

---

## 15. Success Metrics

### Decision quality

- Higher paired final score than v7.2
- Reduced catastrophic low-price melon sales
- Seed purchases correspond to actual planting
- Animal count varies appropriately across states
- Land timing varies when expected value changes
- No increase in animal deaths or crashes

### Adaptation

- Decisions differ across materially different market states
- Strongly opponent-dependent decisions respond to visible opponent supply
- Opponent-independent safety actions remain stable
- No excessive oscillation between investments

### Model calibration

- Logged expected values correlate with realized outcomes
- Forecast error decreases over replay batches
- Confidence estimates are not systematically overconfident
- Challenger improvements survive fresh seeds and opponent pools

---

## 16. Final Design Summary

V8 is not primarily an opponent-strategy classifier.

It is an expected-value economic decision system.

The design changes from:

```text
Fixed thresholds
+ hard fleet target
+ universal crop priority
+ scheduled dump
```

to:

```text
Current state
+ feasible candidate actions
+ comparable value estimates
+ real constraints
= selected decisions
```

Opponent information remains important where it changes market payoff, especially for:

- Selling
- Product mix
- Animal expansion
- Crop allocation

Directly visible opponent facts should be read, not inferred.

Probabilistic reasoning should be added later only for uncertain future behavior.

A meta-agent should be added only if the simpler decision engine fails to maintain coherent multi-turn plans.

The key objective is:

> **Remove arbitrary strategic ceilings, unify disconnected decisions, and make every major economic choice compete on a shared state-dependent value model.**
