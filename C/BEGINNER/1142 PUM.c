#include <stdio.h>

int main()
{
    int num, first = 1, second = 2, third = 3;
    scanf("%d", &num);
    while (num != 0)
    {
        printf("%d %d %d PUM\n", first, second, third);
        first += 4;
        second += 4;
        third += 4;
        num -= 1;
    }
    return 0;
}