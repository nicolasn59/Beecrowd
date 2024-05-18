# PRINCIPAL
hi, mi, hf, mf = list(map(int, input().split()))
while hi != 0 or mi != 0 or hf != 0 or mf != 0:
    if mf <= mi and hf <= hi:
        minutos_sono = (((hf + 24) * 60) + mf) - ((hi * 60) + mi)
        print(minutos_sono)
    elif mf > mi and hf < hi:
        minutos_sono = (((hf + 24) * 60) + mf) - ((hi * 60) + mi)
        print(minutos_sono)
    else:
        mi += hi * 60
        mf += hf * 60
        minutos_sono = abs(mf - mi)
        print(minutos_sono)

    hi, mi, hf, mf = list(map(int, input().split()))
