# SUBPROGRAMA
def fat(num):
    if num == 0:
        return 1
    else:
        return num * fat(num-1)


# PROGRAMA PRINCIPAL
while True:
    try:
        num1, num2 = map(int, input().split())
        print(fat(num1) + fat(num2))
    except EOFError:
        break
