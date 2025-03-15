#include <stdio.h>
int main()
{
    int opcao, alcool=0, gasolina=0, diesel=0, fim=0;
    while (fim != 4)
    {
        scanf("%d", &opcao);
        if (opcao == 1)
            alcool += 1;
        else if (opcao == 2)
            gasolina += 1;
        else if (opcao == 3)
            diesel += 1;
        else if (opcao == 4)
            fim = 4; 
    }
    printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\n", alcool);
    printf("Gasolina: %d\n", gasolina);
    printf("Diesel: %d\n", diesel);
    return 0;
}
