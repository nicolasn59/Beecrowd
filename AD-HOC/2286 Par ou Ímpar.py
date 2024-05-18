cont = 1
while True:
    lista = []
    n = int(input())

    if n == 0:
        break

    j1 = input().strip()
    j2 = input().strip()

    for i in range(n):
        a, b = map(int, input().split())
        lista.append(j1 if (a + b) % 2 == 0 else j2)

    print(f'Teste {cont}')
    for nome in lista:
        print(nome)
    print()
    cont += 1
