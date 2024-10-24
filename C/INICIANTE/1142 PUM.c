#include <stdio.h>

int main()
{
    int num, primeiro=1, segundo=2, terceiro=3;
    scanf("%d", &num);
    while (num != 0)
    {
        printf("%d %d %d PUM\n", primeiro, segundo, terceiro);
        primeiro += 4;
        segundo += 4;
        terceiro += 4;
        num -= 1;
    }
    return 0;
}
