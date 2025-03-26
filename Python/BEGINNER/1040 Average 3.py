n1, n2, n3, n4 = map(float, input().split())

total_average = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

if total_average >= 7.0:
    print('Media: %.1f' % total_average)
    print('Aluno aprovado.')
elif total_average < 5.0:
    print('Media: %.1f' % total_average)
    print('Aluno reprovado.')
else:
    print("Media: %.1f" % total_average)
    print('Aluno em exame.')

    new_score = float(input())
    print('Nota do exame: %.1f' % new_score)
    final_average = (new_score + total_average) / 2

    if final_average >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % final_average)
