def sortByLength(words):
    sortedList = list()
    wordLengths = [len(word) for word in words]

    while len(wordLengths) >= 1:
        maxLength = pos = 0
        for index, length in enumerate(wordLengths):
            if maxLength == 0:
                maxLength = length
                pos = index
            elif length > maxLength:
                maxLength = length
                pos = index
        sortedList.append(words[pos])
        wordLengths.pop(pos)
        words.pop(pos)

    return ' '.join(sortedList)


tests = int(input())
for i in range(tests):
    phrase = list(map(str, input().split()))
    sortedLength = sortByLength(phrase)
    print(sortedLength)