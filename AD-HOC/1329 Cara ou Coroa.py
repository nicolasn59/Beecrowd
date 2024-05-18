# algoritmo
# ESCREVER UM PROGRAMA INFORMANDO QUANTIDADE DE VITORIAS DE CADA UM
# RECEBER NUMERO DE TESTES EM INTEIRO
# RECEBER VALORES: 0 ou 1
# SE O VALOR FOR IGUAL A 0 É 1 VITORIA PARA MARIA, CASO CONTRÁRIO É PARA O JOAO
# APÓS CADA TESTE IMPRIMIR A SAIDA SÁIDA COM A MENSAGEM: Mary won "X" times and John won "Y" times
# O PROGRAMA FINALIZA COM O NUMERO DE TESTE IGUAL A 0

# SUBPROGRAMA
#PROGRAMA PRINCIPAL

numero_teste = int(input())

while numero_teste != 0:
    jogadas = list(map(int, input().split()))
    joao = maria = 0

    for valor in jogadas:
        if valor == 0:
            maria += 1
        else:
            joao += 1

    print('Mary won %d times and John won %d times' % (maria, joao))
    numero_teste = int(input())
