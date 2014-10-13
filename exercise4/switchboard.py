__authors__ = 'Stein-Otto Svorstol and Andreas Drivenes'
import math, random

class Switchboard(object):
    def __init__(self, m, n, d, w, start, end):
		self.switchboard = []
        self.distance = d
        self.turnCost = w
        for i in range (0, n):




def simulatedAnnealing(M, N, D, W, start, end):
    # Takes Tmax and dT in to allow for experimentation.
    # When everything's done it'll only take the size of a the board, and eggs (M, N, k)
    State = Switchboard(M, N, D, W) # The State to be returned when optimal
    State.generateEggs(5, 5, 2) # Initial values

    #Just some values for now
    Temp = 0.7
    dT = 0.01
    targetBoardEvaluation = 0.7
    while (State.evaluateBoard() < targetBoardEvaluation):
        neighbours = State.generateNeighbours()
        newState = None # The best neighbour
        for neighbour in neighbours: # Loop through neighbours to find the best one
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
    return State


def main():
    print(simulatedAnnealing(4,4,3, 2, [])) # M=N=4, D=3, W=2
    print(simulatedAnnealing(6, 5, 3, 2, []))