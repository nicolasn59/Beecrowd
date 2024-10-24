#include <stdio.h>

int main(int argc, char const *argv[])
{
    double time, speed;
    scanf("%lf", &time);
    scanf("%lf", &speed);
    printf("%.3lf\n", ((speed*time)/12));
    return 0;
}
