#include <stdio.h>

int main()
{
    int x, y, cont, maior, menor, somaNaoDivisores=0;
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
    cont = menor;
    while (cont != (maior + 1))
    {
        if (cont % 13 != 0)
            somaNaoDivisores += cont;
        cont += 1;
    }
    printf("%d\n", somaNaoDivisores);
    return 0;
}
