value = float(input()) * 100

banknotes100 = value // 10000
value %= 10000

banknotes50 = value // 5000
value %= 5000

banknotes20 = value // 2000
value %= 2000

banknotes10 = value // 1000
value %= 1000

banknotes5 = value // 500
value %= 500

banknotes2 = value // 200
value %= 200

#COINS

coins1 = value // 100
value %= 100

coins050 = value // 50
value %= 50

coins025 = value // 25
value %= 25

coins010 = value // 10
value %= 10

coins005 = value // 5
value %= 5

coins001 = value // 1
value %= 1

print(f'NOTAS:\n'
      f'{banknotes100:.0f} nota(s) de R$ 100.00\n'
      f'{banknotes50:.0f} nota(s) de R$ 50.00\n'
      f'{banknotes20:.0f} nota(s) de R$ 20.00\n'
      f'{banknotes10:.0f} nota(s) de R$ 10.00\n'
      f'{banknotes5:.0f} nota(s) de R$ 5.00\n'
      f'{banknotes2:.0f} nota(s) de R$ 2.00\n'
      f'MOEDAS:\n'
      f'{coins1:.0f} moeda(s) de R$ 1.00\n'
      f'{coins050:.0f} moeda(s) de R$ 0.50\n'
      f'{coins025:.0f} moeda(s) de R$ 0.25\n'
      f'{coins010:.0f} moeda(s) de R$ 0.10\n'
      f'{coins005:.0f} moeda(s) de R$ 0.05\n'
      f'{coins001:.0f} moeda(s) de R$ 0.01')
