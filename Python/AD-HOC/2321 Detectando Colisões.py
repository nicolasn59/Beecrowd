# indices:
# X0 = 0; X1 = 2
# Y0 = 1; Y1 = 3

count = 0
plane1 = list(map(int, input().split()))
plane2 = list(map(int, input().split()))

if (plane2[0] <= plane1[0] <= plane2[2]) or (plane2[0] <= plane1[2] <= plane2[2]) or (plane1[0] <= plane2[0] <= plane1[2]) or (plane1[0] <= plane2[2] <= plane1[2]): # X0
    count += 1
if (plane2[1] <= plane1[1] <= plane2[3]) or (plane2[1] <= plane1[3] <= plane2[3]) or (plane1[1] <= plane2[1] <= plane1[3]) or (plane1[1] <= plane2[3] <= plane1[3]): # Y0
    count += 1

if count >= 2:
    print(1)
else:
    print(0)