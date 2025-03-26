#include <stdio.h>
int main()
{
    int tests, PA, PB, counter;
    double GA, GB;
    scanf("%d", &tests);
    while (tests != 0)
    {
        counter = 0;
        scanf("%d %d %lf %lf", &PA, &PB, &GA, &GB);
            while (PA <= PB)
            {
                PA += (PA * (GA / 100.0));
                PB += (PB * (GB / 100.0));
                counter += 1;
                if (counter > 100)
                    PA = (PB + 1);
            }
        if (counter > 100)
            printf("Mais de 1 seculo.\n");
        else
            printf("%d anos.\n", counter);
        tests -= 1;
    }
    return 0;
}
