salario = float(input())
if salario <= 400:
    novoSalario = (salario*115)/100
elif 400 < salario <= 800:
    novoSalario = (salario * 112)/100
elif 800 < salario <= 1200:
    novoSalario = (salario * 110)/100
elif 1200 < salario <= 2000:
    novoSalario = (salario * 107)/100
else:
    novoSalario = (salario * 104)/100

print("Novo salario: %.2f" % novoSalario)
print("Reajuste ganho: %.2f" % (novoSalario - salario))
print("Em percentual: %d" % (((novoSalario * 100)/salario)-100), "%")
