def converter_num_int(valores):
    novos_valores = []
    for valor in valores:
        if valor.isnumeric() == True:
            novos_valores.append(int(valor))
        else:
            novos_valores.append(valor)
    return novos_valores


def calculo_fracao(novos_valores):
    N1, D1, N2, D2 = novos_valores[0], novos_valores[2], novos_valores[4], novos_valores[6]
    sinal = novos_valores[3]

    if sinal == '+':
        numerador = ((N1 * D2) + (N2 * D1))
        denominador = (D1 * D2)

    elif sinal == '-':
        numerador = ((N1 * D2) - (N2 * D1))
        denominador = (D1 * D2)

    elif sinal == '*':
        numerador = (N1 * N2)
        denominador = (D1 * D2)

    else:
        numerador = (N1 * D2)
        denominador = (N2 * D1)


    numerador_simplificado = numerador
    denominador_simplificado = denominador
    lista_num = [2, 3, 5, 7, 9]
    cont = 1

    while True:

        if numerador_simplificado == denominador_simplificado:
            numerador_simplificado = 1
            denominador_simplificado = 1
            break

        for num in lista_num:
            if numerador_simplificado % num == 0 and denominador_simplificado % num == 0:
                numerador_simplificado //= num
                denominador_simplificado //= num
                cont -= 1
            else:
                cont += 1

        if cont > 5:
            break

    return f'{numerador}/{denominador} = {numerador_simplificado}/{denominador_simplificado}'


n = int(input())

for _ in range(n):
    valores = list(map(str, input().split()))

    novos_valores = converter_num_int(valores)
    resultado = calculo_fracao(novos_valores)

    print(resultado)
