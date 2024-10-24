#include <stdio.h>

int main()
{
    int numPerguntas, resposta;
    scanf("%d", &numPerguntas);
    for (int i=1; i <= numPerguntas; i++)
    {
        scanf("%d", &resposta);
        printf("resposta %d: %d\n", i, resposta);
    }
    return 0;
}