#include <stdio.h>

int main()
{
    unsigned long long int numSides, sideLength;
    scanf("%llu %llu", &numSides, &sideLength);
    printf("%llu\n", (numSides * sideLength));
    return 0;
}