from heapq import heappush, heappop
from math import ceil

numCases = int(input())
for i in range(1, numCases+1):
    stalls, people = [int(s) for s in raw_input().split(' ')]
    nextStall = []
    heappush(nextStall, stalls*-1)

    leftSpace, rightSpace = 0, 0
    if ((people)*2 > stalls):
        people = 0

    while(people != 0):
        nextStallNum = int(heappop(nextStall))*-1
        nextStallIndex = int(ceil(nextStallNum/2.0))

        leftSpace = nextStallIndex-1
        rightSpace = nextStallNum-nextStallIndex

        if (leftSpace < 0):
            leftSpace = 0
        else:
            heappush(nextStall, leftSpace*-1)
        if (rightSpace < 0):
            rightSpace = 0
        else:
            heappush(nextStall, rightSpace*-1)

        people -= 1

    lastTuple = (leftSpace, rightSpace)
    print("Case #{}: {} {}").format(i, max(lastTuple), min(lastTuple))
