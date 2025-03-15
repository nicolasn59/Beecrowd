#include <stdio.h>

int main()
{
    int i;
    double num, vetor[100];
    for (i=0; i<100; i++)
    {
        scanf("%lf", &num);
        vetor[i] = num;
    }
    for (i=0; i<100; i++)
    {
        if (vetor[i] <= 10)
            printf("A[%d] = %.1lf\n", i, vetor[i]);
    }
    return 0;
}
