# SUBPROGRAMA
def distanciaMaxima(numP, numA):
    maiorDistancia = numA[0] - 1
    inicio = 1
    for i in range(numP):
        for j in range(inicio, len(numA)):
            if (((numA[i] + numA[j])-2) + abs(i - j)) > maiorDistancia:
                maiorDistancia = ((numA[i] + numA[j])) + abs(i - j)
        inicio += 1
    print(maiorDistancia)
    return None

# PRINCIPAL
numeroDePredios = int(input())
numeroDeAndares = list(map(int, input().split()))
# numeroDeAndares = [andar + 1 for andar in numeroDeAndares]
distanciaMaxima(numeroDePredios, numeroDeAndares)
