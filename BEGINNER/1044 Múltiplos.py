a, b = map(int, input().split())
if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
