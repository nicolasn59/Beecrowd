menor = 0
dias, saldo_inicial = map(int, input().split())
for _ in range(dias):
    saldo = int(input())
    saldo_inicial += saldo

    if menor == 0:
        menor = saldo_inicial
    else:
        if saldo_inicial < menor:
            menor = saldo_inicial
print(menor)
