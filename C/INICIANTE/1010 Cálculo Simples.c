#include <stdio.h>

int main(int argc, char const *argv[])
{
    int numDePecas1, numDePecas2, codDaPeca1, codDaPeca2;
    float valorDaPeca1, valorDaPeca2;
    scanf("%d %d %f", &codDaPeca1, &numDePecas1, &valorDaPeca1);
    scanf("%d %d %f", &codDaPeca2, &numDePecas2, &valorDaPeca2);
    printf("VALOR A PAGAR: R$ %.2f\n", (numDePecas1*valorDaPeca1 + numDePecas2*valorDaPeca2));
    return 0;
}
