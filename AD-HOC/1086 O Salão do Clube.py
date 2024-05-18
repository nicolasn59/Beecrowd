# RECEBER DIMENSÃO DA SALA M x N
# RECEBER LARGURA DA TABUA EM CM
# RECEBER QUANTIDADE DE TABUAS DOADAS
# RECEBER COMPRIMENTO DE CADA TABUA EM METROS
# FINALIZAR SE M E N == 0

# PEGAR O AREA DO SALAO EM M²
# PEGAR A AREA DAS TABUAS ATÉ CHEGAR NA AREA DO SALAO
# FAZER A CONTAGEM DE QUANTAS DA TABUA VÃO SER USADAS


while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    largura = int(input())
    doacao = int(input())

    comprimento = list(map(int, input().split()))
    comprimento = sorted(comprimento, reverse=True)
    print(comprimento)
    area_salao = m * n
    area_tabua = cont = 0

    for valor in comprimento:
        area_tabua += valor * (largura / 100)
        cont += 1
        if area_tabua >= area_salao:
            print(cont)
            break

    if area_tabua < area_salao:
        print('impossivel')
