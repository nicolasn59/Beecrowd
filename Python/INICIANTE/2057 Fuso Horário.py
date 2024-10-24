#SUBPROGRAMA
def calcularTempoDeChegada(s, t, f):
    if (s+t+f) >= 24:
        print("%d" % ((s+t+f) - 24))
    elif (s+t+f) < 0:
        print("%d" % ((s+t+f) + 24))
    else:
        print("%d" % (s+t+f))
    return None

#PROGRAMA PRINCIPAL
saida, tempoViagem, fusoHorario = map(int, input().split())
calcularTempoDeChegada(saida, tempoViagem, fusoHorario)
