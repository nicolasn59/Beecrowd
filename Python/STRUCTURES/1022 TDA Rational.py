def convert_to_int(values):
    new_values = []
    for value in values:
        if value.isnumeric() == True:
            new_values.append(int(value))
        else:
            new_values.append(value)
    return new_values


def fraction_calculation(new_values):
    N1, D1, N2, D2 = new_values[0], new_values[2], new_values[4], new_values[6]
    operator = new_values[3]

    if operator == '+':
        numerator = ((N1 * D2) + (N2 * D1))
        denominator = (D1 * D2)

    elif operator == '-':
        numerator = ((N1 * D2) - (N2 * D1))
        denominator = (D1 * D2)

    elif operator == '*':
        numerator = (N1 * N2)
        denominator = (D1 * D2)

    else:
        numerator = (N1 * D2)
        denominator = (N2 * D1)


    simplified_numerator = numerator
    simplified_denominator = denominator
    num_list = [2, 3, 5, 7, 9]
    count = 1

    while True:

        if simplified_numerator == simplified_denominator:
            simplified_numerator = 1
            simplified_denominator = 1
            break

        for num in num_list:
            if simplified_numerator % num == 0 and simplified_denominator % num == 0:
                simplified_numerator //= num
                simplified_denominator //= num
                count -= 1
            else:
                count += 1

        if count > 5:
            break

    return f'{numerator}/{denominator} = {simplified_numerator}/{simplified_denominator}'


n = int(input())

for _ in range(n):
    values = list(map(str, input().split()))

    new_values = convert_to_int(values)
    result = fraction_calculation(new_values)

    print(result)