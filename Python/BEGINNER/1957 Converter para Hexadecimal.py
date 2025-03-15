# SUBPROGRAMA
def hex(n):
    array = list()
    while n >= 1:
        array += [int(n % 16)]
        n /= 16
    array = array[::-1]
    indice = len(array) - 1
    for numero in array:
        if numero < 10:
            print(numero, end='' if indice != 0 else None)
        elif numero == 10:
            print("A", end='' if indice != 0 else None)
        elif numero == 11:
            print("B", end='' if indice != 0 else None)
        elif numero == 12:
            print("C", end='' if indice != 0 else None)
        elif numero == 13:
            print("D", end='' if indice != 0 else None)
        elif numero == 14:
            print("E", end='' if indice != 0 else None)
        else:
            print("F", end='' if indice != 0 else None)
        indice -= 1
    return None

# PROGRAMA PRINCIPAL
num = int(input())
hex(num)
