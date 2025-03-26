# SUBPROGRAM
def checkLastName(lastName):
    count = 0
    for letter in lastName:
        if letter not in "aeiou":
            count += 1
        else:
            count = 0
        if count == 3:
            print("%s nao eh facil" % (lastName[0].upper() + lastName[1:]))
            return None
    print("%s eh facil" % (lastName[0].upper() + lastName[1:]))
    return None


# MAIN
tests = int(input())
for test in range(tests):
    lastName = input().lower()
    checkLastName(lastName)