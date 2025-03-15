#include <stdio.h>

int main()
{
    int x, z, soma=1, cont;
    scanf("%d", &x);
    scanf("%d", &z);
    while (z <= x)
        scanf("%d", &z);
    cont = (x+1);
    while (x <= z)
    {
        x += cont;
        soma += 1;
        cont += 1;
    }
    printf("%d\n", soma);
    return 0;
}
