#include <stdio.h>
double calculateIncrease(double oldPrice, double newPrice)
{
    return (((newPrice * 100.0) / oldPrice) - 100.0);
}

int main()
{
    double oldPrice, newPrice;
    scanf("%lf %lf", &oldPrice, &newPrice);
    printf("%.2lf%%\n", calculateIncrease(oldPrice, newPrice));
    return 0;
}
