#include <stdio.h>

void verificarMultiplos(int lenLista, int list[]);

int main()
{
    int len;
    scanf("%d", &len);
    int lista[len];
    for (int i=0; i < len; i++)
    {
        scanf("%d", &lista[i]);
    }
    verificarMultiplos(len, lista);
    return 0;
}

void verificarMultiplos(int lenLista, int list[])
{
    int multiplosDeDois=0, multiplosDeTres=0, multiplosDeQuatro=0, multiplosDeCinco=0;
    for (int i=0; i < lenLista; i++)
    {
        if ((list[i] % 2) == 0)
            multiplosDeDois += 1;
        if ((list[i] % 3) == 0)
            multiplosDeTres += 1;
        if ((list[i] % 4) == 0)
            multiplosDeQuatro += 1;
        if ((list[i] % 5) == 0)
            multiplosDeCinco += 1;
    }
    printf("%d Multiplo(s) de 2\n", multiplosDeDois);
    printf("%d Multiplo(s) de 3\n", multiplosDeTres);
    printf("%d Multiplo(s) de 4\n", multiplosDeQuatro);
    printf("%d Multiplo(s) de 5\n", multiplosDeCinco);
}
#include <stdio.h>

void verificarMultiplos(int lenLista, int list[]);

int main()
{
    int len;
    scanf("%d", &len);
    int lista[len];
    for (int i=0; i < len; i++)
    {
        scanf("%d", &lista[i]);
    }
    verificarMultiplos(len, lista);
    return 0;
}

void verificarMultiplos(int lenLista, int list[])
{
    int multiplosDeDois=0, multiplosDeTres=0, multiplosDeQuatro=0, multiplosDeCinco=0;
    for (int i=0; i < lenLista; i++)
    {
        if ((list[i] % 2) == 0)
            multiplosDeDois += 1;
        if ((list[i] % 3) == 0)
            multiplosDeTres += 1;
        if ((list[i] % 4) == 0)
            multiplosDeQuatro += 1;
        if ((list[i] % 5) == 0)
            multiplosDeCinco += 1;
    }
    printf("%d Multiplo(s) de 2\n", multiplosDeDois);
    printf("%d Multiplo(s) de 3\n", multiplosDeTres);
    printf("%d Multiplo(s) de 4\n", multiplosDeQuatro);
    printf("%d Multiplo(s) de 5\n", multiplosDeCinco);
}
