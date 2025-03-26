# SUBPROGRAM
def countPoints(rounds):
    p1 = p2 = 0
    while rounds != 0:
        n1, n2 = map(int, input().split())
        if n1 > n2:
            p1 += 1
        elif n2 > n1:
            p2 += 1
        rounds -= 1
    print(p1, p2)
    return None


# MAIN PROGRAM
rounds = int(input())
while rounds != 0:
    countPoints(rounds)
    rounds = int(input())