inicio = fim = 0
x = int(input())
y = int(input())
inicio = x if x < y else y
fim = x if x > y else y
for num in range(inicio+1, fim):
	if num % 5 == 2 or num % 5 == 3:
		print(num)
