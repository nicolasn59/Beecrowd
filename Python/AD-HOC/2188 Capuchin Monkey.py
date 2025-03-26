# SUBPROGRAM
def generateRegions(numTests):
    regions = list()
    maxX = minY = minU = maxV = 0
    for _ in range(numTests):
        region = list(map(int, input().split()))
        regions.append(region)
        if len(regions) == 1:
            maxX, minY, minU, maxV = region[0], region[1], region[2], region[3]
        else:
            if region[0] > maxX:
                maxX = region[0]
            if region[1] < minY:
                minY = region[1]
            if region[2] < minU:
                minU = region[2]
            if region[3] > maxV:
                maxV = region[3]
    return maxX, minY, minU, maxV

def checkIntersection(maxX, minY, minU, maxV, count):
    print("Teste %d" % count)
    if maxX >= minU:
        print("nenhum")
        print()
    elif minY <= maxV:
        print('nenhum')
        print()
    else:
        print("%d %d %d %d" % (maxX, minY, minU, maxV))
        print()
    return None

# MAIN PROGRAM
counter = 1
numTests = int(input())
while numTests != 0:
    maxX, minY, minU, maxV = generateRegions(numTests)
    checkIntersection(maxX, minY, minU, maxV, counter)
    numTests = int(input())
    counter += 1