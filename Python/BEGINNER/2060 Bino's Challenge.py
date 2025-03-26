# SUBPROGRAM
def checkMultiples(lst):
    multiplesOfTwo = multiplesOfThree = multiplesOfFour = multiplesOfFive = 0
    for num in lst:
        if (num % 2) == 0:
            multiplesOfTwo += 1
        if (num % 3) == 0:
            multiplesOfThree += 1
        if (num % 4) == 0:
            multiplesOfFour += 1
        if (num % 5) == 0:
            multiplesOfFive += 1
    print("%d Multiplo(s) de 2" % multiplesOfTwo)
    print("%d Multiplo(s) de 3" % multiplesOfThree)
    print("%d Multiplo(s) de 4" % multiplesOfFour)
    print("%d Multiplo(s) de 5" % multiplesOfFive)
    return None

# MAIN PROGRAM
listSize = int(input())
lst = list(map(int, input().split()))
checkMultiples(lst)