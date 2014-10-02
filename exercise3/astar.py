f = open('boards/board-1-1.txt')
board = []
start = (0,0)
finish = (0,0)

for line in f:
	row = []
	for element in line:
		if not element == '\n':
			row.append(element)
	board.append(row)
	
for i in xrange(0, len(board)):
	for j in xrange(0, len(board[0])):
		if board[i][j] == 'A':
			start = (i, j)
		elif board[i][j] == 'B':
			finish = (i, j)

print board
print start
print finish

class Node:
	def __init__(self, g, h, x, y):
		self.g = g
		self.h = h
		self.x = x
		self.y = y
		self.type = 'start'
		self.parent = None
		self.children = None
	def setParent(parent):
		self.parent = parent
	def addChildren(children):
		self.children.append(children)
	def isGoalNode(self):
		return self.type == 'finish'


def best_first_search(board, startNode, finishNode):
	closedSet = set()
	openSet = set()
	openSet.add(start)

	while openSet:
		currentNode = min(openSet, key: lambda node: node.g + node.h) 
		closedSet.add(currentNode)
		if currentNode == finish:
			return an answer
		openSet.remove(currentNode)






	