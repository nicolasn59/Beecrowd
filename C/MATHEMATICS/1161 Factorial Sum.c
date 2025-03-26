#include<stdio.h>

long double factorial(long double num);

int main()
{
    long double number1, number2;
    while (scanf("%Lf %Lf", &number1, &number2) != EOF)
    {
        printf("%.0Lf\n", (factorial(number1)) + (factorial(number2)));
    }    
    return 0;
}

long double factorial(long double num)
{
    if (num == 0)
        return 1.0;
    else
        return num * factorial(num - 1);
}
