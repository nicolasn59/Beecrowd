#include <stdio.h>

int main()
{
    int n, cont=1;
    scanf("%d", &n);
    while (n != 0)
    {
        while (cont < (n+1))
        {
            if (cont != n)
                printf("%d ", cont);
            else
                printf("%d\n", cont);
            cont += 1;
        }
        scanf("%d", &n);
        cont = 1;
    }
    return 0;
}
