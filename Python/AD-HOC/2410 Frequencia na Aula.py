# SUBPROGRAMA
# PROGRAMA PRINCIPAL
registros = list()
numeroDeRegistros = int(input())
for registro in range(numeroDeRegistros):
    registros += [int(input())]
print(len(list(set(registros))))
