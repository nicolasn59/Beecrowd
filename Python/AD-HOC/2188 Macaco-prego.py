# SUBPROGRAMA
def gerarRegioes(numTestes):
    regioes = list()
    maxX = minY = minU = maxV = 0
    for _ in range(numTestes):
        regiao = list(map(int, input().split()))
        regioes.append(regiao)
        if len(regioes) == 1:
            maxX, minY, minU, maxV = regiao[0], regiao[1], regiao[2], regiao[3]
        else:
            if regiao[0] > maxX:
                maxX = regiao[0]
            if regiao[1] < minY:
                minY = regiao[1]
            if regiao[2] < minU:
                minU = regiao[2]
            if regiao[3] > maxV:
                maxV = regiao[3]
    return maxX, minY, minU, maxV

def verificarIntercepcao(maxX, minY, minU, maxV, cont):
    print("Teste %d" % cont)
    if maxX >= minU:
        print("nenhum")
        print()
    elif minY <= maxV:
        print('nenhum')
        print()
    else:
        print("%d %d %d %d" % (maxX, minY, minU, maxV))
        print()
    return None

# PROGRAMA PRINCIPAL
contador = 1
numeroDeTestes = int(input())
while numeroDeTestes != 0:
    maiorX, menorY, menorU, maiorV = gerarRegioes(numeroDeTestes)
    verificarIntercepcao(maiorX, menorY, menorU, maiorV, contador)
    numeroDeTestes = int(input())
    contador += 1
