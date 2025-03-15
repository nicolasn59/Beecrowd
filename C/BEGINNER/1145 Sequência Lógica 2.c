#include <stdio.h>

int main()
{
    int sequencia, final, cont=1, quebraLinha, pararLoop;
    scanf("%d %d", &sequencia, &final);
    pararLoop = final;
    quebraLinha = sequencia;
    while (pararLoop != 0)
    {   
        if (quebraLinha == 1)
            printf("%d\n", cont);
        else
            printf("%d ", cont);
        quebraLinha -= 1;
        cont += 1;
        pararLoop -= 1;
        if (quebraLinha == 0)
            quebraLinha = sequencia;
    }
    return 0;
}
