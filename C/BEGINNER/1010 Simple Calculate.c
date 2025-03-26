#include <stdio.h>

int main(int argc, char const *argv[])
{
    int numParts1, numParts2, partCode1, partCode2;
    float partValue1, partValue2;
    scanf("%d %d %f", &partCode1, &numParts1, &partValue1);
    scanf("%d %d %f", &partCode2, &numParts2, &partValue2);
    printf("VALOR A PAGAR: R$ %.2f\n", (numParts1 * partValue1 + numParts2 * partValue2));
    return 0;
}