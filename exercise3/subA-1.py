# Subtask A-1
# Solving with A*
__author__ = 'Stein-Otto Svorstol'

import heapq

class Cell(object):
    def __init__(self, x, y, reachable):
        self.x = x
        self.y = y
        self.reachable = reachable

# # is wall
# A is start
# B is goal
# . is empty cell


class AStar(object):
    def __init__(self):
        self.opened = [] # Visited nodes
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid_height = 0 # Set in init_grid
        self.grid_width = 0
        self.init_grid()

    def readFile(self, filename):
        #Goes over file and creates a matrix of it
        file = open(filename, 'r')
        matrix = []
        for line in file:
            lineMatrix = []
            for char in line:
                if(char == '\n'): # We don't want the linebreak in our matrix.
                    break
                lineMatrix.append(char)
            matrix.append(lineMatrix)
        return matrix

    def getAB(self, matrix):
        # Goes over a matrix and returns location of A and B
        A, B = (0,0), (0,0)
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if(matrix[y][x] == 'A'):
                    A = (x, y)
                elif (matrix[y][x] == 'B'):
                    B = (x, y)
        return A, B

    def getWalls(self, matrix):
        # Goes over a matrix and returns coordinates for the walls as a list
        walls = []
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if(matrix[y][x] == '#'):
                    walls.append((x, y))
        return walls

    def init_grid(self):
        # First get our coordinates:
        matrix = self.readFile('boards/board-1-1.txt') # Need method for giving coordinates of walls
        walls = self.getWalls(matrix)
        start, end = self.getAB(matrix)

        self.grid_height = len(matrix)
        self.grid_width = len(matrix[0])


        # Let's make some cells
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                reachable = True if (x, y) in walls else False
                self.cells.append(Cell(x, y, reachable))
        self.start = start # These needs to be made into cells.
        self.end = end

    def printEverything(self): # test
        print(self.cells)


thing = AStar().printEverything() # test
