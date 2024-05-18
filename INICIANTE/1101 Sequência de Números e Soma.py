def somaDaSequencia(num1, num2):
	maior = menor = soma = 0
	if num1 > num2:
		maior = num1
		menor = num2
	else:
		maior = num2
		menor = num1
	for i in range(menor, maior+1):
		print(i, end=' ')
		soma += i
	msg = 'Sum=%d' % soma
	return msg

valor1, valor2 = map(int, input().split())
while valor1 > 0 and valor2 > 0:
	somador = somaDaSequencia(valor1, valor2)
	print(somador)
	valor1, valor2 = map(int, input().split())
