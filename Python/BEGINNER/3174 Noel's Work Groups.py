# SUBPROGRAM
def PresentProduction(numElves):
    sumDolls = sumArchitects = sumMusicians = sumDesigners = 0
    for i in range(numElves):
        name, profession, workTime = input().split()
        if profession == "bonecos":
            sumDolls += int(workTime)
        elif profession == "arquitetos":
            sumArchitects += int(workTime)
        elif profession == "musicos":
            sumMusicians += int(workTime)
        else:
            sumDesigners += int(workTime)
    print("%d" % ((sumDolls//8) + (sumArchitects//4) + (sumMusicians//6) + (sumDesigners//12)))
    return None

# MAIN
numberOfElves = int(input())
PresentProduction(numberOfElves)