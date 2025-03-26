# SUBPROGRAM
# MAIN PROGRAM
value, payment = map(int, input().split())
while ((value != 0) or (payment != 0)):
    change = payment - value
    for i in range(2):
        if change >= 100:
            change -= 100
        elif change >= 50:
            change -= 50
        elif change >= 20:
            change -= 20
        elif change >= 10:
            change -= 10
        elif change >= 5:
            change -= 5
        elif change >= 2:
            change -= 2
        else:
            change = -1
    if change == 0:
        print("possible")
    else:
        print("impossible")
    value, payment = map(int, input().split())