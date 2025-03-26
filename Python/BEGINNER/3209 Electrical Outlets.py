# SUBPROGRAM
def ConnectedDevices(filters):
    total = 0
    for j in range(1, filters[0]+1):
        total += (filters[j]-1)
    print("%d" % (total+1))
    return None


# MAIN
numTests = int(input())
for i in range(numTests):
    powerStrip = list(map(int, input().split()))
    ConnectedDevices(powerStrip)