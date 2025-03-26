tests = int(input())
while tests != 0:
    year = int(input())
    if year >= 2015:
        print("%d A.C." % (year - (2015 - 1)))
    else:
        print("%d D.C." % (2015 - year))
    tests -= 1