#include <stdio.h>

int main()
{
    char digitoFalho[2], numOriginal[150];
    int finalOriginal, i, j;
    scanf("%s ", digitoFalho);
    fgets(numOriginal, 103, stdin);
    while (digitoFalho[0] != '0' || numOriginal[0] != '0')
    {
        char numContrato[150] = {};
        // TAMANHO DO VETOR
        finalOriginal = 0;
        while (numOriginal[finalOriginal] != '\0' && numOriginal[finalOriginal] != '\n')
            finalOriginal += 1;
        // REMOVER DÍGITOS FALHOS
        i = j = 0;
        while (i != finalOriginal)
        {
            if (numOriginal[i] != digitoFalho[0])
            {
                numContrato[j] = numOriginal[i];
                j += 1;
            }
            i += 1;
        }
        numContrato[finalOriginal] = '\0';
        // Verificar início e fim
        int confirmar, finalContrato;
        finalContrato = j;
        confirmar = 0;
        if (numContrato[0] == '0' && numContrato[finalContrato-1] == '0') // FICAR DE OLHO
        {
            i = 0;
            while (i != finalContrato)
            {
                if (numContrato[i] == '0')
                    confirmar += 1;
                i += 1;    
            }
        }
        if (confirmar == j || j == 0)
            {
                printf("0\n");
            }
        else
        {   

            if (numContrato[0] == '0')
            {
                i = 0;
                while (numContrato[i] == '0')
                {
                    i += 1;
                }
                for (j=i; numContrato[j] != '\0'; j++)
                {
                    printf("%c", numContrato[j]);
                }
                printf("\n");
            }
            else
                printf("%s\n", numContrato);
        }
        // char digitoFalho[2] = {}, numOriginal[150] = {};
        scanf("%s ", digitoFalho);
        fgets(numOriginal, 103, stdin);
    }
    return 0;
}
