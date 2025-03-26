# SUBPROGRAM
def gameWinner(participants, rounds):
    participantOrder = list(map(int, input().split()))
    for _ in range(rounds):
        info = list(map(int, input().split()))
        for i in range(2, len(info)):
            if info[i] != info[1]:
                info[i] = 2

        winner = list()
        for i in range(2, len(info)):
            if info[i] != 2:
                winner.append(participantOrder[i-2])
        participantOrder = winner

    msg = 'Teste %d\n%d' % (roundCounter, winner[0])
    return msg

# MAIN PROGRAM
roundCounter = 1
numParticipants, numRounds = map(int, input().split())
while numParticipants != 0 and numRounds != 0:
    winner = gameWinner(numParticipants, numRounds)
    print(winner)
    print()
    roundCounter += 1
    numParticipants, numRounds = map(int, input().split())