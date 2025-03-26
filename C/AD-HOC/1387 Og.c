#include <stdio.h>

int main()
{
    int sons, daughters;
    scanf("%d %d", &sons, &daughters);
    while ((sons != 0) && (daughters != 0))
    {
        printf("%d\n", (sons + daughters));
        scanf("%d %d", &sons, &daughters);
    }
    return 0;
}
