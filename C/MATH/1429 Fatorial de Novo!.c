#include<stdio.h>

int fat(int n);

int main()
{
    int num;
    scanf("%d", &num);
    while (num != 0)
    {
        int soma=0;
        if (num <= 9)
        {
            soma += (num * fat(1));
        }
        else if (num <= 99)
        {
            soma += ((num/10)*fat(2)) + ((num%10)*fat(1));
        }
        else if (num <= 999)
        {
            soma += ((num/100)*fat(3)) + (((num/10)%10)*fat(2)) + ((num%10)*fat(1));
        }
        else if (num <= 9999)
        {
            soma += (((num/1000))*fat(4)) + (((num/100)%10)*fat(3)) + (((num/10)%10)*fat(2)) + ((num%10)+fat(1));
        }
        else
        {
            soma += ((num/10000)*fat(5) + (((num/1000)%10)*fat(4)) + (((num/100)%10)*fat(3)) + (((num/10)%10)*fat(2)) + ((num%10)*fat(1)));
        }
        printf("%d\n", soma);
        scanf("%d", &num);
    }
    return 0;
}

int fat(int n)
{
    if (n == 1)
        return 1;
    else
        return (n * fat(n-1));
}
