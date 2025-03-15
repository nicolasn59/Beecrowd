testes = int(input())
total = coelho = rato = sapo = 0
for i in range(testes):
	cobaia = input().split()
	if cobaia[-1] == "C":
		coelho += int(cobaia[0])
	elif cobaia[-1] == "R":
		rato += int(cobaia[0])
	else:
		sapo += int(cobaia[0])
	total += int(cobaia[0])
print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % coelho)
print("Total de ratos: %d" % rato)
print("Total de sapos: %d" % sapo)
print("Percentual de coelhos: %.2f" % ((coelho*100)/total), "%")
print("Percentual de ratos: %.2f" % ((rato*100)/total), "%")
print("Percentual de sapos: %.2f" % ((sapo*100)/total), "%")
