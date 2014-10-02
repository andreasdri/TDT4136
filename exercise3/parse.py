__author__ = 'Stein-Otto Svorstol'

def readFile(filename):
    file = open(filename, 'r')
    matrix = []
    for line in file:
        lineMatrix = []
        for char in line:
            if(char == '\n'):
                break
            lineMatrix.append(char)
        matrix.append(lineMatrix)
    return matrix

print(readFile('boards/board-1-1.txt'))

