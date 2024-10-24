#include <stdio.h>
int main()
{
    int numDePessoas;
    scanf("%d", &numDePessoas);
    int possiveisExecutores[numDePessoas], cont, melhorEscolha, menor;
    cont = 0;
    while (cont != numDePessoas)
    {
        scanf("%d", &possiveisExecutores[cont]);
        cont += 1;
    }
    melhorEscolha = 1;
    menor = possiveisExecutores[0];
    cont = 1;
    while (cont != numDePessoas)
    {
        if (possiveisExecutores[cont] < menor)
        {
            menor = possiveisExecutores[cont];
            melhorEscolha = cont+1;
        }

        cont += 1;
    }
    printf("%d\n", melhorEscolha);
    return 0;
}
