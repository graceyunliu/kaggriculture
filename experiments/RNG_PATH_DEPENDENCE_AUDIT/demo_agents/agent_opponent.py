"""Demo agent for eval_protocol.py validation ONLY -- not a strategy candidate.
Fixed common opponent used for both arms of the paired comparison (the
"same seed, same opponent" leg of the common-random-numbers design): a
simple carrot loop, adapted from the engine's own starter_agent reference
implementation (vendor/kaggle_environments_engine_master/kaggriculture.py)."""

CARROT_SEED_COST = 20


def agent(obs, config):
    farms = obs.get("farms", [])
    player = obs.get("player", 0)
    private = obs.get("private", {}) or {}
    if not farms or player >= len(farms):
        return {"farmer": ["PASS"], "hands": [], "market": []}
    farm = farms[player]
    fx, fy = farm["farmer"]
    tile = farm["tiles"][fy][fx]
    day = obs.get("day", 0)
    seeds = private.get("seeds", {})
    shed = private.get("shed", {})

    market = []
    if shed.get("CARROT", 0) > 0:
        market.append(["SELL", "CARROT", shed["CARROT"]])
    if seeds.get("CARROT", 0) == 0 and farm["money"] >= CARROT_SEED_COST:
        market.append(["BUY_SEED", "CARROT", 1])

    farmer = ["PASS"]
    if tile is None and seeds.get("CARROT", 0) > 0:
        farmer = ["PLANT", "CARROT"]
    elif isinstance(tile, dict) and tile.get("kind") == "PLANT" and tile.get("crop") == "CARROT":
        age = day - tile.get("planted_day", day)
        if age >= 3:
            farmer = ["HARVEST"]
        elif not tile.get("watered_today"):
            farmer = ["WATER"]
    return {"farmer": farmer, "hands": [], "market": market}
