case = 1
while True:
    try:
        sequence = []
        countSequence = 0
        sequenceSize = int(input())

        while True:
            if countSequence >= sequenceSize and sequenceSize != 0:
                break
            while countSequence < sequenceSize:
                sequence.append(sequenceSize)
                countSequence += 1
            sequenceSize -= 1
            countSequence = 0

        sequence.append(0)
        sortedSequence = sorted(sequence)
        sequenceString = (str(number) for number in sortedSequence)
        sequenceString = ' '.join(sequenceString)

    except EOFError:
        break
    else:
        if len(sortedSequence) <= 2:
            print('Caso %d: %d numero' % (case, len(sortedSequence)))
        else:
            print('Caso %d: %d numeros' % (case, len(sortedSequence)))
        print(sequenceString)
        case += 1
        print()