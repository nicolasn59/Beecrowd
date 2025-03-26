#include <stdio.h>

int main()
{
    int x, z, sum = 1, count;
    scanf("%d", &x);
    scanf("%d", &z);
    while (z <= x)
        scanf("%d", &z);
    count = (x + 1);
    while (x <= z)
    {
        x += count;
        sum += 1;
        count += 1;
    }
    printf("%d\n", sum);
    return 0;
}