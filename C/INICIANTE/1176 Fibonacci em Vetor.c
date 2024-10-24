#include <stdio.h>

int main()
{
    unsigned long long vetor[60], tests, num, valAnterior, valAnteAnterior, valAtual, cont;;

    scanf("%llu", &tests);
    while (tests != 0)
    {
        vetor[0] = 0;
        vetor[1] = 1;
        valAnteAnterior = 0;
        valAnterior = 1;
        scanf("%llu", &num);
        cont = 2;
        if (num > 1)
        {
            while (cont != (num+1))
            {
                valAtual = 0;
                valAtual = valAnteAnterior + valAnterior;
                vetor[cont] = valAtual;
                valAnteAnterior = valAnterior;
                valAnterior = valAtual;
                cont += 1;
            }
        }
        printf("Fib(%llu) = %llu\n", num, vetor[num]);
        tests -= 1;
    }
    return 0;
}
