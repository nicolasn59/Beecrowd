#include <stdio.h>

int main()
{
    int sabor, resposta, cont=0;
    scanf("%d", &sabor);
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &resposta);
        if (resposta == sabor)
            cont += 1;
    }
    printf("%d\n", cont);
    return 0;
}
