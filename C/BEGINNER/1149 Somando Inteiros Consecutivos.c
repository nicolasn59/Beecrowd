#include <stdio.h>

int main()
{
    int a, n=0, cont, soma=0;
    scanf("%d %d", &a, &n);
    while (n <= 0)
        scanf("%d", &n);
    cont = n;
    while (cont != 0)
    {
        cont -= 1;
        soma += (a + cont);
    }
    printf("%d\n", soma);
    return 0;
}
