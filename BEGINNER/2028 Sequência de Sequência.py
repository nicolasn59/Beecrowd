# algoritmo
# VARIOS CASOS DE TESTE
# PROGRAMA TERMINA COM EOF
# RECEBER O VALOR N DA SEQUENCIA
# O NUMERO 0 EQUIVALE A 1 NUMERO
# A SOMA DE TODOS OS NUMEROS RESULTA NO TOTAL DE NUMEROS DA SEQUENCIA (0 + 1 = 2 NUMEROS)
# PASSO - PASSO E REGRAS
# OBS: ADICIONAR OS NUMEROS DA SEQUENCIA EM UMA LISTA
# PASSO 1: INICIAR UM LOOP QUE VAI RECEBER N NUMEROS DA SEQUENCIA PARA FAZER UMA CONTAGEM
# PASSO 2: INICIAR OUTRO LOOP QUE VAI RECEBER A VARIAVEL DO LOOP ANTERIOR E FAZER UMA CONTAGEM DE X NUMEROS
# PASSO 3: NO SEGUNDO LOOP, ELE IRÁ ADICIONAR NA LISTA O NUMERO DE ACORDO COM O SEU VALOR. EX.: 3 = 3, 3, 3
# PASSO 4: FAZER UM CONTADOR PARA AMARZENAR A QUANTIDADE DE NUMEROS
# PASSO 5: IMPRIMIR A MENSAGEM FORMATADA E LOGO ABAIXO A SEQUENCIA DENTRO DA LISTA


# SUBPROGRAMA
# PROGRAMA PRINCIPAL
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
