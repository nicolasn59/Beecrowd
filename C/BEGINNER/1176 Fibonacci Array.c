#include <stdio.h>

int main()
{
    unsigned long long vector[60], tests, num, previousValue, secondPreviousValue, currentValue, count;

    scanf("%llu", &tests);
    while (tests != 0)
    {
        vector[0] = 0;
        vector[1] = 1;
        secondPreviousValue = 0;
        previousValue = 1;
        scanf("%llu", &num);
        count = 2;
        if (num > 1)
        {
            while (count != (num + 1))
            {
                currentValue = 0;
                currentValue = secondPreviousValue + previousValue;
                vector[count] = currentValue;
                secondPreviousValue = previousValue;
                previousValue = currentValue;
                count += 1;
            }
        }
        printf("Fib(%llu) = %llu\n", num, vector[num]);
        tests -= 1;
    }
    return 0;
}