# SUBPROGRAMA
def vencedorDoJogo(participantes, rodadas):
    ordemDosParticipantes = list(map(int, input().split()))
    for _ in range(rodadas):
        informacoes = list(map(int, input().split()))
        for i in range(2, len(informacoes)):
            if informacoes[i] != informacoes[1]:
                informacoes[i] = 2

        vitorioso = list()
        for i in range(2, len(informacoes)):
            if informacoes[i] != 2:
                vitorioso.append(ordemDosParticipantes[i-2])
        ordemDosParticipantes = vitorioso

    msg = 'Teste %d\n%d' % (contadorDeRodadas, vitorioso[0])
    return msg

# PROGRAMA PRINCIPAL
contadorDeRodadas = 1
numeroDeParticipantes, numeroDeRodadas = map(int, input().split())
while numeroDeParticipantes != 0 and numeroDeRodadas != 0:
    vencedor = vencedorDoJogo(numeroDeParticipantes, numeroDeRodadas)
    print(vencedor)
    print()
    contadorDeRodadas += 1
    numeroDeParticipantes, numeroDeRodadas = map(int, input().split())
