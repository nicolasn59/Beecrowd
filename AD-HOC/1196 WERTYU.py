frase_decodificada = []

teclado = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', "\\",
'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    try:
        frase = str(input()).upper()

    except EOFError:
        break

    else:
        lista = [caractere for caractere in frase]

        for indice, caractere in enumerate(lista):

            if caractere in teclado:
                i = teclado.index(caractere)
                frase_decodificada.append(teclado[i - 1] if i > 0 else caractere)
            else:
                frase_decodificada.append(' ')

        print(''.join(frase_decodificada))
        frase_decodificada.clear()
