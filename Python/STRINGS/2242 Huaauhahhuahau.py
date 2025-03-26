# SUBPROGRAM
# MAIN PROGRAM
word = input()
onlyVowels = list()
for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        onlyVowels += [letter]
laugh = ''.join(onlyVowels)
if laugh == laugh[::-1]:
    print('S')
else:
    print('N')