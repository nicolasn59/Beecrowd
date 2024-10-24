# SUBPROGRAMA
def partition(divs, left, right):
    pivot = divs[right]
    i = left-1
    for j in range(left, right):
        if divs[j] <= pivot:
            i = i+1
            divs[i], divs[j] = divs[j], divs[i]
    divs[i+1], divs[right] = divs[right], divs[i+1]
    return i+1

def quicksort(divs, left, right):
    if left < right:
        pivo = partition(divs, left, right)
        quicksort(divs, left, pivo-1)
        quicksort(divs, pivo+1, right)
    return divs

# PROGRAMA PRINCIPAL

binario = str(input())
decimal = int(binario, 2)
qtdNums = int(input())
divisores = list()
for i in range(qtdNums):
    num = int(input())
    if decimal % num == 0:
        divisores += [num]
if divisores == []:
    print("Nenhum")
else:
    divisores = quicksort(divisores, 0, len(divisores)-1)
    cont = 0
    for i in range(len(divisores)):
        if cont == len(divisores)-1:
            print("%d" % divisores[i])
        else:
            print("%d" % divisores[i], end=' ')
        cont += 1
