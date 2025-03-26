# SUBPROGRAM
def partition(divisors, left, right):
    pivot = divisors[right]
    i = left-1
    for j in range(left, right):
        if divisors[j] <= pivot:
            i = i+1
            divisors[i], divisors[j] = divisors[j], divisors[i]
    divisors[i+1], divisors[right] = divisors[right], divisors[i+1]
    return i+1

def quicksort(divisors, left, right):
    if left < right:
        pivot = partition(divisors, left, right)
        quicksort(divisors, left, pivot-1)
        quicksort(divisors, pivot+1, right)
    return divisors

# MAIN PROGRAM

binary = str(input())
decimal = int(binary, 2)
numNumbers = int(input())
divisors = list()
for i in range(numNumbers):
    num = int(input())
    if decimal % num == 0:
        divisors += [num]
if divisors == []:
    print("Nenhum")
else:
    divisors = quicksort(divisors, 0, len(divisors)-1)
    count = 0
    for i in range(len(divisors)):
        if count == len(divisors)-1:
            print("%d" % divisors[i])
        else:
            print("%d" % divisors[i], end=' ')
        count += 1