#SUBPROGRAMA
def melhorCarta(ca1, ca2):
    if ca1 > ca2:
        return ca1
    else:
        return ca2

# PRINCIPAL
carta1, carta2 = map(int, input().split())
cartaDaVitoria = melhorCarta(carta1, carta2)
print(cartaDaVitoria)
