#include <stdio.h>
int main()
{
    int num, i, vetor[10];
    scanf("%d", &num);
    for (i=0; i < 10; i++)
        {
            vetor[i] = num;
            num *= 2;
        }
    for (i=0; i < 10; i++)
        printf("N[%d] = %d\n", i, vetor[i]);
    return 0;
}
