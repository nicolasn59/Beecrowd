#include <stdio.h>

int main(int argc, char const *argv[])
{
    int x, y, z, maior, medio, menor;
    scanf("%d %d %d", &x, &y, &z);

    if (x > y && x > z)
    {
        maior = x;
        if (y > z)
        {
            medio = y;
            menor = z;
        }
        else
        {
            medio = z;
            menor = y;
        }
    }
    else if (y > x && y > z)
    {
        maior = y;
        if (x > z)
        {
            medio = x;
            menor = z;
        }
        else 
        {
            medio = z;
            menor = x;
        }
    }
    else
    {
        maior = z;
        if (x > y)
        {
            medio = x;
            menor = y;
        }
        else
        {
            medio = y;
            menor = x;
        }
    }

    printf("%d\n", menor);
    printf("%d\n", medio);
    printf("%d\n", maior);
    printf("\n");
    printf("%d\n", x);
    printf("%d\n", y);
    printf("%d\n", z);
    return 0;
}
