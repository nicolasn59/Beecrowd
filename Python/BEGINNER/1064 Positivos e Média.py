n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
soma = cont = 0

if n1 > 0:
    cont += 1
    soma += n1
if n2 > 0:
    cont += 1
    soma += n2
if n3 > 0:
    cont += 1
    soma += n3
if n4 > 0:
    cont += 1
    soma += n4
if n5 > 0:
    cont += 1
    soma += n5
if n6 > 0:
    cont += 1
    soma += n6

print("%d valores positivos" % int(cont))
print("%.1f" % (soma/cont))
