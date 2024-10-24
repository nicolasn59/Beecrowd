#include <stdio.h>

int main()
{
    int v1, v2, menor, maior, cont, soma=0;
    scanf("%d %d", &v1, &v2);
    while (v1 > 0 && v2 > 0)
    {
        if (v1 > v2)
        {
            maior = v1;
            menor = v2;
        }
        else
        {
            maior = v2;
            menor = v1;
        }
        cont = menor;
        while (cont != (maior+1))
        {
            printf("%d ", cont);
            soma += cont;
            cont += 1;
        }
        printf("Sum=%d\n", soma);
        soma = 0;
        scanf("%d %d", &v1, &v2);
    }
    return 0;
}
