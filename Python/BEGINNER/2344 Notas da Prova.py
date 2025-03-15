n = int(input())
if n == 0:
    print('E')
elif 0 < n <= 35:
    print('D')
elif 35 < n <= 60:
    print('C')
elif 60 < n <= 85:
    print('B')
else:
    print('A')
