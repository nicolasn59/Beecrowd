salary = float(input())
if salary <= 400:
    new_salary = (salary*115)/100
elif 400 < salary <= 800:
    new_salary = (salary * 112)/100
elif 800 < salary <= 1200:
    new_salary = (salary * 110)/100
elif 1200 < salary <= 2000:
    new_salary = (salary * 107)/100
else:
    new_salary = (salary * 104)/100

print("Novo salario: %.2f" % new_salary)
print("Reajuste ganho: %.2f" % (new_salary - salary))
print("Em percentual: %d" % (((new_salary * 100)/salary)-100), "%")
