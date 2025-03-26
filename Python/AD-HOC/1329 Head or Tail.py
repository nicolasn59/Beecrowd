numTests = int(input())

while numTests != 0:
    plays = list(map(int, input().split()))
    john = mary = 0

    for value in plays:
        if value == 0:
            mary += 1
        else:
            john += 1

    print('Mary won %d times and John won %d times' % (mary, john))
    numTests = int(input())