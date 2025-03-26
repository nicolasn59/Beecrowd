tests = int(input())
while tests != 0:
    sum = start = end = 0
    x, y = map(int, input().split())
    start = x if x > y else y
    end = x if x < y else y
    for num in range(start, end, -1):
        if num % 2 == 1 and x != num != y:
            sum += num
    print(sum)
    tests -= 1
