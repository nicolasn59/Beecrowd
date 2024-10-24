#include <stdio.h>

int main()
{
    double f1, f2;
    scanf("%lf %lf", &f1, &f2);
    printf("%.6lf\n", ((((1+(f1/100)) * (1+(f2/100)))-1)*100));
    return 0;
}
