#include <stdio.h>

int main()
{
    int numSequencia, cont, caso, i, j;
    caso = 1;
    while (scanf("%d", &numSequencia) != EOF)
    {
        if (numSequencia == 0)
        {
            printf("Caso %d: 1 numero\n", caso);
            printf("0\n");
        }
        else if (numSequencia == 1)
        {
            printf("Caso %d: 2 numeros\n", caso);
            printf("0 1\n");
        }
        else
        {
            cont = 1;
            for (i=1; i <= numSequencia; i++)
            {
                for (j=i; j != 0; j--)
                {
                    cont += 1;
                }
            }
            printf("Caso %d: %d numeros\n", caso, cont);
            printf("0 ");
            for (i=1; i <= numSequencia; i++)
            {
                for (j=i; j != 0; j--)
                {
                    if ((j == 1) && (i == numSequencia))
                        break;
                    printf("%d ", i);
                }
            }
            printf("%d\n", numSequencia);
        }
        printf("\n");
        caso += 1;
    }
    return 0;
}
