highest = position = 0
for i in range(1, 101):
	num = int(input())
	if highest == 0:
		highest = num
		position = i
	elif num > highest:
		highest = num
		position = i
print(highest)
print(position)
