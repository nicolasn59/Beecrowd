# SUBPROGRAMA
def superPrimo(n):
    n = str(n)
    numeros = [int(num) for num in n]
    cont = 0
    for num in numeros:
        if primo(num) == "Primo":
            cont += 1
    if cont == len(numeros):
        return "Super"
    return "Primo"


def primo(n):
    if n <= 1:
        return "Nada"
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return "Nada"
    return "Primo"


# PROGRAMA PRINCIPAL
entrada = False
try:
    while entrada != True:
        numero = int(input())
        if primo(numero) == "Primo":
            print(superPrimo(numero))
        else:
            print("Nada")
except EOFError:
    entrada = True
