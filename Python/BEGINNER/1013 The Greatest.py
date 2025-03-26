a, b, c = map(int, input().split())
biggest_AB = (a+b+abs(a-b))/2
if biggest_AB > c:
    print(f'{biggest_AB:.0f} eh o maior')
else:
    print(f'{c} eh o maior')
