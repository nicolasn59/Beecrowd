#include <stdio.h>

int main()
{
    int a, n=0, cont, sum=0;
    scanf("%d %d", &a, &n);
    while (n <= 0)
        scanf("%d", &n);
    cont = n;
    while (cont != 0)
    {
        cont -= 1;
        sum += (a + cont);
    }
    printf("%d\n", sum);
    return 0;
}
