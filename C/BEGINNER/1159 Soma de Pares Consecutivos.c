#include <stdio.h>

int main()
{
    int x, somatorio, repeticao, cont;
    scanf("%d", &x);
    while (x != 0)
    {
        somatorio = 0;
        repeticao = 5;
        if (x % 2 == 0)
            {
                cont = x;
                while (repeticao != 0)
                {
                    somatorio += cont;
                    cont += 2;
                    repeticao -= 1;
                }
            }
        else
        {
            cont = (x + 1);
            while (repeticao != 0)
            {
                somatorio += cont;
                cont += 2;
                repeticao -= 1;
            }
        }
        printf("%d\n", somatorio);
        scanf("%d", &x);
    }
    return 0;
}
