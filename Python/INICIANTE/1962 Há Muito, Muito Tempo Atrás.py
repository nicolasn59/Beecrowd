testes = int(input())
while testes != 0:
    ano = int(input())
    if ano >= 2015:
        print("%d A.C." % (ano - (2015-1)))
    else:
        print("%d D.C." % (2015 - ano))
    testes -= 1
