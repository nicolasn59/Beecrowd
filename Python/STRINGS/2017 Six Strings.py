# SUBPROGRAM
def findSmallest(count):
    smallest = count[0]
    index = 0
    for i in range(1, len(count)):
        if count[i] < smallest:
            smallest = count[i]
            index = i
    count.pop(index)
    return count, index, smallest

def editDistance(originalWord, num):
    count = [0] * 5
    difference = smallest = 0
    for i in range(5):
        word = input()
        word = [letter for letter in word]
        if len(word) > len(originalWord):
            originalWord += ["."] * (len(word) - len(originalWord))
            difference = (len(word) - len(originalWord))
        else:
            if len(word) < len(originalWord):
                word += ["."] * (len(originalWord) - len(word))
                difference = (len(originalWord) - len(word))
        for j in range(len(word)):
            if originalWord[j] != word[j]:
                count[i] += 1
        count[i] += difference
    count, index, smallest = findSmallest(count)
    if smallest < num:
        print(index+1)
        print(smallest)
    else:
        print(-1)
    return None

# MAIN PROGRAM
originalWord = input()
number = int(input())
originalWord = [letter for letter in originalWord]
editDistance(originalWord, number)