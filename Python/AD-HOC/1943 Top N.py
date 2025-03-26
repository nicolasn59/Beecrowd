position = int(input())
if position == 1:
    print('Top 1')
elif 1 < position <= 3:
    print('Top 3')
elif 3 < position <= 5:
    print('Top 5')
elif 5 < position <= 10:
    print('Top 10')
elif 10 < position <= 25:
    print('Top 25')
elif 25 < position <= 50:
    print('Top 50')
else:
    print('Top 100')