#algoritmo
# RECEBER AS 4 NOTAS DO ALUNO
# CALCULAR A MEDIA USANDO OS PESOS: 2, 3, 4, 1
# CRIAR AS CONDIÇÕES PARA O ALUNO
# NOTA >= 7.0 -> APROVADO
# NOTA ENTRE 5.0 E 6.9 ALUNO EM EXAME
# NOTA < 5.0 REPROVADO
# EM CASO DE EXAME:
# RECEBER NOVA NOTA, SOMAR COM A MÉDIA ANTERIOR E DIVIDIR POR 2
# IMPRIMIR RESULTADO

#SUBPROGRAMA

# PROGRAMA PRINCIPAL
n1, n2, n3, n4 = map(float, input().split())

media_total = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if media_total >= 7.0:
    print('Media: %.1f' % media_total)
    print('Aluno aprovado.')
elif media_total < 5.0:
    print('Media: %.1f' % media_total)
    print('Aluno reprovado.')
else:
    print("Media: %.1f" % media_total)
    print('Aluno em exame.')

    nova_nota = float(input())
    print('Nota do exame: %.1f' % nova_nota)
    media_final = (nova_nota + media_total) / 2

    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % media_final)
