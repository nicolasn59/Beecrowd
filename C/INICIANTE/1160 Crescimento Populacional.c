#include <stdio.h>
int main()
{
    int testes, PA, PB, contador;
    double GA, GB;
    scanf("%d", &testes);
    while (testes != 0)
    {
        contador = 0;
        scanf("%d %d %lf %lf", &PA, &PB, &GA, &GB);
            while (PA <= PB)
            {
                PA += (PA * (GA/100.0));
                PB += (PB * (GB/100.0));
                contador += 1;
                if (contador > 100)
                    PA = (PB + 1);
            }
        if (contador > 100)
            printf("Mais de 1 seculo.\n");
        else
            printf("%d anos.\n", contador);
        testes -= 1;
    }
    return 0;
}
