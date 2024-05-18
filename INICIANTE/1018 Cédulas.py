valor = int(input())
resto = valor
#NOTAS DE 100
notas100 = valor // 100
resto %= 100
#NOTAS DE 50
notas50 = resto // 50
resto %= 50
#NOTAS DE 20
notas20 = resto // 20
resto %= 20
#NOTAS DE 10
notas10 = resto // 10
resto %= 10
#NOTAS DE 5
notas5 = resto // 5
resto %= 5
#NOTAS DE 2
notas2 = resto // 2
resto %= 2
#NOTA DE 1
notas1 = resto // 1
####
print(valor)
print(f'{notas100} nota(s) de R$ 100,00\n'
      f'{notas50} nota(s) de R$ 50,00\n'
      f'{notas20} nota(s) de R$ 20,00\n'
      f'{notas10} nota(s) de R$ 10,00\n'
      f'{notas5} nota(s) de R$ 5,00\n'
      f'{notas2} nota(s) de R$ 2,00\n'
      f'{notas1} nota(s) de R$ 1,00')
