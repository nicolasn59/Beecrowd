#include <stdio.h>

int somaDosQuadrados(int num);

int main()
{
    int number;
    while (scanf("%d", &number) != EOF)
    {
        if (number < 0)
            printf("NO\n");
        else
            somaDosQuadrados(number);
    }
    return 0;
}

int somaDosQuadrados(int num)
{
    int n1=0, n2=0, cont=0, true=1;
    while (true == 1)
    {
        if (((n1*n1) + (n2*n2)) == num)
        {
            printf("YES\n");
            return 1;
        }
        else if ((((n1*n1) + (n2*n2)) > num) && (cont == 1))
        {
            n1 -= 1;
        }
        else
        {
            if (((n1*n1) < num) && (cont == 0))
                n1 += 2;
            else if (((n1*n1) > num) && (cont == 0))
            {
                n1 -= 1;
                cont = 1;
            }
            else
                n2 += 1;
                
        }
        if ((n1 == 0) && (cont == 1))
        {
            printf("NO\n");
            return 0;
        }
    }
    return 0;
}
