# SUBPROGRAMA
def potencia(bas, exp):
    potenciacao = bas ** exp   #base elevado o expoente
    potenciacao = str(potenciacao)
    return len(potenciacao)

# PRINCIPAL
numeroDeOperacoes = int(input())
while numeroDeOperacoes != 0:
    base, expoente = map(int, input().split())
    numeroDeDigitos = potencia(base, expoente)
    print(numeroDeDigitos)
    numeroDeOperacoes -= 1
