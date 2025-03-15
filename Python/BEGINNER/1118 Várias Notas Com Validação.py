decisao = somaDasNotas = cont = 0
while decisao != 2:
	nota = float(input())
	if nota < 0 or nota > 10:
		print("nota invalida")
	if 0 <= nota <= 10:
		somaDasNotas += nota
		cont += 1
	if cont == 2:
		print("media = %.2f" % (somaDasNotas/2))
		print("novo calculo (1-sim 2-nao)")
		decisao = int(input())
		while decisao != 1 and decisao != 2:
			print("novo calculo (1-sim 2-nao)")
			decisao = int(input())
		cont = somaDasNotas = 0
