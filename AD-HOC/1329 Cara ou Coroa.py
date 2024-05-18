numero_teste = int(input())

while numero_teste != 0:
    jogadas = list(map(int, input().split()))
    joao = maria = 0

    for valor in jogadas:
        if valor == 0:
            maria += 1
        else:
            joao += 1

    print('Mary won %d times and John won %d times' % (maria, joao))
    numero_teste = int(input())
