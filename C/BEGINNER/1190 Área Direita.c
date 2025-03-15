#include <stdio.h>

int main()
{
    int i, j, diagonalPrincipal, diagonalSecundaria;
    char operacao[2];
    double matriz[12][12], soma, cont;
    scanf("%s ", operacao);
    for (i=0; i<12; i++)
        for (j=0; j<12; j++)
            scanf("%lf", &matriz[i][j]);
    soma = cont = 0;
    diagonalPrincipal = 11;
    diagonalSecundaria = 0;
    for (i=0; i<12; i++)
    {
        for (j=0; j<12; j++)
        {
            if (i < 6 && j > diagonalPrincipal)
            {
                soma += matriz[i][j];
                cont += 1.0;
            }
            else if (i > 5 && j > diagonalSecundaria)
            {
                soma += matriz[i][j];
                cont += 1.0;
            }
        }
        diagonalPrincipal -= 1;
        diagonalSecundaria += 1;
    }
    if (operacao[0] == 'S')
        printf("%.1lf\n", soma);
    else
        printf("%.1lf\n", (soma/cont));
    return 0;
}