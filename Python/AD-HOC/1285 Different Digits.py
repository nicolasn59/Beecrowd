# Subprogram
def count_digits(i, f):
    numbers = []
    count = 0
    while True:
        start_string = str(i)
        for digit in start_string:
            if digit in numbers:
                break
            else:
                numbers.append(digit)
        if len(numbers) == len(start_string):
            count += 1
        if i == f:
            break
        i += 1
        numbers.clear()

    return count


# Main Program
while True:
    try:
        n, m = map(int, input().split())   #N = START VALUE, M = END VALUE
        print(count_digits(n, m))
    except EOFError:
        break