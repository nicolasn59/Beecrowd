#include <stdio.h>

int main()
{
    int numDeLesmas;
    while (scanf("%d", &numDeLesmas) != EOF)
    {
        int velocidadeDasLemas[numDeLesmas], cont;
        cont = 0;
        while (cont != numDeLesmas)
            {
                scanf("%d", &velocidadeDasLemas[cont]);
                cont += 1;
            }
        int maisVeloz;
        cont = 1;
        maisVeloz = velocidadeDasLemas[0];
        while (cont != numDeLesmas)
        {
            if (velocidadeDasLemas[cont] > maisVeloz)
                maisVeloz = velocidadeDasLemas[cont];
            cont += 1;
        }
        if (maisVeloz < 10)
            printf("1\n");
        else if (maisVeloz >= 10 && maisVeloz < 20)
            printf("2\n");
        else
            printf("3\n");        
    }
    return 0;
}
