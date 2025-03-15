#include <stdio.h>

int main()
{
    int tamanho;
    scanf("%d", &tamanho);
    if (tamanho % 2 == 0)
        printf("%d casas brancas e %d casas pretas\n", (tamanho*(tamanho/2)), (tamanho*(tamanho/2)));
    else
        printf("%d casas brancas e %d casas pretas\n", (((tamanho*tamanho)/2)+1), ((tamanho*tamanho)/2));
    return 0;
}
