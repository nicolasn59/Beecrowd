gols_time1 = 0
gols_time2 = 0
numero_teste = int(input())
for _ in range(numero_teste):

    #RODADA DE IDA (TIME 2 VISITANTE)

    placar_time1_mandante, x, placar_time2_visitante = map(str, input().split())
    gols_time1 += int(placar_time1_mandante)
    gols_time2 += int(placar_time2_visitante)

    # RODADA DE VOLTA (TIME 1 VISITANTE)

    placar_time2_mandante, x, placar_time1_visitante = map(str, input().split())
    gols_time1 += int(placar_time1_visitante)
    gols_time2 += int(placar_time2_mandante)

    if gols_time1 > gols_time2:
        print('Time 1')
    elif gols_time2 > gols_time1:
        print('Time 2')
    else:
        if placar_time1_visitante > placar_time2_visitante:
            print('Time 1')
        elif placar_time2_visitante > placar_time1_visitante:
            print('Time 2')
        else:
            print('Penaltis')

    gols_time1 = 0
    gols_time2 = 0
