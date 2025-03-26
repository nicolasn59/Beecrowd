def countLeds(numbers):
    leds = 0
    for number in numbers:
        if number == '1':
            leds += 2
        elif number == '2' or number == '3' or number == '5':
            leds += 5
        elif number == '4':
            leds += 4
        elif number == '7':
            leds += 3
        elif number == '8':
            leds += 7
        else:
            leds += 6
    return leds


numTests = int(input())
for i in range(numTests):
    value = str(input())
    numLeds = countLeds(value)
    print('%.f leds' % numLeds)