start_hour, final_hour = map(int, input().split())
if start_hour > final_hour:
    result = ((final_hour + 24) - start_hour)
elif start_hour < final_hour:
    result = (final_hour - start_hour)
else:
    result = 24
print('O JOGO DUROU %d HORA(S)' % result)
