# SUBPROGRAMA
def trocaMaxima(numCartasA, numCartasB, cartasA, cartasB):
    if len(cartasA.difference(cartasB)) < len(cartasB.difference(cartasA)):
        print(len(cartasA.difference(cartasB)))
    else:
        print(len(cartasB.difference(cartasA)))
    return None

# PRINCIPAL
numeroDeCartasDeAlice, numeroDeCartasDeBeatriz = map(int, input().split())
while numeroDeCartasDeAlice != 0 and numeroDeCartasDeBeatriz != 0:
    cartasDeAlice = set(map(int, input().split()))
    cartasDeBeatriz = set(map(int, input().split()))
    trocaMaxima(numeroDeCartasDeAlice, numeroDeCartasDeBeatriz, cartasDeAlice, cartasDeBeatriz)
    numeroDeCartasDeAlice, numeroDeCartasDeBeatriz = map(int, input().split())
