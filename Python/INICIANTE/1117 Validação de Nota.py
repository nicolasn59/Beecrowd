somaDasNotas = cont = 0
while cont != 2:
	nota = float(input())
	if 0 > nota or nota > 10:
		print("nota invalida")
	if 0 <= nota <= 10:
		somaDasNotas += nota
		cont += 1
print("media = %.2f" % (somaDasNotas/2))
