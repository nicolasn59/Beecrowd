#include <stdio.h>

int main()
{
    int x, y, max, min, count;
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
    count = (min + 1);

    while (count != max)
    {
        if (count % 5 == 2 || count % 5 == 3)
            printf("%d\n", count);
        count += 1;
    }
    return 0;
}