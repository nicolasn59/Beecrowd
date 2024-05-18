caso = 1
while True:
    try:
        sequencia = []
        contarSequencia = 0
        tamanhoDaSequencia = int(input())

        while True:
            if contarSequencia >= tamanhoDaSequencia and tamanhoDaSequencia != 0:
                break
            while contarSequencia < tamanhoDaSequencia:
                sequencia.append(tamanhoDaSequencia)
                contarSequencia += 1
            tamanhoDaSequencia -= 1
            contarSequencia = 0

        sequencia.append(0)
        sequenciaOrdenada = sorted(sequencia)
        sequenciaString = (str(numero) for numero in sequenciaOrdenada)
        sequenciaString = ' '.join(sequenciaString)

    except EOFError:
        break
    else:
        if len(sequenciaOrdenada) <= 2:
            print('Caso %d: %d numero' % (caso, len(sequenciaOrdenada)))
        else:
            print('Caso %d: %d numeros' % (caso, len(sequenciaOrdenada)))
        print(sequenciaString)
        caso += 1
        print()
