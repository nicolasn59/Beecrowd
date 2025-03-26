# SUBPROGRAM
def calculateArrivalTime(departure, travelTime, timeZone):
    if (departure + travelTime + timeZone) >= 24:
        print("%d" % ((departure + travelTime + timeZone) - 24))
    elif (departure + travelTime + timeZone) < 0:
        print("%d" % ((departure + travelTime + timeZone) + 24))
    else:
        print("%d" % (departure + travelTime + timeZone))
    return None

# MAIN PROGRAM
departure, travelTime, timeZone = map(int, input().split())
calculateArrivalTime(departure, travelTime, timeZone)