# algoritmo
# ENTRADA COM VARIOS TESTES
# RECEBER QUANTIDADE DE MOEDAS
# RECEBER VALORES DA N MOEDAS
# RECEBER NUMERO DE SALTO
# PASSO A PASSO
# PASSO 1: SOMAR TODAS AS MOEDAS DE ACORDO COM O SALTO
# PASSO 2: VERIFICAR SE É PRIMO (CASO SEJA DIVISIVEL POR MAIS DE 2 NUMEROS NÃO É PRIMO)
# SE FOR PRIMO IMPRIMIR "Bad boy! I’ll hit you."
# SE NÃO “You’re a coastal aircraft, Robbie, a large silver aircraft.”
# ENTRADA TERMINA COM EOF

#SUBPROGRAMA

#PROGRAMA PRINCIPAL
while True:
    try:
        lista_moedas = []
        soma_moedas = cont = 0

        moedas = int(input())
        for _ in range(moedas):
            lista_moedas.append(int(input()))

        salto = int(input())
        for i in range(moedas-1, -1, -salto):
            soma_moedas += lista_moedas[i]

        for numero in range(1, soma_moedas + 1):
            if soma_moedas % numero == 0:
                cont += 1

        if cont == 2:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError:
        break
