#include <stdio.h>

int main()
{
    int x, sum, repetition, count;
    scanf("%d", &x);
    while (x != 0)
    {
        sum = 0;
        repetition = 5;
        if (x % 2 == 0)
            {
                count = x;
                while (repetition != 0)
                {
                    sum += count;
                    count += 2;
                    repetition -= 1;
                }
            }
        else
        {
            count = (x + 1);
            while (repetition != 0)
            {
                sum += count;
                count += 2;
                repetition -= 1;
            }
        }
        printf("%d\n", sum);
        scanf("%d", &x);
    }
    return 0;
}