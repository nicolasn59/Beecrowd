#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int a, b, c, maiorAB;
    scanf("%d %d %d", &a, &b, &c);
    maiorAB = (a+b+abs(a-b))/2;
    printf("%d eh o maior\n", ((maiorAB+c+abs(maiorAB-c))/2));
    return 0;
}
