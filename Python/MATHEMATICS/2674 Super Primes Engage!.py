# SUBPROGRAM
def superPrime(n):
    n = str(n)
    numbers = [int(num) for num in n]
    count = 0
    for num in numbers:
        if isPrime(num) == "Primo":
            count += 1
    if count == len(numbers):
        return "Super"
    return "Primo"


def isPrime(n):
    if n <= 1:
        return "Nada"
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return "Nada"
    return "Primo"


# MAIN PROGRAM
inputFlag = False
try:
    while inputFlag != True:
        number = int(input())
        if isPrime(number) == "Primo":
            print(superPrime(number))
        else:
            print("Nada")
except EOFError:
    inputFlag = True