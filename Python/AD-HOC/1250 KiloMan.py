while True:
    try:
        numeroDeTestes = int(input())
        for caso in range(numeroDeTestes):
            atingido = 0
            listaDeAcao = []

            numeroDeTiros = int(input())
            alturaDoTiro = list(map(int, input().split()))
            acaoDoJogador = input()

            listaDeAcao = [caractere for caractere in acaoDoJogador]

            for posicao in range(numeroDeTiros):
                if alturaDoTiro[posicao] <= 2 and acaoDoJogador[posicao] == "S":
                    atingido += 1
                elif alturaDoTiro[posicao] > 2 and acaoDoJogador[posicao] == "J":
                    atingido += 1
                else:
                    continue
            print(atingido)

    except EOFError:
        break
