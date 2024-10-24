#include <stdio.h>
#include <string.h>

int main()
{
    char estrutura[13], tipo[9], alimentacao[11];
    scanf("%s", estrutura);
    scanf("%s", tipo);
    scanf("%s", alimentacao);
    if (strcmp(estrutura, "vertebrado") == 0)
    {
        if (strcmp(tipo, "ave") == 0)
        {
            if (strcmp(alimentacao, "carnivoro") == 0)
                printf("aguia\n");
            else
                printf("pomba\n");
        }
        else
        {
            if (strcmp(alimentacao, "onivoro") == 0)
                printf("homem\n");
            else
                printf("vaca\n");
        }   
    }
    else
    {
        if (strcmp(tipo, "inseto") == 0)
        {
            if (strcmp(alimentacao, "hematofago") == 0)
                printf("pulga\n");
            else
                printf("lagarta\n");
        }
        else
        {
            if (strcmp(alimentacao, "hematofago") == 0)
                printf("sanguessuga\n");
            else
                printf("minhoca\n");
        }
    }
    return 0;
}
