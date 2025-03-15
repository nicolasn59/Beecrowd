#include<stdio.h>

long double fat(long double num);

int main()
{
    long double number1, number2;
    while (scanf("%Lf %Lf", &number1, &number2) != EOF)
    {
        printf("%.0Lf\n", (fat(number1)) + (fat(number2)));
    }    
    return 0;
}

long double fat(long double num)
{
    if (num == 0)
        return 1.0;
    else
        return num * fat(num-1);
}
