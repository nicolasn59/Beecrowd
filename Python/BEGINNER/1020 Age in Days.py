age = int(input())
print(f'{(age // 365)} ano(s)\n'
      f'{(age % 365) // 30} mes(es)\n'
      f'{(age % 365) % 30} dia(s)')
