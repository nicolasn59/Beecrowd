#algoritmo

# VARIOS CASOS DE TESTE: RECEBER NUMERO DE QUESTÕES ANTES DO LOOP E AO FINAL DO LOOP
# INICIAR UM LOOP "FOR" PARA RECEBER AS ENTRADAS DAS MÉDIAS
# RECEBER 5 VALORES INTEIROS CORRESPONDENTE À MEDIA DAS CORES
# DETERMINAR QUAL É A RESPOSTA CORRETA DE ACORDO COM AS REGRAS:
# 1- SERÁ CONSIDERA RESPOSTA MARCADA APENAS NA SEGUINTE OCASIÃO: MÉDIA 0, MÉDIA MENOR OU IGUAL À 127
# 2- EM CASO DE MÉDIA 255 OU ACIMA DE 127 É CONSIDERADO RESPOSTA EM BRANCO
# 3- SE MARCA MAIS DE UMA RESPOSTA OU NENHUMA A QUESTÃO É DESCONSIDERADA
# IMPRIMIR SAÍDA A CADA LINHA DE MÉDIA RECEBIDA
# A SÁIDA DEVE CONTER A RESPOSTA MARCADA: A,B,C,D ou E.
# CASO TENHA MARCADO MAIS DE UMA RESPOSTA OU NENHUM, IMPRIMI UM "*"
# PROGRAMA ENCERRA COM NUMERO DE QUESTÕES IGUAL A 0.

#subprograma
#programa principal

numero_questoes = int(input())
while numero_questoes != 0:
    cont = 0

    for _ in range(numero_questoes):
        medias = list(map(int, input().split()))

        for indice in range(len(medias)):

            if medias[indice] == 0 or medias[indice] <= 127:
                resposta = indice
                cont += 1

        if cont > 1 or cont == 0:
            print('*')
            cont = 0
        else:
            if resposta == 0:
                print('A')
            elif resposta == 1:
                print('B')
            elif resposta == 2:
                print('C')
            elif resposta == 3:
                print('D')
            else:
                print('E')

            cont = 0

    numero_questoes = int(input())
