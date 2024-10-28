# SUBPROGRAMA
def contarPontos(rounds):
    j1 = j2 = 0
    while rounds != 0:
        n1, n2 = map(int, input().split())
        if n1 > n2:
            j1 += 1
        elif n2 > n1:
            j2 += 1
        rounds -= 1
    print(j1, j2)
    return None


# PROGRAMA PRINCIPAL
rodadas = int(input())
while rodadas != 0:
    contarPontos(rodadas)
    rodadas = int(input())
