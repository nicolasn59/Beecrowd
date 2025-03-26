# SUBPROGRAM
def hex(n):
    array = list()
    while n >= 1:
        array += [int(n % 16)]
        n /= 16
    array = array[::-1]
    index = len(array) - 1
    for number in array:
        if number < 10:
            print(number, end='' if index != 0 else None)
        elif number == 10:
            print("A", end='' if index != 0 else None)
        elif number == 11:
            print("B", end='' if index != 0 else None)
        elif number == 12:
            print("C", end='' if index != 0 else None)
        elif number == 13:
            print("D", end='' if index != 0 else None)
        elif number == 14:
            print("E", end='' if index != 0 else None)
        else:
            print("F", end='' if index != 0 else None)
        index -= 1
    return None

# MAIN PROGRAM
num = int(input())
hex(num)