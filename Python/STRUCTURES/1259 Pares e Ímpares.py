# SUBPROGRAMA
def quicksort(arr, start, end):
    if start < end:
        if arr[0] % 2 == 0:  # if arr[0] == even number
            pivotPosition = partitionAscending(arr, start, end)
            quicksort(arr, start, pivotPosition-1)
            quicksort(arr, pivotPosition+1, end)
        else:  # if arr[0] == odd number
            pivotPosition = partitionDescending(arr, start, end)
            quicksort(arr, start, pivotPosition-1)
            quicksort(arr, pivotPosition+1, end)
    return None

def partitionAscending(arr, start, end):
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]  # pivot = arr[end]
    return i

def partitionDescending(arr, start, end):
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] >= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]  # pivot = arr[end]
    return i


# PROGRAMA PRINCIPAL
lengh = int(input())
evenNumbers = list()
oddNumbers = list()
for i in range(0, lengh):
    number = int(input())
    if number % 2 == 0:
        evenNumbers += [number]
    else:
        oddNumbers += [number]
quicksort(evenNumbers, 0, len(evenNumbers)-1)
quicksort(oddNumbers, 0, len(oddNumbers)-1)
for i in range(0, len(evenNumbers)):
    print("%d" % evenNumbers[i])
for i in range(0, len(oddNumbers)):
    print("%d" % oddNumbers[i])
