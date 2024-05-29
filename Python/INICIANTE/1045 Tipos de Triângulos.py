valores = map(float, input().split())
valores = sorted(valores, reverse=True)
A, B, C = valores[0], valores[1], valores[2]

if A >= B + C:
	print('NAO FORMA TRIANGULO')
elif (A**2) == (B**2) + (C**2):
	print("TRIANGULO RETANGULO")
elif (A**2) > (B**2) + (C**2):
	print("TRIANGULO OBTUSANGULO")
elif (A**2) < (B**2) + (C**2):
	print("TRIANGULO ACUTANGULO")

if A == B == C:
	print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
	print("TRIANGULO ISOSCELES")
