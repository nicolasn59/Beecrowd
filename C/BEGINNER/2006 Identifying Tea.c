#include <stdio.h>

int main()
{
    int flavor, answer, count = 0;
    scanf("%d", &flavor);
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &answer);
        if (answer == flavor)
            count += 1;
    }
    printf("%d\n", count);
    return 0;
}
