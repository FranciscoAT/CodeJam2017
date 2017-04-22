import numpy as np
import networkx as nx

numCases = int(input())
for i in range(1, numCases+1):
    numCities, numTrips = [int(s) for s in raw_input().split(" ")]
    horsesDist, horseSpeed = [], []
    distMatrix = []

    for n in xrange(numCities):
        currDist, currSpeed = [int(s) for s in raw_input().split(" ")]
        horsesDist.append(currDist)
        horseSpeed.append(currSpeed)

    for n in xrange(numCities):
        curRow = [int(s) for s in raw_input().split(" ")]
        distMatrix.append(curRow)

    distMatrix = np.matrix(distMatrix)
    distGraph = nx.from_numpy_matrix(distMatrix)

    pairs = []

    for n in xrange(numTrips):
        currFromCity, currToCity = [int(s) for s in raw_input().split(" ")]
        pairs.append((currFromCity, currToCity))

    print (nx.shortest_path(distGraph, 0, 2))
    print("Case #{}:").format(i)
