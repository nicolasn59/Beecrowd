cups = list(map(int, input().split()))
for i, v in enumerate(cups, start=1):
    if v == 1:
        print(i)