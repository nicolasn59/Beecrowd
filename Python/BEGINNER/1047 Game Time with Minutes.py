# hi = start hour
# hf = final hour
# mi = start minute
# mf = final minute


hi, mi, hf, mf = map(int, input().split())

if hf > hi or mf > mi or hf < hi or mf < mi or hf == hi or mf == mi:
    if hf > hi and mf > mi:
        print(f'O JOGO DUROU {hf - hi} HORA(S) E {(mf - mi)} MINUTO(S)')

    elif hf > hi and mf < mi:
        print(f'O JOGO DUROU {(hf - hi) - 1 if (hi+1) != hf else 0} HORA(S) E {60 - (mi - mf)} MINUTO(S)')

    elif hf < hi and mf > mi:
        print(f'O JOGO DUROU {24 - (hi - hf)} HORA(S) E {(mf - mi)} MINUTO(S)')

    elif hf < hi and mf < mi:
        print(f'O JOGO DUROU {(24 - (hi - hf)) - 1 if (hf + 1) != hi else (24 - (hi - hf))} HORA(S) E {60 - (mi - mf)} MINUTO(S)')

    elif hf == hi and mf == mi:
        print(f'O JOGO DUROU {24 - (hf - hi)} HORA(S) E {0} MINUTO(S)')

    elif hf == hi and mf > mi:
        print(f'O JOGO DUROU {0} HORA(S) E {(mf - mi)} MINUTO(S)')

    elif hf == hi and mf < mi:
        print(f'O JOGO DUROU {24 - 1} HORA(S) E {60 - (mi - mf)} MINUTO(S)')

    elif hf > hi and mf == mi:
        print(f'O JOGO DUROU {(hf - hi) + 1} HORA(S) E {0} MINUTO(S)')

    else:
        print(f'O JOGO DUROU {24 - (hi - hf)} HORA(S) E {0} MINUTO(S)')
