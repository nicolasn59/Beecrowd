#include <stdio.h>

int main()
{
    int tamanhoDaMatriz, i , j, linhaInicial, linhaFinal, colunaInicial, colunaFinal, valor, valorMeio;
    scanf("%d", &tamanhoDaMatriz);
    while (tamanhoDaMatriz != 0)
    {
        linhaInicial = colunaInicial = 0;
        linhaFinal = colunaFinal = tamanhoDaMatriz-1;
        valor = 1;

        if (tamanhoDaMatriz % 2 == 0)
            valorMeio = tamanhoDaMatriz / 2;
        else
            valorMeio = (tamanhoDaMatriz + 1) / 2;

        int matriz[tamanhoDaMatriz][tamanhoDaMatriz];

        for (j=valor; j<=valorMeio; j++)
        {
            for (i=colunaInicial; i<=colunaFinal; i++)
            {
                matriz[linhaInicial][i] = valor;
                matriz[linhaFinal][i] = valor;
            }
            for (i=(linhaInicial+1); i<linhaFinal; i++)
            {
                matriz[i][colunaInicial] = valor;
                matriz[i][colunaFinal] = valor;
            }
            linhaFinal -= 1;
            colunaInicial += 1;
            linhaInicial += 1;
            colunaFinal -= 1;
            valor += 1;
        }

        // IMPRIMIR MATRIZ
        // char tx[2];
        for (i=0; i<tamanhoDaMatriz; i++)
        {
            for (j=0; j<tamanhoDaMatriz; j++)
            {
                
                if (tamanhoDaMatriz == 1)
                    printf("  %d\n", matriz[i][j]);
                else if (j == tamanhoDaMatriz-1)
                    printf("   %d\n", matriz[i][j]);
                else if (j == 0)
                    printf("  %d", matriz[i][j]);
                else
                    printf("   %d", matriz[i][j]);
            }
        }
        // printf("\n");
        scanf("%d", &tamanhoDaMatriz);
    }
    // printf("\n");
    return 0;
}
