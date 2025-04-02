import numpy as np


COLOR_STR = 'color'
QUEEN_STR = 'queen'

COLOR_INDEX = 0
QUEEN_INDEX = 1


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

    def putQueen(self, x, y):
        self.grid[x, y][QUEEN_STR] = 1
        self._validateGrid(x, y)

    def removeQueen(self, x, y):
        self.grid[x, y][QUEEN_STR] = 0
        self._validateGrid(x, y)

    def _validateGrid(self, x, y):
        self._validateColor()
        self._validateCol()
        self._validateRow()
        self._validateNeighbors(x, y)
        
    def _validateColor(self):
        distinct_colors = np.unique(self.grid[COLOR_STR])
        for color in distinct_colors:
            if np.sum(self.grid[self.grid[COLOR_STR] == color][QUEEN_STR]) > 1:
                print(f"Invalid grid: Multiple queens of color {color} found.")
                return False
        return True
    
    def _validateCol(self):
        col = self.grid[:, 0]
        if col[QUEEN_STR].sum() > 1:
            print("Invalid grid: Multiple queens in the same column.")
            return False
        return True

    def _validateRow(self):
        row = self.grid[0, :]
        if row[QUEEN_STR].sum() > 1:
            print("Invalid grid: Multiple queens in the same row.")
            return False
        return True
    
    def _validateNeighbors(self, x, y):
        neighbors_coords = np.array(self._getNeighborsCoords(x, y))
        if self.grid[neighbors_coords[:, 0], neighbors_coords[:, 1]][QUEEN_STR].sum() >= 1:
            print(f"Invalid grid: Multiple queens in the same neighborhood.")
            return False
        return True

    def _getNeighborsCoords(self, x, y):
        """Get the neighbors of a specific coordinate (x, y) in the grid."""
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        return [
            (x + dx, y + dy)
            for dx, dy in directions
            if 0 <= x + dx < self.GRID_SIZE and 0 <= y + dy < self.GRID_SIZE
        ]
    
    def printGrid(self):
        print(self.grid)


if __name__ == '__main__':
    grid = Grid()
    grid.putQueen(0, 0)
    grid.putQueen(0, 1)
    grid.putQueen(1, 0)
    grid.putQueen(1, 1)

    grid.printGrid()
