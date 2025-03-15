# PRINCIPAL
listaDeNumeros = list()
a, b, c, d = map(int, input().split())
for num in range(1, int(c**0.5) + 1):
    if c % num == 0:
        if num % a == 0 and num % b != 0 and c % num == 0 and d % num != 0:
            listaDeNumeros += [num]
        if (c // num) % a == 0 and (c // num) % b != 0 and c % (c // num) == 0 and d % (c // num) != 0:
            listaDeNumeros += [c // num]
if listaDeNumeros == []:
    print(-1)
else:
    print(min(listaDeNumeros))
