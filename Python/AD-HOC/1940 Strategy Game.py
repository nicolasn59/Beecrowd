# SUBPROGRAM
def calculatePoints(players, rounds, points):
    totalPoints = [0] * players
    for row in range(rounds):
        for col in range(players):
            totalPoints[col] += points[row][col]
    return totalPoints

def findWinner(players, rounds, totalPoints):
    maxPoints = totalPoints[0]
    player = 1
    for point in range(1, players):
        if totalPoints[point] >= maxPoints:
            maxPoints = totalPoints[point]
            player = point + 1
    print(player)
    return None

# MAIN PROGRAM
points = list()
numPlayers, numRounds = map(int, input().split())
roundPoints = list(map(int, input().split()))
for i in range(numRounds):
   row = list()
   for j in range(numPlayers):
       row.append(roundPoints[j])
   points.append(row)
   roundPoints = roundPoints[numPlayers:]
totalPoints = calculatePoints(numPlayers, numRounds, points)
findWinner(numPlayers, numRounds, totalPoints)