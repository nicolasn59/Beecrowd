sequence = []
count = 1
length = int(input())

for _ in range(length):
    sequence.append(int(input()))

for i in range(len(sequence) - 1):
    if sequence[i] != sequence[i + 1]:
        count += 1

print(count)