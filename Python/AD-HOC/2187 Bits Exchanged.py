# SUBPROGRAM
def calculateBills(val):
    fifty = ten = five = one = 0
    while val != 0:
        if (val - 50) >= 0:
            val -= 50
            fifty += 1
        elif (val - 10) >= 0:
            val -= 10
            ten += 1
        elif (val - 5) >= 0:
            val -= 5
            five += 1
        else:
            val -= 1
            one += 1
    return fifty, ten, five, one


# MAIN
testNumber = 1
value = int(input())
while value != 0:
    billsUsed = calculateBills(value)
    print('Teste %d' % testNumber)
    print(billsUsed[0], billsUsed[1], billsUsed[2], billsUsed[3])
    print()
    value = int(input())
    testNumber += 1