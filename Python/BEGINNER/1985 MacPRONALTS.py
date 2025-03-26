p = int(input())
value = 0
for _ in range(p):
    a, b = map(int, input().split())
    if a == 1001:
        value += b * 1.50
    elif a == 1002:
        value += b * 2.50
    elif a == 1003:
        value += b * 3.50
    elif a == 1004:
        value += b * 4.50
    else:
        value += b * 5.50
print(f'{value:.2f}')
