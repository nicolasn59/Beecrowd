i = 0
j = 0
while i < 2:
    contI = float("%.1f" % i)
    if str(contI)[-1] != "0":
        sum = 1
        for _ in range(3):
            print("I=%.1f" % i, end=' ')
            print("J=%.1f" % (j + sum))
            sum += 1
    else:
        sum = 1
        contI = float("%.0f" % i)
        contJ = float("%.0f" % j)
        for _ in range(3):
            print("I=%d" % int(contI), end=' ')
            print("J=%d" % int(contJ + sum))
            sum += 1
    i += 0.2
    j += 0.2
