def decodeMessage(encodedMsg):
    message = []
    if encodedMsg == []:
        return ''
    else:
        for word in range(len(encodedMsg)):
            message.append(encodedMsg[word][0])
    return ''.join(message)


# MAIN PROGRAM
numPhrases = int(input())
while numPhrases != 0:
    encodedMessage = input().split()
    message = decodeMessage(encodedMessage)
    print(message)
    numPhrases -= 1