__authors__ = 'Stein-Otto Svorstol and Andreas Drivenes'
import math, random

class Switchboard(object):
    def __init__(self, m, n, d, w, start, end):
    # 0 for no wire, 1 for regular wire, 2 for turn
        self.switchboard =  [[0 for x in range(n)] for x in range(m)]
        self.distanceCost = d
        self.turnCost = w
        self.start = start
        self.end = end

    def evaluateBoard(self):
        price = 0
        for line in self.switchboard:
            for val in line:
                if (val == 1):
                    price += self.distanceCost
                elif val == 2:
                    price += self.turnCost
        return price

    def __str__(self):
        return str(self.switchboard)





def simulatedAnnealing(M, N, D, W, start, end):
    # Takes Tmax and dT in to allow for experimentation.
    # When everything's done it'll only take the size of a the board, and eggs (M, N, k)
    State = Switchboard(M, N, D, W) # The State to be returned when optimal

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


def main(): # Missing starting points
    #print(simulatedAnnealing(4,4,3, 2, (1,4), (4, 4))) # M=N=4, D=3, W=2
    #print(simulatedAnnealing(6, 5, 3, 2, (), (6, 5)))
    #print(simulatedAnnealing(8, 8, 3, 2, (), (8, 8)))
    print(Switchboard(4,2,3, 2, (1,4), (4, 4)))

main()