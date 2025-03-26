value = int(input())
remainder = value
#BANKNOTES 100
banknotes100 = value // 100
remainder %= 100
#BANKNOTES 50
banknotes50 = remainder // 50
remainder %= 50
#BANKNOTES 20
banknotes20 = remainder // 20
remainder %= 20
#BANKNOTES 10
banknotes10 = remainder // 10
remainder %= 10
#BANKNOTES 5
banknotes5 = remainder // 5
remainder %= 5
#BANKNOTES 2
banknotes2 = remainder // 2
remainder %= 2
#BANKNOTES 1
banknotes1 = remainder // 1
####
print(value)
print(f'{banknotes100} nota(s) de R$ 100,00\n'
      f'{banknotes50} nota(s) de R$ 50,00\n'
      f'{banknotes20} nota(s) de R$ 20,00\n'
      f'{banknotes10} nota(s) de R$ 10,00\n'
      f'{banknotes5} nota(s) de R$ 5,00\n'
      f'{banknotes2} nota(s) de R$ 2,00\n'
      f'{banknotes1} nota(s) de R$ 1,00')
