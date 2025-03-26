# SUBPROGRAM
def filterDistance(studentList):
    distanceFilter = list()
    for _ in range(len(studentList)):
        minDistance = studentList[0]['distancia']
        index = 0
        for i in range(1, len(studentList)):
            if studentList[i]['distancia'] < minDistance:
                minDistance = studentList[i]['distancia']
                index = i
        distanceFilter += [studentList[index]]
        studentList.pop(index)
        if studentList == []:
            return distanceFilter


def filterDirection(distanceFilter):
    directionFilter = list()
    size = len(distanceFilter)
    for _ in range(size):
        minDistance = distanceFilter[0]['distancia']
        minDirection = distanceFilter[0]['direcao']
        index = 0
        for i in range(len(distanceFilter)):
            if distanceFilter[i]['direcao'] < minDirection and distanceFilter[i]['distancia'] == minDistance:
                minDirection = distanceFilter[i]['direcao']
                index = i
        directionFilter += [distanceFilter[index]]
        distanceFilter.pop(index)
        if distanceFilter == []:
            return directionFilter

def filterName(directionFilter):
    nameFilter = list()
    size = len(directionFilter)
    for _ in range(size):
        minDistance = directionFilter[0]['distancia']
        minDirection = directionFilter[0]['direcao']
        minName = directionFilter[0]['nome']
        index = 0
        for i in range(len(directionFilter)):
            if directionFilter[i]['nome'] < minName and directionFilter[i]['direcao'] == minDirection and directionFilter[i]['distancia'] == minDistance:
                minName = directionFilter[i]['nome']
                index = i
        nameFilter += [directionFilter[index]]
        directionFilter.pop(index)
        if directionFilter == []:
            return nameFilter


# MAIN PROGRAM
stop = False
while stop == False:
    try:
        presentStudents = int(input())
        studentList = list()
        for i in range(presentStudents):
            student = dict()
            student['nome'], student['direcao'], student['distancia'] = input().split()
            studentList.append(student)
    except EOFError:
        stop = True
    else:
        for i in range(len(studentList)):
            studentList[i]['distancia'] = int(studentList[i]['distancia'])
        distanceFiltered = filterDistance(studentList)
        directionFiltered = filterDirection(distanceFiltered)
        bestRoutes = filterName(directionFiltered)
        for route in bestRoutes:
            print(route['nome'])