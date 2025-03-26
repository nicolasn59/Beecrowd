while True:
    try:
        numTests = int(input())
        for case in range(numTests):
            hits = 0
            actionList = []

            numShots = int(input())
            shotHeight = list(map(int, input().split()))
            playerAction = input()

            actionList = [char for char in playerAction]

            for position in range(numShots):
                if shotHeight[position] <= 2 and playerAction[position] == "S":
                    hits += 1
                elif shotHeight[position] > 2 and playerAction[position] == "J":
                    hits += 1
                else:
                    continue
            print(hits)

    except EOFError:
        break