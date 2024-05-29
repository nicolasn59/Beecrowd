# SUBPROGRAMA
def calcularPedrasMovidas(qtdPilhas, cuboPedras):
    somaDosCubos = somaDasPosicoes = pedrasMovidas = contarDiferenca = 0
    escada = list()

    #VERIFICANDO SE AS PILHAS DE PEDRAS POSSUEM A MESMA QUANTIDADE DE PEDRAS
    cont = 1
    while cont != qtdPilhas:
        contarDiferenca += cuboPedras[cont-1] - cuboPedras[cont]
        cont += 1
    if contarDiferenca == 0:
        print(-1)
        return None
    ####

    cont = 0
    while cont != qtdPilhas:
        somaDosCubos += cuboPedras[cont]
        cont += 1
    cont = 0
    while cont != qtdPilhas:
        somaDasPosicoes += cont
        cont += 1

    #QUANTIDADE DE PEDRAS QUE TERÃO NA PRIMEIRA PILHA DA ESCADA
    inicioDaEscada = (somaDosCubos - somaDasPosicoes) // qtdPilhas

    #VERIFICANDO SE É POSSÍVEL FAZER UMA ESCADA PERFEITA
    if (somaDosCubos - somaDasPosicoes) % qtdPilhas == 0:
        cont = 0
        while cont != qtdPilhas:
            escada.append(inicioDaEscada + cont)
            cont += 1
        cont = 0
        while cont != qtdPilhas:
            diferenca = cuboPedras[cont] - escada[cont]
            if diferenca >= 0:
                pedrasMovidas += diferenca
            cont += 1
        print(pedrasMovidas)
    else:
        print(-1)
    return None

# PROGRAMA PRINCIPAL
quantidadeDePilhas = int(input())
cubosDePedras = list(map(int, input().split()))
calcularPedrasMovidas(quantidadeDePilhas, cubosDePedras)
