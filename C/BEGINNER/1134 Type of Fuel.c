#include <stdio.h>
int main()
{
    int option, alcohol = 0, gasoline = 0, diesel = 0, end = 0;
    while (end != 4)
    {
        scanf("%d", &option);
        if (option == 1)
            alcohol += 1;
        else if (option == 2)
            gasoline += 1;
        else if (option == 3)
            diesel += 1;
        else if (option == 4)
            end = 4; 
    }
    printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\n", alcohol);
    printf("Gasolina: %d\n", gasoline);
    printf("Diesel: %d\n", diesel);
    return 0;
}