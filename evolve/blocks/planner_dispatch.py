def _unit_action(i, pos, carry, obs, v, pools, seeds_left, shed, unlocked_shed):
    day, hour = obs["day"], obs["hour"]

    def chore(kind, tp, value, hard=False, needs=None, deadline=23):
        return {"id": "%s:%d,%d" % (kind, tp[0], tp[1]), "kind": kind, "pos": tp,
                "deadline": deadline, "value": float(value), "needs": needs, "hard": hard}

    def enumerate_all():
        out = []
        prices = obs.get("market", {}).get("prices", {})
        for tp, tile in v["crops"]:
            crop = tile.get("crop")
            spec = CROPS.get(crop, {})
            age = day - tile.get("planted_day", day)
            urgent = tile.get("consecutive_unwatered", 0) >= 1
            in_window = (not spec.get("ongoing") and (spec.get("max_day", 0) + 1) // 2 <= age <= spec.get("max_day", -1)
                         and tile.get("yield_units", 0) < spec.get("max_yield", 0))
            fert_water = spec.get("ongoing") and tile.get("fertilized_until_day", -1) >= day
            if not tile.get("watered_today") and (urgent or in_window or fert_water):
                hard = urgent or (crop == "MELON" and in_window)
                val = 1000 if urgent else prices.get(crop, CROP_SPECS.get(crop, {}).get("base", 40))
                if crop == "MELON" and 6 <= age <= 10:
                    val *= 1.5
                out.append(chore("water", tp, val, hard))
            if _harvest_ready(tile, day):
                out.append(chore("harvest_crop", tp, tile.get("yield_units", 0) * prices.get(crop, 40)))
            if _fert_eligible(tile, day):
                out.append(chore("fertilize", tp, prices.get(crop, 100), False, "FERTILIZER"))
        for tp, tile in v["animals"]:
            animal = tile.get("animal")
            product = PRODUCT_OF.get(animal, "EGG")
            daily = prices.get(product, 100) / max(1.0, 2.0 if animal == "COW" else 3.0 if animal == "SHEEP" else 1.0)
            # The addendum permits alternate-day feed, but never skip a second day.
            if day < 29 and not tile.get("fed_today"):
                # P2 reliability rule: feed every animal before scheduling growth.
                # Alternate-day feeding can return only after zero escapes is proven.
                out.append(chore("feed", tp, daily + prices.get("FERTILIZER", 20), True, "WHEAT"))
            if day < 28 and not tile.get("cared_today"):
                out.append(chore("care", tp, daily))
            if tile.get("fertilizer_available"):
                out.append(chore("collect", tp, prices.get("FERTILIZER", 20)))
            if tile.get("yield_units", 0) > 0:
                out.append(chore("harvest_animal", tp, tile.get("yield_units", 0) * prices.get(product, 100)))
        for tp in v["weeds"]:
            out.append(chore("dig", tp, 10))
        # Late planting has no time to repay its watering burden and was the
        # source of every observed P2 weed (all appeared from day 21 onward).
        for tp in (pools.get("plant", []) if day <= 18 else []):
            crop = _plant_choice(tp, seeds_left)
            if crop:
                spec = CROP_SPECS[crop]
                out.append(chore("plant", tp, spec["base"] * spec["units"] / max(1, spec["cycle"]), False,
                                 "SEED:" + crop, 21))
        return out

    def route_eta(start, stops, needs_pickup):
        cur = start
        total = hour
        if needs_pickup and cur not in unlocked_shed:
            sh = min(unlocked_shed, key=lambda q: (_dist(cur, q), q)) if unlocked_shed else cur
            total += _dist(cur, sh) + 1
            cur = sh
        elif needs_pickup:
            total += 1
        for c in stops:
            total += _dist(cur, c["pos"]) + 1
            if total > c["deadline"]:
                return 99
            cur = c["pos"]
        return total

    def make_plan():
        positions = v["positions"]
        routes = {j: {"unit": j, "stops": [], "pickup": {}, "eta_end": hour} for j in range(len(positions))}
        all_chores = enumerate_all()
        previous = S.get("plan") or {}
        # Chore ids are intentionally position-based, but completion is only a
        # same-day fact.  Carrying this set across days suppresses all recurring
        # feed/water work at those positions.
        done = set(previous.get("chore_done", set())) if previous.get("day") == day else set()
        all_chores = [c for c in all_chores if c["id"] not in done]
        ordered = sorted(all_chores, key=lambda c: (not c["hard"], c["deadline"], -c["value"], c["pos"], c["kind"]))
        unassigned = []
        inventories = obs["private"].get("inventories") or []
        wheat_left = shed.get("WHEAT", 0)
        fert_left = shed.get("FERTILIZER", 0)
        for c in ordered:
            if not c["hard"] and any(x["hard"] for x in unassigned):
                unassigned.append(c)
                continue
            best = None
            # Keep every action at one tile on the same worker.  In particular,
            # animal feed/care/collect/harvest becomes one visit, not four trips.
            owners = [j for j in range(len(positions))
                      if any(x["pos"] == c["pos"] for x in routes[j]["stops"])]
            candidates = owners if owners else list(range(len(positions)))
            for j in candidates:
                inv = inventories[j] if j < len(inventories) else {}
                already = sum(1 for x in routes[j]["stops"] if x["needs"] == c["needs"])
                extra = max(0, already + 1 - inv.get(c["needs"], 0)) - max(0, already - inv.get(c["needs"], 0))
                if c["needs"] == "WHEAT" and extra > wheat_left:
                    continue
                if c["needs"] == "FERTILIZER" and extra > fert_left:
                    continue
                old = routes[j]["stops"]
                for at in range(len(old) + 1):
                    trial = old[:at] + [c] + old[at:]
                    need_pickup = any(x["needs"] in ("WHEAT", "FERTILIZER") for x in trial)
                    eta = route_eta(positions[j], trial, need_pickup)
                    if eta <= c["deadline"] and eta <= 23:
                        key = (eta - routes[j]["eta_end"], eta, j, at)
                        if best is None or key < best[0]: best = (key, j, at, eta)
            if best is None:
                unassigned.append(c); continue
            _key, j, at, eta = best
            routes[j]["stops"].insert(at, c)
            routes[j]["eta_end"] = eta
            if c["needs"] == "WHEAT":
                inv = inventories[j] if j < len(inventories) else {}
                total = sum(1 for x in routes[j]["stops"] if x["needs"] == "WHEAT")
                old_pickup = routes[j]["pickup"].get("WHEAT", 0)
                new_pickup = max(0, total - inv.get("WHEAT", 0))
                routes[j]["pickup"]["WHEAT"] = new_pickup; wheat_left -= new_pickup - old_pickup
            elif c["needs"] == "FERTILIZER":
                inv = inventories[j] if j < len(inventories) else {}
                total = sum(1 for x in routes[j]["stops"] if x["needs"] == "FERTILIZER")
                old_pickup = routes[j]["pickup"].get("FERTILIZER", 0)
                new_pickup = max(0, total - inv.get("FERTILIZER", 0))
                routes[j]["pickup"]["FERTILIZER"] = new_pickup; fert_left -= new_pickup - old_pickup
        return {"day": day, "hour": hour, "routes": routes, "unassigned": unassigned,
                "chore_done": done, "seeds_left": dict(seeds_left),
                "replans": (previous.get("replans", 0) + 1) if previous.get("day") == day else 1,
                "replan_hours": set(previous.get("replan_hours", set())) if previous.get("day") == day else set()}

    if any(carry.get(a, 0) > 0 for a in ANIMALS):
        op = _setup_step(i, pos, v, carry)
        if op is not None: return op
    prod_carried = sum(carry.get(k, 0) for k in PRODUCTS if k != "WHEAT")
    if day >= 28 and prod_carried >= (3 if day == 29 else 6):
        if pos in unlocked_shed: return ["DROP"]
        if day == 29 or hour >= 18: return [_step(pos, min(unlocked_shed, key=lambda q: (_dist(pos, q), q)))]

    plan = S.get("plan")
    if not plan or plan.get("day") != day or (hour == 1 and plan.get("hour") != 1):
        S["plan"] = make_plan()
    op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
    if op is not None: return op
    plan = S.get("plan") or {}
    pending = set(c["id"] for r in plan.get("routes", {}).values() for c in r.get("stops", []))
    missing_hard = [c for c in enumerate_all() if c["hard"] and c["id"] not in pending
                    and c["id"] not in plan.get("chore_done", set())]
    if missing_hard and plan.get("replans", 0) < 4 and hour not in plan.get("replan_hours", set()):
        old_done = set(plan.get("chore_done", set()))
        old_hours = set(plan.get("replan_hours", set())); old_hours.add(hour)
        S["plan"] = make_plan()
        S["plan"]["chore_done"].update(old_done)
        S["plan"]["replan_hours"] = old_hours
        op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
        if op is not None: return op
    # Install purchased animals before accepting optional overflow work.
    shed_animals = sorted((a, n) for a, n in shed.items() if a in ANIMALS and n > 0)
    if shed_animals and hour >= 1 and day < 27:
        if pos in unlocked_shed:
            return ["PICKUP", shed_animals[0][0], 1]
        return [_step(pos, min(unlocked_shed, key=lambda q: (_dist(pos, q), q)))]
    if prod_carried >= 4 and carry.get("WHEAT", 0) == 0 and _shed_dist(pos) <= 2:
        if pos in unlocked_shed: return ["DROP"]
        return [_step(pos, min(unlocked_shed, key=lambda q: (_dist(pos, q), q)))]
    return ["PASS"]
