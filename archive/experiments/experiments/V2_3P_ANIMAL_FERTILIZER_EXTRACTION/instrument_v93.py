"""V2_3P: non-controlling instrumentation for main_v9.3_fertilize.py.

Loads the real agent module fresh (importlib, own namespace, never edits
the .py file on disk) and monkeypatches a handful of its module-level
functions with logging wrappers that call straight through to the
original implementation and return its exact result unmodified. This
produces ORACLE call records (deep-copied inputs/outputs) for the shadow
modules to be compared against. No control flow, ordering, or return
value is altered -- verified downstream by the terminal-money /
determinism check in run_extraction.py.
"""
import copy
import importlib.util


def load_instrumented_agent(path, log):
    """Returns (agent_callable, module). `log` is a dict of lists that
    call records get appended to, keyed by function name."""
    spec = importlib.util.spec_from_file_location(
        path.replace("/", "_").replace(".", "_") + "_instrumented", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    turn_counter = {"t": -1}
    orig_agent_fn = m._agent

    def wrapped_agent(obs):
        turn_counter["t"] += 1
        log.setdefault("turns", []).append({
            "t": turn_counter["t"], "day": obs.get("day"), "hour": obs.get("hour"),
        })
        return orig_agent_fn(obs)
    m._agent = wrapped_agent

    def make_wrapper(name, extra_capture=None):
        orig = getattr(m, name)

        def wrapper(*args, **kwargs):
            t = turn_counter["t"]
            args_copy = copy.deepcopy(args)
            kwargs_copy = copy.deepcopy(kwargs)
            result = orig(*args, **kwargs)
            record = {"t": t, "args": args_copy, "kwargs": kwargs_copy,
                       "result": copy.deepcopy(result)}
            if extra_capture is not None:
                record["extra"] = extra_capture(m)
            log.setdefault(name, []).append(record)
            return result
        return wrapper

    def reserved_sites_extra(mod):
        # reserved_sites is module-level mutable state that only grows via
        # _grow_reserved_sites() during _agent's confirmation pass (which
        # always runs BEFORE economy()/these gate calls within a turn), so
        # its value at call time is stable for the remainder of the turn.
        # Captured per-call because the list is mutated in place across the
        # whole game -- reading it post-hoc would return the FINAL,
        # end-of-game value for every historical call.
        return {"reserved_sites": list(mod.reserved_sites)}

    for fn_name in ("animal_setup_action", "animal_maintenance_action",
                     "animal_reconcile"):
        setattr(m, fn_name, make_wrapper(fn_name))
    for fn_name in ("_animal_expansion_feasible", "_sheep_expansion_feasible"):
        setattr(m, fn_name, make_wrapper(fn_name, extra_capture=reserved_sites_extra))

    def econ_extra(mod):
        return {
            "n_reserved_sites": len(mod.reserved_sites),
            "reserved_sites": list(mod.reserved_sites),
            "animal_plans": copy.deepcopy(mod.animal_plans),
        }
    setattr(m, "economy", make_wrapper("economy", extra_capture=econ_extra))

    # Also wrap _agent's *return value* to get the actual per-turn action,
    # for the fertilizer-diversion (Track B) and overall determinism check.
    inner_wrapped = m._agent

    def wrapped_agent2(obs):
        result = inner_wrapped(obs)
        log.setdefault("agent_actions", []).append({
            "t": turn_counter["t"], "action": copy.deepcopy(result),
        })
        return result
    m._agent = wrapped_agent2

    def agent(obs, configuration=None):
        try:
            return m._agent(obs)
        except Exception:
            return {"farmer": ["PASS"], "hands": [], "market": []}

    return agent, m
