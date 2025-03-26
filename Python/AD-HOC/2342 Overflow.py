# SUBPROGRAM
def calculateOperation(operation, maxNumber):
    operation[0] = int(operation[0])
    operation[2] = int(operation[2])
    if operation[1] == "+":
        if (operation[0] + operation[2]) > maxNumber:
            return "OVERFLOW"
        else:
            return "OK"
    else:
        if (operation[0] * operation[2]) > maxNumber:
            return "OVERFLOW"
        else:
            return "OK"


# MAIN
maxNumber = int(input())
operation = input().split()
print(calculateOperation(operation, maxNumber))