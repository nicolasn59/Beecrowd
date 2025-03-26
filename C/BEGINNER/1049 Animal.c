#include <stdio.h>
#include <string.h>

int main()
{
    char structure[13], type[9], diet[11];
    scanf("%s", structure);
    scanf("%s", type);
    scanf("%s", diet);
    if (strcmp(structure, "vertebrado") == 0)
    {
        if (strcmp(type, "ave") == 0)
        {
            if (strcmp(diet, "carnivoro") == 0)
                printf("aguia\n");
            else
                printf("pomba\n");
        }
        else
        {
            if (strcmp(diet, "onivoro") == 0)
                printf("homem\n");
            else
                printf("vaca\n");
        }   
    }
    else
    {
        if (strcmp(type, "inseto") == 0)
        {
            if (strcmp(diet, "hematofago") == 0)
                printf("pulga\n");
            else
                printf("lagarta\n");
        }
        else
        {
            if (strcmp(diet, "hematofago") == 0)
                printf("sanguessuga\n");
            else
                printf("minhoca\n");
        }
    }
    return 0;
}
