#include <stdio.h>
#include <string.h>

void producaoDePresentes(int numeroDeElfos);

int main()
{
    int numeroDeElfos;
    scanf("%d", &numeroDeElfos);
    producaoDePresentes(numeroDeElfos);
    return 0;
}

void producaoDePresentes(int numElfos)
{
    char nome[100], profissao[100];
    int tempoDeTrabalho, somaBonecos=0, somaArquitetos=0, somaMusicos=0, somaDesenhistas=0;
    for (int i=0; i < numElfos; i++)
    {
        scanf("%s %s %d", nome, profissao, &tempoDeTrabalho);
        if (strcmp(profissao, "bonecos") == 0)
            somaBonecos += tempoDeTrabalho;
        else if (strcmp(profissao, "arquitetos") == 0)
            somaArquitetos += tempoDeTrabalho;
        else if (strcmp(profissao, "musicos") == 0)
            somaMusicos += tempoDeTrabalho;
        else
            somaDesenhistas += tempoDeTrabalho;
    }
    printf("%d\n", ((somaBonecos/8) + (somaArquitetos/4) + (somaMusicos/6) + (somaDesenhistas/12)));
}
