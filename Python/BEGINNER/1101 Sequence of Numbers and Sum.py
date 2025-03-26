def sum_of_sequence(num1, num2):
	biggest = smallest = sum = 0
	if num1 > num2:
		biggest = num1
		smallest = num2
	else:
		biggest = num2
		smallest = num1
	for i in range(smallest, biggest+1):
		print(i, end=' ')
		sum += i
	msg = 'Sum=%d' % sum
	return msg

value1, value2 = map(int, input().split())
while value1 > 0 and value2 > 0:
	adder = sum_of_sequence(value1, value2)
	print(adder)
	value1, value2 = map(int, input().split())
