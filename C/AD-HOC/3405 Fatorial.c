#include <stdio.h>
#include <math.h>

long double fat(long double num);
long double contaZeros(long double num);

int main()
{
    long double number;
    scanf("%Lf", &number);
    printf("%.0Lf\n", contaZeros(fat(number)));
    return 0;
}

long double fat(long double num)
{
    if (num == 1.0)
        return 1.0;
    else
        return num * fat(num-1.0);
}

long double contaZeros(long double num)
{
    if ((num/10.0) < 1)
        return 0;
    else
        if ((fmod(num, 10)) == 0)
            return 1.0 + contaZeros(num/10);
        else
            return contaZeros(num/10);
}
