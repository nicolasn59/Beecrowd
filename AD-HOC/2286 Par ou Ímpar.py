# RECEBER NUM DE PARTIDAS
# NOME DOS DOIS JOGADORES  (MÁXIMO DE DEZ LETRAS E SEM ESPAÇOS EM BRANCO)
# A SEGUINTES LINHAS SERAO O NUM DE DEDOS DE CADA JOGADOR
# O PRIMEIRO JOGADOR SEMPRE ESCOLHE PAR
# FINALIZAR: N = 0

cont = 1
while True:
    lista = []
    n = int(input())

    if n == 0:
        break

    j1 = input().strip()
    j2 = input().strip()

    for i in range(n):
        a, b = map(int, input().split())
        lista.append(j1 if (a + b) % 2 == 0 else j2)

    print(f'Teste {cont}')
    for nome in lista:
        print(nome)
    print()
    cont += 1
