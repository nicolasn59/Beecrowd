#include <stdio.h>

int main(int argc, char const *argv[])
{
    int x, y, z, max, mid, min;
    scanf("%d %d %d", &x, &y, &z);

    if (x > y && x > z)
    {
        max = x;
        if (y > z)
        {
            mid = y;
            min = z;
        }
        else
        {
            mid = z;
            min = y;
        }
    }
    else if (y > x && y > z)
    {
        max = y;
        if (x > z)
        {
            mid = x;
            min = z;
        }
        else 
        {
            mid = z;
            min = x;
        }
    }
    else
    {
        max = z;
        if (x > y)
        {
            mid = x;
            min = y;
        }
        else
        {
            mid = y;
            min = x;
        }
    }

    printf("%d\n", min);
    printf("%d\n", mid);
    printf("%d\n", max);
    printf("\n");
    printf("%d\n", x);
    printf("%d\n", y);
    printf("%d\n", z);
    return 0;
}
