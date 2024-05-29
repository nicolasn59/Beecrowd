# SUBPROGRAMA
def receberAssociacoes(numAssociacoes):
    listaDeAssociacoes = list()
    for _ in range(numAssociacoes):
        linhaDeAssociacao = input().split()
        listaDeAssociacoes.append(linhaDeAssociacao)
    return listaDeAssociacoes

def separarAssociacoes(listaDeAssociacoes, numAssociacoes):
    senhaCod = list()
    digitos = list()
    linha = 0
    for i in range(numAssociacoes):
        senhaCod.append(listaDeAssociacoes[i][-6:])
        digitos.append([int(listaDeAssociacoes[i][num]) for num in range(10)])
    return digitos, senhaCod

def separarDigitosEmPares(digitos):
    digitosSeparados = list()
    cont = 0
    for lin in digitos:
        linha = list()
        for col in lin:
            pares = list()
            pares += [digitos[cont][:2]]
            linha += pares
            del digitos[cont][:2]
        linha.append(digitos[cont])
        digitosSeparados.append(linha)
        cont += 1
    digitos = digitosSeparados
    return digitos

def posicoesDosCaracteres(senhaCod):
    for lin in range(len(senhaCod)):
        for col in range(len(senhaCod[lin])):
            if senhaCod[lin][col] == 'A':
                senhaCod[lin][col] = 0
            elif senhaCod[lin][col] == 'B':
                senhaCod[lin][col] = 1
            elif senhaCod[lin][col] == 'C':
                senhaCod[lin][col] = 2
            elif senhaCod[lin][col] == 'D':
                senhaCod[lin][col] = 3
            else:
                senhaCod[lin][col] = 4
    return senhaCod

def decodificarSenha(digitos, senhaCod, numTeste):
    senhaDecodificada = list()
    for col in range(len(senhaCod[0])):
        interseccao = list()
        for lin in range(len(digitos)):
            if interseccao == []:
                interseccao = digitos[lin][senhaCod[lin][col]]
            else:
                interseccao = set(interseccao).intersection(digitos[lin][senhaCod[lin][col]])
        senhaDecodificada.append(list(interseccao))
    print('Teste %d' % numTeste)
    for lin in range(len(senhaDecodificada)):
        for col in range(len(senhaDecodificada[lin])):
            print(senhaDecodificada[lin][col], end=' ')
    print()
    print()
    return None

# PROGRAMA PRINCIPAL
numeroDeAssociacoes = int(input())
numeroDeTeste = 1
while numeroDeAssociacoes != 0:
    associacoes = receberAssociacoes(numeroDeAssociacoes)
    digitosDeAssociacoes, senhaCodificadas = separarAssociacoes(associacoes, numeroDeAssociacoes)
    digitosDeAssociacoes = separarDigitosEmPares(digitosDeAssociacoes)
    senhaCodificadas = posicoesDosCaracteres(senhaCodificadas)
    decodificarSenha(digitosDeAssociacoes, senhaCodificadas, numeroDeTeste)
    numeroDeAssociacoes = int(input())
    numeroDeTeste += 1
