# SUBPROGRAM
def calculateStonesMoved(numPiles, stoneCubes):
    sumCubes = sumPositions = stonesMoved = countDifference = 0
    ladder = list()

    # CHECKING IF THE PILES HAVE THE SAME NUMBER OF STONES
    count = 1
    while count != numPiles:
        countDifference += stoneCubes[count-1] - stoneCubes[count]
        count += 1
    if countDifference == 0:
        print(-1)
        return None
    ####

    count = 0
    while count != numPiles:
        sumCubes += stoneCubes[count]
        count += 1
    count = 0
    while count != numPiles:
        sumPositions += count
        count += 1

    # NUMBER OF STONES IN THE FIRST PILE OF THE LADDER
    ladderStart = (sumCubes - sumPositions) // numPiles

    # CHECKING IF A PERFECT LADDER CAN BE MADE
    if (sumCubes - sumPositions) % numPiles == 0:
        count = 0
        while count != numPiles:
            ladder.append(ladderStart + count)
            count += 1
        count = 0
        while count != numPiles:
            difference = stoneCubes[count] - ladder[count]
            if difference >= 0:
                stonesMoved += difference
            count += 1
        print(stonesMoved)
    else:
        print(-1)
    return None

# MAIN PROGRAM
numPiles = int(input())
stoneCubes = list(map(int, input().split()))
calculateStonesMoved(numPiles, stoneCubes)