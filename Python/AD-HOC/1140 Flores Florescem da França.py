# SUBPROGRAMA
def verificarTautograma(letras):
    filtroDeLetras = []
    for posicao in range(len(letras)):
        if letras[posicao][0].lower() == letras[0][0].lower():
            filtroDeLetras.append('Y')
        else:
            filtroDeLetras.append('N')
    if 'N' in filtroDeLetras:
        return 'N'
    else:
        return 'Y'


# PROGRAMA PRINCIPAL
frase = list(map(str, input().split()))
while frase[0][0] != '*':
    resultado = verificarTautograma(frase)
    print(resultado)
    frase = list(map(str, input().split()))
