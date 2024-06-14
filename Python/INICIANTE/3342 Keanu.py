pretas = brancas = 0
tamanho = int(input())
for casa in range(tamanho**2):
	if casa % 2 == 0:
		brancas += 1
	else:
		pretas += 1
print("%d casas brancas e %d casas pretas" % (brancas, pretas))
