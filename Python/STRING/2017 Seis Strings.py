# SUBPROGRAMA
def acharMenor(contagem):
    menor = contagem[0]
    indice = 0
    for i in range(1, len(contagem)):
        if contagem[i] < menor:
            menor = contagem[i]
            indice = i
    contagem.pop(indice)
    return contagem, indice, menor

def distanciaDeEdicao(palOriginal, num):
    contagem = [0] * 5
    diferenca = menor = 0
    for i in range(5):
        palavra = input()
        palavra = [letra for letra in palavra]
        if len(palavra) > len(palOriginal):
            palOriginal += ["."] * (len(palavra) - len(palOriginal))
            diferenca = (len(palavra) - len(palOriginal))
        else:
            if len(palavra) < len(palOriginal):
                palavra += ["."] * (len(palOriginal) - len(palavra))
                diferenca = (len(palOriginal) - len(palavra))
        for j in range(len(palavra)):
            if palOriginal[j] != palavra[j]:
                contagem[i] += 1
        contagem[i] += diferenca
    contagem, indice, menor = acharMenor(contagem)
    if menor < num:
        print(indice+1)
        print(menor)
    else:
        print(-1)
    return None

# PROGRAMA PRINCIPAL
palavraOriginal = input()
numero = int(input())
palavraOriginal = [letra for letra in palavraOriginal]
distanciaDeEdicao(palavraOriginal, numero)
