#include <stdio.h>
int main()
{
    double vetor[100], num;
    int i;
    scanf("%lf", &num);
    for (i = 0; i < 100; i++)
    {
        vetor[i] = num;
        num /= 2;
    }
    for (i=0; i<100; i++)
        printf("N[%d] = %.4lf\n", i, vetor[i]);
    return 0;
}
