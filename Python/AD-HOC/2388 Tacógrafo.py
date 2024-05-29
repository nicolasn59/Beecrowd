distancia = 0
intervalos = int(input())
for _ in range(intervalos):
    horas, velocidade_media = map(int, input().split())
    distancia += horas * velocidade_media
print(distancia)
