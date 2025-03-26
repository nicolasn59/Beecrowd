#include <stdio.h>

int main()
{
    int num, i, vector[10];
    for (i = 0; i != 10; i++)
    {
        scanf("%d", &num);
        if (num <= 0)
            vector[i] = 1;
        else
            vector[i] = num;
    }
    for (i = 0; i != 10; i++)
    {
        printf("X[%d] = %d\n", i, vector[i]);
    }
    return 0;
}