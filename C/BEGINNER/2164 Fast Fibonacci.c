#include <stdio.h>
#include <math.h>

double fastFibonacci(double exponent);

int main()
{
    double n;
    scanf("%lf", &n);
    fastFibonacci(n);
    return 0;
}

double fastFibonacci(double exponent)
{
    double fibonacci, base1, base2;
    base1 = (1.0+sqrt(5.0))/2.0;
    base2 = (1.0-sqrt(5.0))/2.0;
    fibonacci = (pow(base1, exponent) - pow(base2, exponent))/sqrt(5.0);
    printf("%.1lf\n", fibonacci);
    return 1.0;
}