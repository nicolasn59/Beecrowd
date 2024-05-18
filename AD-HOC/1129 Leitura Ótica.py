numero_questoes = int(input())
while numero_questoes != 0:
    cont = 0

    for _ in range(numero_questoes):
        medias = list(map(int, input().split()))

        for indice in range(len(medias)):

            if medias[indice] == 0 or medias[indice] <= 127:
                resposta = indice
                cont += 1

        if cont > 1 or cont == 0:
            print('*')
            cont = 0
        else:
            if resposta == 0:
                print('A')
            elif resposta == 1:
                print('B')
            elif resposta == 2:
                print('C')
            elif resposta == 3:
                print('D')
            else:
                print('E')

            cont = 0

    numero_questoes = int(input())
