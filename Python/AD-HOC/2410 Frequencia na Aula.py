# SUBPROGRAM
# MAIN PROGRAM
records = list()
numRecords = int(input())
for record in range(numRecords):
    records += [int(input())]
print(len(list(set(records))))