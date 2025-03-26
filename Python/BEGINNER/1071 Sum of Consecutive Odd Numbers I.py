x = int(input())
y = int(input())
sum = 0
if y > x:
    for num in range(x+1, y):
        if num % 2 != 0:
            sum += num
else:
    for num in range(x-1, y, -1):
        if num % 2 != 0:
            sum += num
print(sum)
