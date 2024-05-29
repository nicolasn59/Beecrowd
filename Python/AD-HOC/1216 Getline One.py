cont = distancia = 0
while True:
    try:
        nome = input()
        distancia += int(input())
        cont += 1
        media = distancia / cont

    except EOFError:
        print("%.1f" % media)
        break
