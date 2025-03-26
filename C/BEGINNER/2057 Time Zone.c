#include <stdio.h>

void calculateArrival(int departure, int travelTime, int timeZone);

int main() {
    int departure, travelTime, timeZone;
    scanf("%d %d %d", &departure, &travelTime, &timeZone);
    calculateArrival(departure, travelTime, timeZone);
    return 0;
}

void calculateArrival(int departure, int travelTime, int timeZone)
{
    if ((departure + travelTime + timeZone) >= 24)
        printf("%d\n", ((departure + travelTime + timeZone) - 24));
    else if ((departure + travelTime + timeZone) < 0)
        printf("%d\n", ((departure + travelTime + timeZone) + 24));
    else
        printf("%d\n", (departure + travelTime + timeZone));
}
