#include <stdio.h>

int main()
{
    double v1, v2, v3, v4, v5, v6, average, sumPositives = 0;
    int numPositives = 0;
    scanf("%lf", &v1);
    scanf("%lf", &v2);
    scanf("%lf", &v3);
    scanf("%lf", &v4);
    scanf("%lf", &v5);
    scanf("%lf", &v6);

    if (v1 > 0)
    {
        sumPositives += v1;
        numPositives += 1;
    }
    if (v2 > 0)
    {
        sumPositives += v2;
        numPositives += 1;
    }
    if (v3 > 0)
    {
        sumPositives += v3;
        numPositives += 1;
    }
    if (v4 > 0)
    {
        sumPositives += v4;
        numPositives += 1;
    }
    if (v5 > 0)
    {
        sumPositives += v5;
        numPositives += 1;
    }
    if (v6 > 0)
    {
        sumPositives += v6;
        numPositives += 1;
    }
    
    average = (sumPositives / numPositives);

    printf("%d valores positivos\n", numPositives);
    printf("%.1lf\n", average);
    return 0;
}
