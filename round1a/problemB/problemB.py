from heapq import heappush, heappop

numCases = int(input())
for i in range(1, numCases+1):
    numIngredients, numPackages = [int(s) for s in raw_input().split(" ")]
    serving = [int(s) for s in raw_input().split(" ")]

    packageList = []
    filledPackageList = []
    for s in xrange(numIngredients):
        tempList = [int(s) for s in raw_input().split(" ")]
        packageList.append(tempList)

    print packageList

    for index in xrange(numIngredients):
        packages = packageList[index]
        newList = []
        for x in xrange(numPackages):
            multiplier = round((packages[x]*1.0)/(serving[index]*1.0))
            litmus = multiplier*serving[index]
            if(0.9*litmus <= packages[x] and packages[x] <= 1.1*litmus):
                filledPackageList[index][x][multiplier] = filledPackageList[index][x][multiplier].append(packages[x])

    for index in xrange(numPackages):
        currentPackages = []
        for ingredient in xrange(numIngredients):
            currentPackages[ingredient] = heappop(packageList[index])




    numAllowed = 0




    print("Case #{}: {}").format(i,numAllowed)
