# SUBPROGRAM
def gcd(dividend, divisor):
    if divisor == 0:
        return dividend
    else:
        return gcd(divisor, dividend % divisor)


def simplify(dividend, divisor):
    return (dividend // gcd(dividend, divisor)), (divisor // gcd(dividend, divisor))


def sumFractions(a, b, c, d):
    a, b = simplify(a, b)
    c, d = simplify(c, d)
    x, y = ((a*d) + (b * c)), (b * d)
    return simplify(x, y)


# MAIN PROGRAM
A, B, C, D = map(int, input().split())
X, Y = sumFractions(A, B, C, D)
print(X, Y)