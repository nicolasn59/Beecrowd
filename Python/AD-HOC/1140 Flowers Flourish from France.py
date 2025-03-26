# SUBPROGRAM
def checkTautogram(letters):
    letterFilter = []
    for position in range(len(letters)):
        if letters[position][0].lower() == letters[0][0].lower():
            letterFilter.append('Y')
        else:
            letterFilter.append('N')
    if 'N' in letterFilter:
        return 'N'
    else:
        return 'Y'


# MAIN PROGRAM
phrase = list(map(str, input().split()))
while phrase[0][0] != '*':
    result = checkTautogram(phrase)
    print(result)
    phrase = list(map(str, input().split()))