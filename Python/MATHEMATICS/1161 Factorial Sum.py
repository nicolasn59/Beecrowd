# SUBPROGRAM
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


# MAIN PROGRAM
while True:
    try:
        num1, num2 = map(int, input().split())
        print(factorial(num1) + factorial(num2))
    except EOFError:
        break