N = int(input())

for _ in range(N):
    phrase = input().strip().lower()

    frequencies = {}
    for letter in phrase:
        if (letter.isalpha()):
            if (not letter in frequencies):
                frequencies[letter] = 0
            frequencies[letter] += 1

    maxFreq = 0
    for letter in frequencies:
        maxFreq = frequencies[letter] if frequencies[letter] > maxFreq else maxFreq

    answer = []
    for letter in frequencies:
        if (frequencies[letter] == maxFreq):
            answer.append(letter)

    answer.sort()
    print(''.join(answer))