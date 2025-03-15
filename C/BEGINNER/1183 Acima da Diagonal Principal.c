#include <stdio.h>
int main()
{
    int i, j, diagonal;
    char operacao[2];
    double matriz[12][12], soma, cont;
    soma = cont = diagonal = 0;
    scanf("%s ", operacao);
    for (i=0; i<12; i++)
        for (j=0; j<12; j++)
            scanf("%lf", &matriz[i][j]);
    for (i=0; i<12; i++)
    {
        for (j=0; j<12; j++)
        {
            if (j > diagonal)
            {
                soma += matriz[i][j];
                cont += 1;
            }
        }
        diagonal += 1;
    }
    if (operacao[0] == 'S')
        printf("%.1lf\n", soma);
    else
        printf("%.1lf\n", (soma/cont));
    return 0;
}
