p = int(input())
valor = 0
for _ in range(p):
    a, b = map(int, input().split())
    if a == 1001:
        valor += b * 1.50
    elif a == 1002:
        valor += b * 2.50
    elif a == 1003:
        valor += b * 3.50
    elif a == 1004:
        valor += b * 4.50
    else:
        valor += b * 5.50
print(f'{valor:.2f}')
