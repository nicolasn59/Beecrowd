a, b, c = map(int, input().split())
maiorAB = (a+b+abs(a-b))/2
if maiorAB > c:
    print(f'{maiorAB:.0f} eh o maior')
else:
    print(f'{c} eh o maior')
