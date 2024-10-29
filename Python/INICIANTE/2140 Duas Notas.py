# SUBPROGRAMA
# PROGRAMA PRINCIPAL
valor, pagamento = map(int, input().split())
while ((valor != 0) or (pagamento != 0)):
    troco = pagamento - valor
    for i in range(2):
        if troco >= 100:
            troco -= 100
        elif troco >= 50:
            troco -= 50
        elif troco >= 20:
            troco -= 20
        elif troco >= 10:
            troco -= 10
        elif troco >= 5:
            troco -= 5
        elif troco >= 2:
            troco -= 2
        else:
            troco = -1
    if troco == 0:
        print("possible")
    else:
        print("impossible")
    valor, pagamento = map(int, input().split())
