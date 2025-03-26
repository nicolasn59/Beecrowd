#include <stdio.h>

int main()
{
    int v1, v2, min, max, count, sum = 0;
    scanf("%d %d", &v1, &v2);
    while (v1 > 0 && v2 > 0)
    {
        if (v1 > v2)
        {
            max = v1;
            min = v2;
        }
        else
        {
            max = v2;
            min = v1;
        }
        count = min;
        while (count != (max + 1))
        {
            printf("%d ", count);
            sum += count;
            count += 1;
        }
        printf("Sum=%d\n", sum);
        sum = 0;
        scanf("%d %d", &v1, &v2);
    }
    return 0;
}
