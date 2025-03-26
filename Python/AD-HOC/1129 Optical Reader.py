numQuestions = int(input())
while numQuestions != 0:
    count = 0

    for _ in range(numQuestions):
        averages = list(map(int, input().split())

        for index in range(len(averages)):

            if averages[index] == 0 or averages[index] <= 127:
                answer = index
                count += 1

        if count > 1 or count == 0:
            print('*')
            count = 0
        else:
            if answer == 0:
                print('A')
            elif answer == 1:
                print('B')
            elif answer == 2:
                print('C')
            elif answer == 3:
                print('D')
            else:
                print('E')

            count = 0

    numQuestions = int(input())