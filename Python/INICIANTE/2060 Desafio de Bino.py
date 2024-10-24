# SUBPROGRAMA
def verificarMultiplos(lis):
    multiplosDeDois = multiplosDeTres = multiplosDeQuatro = multiplosDeCinco = 0
    for num in lis:
        if (num % 2) == 0:
            multiplosDeDois += 1
        if (num % 3) == 0:
            multiplosDeTres += 1
        if (num % 4) == 0:
            multiplosDeQuatro += 1
        if (num % 5) == 0:
            multiplosDeCinco += 1
    print("%d Multiplo(s) de 2" % multiplosDeDois)
    print("%d Multiplo(s) de 3" % multiplosDeTres)
    print("%d Multiplo(s) de 4" % multiplosDeQuatro)
    print("%d Multiplo(s) de 5" % multiplosDeCinco)
    return None

# PROGRAMA PRINCIPAL
tamanhoDaLista = int(input())
lista = list(map(int, input().split()))
verificarMultiplos(lista)
