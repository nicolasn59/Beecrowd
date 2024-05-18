from math import ceil

v = int(input())
p = int(input())

cont = 0
for _ in range(p):
    if cont < (v % p):
        print(ceil(v/p))
        cont += 1
    else:
        print(v//p)
