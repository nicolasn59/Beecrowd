#include <stdio.h>

int main()
{
    double v1, v2, v3, v4, v5, v6, media, somaPositivos=0;
    int NumPositivos=0;
    scanf("%lf", &v1);
    scanf("%lf", &v2);
    scanf("%lf", &v3);
    scanf("%lf", &v4);
    scanf("%lf", &v5);
    scanf("%lf", &v6);

    if (v1 > 0)
    {
        somaPositivos += v1;
        NumPositivos += 1;
    }
    if (v2 > 0)
    {
        somaPositivos += v2;
        NumPositivos += 1;
    }
    if (v3 > 0)
    {
        somaPositivos += v3;
        NumPositivos += 1;
    }
    if (v4 > 0)
    {
        somaPositivos += v4;
        NumPositivos += 1;
    }
    if (v5 > 0)
    {
        somaPositivos += v5;
        NumPositivos += 1;
    }
    if (v6 > 0)
    {
        somaPositivos += v6;
        NumPositivos += 1;
    }
    
    media = (somaPositivos / NumPositivos);

    printf("%d valores positivos\n", NumPositivos);
    printf("%.1lf\n", media);
    return 0;
}
