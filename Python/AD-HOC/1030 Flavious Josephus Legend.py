nc = int(input())
for _ in range(nc):
    count = 0
    n, k = map(int, input().split())
    list = [i for i in range(1, n, k)]

    for i in range(k):
        for v in list:
            print(v)
            if count >= k:
                list.remove(v)
                break
            count += 1
        if count >= k:
            break

    resultList = []
    print(list)