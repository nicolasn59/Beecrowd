#include <stdio.h>
#include <math.h>

int verificarExistencia(int num, int len, int *numDaCombs)
{
    for (int i=0; i < len; i++)
        if (numDaCombs[i] == num)
        {
            return 1;
        }
    return 0;
}


int sorteio(int comb, int qtdBolas)
{
    int balls[qtdBolas];
    for (int i=0; i < qtdBolas; i++)
        scanf("%d", &balls[i]);

    int len=1, num, numDaCombs[comb];
    numDaCombs[0] = 0;
    for (int i=0; i < qtdBolas; i++)
    {
        for (int j=0; j < qtdBolas; j++)
        {
            num = abs(balls[i] - balls[j]);
            if (num <= comb)
            {
                if (verificarExistencia(num, len, numDaCombs) == 0) // SEM REPETIÇOES NO VETOR
                {
                    numDaCombs[len] = num;
                    len += 1;
                }
            }
            if (len == (comb+1)) // ECONOMIZAR TEMPO
            {
                printf("Y\n");
                return 0;
            }
        }
        if (len == (comb+1)) // ECONOMIZAR TEMPO
        {
            printf("Y\n");
            return 0;
        }
    }
    if (len == (comb+1)) // ECONOMIZAR TEMPO
    {
        printf("Y\n");
        return 0;
    }
    else
    {
        printf("N\n");
        return 0;
    }
}

int main()
{
    int combinacao, quantidadeDeBolas;
    scanf("%d %d", &combinacao, &quantidadeDeBolas);
    while ((combinacao != 0) || (quantidadeDeBolas != 0))
    {
        sorteio(combinacao, quantidadeDeBolas);
        scanf("%d %d", &combinacao, &quantidadeDeBolas);
    }

    return 0;
}
