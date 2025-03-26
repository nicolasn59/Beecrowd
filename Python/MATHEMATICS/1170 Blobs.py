# SUBPROGRAM
def days_with_food():
    days = 0
    food_amount = float(input())

    if food_amount == 1:
        return days

    while food_amount > 1:
        food_amount //= 2
        days += 1
    return days

# MAIN PROGRAM

num_tests = int(input())
for _ in range(num_tests):
    result = days_with_food()
    print('%d %s' % (result, 'dias'))