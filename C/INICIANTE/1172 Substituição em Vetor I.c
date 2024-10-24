#include <stdio.h>

int main()
{
    int num, i, vetor[10];
    for (i=0; i != 10; i++)
    {
        scanf("%d", &num);
        if (num <= 0)
            vetor[i] = 1;
        else
            vetor[i] = num;
    }
    for (i=0; i != 10; i++)
    {
        printf("X[%d] = %d\n", i, vetor[i]);
    }
    return 0;
}
