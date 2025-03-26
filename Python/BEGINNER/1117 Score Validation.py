sum_of_scores = cont = 0
while cont != 2:
	score = float(input())
	if 0 > score or score > 10:
		print("nota invalida")
	if 0 <= score <= 10:
		sum_of_scores += score
		cont += 1
print("media = %.2f" % (sum_of_scores/2))
