decision = sum_of_scores = cont = 0
while decision != 2:
	score = float(input())
	if score < 0 or score > 10:
		print("nota invalida")
	if 0 <= score <= 10:
		sum_of_scores += score
		cont += 1
	if cont == 2:
		print("media = %.2f" % (sum_of_scores/2))
		print("novo calculo (1-sim 2-nao)")
		decision = int(input())
		while decision != 1 and decision != 2:
			print("novo calculo (1-sim 2-nao)")
			decision = int(input())
		cont = sum_of_scores = 0
