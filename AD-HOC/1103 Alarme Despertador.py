# ENTRADA COM VARIOS CASOS DE TESTE
# RECEBER OS 4 HORÁRIOS: HI, MI, HF, MF
# CASO OS 4 HORÁRIOS SEJAM IGUAIS A 0, FINALIZA O PROGRAMA
# PASSO 1: TRANSFORMAR AS HORAS EM MINUTOS E SOMAR ENTRE INICIAIS E FINAIS
# PASSO 2: FAZER A DIFERENÇA ENTRE OS MINUTOS INICIAS E FINAIS (USAR UM ABS PARA UM RESULTADO ABSOLUTO)
# CASO A HORA FINAL SEJA MAIOR QUE A HORA INICIAL:
# PASSO 1: ADIONAR 24 A HORA FINAL E CONVERTER AMBAS HORAS PARA MINUTOS
# PASSO 2: SOMAR MINUTO ENTRE OS INICIAS E FINAIS
# PASSO 3: FAZER A DIFERENÇA ENTRE ELES
# SUBPROGRAMA

# PRINCIPAL

hi, mi, hf, mf = list(map(int, input().split()))
while hi != 0 or mi != 0 or hf != 0 or mf != 0:
    if mf <= mi and hf <= hi:
        minutos_sono = (((hf + 24) * 60) + mf) - ((hi * 60) + mi)
        print(minutos_sono)
    elif mf > mi and hf < hi:
        minutos_sono = (((hf + 24) * 60) + mf) - ((hi * 60) + mi)
        print(minutos_sono)
    else:
        mi += hi * 60
        mf += hf * 60
        minutos_sono = abs(mf - mi)
        print(minutos_sono)

    hi, mi, hf, mf = list(map(int, input().split()))
