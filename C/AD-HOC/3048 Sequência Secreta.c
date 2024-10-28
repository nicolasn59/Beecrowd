#include <stdio.h>

int main()
{
    int len, marcados=1;
    scanf("%d", &len);
    int sequencia[len];
    for (int i=0; i < len; i++)
        scanf("%d", &sequencia[i]);
    for (int i=1; i < (len); i++)
    {
        if (sequencia[i-1] != sequencia[i])
            marcados += 1;
    }
    printf("%d\n", marcados);
    return 0;
}
