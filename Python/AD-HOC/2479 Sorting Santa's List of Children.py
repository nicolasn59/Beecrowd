good = bad = 0
nameList = list()
numChildren = int(input())
for i in range(numChildren):
    signal, name = input().split()
    if signal == '+':
        good += 1
    else:
        bad += 1
    nameList += [name]
nameList.sort()
for child in nameList:
    print(child)
print("Se comportaram: %d | Nao se comportaram: %d" % (good, bad))