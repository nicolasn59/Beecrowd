a, b, c, d = map(int, input().split())
if (a+b > c) == True and (a+c > b) == True and (b+c > a) == True:
    print('S')
elif (a+b > d) == True and (a+d > b) == True and (b+d > a) == True:
    print('S')
elif (a+c > d) == True and (a+d > c) == True and (c+d > a) == True:
    print('S')
elif (b+c > d) == True and (b+d > c) == True and (c+d > b) == True:
    print('S')
else:
    print('N')
