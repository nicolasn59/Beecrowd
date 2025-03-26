#include <stdio.h>
#include <math.h>

int main()
{
    double value, installments;
    scanf("%lf", &value);
    scanf("%lf", &installments);
    int count = 0;
    for (int i = 0; i < (int) installments; i++)
    {
        if (count < (fmod(value, installments)))
        {
            printf("%0.lf\n", ceil(value / installments));
            count += 1;
        }
        else
            printf("%0.lf\n", trunc(value / installments));
    }
    return 0;
}