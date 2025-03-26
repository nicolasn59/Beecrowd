#include <stdio.h>
int main()
{
    int odd[5], even[5], i, j, countOdd, countEven, num;
    countEven = countOdd = 0;
    for (j = 0; j < 15; j++)
    {
        scanf("%d", &num);
        if (num % 2 == 0)
        {
            if (countEven == 5)
            {
                for (i = 0; i < 5; i++)
                {
                    printf("par[%d] = %d\n", i, even[i]);
                    countEven = 0;
                }
            }
            even[countEven] = num;
            countEven += 1;
        }
        else
        {
            if (countOdd == 5)
            {
                for (i = 0; i < 5; i++)
                {
                    printf("impar[%d] = %d\n", i, odd[i]);
                    countOdd = 0;
                }
            }
            odd[countOdd] = num;
            countOdd += 1;
        }
    }
    for (i = 0; i < countOdd; i++)
        printf("impar[%d] = %d\n", i, odd[i]);
    for (i = 0; i < countEven; i++)
        printf("par[%d] = %d\n", i, even[i]);
    return 0;
}