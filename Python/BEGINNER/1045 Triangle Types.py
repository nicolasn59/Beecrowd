values = map(float, input().split())
values = sorted(values, reverse=True)
A, B, C = values[0], values[1], values[2]

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
