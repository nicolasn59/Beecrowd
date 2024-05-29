# SUBPROGRAMA
def calcularOperacao(ope, numMaior):
    ope[0] = int(ope[0])
    ope[2] = int(ope[2])
    if operacao[1] == "+":
        if (ope[0] + ope[2]) > numMaior:
            return "OVERFLOW"
        else:
            return "OK"
    else:
        if (ope[0] * ope[2]) > numMaior:
            return "OVERFLOW"
        else:
            return "OK"


# PRINCIPAL
maiorNumero = int(input())
operacao = input().split()
print(calcularOperacao(operacao, maiorNumero))
