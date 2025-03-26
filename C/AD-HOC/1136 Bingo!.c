#include <stdio.h>
#include <math.h>

int checkExistence(int num, int len, int *numFromCombs)
{
    for (int i = 0; i < len; i++)
        if (numFromCombs[i] == num)
        {
            return 1;
        }
    return 0;
}

int draw(int comb, int numBalls)
{
    int balls[numBalls];
    for (int i = 0; i < numBalls; i++)
        scanf("%d", &balls[i]);

    int len = 1, num, numFromCombs[comb];
    numFromCombs[0] = 0;
    for (int i = 0; i < numBalls; i++)
    {
        for (int j = 0; j < numBalls; j++)
        {
            num = abs(balls[i] - balls[j]);
            if (num <= comb)
            {
                if (checkExistence(num, len, numFromCombs) == 0) // WITHOUT REPETITIONS IN THE ARRAY
                {
                    numFromCombs[len] = num;
                    len += 1;
                }
            }
            if (len == (comb + 1)) // SAVE TIME
            {
                printf("Y\n");
                return 0;
            }
        }
        if (len == (comb + 1)) // SAVE TIME
        {
            printf("Y\n");
            return 0;
        }
    }
    if (len == (comb + 1)) // SAVE TIME
    {
        printf("Y\n");
        return 0;
    }
    else
    {
        printf("N\n");
        return 0;
    }
}

int main()
{
    int combination, numBalls;
    scanf("%d %d", &combination, &numBalls);
    while ((combination != 0) || (numBalls != 0))
    {
        draw(combination, numBalls);
        scanf("%d %d", &combination, &numBalls);
    }

    return 0;
}
