# SUBPROGRAMA
def dias_com_comida():
    dias = 0
    quantidade_comida = float(input())

    if quantidade_comida == 1:
        return dias

    while quantidade_comida > 1:
        quantidade_comida //= 2
        dias += 1
    return dias

#  PROGRAMA PRINCIPAL

numero_testes = int(input())
for _ in range(numero_testes):
    resultado = dias_com_comida()
    print('%d %s' % (resultado, 'dias'))
