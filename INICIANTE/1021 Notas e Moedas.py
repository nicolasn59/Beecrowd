valor = float(input()) * 100

notas100 = valor // 10000
valor %= 10000

notas50 = valor // 5000
valor %= 5000

notas20 = valor // 2000
valor %= 2000

notas10 = valor // 1000
valor %= 1000

notas5 = valor // 500
valor %= 500

notas2 = valor // 200
valor %= 200

#MOEDAS

moeda1 = valor // 100
valor %= 100

moeda050 = valor // 50
valor %= 50

moeda025 = valor // 25
valor %= 25

moeda010 = valor // 10
valor %= 10

moeda005 = valor // 5
valor %= 5

moeda001 = valor // 1
valor %= 1

print(f'NOTAS:\n'
      f'{notas100:.0f} nota(s) de R$ 100.00\n'
      f'{notas50:.0f} nota(s) de R$ 50.00\n'
      f'{notas20:.0f} nota(s) de R$ 20.00\n'
      f'{notas10:.0f} nota(s) de R$ 10.00\n'
      f'{notas5:.0f} nota(s) de R$ 5.00\n'
      f'{notas2:.0f} nota(s) de R$ 2.00\n'
      f'MOEDAS:\n'
      f'{moeda1:.0f} moeda(s) de R$ 1.00\n'
      f'{moeda050:.0f} moeda(s) de R$ 0.50\n'
      f'{moeda025:.0f} moeda(s) de R$ 0.25\n'
      f'{moeda010:.0f} moeda(s) de R$ 0.10\n'
      f'{moeda005:.0f} moeda(s) de R$ 0.05\n'
      f'{moeda001:.0f} moeda(s) de R$ 0.01')
