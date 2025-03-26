#include <stdio.h>
#include <math.h>

long double factorial(long double num);
long double countZeros(long double num);

int main()
{
    long double number;
    scanf("%Lf", &number);
    printf("%.0Lf\n", countZeros(factorial(number)));
    return 0;
}

long double factorial(long double num)
{
    if (num == 1.0)
        return 1.0;
    else
        return num * factorial(num - 1.0);
}

long double countZeros(long double num)
{
    if ((num / 10.0) < 1)
        return 0;
    else
        if ((fmod(num, 10)) == 0)
            return 1.0 + countZeros(num / 10);
        else
            return countZeros(num / 10);
}