import numpy as np

from grid_validation import validate_grid
from constants import QUEEN_STR, COLOR_STR


class Grid:
    GRID_SIZE = 4

    def __init__(self):
        self.grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=[(COLOR_STR, 'U1'), (QUEEN_STR, 'i1')])
            # 'U1' (a Unicode string of length 1).
            # 'i1' (a signed 8-bit integer).

        self.set_custom_grid()

    def set_custom_grid(self):
        colors = np.array([
            ['R', 'R', 'R', 'G'],
            ['R', 'Y', 'Y', 'G'],
            ['Y', 'Y', 'Y', 'B'],
            ['B', 'B', 'B', 'B']
        ])
        self.grid[COLOR_STR] = colors

    def reset_grid(self):
        self.grid[QUEEN_STR] = 0
        return "Grid reset successfully!"

    def put_queen(self, x, y):
        self.grid[x, y][QUEEN_STR] = 1
        validation_message = validate_grid(self.grid, x, y)
        return validation_message

    def remove_queen(self, x, y):
        self.grid[x, y][QUEEN_STR] = 0
        validation_message = validate_grid(self.grid, x, y)
        return validation_message
    
    def print_grid(self):
        print(self.grid)


if __name__ == '__main__':
    grid = Grid()
    grid.print_grid()
    print(grid.put_queen(0, 0))
    grid.print_grid()
    print(grid.put_queen(0, 1))
    grid.print_grid()

