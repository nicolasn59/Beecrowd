posicao = int(input())
termoAnterior = 0
termoAtual = 1
for termo in range(posicao):
    if termo == 0:
        print(termoAnterior, end=' ')
    elif termo == 1:
        print(termoAtual, end=' ')
    elif termo < (posicao - 1):
        termoResultado = termoAnterior + termoAtual
        termoAnterior = termoAtual
        termoAtual = termoResultado
        print(termoResultado, end=' ')
    else:
        termoResultado = termoAnterior + termoAtual
        termoAnterior = termoAtual
        termoAtual = termoResultado
        print(termoResultado)
