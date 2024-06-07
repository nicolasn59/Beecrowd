boas = ruins = 0
listaDeNomes = list()
numeroDeCriancas = int(input())
for i in range(numeroDeCriancas):
    sinal, nome = input().split()
    if sinal == '+':
        boas += 1
    else:
        ruins += 1
    listaDeNomes += [nome]
listaDeNomes.sort()
for crianca in listaDeNomes:
    print(crianca)
print("Se comportaram: %d | Nao se comportaram: %d" % (boas, ruins))
