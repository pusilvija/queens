import pdb
import numpy as np

from constants import COLOR_STR, QUEEN_STR


def update_grid_with_queens(grid):
    size = grid.shape[0]

    while True:
        grid, queen_dict, available_queen_index = reset_grid(grid, size)

        while sum(queen_dict.values()) < size:
            grid, available_queen_index, queen_dict, size = add_queen(grid, available_queen_index, queen_dict, size)

            if len(available_queen_index) == 0:
                break
        else:
            print("All queens placed successfully!")
            break

    return grid


def reset_grid(grid, size):
    grid[QUEEN_STR] = 0
    queen_dict = {i: 0 for i in range(size * size)}
    available_queen_index = np.arange(0, size * size)
    return grid, queen_dict, available_queen_index


def add_queen(grid, available_queen_index, queen_dict, size):

    # Check if there are any available positions left
    if len(available_queen_index) == 0:
        return grid, available_queen_index, queen_dict, size

    # Randomly select an index from the available positions and update avaiable_queen_index
    random_index = int(np.random.choice(available_queen_index))
    available_queen_index = np.delete(available_queen_index, np.where(available_queen_index == random_index))

    row, col = get_index_coordinates(random_index, size)
    if is_valid_position(grid, row, col):
        queen_dict[random_index] = 1
        grid[row, col][QUEEN_STR] = 1

        if sum(queen_dict.values()) == size:
            return grid, available_queen_index, queen_dict, size
        else:
            return add_queen(grid, available_queen_index, queen_dict, size)
        
    else:
        return add_queen(grid, available_queen_index, queen_dict, size)
    

def get_index_coordinates(index, size):
    row = index // size
    col = index % size
    return row, col


def is_valid_position(grid, row, col):
    """
    Check if placing a queen at (row, col) is valid.
    - No queens in the same row or column.
    - No queens in the neighborhood of (row, col).
    """
    size = grid.shape[0]

    # Check for queens in the same row or column
    for i in range(size):
        if grid[row, i][QUEEN_STR] == 1 or grid[i, col][QUEEN_STR] == 1:
            return False  # Invalid if a queen is in the same row or column

    # Check for queens in the neighborhood
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    for dx, dy in directions:
        x, y = row + dx, col + dy
        if 0 <= x < size and 0 <= y < size and grid[QUEEN_STR][x, y] == 1:
            return False  # Invalid if a queen is in the neighborhood

    return True

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