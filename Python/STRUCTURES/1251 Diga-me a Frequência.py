# SUBPROGRAMA
def contarFrequencia(lisCaracteres, filtro, contagem, cont):
    if lisCaracteres == [0]:
        return contagem
    else:
        for i in range(len(lisCaracteres)):
            if lisCaracteres[i] == filtro[cont]:
                contagem[cont] += 1
            else:
                lisCaracteres = lisCaracteres[i:]
                return contarFrequencia(lisCaracteres, filtro, contagem, cont+1)

def imprimirFrequencia(filtro, contagem):
    indice = 0
    menor = contagem[0]
    if len(contagem) == 1:
        print(filtro[indice], menor)
        return None
    else:
        for i in range(1, len(contagem)):
            if menor > contagem[i]:
                menor = contagem[i]
                indice = i
        print(filtro[indice], menor)
        filtro.pop(indice)
        contagem.remove(menor)
        return imprimirFrequencia(filtro, contagem)

# PROGRAMA PRINCIPAL
parar = False
entradas = 0
while parar != True:
    try:
        contador = 0
        linhaDeTexto = input()

    except EOFError:
        parar = True
    else:
        if entradas != 0:
            print()
        listaDeCaracteres = [ord(caracter) for caracter in linhaDeTexto]
        listaDeCaracteres += [0]
        listaDeCaracteres = sorted(listaDeCaracteres, reverse=True)
        filtroDeCaracteres = sorted((list(set(listaDeCaracteres))), reverse=True)
        contagemDaFrequencia = [0] * len(filtroDeCaracteres)
        contagemDaFrequencia = contarFrequencia(listaDeCaracteres, filtroDeCaracteres, contagemDaFrequencia, contador)
        contagemDaFrequencia, filtroDeCaracteres = contagemDaFrequencia[:-1], filtroDeCaracteres[:-1]
        imprimirFrequencia(filtroDeCaracteres, contagemDaFrequencia)
        entradas += 1
