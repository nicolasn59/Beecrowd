count = distance = 0
while True:
    try:
        name = input()
        distance += int(input())
        count += 1
        average = distance / count

    except EOFError:
        print("%.1f" % average)
        break