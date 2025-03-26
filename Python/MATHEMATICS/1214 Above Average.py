# SUBPROGRAM
def calculateAverage(studentGrades):
    sumGrades = 0
    for i in range(len(studentGrades)):
        sumGrades += studentGrades[i]
    averageGrades = sumGrades/len(studentGrades)
    return averageGrades


def aboveAverage(studentGrades, averageGrades):
    counter = 0
    for i in range(len(studentGrades)):
        if studentGrades[i] > averageGrades:
            counter += 1
    print("%.3f%%" % ((100*counter)/len(studentGrades)))
    return None


# MAIN PROGRAM

classes = int(input())
while classes != 0:
    grades = list(map(int , input().split()[1:]))
    average = calculateAverage(grades)
    aboveAverage(grades, average)
    classes -= 1