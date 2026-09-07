"""Demo agent for eval_protocol.py validation ONLY -- not a strategy candidate.
Sweeps the farmer across tiles, buying/planting WHEAT (cheapest crop) wherever
it lands, so it occupies visibly more tiles than agent_passive.py by end of
day -- the "dense" arm of the RNG-coupling divergence check. Movement pattern
is a simple boustrophedon (snake) sweep; no attempt at being a good policy."""

_MOVES = ["EAST", "EAST", "EAST", "EAST", "SOUTH", "WEST", "WEST", "WEST", "WEST", "SOUTH"]


def agent(obs, config):
    farms = obs.get("farms", [])
    player = obs.get("player", 0)
    private = obs.get("private", {}) or {}
    step = obs.get("step", 0)
    if not farms or player >= len(farms):
        return {"farmer": ["PASS"], "hands": [], "market": []}
    farm = farms[player]
    fx, fy = farm["farmer"]
    tile = farm["tiles"][fy][fx]
    seeds = private.get("seeds", {})

    market = []
    if seeds.get("WHEAT", 0) == 0 and farm["money"] >= 10:
        market.append(["BUY_SEED", "WHEAT", 1])

    if tile is None and seeds.get("WHEAT", 0) > 0:
        farmer = ["PLANT", "WHEAT"]
    else:
        farmer = [_MOVES[step % len(_MOVES)]]

    return {"farmer": farmer, "hands": [], "market": market}
