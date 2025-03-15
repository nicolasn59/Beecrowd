A1 = int(input())
A2 = int(input())
A3 = int(input())

cafeNoPrimeiroAndar = ((A2*2) + (A3*4))
cafeNoSegundoAndar = ((A1*2)+(A3*2))
cafeNoTerceiroAndar = ((A1*4)+(A2*2))

menorTempo = cafeNoPrimeiroAndar
if cafeNoSegundoAndar < menorTempo:
    menorTempo = cafeNoSegundoAndar
if cafeNoTerceiroAndar < menorTempo:
    menorTempo = cafeNoTerceiroAndar
print(menorTempo)
