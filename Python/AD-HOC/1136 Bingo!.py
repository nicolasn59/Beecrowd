# SUBPROGRAM
def partition(bolas, left, right):
    pivot = bolas[right]
    i = left - 1
    for j in range(left, right):
        if bolas[j] <= pivot:
            i = i+1
            bolas[i], bolas[j] = bolas[j], bolas[i]
    bolas[i+1], bolas[right] = bolas[right], bolas[i+1]
    return i+1

def quicksort(bolas, left, right):
    if left < right:
        pivo = partition(bolas, left, right)
        quicksort(bolas, left, pivo-1)
        quicksort(bolas, pivo+1, right)
    return bolas

def sorteio(comb, qtdBolas):
    bolas = list(map(int, input().split()))
    bolas = quicksort(bolas, 0, (len(bolas)-1))
    numDeCombs = list()
    numDeCombs += [0]
    while len(bolas) != 0:
        for j in range(0, len(bolas)):
            num = abs(bolas[0] - bolas[j])
            if num <= comb:
                if num not in numDeCombs:
                    numDeCombs += [num]
            if len(numDeCombs) == (comb+1):
                print("Y")
                return None
        if len(numDeCombs) == (comb+1):
            print("Y")
            return None
        bolas.pop(0)
    if len(numDeCombs) == (comb+1):
        print("Y")
        return None
    else:
        print("N")
        return None

# MAIN
combinacao, quantidadeDeBolas = map(int, input().split())
while combinacao != 0 or quantidadeDeBolas != 0:
    sorteio(combinacao, quantidadeDeBolas)
    combinacao, quantidadeDeBolas = map(int, input().split())
