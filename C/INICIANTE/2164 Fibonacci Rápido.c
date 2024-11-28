#include <stdio.h>
#include <math.h>

double fibonacciRapido(double expoente);

int main()
{
    double n;
    scanf("%lf", &n);
    fibonacciRapido(n);
    return 0;
}

double fibonacciRapido(double expoente)
{
    double fibonacci, base1, base2;
    base1 = (1.0+sqrt(5.0))/2.0;
    base2 = (1.0-sqrt(5.0))/2.0;
    fibonacci = (pow(base1, expoente) - pow(base2, expoente))/sqrt(5.0);
    printf("%.1lf\n", fibonacci);
    return 1.0;
}

