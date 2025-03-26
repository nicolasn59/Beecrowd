# SUBPROGRAM
# MAIN PROGRAM
while True:
    try:
        arr = list(input().split())
        hours = int(arr[0][0])
        minutes = int((arr[0][2] + arr[0][3]))
        minutes = int(minutes)
        if ((hours <= 7) and (minutes == 0)) or (hours < 7):
            print("Atraso maximo: 0")
        else:
            if hours == 9:
                print("Atraso maximo: %d" % (60*2))
            elif hours == 8:
                print("Atraso maximo: %d" % (60+minutes))
            else:
                print("Atraso maximo: %d" % minutes)
    except EOFError:
        break