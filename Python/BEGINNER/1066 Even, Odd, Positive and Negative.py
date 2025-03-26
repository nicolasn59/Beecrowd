even_cont = odd_cont = positive_cont = negative_cont = 0
for i in range(5):
    number = int(input())
    if number % 2 == 0:
        even_cont += 1
    else:
        odd_cont += 1
    if number > 0:
        positive_cont += 1
    if number < 0:
        negative_cont += 1
print('%d valor(es) par(es)' % even_cont)
print('%d valor(es) impar(es)' % odd_cont)
print('%d valor(es) positivo(s)' % positive_cont)
print('%d valor(es) negativo(s)' % negative_cont)
