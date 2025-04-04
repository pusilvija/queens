import numpy as np

from app.grid_validation import validate_grid
from app.constants import QUEEN_STR, COLOR_STR


class Grid:
    GRID_SIZE = 4

    def __init__(self):
        self.grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=[(COLOR_STR, 'U1'), (QUEEN_STR, 'i1')])
            # 'U1' (a Unicode string of length 1).
            # 'i1' (a signed 8-bit integer).

        self.setCustomGrid()

    def setCustomGrid(self):
        colors = np.array([
            ['R', 'R', 'R', 'G'],
            ['R', 'Y', 'Y', 'G'],
            ['Y', 'Y', 'Y', 'B'],
            ['B', 'B', 'B', 'B']
        ])
        self.grid[COLOR_STR] = colors

    def resetGrid(self):
        self.grid[QUEEN_STR] = 0
        return "Grid reset successfully!"

    def putQueen(self, x, y):
        self.grid[x, y][QUEEN_STR] = 1
        validation_message = validate_grid(self.grid, x, y)
        return validation_message

    def removeQueen(self, x, y):
        self.grid[x, y][QUEEN_STR] = 0
        validation_message = validate_grid(self.grid, x, y)
        return validation_message
    
    def printGrid(self):
        print(self.grid)


if __name__ == '__main__':
    grid = Grid()
    grid.printGrid()
    print(grid.putQueen(0, 0))
    grid.printGrid()
    print(grid.putQueen(0, 1))
    grid.printGrid()

