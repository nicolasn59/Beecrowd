n = int(input())
for i in range(n):
    score1, score2, score3 = map(float, input().split())
    print("%.1f" % (((score1 * 2) + (score2 * 3) + (score3 * 5)) / (2 + 3 + 5)))
