#include <stdio.h>

int main(int argc, char const *argv[])
{
    int qtdVals, valor;
    scanf("%d", &qtdVals);
    while (qtdVals != 0)
    {
        scanf("%d", &valor);
        if (valor == 0)
            printf("NULL\n");
        else if (valor % 2 == 0) // PAR
        {
            if (valor > 0) //PAR POSITIVO
                printf("EVEN POSITIVE\n");
            else if (valor < 0) // PAR NEGATIVO
                printf("EVEN NEGATIVE\n");
        }
        else if (valor % 2 != 0) // IMPAR
        {
            if (valor > 0) // IMPAR POSITIVO
                printf("ODD POSITIVE\n");
            else if (valor < 0) // IMPAR NEGATIVO
                printf("ODD NEGATIVE\n");
        }
        qtdVals -= 1;
    }
    return 0;
}
