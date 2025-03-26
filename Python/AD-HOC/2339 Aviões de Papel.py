competitors, paperQuantity, paperPerCompetitor = map(int, input().split())
if paperQuantity // competitors >= paperPerCompetitor:
    print('S')
else:
    print('N')