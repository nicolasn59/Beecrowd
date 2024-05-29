
# Subprograma
def contador_casas(i, f):
    numeros = []
    cont = 0
    while True:
        inicio_string = str(i)
        for digito in inicio_string:
            if digito in numeros:
                break
            else:
                numeros.append(digito)
        if len(numeros) == len(inicio_string):
            cont += 1
        if i == f:
            break
        i += 1
        numeros.clear()

    return cont


# Programa Princípal
while True:
    try:
        n, m = map(int, input().split())   #N = VALOR INICIAL, M = VALOR FINAL
        print(contador_casas(n, m))
    except EOFError:
        break
