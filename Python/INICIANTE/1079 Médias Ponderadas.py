n = int(input())
for i in range(n):
    nota1, nota2, nota3 = map(float, input().split())
    print("%.1f" % (((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)))
