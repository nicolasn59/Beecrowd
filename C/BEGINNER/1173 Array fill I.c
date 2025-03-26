#include <stdio.h>
int main()
{
    int num, i, vector[10];
    scanf("%d", &num);
    for (i = 0; i < 10; i++)
        {
            vector[i] = num;
            num *= 2;
        }
    for (i = 0; i < 10; i++)
        printf("N[%d] = %d\n", i, vector[i]);
    return 0;
}