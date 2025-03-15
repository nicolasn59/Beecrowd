#include <stdio.h>
int main()
{
    int testes, x, y, somatorio, i, j, cont;
    scanf("%d", &testes);
    somatorio = 0;
    for (i=1; testes !=0; i++)
    {
        scanf("%d %d", &x, &y);
        if (x % 2 == 0)
        {
            cont = (x+1);
            for (j=1; y != 0;j+=2)
            {
                somatorio += cont;
                cont += 2;
                y -= 1;
            }
        }
        else
        {
            cont = x;
            for (j=1; y != 0;j+=2)
            {
                somatorio += cont;
                cont += 2;
                y -= 1;
            }
        }
        testes -= 1;
        printf("%d\n", somatorio);
        somatorio = 0;
    }
    return 0;
}
