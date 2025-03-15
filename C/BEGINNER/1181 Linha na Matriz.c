#include <stdio.h>
int main()
{
    int linhaDaOperacao, i, j;
    char operacao[2];
    double matriz[12][12], soma;
    soma = 0;
    scanf("%d %s", &linhaDaOperacao, operacao);
    for (i=0; i<12; i++)
        for (j=0; j<12; j++)
            scanf("%lf", &matriz[i][j]);
    for (i=0; i<12; i++)
        for (j=0; j<12; j++)
            if (i == linhaDaOperacao)
                soma += matriz[i][j];
    if (operacao[0] == 'S')
        printf("%.1lf\n", soma);
    else
        printf("%.1lf\n", (soma/12.0));
    return 0;
}
