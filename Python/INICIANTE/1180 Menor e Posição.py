tamanhoDoVetor = int(input())
vetor = list(map(int, input().split()))
menor = vetor[0]
posicao = 0

for i in range(1, len(vetor)):
    if vetor[i] < menor:
        menor = vetor[i]
        posicao = i

print("Menor valor: %d" % menor)
print("Posicao: %d" % (posicao))
