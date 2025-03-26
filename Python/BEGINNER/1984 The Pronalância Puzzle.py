# SUBPROGRAM
# MAIN PROGRAM
number = int(input())
numberString = list()
for num in str(number):
    numberString += [num]
print(''.join(numberString[::-1]))