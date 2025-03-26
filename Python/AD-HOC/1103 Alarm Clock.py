# MAIN
hi, mi, hf, mf = list(map(int, input().split()))
while hi != 0 or mi != 0 or hf != 0 or mf != 0:
    if mf <= mi and hf <= hi:
        sleepMinutes = (((hf + 24) * 60) + mf) - ((hi * 60) + mi)
        print(sleepMinutes)
    elif mf > mi and hf < hi:
        sleepMinutes = (((hf + 24) * 60) + mf) - ((hi * 60) + mi)
        print(sleepMinutes)
    else:
        mi += hi * 60
        mf += hf * 60
        sleepMinutes = abs(mf - mi)
        print(sleepMinutes)

    hi, mi, hf, mf = list(map(int, input().split()))