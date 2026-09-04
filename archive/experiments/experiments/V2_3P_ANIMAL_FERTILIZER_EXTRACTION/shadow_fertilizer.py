"""V2_3P shadow reimplementation of V9.3's fertilizer-diversion dispatch
(the inline block in _agent(), v9.3 iter F).

Independent transcription -- does not call _agent or any real decision
function. Reproduces the exact fert_pool consumption order: farmer first
(if it needs a crop task and already carries fertilizer), then hands in
roster order (carry-first, else shed-restock-if-at-center).

Distinguishes the four fertilizer states named in TRACK B:
  1. generated  -- tile is in view["fert_targets"] this turn
  2. admitted   -- unit is eligible to consider fertilizer this turn
                   (fell through to ordinary crop duty AND (carries
                   fertilizer OR is at a center tile with shed stock))
  3. selected   -- this reimplementation's chosen op for that unit
  4. executed   -- compared by the caller against the real returned op
"""


def _nearest(pos2, pool, dist_fn):
    if not pool:
        return None
    return min(pool, key=lambda t: dist_fn(pos2, t))


def fert_dispatch(farmer_pos, farmer_needs_crop, farmer_carry,
                   hand_needs_crop, inventories, shed,
                   fert_targets, center_tiles,
                   *, dist_fn, step_toward_fn):
    """Returns (farmer_op_or_None, farmer_needs_crop_after,
    {i: op_or_None}, still_need_list) mirroring the real inline block.
    `hand_needs_crop` is a list of (index, pos) in roster order, matching
    what the real code passes in."""
    fert_pool = list(fert_targets)
    if not fert_pool:
        return None, farmer_needs_crop, {}, list(hand_needs_crop)

    def _fert_op(pos2):
        if pos2 in fert_pool:
            fert_pool.remove(pos2)
            return ["FERTILIZE"]
        tgt = _nearest(pos2, fert_pool, dist_fn)
        if tgt:
            st = step_toward_fn(pos2, tgt)
            if st:
                fert_pool.remove(tgt)
                return [st]
        return None

    farmer_op = None
    if farmer_needs_crop and farmer_carry.get("FERTILIZER", 0) > 0:
        op = _fert_op(farmer_pos)
        if op is not None:
            farmer_op = op
            farmer_needs_crop = False

    fert_shed_avail = shed.get("FERTILIZER", 0)
    hand_ops = {}
    still_need = []
    for (i, pos2) in hand_needs_crop:
        carry_i = inventories[i + 1] if len(inventories) > i + 1 else {}
        op = None
        if carry_i.get("FERTILIZER", 0) > 0 and fert_pool:
            op = _fert_op(pos2)
        elif fert_shed_avail >= 2 and fert_pool and pos2 in center_tiles:
            op = ["PICKUP", "FERTILIZER", 2]
            fert_shed_avail -= 2
        if op is not None:
            hand_ops[i] = op
        else:
            still_need.append((i, pos2))

    return farmer_op, farmer_needs_crop, hand_ops, still_need
