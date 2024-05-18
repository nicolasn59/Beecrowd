#algoritmo
# RECEBER O DOIS HORÁRIOS(HORA INICIAL E HORA FINAL)
# DETERMINAR A HORA QUE PASSOU
# SE HI > HF, (HI - HF + 24)
# SE HI == HF, (24)
# SE HI < HF, (HF - HI)

# PROGRAMA PRINCIPAL
Hi, Hf = map(int, input().split())
if Hi > Hf:
    resultado = ((Hf + 24) - Hi)
elif Hi < Hf:
    resultado = (Hf - Hi)
else:
    resultado = 24
print('O JOGO DUROU %d HORA(S)' % resultado)
