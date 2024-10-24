#include <stdio.h>
#include <math.h>

int main()
{
    double valor, parcelas;
    scanf("%lf", &valor);
    scanf("%lf", &parcelas);
    int cont=0;
    for (int i=0; i < (int) parcelas; i++)
    {
        if (cont < (fmod(valor, parcelas)))
        {
            printf("%0.lf\n", ceil(valor/parcelas));
            cont += 1;
        }
        else
            printf("%0.lf\n", trunc(valor/parcelas));
    }
    return 0;
}
