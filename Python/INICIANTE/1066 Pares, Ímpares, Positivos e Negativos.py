contPar = contImpar = contPositivo = contNegativo = 0
for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        contPar += 1
    else:
        contImpar += 1
    if numero > 0:
        contPositivo += 1
    if numero < 0:
        contNegativo += 1
print('%d valor(es) par(es)' % contPar)
print('%d valor(es) impar(es)' % contImpar)
print('%d valor(es) positivo(s)' % contPositivo)
print('%d valor(es) negativo(s)' % contNegativo)
