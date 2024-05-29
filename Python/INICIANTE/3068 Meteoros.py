def MeteoritosCaidos(a1, b1, a2, b2):
    meteoritos = 0
    numeroDeMeteoritos = int(input())
    for i in range(numeroDeMeteoritos):
        x, y = map(int, input().split())
        if x >= a1 and x <= a2 and y <= b1 and y >= b2:
            meteoritos += 1
    return meteoritos


x1, y1, x2, y2 = map(int, input().split())
cont = 0
while x1 != 0 or y1 != 0 or x2 != 0 or y2 != 0:
    meteoritosNaFazenda = MeteoritosCaidos(x1, y1, x2, y2)
    cont += 1
    print('Teste %d' % cont)
    print(meteoritosNaFazenda)
    x1, y1, x2, y2 = map(int, input().split())
