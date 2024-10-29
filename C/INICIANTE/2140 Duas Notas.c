#include <stdio.h>

int main()
{
    int valor, pagamento;
    scanf("%d %d", &valor, &pagamento);
    while ((valor != 0) || (pagamento != 0))
    {
        int troco;
        troco = pagamento - valor;
        for (int i=0; i < 2; i++)
        {
            if (troco >= 100)
                troco -= 100;
            else if (troco >= 50)
                troco -= 50;
            else if (troco >= 20)
                troco -= 20;
            else if (troco >= 10)
                troco -= 10;
            else if (troco >= 5)
                troco -= 5;
            else if (troco >= 2)
                troco -= 2;
            else
                troco -= 1;
        }
        if (troco == 0)
            printf("possible\n");
        else
            printf("impossible\n");
        scanf("%d %d", &valor, &pagamento);
    }
    return 0;
}
