# SUBPROGRAMA
def criptografia():
    frase = input()
    frase = [ord(caractere) for caractere in frase]
    frase = [(valor + 3) if chr(valor).isalpha() else valor for valor in frase]
    frase.reverse()
    frase = [(valor-1) if indice >= (len(frase)//2) else valor for indice, valor in enumerate(frase)]
    frase = [chr(numero) for numero in frase]
    frase = ''.join(frase)
    return frase


# PRINCIPAL
qtdDeFrases = int(input())
for i in range(qtdDeFrases):
    fraseCriptografada = criptografia()
    print(fraseCriptografada)
