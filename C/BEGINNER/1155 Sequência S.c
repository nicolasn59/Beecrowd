#include <stdio.h>

int main()
{
    double s, cont;
    s = 0.0;
    cont = 1.0;
    while (cont <= 100.0)
    {
        s += (1/cont);
        cont += 1.0;
    }
    printf("%.2lf\n", s);
    return 0;
}
