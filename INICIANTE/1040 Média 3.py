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
