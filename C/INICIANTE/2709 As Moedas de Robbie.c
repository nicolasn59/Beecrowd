#include <stdio.h>

void verificarPrimo(int sum)
{
    int cont=0;
    for (int i=2; i <= sum; i++)
    {
        if (sum % i == 0)
            cont += 1;
    }
    if (cont == 1)
        printf("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");
    else
        printf("Bad boy! I’ll hit you.\n");
}

int main()
{
    int quantidadeDeMoedas, salto;
    
    while (scanf("%d", &quantidadeDeMoedas) != EOF)
    {    
        int poteDeMoedas[quantidadeDeMoedas];
        for (int i=(quantidadeDeMoedas-1); i >= 0; i--)
        {
            scanf("%d", &poteDeMoedas[i]);
        }
        scanf("%d", &salto);
        int soma=0;
        for (int i=0; i < quantidadeDeMoedas; i+=salto)
        {
            soma += poteDeMoedas[i];
        }
        verificarPrimo(soma);
    }
    return 0;
}
