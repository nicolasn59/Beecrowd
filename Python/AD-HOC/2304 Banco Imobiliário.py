dinheiro, turnos = map(int, input().split())
D = E = F = dinheiro
for elon_musk in range(turnos):
    capital = list(map(str, input().split()))
    capital[-1] = int(capital[-1])

    if capital[0] == 'C':
        if capital[1] == 'D':
            D -= capital[-1]
        elif capital[1] == 'E':
            E -= capital[-1]
        else:
            F -= capital[-1]

    elif capital[0] == 'V':
        if capital[1] == 'D':
            D += capital[-1]
        elif capital[1] == 'E':
            E += capital[-1]
        else:
            F += capital[-1]

    else: #capital[0] == A
        if capital[1] == 'D' and capital[2] == 'E':
            D += capital[-1]
            E -= capital[-1]
        elif capital[1] == 'D' and capital[2] == 'F':
            D += capital[-1]
            F -= capital[-1]
        elif capital[1] == 'E' and capital[2] == 'D':
            E += capital[-1]
            D -= capital[-1]
        elif capital[1] == 'E' and capital[2] == 'F':
            E += capital[-1]
            F -= capital[-1]
        elif capital[1] == 'F' and capital[2] == 'D':
            F += capital[-1]
            D -= capital[-1]
        else:
            F += capital[-1]
            E -= capital[-1]

print(D, E, F)
