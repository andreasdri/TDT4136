from sys import stdin

def print_path(node, predec):
   if predec[node] == None:
       return str(0)
   return print_path(predec[node], predec) + "-" + str(node)


def extractMin(Q, estimat):
    max_prob = 0
    best_node = None
    for node in Q:
        if estimat[node] > max_prob:
            max_prob = estimat[node]
            best_node = node
    return best_node



def beste_sti(nm, prob):
    n = len(nm[0])
    last_node = n-1
    S = set() # shortest path already determined
    Q = set(i for i in range(n))

    estimat = [0.0]*n
    estimat[0] = prob[0]
    predec = [None]*n

    while Q:
        u = extractMin(Q, estimat)
        if u == last_node or u == None:
            break
        S.add(u)
        Q.remove(u)
        for adj_u in Q:
            if nm[u][adj_u]:
                if estimat[u]*prob[adj_u] > estimat[adj_u]:
                    estimat[adj_u] = estimat[u]*prob[adj_u]
                    predec[adj_u] = u

    return print_path(last_node, predec)

def solve():
    n = int(stdin.readline())
    sansynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print beste_sti(nabomatrise, sansynligheter)

solve()