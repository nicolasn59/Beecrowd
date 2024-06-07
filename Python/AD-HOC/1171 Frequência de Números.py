# SUBPROGRAMA
def receberEntradas(qtdVals):
    listaNums = list()
    filtroNums = list()
    for i in range(qtdVals):
        num = int(input())
        listaNums += [num]
        if num not in filtroNums:
            filtroNums += [num]
    filtroNums.sort()
    listaNums.sort()
    return listaNums, filtroNums

def contarNumeros(listaNums, filtroNums, qtdVals, cont, ind):
    listaNums += [0]
    filtroNums += [0]
    while True:
        j = 0
        while filtroNums[0] == listaNums[j]:
            if listaNums[j] == 0:
                return cont
            else:
                cont[ind] += 1
                j += 1
        listaNums = listaNums[j:]
        filtroNums = filtroNums[1:]
        ind += 1


# PROGRAMA PRINCIPAL
indice = 0
quantidadeDeValores = int(input())
listaDeNumeros, filtroDeNumeros = receberEntradas(quantidadeDeValores)
contagem = [0] * len(filtroDeNumeros)
contagemDosNumeros = contarNumeros(listaDeNumeros, filtroDeNumeros, quantidadeDeValores, contagem, indice)
filtroDeNumeros.remove(0)
listaDeNumeros.remove(0)
for i in range(len(filtroDeNumeros)):
    print("%s aparece %s vez(es)" % (filtroDeNumeros[i], contagem[i]))
