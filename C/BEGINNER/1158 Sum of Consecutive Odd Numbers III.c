#include <stdio.h>
int main()
{
    int tests, x, y, sum, i, j, count;
    scanf("%d", &tests);
    sum = 0;
    for (i = 1; tests != 0; i++)
    {
        scanf("%d %d", &x, &y);
        if (x % 2 == 0)
        {
            count = (x + 1);
            for (j = 1; y != 0; j += 2)
            {
                sum += count;
                count += 2;
                y -= 1;
            }
        }
        else
        {
            count = x;
            for (j = 1; y != 0; j += 2)
            {
                sum += count;
                count += 2;
                y -= 1;
            }
        }
        tests -= 1;
        printf("%d\n", sum);
        sum = 0;
    }
    return 0;
}