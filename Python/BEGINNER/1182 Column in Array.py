# SUBPROGRAM
def makeMatrix():
    myMatrix = []
    for col in range(12):
        row = []
        for lin in range(12):
            row.append(float(input()))
        myMatrix.append(row)
    return myMatrix


def sumColumn(columnOp, matrix):
    columnSum = 0
    for lin in range(len(matrix)):
        columnSum += matrix[lin][columnOp]
    return columnSum


def averageColumn(columnOp, matrix):
    columnSum = sumColumn(columnOp, matrix)
    columnAverage = columnSum / len(matrix)
    return columnAverage


# MAIN
operationColumn = int(input())
operation = input()
thisMatrix = makeMatrix()
if operation == 'S':
    sumResult = sumColumn(operationColumn, thisMatrix)
    print('%.1f' % sumResult)
else:
    averageResult = averageColumn(operationColumn, thisMatrix)
    print('%.1f' % averageResult)