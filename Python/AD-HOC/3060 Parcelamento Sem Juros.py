from math import ceil

value = int(input())
installments = int(input())

count = 0
for _ in range(installments):
    if count < (value % installments):
        print(ceil(value/installments))
        count += 1
    else:
        print(value//installments)