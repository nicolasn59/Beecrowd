#include <stdio.h>
#include <string.h>

int main()
{
    int testes, numJ1, numJ2;
    char nomeJ1[101], escolhaJ1[6], nomeJ2[101], escolhaJ2[6];
    scanf("%d", &testes);
    for (int i=0; i < testes; i++)
    {
        scanf("%s\n %s\n %s\n %s\n", nomeJ1, escolhaJ1, nomeJ2, escolhaJ2);
        scanf("%d %d", &numJ1, &numJ2);
        if ((numJ1 + numJ2) % 2 == 0)
        {
            if (strcmp(escolhaJ1, "PAR") == 0)
                printf("%s\n", nomeJ1);
            else
                printf("%s\n", nomeJ2);
        }
        else
        {
            if (strcmp(escolhaJ1, "IMPAR") == 0)
                printf("%s\n", nomeJ1);
            else
                printf("%s\n", nomeJ2);
        } 
    }
    return 0;
}