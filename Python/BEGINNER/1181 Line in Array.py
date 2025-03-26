# SUBPROGRAM
def create_array():
	my_array = []
	for col in range(12):
		row = []
		for lin in range(12):
			row.append(float(input()))
		my_array.append(row)
	return my_array


def sum_a_row(op_row, my_array):
	row_sum = 0
	for col in range(len(my_array)):
		row_sum += my_array[op_row][col]
	return row_sum


def average_a_row(op_row, my_array):
	row_sum = sum_a_row(op_row, my_array)
	row_average = row_sum / len(my_array[op_row])
	return row_average


# MAIN
operation_row = int(input())
operation = input()
array = create_array()
if operation == 'S':
	sum = sum_a_row(operation_row, array)
	print('%.1f' % sum)
else:
	average = average_a_row(operation_row, array)
	print('%.1f' % average)
