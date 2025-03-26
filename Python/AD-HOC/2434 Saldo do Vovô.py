minBalance = 0
days, initialBalance = map(int, input().split())
for _ in range(days):
    balance = int(input())
    initialBalance += balance

    if minBalance == 0:
        minBalance = initialBalance
    else:
        if initialBalance < minBalance:
            minBalance = initialBalance
print(minBalance)