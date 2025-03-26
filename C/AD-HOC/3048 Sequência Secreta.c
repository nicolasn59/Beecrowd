#include <stdio.h>

int main()
{
    int len, marked = 1;
    scanf("%d", &len);
    int sequence[len];
    for (int i = 0; i < len; i++)
        scanf("%d", &sequence[i]);
    for (int i = 1; i < (len); i++)
    {
        if (sequence[i - 1] != sequence[i])
            marked += 1;
    }
    printf("%d\n", marked);
    return 0;
}