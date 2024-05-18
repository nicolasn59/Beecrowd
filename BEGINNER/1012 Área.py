a, b, c = map(float, input().split())
print(f'TRIANGULO: {(a * c)/2:.3f}\n'
      f'CIRCULO: {(3.14159) * (c ** 2):.3f}\n'
      f'TRAPEZIO: {((a + b) * c)/2:.3f}\n'
      f'QUADRADO: {(b*b):.3f}\n'
      f'RETANGULO: {a*b:.3f}')
