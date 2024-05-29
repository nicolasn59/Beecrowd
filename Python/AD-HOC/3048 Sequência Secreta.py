lista = []
cont = 1
tamanho = int(input())

for _ in range(tamanho):
    lista.append(int(input()))

for i in range(len(lista) - 1):
    if lista[i] != lista[i + 1]:
        cont += 1

print(cont)
