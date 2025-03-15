#include <stdio.h>

int main()
{
    int vetor[1000], num, i, cont;
    scanf("%d", &num);
    cont = 0;
    for (i = 0; i < 1000; i++)
    {
        vetor[i] = cont;
        cont += 1;
        if (cont == num)
            cont = 0;
    }
    for (i = 0; i < 1000; i++)
    {
        printf("N[%d] = %d\n", i, vetor[i]);
    }
    return 0;
}
