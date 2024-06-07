testes = int(input())
while testes != 0:
    soma = inicio = final = 0
    x, y = map(int, input().split())
    inicio = x if x > y else y
    final = x if x < y else y
    for num in range(inicio, final, -1):
        if num % 2 == 1 and x != num != y:
            soma += num
    print(soma)
    testes -= 1
