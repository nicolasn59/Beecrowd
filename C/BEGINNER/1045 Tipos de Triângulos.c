#include <stdio.h>

int main(int argc, char const *argv[])
{
    double a, b, c, cont;
    scanf("%lf %lf %lf", &a, &b, &c);
   
    if (b > a && b > c)
    {
        cont = a;
        a = b;
        b = cont;
    }
    else if (c > a && c > b)
    {
        cont = a;
        a = c;
        c = cont;
    }
    if (c > b)
    {
        cont = b;
        b = c;
        c = cont;
    }
    // printf("%lf %lf %lf\n", a, b, c);
    if (a >= (b+c))
    {
        printf("NAO FORMA TRIANGULO\n");
    }
    else
    {
        if ((a*a) == ((b*b)+(c*c)))
                printf("TRIANGULO RETANGULO\n");
            if ((a*a) > ((b*b)+(c*c)))
                printf("TRIANGULO OBTUSANGULO\n");
            if ((a*a) < ((b*b)+(c*c)))
                printf("TRIANGULO ACUTANGULO\n");
            if (a == b && a == c && b == c)
                printf("TRIANGULO EQUILATERO\n");
            else if (a == b || a == c || b == c)
                printf("TRIANGULO ISOSCELES\n");
    }
    return 0;
}
