import numpy as np

from constants import QUEEN_STR, COLOR_STR


def validate_grid(grid, x, y):
    messages = []

    if not validate_color(grid):
        messages.append("Multiple queens of the same color.")
    if not validate_col(grid):
        messages.append("Multiple queens in the same column.")
    if not validate_row(grid):
        messages.append("Multiple queens in the same row.")
    if not validate_neighbors(grid, x, y):
        messages.append(f"Multiple queens in the neighborhood of ({x}, {y}).")

    if messages:
        messages.insert(0, "Grid validation failed: ")
        return " | ".join(messages)
    elif grid[QUEEN_STR].sum() == 4:
        return "Victory"
    else:
        return "Validation successful!"


def validate_color(grid):
    distinct_colors = np.unique(grid[COLOR_STR])
    for color in distinct_colors:
        if np.sum(grid[grid[COLOR_STR] == color][QUEEN_STR]) > 1:
            return False
    return True


def validate_col(grid):
    col = grid[:, 0]
    if col[QUEEN_STR].sum() > 1:
        return False
    return True


def validate_row(grid):
    row = grid[0, :]
    if row[QUEEN_STR].sum() > 1:
        return False
    return True


def validate_neighbors(grid, x, y):
    grid_size = grid.shape[0]
    neighbors_coords = np.array(get_neighbors_coords(grid_size, x, y))
    if grid[neighbors_coords[:, 0], neighbors_coords[:, 1]][QUEEN_STR].sum() > 1:
        return False
    return True


def get_neighbors_coords(grid_size, x, y):
    """Get the neighbors of a specific coordinate (x, y) in the grid."""
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    return [
        (x + dx, y + dy)
        for dx, dy in directions
        if 0 <= x + dx < grid_size and 0 <= y + dy < grid_size
    ]
