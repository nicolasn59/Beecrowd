# SUBPROGRAM
def lottery():
    sum = countCaw = 0
    while countCaw != 3:
        crow = input()
        if crow == "caw caw":
            print("%d" % sum)
            sum = 0
            countCaw += 1
        elif crow == "--*":
            sum += 1
        elif crow == "-*-":
            sum += 2
        elif crow == "-**":
            sum += 3
        elif crow == "*--":
            sum += 4
        elif crow == "*-*":
            sum += 5
        elif crow == "**-":
            sum += 6
        else:
            sum += 7
    return None

# MAIN
lottery()
