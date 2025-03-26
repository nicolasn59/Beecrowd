a, b, c = map(float, input().split())
if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    areaTrapezium = ((a + b)*c)/2
    print("Area = %.1f" % areaTrapezium)
else:
    perimeter = a + b + c
    print("Perimetro = %.1f" % perimeter)
    