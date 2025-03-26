start = end = 0
x = int(input())
y = int(input())
start = x if x < y else y
end = x if x > y else y
for num in range(start+1, end):
	if num % 5 == 2 or num % 5 == 3:
		print(num)
