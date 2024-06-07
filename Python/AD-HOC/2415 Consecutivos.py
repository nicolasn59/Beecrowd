# SUBPROGRAMA
# PROGRAMA PRINCIPAL
cont = 0
maior = 0
numSorteios = int(input())
valores = list(map(int, input().split()))
valores += [0]
for num in range(1, len(valores)):
    if valores[num - 1] == valores[num]:
        cont += 1
    else:
        if cont > maior:
            maior = cont
        cont = 0
print(maior + 1)
