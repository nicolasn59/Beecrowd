# SUBPROGRAM
def breakSequence(sequence):
    paList = list()
    pa = list()
    difference = 0
    for num in range(1, len(sequence)):
        if pa == []:
            difference = sequence[num - 1] - sequence[num]
            pa += [sequence[num - 1]]
        else:
            if sequence[num - 1] - sequence[num] == difference:
                pa += [sequence[num - 1]]
            else:
                pa += [sequence[num - 1]]
                paList += [pa]
                pa = list()
                difference = 0
    if len(pa) == 1:
        paList += [pa]
    print(len(paList))
    return None

# MAIN PROGRAM
numElements = int(input())
sequenceValues = list(map(int, input().split()))
sequenceValues += [float('inf')]
breakSequence(sequenceValues)