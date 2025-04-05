import pdb
import numpy as np

from constants import COLOR_STR, QUEEN_STR


def generate_grid(size):
    empty_grid = np.zeros((size, size), dtype=[(COLOR_STR, 'U1'), (QUEEN_STR, 'i1')])
    queen_dict = {i: 0 for i in range(size*size)}
    available_queen_index = np.arange(0, size*size)
    grid_with_queens = place_queens(empty_grid, available_queen_index, queen_dict, size)
    return grid_with_queens


def place_queens(grid, available_queen_index, queen_dict, size):
    while True:
        # reset
        grid[QUEEN_STR] = 0
        queen_dict = {i: 0 for i in range(size * size)}
        available_queen_index = np.arange(0, size * size)

        while sum(queen_dict.values()) < size:
            grid, available_queen_index, queen_dict, size = add_queen(grid, available_queen_index, queen_dict, size)

            if len(available_queen_index) == 0:
                break
        else:
            # If all queens are placed successfully, exit the loop
            # print("All queens placed successfully!")
            break

    print("Final grid after placing queens:")
    print(grid[QUEEN_STR])
    print(grid)

    return grid


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
    
    return grid, available_queen_index, queen_dict, size


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


if __name__ == '__main__':
    grid = generate_grid(10)
    # print(grid)