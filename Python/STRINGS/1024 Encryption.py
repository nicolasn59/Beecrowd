# SUBPROGRAM
def encryption():
    phrase = input()
    phrase = [ord(char) for char in phrase]
    phrase = [(value + 3) if chr(value).isalpha() else value for value in phrase]
    phrase.reverse()
    phrase = [(value-1) if index >= (len(phrase)//2) else value for index, value in enumerate(phrase)]
    phrase = [chr(number) for number in phrase]
    phrase = ''.join(phrase)
    return phrase


# MAIN
numPhrases = int(input())
for i in range(numPhrases):
    encryptedPhrase = encryption()
    print(encryptedPhrase)