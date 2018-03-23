def _get_diffs(x1, y1, x2, y2):
    return (x2 - x1, y2 - y1)


def is_valid_bishop_move(x1, y1, x2, y2):
    dx, dy = _get_diffs(x1, y1, x2, y2)
    return (dx != 0) and (abs(dx) == abs(dy))


def is_valid_queen_move(x1, y1, x2, y2):
    dx, dy = _get_diffs(x1, y1, x2, y2)
    dx_abs = abs(dx)
    dy_abs = abs(dy)
    return (dx_abs > 0 and dy == 0) or \
        (dx == 0 and dy_abs > 0) or \
        (dx != 0 and dx_abs == dy_abs)


def is_valid_knight_move(x1, y1, x2, y2):
    dx, dy = _get_diffs(x1, y1, x2, y2)
    dx_abs = abs(dx)
    dy_abs = abs(dy)
    return (dx_abs == 2 and dy_abs == 1) or \
        (dx_abs == 1 and dy_abs == 2)
