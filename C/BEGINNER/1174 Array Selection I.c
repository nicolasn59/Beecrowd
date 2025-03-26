#include <stdio.h>

int main()
{
    int i;
    double num, vector[100];
    for (i = 0; i < 100; i++)
    {
        scanf("%lf", &num);
        vector[i] = num;
    }
    for (i = 0; i < 100; i++)
    {
        if (vector[i] <= 10)
            printf("A[%d] = %.1lf\n", i, vector[i]);
    }
    return 0;
}