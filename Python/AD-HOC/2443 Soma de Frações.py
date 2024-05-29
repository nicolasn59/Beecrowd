# SUBPROGRAMA
def mdc(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return mdc(divisor, dividendo % divisor)


def simplificar(dividendo, divisor):
    return (dividendo // mdc(dividendo, divisor)), (divisor // mdc(dividendo, divisor))


def somaFracoes(a, b, c, d):
    a, b = simplificar(a, b)
    c, d = simplificar(c, d)
    x, y = ((a*d) + (b * c)), (b * d)
    return simplificar(x, y)


# PROGRAMA PRINCIPAL
A, B, C, D = map(int, input().split())
X, Y = somaFracoes(A, B, C, D)
print(X, Y)