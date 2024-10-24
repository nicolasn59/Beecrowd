# SUBPROGRAMA
def loteria():
    soma = contarGritos = 0
    while contarGritos != 3:
        corvo = input()
        if corvo == "caw caw":
            print("%d" % soma)
            soma = 0
            contarGritos += 1
        elif corvo == "--*":
            soma += 1
        elif corvo == "-*-":
            soma += 2
        elif corvo == "-**":
            soma += 3
        elif corvo == "*--":
            soma += 4
        elif corvo == "*-*":
            soma += 5
        elif corvo == "**-":
            soma += 6
        else:
            soma += 7
    return None

# PROGRAMA PRINCIPAL
loteria()
