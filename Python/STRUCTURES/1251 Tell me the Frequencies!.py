# SUBPROGRAM
def countFrequency(charList, filterList, countList, count):
    if charList == [0]:
        return countList
    else:
        for i in range(len(charList)):
            if charList[i] == filterList[count]:
                countList[count] += 1
            else:
                charList = charList[i:]
                return countFrequency(charList, filterList, countList, count+1)

def printFrequency(filterList, countList):
    index = 0
    minCount = countList[0]
    if len(countList) == 1:
        print(filterList[index], minCount)
        return None
    else:
        for i in range(1, len(countList)):
            if minCount > countList[i]:
                minCount = countList[i]
                index = i
        print(filterList[index], minCount)
        filterList.pop(index)
        countList.remove(minCount)
        return printFrequency(filterList, countList)

# MAIN PROGRAM
stop = False
entries = 0
while stop != True:
    try:
        count = 0
        textLine = input()

    except EOFError:
        stop = True
    else:
        if entries != 0:
            print()
        charList = [ord(char) for char in textLine]
        charList += [0]
        charList = sorted(charList, reverse=True)
        filterList = sorted((list(set(charList))), reverse=True)
        countList = [0] * len(filterList)
        countList = countFrequency(charList, filterList, countList, count)
        countList, filterList = countList[:-1], filterList[:-1]
        printFrequency(filterList, countList)
        entries += 1