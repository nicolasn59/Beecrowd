n = int(input())
for i in range(n + 1):
    if n % (i+1) == 0:
        print(i+1)
