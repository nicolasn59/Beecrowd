Hi, Hf = map(int, input().split())
if Hi > Hf:
    resultado = ((Hf + 24) - Hi)
elif Hi < Hf:
    resultado = (Hf - Hi)
else:
    resultado = 24
print('O JOGO DUROU %d HORA(S)' % resultado)
