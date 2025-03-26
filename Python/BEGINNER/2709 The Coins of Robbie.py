while True:
    try:
        coinList = []
        sumCoins = count = 0

        coins = int(input())
        for _ in range(coins):
            coinList.append(int(input()))

        jump = int(input())
        for i in range(coins-1, -1, -jump):
            sumCoins += coinList[i]

        for number in range(1, sumCoins + 1):
            if sumCoins % number == 0:
                count += 1

        if count == 2:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError:
        break