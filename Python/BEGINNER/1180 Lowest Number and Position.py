vector_size = int(input())
vector = list(map(int, input().split()))
smaller = vector[0]
position = 0

for i in range(1, len(vector)):
    if vector[i] < smaller:
        smaller = vector[i]
        position = i

print("Menor valor: %d" % smaller)
print("Posicao: %d" % (position))
