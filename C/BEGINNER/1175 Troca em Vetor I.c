#include <stdio.h>
int main()
{
    int num, i, cont, vetorOriginal[20], vetorModificado[20];
    for (i=0; i<20; i++)
    {
        scanf("%d", &num);
        vetorOriginal[i] = num;
    }
    cont = 19;
    for (i=0; i<10; i++)
    {
        vetorModificado[i] = vetorOriginal[cont];
        vetorModificado[cont] = vetorOriginal[i];
        cont -= 1;
    }
    for (i=0; i<20; i++)
        printf("N[%d] = %d\n", i, vetorModificado[i]);
    return 0;
}
