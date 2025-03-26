while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    width = int(input())
    donation = int(input())

    length = list(map(int, input().split()))
    length = sorted(length, reverse=True)
    print(length)
    areaHall = m * n
    areaBoard = count = 0

    for value in length:
        areaBoard += value * (width / 100)
        count += 1
        if areaBoard >= areaHall:
            print(count)
            break

    if areaBoard < areaHall:
        print('impossivel')