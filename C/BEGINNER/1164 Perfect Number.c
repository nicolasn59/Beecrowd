#include <stdio.h>

int main()
{
    int tests, n, i, sum;
    scanf("%d", &tests);
    while (tests != 0)
    {
        sum = 0;
        scanf("%d", &n);
        for (i = 1; i != n; i++)
        {
            if (n % i == 0)
                sum += i;
        }
        if (sum == n)
            printf("%d eh perfeito\n", n);
        else
            printf("%d nao eh perfeito\n", n);
        tests -= 1;
    }
    return 0;
}