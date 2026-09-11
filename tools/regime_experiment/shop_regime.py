"""Reconstruct the deterministic town shop-unlock timeline per seed, and stratify
existing per-seed candidate margins by the resulting demand regime.

Pure function of seed (matches _end_of_day's rng = Random((seed*1_000_003) ^ day)).
"""
import random, json, glob, os
from collections import defaultdict

SHOPS = {
    "BAKERY":         ["EGG", "WHEAT"],
    "PIZZA_SHOP":     ["MILK", "TOMATO", "WHEAT"],
    "BRUNCH_SPOT":    ["EGG", "WHEAT", "STRAWBERRY"],
    "YARN_STORE":     ["WOOL"],
    "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"],
    "PET_CAFE":       ["CARROT"],
    "SMOOTHIE_SHOP":  ["STRAWBERRY", "MILK"],
    "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"],
}
MAX_SHOP_INSTANCES = 8
UNLOCK_INTERVAL = 3
PRODUCTS = ["EGG","WHEAT","STRAWBERRY","MILK","TOMATO","WOOL","CARROT"]

def unlock_sequence(seed, max_day=29):
    """List of (day, shop_name) unlock events, matching engine's _end_of_day."""
    unlocked = []
    events = []
    for day in range(0, max_day):
        rng = random.Random((seed * 1_000_003) ^ day)
        next_day = day + 1
        if next_day > 0 and next_day % UNLOCK_INTERVAL == 0:
            if len(unlocked) < MAX_SHOP_INSTANCES:
                shop = rng.choice(sorted(SHOPS))
                unlocked.append(shop)
                events.append((next_day, shop))
    return events

def demand_vector(events, as_of_day):
    """Cumulative per-product 'incremental buyer weight' from shops unlocked by as_of_day."""
    v = {p: 0.0 for p in PRODUCTS}
    for day, shop in events:
        if day > as_of_day:
            continue
        products = SHOPS[shop]
        mult = 2 if len(products) == 1 else 1
        for p in products:
            v[p] += mult
    return v

def timing_features(events):
    """Day each product first gets extra demand, and total instance count."""
    first_day = {p: None for p in PRODUCTS}
    for day, shop in events:
        for p in SHOPS[shop]:
            if first_day[p] is None:
                first_day[p] = day
    return first_day

if __name__ == "__main__":
    for seed in range(1, 16):
        ev = unlock_sequence(seed)
        d6 = demand_vector(ev, 6)
        d12 = demand_vector(ev, 12)
        d24 = demand_vector(ev, 24)
        print(seed, "events:", ev)
        print("  d6:", {k:v for k,v in d6.items() if v}, "d12:", {k:v for k,v in d12.items() if v}, "d24:", {k:v for k,v in d24.items() if v})
