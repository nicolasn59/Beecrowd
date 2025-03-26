def FallenMeteorites(a1, b1, a2, b2):
    meteorites = 0
    numberOfMeteorites = int(input())
    for i in range(numberOfMeteorites):
        x, y = map(int, input().split())
        if x >= a1 and x <= a2 and y <= b1 and y >= b2:
            meteorites += 1
    return meteorites


x1, y1, x2, y2 = map(int, input().split())
count = 0
while x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0:
    meteoritesOnFarm = FallenMeteorites(x1, y1, x2, y2)
    count += 1
    print('Teste %d' % count)
    print(meteoritesOnFarm)
    x1, y1, x2, y2 = map(int, input().split())