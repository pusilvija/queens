import numpy as np

from app.grid import Grid
from constants import QUEEN_STR


# Utility Functions
def initialize_queens_dict(size):
    """
    Initialize the queen dictionary with all positions set to 0.
    """
    return {i: 0 for i in range(size * size)}


def initialize_available_indices(size):
    """
    Initialize an array of all available indices for the grid.
    """
    return np.arange(0, size * size)


def select_random_index(available_queen_index):
    """
    Select a random index from the available positions and remove it.
    """
    random_index = int(np.random.choice(available_queen_index))
    available_queen_index = np.delete(available_queen_index, np.where(available_queen_index == random_index))
    return random_index, available_queen_index


def get_index_coordinates(index, size):
    """
    Calculate the row and column coordinates of a given index in a grid.
    """
    row = index // size
    col = index % size
    return row, col


def set_queen_position(grid, queen_dict, index, row, col):
    """
    Set a queen's position on the grid and update the queen dictionary.
    """
    queen_dict[index] = 1
    grid[row, col][QUEEN_STR] = 1


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
            return False

    # Check for queens in the neighborhood
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    for dx, dy in directions:
        x, y = row + dx, col + dy
        if 0 <= x < size and 0 <= y < size and grid[QUEEN_STR][x, y] == 1:
            return False

    return True


# Grid Initialization
def reset_grid(grid, size):
    """
    Reset the grid and initialize the queen dictionary and available indices.
    """
    grid[QUEEN_STR] = 0
    queen_dict = initialize_queens_dict(size)
    available_queens_index = initialize_available_indices(size)
    return grid, queen_dict, available_queens_index


# Queen Placement Logic
def add_queen(grid, available_queen_index, queen_dict, size):
    """
    Attempt to place a queen on the grid.
    If no valid positions are left, return the current state.
    """
    if not available_queen_index.size:
        return grid, available_queen_index, queen_dict, size

    random_index, available_queen_index = select_random_index(available_queen_index)
    row, col = get_index_coordinates(random_index, size)

    if is_valid_position(grid, row, col):
        set_queen_position(grid, queen_dict, random_index, row, col)

        if np.sum(grid[QUEEN_STR]) == size:
            return grid, available_queen_index, queen_dict, size

    return add_queen(grid, available_queen_index, queen_dict, size)


def place_queens(grid, queen_dict, available_queen_index, size):
    """
    Place queens on the grid one by one.
    Returns True if all queens are placed successfully, False otherwise.
    """
    while np.sum(grid[QUEEN_STR]) < size:
        grid, available_queen_index, queen_dict, size = add_queen(grid, available_queen_index, queen_dict, size)

        if not available_queen_index.size:
            print("Failed to place all queens. Retrying...")
            return False

    return True


def update_grid_with_queens(grid):
    """
    Attempt to place queens on the grid until all queens are placed successfully.
    If no valid positions are left, reset the grid and try again.
    """
    size = grid.shape[0]

    while True:
        grid, queens_dict, available_queens_index = reset_grid(grid, size)

        if place_queens(grid, queens_dict, available_queens_index, size):
            print("All queens placed successfully!")
            break

    return grid
