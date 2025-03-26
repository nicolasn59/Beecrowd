#include <stdio.h>

int main()
{
    int vector[1000], num, i, count;
    scanf("%d", &num);
    count = 0;
    for (i = 0; i < 1000; i++)
    {
        vector[i] = count;
        count += 1;
        if (count == num)
            count = 0;
    }
    for (i = 0; i < 1000; i++)
    {
        printf("N[%d] = %d\n", i, vector[i]);
    }
    return 0;
}