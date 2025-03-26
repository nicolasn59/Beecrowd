# SUBPROGRAM
# MAIN PROGRAM
count = 0
maxCount = 0
numDraws = int(input())
values = list(map(int, input().split()))
values += [0]
for num in range(1, len(values)):
    if values[num - 1] == values[num]:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 0
print(maxCount + 1)