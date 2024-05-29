def raios_repetidos(registros):
    conjunto_quadrantes = set()  # CONJUNTO NÃO DEIXA ELEM repetidos
    for raio in registros:
        quadrante = f"{raio[0]}_{raio[1]}" # CONCATENANDO OS VALORES EM UMA ÚNICA STRING, O TEMPO DE EXECUÇÃO É REDUZIDO PELA METADE
        if quadrante in conjunto_quadrantes:
            return 1
        conjunto_quadrantes.add(quadrante)
    return 0


registros = []
n = int(input())

for _ in range(n):
    x, y = list(map(int, input().split()))
    registros.append((x, y))

print(raios_repetidos(registros))
