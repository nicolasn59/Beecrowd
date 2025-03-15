tipo = int(input())
a, b, c, d, e = map(int, input().split())
cont = 0
if a == tipo:
    cont += 1
if b == tipo:
    cont += 1
if c == tipo:
    cont += 1
if d == tipo:
    cont += 1
if e == tipo:
    cont += 1
print(cont)
