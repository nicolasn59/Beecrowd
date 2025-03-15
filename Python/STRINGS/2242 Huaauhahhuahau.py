# SUBPROGRAMA
# PROGRAMA PRINCIPAL
palavra = input()
apenasVogais = list()
for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        apenasVogais += [letra]
risada = ''.join(apenasVogais)
if risada == risada[::-1]:
    print('S')
else:
    print('N')
