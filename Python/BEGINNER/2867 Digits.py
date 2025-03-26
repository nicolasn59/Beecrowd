# SUBPROGRAM
def power(base, exponent):
    powerResult = base ** exponent   # base raised to the exponent
    powerResult = str(powerResult)
    return len(powerResult)

# MAIN
numberOfOperations = int(input())
while numberOfOperations != 0:
    base, exponent = map(int, input().split())
    numberOfDigits = power(base, exponent)
    print(numberOfDigits)
    numberOfOperations -= 1