# SUBPROGRAM
def receiveInputs(numValues):
    numList = list()
    numFilter = list()
    for i in range(numValues):
        num = int(input())
        numList += [num]
        if num not in numFilter:
            numFilter += [num]
    numFilter.sort()
    numList.sort()
    return numList, numFilter

def countNumbers(numList, numFilter, numValues, count, index):
    numList += [0]
    numFilter += [0]
    while True:
        j = 0
        while numFilter[0] == numList[j]:
            if numList[j] == 0:
                return count
            else:
                count[index] += 1
                j += 1
        numList = numList[j:]
        numFilter = numFilter[1:]
        index += 1


# MAIN PROGRAM
index = 0
numValues = int(input())
numList, numFilter = receiveInputs(numValues)
count = [0] * len(numFilter)
numCount = countNumbers(numList, numFilter, numValues, count, index)
numFilter.remove(0)
numList.remove(0)
for i in range(len(numFilter)):
    print("%s aparece %s vez(es)" % (numFilter[i], count[i]))