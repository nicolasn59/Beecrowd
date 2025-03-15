def ordenarTamanho(palavras):
    listaOrdenadaDeStrings = list()
    tamanhoDasPalavras = [len(palavra) for palavra in palavras]

    while len(tamanhoDasPalavras) >= 1:
        maior = pos = 0
        for indice, tamanho in enumerate(tamanhoDasPalavras):
            if maior == 0:
                maior = tamanho
                pos = indice
            elif tamanho > maior:
                maior = tamanho
                pos = indice
        listaOrdenadaDeStrings.append(palavras[pos])
        tamanhoDasPalavras.pop(pos)
        palavras.pop(pos)

    return ' '.join(listaOrdenadaDeStrings)


testes = int(input())
for i in range(testes):
    frase = list(map(str, input().split()))
    tamanhoOrdenado = ordenarTamanho(frase)
    print(tamanhoOrdenado)
