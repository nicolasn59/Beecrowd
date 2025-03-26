#include <stdio.h>

int main()
{
    int vectorSize;
    scanf("%d", &vectorSize);
    int vector[vectorSize], i, min, position;
    for (i = 0; i < vectorSize; i++)
        scanf("%d", &vector[i]);
    min = vector[0];
    position = 0;
    for (i = 1; i < vectorSize; i++)
    {
        if (vector[i] < min)
        {
            min = vector[i];
            position = i;
        }
    }
    printf("Menor valor: %d\n", min);
    printf("Posicao: %d\n", position);
    return 0;
}