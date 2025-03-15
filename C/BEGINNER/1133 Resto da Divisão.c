#include <stdio.h>

int main()
{
    int x, y, maior, menor, cont;
    scanf("%d", &x);
    scanf("%d", &y);

    if (x > y)
    {
        maior = x;
        menor = y;
    }
    else
    {
        maior = y;
        menor = x;
    }
    cont = (menor + 1);

    while (cont != maior)
    {
        if (cont % 5 == 2 || cont % 5 == 3)
            printf("%d\n", cont);
        cont += 1;
    }
    return 0;
}
