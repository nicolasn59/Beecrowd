# SUBPROGRAM
def decodeText(numTests):
    while numTests != 0:
        decoder = list()
        code = input()
        shift = int(input())
        count = 0
        for letter in code:
            if (ord(letter) - shift) < 65:
                newLetter = 91 - (65 - (ord(letter) - shift))
                decoder += [chr(newLetter)]
            else:
                decoder += [(chr(ord(letter) - shift))]
            count += 1
        numTests -= 1
        print(''.join(decoder))
    return None

# MAIN
numTests = int(input())
decodeText(numTests)