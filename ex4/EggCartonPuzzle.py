__authors__ = 'Stein-Otto Svorstol and Andreas Drivenes'


import random
import numpy as np
import math

class Board(object):
	def __init__(self, board=[], k=0):
		self.board = board
		if len(board) > 0:
			self.n = len(self.board[0])
			self.m = len(self.board)
		self.k = k

	# Generate a puzzle with m rows, n columns
	def generateEggBoard(self, m, n, k):
		# No eggs initially
		self.board = [[False for x in range(n)] for y in range(m)]
		# Our constraint
		self.k = k
		self.n = len(self.board[0])
		self.m = len(self.board)

	def __str__(self):
		board = ''
		for y in range(self.m):
			for x in range(self.n):
				cell = self.board[y][x]
				if cell == True:
					board += 'Egg'
				else:
					board += 'x'
				board += '	'
				if(x == self.n - 1):
					board += '\n\n'
		return board

	def evaluateBoard(self):
		spareEggs = 0.0

		# this should be correct for quadratic puzzles, dont know how good the estimate is for rectangular puzzles
		numberOfEggsInSolution = min(self.n, self.m) * self.k * 1.0

		# constraint on rows
		for row in self.board:
			eggs = 0.0
			for cell in row:
				if cell:
					eggs += 1
			spareEggs += Board.calculateValue(eggs, self.k)

		# contstraint on columns
		for x in range(self.n):
			column = [row[x] for row in self.board]
			eggs = 0.0
			for cell in column:
				if cell:
					eggs += 1

			spareEggs += Board.calculateValue(eggs, self.k)

		# constraint on diagonals
		# used a four liner we found on stackoverflow for getting diagonals with numpy
		a = np.asarray(self.board)
		diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
		diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
		diagonals = [n.tolist() for n in diags]

		for diagonal in diagonals:
			eggs = 0.0
			# no need to check diagonals equal or shorter than k! 
			if len(diagonal) > self.k:
				for cell in diagonal:
					if cell:
						eggs += 1
				spareEggs += Board.calculateValue(eggs, self.k)

		eggPlaced = 0.0
		for row in self.board:
			for cell in row:
				if cell:
					eggPlaced += 1

		eggFraction = eggPlaced/numberOfEggsInSolution
		# penalize 0.1 per constraint break
		evaluation = eggFraction - spareEggs*0.1
		return evaluation

	def generateNeighbours(self):
		neighbours = []
		# generate n*m neighbours with one randomly placed change compared to the parent
		for i in range(self.n*self.m):
			x = random.randint(0, self.n - 1)
			y = random.randint(0, self.m - 1)
			cell = self.board[y][x]
			cell = True if cell == False else False
			neighbours.append(Board(Board.copyList(self.board, cell, x, y), self.k))

		return neighbours

	def calculateValue(eggs, k):
		return eggs - k if eggs > k else 0

	# returns a new copy of the list with a switched cell. todo: use clone?
	def copyList(array, cell, x, y):
		newArray = [[None] * len(array[0]) for i in range(len(array))]
		for i in range(len(array)):
			for j in range(len(array[0])):
				if(i == y and j == x):
					newArray[i][j] = cell
				else:
					newArray[i][j] = array[i][j]
		return newArray



def simulatedAnnealing(problemData, Tmax, dT, targetBoardEvaluation):
	# Takes Tmax and dT in to allow for experimentation.
	# Problemdata is [M, N, K]
	state = Board() # The State to be returned when optimal
	state.generateEggBoard(problemData[0], problemData[1], problemData[2]) # Initial values
	temp = Tmax
	iterations = 0
	while (state.evaluateBoard() < targetBoardEvaluation):
		if temp < 0:
			break
		neighbours = state.generateNeighbours()
		bestNeighbour = neighbours[0]
		for neighbour in neighbours: # Loop through neighbours to find the best one
			if (neighbour.evaluateBoard() > bestNeighbour.evaluateBoard()): # Is this better than the best?
				bestNeighbour = neighbour
		q = 0.0
		if state.evaluateBoard() != 0:
			q = ((bestNeighbour.evaluateBoard()-state.evaluateBoard())/state.evaluateBoard()) # Now lets do some calculations

		p = min(1, math.exp((-q)/temp)) # To find if we want to go in that direction
		x = random.random() # Random number between 0 and 1
		if x > p:
			state = bestNeighbour
		else:
			state = neighbours[random.randint(0, len(neighbours) - 1)] # None of them were very good, choose a random one
		temp -= dT # We don't wanna go on forever now do we?
		iterations += 1

	print(iterations, state.evaluateBoard())
	return state

def main():
	print(simulatedAnnealing([5,5, 2], 0.07, 0.00001, 1))
	print(simulatedAnnealing([6, 6, 2], 0.07, 0.00001, 1))
	print(simulatedAnnealing([8, 8, 1], 0.07, 0.00001, 1))
	print(simulatedAnnealing([10, 10, 3], 0.07, 0.00001, 1))

main()