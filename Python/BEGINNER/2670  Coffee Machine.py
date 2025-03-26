A1 = int(input())
A2 = int(input())
A3 = int(input())

cafeFirstFloor = ((A2*2) + (A3*4))
cafeSecondFloor = ((A1*2)+(A3*2))
cafeThirdFloor = ((A1*4)+(A2*2))

minTime = cafeFirstFloor
if cafeSecondFloor < minTime:
    minTime = cafeSecondFloor
if cafeThirdFloor < minTime:
    minTime = cafeThirdFloor
print(minTime)