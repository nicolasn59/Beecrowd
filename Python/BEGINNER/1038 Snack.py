code, amount = map(int, input().split())
if code == 1:
    print(f'Total: R$ {amount * 4:.2f}')

elif code == 2:
    print(f'Total: R$ {amount * 4.5:.2f}')

elif code == 3:
    print(f'Total: R$ {amount * 5:.2f}')

elif code == 4:
    print(f'Total: R$ {amount * 2:.2f}')

else:
    print(f'Total: R$ {amount * 1.5:.2f}')
