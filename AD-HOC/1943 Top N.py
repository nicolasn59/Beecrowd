posiçao = int(input())
if posiçao == 1:
    print('Top 1')
elif 1 < posiçao <= 3:
    print('Top 3')
elif 3 < posiçao <= 5:
    print('Top 5')
elif 5 < posiçao <= 10:
    print('Top 10')
elif 10 < posiçao <= 25:
    print('Top 25')
elif 25 < posiçao <= 50:
    print('Top 50')
else:
    print('Top 100')
