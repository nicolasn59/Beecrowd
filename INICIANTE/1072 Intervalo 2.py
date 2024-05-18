dentro = fora = 0
entradas = int(input())
for i in range(1, entradas + 1):
    valor = int(input())
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1
print("%d in" % dentro)
print("%d out" % fora)
