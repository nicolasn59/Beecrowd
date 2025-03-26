#include <stdio.h>

int main()
{
    int tests, num, i, prime;
    scanf("%d", &tests);
    while (tests != 0)
    {
        prime = 0;
        scanf("%d", &num);
        for (i = 2; i != num; i++)
        {
            if (num % i == 0)
                prime += 1;
        }
        if (prime == 0)
            printf("%d eh primo\n", num);
        else
            printf("%d nao eh primo\n", num);
        tests -= 1;
    }
    return 0;
}