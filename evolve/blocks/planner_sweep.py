def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):
    """Crop work is represented directly in the shared planner routes."""
    plan = S.get("plan") or {}
    route = plan.get("routes", {}).get(i)
    return route.get("stops") if route else None


def _crop_step(i, pos, v, day, hour, carry, pools, seeds_left):
    # Kept as a block-compatible entry point.  Dispatch calls _route_step so crop
    # and animal actions share one route and one pickup budget.
    return None
