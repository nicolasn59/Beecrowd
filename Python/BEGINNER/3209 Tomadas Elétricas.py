#SUBPROGRAMA
def aparelhosConectados(filtros):
    total = 0
    for j in range(1, filtros[0]+1):
        total += (filtros[j]-1)
    print("%d" % (total+1))
    return None


#PRINCIPAL
numTestes = int(input())
for i in range(numTestes):
    filtroDeLinha = list(map(int, input().split()))
    aparelhosConectados(filtroDeLinha)
