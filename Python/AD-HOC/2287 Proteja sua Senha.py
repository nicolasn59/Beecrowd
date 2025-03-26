# SUBPROGRAM
def receiveAssociations(numAssociations):
    associationList = list()
    for _ in range(numAssociations):
        associationLine = input().split()
        associationList.append(associationLine)
    return associationList

def separateAssociations(associationList, numAssociations):
    codedPassword = list()
    digits = list()
    line = 0
    for i in range(numAssociations):
        codedPassword.append(associationList[i][-6:])
        digits.append([int(associationList[i][num]) for num in range(10)])
    return digits, codedPassword

def separateDigitsIntoPairs(digits):
    separatedDigits = list()
    count = 0
    for row in digits:
        line = list()
        for col in row:
            pairs = list()
            pairs += [digits[count][:2]]
            line += pairs
            del digits[count][:2]
        line.append(digits[count])
        separatedDigits.append(line)
        count += 1
    digits = separatedDigits
    return digits

def characterPositions(codedPassword):
    for row in range(len(codedPassword)):
        for col in range(len(codedPassword[row])):
            if codedPassword[row][col] == 'A':
                codedPassword[row][col] = 0
            elif codedPassword[row][col] == 'B':
                codedPassword[row][col] = 1
            elif codedPassword[row][col] == 'C':
                codedPassword[row][col] = 2
            elif codedPassword[row][col] == 'D':
                codedPassword[row][col] = 3
            else:
                codedPassword[row][col] = 4
    return codedPassword

def decodePassword(digits, codedPassword, testNumber):
    decodedPassword = list()
    for col in range(len(codedPassword[0])):
        intersection = list()
        for row in range(len(digits)):
            if intersection == []:
                intersection = digits[row][codedPassword[row][col]]
            else:
                intersection = set(intersection).intersection(digits[row][codedPassword[row][col]])
        decodedPassword.append(list(intersection))
    print('Teste %d' % testNumber)
    for row in range(len(decodedPassword)):
        for col in range(len(decodedPassword[row])):
            print(decodedPassword[row][col], end=' ')
    print()
    print()
    return None

# MAIN PROGRAM
numAssociations = int(input())
testNumber = 1
while numAssociations != 0:
    associations = receiveAssociations(numAssociations)
    associationDigits, codedPasswords = separateAssociations(associations, numAssociations)
    associationDigits = separateDigitsIntoPairs(associationDigits)
    codedPasswords = characterPositions(codedPasswords)
    decodePassword(associationDigits, codedPasswords, testNumber)
    numAssociations = int(input())
    testNumber += 1