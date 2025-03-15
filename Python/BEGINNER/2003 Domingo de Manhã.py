# SUBPROGRAMA
# PROGRAMA PRINCIPAL
while True:
    try:
        array = list(input().split())
        horas = int(array[0][0])
        minutos = int((array[0][2] + array[0][3]))
        minutos = int(minutos)
        if ((horas <= 7) and (minutos == 0)) or (horas < 7):
            print("Atraso maximo: 0")
        else:
            if horas == 9:
                print("Atraso maximo: %d" % (60*2))
            elif horas == 8:
                print("Atraso maximo: %d" % (60+minutos))
            else:
                print("Atraso maximo: %d" % minutos)
    except EOFError:
        break
