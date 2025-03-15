#include <stdio.h>

int main()
{
    int testes, n, i, soma;
    scanf("%d", &testes);
    while (testes != 0)
    {
        soma = 0;
        scanf("%d", &n);
        for (i=1; i != n; i++)
        {
            if (n % i == 0)
                soma += i;
        }
        if (soma == n)
            printf("%d eh perfeito\n", n);
        else
            printf("%d nao eh perfeito\n", n);
        testes -= 1;
    }
    return 0;
}
