#include <stdio.h>

int main()
{
    int x, y, cont, soma=0;
    scanf("%d", &x);
    scanf("%d", &y);
    if (x > y)
    {
        cont = (y + 1);
        while (cont != x)
        {
            if (cont % 2 != 0)
                soma += cont;
            cont += 1;

        }
    }
    else
    {
        cont = (x + 1);
        while (cont != y)
        {
            if (cont % 2 != 0)
                soma += cont;
            cont += 1;
        }
    }
    printf("%d\n", soma);
    return 0;
}
