#include<stdio.h>

int factorial(int n);

int main()
{
    int num;
    scanf("%d", &num);
    while (num != 0)
    {
        int sum = 0;
        if (num <= 9)
        {
            sum += (num * factorial(1));
        }
        else if (num <= 99)
        {
            sum += ((num / 10) * factorial(2)) + ((num % 10) * factorial(1));
        }
        else if (num <= 999)
        {
            sum += ((num / 100) * factorial(3)) + (((num / 10) % 10) * factorial(2)) + ((num % 10) * factorial(1));
        }
        else if (num <= 9999)
        {
            sum += (((num / 1000)) * factorial(4)) + (((num / 100) % 10) * factorial(3)) + (((num / 10) % 10) * factorial(2)) + ((num % 10) + factorial(1));
        }
        else
        {
            sum += ((num / 10000) * factorial(5) + (((num / 1000) % 10) * factorial(4)) + (((num / 100) % 10) * factorial(3)) + (((num / 10) % 10) * factorial(2)) + ((num % 10) * factorial(1)));
        }
        printf("%d\n", sum);
        scanf("%d", &num);
    }
    return 0;
}

int factorial(int n)
{
    if (n == 1)
        return 1;
    else
        return (n * factorial(n - 1));
}
