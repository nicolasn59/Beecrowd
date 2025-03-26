# SUBPROGRAM
def bestCard(card1, card2):
    if card1 > card2:
        return card1
    else:
        return card2

# MAIN
card1, card2 = map(int, input().split())
winningCard = bestCard(card1, card2)
print(winningCard)
