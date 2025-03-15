#include <stdio.h>
double calcularAumento(double precoAnterior, double precoNovo)
{
    return (((precoNovo * 100.0)/precoAnterior)-100.0);
}

int main()
{
    double precoAntigo, precoNovo;
    scanf("%lf %lf", &precoAntigo, &precoNovo);
    printf("%.2lf%%\n", calcularAumento(precoAntigo, precoNovo));
    return 0;
}
