import numpy as np

from constants import QUEEN_STR, COLOR_STR

def generate_grid_colors(grid):
    squares_total = grid.GRID_SIZE ** 2
    colors_total = grid.GRID_SIZE
    color_options = np.arange(1, colors_total + 1)
    color_sizes = 1 + np.random.multinomial(squares_total-colors_total, [1/colors_total]*colors_total, size=1)[0]
    queens_coordinates = np.argwhere(grid.grid[QUEEN_STR] == 1)
    for color, size, queen in zip(color_options, color_sizes, queens_coordinates):
        row, col = queen     
        grid.grid[COLOR_STR][row,col] = color

        for i in range(size-1):
            row_next, col_next = get_random_neighbor_coords(grid, row, col)
            grid.grid[COLOR_STR][row_next,col_next] = color
    return grid.grid[COLOR_STR]

def get_random_neighbor_coords(grid, x, y):
    directions = [
        (-1, 0), (0, -1), (0, 1),  (1, 0)
    ]
    grid_size = grid.GRID_SIZE
    all_neighbors = [
        (x + dx, y + dy)
        for dx, dy in directions
        if 0 <= x + dx < grid_size and 0 <= y + dy < grid_size
    ]
    available_neighbors = [
        (xa, ya)
        for xa, ya in all_neighbors
        if not is_queen(grid.grid, xa, ya) and not is_colored(grid.grid, xa, ya)
    ]
    same_color_neighbors = [
        (xc, yc) for xc, yc in all_neighbors if grid.grid[COLOR_STR][xc, yc] == grid.grid[COLOR_STR][x, y]
    ]
    if len(available_neighbors) == 0 and np.sum(grid.grid[COLOR_STR] != '') != grid_size ** 2:
        x_next, y_next = same_color_neighbors[np.random.randint(0, len(same_color_neighbors))]
        return get_random_neighbor_coords(grid, x_next, y_next)
    else:
        return available_neighbors[np.random.randint(0, len(available_neighbors))] or None

def is_queen(grid, x, y):
    return grid[x, y][QUEEN_STR] == 1

def is_colored(grid, x, y):
    return grid[x, y][COLOR_STR] != ''


