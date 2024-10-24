#include <stdio.h>
int main()
{
    double s, divisor, dividendo;
    s = 1.0;
    divisor = 3.0;
    dividendo = 2.0;
    while (divisor < 39.0)
    {
        s += (divisor/dividendo);
        divisor += 2.0;
        dividendo *= 2.0;
    } 
    printf("%.2lf\n", s);
    return 0;
}
