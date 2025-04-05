import numpy as np

from grid_validation import validate_grid
from grid_generation import generate_grid_colors, update_grid_with_queens

from constants import QUEEN_STR, COLOR_STR


class Grid:
    GRID_SIZE = None

    def __init__(self, size):
        self.GRID_SIZE = size
        self.grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=[(COLOR_STR, 'i1'), (QUEEN_STR, 'i1')])
        self._generate_grid()

    # def set_custom_grid(self):
    #     colors = np.array([
    #         ['R', 'R', 'R', 'G'],
    #         ['R', 'Y', 'Y', 'G'],
    #         ['Y', 'Y', 'Y', 'B'],
    #         ['B', 'B', 'B', 'B']
    #     ])
    #     self.grid[COLOR_STR] = colors

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
    
    def _generate_grid(self):
        self.grid = update_grid_with_queens(self.grid)
        while True:
            try:
                self.grid[COLOR_STR] = generate_grid_colors(self)
                break
            except Exception as e:
                self._reset_colors()
        self.reset_queens()

    def _reset_colors(self):
        self.grid[COLOR_STR] = 0
    
    def print_grid(self):
        print(self.grid)

    def get_grid_json(self):
        grid_json = {
            "grid": [
            {
                "x": x,
                "y": y,
                "color": int(self.grid[x, y][COLOR_STR]),
            }
            for x in range(self.GRID_SIZE)
            for y in range(self.GRID_SIZE)
            ],
            "size": self.GRID_SIZE
        }
        return grid_json

if __name__ == '__main__':
    grid = Grid(4)
    grid.print_grid()
    print(grid.get_grid_json())

