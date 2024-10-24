# include <stdio.h>

int main()
{
    int tamanho, cont, i, sequencia;
    scanf("%d", &tamanho);
    cont = 0;
    long long int escada[tamanho];
    for (i=0; i != tamanho; i++)
    {
        scanf("%lld", &escada[i]);
        if (i == 1)
        {
            sequencia = (escada[i-1] - escada[i]);
            cont += 1;
        }
        else if (i > 1)
        {
            if ((escada[i-1] - escada[i]) != sequencia)
            {
                cont += 1;
                sequencia = (escada[i-1] - escada[i]);
            }
        }
    }
    if (cont == 0)
        printf("%d\n", ++cont);
    else
        printf("%d\n", cont);
    return 0;
}
