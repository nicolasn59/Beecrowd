def contadorDeLeds(numeros):
    leds = 0
    for numero in numeros:
        if numero == '1':
            leds += 2
        elif numero == '2' or numero == '3' or numero == '5':
            leds += 5
        elif numero == '4':
            leds += 4
        elif numero == '7':
            leds += 3
        elif numero == '8':
            leds += 7
        else:
            leds += 6
    return leds


numeroDeTestes = int(input())
for i in range(numeroDeTestes):
    valor = str(input())
    qtdDeLeds = contadorDeLeds(valor)
    print('%.f leds' % qtdDeLeds)
