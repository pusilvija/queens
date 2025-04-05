import numpy as np

from grid_validation import validate_grid
from grid_generation import generate_grid_colors, update_grid_with_queens

from constants import QUEEN_STR, COLOR_STR


class Grid:
    GRID_SIZE = None

    def __init__(self, size):
        self.GRID_SIZE = size
        self.grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=[(COLOR_STR, 'U1'), (QUEEN_STR, 'i1')])
            # 'U1' (a Unicode string of length 1).
            # 'i1' (a signed 8-bit integer).
        self._generate_colors()

    # def set_custom_grid(self):
    #     colors = np.array([
    #         ['R', 'R', 'R', 'G'],
    #         ['R', 'Y', 'Y', 'G'],
    #         ['Y', 'Y', 'Y', 'B'],
    #         ['B', 'B', 'B', 'B']
    #     ])
    #     self.grid[COLOR_STR] = colors

    # def set_custom_queens(self):
    #     queens = np.array([
    #         [0, 1, 0, 0],
    #         [0, 0, 0, 1],
    #         [1, 0, 0, 0],
    #         [0, 0, 1, 0]
    #     ])
    #     self.grid[QUEEN_STR] = queens

    def _generate_queens(self):
        self.grid = update_grid_with_queens(self.grid)

    def reset_queens(self):
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
    
    def _generate_colors(self):
        self._generate_queens()
        while True:
            try:
                self.grid[COLOR_STR] = generate_grid_colors(self)
                break
            except Exception as e:
                self._reset_colors()
        self.reset_queens()

    def _reset_colors(self):
        self.grid[COLOR_STR] = ''
    
    def print_grid(self):
        print(self.grid)


if __name__ == '__main__':
    grid = Grid(4)
    grid.print_grid()

