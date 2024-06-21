# SUBPROGRAMA
def imprimirOrdem(cards):
    crescente = decrescente = 0
    for i in range(1, len(cards)):
        if cards[i-1] < cards[i]:
            crescente += 1
        elif cards[i-1] > cards[i]:
            decrescente += 1
    if crescente == len(cards)-1:
        print('C')
    elif decrescente == len(cards)-1:
        print('D')
    else:
        print('N')
    return None

# PROGRAMA PRINCIPAL
cartas = list(map(int, input().split()))
imprimirOrdem(cartas)
