__authors__ = 'Stein-Otto Svorstol and Andreas Drivenes'


import random
import numpy as np
import math

class Board(object):
	def __init__(self, board=[]):
		self.board = board

	# Generate a puzzle with m rows, n columns
	def generateEggs(self, m, n, k):
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



def simulatedAnnealing(Tmax, dT, targetBoardEvaluation):
    # Takes Tmax and dT in to allow for experimentation.
    # When everything's done it'll only take the size of a the board, and eggs (M, N, k)
    State = Board() # The State to be returned when optimal
    State.generateEggs(5, 5, 2) # Initial values
    Temp = Tmax
    while (State.evaluateBoard() < targetBoardEvaluation):
        neighbours = State.generateNeighbours()
        newState = None # The best neighbour
        for (neighbour in neighbours): # Loop through neighbours to find the best one
            if (neighbour.evaluateBoard() > newState):
                newState = neighbour
        q = ((newState.evaluateBoard()-State.evaluateBoard())/State.evaluateBoard())
        p = math.min(1, math.e((-q)/Temp))
        x = random.random() # Random number between 0 and 1
        if (x > p ):
            State = newState
        else:
            State = neighbours[random.randint(0, len(neighbours))] # None of them were very good, choose a random one
        Temp -= dT
    return State;


def main():
	# board = Board()
	# board.generateEggs(3, 3, 1)
	# board.printBoard()
	# print(board.evaluateBoard())
	bestValue = -1000000
	bestBoard = Board()
	for i in range(100000):
		board = Board()
		board.generateEggs(5, 5, 2)
		
		value = board.evaluateBoard()
		if value > bestValue:
			bestValue = value
			bestBoard = board
	print(bestValue)
	print(bestBoard.printBoard())



main()