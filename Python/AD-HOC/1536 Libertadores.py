team1Goals = 0
team2Goals = 0
numTests = int(input())
for _ in range(numTests):

    # FIRST LEG (TEAM 2 AWAY)

    team1HomeScore, x, team2AwayScore = map(str, input().split())
    team1Goals += int(team1HomeScore)
    team2Goals += int(team2AwayScore)

    # SECOND LEG (TEAM 1 AWAY)

    team2HomeScore, x, team1AwayScore = map(str, input().split())
    team1Goals += int(team1AwayScore)
    team2Goals += int(team2HomeScore)

    if team1Goals > team2Goals:
        print('Time 1')
    elif team2Goals > team1Goals:
        print('Time 2')
    else:
        if team1AwayScore > team2AwayScore:
            print('Time 1')
        elif team2AwayScore > team1AwayScore:
            print('Time 2')
        else:
            print('Penaltis')

    team1Goals = 0
    team2Goals = 0