#include <stdio.h>
int main()
{
    double s, divisor, dividend;
    s = 1.0;
    divisor = 3.0;
    dividend = 2.0;
    while (divisor < 39.0)
    {
        s += (divisor / dividend);
        divisor += 2.0;
        dividend *= 2.0;
    } 
    printf("%.2lf\n", s);
    return 0;
}