#SUBPROGRAMA
def calcularCedulas(val):
    cinquenta = dez = cinco = um = 0
    while val != 0:
        if (val - 50) >= 0:
            val -= 50
            cinquenta += 1
        elif (val - 10) >= 0:
            val -= 10
            dez += 1
        elif (val - 5) >= 0:
            val -= 5
            cinco += 1
        else:
            val -= 1
            um += 1
    return cinquenta, dez, cinco, um


#PRINCIPAL
numeroDoTeste = 1
valor = int(input())
while valor != 0:
    cedulasUsadas = calcularCedulas(valor)
    print('Teste %d' % numeroDoTeste)
    print(cedulasUsadas[0], cedulasUsadas[1], cedulasUsadas[2], cedulasUsadas[3])
    print()
    valor = int(input())
    numeroDoTeste += 1
