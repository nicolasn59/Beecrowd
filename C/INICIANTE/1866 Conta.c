#include <stdio.h>

void resultadoDaSoma(int qtdTermos)
{
    int soma=0;
    for (int i=0; i < qtdTermos; i++)
    {
        if (soma == 0)
            soma += 1;
        else
            soma -= 1;
    }
    printf("%d\n", soma);
}

int main()
{
    int qtdTestes, termos;
    scanf("%d", &qtdTestes);
    for (int i=0; i < qtdTestes; i++)
    {
        scanf("%d", &termos);
        resultadoDaSoma(termos);
    }
    return 0;
}
