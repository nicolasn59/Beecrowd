#include <stdio.h>

int main(){
    int distance;
    double fuel;
    scanf("%d", &distance);
    scanf("%lf", &fuel);
    printf("%.3lf km/l\n", (distance/fuel));
    return 0;
}
