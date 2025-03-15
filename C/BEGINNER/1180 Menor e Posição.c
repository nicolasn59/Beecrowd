#include <stdio.h>

int main()
{
    int tamanhoDoVetor;
    scanf("%d", &tamanhoDoVetor);
    int vetor[tamanhoDoVetor], i, menor, posicao;
    for (i=0; i<tamanhoDoVetor; i++)
        scanf("%d", &vetor[i]);
    menor = vetor[0];
    posicao = 0;
    for (i=1; i<tamanhoDoVetor; i++)
    {
        if (vetor[i] < menor)
        {
            menor = vetor[i];
            posicao = i;
        }
    }
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);
    return 0;
}
