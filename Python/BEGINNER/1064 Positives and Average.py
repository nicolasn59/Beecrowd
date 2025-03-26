n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
sum = cont = 0

if n1 > 0:
    cont += 1
    sum += n1
if n2 > 0:
    cont += 1
    sum += n2
if n3 > 0:
    cont += 1
    sum += n3
if n4 > 0:
    cont += 1
    sum += n4
if n5 > 0:
    cont += 1
    sum += n5
if n6 > 0:
    cont += 1
    sum += n6

print("%d valores positivos" % int(cont))
print("%.1f" % (sum/cont))
