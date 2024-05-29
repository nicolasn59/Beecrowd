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
