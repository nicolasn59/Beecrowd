# op = option

op1 = input()
op2 = input()
op3 = input()

if op1 == 'vertebrado':
    if op2 == 'ave':
        if op3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if op3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if op2 == 'inseto':
        if op3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if op3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
