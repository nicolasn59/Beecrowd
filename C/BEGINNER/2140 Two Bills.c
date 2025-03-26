#include <stdio.h>

int main()
{
    int value, payment;
    scanf("%d %d", &value, &payment);
    while ((value != 0) || (payment != 0))
    {
        int change;
        change = payment - value;
        for (int i = 0; i < 2; i++)
        {
            if (change >= 100)
                change -= 100;
            else if (change >= 50)
                change -= 50;
            else if (change >= 20)
                change -= 20;
            else if (change >= 10)
                change -= 10;
            else if (change >= 5)
                change -= 5;
            else if (change >= 2)
                change -= 2;
            else
                change -= 1;
        }
        if (change == 0)
            printf("possible\n");
        else
            printf("impossible\n");
        scanf("%d %d", &value, &payment);
    }
    return 0;
}
