# SUBPROGRAM
def maxExchange(numCardsA, numCardsB, cardsA, cardsB):
    if len(cardsA.difference(cardsB)) < len(cardsB.difference(cardsA)):
        print(len(cardsA.difference(cardsB)))
    else:
        print(len(cardsB.difference(cardsA)))
    return None

# MAIN
numAliceCards, numBeatrizCards = map(int, input().split())
while numAliceCards != 0 and numBeatrizCards != 0:
    aliceCards = set(map(int, input().split()))
    beatrizCards = set(map(int, input().split()))
    maxExchange(numAliceCards, numBeatrizCards, aliceCards, beatrizCards)
    numAliceCards, numBeatrizCards = map(int, input().split())