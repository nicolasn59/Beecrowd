# SUBPROGRAMA
def calcularPontos(jogadores, rodadas, pontos):
    somaPontos = [0] * jogadores
    for lin in range(rodadas):
        for col in range(jogadores):
            somaPontos[col] += pontos[lin][col]
    return somaPontos

def acharVencedor(jogadores, rodadas, somaPontos):
    maior = somaPontos[0]
    jogador = 1
    for ponto in range(1, jogadores):
        if somaPontos[ponto] >= maior:
            maior = somaPontos[ponto]
            jogador = ponto + 1
    print(jogador)
    return None

# PROGRAMA PRINCIPAL
pontuacao = list()
numeroDeJogadores, numeroDeRodadas = map(int, input().split())
pontosDaRodada = list(map(int, input().split()))
for i in range(numeroDeRodadas):
   linha = list()
   for j in range(numeroDeJogadores):
       linha.append(pontosDaRodada[j])
   pontuacao.append(linha)
   pontosDaRodada = pontosDaRodada[numeroDeJogadores:]
somaDosPontos = calcularPontos(numeroDeJogadores, numeroDeRodadas, pontuacao)
acharVencedor(numeroDeJogadores, numeroDeRodadas, somaDosPontos)
