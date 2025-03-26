# SUBPROGRAM
def sumWorms(field, rows, cols):
    rowSum = colSum = maxSum = 0
    for row in range(rows):
        for col in range(cols):
            rowSum += field[row][col]
        if rowSum > maxSum:
            maxSum = rowSum
        rowSum = 0
    for col in range(cols):
        for row in range(rows):
            colSum += field[row][col]
            if colSum > maxSum:
                maxSum = colSum
        colSum = 0
    return maxSum

# MAIN PROGRAM
wormField = []
rows, cols = map(int, input().split())
for i in range(rows):
    cells = list(map(int, input().split()))
    wormField.append(cells)
totalWorms = sumWorms(wormField, rows, cols)
print(totalWorms)