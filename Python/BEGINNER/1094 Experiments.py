# coelho = rabbit
# rato = mouse
# sapo = frog

inputs = int(input())
total = coelho = rato = sapo = 0
for i in range(inputs):
	lab_animal = input().split()
	if lab_animal[-1] == "C":
		coelho += int(lab_animal[0])
	elif lab_animal[-1] == "R":
		rato += int(lab_animal[0])
	else:
		sapo += int(lab_animal[0])
	total += int(lab_animal[0])
print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % coelho)
print("Total de ratos: %d" % rato)
print("Total de sapos: %d" % sapo)
print("Percentual de coelhos: %.2f" % ((coelho*100)/total), "%")
print("Percentual de ratos: %.2f" % ((rato*100)/total), "%")
print("Percentual de sapos: %.2f" % ((sapo*100)/total), "%")
