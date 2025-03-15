idade = int(input())
print(f'{(idade // 365)} ano(s)\n'
      f'{(idade % 365) // 30} mes(es)\n'
      f'{(idade % 365) % 30} dia(s)')
