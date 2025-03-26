# SUBPROGRAM
def fruitConsumption(days):
    weight = value = 0
    for day in range(1, days+1):
        value += float(input())
        fruits = list(map(str, input().split()))
        print('day %s: %d kg' % (day, len(fruits)))
        weight += len(fruits)

    averageWeight = '%.2f kg by day' % (weight/days)
    averagePrice = 'R$ %.2f by day' % (value/days)
    return '%s\n%s' % (averageWeight, averagePrice)

# MAIN
numTests = int(input())
print(fruitConsumption(numTests))