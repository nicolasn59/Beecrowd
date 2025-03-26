# SUBPROGRAM
def printOrder(cards):
    increasing = decreasing = 0
    for i in range(1, len(cards)):
        if cards[i-1] < cards[i]:
            increasing += 1
        elif cards[i-1] > cards[i]:
            decreasing += 1
    if increasing == len(cards)-1:
        print('C')
    elif decreasing == len(cards)-1:
        print('D')
    else:
        print('N')
    return None

# MAIN PROGRAM
cards = list(map(int, input().split()))
printOrder(cards)