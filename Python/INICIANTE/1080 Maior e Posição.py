maior = posicao = 0
for i in range(1, 101):
	num = int(input())
	if maior == 0:
		maior = num
		posicao = i
	elif num > maior:
		maior = num
		posicao = i
print(maior)
print(posicao)
