"""Demo agent for eval_protocol.py validation ONLY -- not a strategy candidate.
Never plants anything: leaves every tile empty, maximizing weed-spawn draws
consumed per day (the "sparse" arm of the RNG-coupling divergence check)."""


def agent(obs, config):
    return {"farmer": ["PASS"], "hands": [], "market": []}
