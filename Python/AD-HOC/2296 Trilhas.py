def calculo_esforco(altitude):
    esforco = 0
    for i in range(1, len(altitude)):
        desnivel = altitude[i] - altitude[i -1]
        if desnivel > 0:
            esforco += desnivel
    return esforco


def encontrar_trilha_facil(trilhas):
    menor_esforco = float('inf')
    melhor_trilha = -1

    for indice, altitude in enumerate(trilhas):
        esforco = min(calculo_esforco(altitude), calculo_esforco(altitude[::-1]))
        if esforco < menor_esforco:
            menor_esforco = esforco
            melhor_trilha = indice + 1
    return melhor_trilha


num_testes = int(input())
trilhas = []
for _ in range(num_testes):
    altitudes = list(map(int, input().split()))[1:]
    trilhas.append(altitudes)

print(encontrar_trilha_facil(trilhas))
