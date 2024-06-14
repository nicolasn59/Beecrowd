# SUBPROGRAMA
def verificarSobrenome(sobNome):
    cont = 0
    for letra in sobNome:
        if letra not in "aeiou":
            cont += 1
        else:
            cont = 0
        if cont == 3:
            print("%s nao eh facil" % (sobNome[0].upper() + sobNome[1:]))
            return None
    print("%s eh facil" % (sobNome[0].upper() + sobNome[1:]))
    return None


# PRINCIPAL
testes = int(input())
for teste in range(testes):
    sobrenome = input().lower()
    verificarSobrenome(sobrenome)
