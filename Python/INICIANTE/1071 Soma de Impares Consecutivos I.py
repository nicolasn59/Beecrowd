x = int(input())
y = int(input())
soma = 0
if y > x:
    for num in range(x+1, y):
        if num % 2 != 0:
            soma += num
else:
    for num in range(x-1, y, -1):
        if num % 2 != 0:
            soma += num
print(soma)