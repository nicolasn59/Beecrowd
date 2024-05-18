nc = int(input())
for _ in range(nc):
    cont = 0
    n, k = map(int, input().split())
    lista = [i for i in range(1, n, k)]

    for i in range(k):
        for v in lista:
            print(v)
            if cont >= k:
                lista.remove(v)
                break
            cont += 1
        if cont >= k:
            break

    lista_resultado = []
    print(lista)
