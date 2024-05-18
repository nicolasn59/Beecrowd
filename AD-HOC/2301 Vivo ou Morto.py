# ENTRADA COM VARIOS CASOS DE TESTES
# RECEBER QUANTIDADE DE PARTICUPANTE E QUANTIDADE DE RODADAS DA PARTIDA
# RECEBER EM UMA LISTA A ORDEM DOS PARTICIPANTES
# RECEBER NUMERO DE PARTICIPANTE DA RODADA, ORDEM DADA PELO CHEFE, E ACÃO DOS PARTICIPANTES
# SE ORDEM FOR 1, É VIVO, SE NÃO, É MORTO
# A ENTRADA TERMINA COM QTD DE PARTICIPANTES E QTD DE RODADAS = 0
# PASSO A PASSO:
# PASSO 1: INICIAR UM LOOP FOR COM UMA CONTAGEM DE QTD DE RODADAS
# PASSO 2: RECEBER INFORMAÇÕES DE QTD DE PARTICIPANTES, ORDEM DO CHEFE, AÇÕES
# PASSO 3: ELIMINAR DA LISTA QUEM NÃO FEZ AÇÃO CORRETA
# PASSO 4: IMPRIMIR VENCEDOR DA RODADA COM MSG DO ENUNCIADO
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
