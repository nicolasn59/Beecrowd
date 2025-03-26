blacks = whites = 0
size = int(input())
for square in range(size**2):
    if square % 2 == 0:
        whites += 1
    else:
        blacks += 1
print("%d casas brancas e %d casas pretas" % (whites, blacks))