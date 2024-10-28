#include<stdio.h>

int main()
{
    int rounds;
    scanf("%d", &rounds);
    while (rounds != 0)
    {
        int p1=0, p2=0;
        while (rounds != 0)
        {
            int n1, n2;
            scanf("%d %d", &n1, &n2);
            if (n1 > n2)
                p1 += 1;
            else if (n2 > n1)
                p2 += 1;    
            rounds -= 1;
        }
        printf("%d %d\n", p1, p2);
        scanf("%d", &rounds);
    }
    return 0;
}
