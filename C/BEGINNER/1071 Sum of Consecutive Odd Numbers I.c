#include <stdio.h>

int main()
{
    int x, y, count, sum = 0;
    scanf("%d", &x);
    scanf("%d", &y);
    if (x > y)
    {
        count = (y + 1);
        while (count != x)
        {
            if (count % 2 != 0)
                sum += count;
            count += 1;

        }
    }
    else
    {
        count = (x + 1);
        while (count != y)
        {
            if (count % 2 != 0)
                sum += count;
            count += 1;
        }
    }
    printf("%d\n", sum);
    return 0;
}
