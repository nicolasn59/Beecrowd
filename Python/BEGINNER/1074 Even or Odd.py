n = int(input())
for i in range(n):
    num = int(input())
    if num == 0:
        print("NULL")
    else:
        print("EVEN" if num % 2 == 0 else "ODD", end=' ')
        print("POSITIVE" if num > 0 else "NEGATIVE")
