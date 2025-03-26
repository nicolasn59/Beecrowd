#include <math.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    double pi, volume;
    int radius;
    pi = 3.14159;
    scanf("%d", &radius);
    volume = (4 * pi * pow(radius, 3)) / 3;
    printf("VOLUME = %.3lf\n", volume);
    return 0;
}
