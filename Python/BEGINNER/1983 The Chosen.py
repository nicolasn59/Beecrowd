# SUBPROGRAM
# MAIN PROGRAM
highest = 0
students = int(input())
while students != 0:
    registration, grade = map(float, input().split())
    int(registration)
    if highest < grade:
        highest = grade
        approved = registration
    students -= 1
if highest < 8:
    print("Minimum note not reached")
else:
    print("%d" % approved)