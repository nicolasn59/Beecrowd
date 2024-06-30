# SUBPROGRAMA
def decodificarTexto(numTestes):
    while numTestes != 0:
        decoder = list()
        codigo = input()
        deslocamento = int(input())
        cont = 0
        for letra in codigo:
            if (ord(letra) - deslocamento) < 65:
                novaLetra = 91 - (65 - (ord(letra) - deslocamento))
                decoder += [chr(novaLetra)]
            else:
                decoder += [(chr(ord(letra) - deslocamento))]
            cont += 1
        numTestes -= 1
        print(''.join(decoder))
    return None

# PRINCIPAL
numeroDeTeste = int(input())
decodificarTexto(numeroDeTeste)
