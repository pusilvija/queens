import numpy as np

COLOR_INDEX = 0
QUEEN_INDEX = 1

class Grid:
    GRID_SIZE = 4


    def __init__(self):
        self.grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=object)
        self.setCustomGrid()

    
    def setCustomGrid(self):
        self.grid[0, 0] = ('R', 0)
        self.grid[1, 0] = ('R', 0)
        self.grid[2, 0] = ('R', 0)
        self.grid[3, 0] = ('G', 0)

        self.grid[0, 1] = ('R', 0)
        self.grid[1, 1] = ('Y', 0)
        self.grid[2, 1] = ('Y', 0)
        self.grid[3, 1] = ('G', 0)

        self.grid[0, 2] = ('Y', 0)
        self.grid[1, 2] = ('Y', 0)
        self.grid[2, 2] = ('Y', 0)
        self.grid[3, 2] = ('B', 0)

        self.grid[0, 3] = ('B', 0)
        self.grid[1, 3] = ('B', 0)
        self.grid[2, 3] = ('B', 0)
        self.grid[3, 3] = ('B', 0)

    def putQueen(self, x, y):
        # Place a queen on the grid at the specified coordinates
        self.grid[x, y] = (self.grid[x, y][QUEEN_INDEX], 1)

    def removeQueen(self, x, y):
        # Place a queen on the grid at the specified coordinates
        self.grid[x, y] = (self.grid[x, y][QUEEN_INDEX], 0)

    def validateGrid(self):
        # Validate the position of the queen on the grid
        #TODO implement logic for validation
        
        
    def hasQueenOnColor(self):
        return np.sum((self.grid[:, :, COLOR_INDEX] == 'B') & (self.grid[:, :, QUEEN_INDEX] == 1)) > 1
    
    def printGrid(self):
        print(self.grid)

if __name__ == '__main__':
    grid = Grid()
    grid.printGrid()  # Should return True since no queens are in the same row/column/diagonal