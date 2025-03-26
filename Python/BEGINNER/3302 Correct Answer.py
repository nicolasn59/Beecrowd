numberOfQuestions = int(input())
count = 0
while count != numberOfQuestions:
    count += 1
    answer = int(input())
    print('resposta %d: %d' % (count, answer))