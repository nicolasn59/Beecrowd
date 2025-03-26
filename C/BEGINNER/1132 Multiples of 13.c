#include <stdio.h>

int main()
{
    int x, y, count, max, min, sumNonDivisors = 0;
    scanf("%d", &x);
    scanf("%d", &y);
    if (x > y)
    {
        max = x;
        min = y;
    }
    else
    {
        max = y;
        min = x;
    }
    count = min;
    while (count != (max + 1))
    {
        if (count % 13 != 0)
            sumNonDivisors += count;
        count += 1;
    }
    printf("%d\n", sumNonDivisors);
    return 0;
}