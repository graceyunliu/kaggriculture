from collections import deque

# =====================================================================
# 1. SPATIAL & PATHFINDING MANAGER
# =====================================================================
class SpatialManager:
    def __init__(self, grid_size=(20, 20)):
        self.grid_size = grid_size
        self.pasture_tiles = set()
        self.crop_tiles = set()
        self.shed_location = (0, 0)

    def allocate_pasture_zone(self, grid_state, num_animals=4):
        """Pre-clears contiguous pasture tiles near shed BEFORE livestock purchase."""
        needed_tiles = num_animals
        allocated = set()
        queue = deque([self.shed_location])
        visited = {self.shed_location}

        while queue and len(allocated) < needed_tiles:
            curr = queue.popleft()
            if curr not in self.crop_tiles and grid_state.get(curr, "empty") == "empty":
                allocated.add(curr)

            r, c = curr
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.grid_size[0] and 0 <= nc < self.grid_size[1]:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        self.pasture_tiles.update(allocated)
        return self.pasture_tiles

    def bfs_path(self, start, target, grid_obstacles=None):
        """BFS pathfinding to bundle actions without idle steps."""
        if start == target:
            return []
        obstacles = grid_obstacles or set()
        queue = deque([(start, [])])
        visited = {start}

        while queue:
            (curr_r, curr_c), path = queue.popleft()
            for move, (dr, dc) in [("NORTH", (-1,0)), ("SOUTH", (1,0)), ("WEST", (0,-1)), ("EAST", (0,1))]:
                nxt = (curr_r + dr, curr_c + dc)
                if nxt == target:
                    return path + [move]
                if (0 <= nxt[0] < self.grid_size[0] and 0 <= nxt[1] < self.grid_size[1] 
                        and nxt not in obstacles and nxt not in visited):
                    visited.add(nxt)
                    queue.append((nxt, path + [move]))
        return []

# =====================================================================
# 2. JIT LIVESTOCK & FERTILIZER ENGINE (D40 / D41)
# =====================================================================
class JITLivestockEngine:
    def __init__(self, target_herd_size=4, min_crop_liquidity=2100):
        self.target_herd_size = target_herd_size
        self.min_crop_liquidity = min_crop_liquidity

    def generate_jit_market_orders(self, current_turn, current_bank, inventory, market_prices, active_animals):
        """D41 JIT feed purchases + D40 immediate fertilizer liquidation."""
        market_orders = []

        # Maintain crop liquidity buffer before buying stock
        if current_bank < self.min_crop_liquidity and len(active_animals) == 0:
            return market_orders

        # D41: Buy feed (wheat) directly off market churn
        needed_feed = len(active_animals) * 2
        current_wheat = inventory.get("wheat", 0)
        feed_shortfall = needed_feed - current_wheat

        if feed_shortfall > 0 and "wheat" in market_prices:
            buy_qty = min(feed_shortfall, 10)
            market_orders.append({"action": "BUY", "item": "wheat", "quantity": buy_qty})

        # D40: Auto-sell manure/fertilizer daily
        fertilizer_qty = inventory.get("fertilizer", 0)
        if fertilizer_qty > 0:
            sell_qty = min(fertilizer_qty, 10 - len(market_orders))
            market_orders.append({"action": "SELL", "item": "fertilizer", "quantity": sell_qty})

        return market_orders

# =====================================================================
# 3. TASK ALLOCATOR WITH URGENT WATERING
# =====================================================================
class V4TaskAllocator:
    def __init__(self, spatial_mgr):
        self.spatial = spatial_mgr

    def prioritize_tasks(self, farm_state):
        urgent_water, normal_water, animal_care, harvest = [], [], [], []

        for tile, plant in farm_state.get("crops", {}).items():
            if plant.get("consecutive_unwatered", 0) >= 1:
                urgent_water.append(tile)  # Priority 0
            elif plant.get("ready_for_harvest", False):
                harvest.append(tile)
            else:
                normal_water.append(tile)

        for animal_id, animal in farm_state.get("animals", {}).items():
            if animal.get("needs_care", False) or animal.get("needs_feed", False):
                animal_care.append(animal["location"])

        return {
            "p0_urgent_water": urgent_water,
            "p1_animal_care": animal_care,
            "p2_harvest": harvest,
            "p3_normal_water": normal_water
        }

# =====================================================================
# 4. KAGGLE AGENT ENTRY POINT
# =====================================================================
# Global instances persist across turn invocations
spatial_mgr = SpatialManager()
jit_engine = JITLivestockEngine()
task_allocator = V4TaskAllocator(spatial_mgr)

def agent(obs, configuration):
    """
    Main entry point invoked by the Kaggle environment every step.
    Returns: dict with farmer, hands, and market action lists.
    """
    turn = obs.get("step", 0)
    bank = obs.get("player_cash", 3000)
    inventory = obs.get("inventory", {})
    market_prices = obs.get("market_prices", {})
    farm_state = obs.get("farm_state", {})
    active_animals = farm_state.get("animals", {})

    # 1. Market orders (JIT feed + Fertilizer liquidation)
    market_orders = jit_engine.generate_jit_market_orders(turn, bank, inventory, market_prices, active_animals)

    # 2. Priority task queueing
    tasks = task_allocator.prioritize_tasks(farm_state)

    # 3. Worker operations assembly
    farmer_action = "PASS"
    hand_actions = ["PASS"] * len(obs.get("hands", []))

    # Assemble and return legal step dict
    return {
        "farmer": farmer_action,
        "hands": hand_actions,
        "market": market_orders
    }