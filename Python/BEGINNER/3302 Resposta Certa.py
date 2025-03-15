numeroDePerguntas = int(input())
cont = 0
while cont != numeroDePerguntas:
    cont += 1
    resposta = int(input())
    print('resposta %d: %d' % (cont, resposta))
