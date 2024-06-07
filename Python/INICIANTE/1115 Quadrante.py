x, y = map(int, input().split())
while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        print("quarto")
    x, y = map(int, input().split())
