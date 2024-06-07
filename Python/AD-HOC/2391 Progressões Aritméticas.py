# SUBPROGRAMA
def quebrarSequencia(sequencia):
    listaDePas = list()
    pa = list()
    diferenca = 0
    for num in range(1, len(sequencia)):
        if pa == []:
            diferenca = sequencia[num - 1] - sequencia[num]
            pa += [sequencia[num - 1]]
        else:
            if sequencia[num - 1] - sequencia[num] == diferenca:
                pa += [sequencia[num - 1]]
            else:
                pa += [sequencia[num - 1]]
                listaDePas += [pa]
                pa = list()
                diferenca = 0
    if len(pa) == 1:
        listaDePas += [pa]
    print(len(listaDePas))
    return None

# PROGRAMA PRINCIPAL
numerosDeElementos = int(input())
valoresDaSequencia = list(map(int, input().split()))
valoresDaSequencia += [float('inf')]
quebrarSequencia(valoresDaSequencia)
