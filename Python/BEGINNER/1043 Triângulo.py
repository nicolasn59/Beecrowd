a, b, c = map(float, input().split())
if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    areaTrapezio = ((a + b)*c)/2
    print("Area = %.1f" % areaTrapezio)
else:
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
