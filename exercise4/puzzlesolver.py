__authors__ = 'Stein-Otto Svorstol and Andreas Drivenes'


import random
import numpy as np
import math

class Board(object):
	def __init__(self, board=[]):
		self.board = board

	# Generate a puzzle with m rows, n columns
	def generateEggBoard(self, m, n, k):
		# The eggs are randomly placed
		self.board = [[random.choice([True, False]) for x in range(n)] for y in range(m)]
		# Our constraint
		self.k = k

	def printBoard(self):
		board = ''
		for y in range(len(self.board)):
			for x in range(len(self.board[0])):
				cell = self.board[y][x]
				if cell == True:
					board += 'Egg'
				else:
					board += 'Empty'
				board += '	'
				if(x == len(self.board[0]) - 1):
					board += '\n\n'
		print(board)

	def evaluateBoard(self):
		value = 1
		n = len(self.board[0])
		m = len(self.board)
		# constraint on rows
		for row in self.board:
			eggs = 0
			for cell in row:
				if cell == True:
					eggs += 1
			value += Board.calculateValue(eggs, self.k)

		# contstraint on columns
		for x in range(n):
			column = [row[x] for row in self.board]
			eggs = 0
			for cell in column:
				if cell == True:
					eggs += 1

			value += Board.calculateValue(eggs, self.k)



		# constraint on diagonals
		a = np.asarray(self.board)
		diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
		diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
		diagonals = [n.tolist() for n in diags]
		for diagonal in diagonals:
			eggs = 0
			if len(diagonal) > 1:
				for cell in diagonal:
					if cell == True:
						eggs += 1
				if eggs > self.k:
					value += (self.k - eggs)/20
				elif eggs < self.k:
					value += (eggs - self.k)/20
				else: 
					value += 0.05

		return value

	def calculateValue(eggs, k):
		if eggs > k:
			return (k - eggs)/10
		elif eggs < k:
			return (eggs - k)/10
		else:
			return 0.20

    def generateNeighbours():
        neighbours = []
        return neighbours


def simulatedAnnealing(problemData, Tmax, dT, targetBoardEvaluation):
    # Takes Tmax and dT in to allow for experimentation.
    # Problemdata is [M, N, K]
    state = Board() # The State to be returned when optimal
    state.generateEggBoard(problemData[0], problemData[1], problemData[2]) # Initial values
    temp = Tmax
    while (state.evaluateBoard() < targetBoardEvaluation):
        neighbours = state.generateNeighbours()
        bestNeighbour = neighbours[0]
        for neighbour in neighbours: # Loop through neighbours to find the best one
            if (neighbour.evaluateBoard() > bestNeighbour.evaluateBoard()): # Is this better than the best?
                bestNeighbour = neighbour
        q = ((bestNeighbour.evaluateBoard()-state.evaluateBoard())/state.evaluateBoard()) # Now lets do some calculations
        p = math.min(1, math.e((-q)/temp)) # To find if we want to go in that direction
        x = random.random() # Random number between 0 and 1
        if x > p:
            state = bestNeighbour
        else:
            state = neighbours[random.randint(0, len(neighbours))] # None of them were very good, choose a random one
        temp -= dT # We don't wanna go on forever now do we?
    return state


def main():
    print(simulatedAnnealing([5,5, 2], 1, 0.01, 0.7))
    print(simulatedAnnealing([6, 6, 2], 1, 0.01, 0.7))
    print(simulatedAnnealing([8, 8, 1], 1, 0.01, 0.7))
    print(simulatedAnnealing([10, 10, 3], 1, 0.01, 0.7))

main()