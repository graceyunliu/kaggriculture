"""Standalone per-day net-worth extraction for mini_engine games."""
from __future__ import annotations
import copy
import sys
import time
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import mini_engine as me

def _tiles(farm):
    for y, row in enumerate(farm["tiles"]):
        for x, tile in enumerate(row):
            if isinstance(tile, dict):
                yield (x, y), tile

def _inventory_value(inventory, prices):
    return sum(qty * prices.get(item, 0) for item, qty in (inventory or {}).items())

def _networth(observation, private, player, animal_cost):
    farm = observation.farms[player]
    prices = observation.get("market", {}).get("prices", {})
    shed = private.get("shed", {}) or {}
    carried = private.get("inventories", []) or []
    animal_value = sum(animal_cost.get(tile["animal"], 0) for _, tile in _tiles(farm) if "animal" in tile)
    return (farm["money"] + _inventory_value(shed, prices)
            + sum(_inventory_value(hand, prices) for hand in carried) + animal_value)

def networth_game(agent_a_path, agent_b_path, seed, engine="master", config=None):
    """Run one game with A in seat 0 and return net worth for days 0 through 29."""
    module, defaults = me.load_engine(engine)
    cfg = dict(defaults)
    if config:
        cfg.update(config)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(agent_a_path), me.load_agent(agent_b_path)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
         "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}}
        for i in range(2)
    ])
    state = module.interpreter(state, env)
    for player_state in state:
        player_state.observation.step = 0
    steps = int(cfg["episodeSteps"])
    animal_cost = {name: spec["cost"] for name, spec in module.ANIMALS.items()}
    trajectories = [[], []]
    current_day = None
    step = 0
    started = time.monotonic()
    while True:
        observation0 = state[0].observation
        day = observation0.day
        if day != current_day and 0 <= day < 30:
            current_day = day
            for player in range(2):
                trajectories[player].append(round(_networth(observation0, state[player].observation.private, player, animal_cost)))
        for player in range(2):
            observation = copy.deepcopy(state[player].observation)
            observation["step"] = step
            try:
                action = agents[player](observation, copy.deepcopy(env.configuration))
            except Exception:
                action = {}
            state[player].action = action if isinstance(action, dict) else {}
        state = module.interpreter(state, env)
        step += 1
        for player_state in state:
            player_state.observation.step = step
        if all(player_state.status == "DONE" for player_state in state) or step >= steps:
            break
    if any(len(trajectory) != 30 for trajectory in trajectories):
        raise RuntimeError(f"expected 30 day snapshots, got {[len(t) for t in trajectories]} (seed={seed}, engine={engine}, elapsed={time.monotonic() - started:.1f}s)")
    return trajectories
