#include <stdio.h>

int main()
{
    int x, cont=0;
    scanf("%d", &x);
    while (cont != x)
    {
        cont += 1;
        if (cont % 2 != 0)
            printf("%d\n", cont);
    }
    return 0;
}
