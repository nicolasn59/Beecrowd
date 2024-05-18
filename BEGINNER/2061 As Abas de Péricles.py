# Fechou: fecha uma e abre duas abas
# Clicou: Fecha uma aba
inicial, açoes = map(int, input().split())
for _ in range(açoes):
    abas = input()
    if abas == 'fechou':
        inicial += 1
    else:
        inicial -= 1
print(inicial)
