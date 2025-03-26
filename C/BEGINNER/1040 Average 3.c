#include <stdio.h>

int main(int argc, char const *argv[])
{
    float n1, n2, n3, n4, average;
    scanf("%f %f %f %f", &n1, &n2, &n3, &n4);
    average = ((n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10);
    printf("Media: %.1f\n", average);
    if (average >= 7.0)
        printf("Aluno aprovado.\n");
    else if (average < 7.0 && average >= 5.0)
    {
        printf("Aluno em exame.\n");
        float n5;
        scanf("%f", &n5);
        printf("Nota do exame: %.1f\n", n5);
        if (((average + n5) / 2) >= 5.0)
            printf("Aluno aprovado.\n");
        else
            printf("Aluno reprovado.\n");
        printf("Media final: %.1f\n", ((average + n5) / 2));
    }
    else
        printf("Aluno reprovado.\n");
    return 0;
}
