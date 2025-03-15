#include <stdio.h>
#include <string.h>

void loteria();

int main()
{
    loteria();
    return 0;
}

void loteria()
{
    char corvo[10];
    int soma=0, contarGritos=0;
    while (contarGritos != 3)
    {
        fgets(corvo, sizeof(corvo), stdin);
        if (strcmp(corvo, "caw caw\n") == 0)
        {   
            printf("%d\n", soma);
            soma = 0;
            contarGritos += 1;
        }
        else if (strcmp(corvo, "--*\n") == 0)
        {
            soma += 1;
        }
        else if (strcmp(corvo, "-*-\n") == 0)
        {
            soma += 2;
        }
        else if (strcmp(corvo, "-**\n") == 0)
        {
            soma += 3;
        }
        else if (strcmp(corvo, "*--\n") == 0)
        {
            soma += 4;
        }
        else if (strcmp(corvo, "*-*\n") == 0)
        {
            soma += 5;
        }
        else if (strcmp(corvo, "**-\n") == 0)
        {
            soma += 6;
        }
        else
        {
            soma += 7;
        }
    }
    return;
}
