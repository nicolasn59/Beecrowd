#include <stdio.h>

int main() {
    int desiredPressure, tirePressure;
    scanf("%d %d", &desiredPressure, &tirePressure);
    printf("%d\n", (desiredPressure - tirePressure));
    return 0;
}