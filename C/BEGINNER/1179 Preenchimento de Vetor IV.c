#include <stdio.h>
int main()
{
    int impar[5], par[5], i, j, contImpar, contPar, num;
    contPar = contImpar = 0;
    for (j = 0; j < 15; j++)
    {
        scanf("%d", &num);
        if (num % 2 == 0)
        {
            if (contPar == 5)
            {
                for (i=0; i<5; i++)
                {
                    printf("par[%d] = %d\n", i, par[i]);
                    contPar = 0;
                }
            }
            par[contPar] = num;
            contPar += 1;
        }
        else
        {
            if (contImpar == 5)
            {
                for (i = 0; i < 5; i++)
                {
                    printf("impar[%d] = %d\n", i, impar[i]);
                    contImpar = 0;
                }
            }
            impar[contImpar] = num;
            contImpar += 1;
        }
    }
    for (i=0; i < contImpar; i++)
        printf("impar[%d] = %d\n", i, impar[i]);
    for (i=0; i<contPar; i++)
        printf("par[%d] = %d\n", i, par[i]);
    return 0;
}
