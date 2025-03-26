#include <stdio.h>
int main()
{
    int num, i, count, originalVector[20], modifiedVector[20];
    for (i = 0; i < 20; i++)
    {
        scanf("%d", &num);
        originalVector[i] = num;
    }
    count = 19;
    for (i = 0; i < 10; i++)
    {
        modifiedVector[i] = originalVector[count];
        modifiedVector[count] = originalVector[i];
        count -= 1;
    }
    for (i = 0; i < 20; i++)
        printf("N[%d] = %d\n", i, modifiedVector[i]);
    return 0;
}
