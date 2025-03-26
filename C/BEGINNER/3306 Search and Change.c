#include <stdio.h>

int main()
{
    double factor1, factor2;
    scanf("%lf %lf", &factor1, &factor2);
    printf("%.6lf\n", ((((1+(factor1/100)) * (1+(factor2/100)))-1)*100));
    return 0;
}
