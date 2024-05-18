valor = int(input())
for i in range(valor+2):
    if i % 2 == 0 and i != 0:
        print("%d^2 = %d" % (i, (i**2)))
