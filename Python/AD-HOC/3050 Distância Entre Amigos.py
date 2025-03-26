# SUBPROGRAM
def maxDistance(numBuildings, numFloors):
    maxDistance = numFloors[0] - 1
    start = 1
    for i in range(numBuildings):
        for j in range(start, len(numFloors)):
            if (((numFloors[i] + numFloors[j])-2) + abs(i - j)) > maxDistance:
                maxDistance = ((numFloors[i] + numFloors[j])) + abs(i - j)
        start += 1
    print(maxDistance)
    return None

# MAIN
numBuildings = int(input())
numFloors = list(map(int, input().split()))
# numFloors = [floor + 1 for floor in numFloors]
maxDistance(numBuildings, numFloors)