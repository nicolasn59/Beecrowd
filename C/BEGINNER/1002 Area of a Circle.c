#include <stdio.h>

int main()
{
    double pi, radius, area;
    pi = 3.14159;
    scanf("%lf", &radius);
    area = (pi * (radius * radius));
    printf("A=%.4lf\n", (area));
    return 0;
}
