#include <stdio.h>

int main() {
    double value1, value2, value3;
    scanf("%lf", &value1);
    scanf("%lf", &value2);
    scanf("%lf", &value3);
    printf("MEDIA = %.1lf\n", ((value1*2 + value2*3 + value3*5)/10));
    return 0;
}
